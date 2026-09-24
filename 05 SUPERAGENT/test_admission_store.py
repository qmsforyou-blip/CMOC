#!/usr/bin/env python3
"""Acceptance tests for ADMISSION-STORAGE-CONTRACT-001 v0.1."""
from __future__ import annotations

import copy
import json
import tempfile
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))

from admission import admit_existing, admit_new  # noqa: E402
from admission_store import AdmissionStore, AdmissionStoreError  # noqa: E402


def _existing_admission():
    return admit_existing({
        "type": "DECISION",
        "decision": {
            "decision_id": "DEC-001",
            "decision_result": "ADMIT_EXISTING",
            "match_id": "MAT-001",
            "source_id": "SRC-003",
            "cmoc_object_id": "T-0001",
            "decided_at": "2026-09-24T15:00:00+05:00",
            "traceability": {
                "source_id": "SRC-003",
                "discovery_run": "RUN-001",
                "reconciliation_id": "RECON-001",
                "match_id": "MAT-001",
            },
        },
    })


def _new_admission():
    return admit_new({
        "type": "DECISION",
        "decision": {
            "decision_id": "DEC-002",
            "decision_result": "ADMIT_NEW",
            "match_id": "MAT-002",
            "source_id": "SRC-003",
            "cmoc_object_id": None,
            "basis": "NEW_APPROVED_BY_HUMAN",
            "decided_at": "2026-09-24T15:05:00+05:00",
            "traceability": {
                "source_id": "SRC-003",
                "discovery_run": "RUN-001",
                "reconciliation_id": "RECON-002",
                "match_id": "MAT-002",
            },
        },
    })


def test_write_and_read():
    with tempfile.TemporaryDirectory() as tmp:
        store = AdmissionStore(tmp)
        artifact = _existing_admission()
        assert store.write(artifact) == "PERSISTED"
        assert store.read(artifact["admission"]["admission_id"]) == artifact


def test_idempotent_repeat():
    with tempfile.TemporaryDirectory() as tmp:
        store = AdmissionStore(tmp)
        artifact = _existing_admission()
        assert store.write(artifact) == "PERSISTED"
        assert store.write(artifact) == "ALREADY_PERSISTED"
        assert len(list(Path(tmp).glob("*.json"))) == 1


def test_conflicting_rewrite_rejected():
    with tempfile.TemporaryDirectory() as tmp:
        store = AdmissionStore(tmp)
        artifact = _existing_admission()
        assert store.write(artifact) == "PERSISTED"

        changed = copy.deepcopy(artifact)
        changed["admission"]["source_id"] = "SRC-CHANGED"

        try:
            store.write(changed)
        except AdmissionStoreError as exc:
            assert str(exc) == "ADMISSION_WRITE_CONFLICT"
        else:
            raise AssertionError("conflicting rewrite must be rejected")


def test_invalid_artifact_rejected():
    with tempfile.TemporaryDirectory() as tmp:
        store = AdmissionStore(tmp)
        for artifact, expected in (
            ({"type": "DECISION"}, "ADMISSION_TYPE_MISMATCH"),
            ({"type": "ADMISSION"}, "ADMISSION_BODY_MISSING"),
            (None, "ADMISSION_NOT_OBJECT"),
        ):
            try:
                store.write(artifact)
            except AdmissionStoreError as exc:
                assert str(exc) == expected
            else:
                raise AssertionError(f"expected {expected}")


def test_missing_admission_rejected():
    with tempfile.TemporaryDirectory() as tmp:
        store = AdmissionStore(tmp)
        try:
            store.read("ADM-404")
        except AdmissionStoreError as exc:
            assert str(exc) == "ADMISSION_NOT_FOUND"
        else:
            raise AssertionError("missing Admission must be rejected")


def test_new_admission_status_preserved():
    with tempfile.TemporaryDirectory() as tmp:
        store = AdmissionStore(tmp)
        artifact = _new_admission()
        assert artifact["admission"]["pipeline_status"] == "PENDING_C1"

        assert store.write(artifact) == "PERSISTED"
        saved = store.read(artifact["admission"]["admission_id"])

        assert saved["admission"]["pipeline_status"] == "PENDING_C1"
        assert saved["boundary"]["canonization_execution"] == "NOT_PERFORMED"
        assert saved["boundary"]["c1_c2_c3_execution"] == "NOT_PERFORMED"


def test_storage_does_not_execute_downstream():
    with tempfile.TemporaryDirectory() as tmp:
        store = AdmissionStore(tmp)
        artifact = _new_admission()

        assert store.write(artifact) == "PERSISTED"
        files = {p.name for p in Path(tmp).iterdir()}
        assert files == {artifact["admission"]["admission_id"] + ".json"}

        saved = json.loads(
            (Path(tmp) / (artifact["admission"]["admission_id"] + ".json"))
            .read_text(encoding="utf-8")
        )
        assert saved["boundary"]["cmoc_write"] == "NONE"
        assert saved["boundary"]["object_index_write"] == "NONE"
        assert saved["boundary"]["c1_c2_c3_execution"] == "NOT_PERFORMED"


if __name__ == "__main__":
    tests = [
        test_write_and_read,
        test_idempotent_repeat,
        test_conflicting_rewrite_rejected,
        test_invalid_artifact_rejected,
        test_missing_admission_rejected,
        test_new_admission_status_preserved,
        test_storage_does_not_execute_downstream,
    ]
    for test in tests:
        test()
    print("ADMISSION STORAGE CONTRACT TEST: PASS")
