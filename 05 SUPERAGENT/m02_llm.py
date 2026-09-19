"""M02 semantic distinction extractor adapter for SUPERAGENT MVP.

The adapter is source/task agnostic. It accepts EXTRACTION_RECORDS and asks an
OpenAI-compatible chat-completions endpoint to produce source-grounded
DISTINCTION_RECORDS. The orchestration kernel remains deterministic.
"""
from __future__ import annotations

import json
import os
import urllib.request
from typing import Any, Dict, List


M02_SYSTEM_PROMPT = """You are MACHINE-SOURCE-001 executing TASK M02 DISTINCTIONS.

Transform each supplied Extraction Record into one engineering distinction
derived only from that record.

Rules:
- Process each Extraction Record independently.
- Produce exactly one Distinction Record for each input Extraction Record.
- Preserve the source-grounded meaning; do not add external knowledge.
- A distinction must state what the source differentiates, separates, defines,
  requires, or makes operationally significant.
- Do not perform formulation, nomenclature, classification, passporting,
  relation-building, canonization, or synthesis across records.
- Do not merge records.
- Keep the link to the input extraction record.
- If a record is insufficient to support a reliable distinction, mark
  uncertainty as UNCERTAIN rather than inventing content.

For every output return:
- id: DIS-###
- extraction_id: input Extraction Record id
- distinction: concise source-grounded engineering distinction
- uncertainty: CLEAR or UNCERTAIN
- source_id

Return JSON only:
{"records":[...]}

Do not invent source locations or evidence.
"""


class M02LLMError(RuntimeError):
    pass


def _request_json(payload: Dict[str, Any], timeout: int = 120) -> Dict[str, Any]:
    api_key = os.environ.get("LLM_API_KEY")
    model = os.environ.get("LLM_MODEL")
    base_url = os.environ.get(
        "LLM_BASE_URL", "https://api.openai.com/v1"
    ).rstrip("/")

    if not api_key:
        raise M02LLMError("LLM_API_KEY is not set")
    if not model:
        raise M02LLMError("LLM_MODEL is not set")

    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    req = urllib.request.Request(
        f"{base_url}/chat/completions",
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as exc:
        raise M02LLMError(f"LLM request failed: {exc}") from exc


def extract_distinctions(extraction_input: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Execute semantic M02 against supplied EXTRACTION_RECORDS."""
    records = extraction_input.get("records", [])
    if not records:
        raise M02LLMError("EXTRACTION_RECORDS has no records")

    user_payload = {
        "source_id": extraction_input["source_id"],
        "records": records,
    }

    response = _request_json({
        "model": os.environ["LLM_MODEL"],
        "messages": [
            {"role": "system", "content": M02_SYSTEM_PROMPT},
            {
                "role": "user",
                "content": json.dumps(user_payload, ensure_ascii=False),
            },
        ],
    })

    try:
        content = response["choices"][0]["message"]["content"]
        parsed = json.loads(content)
        output_records = parsed["records"]
    except (KeyError, TypeError, json.JSONDecodeError) as exc:
        raise M02LLMError(f"Invalid M02 JSON response: {exc}") from exc

    if not isinstance(output_records, list):
        raise M02LLMError("M02 records must be a list")

    if len(output_records) != len(records):
        raise M02LLMError(
            f"M02 cardinality mismatch: {len(records)} input -> "
            f"{len(output_records)} output"
        )

    normalized: List[Dict[str, Any]] = []
    for i, record in enumerate(output_records, 1):
        required = {"extraction_id", "distinction", "uncertainty"}
        if not required.issubset(record):
            raise M02LLMError(
                f"M02 record {i} is missing required fields"
            )
        normalized.append({
            "id": f"DIS-{i:03d}",
            "extraction_id": record["extraction_id"],
            "distinction": record["distinction"],
            "uncertainty": record["uncertainty"],
            "source_id": extraction_input["source_id"],
        })

    expected_ids = [r["id"] for r in records]
    actual_ids = [r["extraction_id"] for r in normalized]
    if actual_ids != expected_ids:
        raise M02LLMError(
            "M02 extraction trace mismatch: output order/IDs do not match input"
        )

    return normalized
