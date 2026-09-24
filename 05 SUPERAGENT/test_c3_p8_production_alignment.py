#!/usr/bin/env python3
"""Acceptance test for C3 contract against the production P8 runtime boundary."""
from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))

from production_object_index_synchronizer import ProductionObjectIndexSynchronizer


ROOT = Path(__file__).resolve().parents[1]


def payload():
    return {
        "status": "CMOC_WRITE_ACCEPTED",
        "run_id": "RUN-C3-P8-001",
        "source_id": "SRC-C3-P8-001",
        "batch_id": "BATCH-C3-P8-001",
        "stage_id": "C2_CMOC_WRITE",
        "attempt_id": "ATT-C3-P8-001",
        "result_id": "RESULT-C3-P8-001",
        "cmoc_write_id": "CMOC-WRITE-C3-P8-001",
        "object_id": "OC-0001",
        "provenance": "C3-P8-CONTRACT-CHECK",
        "traceability": "RUN-C3-P8-001/CMOC-WRITE-C3-P8-001",
        "write_verification": True,
    }


def test_c3_production_alignment():
    sync = ProductionObjectIndexSynchronizer(ROOT)
    out = sync.synchronize(payload())

    assert out.status == "ALREADY_SYNCHRONIZED"
    assert out.object_id == payload()["object_id"]
    assert out.verification["builder_check"]["check"] == "PASS"
    assert out.verification["object_id_match"] is True
    assert out.verification["index_bytes_unchanged"] is True

    # Contract/runtime responsibility isolation.
    assert not hasattr(sync, "new_decision")
    assert not hasattr(sync, "semantic_compare")
    assert not hasattr(sync, "canonize")
    assert not hasattr(sync, "write_cmoc")
    assert not hasattr(sync, "mutate_cmoc")


if __name__ == "__main__":
    test_c3_production_alignment()
    print("C3 CONTRACT -> P8 PRODUCTION ALIGNMENT: PASS")
