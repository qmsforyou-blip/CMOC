#!/usr/bin/env python3
"""Acceptance tests for ADMIT_EXISTING MVP boundary."""
from __future__ import annotations

import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from admission import AdmissionError, admit_existing, admit_new  # noqa: E402


def _decision():
    return {
        "type": "DECISION",
        "decision": {
            "decision_id": "DEC-001",
            "decision_type": "HUMAN",
            "decision_result": "ADMIT_EXISTING",
            "match_id": "MAT-001",
            "basis": "Human decision after exact reconciliation",
            "source_id": "SRC-003",
            "traceability": {
                "source_id": "SRC-003",
                "discovery_run": "RUN-001",
                "reconciliation_id": "RECON-001",
                "match_id": "MAT-001",
                "cmoc_object_id": "OBJ-001",
                "source_package": "SOURCE-003-PACKAGE-001",
            },
            "decided_by": "operator-001",
            "decided_at": "2026-09-24T09:00:00+02:00",
            "rule_id": None,
            "rule_version": None,
        },
        "boundary": {
            "origin": "DECISION",
            "reconciliation_mutation": "NONE",
            "cmoc_write": "NONE",
            "object_index_write": "NONE",
            "admission_execution": "NOT_PERFORMED",
        },
    }


def test_admit_existing_creates_record():
    out = admit_existing(_decision())
    assert out["type"] == "ADMISSION"
    assert out["admission"]["decision_id"] == "DEC-001"
    assert out["admission"]["match_id"] == "MAT-001"
    assert out["admission"]["target_cmoc_object_id"] == "OBJ-001"
    assert out["admission"]["admission_result"] == "ADMIT_EXISTING"


def test_admission_id_is_deterministic():
    a = admit_existing(_decision())
    b = admit_existing(_decision())
    assert a["admission"]["admission_id"] == b["admission"]["admission_id"]


def test_no_cmoc_write_for_admit_existing_mvp():
    out = admit_existing(_decision())
    assert out["boundary"]["cmoc_write"] == "NONE"
    assert out["boundary"]["object_index_write"] == "NONE"


def test_decision_is_not_mutated():
    decision = _decision()
    before = copy.deepcopy(decision)
    admit_existing(decision)
    assert decision == before


def test_wrong_decision_rejected():
    decision = _decision()
    decision["decision"]["decision_result"] = "ADMIT_NEW"
    try:
        admit_existing(decision)
    except AdmissionError as exc:
        assert str(exc) == "ADMIT_EXISTING_DECISION_REQUIRED"
    else:
        raise AssertionError("non-ADMIT_EXISTING decision must be rejected")


def test_missing_target_rejected():
    decision = _decision()
    del decision["decision"]["traceability"]["cmoc_object_id"]
    try:
        admit_existing(decision)
    except AdmissionError as exc:
        assert str(exc) == "TARGET_CMOC_OBJECT_REQUIRED"
    else:
        raise AssertionError("missing target CMOC object must be rejected")


if __name__ == "__main__":
    tests = [
        test_admit_existing_creates_record,
        test_admission_id_is_deterministic,
        test_no_cmoc_write_for_admit_existing_mvp,
        test_decision_is_not_mutated,
        test_wrong_decision_rejected,
        test_missing_target_rejected,
    ]
    for test in tests:
        test()
    print("ADMISSION ADMIT_EXISTING TEST: PASS")


def test_admit_new_registers_pending_pipeline_only():
    decision = _decision()
    decision["decision"]["decision_result"] = "ADMIT_NEW"
    decision["decision"]["cmoc_object_id"] = None
    out = admit_new(decision)
    assert out["admission"]["admission_result"] == "ADMIT_NEW"
    assert out["admission"]["pipeline_status"] == "PENDING_C1"
    assert out["admission"]["target_cmoc_object_id"] is None
    assert out["boundary"]["cmoc_write"] == "NONE"
    assert out["boundary"]["canonization_execution"] == "NOT_PERFORMED"
    assert out["boundary"]["c1_c2_c3_execution"] == "NOT_PERFORMED"


def test_admit_new_requires_explicit_decision():
    decision = _decision()
    decision["decision"]["decision_result"] = "DEFER"
    try:
        admit_new(decision)
    except AdmissionError as exc:
        assert str(exc) == "ADMIT_NEW_DECISION_REQUIRED"
    else:
        raise AssertionError("non-ADMIT_NEW decision must be rejected")


def test_admit_new_to_c1_boundary():
    from admission import execute_c1_from_admission

    decision = _decision()
    decision["decision"]["decision_result"] = "ADMIT_NEW"
    decision["decision"]["cmoc_object_id"] = None

    admission = admit_new(decision)
    approved_candidate = {
        "decision_result": "NEW_APPROVED",
        "candidate": {"record_id": "REC-001", "value": "Approved object"},
        "provenance": {"source_id": "SRC-003"},
        "traceability": {"source_id": "SRC-003", "match_id": "MAT-001"},
        "approved_candidate_hash": "HASH-001",
    }

    c1_input = execute_c1_from_admission(admission, approved_candidate)

    assert c1_input["decision_result"] == "NEW_APPROVED"
    assert c1_input["admission_id"] == admission["admission"]["admission_id"]
    assert c1_input["decision_id"] == "DEC-001"
    assert c1_input["match_id"] == "MAT-001"
    assert c1_input["source_id"] == "SRC-003"


def test_admit_new_c1_requires_pending_state():
    from admission import execute_c1_from_admission

    decision = _decision()
    decision["decision"]["decision_result"] = "ADMIT_NEW"
    admission = admit_new(decision)
    admission["admission"]["pipeline_status"] = "COMPLETED"

    try:
        execute_c1_from_admission(admission, {"decision_result": "NEW_APPROVED"})
    except AdmissionError as exc:
        assert str(exc) == "ADMISSION_NOT_PENDING_C1"
    else:
        raise AssertionError("non-pending Admission must not enter C1")
