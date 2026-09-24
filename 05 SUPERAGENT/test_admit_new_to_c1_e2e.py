#!/usr/bin/env python3
"""Acceptance test for ADMIT_NEW -> C1 -> CANONICALIZATION_READY."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from admission import admit_new, execute_c1_from_admission
from c1_canonization import canonize


def _decision():
    return {
        "type": "DECISION",
        "decision": {
            "decision_id": "DEC-E2E-001",
            "decision_type": "HUMAN",
            "decision_result": "ADMIT_NEW",
            "match_id": "MAT-E2E-001",
            "basis": "Explicit human admission after NEW decision",
            "source_id": "SRC-003",
            "traceability": {
                "source_id": "SRC-003",
                "discovery_run": "RUN-E2E-001",
                "reconciliation_id": "RECON-E2E-001",
                "match_id": "MAT-E2E-001",
            },
            "decided_by": "operator-001",
            "decided_at": "2026-09-24T10:00:00+02:00",
            "rule_id": None,
            "rule_version": None,
        },
    }


def _approved_candidate():
    candidate = {
        "record_id": "REC-E2E-001",
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
            "discovery_run": "RUN-E2E-001",
        },
        "traceability": {
            "source_id": "SRC-003",
            "match_id": "MAT-E2E-001",
        },
        "approved_candidate_hash": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
        "new_evidence_ref": "NEW-EVIDENCE-E2E-001",
    }


def test_admit_new_to_c1_to_canonicalization_ready():
    admission = admit_new(_decision())
    c1_input = execute_c1_from_admission(admission, _approved_candidate())
    out = canonize(c1_input)

    assert admission["admission"]["pipeline_status"] == "PENDING_C1"
    assert out["status"] == "CANONICALIZATION_READY"
    assert out["object_id"].startswith("OBJ-")
    assert out["boundary"]["canonization"] == "PERFORMED"
    assert out["boundary"]["cmoc_write"] == "NONE"
    assert out["boundary"]["object_index_write"] == "NONE"


if __name__ == "__main__":
    test_admit_new_to_c1_to_canonicalization_ready()
    print("ADMIT_NEW -> C1 -> CANONICALIZATION_READY: PASS")
