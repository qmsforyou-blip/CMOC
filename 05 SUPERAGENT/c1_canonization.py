#!/usr/bin/env python3
"""Isolated C1 canonization boundary."""
from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from typing import Any, Dict


class CanonizationError(ValueError):
    pass


def _canonical_hash(candidate: Dict[str, Any]) -> str:
    raw = json.dumps(candidate, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def canonize(candidate: Dict[str, Any]) -> Dict[str, Any]:
    if not isinstance(candidate, dict):
        raise CanonizationError("CANDIDATE_NOT_OBJECT")
    if candidate.get("decision_result") != "NEW_APPROVED":
        raise CanonizationError("ENTRY_REQUIRES_NEW_APPROVED")

    for field in ("candidate", "provenance", "traceability", "approved_candidate_hash"):
        if not candidate.get(field):
            raise CanonizationError(f"MISSING_{field.upper()}")

    approved = deepcopy(candidate["candidate"])
    actual_hash = _canonical_hash(approved)
    if actual_hash != candidate["approved_candidate_hash"]:
        raise CanonizationError("APPROVED_CANDIDATE_INTEGRITY_MISMATCH")

    if candidate.get("existing_object_mutation"):
        raise CanonizationError("EXISTING_OBJECT_MUTATION_FORBIDDEN")
    if candidate.get("relations"):
        raise CanonizationError("UNSUPPORTED_RELATION_CREATION")
    if candidate.get("semantic_enrichment"):
        raise CanonizationError("HIDDEN_SEMANTIC_ENRICHMENT")

    record_id = approved.get("record_id")
    if not record_id:
        raise CanonizationError("CANDIDATE_RECORD_ID_REQUIRED")

    object_id = "OBJ-" + hashlib.sha256(
        f"C1|{record_id}|{actual_hash}".encode("utf-8")
    ).hexdigest()[:16]

    canonical_name = approved.get("canonical_name") or approved.get("value")
    canonical_representation = deepcopy(approved)

    return {
        "status": "CANONICALIZATION_READY",
        "object_id": object_id,
        "object_type": approved.get("object_type"),
        "canonical_name": canonical_name,
        "canonical_representation": canonical_representation,
        "provenance": deepcopy(candidate["provenance"]),
        "traceability": deepcopy(candidate["traceability"]),
        "new_evidence_ref": candidate.get("new_evidence_ref"),
        "approved_candidate_hash": actual_hash,
        "boundary": {
            "canonization": "PERFORMED",
            "new_decision": "NOT_PERFORMED",
            "semantic_comparison": "NOT_PERFORMED",
            "cmoc_write": "NONE",
            "object_index_write": "NONE",
            "existing_object_mutation": "NONE",
            "relations_created": "NONE",
        },
    }
