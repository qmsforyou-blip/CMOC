from pathlib import Path
from copy import deepcopy
import shutil
import tempfile

from production_cmoc_writer import ProductionCmocWriter


def canonical_payload():
    return {
        "status": "CANONICALIZATION_READY",
        "run_id": "RUN-P7-RT-001",
        "source_id": "SRC-P7-RT-001",
        "batch_id": "BATCH-P7-RT-001",
        "stage_id": "C2_CMOC_WRITE",
        "attempt_id": "ATT-P7-RT-001",
        "result_id": "CANON-P7-RT-001",
        "object_id": "OBJ-P7-RT-001",
        "object_type": "DISTINCTION",
        "canonical_name": "P7 Runtime Test Distinction",
        "canonical_representation": {
            "boundary": "isolated runtime persistence target",
            "provenance": "P7-RUNTIME-CANONICALIZATION",
            "traceability": "RUN-P7-RT-001/CANON-P7-RT-001",
        },
        "provenance": "P7-RUNTIME-CANONICALIZATION",
        "traceability": "RUN-P7-RT-001/CANON-P7-RT-001",
        "new_evidence_ref": "R10-P7-RT-NEW-APPROVED",
        "approved_candidate_hash": "P7-RT-INTEGRITY-001",
        "unsupported_relations": [],
    }


def test_production_cmoc_writer():
    root = Path(tempfile.mkdtemp(prefix="cmoc-p7-runtime-"))
    try:
        writer = ProductionCmocWriter(root)
        payload = canonical_payload()
        original = deepcopy(payload)

        # P7-RT-01: real physical persistence.
        out = writer.write(payload)
        assert out.status == "CMOC_WRITE_ACCEPTED"
        target = root / f"{payload['object_id']}.md"
        assert target.exists()

        # P7-RT-02: read-back verification preserves representation and lineage.
        persisted = writer._decode(target.read_text(encoding="utf-8"))
        assert persisted == payload
        assert persisted["object_id"] == payload["object_id"]
        assert persisted["provenance"] == payload["provenance"]
        assert persisted["traceability"] == payload["traceability"]

        # P7-RT-03: integrity anchor is preserved.
        assert persisted["approved_candidate_hash"] == payload["approved_candidate_hash"]

        # P7-RT-04: duplicate invocation is idempotent.
        assert writer.write(payload).status == "ALREADY_PERSISTED"

        # P7-RT-05: same identity, different representation is never overwritten.
        conflict = deepcopy(payload)
        conflict["canonical_representation"] = {
            "boundary": "conflicting representation",
            "provenance": payload["provenance"],
            "traceability": payload["traceability"],
        }
        assert writer.write(conflict).status == "EXISTING_OBJECT_WRITE_CONFLICT"
        assert writer._decode(target.read_text(encoding="utf-8")) == payload

        # P7-RT-06: incomplete input is rejected before persistence.
        incomplete = deepcopy(payload)
        incomplete.pop("provenance")
        target.unlink()
        assert writer.write(incomplete).status == "CMOC_WRITE_REJECTED"
        assert not target.exists()

        # Restore valid target.
        assert writer.write(payload).status == "CMOC_WRITE_ACCEPTED"

        # P7-RT-07: wrong entry state is rejected.
        invalid = deepcopy(payload)
        invalid["status"] = "NEW_APPROVED"
        target.unlink()
        assert writer.write(invalid).status == "CMOC_WRITE_REJECTED"
        assert not target.exists()

        # P7-RT-08: unsupported relations are rejected.
        related = deepcopy(payload)
        related["unsupported_relations"] = [{"relation": "UNSUPPORTED"}]
        assert writer.write(related).status == "CMOC_WRITE_REJECTED"
        assert not target.exists()

        # Restore valid target again.
        assert writer.write(payload).status == "CMOC_WRITE_ACCEPTED"

        # P7-RT-09: input is preserved.
        assert payload == original

        # P7-RT-10: writer exposes only persistence responsibility.
        assert not hasattr(writer, "new_decision")
        assert not hasattr(writer, "semantic_compare")
        assert not hasattr(writer, "canonize")
        assert not hasattr(writer, "object_index_sync")

        # P7-RT-11: object identity is physically bounded to target_root.
        assert target.parent == root
        assert target.name == "OBJ-P7-RT-001.md"

        # P7-RT-12: target can be removed cleanly after the gate.
        shutil.rmtree(root)
        assert not root.exists()

        print("RUNTIME PRODUCTION CMOC WRITE TEST: PASS")
    finally:
        if root.exists():
            shutil.rmtree(root)


if __name__ == "__main__":
    test_production_cmoc_writer()
