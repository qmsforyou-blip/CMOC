#!/usr/bin/env python3
"""Acceptance test for C1 -> C2/P7 -> CMOC_WRITE_ACCEPTED."""
from __future__ import annotations

import hashlib
import json
import tempfile
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))

from admission import admit_new, execute_c1_from_admission
from c1_canonization import canonize
from production_cmoc_writer import ProductionCmocWriter


def _decision():
    return {
        "type": "DECISION",
        "decision": {
            "decision_id": "DEC-P7-E2E-001",
            "decision_type": "HUMAN",
            "decision_result": "ADMIT_NEW",
            "match_id": "MAT-P7-E2E-001",
            "basis": "Explicit human admission after NEW decision",
            "source_id": "SRC-003",
            "traceability": {
                "source_id": "SRC-003",
                "discovery_run": "RUN-P7-E2E-001",
                "reconciliation_id": "RECON-P7-E2E-001",
                "match_id": "MAT-P7-E2E-001",
            },
            "decided_by": "operator-001",
            "decided_at": "2026-09-24T10:30:00+02:00",
            "rule_id": None,
            "rule_version": None,
        },
    }


def _approved_candidate():
    candidate = {
        "record_id": "REC-P7-E2E-001",
        "value": "Example approved new object",
        "object_type": "REQUIREMENT",
        "canonical_name": "Example approved new object",
    }
    raw = json.dumps(
        candidate, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    )
    return {
        "decision_result": "NEW_APPROVED",
        "candidate": candidate,
        "provenance": {
            "source_id": "SRC-003",
            "discovery_run": "RUN-P7-E2E-001",
        },
        "traceability": {
            "source_id": "SRC-003",
            "match_id": "MAT-P7-E2E-001",
        },
        "approved_candidate_hash": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
        "new_evidence_ref": "NEW-EVIDENCE-P7-E2E-001",
    }


def test_c1_to_c2_cmoc_write():
    admission = admit_new(_decision())
    c1_input = execute_c1_from_admission(admission, _approved_candidate())
    c1 = canonize(c1_input)

    runtime_payload = {
        **c1,
        "run_id": "RUN-P7-E2E-001",
        "source_id": "SRC-003",
        "batch_id": "BATCH-P7-E2E-001",
        "stage_id": "C2_CMOC_WRITE",
        "attempt_id": "ATTEMPT-P7-E2E-001",
        "result_id": "RESULT-P7-E2E-001",
    }

    with tempfile.TemporaryDirectory(prefix="cmoc-p7-e2e-") as tmp:
        writer = ProductionCmocWriter(Path(tmp))
        result = writer.write(runtime_payload)
        assert result.status == "CMOC_WRITE_ACCEPTED"
        assert result.object_id == c1["object_id"]

        persisted = Path(tmp) / f"{c1['object_id']}.md"
        assert persisted.exists()
        assert "<CMOC_JSON>" in persisted.read_text(encoding="utf-8")

        repeat = writer.write(runtime_payload)
        assert repeat.status == "ALREADY_PERSISTED"

    assert c1["boundary"]["cmoc_write"] == "NONE"


if __name__ == "__main__":
    test_c1_to_c2_cmoc_write()
    print("C1 -> C2/P7 -> CMOC_WRITE_ACCEPTED: PASS")
