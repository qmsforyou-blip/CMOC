#!/usr/bin/env python3
"""End-to-end DECISION -> STORE -> ADMISSION -> STORE -> C1 boundary test."""
from __future__ import annotations

import copy
import tempfile
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from decision import build_decision  # noqa: E402
from decision_store import DecisionStore  # noqa: E402
from admission import admit_existing, admit_new, execute_c1_from_admission  # noqa: E402
from admission_store import AdmissionStore  # noqa: E402


def _reconciliation(match_result, cmoc_object_id=None, match_id="MAT-001"):
    return {
        "match_id": match_id,
        "source_id": "SRC-003",
        "cmoc_object_id": cmoc_object_id,
        "match_result": match_result,
        "traceability": {
            "source_id": "SRC-003",
            "discovery_run": "RUN-E2E-001",
            "reconciliation_id": "RECON-E2E-001",
            "match_id": match_id,
            "input_record_id": "REC-001",
        },
    }


def _decision(result, reconciliation):
    return build_decision(
        f"DEC-{reconciliation['match_id']}",
        "HUMAN",
        result,
        reconciliation,
        "explicit human decision basis",
        decided_by="operator-001",
        decided_at="2026-09-24T16:00:00+05:00",
    )


def test_existing_path_end_to_end():
    reconciliation = _reconciliation(
        "EXISTING_EQUIVALENT",
        cmoc_object_id="T-0001",
        match_id="MAT-EXISTING",
    )
    decision = _decision("ADMIT_EXISTING", reconciliation)

    with tempfile.TemporaryDirectory() as tmp:
        decision_store = DecisionStore(Path(tmp) / "decisions")
        admission_store = AdmissionStore(Path(tmp) / "admissions")

        assert decision_store.write(decision) == "PERSISTED"
        restored_decision = decision_store.read("DEC-MAT-EXISTING")

        admission = admit_existing(restored_decision)
        assert admission["admission"]["target_cmoc_object_id"] == "T-0001"

        assert admission_store.write(admission) == "PERSISTED"
        restored_admission = admission_store.read(
            admission["admission"]["admission_id"]
        )

        assert restored_admission == admission
        assert restored_admission["admission"]["admission_result"] == "ADMIT_EXISTING"
        assert restored_admission["boundary"]["cmoc_write"] == "NONE"
        assert restored_admission["boundary"]["object_index_write"] == "NONE"


def test_new_path_end_to_end_to_c1_boundary():
    reconciliation = _reconciliation(
        "NEEDS_REVIEW",
        match_id="MAT-NEW",
    )
    decision = _decision("ADMIT_NEW", reconciliation)

    with tempfile.TemporaryDirectory() as tmp:
        decision_store = DecisionStore(Path(tmp) / "decisions")
        admission_store = AdmissionStore(Path(tmp) / "admissions")

        assert decision_store.write(decision) == "PERSISTED"
        restored_decision = decision_store.read("DEC-MAT-NEW")

        admission = admit_new(restored_decision)
        assert admission["admission"]["pipeline_status"] == "PENDING_C1"

        assert admission_store.write(admission) == "PERSISTED"
        restored_admission = admission_store.read(
            admission["admission"]["admission_id"]
        )

        approved_candidate = {
            "decision_result": "NEW_APPROVED",
            "candidate_id": "CAND-001",
            "source_id": "SRC-003",
            "canonical_name": "Test Object",
            "object_type": "TERM",
        }
        candidate_before = copy.deepcopy(approved_candidate)

        c1_input = execute_c1_from_admission(
            restored_admission,
            approved_candidate,
        )

        assert approved_candidate == candidate_before
        assert c1_input["decision_result"] == "NEW_APPROVED"
        assert c1_input["admission_id"] == restored_admission["admission"]["admission_id"]
        assert c1_input["decision_id"] == "DEC-MAT-NEW"
        assert c1_input["match_id"] == "MAT-NEW"
        assert c1_input["source_id"] == "SRC-003"


def test_storage_does_not_execute_downstream():
    reconciliation = _reconciliation(
        "NEEDS_REVIEW",
        match_id="MAT-NO-DOWNSTREAM",
    )
    decision = _decision("DEFER", reconciliation)

    with tempfile.TemporaryDirectory() as tmp:
        decision_store = DecisionStore(Path(tmp) / "decisions")
        admission_store = AdmissionStore(Path(tmp) / "admissions")

        assert decision_store.write(decision) == "PERSISTED"
        assert not list((Path(tmp) / "admissions").glob("*.json"))

        assert decision_store.read("DEC-MAT-NO-DOWNSTREAM") == decision
        assert not list((Path(tmp) / "admissions").glob("*.json"))


def test_decision_and_admission_payloads_remain_unchanged():
    reconciliation = _reconciliation(
        "EXISTING_EQUIVALENT",
        cmoc_object_id="T-0001",
        match_id="MAT-IMMUTABLE",
    )
    decision = _decision("ADMIT_EXISTING", reconciliation)
    decision_before = copy.deepcopy(decision)

    with tempfile.TemporaryDirectory() as tmp:
        decision_store = DecisionStore(Path(tmp) / "decisions")
        admission_store = AdmissionStore(Path(tmp) / "admissions")

        decision_store.write(decision)
        restored_decision = decision_store.read("DEC-MAT-IMMUTABLE")
        admission = admit_existing(restored_decision)
        admission_before = copy.deepcopy(admission)
        admission_store.write(admission)
        restored_admission = admission_store.read(
            admission["admission"]["admission_id"]
        )

        assert decision == decision_before
        assert admission == admission_before
        assert restored_admission == admission_before


if __name__ == "__main__":
    tests = [
        test_existing_path_end_to_end,
        test_new_path_end_to_end_to_c1_boundary,
        test_storage_does_not_execute_downstream,
        test_decision_and_admission_payloads_remain_unchanged,
    ]
    for test in tests:
        test()
    print("DECISION -> STORE -> ADMISSION -> STORE -> C1 E2E TEST: PASS")
