"""Production M08 decision adapter for SRC-002.

M08 evaluates source-bound passports and an optional source-supported relation
candidate. It does not perform automatic canonization.
"""

from __future__ import annotations

import json
import os
import urllib.request
from typing import Any, Dict, List, Optional


class M08LLMError(RuntimeError):
    pass


SYSTEM_PROMPT = """You are M08 CANONIZATION DECISION for MACHINE-SOURCE-001.

Use ONLY the supplied Passport Records, Relation Candidate records, and explicit
source-bound relation evidence.

Apply this exact decision sequence:
1. Source Evidence
2. Object Boundary
3. Type Assignment
4. PROVISIONAL if all controlled gates pass
5. CANONICAL only if an explicit separate CMOC canonicalization criterion is
   supplied and passed.

For the controlled run, no separate canonicalization criterion is supplied.
Therefore do NOT return CANONICAL.

A relation candidate does not become a canonical relation automatically.

Do not use external knowledge. Do not invent properties. Do not infer relations
from shared source, terminology, working class, shared formulation basis,
adjacency, hierarchy, causality, dependency, or domain knowledge.

If a required evidence element is missing, return NEEDS_EVIDENCE and a concrete
evidence_gap. Do not silently fill missing evidence.

Return JSON only:
{
  "records": [
    {
      "id": "DEC-001",
      "target_id": "...",
      "target_kind": "RELATION_CANDIDATE|PASSPORT",
      "decision": "PROVISIONAL|CANONICAL|NEEDS_EVIDENCE|REJECT",
      "lifecycle_status": "ЧЕРНОВИК",
      "epistemic_status": "PROVISIONAL|NEEDS_EVIDENCE|CANONICAL",
      "reason": "...",
      "basis_refs": ["..."],
      "evidence_gap": null
    }
  ]
}

Preserve supplied IDs and basis references exactly.
For the controlled relation-dependent branch, evaluate the supplied relation
candidate and return one decision for it.
"""


def _request_json(payload: Dict[str, Any]) -> Dict[str, Any]:
    key = os.getenv("LLM_API_KEY")
    if not key:
        raise M08LLMError("LLM_API_KEY is not set")

    model = os.getenv("LLM_MODEL")
    if not model:
        raise M08LLMError("LLM_MODEL is not set")

    base_url = os.getenv("LLM_BASE_URL", "https://api.openai.com/v1").rstrip("/")
    body = json.dumps(
        {
            "model": model,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
            ],
            "response_format": {"type": "json_object"},
        }
    ).encode("utf-8")

    req = urllib.request.Request(
        f"{base_url}/chat/completions",
        data=body,
        headers={
            "Authorization": f"Bearer {key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as response:
            raw = response.read().decode("utf-8")
    except Exception as exc:
        raise M08LLMError(f"M08 API request failed: {exc}") from exc

    try:
        envelope = json.loads(raw)
        content = envelope["choices"][0]["message"]["content"]
        return json.loads(content)
    except Exception as exc:
        raise M08LLMError(f"Invalid M08 API response: {exc}") from exc


def decide(
    passports: List[Dict[str, Any]],
    relation_candidates: Optional[List[Dict[str, Any]]] = None,
    relation_evidence: Optional[List[Dict[str, Any]]] = None,
) -> Dict[str, Any]:
    relation_candidates = relation_candidates or []
    relation_evidence = relation_evidence or []

    if not passports:
        raise M08LLMError("No passport records supplied")

    payload = {
        "task": "M08",
        "passports": passports,
        "relation_candidates": relation_candidates,
        "relation_evidence": relation_evidence,
        "canonicalization_criterion": None,
    }

    result = _request_json(payload)
    records = result.get("records")

    if not isinstance(records, list):
        raise M08LLMError("M08 response must contain records list")

    # Terminal negative branch: M07 may explicitly return NO_RELATION.
    # In that case M08 must consume the actual M07 result and produce no
    # downstream decision. It must not reinterpret NO_RELATION as a relation.
    if relation_candidates and all(
        r.get("status") == "NO_RELATION" for r in relation_candidates
    ):
        if records:
            raise M08LLMError(
                "M08 must return no decisions for a terminal NO_RELATION branch"
            )
        return result

    if relation_candidates and any(
        r.get("status") == "NO_RELATION" for r in relation_candidates
    ):
        raise M08LLMError(
            "Mixed NO_RELATION and relation records require explicit branch handling"
        )

    expected = relation_candidates if relation_candidates else passports
    if len(records) != len(expected):
        raise M08LLMError(
            f"Cardinality mismatch: expected {len(expected)}, got {len(records)}"
        )

    expected_ids = [
        r.get("id") for r in expected
    ]

    for i, (record, source) in enumerate(zip(records, expected), start=1):
        if not isinstance(record, dict):
            raise M08LLMError(f"Record {i} is not an object")

        if record.get("target_id") != source.get("id"):
            raise M08LLMError(
                f"Target mismatch at position {i}: "
                f"{record.get('target_id')} != {source.get('id')}"
            )

        if record.get("decision") == "CANONICAL":
            raise M08LLMError(
                "CANONICAL decision is forbidden without a separate canonicalization criterion"
            )

        if record.get("lifecycle_status") != "ЧЕРНОВИК":
            raise M08LLMError(f"Invalid lifecycle status at position {i}")

        decision = record.get("decision")
        if decision == "PROVISIONAL":
            if record.get("epistemic_status") != "PROVISIONAL":
                raise M08LLMError(f"Invalid epistemic status at position {i}")
        elif decision == "NEEDS_EVIDENCE":
            if not record.get("evidence_gap"):
                raise M08LLMError(f"Missing evidence_gap at position {i}")
            if record.get("epistemic_status") != "NEEDS_EVIDENCE":
                raise M08LLMError(f"Invalid NEEDS_EVIDENCE status at position {i}")
        elif decision != "REJECT":
            raise M08LLMError(f"Unsupported decision at position {i}: {decision}")

        supplied_basis = source.get("basis_refs", [])
        returned_basis = record.get("basis_refs", [])
        if decision == "PROVISIONAL" and returned_basis != supplied_basis:
            raise M08LLMError(
                f"Basis reference mismatch at position {i}: "
                f"{returned_basis} != {supplied_basis}"
            )

    return result
