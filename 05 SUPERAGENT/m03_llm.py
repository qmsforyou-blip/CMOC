"""M03 semantic formulation adapter for SUPERAGENT MVP.

The adapter is source/task agnostic. It accepts DISTINCTION_RECORDS and asks an
OpenAI-compatible chat-completions endpoint to produce three formulation levels
for each distinction. The orchestration kernel remains deterministic.
"""
from __future__ import annotations

import json
import os
import urllib.request
import ssl
from typing import Any, Dict, List


_TLS_CONTEXT = ssl.create_default_context()
_TLS_CONTEXT.minimum_version = ssl.TLSVersion.TLSv1_2
_TLS_CONTEXT.maximum_version = ssl.TLSVersion.TLSv1_2


M03_SYSTEM_PROMPT = """You are MACHINE-SOURCE-001 executing TASK M03 FORMULATIONS.

Transform each supplied Distinction Record into exactly three formulations:
INTUITIVE, ENGINEERING, and CANONICAL_FORMULATION.

Rules:
- Process each Distinction Record independently.
- Produce exactly three formulation records for each input Distinction Record.
- Preserve the distinction's source-grounded meaning.
- INTUITIVE: plain-language formulation, easy to understand.
- ENGINEERING: precise engineering formulation that makes the operational
  distinction explicit without adding external knowledge.
- CANONICAL_FORMULATION: concise stable formulation suitable as a candidate
  wording for CMOC, but do not canonize, classify, name, or relate it.
- Do not add external knowledge.
- Do not merge records.
- Do not perform nomenclature, classification, passporting, relation-building,
  canonization, or synthesis across records.
- Do not infer causal, logical, hierarchical, or justificatory links unless
  they are explicitly present in the input distinction.
- Do not replace, reinterpret, or alter source-grounded qualifiers, directions,
  temporal terms, quantities, modality, or other semantic parameters.
- Preserve such semantic parameters when reformulating.
- Do not turn adjacency or wording into a new relationship.
- Keep the link to the input distinction record.
- If a distinction is insufficient to support a reliable formulation, preserve
  its uncertainty rather than inventing content.

For every output return:
- id: FORM-###
- distinction_id: input Distinction Record id
- level: INTUITIVE, ENGINEERING, or CANONICAL_FORMULATION
- formulation
- uncertainty: CLEAR or UNCERTAIN
- source_id

Return JSON only:
{"records":[...]}

Output order must be: all three levels for DIS-001, then all three for DIS-002,
and so on. Do not invent source locations or evidence.
"""


class M03LLMError(RuntimeError):
    pass


def _request_json(payload: Dict[str, Any], timeout: int = 120) -> Dict[str, Any]:
    api_key = os.environ.get("LLM_API_KEY")
    model = os.environ.get("LLM_MODEL")
    base_url = os.environ.get(
        "LLM_BASE_URL", "https://api.openai.com/v1"
    ).rstrip("/")

    if not api_key:
        raise M03LLMError("LLM_API_KEY is not set")
    if not model:
        raise M03LLMError("LLM_MODEL is not set")

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
        with urllib.request.urlopen(req, context=_TLS_CONTEXT, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception as exc:
        raise M03LLMError(f"LLM request failed: {exc}") from exc


def formulate(distinction_input: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Execute semantic M03 against supplied DISTINCTION_RECORDS."""
    records = distinction_input.get("records", [])
    if not records:
        raise M03LLMError("DISTINCTION_RECORDS has no records")

    user_payload = {
        "source_id": distinction_input["source_id"],
        "records": records,
    }

    response = _request_json({
        "model": os.environ["LLM_MODEL"],
        "messages": [
            {"role": "system", "content": M03_SYSTEM_PROMPT},
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
        raise M03LLMError(f"Invalid M03 JSON response: {exc}") from exc

    if not isinstance(output_records, list):
        raise M03LLMError("M03 records must be a list")

    expected_count = len(records) * 3
    if len(output_records) != expected_count:
        raise M03LLMError(
            f"M03 cardinality mismatch: {len(records)} input -> "
            f"{len(output_records)} output; expected {expected_count}"
        )

    normalized: List[Dict[str, Any]] = []
    levels = ("INTUITIVE", "ENGINEERING", "CANONICAL_FORMULATION")

    for i, record in enumerate(output_records, 1):
        required = {"distinction_id", "level", "formulation", "uncertainty"}
        if not required.issubset(record):
            raise M03LLMError(
                f"M03 record {i} is missing required fields"
            )
        if record["level"] not in levels:
            raise M03LLMError(
                f"M03 record {i} has invalid level: {record['level']}"
            )
        normalized.append({
            "id": f"FORM-{i:03d}",
            "distinction_id": record["distinction_id"],
            "level": record["level"],
            "formulation": record["formulation"],
            "uncertainty": record["uncertainty"],
            "source_id": distinction_input["source_id"],
        })

    expected_pairs = [
        (r["id"], level)
        for r in records
        for level in levels
    ]
    actual_pairs = [
        (r["distinction_id"], r["level"])
        for r in normalized
    ]
    if actual_pairs != expected_pairs:
        raise M03LLMError(
            "M03 distinction/level trace mismatch: output order or IDs do not "
            "match required input sequence"
        )

    return normalized
