"""M04 nomenclature candidate adapter for SUPERAGENT MVP.

Accepts FORMULATION_RECORDS grouped by distinction and selects one provisional
nomenclature candidate per formulation group. The adapter does not classify,
passport, relate, or canonize candidates.
"""
from __future__ import annotations

import json
import os
import urllib.request
from typing import Any, Dict, List


M04_SYSTEM_PROMPT = """You are MACHINE-SOURCE-001 executing TASK M04 NOMENCLATURE.

For each supplied group of exactly three formulation records belonging to one
Distinction Record, select exactly one provisional nomenclature candidate.

Rules:
- Process each formulation group independently.
- Exactly one candidate per input formulation group.
- Use the three formulations together only to select the nomenclature candidate
  for that same distinction.
- The candidate is a proposed stable term/name for the distinction, not a CMOC
  object and not a canonical term.
- Prefer a concise term that is explicitly supported by the formulation group.
- Preserve source-grounded meaning.
- Do not add external knowledge.
- Do not merge different distinction groups.
- Do not classify the candidate.
- Do not create passport fields.
- Do not create relations.
- Do not canonize.
- Do not infer a broader object than the formulation group supports.
- Do not silently split one formulation group into multiple candidates.
- If the group does not support a reliable single candidate, return
  uncertainty=UNCERTAIN and use a minimal source-grounded candidate only when
  possible; otherwise candidate_term may be UNKNOWN.
- Candidate/object boundary must remain explicit.

For every output return:
- id: NOM-###
- distinction_id
- candidate_term
- status: PROVISIONAL
- uncertainty: CLEAR or UNCERTAIN
- source_id

Return JSON only:
{"records":[...]}

Output order must follow the input formulation-group order.
"""


class M04LLMError(RuntimeError):
    pass


def _request_json(payload: Dict[str, Any], timeout: int = 120) -> Dict[str, Any]:
    api_key = os.environ.get("LLM_API_KEY")
    model = os.environ.get("LLM_MODEL")
    base_url = os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1").rstrip("/")

    if not api_key:
        raise M04LLMError("LLM_API_KEY is not set")
    if not model:
        raise M04LLMError("LLM_MODEL is not set")

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
        raise M04LLMError(f"LLM request failed: {exc}") from exc


def select_nomenclature(formulation_input: Dict[str, Any]) -> List[Dict[str, Any]]:
    records = formulation_input.get("records", [])
    if not records:
        raise M04LLMError("FORMULATION_RECORDS has no records")

    groups: List[Dict[str, Any]] = []
    current: Dict[str, List[Dict[str, Any]]] = {}
    order: List[str] = []

    for record in records:
        did = record.get("distinction_id")
        if not did:
            raise M04LLMError("FORMULATION_RECORD is missing distinction_id")
        current.setdefault(did, []).append(record)
        if did not in order:
            order.append(did)

    for did in order:
        group = current[did]
        if len(group) != 3:
            raise M04LLMError(
                f"M04 requires exactly 3 formulations per distinction; "
                f"{did} has {len(group)}"
            )
        levels = [r.get("level") for r in group]
        if levels != ["INTUITIVE", "ENGINEERING", "CANONICAL_FORMULATION"]:
            raise M04LLMError(f"M04 invalid formulation levels for {did}: {levels}")
        groups.append({"distinction_id": did, "formulations": group})

    user_payload = {
        "source_id": formulation_input["source_id"],
        "groups": groups,
    }

    response = _request_json({
        "model": os.environ["LLM_MODEL"],
        "messages": [
            {"role": "system", "content": M04_SYSTEM_PROMPT},
            {"role": "user", "content": json.dumps(user_payload, ensure_ascii=False)},
        ],
    })

    try:
        content = response["choices"][0]["message"]["content"]
        parsed = json.loads(content)
        output_records = parsed["records"]
    except (KeyError, TypeError, json.JSONDecodeError) as exc:
        raise M04LLMError(f"Invalid M04 JSON response: {exc}") from exc

    if not isinstance(output_records, list):
        raise M04LLMError("M04 records must be a list")

    if len(output_records) != len(groups):
        raise M04LLMError(
            f"M04 cardinality mismatch: {len(groups)} formulation groups -> "
            f"{len(output_records)} candidates"
        )

    normalized: List[Dict[str, Any]] = []
    expected_ids = [g["distinction_id"] for g in groups]

    for i, record in enumerate(output_records, 1):
        required = {"distinction_id", "candidate_term", "status", "uncertainty"}
        if not required.issubset(record):
            raise M04LLMError(f"M04 record {i} is missing required fields")
        if record["status"] != "PROVISIONAL":
            raise M04LLMError(
                f"M04 record {i} must have status PROVISIONAL"
            )
        if not isinstance(record["candidate_term"], str) or not record["candidate_term"].strip():
            raise M04LLMError(f"M04 record {i} has empty candidate_term")
        normalized.append({
            "id": f"NOM-{i:03d}",
            "distinction_id": record["distinction_id"],
            "candidate_term": record["candidate_term"].strip(),
            "status": "PROVISIONAL",
            "uncertainty": record["uncertainty"],
            "source_id": formulation_input["source_id"],
        })

    actual_ids = [r["distinction_id"] for r in normalized]
    if actual_ids != expected_ids:
        raise M04LLMError(
            "M04 distinction trace mismatch: output order or IDs do not "
            "match formulation-group order"
        )

    return normalized
