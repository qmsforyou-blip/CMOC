#!/usr/bin/env python3
"""Acceptance test for the P7 CMOC object registration boundary."""
from __future__ import annotations

import copy
import hashlib
import json
import tempfile
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))

from production_cmoc_writer import ProductionCmocWriter


def payload():
    candidate = {
        "record_id": "REC-P7-REG-001",
        "value": "Registered CMOC test object",
        "object_type": "REQUIREMENT",
        "canonical_name": "Registered CMOC test object",
    }
    raw = json.dumps(candidate, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return {
        "status": "CANONICALIZATION_READY",
        "run_id": "RUN-P7-REG-001",
        "source_id": "SRC-P7-REG-001",
        "batch_id": "BATCH-P7-REG-001",
        "stage_id": "C2_CMOC_WRITE",
        "attempt_id": "ATT-P7-REG-001",
        "result_id": "RESULT-P7-REG-001",
        "object_id": "OBJ-P7-REG-001",
        "object_type": "REQUIREMENT",
        "canonical_name": "Registered CMOC test object",
        "canonical_representation": candidate,
        "provenance": {"source_id": "SRC-P7-REG-001", "basis": "P7 boundary test"},
        "traceability": {"run_id": "RUN-P7-REG-001", "record_id": "REC-P7-REG-001"},
        "new_evidence_ref": "NEW-EVIDENCE-P7-REG-001",
        "approved_candidate_hash": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
    }


def test_p7_registration_boundary():
    with tempfile.TemporaryDirectory(prefix="cmoc-p7-registration-") as tmp:
        root = Path(tmp)
        writer = ProductionCmocWriter(root)
        original = payload()

        first = writer.write(original)
        assert first.status == "CMOC_WRITE_ACCEPTED"
        assert first.object_id == original["object_id"]

        target = root / f"{original['object_id']}.md"
        assert target.exists()
        text = target.read_text(encoding="utf-8")
        assert "<CMOC_JSON>" in text

        second = writer.write(copy.deepcopy(original))
        assert second.status == "ALREADY_PERSISTED"

        changed = copy.deepcopy(original)
        changed["canonical_name"] = "Changed representation"
        third = writer.write(changed)
        assert third.status == "EXISTING_OBJECT_WRITE_CONFLICT"

        invalid = copy.deepcopy(original)
        invalid["status"] = "NEW_APPROVED"
        rejected = writer.write(invalid)
        assert rejected.status == "CMOC_WRITE_REJECTED"

        # P7 must not create or mutate an OBJECT INDEX.
        assert not (root / "cmoc_object_index.json").exists()


if __name__ == "__main__":
    test_p7_registration_boundary()
    print("P7 CMOC OBJECT REGISTRATION BOUNDARY TEST: PASS")
