import json
import os
import urllib.request
import ssl
from typing import Any, Dict, List


_TLS_CONTEXT = ssl.create_default_context()
_TLS_CONTEXT.minimum_version = ssl.TLSVersion.TLSv1_2
_TLS_CONTEXT.maximum_version = ssl.TLSVersion.TLSv1_2


class M06LLMError(RuntimeError):
    pass


def _request_json(payload: Dict[str, Any]) -> Dict[str, Any]:
    api_key = os.environ.get("LLM_API_KEY")
    model = os.environ.get("LLM_MODEL")
    base_url = os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1").rstrip("/")

    if not api_key:
        raise M06LLMError("LLM_API_KEY is not set")
    if not model:
        raise M06LLMError("LLM_MODEL is not set")

    req = urllib.request.Request(
        f"{base_url}/chat/completions",
        data=json.dumps({
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "You are M06 PASSPORT in MACHINE-SOURCE-001. "
                        "Work only from the supplied classification records and their "
                        "source-bound candidate terms. Form one source-bound working "
                        "Passport Record per classification. Do not use external knowledge."
                    ),
                },
                {
                    "role": "user",
                    "content": json.dumps(payload, ensure_ascii=False),
                },
            ],
        }).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, context=_TLS_CONTEXT, timeout=120) as response:
            data = json.loads(response.read().decode("utf-8"))
    except Exception as exc:
        raise M06LLMError(f"LLM request failed: {exc}") from exc

    try:
        content = data["choices"][0]["message"]["content"]
        return json.loads(content)
    except Exception as exc:
        raise M06LLMError("Invalid JSON response from LLM") from exc


def build_passports(classifications: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if not classifications:
        raise M06LLMError("No classification records supplied")

    payload = {
        "task": "M06 PASSPORT",
        "rules": [
            "Process every classification independently.",
            "Return exactly one passport per classification.",
            "Preserve candidate_id, classification id, source_id and working class.",
            "lifecycle_status must be ЧЕРНОВИК.",
            "epistemic_status must be PROVISIONAL.",
            "Object boundary must be explicitly source-bound.",
            "source_basis must preserve the supplied upstream basis references; do not invent source locations or evidence.",
            "Do not create relations.",
            "Do not canonize.",
            "Do not assign CANONICAL.",
            "Do not add unsupported external properties.",
            "A Passport is not a canonical CMOC object.",
            "If the supplied basis is insufficient, use NEEDS_EVIDENCE and state a concrete EVIDENCE_GAP.",
            "Return JSON only."
        ],
        "classifications": classifications,
        "output_schema": {
            "records": [
                {
                    "id": "PAS-001",
                    "candidate_id": "NOM-001",
                    "classification_id": "CLS-001",
                    "source_id": "SRC-002",
                    "term": "candidate term",
                    "working_class": "...",
                    "lifecycle_status": "ЧЕРНОВИК",
                    "epistemic_status": "PROVISIONAL",
                    "object_boundary": "...",
                    "source_basis": ["p1"],
                    "evidence_gap": None
                }
            ]
        },
    }

    result = _request_json(payload)
    records = result.get("records")
    if not isinstance(records, list):
        raise M06LLMError("Response does not contain records list")

    if len(records) != len(classifications):
        raise M06LLMError(
            f"Cardinality mismatch: expected {len(classifications)}, got {len(records)}"
        )

    for i, (record, source) in enumerate(zip(records, classifications), start=1):
        if record.get("candidate_id") != source.get("candidate_id"):
            raise M06LLMError(f"Candidate binding mismatch at position {i}")
        if record.get("classification_id") != source.get("id"):
            raise M06LLMError(f"Classification binding mismatch at position {i}")
        if record.get("source_id") != source.get("source_id"):
            raise M06LLMError(f"Source binding mismatch at position {i}")
        if record.get("term") != source.get("candidate_term"):
            raise M06LLMError(f"Candidate term mismatch at position {i}")
        if record.get("source_basis") != source.get("basis_refs", []):
            raise M06LLMError(f"Source basis mismatch at position {i}")
        if record.get("lifecycle_status") != "ЧЕРНОВИК":
            raise M06LLMError(f"Invalid lifecycle status at position {i}")
        if record.get("epistemic_status") not in {"PROVISIONAL", "NEEDS_EVIDENCE"}:
            raise M06LLMError(f"Invalid epistemic status at position {i}")
        record["id"] = f"PAS-{i:03d}"

    return records
