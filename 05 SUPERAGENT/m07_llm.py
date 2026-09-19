"""Production M07 relation-candidate adapter.

Input: Passport Records.
Output: source-bound Relation Candidates / explicit NO_RELATION / NEEDS_EVIDENCE.
"""

import json
import os
import urllib.request
from typing import Any, Dict, List


class M07LLMError(RuntimeError):
    pass


SYSTEM_PROMPT = """
You are M07 RELATIONS of MACHINE-SOURCE-001.

Your operation is strictly limited to identifying SOURCE-SUPPORTED RELATION CANDIDATES
between supplied Passport Records.

Use ONLY the supplied Passport Records and their source_basis references.
Do not use external knowledge.

A relation candidate requires:
- two explicit passport endpoints;
- a source-supported basis for the relation;
- a relation_type;
- basis_refs pointing to supplied evidence.

Do NOT infer a relation from:
- shared source;
- similar terms;
- working classes;
- shared formulation basis;
- source adjacency;
- presumed hierarchy;
- presumed causality;
- presumed dependency;
- general domain knowledge.

If the supplied passports do not contain explicit evidence supporting a relation,
return an explicit NO_RELATION result rather than inventing one.

If a relation might exist but the supplied evidence is insufficient to establish it,
return NEEDS_EVIDENCE with a concrete evidence_gap.

A RELATION_CANDIDATE is provisional. It is NOT an established CMOC relation.
Never assign CANONICAL.

Return JSON only:
{
  "records": [
    {
      "id": "REL-001",
      "source_id": "...",
      "from_passport_id": "PAS-...",
      "to_passport_id": "PAS-...",
      "relation_type": "...",
      "status": "ЧЕРНОВИК",
      "epistemic_status": "PROVISIONAL",
      "basis_refs": ["..."],
      "evidence_gap": null
    }
  ],
  "evaluated_scope": ["PAS-001", "..."]
}

For NO_RELATION or NEEDS_EVIDENCE use:
{
  "id": "REL-NONE-001",
  "source_id": "...",
  "status": "NO_RELATION",
  "epistemic_status": "PROVISIONAL",
  "basis_refs": [],
  "evidence_gap": "..."
}

Every supplied passport must be represented in evaluated_scope.
Do not create a relation merely to satisfy cardinality.
""".strip()


def _request_json(payload: Dict[str, Any]) -> Dict[str, Any]:
    api_key = os.getenv("LLM_API_KEY")
    model = os.getenv("LLM_MODEL")
    base_url = os.getenv("LLM_BASE_URL", "https://api.openai.com/v1")

    if not api_key:
        raise M07LLMError("LLM_API_KEY is not set")
    if not model:
        raise M07LLMError("LLM_MODEL is not set")

    body = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
        ],
    }).encode("utf-8")

    req = urllib.request.Request(
        f"{base_url.rstrip('/')}/chat/completions",
        data=body,
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
        raise M07LLMError(f"LLM request failed: {exc}") from exc

    try:
        outer = json.loads(raw)
        content = outer["choices"][0]["message"]["content"]
        return json.loads(content)
    except Exception as exc:
        raise M07LLMError(f"Invalid M07 LLM response: {exc}") from exc


def build_relation_candidates(passports: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    if not passports:
        raise M07LLMError("No Passport Records supplied")

    payload = {
        "task": "M07 RELATIONS",
        "passports": passports,
    }
    result = _request_json(payload)

    records = result.get("records")
    evaluated_scope = result.get("evaluated_scope")

    if not isinstance(records, list):
        raise M07LLMError("M07 response must contain records list")
    if not isinstance(evaluated_scope, list):
        raise M07LLMError("M07 response must contain evaluated_scope list")

    expected_scope = [p["id"] for p in passports]
    if evaluated_scope != expected_scope:
        raise M07LLMError(
            f"Evaluated scope mismatch: expected {expected_scope}, got {evaluated_scope}"
        )

    passport_ids = set(expected_scope)

    for record in records:
        status = record.get("status")

        if record.get("source_id") != passports[0].get("source_id"):
            raise M07LLMError("Source ID mismatch")

        if status == "RELATION_CANDIDATE":
            if record.get("from_passport_id") not in passport_ids:
                raise M07LLMError("Unknown from_passport_id")
            if record.get("to_passport_id") not in passport_ids:
                raise M07LLMError("Unknown to_passport_id")
            if record.get("from_passport_id") == record.get("to_passport_id"):
                raise M07LLMError("Self-relation is not allowed")
            if not record.get("relation_type"):
                raise M07LLMError("Relation candidate requires relation_type")
            if record.get("status") != "RELATION_CANDIDATE":
                raise M07LLMError("Invalid relation candidate status")
            if record.get("epistemic_status") != "PROVISIONAL":
                raise M07LLMError("Relation candidate must remain PROVISIONAL")
            if not isinstance(record.get("basis_refs"), list) or not record["basis_refs"]:
                raise M07LLMError("Relation candidate requires basis_refs")
            if record.get("evidence_gap") not in (None, ""):
                raise M07LLMError("Accepted relation candidate must not carry evidence_gap")

        elif status == "NO_RELATION":
            if record.get("basis_refs") not in ([], None):
                raise M07LLMError("NO_RELATION must not carry relation basis_refs")
        elif status == "NEEDS_EVIDENCE":
            if not record.get("evidence_gap"):
                raise M07LLMError("NEEDS_EVIDENCE requires evidence_gap")
        else:
            raise M07LLMError(f"Unsupported M07 status: {status}")

        if "CANONICAL" in json.dumps(record, ensure_ascii=False):
            raise M07LLMError("Canonical relation/status detected in M07 output")

    return records
