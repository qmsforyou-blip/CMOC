#!/usr/bin/env python3
"""Acceptance tests for DECISION-STORAGE-CONTRACT-001 v0.1."""
from __future__ import annotations

import copy
import json
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from decision import build_decision  # noqa: E402
from decision_store import DecisionStore, DecisionStoreError  # noqa: E402


def _decision(result="DEFER"):
    return build_decision(
        "DEC-001",
        "HUMAN",
        result,
        {
            "match_id": "MAT-001",
            "source_id": "SRC-003",
            "cmoc_object_id": "OBJ-001" if result == "ADMIT_EXISTING" else None,
            "match_result": "EXISTING_EQUIVALENT" if result == "ADMIT_EXISTING" else "NEEDS_REVIEW",
            "traceability": {
                "source_id": "SRC-003",
                "discovery_run": "RUN-001",
                "reconciliation_id": "RECON-001",
                "match_id": "MAT-001",
            },
        },
        "explicit human basis",
        decided_by="operator-001",
        decided_at="2026-09-24T09:00:00+02:00",
    )


def test_write_and_read():
    with tempfile.TemporaryDirectory() as tmp:
        store = DecisionStore(tmp)
        artifact = _decision()
        assert store.write(artifact) == "PERSISTED"
        assert store.read("DEC-001") == artifact


def test_idempotent_repeat():
    with tempfile.TemporaryDirectory() as tmp:
        store = DecisionStore(tmp)
        artifact = _decision()
        assert store.write(artifact) == "PERSISTED"
        assert store.write(artifact) == "ALREADY_PERSISTED"
        assert len(list(Path(tmp).glob("*.json"))) == 1


def test_conflicting_rewrite_rejected():
    with tempfile.TemporaryDirectory() as tmp:
        store = DecisionStore(tmp)
        artifact = _decision()
        assert store.write(artifact) == "PERSISTED"
        changed = copy.deepcopy(artifact)
        changed["decision"]["basis"] = "changed basis"
        try:
            store.write(changed)
        except DecisionStoreError as exc:
            assert str(exc) == "DECISION_WRITE_CONFLICT"
        else:
            raise AssertionError("conflicting rewrite must be rejected")


def test_invalid_artifact_rejected():
    with tempfile.TemporaryDirectory() as tmp:
        store = DecisionStore(tmp)
        try:
            store.write({"type": "NOT_DECISION"})
        except DecisionStoreError as exc:
            assert str(exc) == "DECISION_TYPE_MISMATCH"
        else:
            raise AssertionError("invalid artifact must be rejected")


def test_missing_decision_rejected():
    with tempfile.TemporaryDirectory() as tmp:
        store = DecisionStore(tmp)
        try:
            store.read("DEC-404")
        except DecisionStoreError as exc:
            assert str(exc) == "DECISION_NOT_FOUND"
        else:
            raise AssertionError("missing Decision must be rejected")


def test_storage_does_not_add_downstream_objects():
    with tempfile.TemporaryDirectory() as tmp:
        store = DecisionStore(tmp)
        artifact = _decision("ADMIT_EXISTING")
        assert store.write(artifact) == "PERSISTED"
        files = {p.name for p in Path(tmp).iterdir()}
        assert files == {"DEC-001.json"}
        saved = json.loads((Path(tmp) / "DEC-001.json").read_text(encoding="utf-8"))
        assert saved["boundary"]["cmoc_write"] == "NONE"
        assert saved["boundary"]["object_index_write"] == "NONE"
        assert saved["boundary"]["admission_execution"] == "NOT_PERFORMED"


if __name__ == "__main__":
    tests = [
        test_write_and_read,
        test_idempotent_repeat,
        test_conflicting_rewrite_rejected,
        test_invalid_artifact_rejected,
        test_missing_decision_rejected,
        test_storage_does_not_add_downstream_objects,
    ]
    for test in tests:
        test()
    print("DECISION STORAGE CONTRACT TEST: PASS")
