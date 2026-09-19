"""Production M05 adapter: Nomenclature Candidate -> Classification Record.

M05 assigns one source-derived provisional working type to each nomenclature
candidate. It does not create passports, relations, or canonical objects.
"""

from __future__ import annotations

import json
import os
import urllib.request
from typing import Any, Dict, List


class M05LLMError(RuntimeError):
    pass


ALLOWED_TYPES = {
    "SOURCE_IDENTITY",
    "COLLECTION",
    "DECISION",
    "ACTIVITY",
    "CONCEPT_MODEL",
    "STRATEGY",
    "STRUCTURAL_DISTINCTION",
}


def _request_json(payload: Dict[str, Any]) -> Dict[str, Any]:
    api_key = os.getenv("LLM_API_KEY")
    model = os.getenv("LLM_MODEL")
    base_url = os.getenv("LLM_BASE_URL", "https://api.openai.com/v1").rstrip("/")

    if not api_key:
        raise M05LLMError("LLM_API_KEY is not set")
    if not model:
        raise M05LLMError("LLM_MODEL is not set")

    data = json.dumps({
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are MACHINE-SOURCE-001 M05 CLASSIFICATION. "
                    "Assign one source-derived provisional working type to each "
                    "nomenclature candidate. Use only the supplied records and "
                    "their upstream source-grounded formulations. Do not use "
                    "external knowledge. Do not infer a CMOC canonical object."
                ),
            },
            {
                "role": "user",
                "content": json.dumps(payload, ensure_ascii=False),
            },
        ],
    }).encode("utf-8")

    req = urllib.request.Request(
        f"{base_url}/chat/completions",
        data=data,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            raw = response.read().decode("utf-8")
    except Exception as exc:
        raise M05LLMError(f"LLM request failed: {exc}") from exc

    try:
        body = json.loads(raw)
        content = body["choices"][0]["message"]["content"]
        return json.loads(content)
    except Exception as exc:
        raise M05LLMError(f"Invalid LLM JSON response: {exc}") from exc


def classify(candidates: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if not candidates:
        raise M05LLMError("No nomenclature candidates supplied")

    payload = {
        "task": "M05 CLASSIFICATION",
        "rules": [
            "Process every candidate independently.",
            "Return exactly one classification record per candidate.",
            "Classification is a source-derived provisional working type assignment.",
            "Use exactly one type from ALLOWED_TYPES.",
            "Preserve candidate_id and source_id.",
            "Do not create passport fields.",
            "Do not create relation fields.",
            "Do not canonize.",
            "Do not merge or split candidates.",
            "Do not use external knowledge.",
            "If the supplied evidence does not support a type, use type UNKNOWN and uncertainty NEEDS_EVIDENCE.",
        ],
        "ALLOWED_TYPES": sorted(ALLOWED_TYPES),
        "input": candidates,
        "output_schema": {
            "records": [
                {
                    "id": "CLS-001",
                    "candidate_id": "NOM-001",
                    "type": "ONE_ALLOWED_TYPE_OR_UNKNOWN",
                    "status": "PROVISIONAL",
                    "uncertainty": "CLEAR_OR_NEEDS_EVIDENCE",
                    "source_id": "SRC-002",
                }
            ]
        },
    }

    result = _request_json(payload)
    records = result.get("records")
    if not isinstance(records, list):
        raise M05LLMError("Response must contain records list")

    if len(records) != len(candidates):
        raise M05LLMError(
            f"Cardinality mismatch: {len(candidates)} candidates -> {len(records)} classifications"
        )

    expected = [c["id"] for c in candidates]
    actual = [r.get("candidate_id") for r in records]
    if actual != expected:
        raise M05LLMError(
            f"Candidate order mismatch: expected {expected}, got {actual}"
        )

    normalized = []
    for i, (record, candidate) in enumerate(zip(records, candidates), start=1):
        ctype = record.get("type")
        if ctype not in ALLOWED_TYPES and ctype != "UNKNOWN":
            raise M05LLMError(
                f"Unsupported classification type for {candidate['id']}: {ctype}"
            )

        status = record.get("status")
        if status != "PROVISIONAL":
            raise M05LLMError(
                f"M05 status must be PROVISIONAL for {candidate['id']}, got {status}"
            )

        uncertainty = record.get("uncertainty")
        if uncertainty not in {"CLEAR", "NEEDS_EVIDENCE"}:
            raise M05LLMError(
                f"Invalid uncertainty for {candidate['id']}: {uncertainty}"
            )

        normalized.append({
            "id": f"CLS-{i:03d}",
            "candidate_id": candidate["id"],
            "type": ctype,
            "status": "PROVISIONAL",
            "uncertainty": uncertainty,
            "source_id": candidate["source_id"],
        })

    return normalized
