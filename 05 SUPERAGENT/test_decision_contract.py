#!/usr/bin/env python3
"""Acceptance tests for DECISION-CONTRACT-001 v0.1."""
from __future__ import annotations

import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from decision import DecisionContractError, build_decision  # noqa: E402


def _record(match_result="NEEDS_REVIEW", cmoc_object_id=None):
    return {
        "match_id": "MAT-PAS-001",
        "source_id": "SRC-003",
        "cmoc_object_id": cmoc_object_id,
        "match_result": match_result,
        "basis": "upstream basis",
        "traceability": {
            "source_id": "SRC-003",
            "discovery_run": "RUN-SRC-003-001",
            "reconciliation_id": "RECON-001",
            "upstream_batch": "BATCH-SRC-003-M06-006",
        },
    }


def _human(result, record):
    return build_decision(
        "DEC-001",
        "HUMAN",
        result,
        record,
        "Human review basis: explicit decision after reconciliation evidence",
        decided_by="operator-001",
        decided_at="2026-09-24T09:00:00+02:00",
    )


def test_admit_existing():
    out = _human(
        "ADMIT_EXISTING",
        _record("EXISTING_EQUIVALENT", "OBJ-001"),
    )
    assert out["type"] == "DECISION"
    assert out["decision"]["decision_result"] == "ADMIT_EXISTING"
    assert out["decision"]["match_id"] == "MAT-PAS-001"
    assert out["decision"]["traceability"]["reconciliation_id"] == "RECON-001"


def test_admit_new():
    out = _human("ADMIT_NEW", _record("NEEDS_REVIEW"))
    assert out["decision"]["decision_result"] == "ADMIT_NEW"
    assert out["boundary"]["admission_execution"] == "NOT_PERFORMED"


def test_reject():
    out = _human("REJECT", _record("NEEDS_REVIEW"))
    assert out["decision"]["decision_result"] == "REJECT"


def test_defer():
    out = _human("DEFER", _record("NEEDS_REVIEW"))
    assert out["decision"]["decision_result"] == "DEFER"


def test_missing_required_fields_rejected():
    record = _record()
    for kwargs, expected in [
        ({"decision_id": ""}, "MISSING_DECISION_ID"),
        ({"decision_id": "DEC-001", "basis": ""}, "MISSING_BASIS"),
    ]:
        params = {
            "decision_id": "DEC-001",
            "decision_type": "HUMAN",
            "decision_result": "DEFER",
            "reconciliation_record": record,
            "basis": "basis",
            "decided_by": "operator-001",
            "decided_at": "2026-09-24T09:00:00+02:00",
        }
        params.update(kwargs)
        try:
            build_decision(**params)
        except DecisionContractError as exc:
            assert str(exc) == expected
        else:
            raise AssertionError(f"{expected} must be rejected")


def test_invalid_result_rejected():
    try:
        _human("NEW", _record())
    except DecisionContractError as exc:
        assert str(exc).startswith("UNSUPPORTED_DECISION_RESULT")
    else:
        raise AssertionError("NEW must not be accepted")


def test_human_without_decided_by_rejected():
    try:
        build_decision(
            "DEC-001", "HUMAN", "DEFER", _record(), "basis",
            decided_at="2026-09-24T09:00:00+02:00",
        )
    except DecisionContractError as exc:
        assert str(exc) == "HUMAN_DECISION_MISSING_DECIDED_BY"
    else:
        raise AssertionError("HUMAN without decided_by must be rejected")


def test_rule_without_rule_fields_rejected():
    try:
        build_decision(
            "DEC-001", "RULE", "ADMIT_EXISTING",
            _record("EXISTING_EQUIVALENT", "OBJ-001"), "rule basis",
            decided_at="2026-09-24T09:00:00+02:00",
        )
    except DecisionContractError as exc:
        assert str(exc) == "RULE_DECISION_MISSING_RULE_ID"
    else:
        raise AssertionError("RULE without rule_id must be rejected")


def test_admit_existing_without_equivalent_rejected():
    try:
        _human("ADMIT_EXISTING", _record("NEEDS_REVIEW"))
    except DecisionContractError as exc:
        assert str(exc) == "ADMIT_EXISTING_REQUIRES_EXISTING_EQUIVALENT"
    else:
        raise AssertionError("ADMIT_EXISTING without equivalent must be rejected")


def test_admit_existing_without_cmoc_id_rejected():
    try:
        _human("ADMIT_EXISTING", _record("EXISTING_EQUIVALENT", None))
    except DecisionContractError as exc:
        assert str(exc) == "ADMIT_EXISTING_REQUIRES_CMOC_OBJECT_ID"
    else:
        raise AssertionError("ADMIT_EXISTING without cmoc_object_id must be rejected")


def test_admit_new_requires_review_state():
    try:
        _human("ADMIT_NEW", _record("EXISTING_EQUIVALENT", "OBJ-001"))
    except DecisionContractError as exc:
        assert str(exc) == "ADMIT_NEW_REQUIRES_NEEDS_REVIEW"
    else:
        raise AssertionError("ADMIT_NEW from existing equivalent must be rejected")


def test_input_is_not_mutated():
    record = _record("EXISTING_EQUIVALENT", "OBJ-001")
    before = copy.deepcopy(record)
    _human("ADMIT_EXISTING", record)
    assert record == before


def test_no_downstream_mutation_boundary():
    out = _human("ADMIT_EXISTING", _record("EXISTING_EQUIVALENT", "OBJ-001"))
    assert out["boundary"] == {
        "origin": "DECISION",
        "reconciliation_mutation": "NONE",
        "cmoc_write": "NONE",
        "object_index_write": "NONE",
        "admission_execution": "NOT_PERFORMED",
    }


if __name__ == "__main__":
    tests = [
        test_admit_existing,
        test_admit_new,
        test_reject,
        test_defer,
        test_missing_required_fields_rejected,
        test_invalid_result_rejected,
        test_human_without_decided_by_rejected,
        test_rule_without_rule_fields_rejected,
        test_admit_existing_without_equivalent_rejected,
        test_admit_existing_without_cmoc_id_rejected,
        test_admit_new_requires_review_state,
        test_input_is_not_mutated,
        test_no_downstream_mutation_boundary,
    ]
    for test in tests:
        test()
    print("DECISION CONTRACT TEST: PASS")
