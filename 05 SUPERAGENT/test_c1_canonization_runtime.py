#!/usr/bin/env python3
"""Acceptance tests for the new executable C1 boundary implementation."""
from __future__ import annotations

import copy
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from c1_canonization import CanonizationError, canonize  # noqa: E402


def _candidate():
    candidate = {
        "record_id": "REC-001",
        "value": "Example requirement",
        "object_type": "REQUIREMENT",
        "canonical_name": "Example requirement",
    }
    raw = json.dumps(candidate, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return {
        "decision_result": "NEW_APPROVED",
        "candidate": candidate,
        "provenance": {"source_id": "SRC-003", "discovery_run": "RUN-001"},
        "traceability": {"source_id": "SRC-003", "match_id": "MAT-001"},
        "approved_candidate_hash": hashlib.sha256(raw.encode()).hexdigest(),
        "new_evidence_ref": "NEW-EVIDENCE-001",
    }


def test_new_approved():
    out = canonize(_candidate())
    assert out["status"] == "CANONICALIZATION_READY"
    assert out["object_id"].startswith("OBJ-")
    assert out["boundary"]["cmoc_write"] == "NONE"


def test_rejected_entry():
    c = _candidate()
    c["decision_result"] = "NEW_REJECTED"
    try:
        canonize(c)
    except CanonizationError as exc:
        assert str(exc) == "ENTRY_REQUIRES_NEW_APPROVED"
    else:
        raise AssertionError("NEW_REJECTED must be rejected")


def test_integrity_mismatch():
    c = _candidate()
    c["candidate"]["value"] = "changed"
    try:
        canonize(c)
    except CanonizationError as exc:
        assert str(exc) == "APPROVED_CANDIDATE_INTEGRITY_MISMATCH"
    else:
        raise AssertionError("changed approved candidate must be rejected")


def test_required_evidence():
    for field in ("provenance", "traceability", "approved_candidate_hash"):
        c = _candidate()
        del c[field]
        try:
            canonize(c)
        except CanonizationError as exc:
            assert str(exc) == f"MISSING_{field.upper()}"
        else:
            raise AssertionError(f"{field} must be required")


def test_forbidden_operations():
    for field, error in (
        ("semantic_enrichment", "HIDDEN_SEMANTIC_ENRICHMENT"),
        ("existing_object_mutation", "EXISTING_OBJECT_MUTATION_FORBIDDEN"),
        ("relations", "UNSUPPORTED_RELATION_CREATION"),
    ):
        c = _candidate()
        c[field] = {"x": True}
        try:
            canonize(c)
        except CanonizationError as exc:
            assert str(exc) == error
        else:
            raise AssertionError(f"{field} must be rejected")


def test_deterministic_identity_and_input_immutability():
    c = _candidate()
    before = copy.deepcopy(c)
    a = canonize(c)
    b = canonize(c)
    assert a["object_id"] == b["object_id"]
    assert c == before


def test_boundary():
    out = canonize(_candidate())
    assert out["boundary"] == {
        "canonization": "PERFORMED",
        "new_decision": "NOT_PERFORMED",
        "semantic_comparison": "NOT_PERFORMED",
        "cmoc_write": "NONE",
        "object_index_write": "NONE",
        "existing_object_mutation": "NONE",
        "relations_created": "NONE",
    }


if __name__ == "__main__":
    tests = [
        test_new_approved,
        test_rejected_entry,
        test_integrity_mismatch,
        test_required_evidence,
        test_forbidden_operations,
        test_deterministic_identity_and_input_immutability,
        test_boundary,
    ]
    for test in tests:
        test()
    print("C1 CANONIZATION RUNTIME TEST: PASS")
