#!/usr/bin/env python3
"""Acceptance tests for RECONCILIATION_RESULT v0.1."""
from __future__ import annotations

import copy
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from reconciliation_result import (  # noqa: E402
    ReconciliationResultError,
    build_reconciliation_result,
)


def _record(
    result="NEEDS_REVIEW",
    cmoc_object_id=None,
    basis="NO_MATCH from configured query modes; NEW not yet proven",
):
    return {
        "match_id": "MAT-PAS-001",
        "source_id": "SRC-003",
        "input_batch_id": "BATCH-SRC-003-M06-006",
        "input_record_id": "PAS-001",
        "cmoc_object_id": cmoc_object_id,
        "match_result": result,
        "basis": basis,
        "status": "PROVISIONAL",
        "traceability": {
            "source_id": "SRC-003",
            "source_package": "SOURCE-003-PACKAGE-001-CONTROLLED-5-6",
            "discovery_run": "RUN-SRC-003-AUTOMATED-M01-M08-001",
            "upstream_batch": "BATCH-SRC-003-M06-006",
            "passport_id": "PAS-001",
            "object_boundary": "source-bound",
        },
    }


def test_needs_review():
    result = build_reconciliation_result(
        "SRC-003",
        "RUN-SRC-003-AUTOMATED-M01-M08-001",
        "BATCH-SRC-003-M06-006",
        "PASSPORT_RECORDS",
        ["TERMS"],
        [_record()],
    )
    assert result["type"] == "RECONCILIATION_RESULT"
    assert result["records"][0]["match_result"] == "NEEDS_REVIEW"
    assert result["summary"] == {
        "total": 1,
        "existing_equivalent": 0,
        "needs_review": 1,
    }
    assert result["boundary"]["admission_decision"] == "NOT_PERFORMED"


def test_existing_equivalent():
    result = build_reconciliation_result(
        "SRC-003",
        "RUN-SRC-003-AUTOMATED-M01-M08-001",
        "BATCH-SRC-003-M06-006",
        "PASSPORT_RECORDS",
        ["TERMS"],
        [
            _record(
                result="EXISTING_EQUIVALENT",
                cmoc_object_id="OBJ-001",
                basis="EXACT match",
            )
        ],
    )
    assert result["records"][0]["cmoc_object_id"] == "OBJ-001"
    assert result["summary"]["existing_equivalent"] == 1


def test_no_match_is_not_new():
    result = build_reconciliation_result(
        "SRC-003",
        "RUN-SRC-003-AUTOMATED-M01-M08-001",
        "BATCH-SRC-003-M06-006",
        "PASSPORT_RECORDS",
        ["TERMS"],
        [_record()],
    )
    assert "NEW" not in result["records"][0]["match_result"]
    assert result["boundary"]["admission_decision"] == "NOT_PERFORMED"


def test_discovery_input_is_not_mutated():
    record = _record()
    before = copy.deepcopy(record)
    build_reconciliation_result(
        "SRC-003",
        "RUN-SRC-003-AUTOMATED-M01-M08-001",
        "BATCH-SRC-003-M06-006",
        "PASSPORT_RECORDS",
        ["TERMS"],
        [record],
    )
    assert record == before


def test_unsupported_decision_rejected():
    try:
        build_reconciliation_result(
            "SRC-003",
            "RUN-SRC-003-AUTOMATED-M01-M08-001",
            "BATCH-SRC-003-M06-006",
            "PASSPORT_RECORDS",
            ["TERMS"],
            [_record(result="NEW")],
        )
    except ReconciliationResultError:
        return
    raise AssertionError("NEW must not be accepted by v0.1")


if __name__ == "__main__":
    tests = [
        test_needs_review,
        test_existing_equivalent,
        test_no_match_is_not_new,
        test_discovery_input_is_not_mutated,
        test_unsupported_decision_rejected,
    ]
    for test in tests:
        test()
    print("RECONCILIATION RESULT TEST: PASS")
