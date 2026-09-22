from pathlib import Path
from production_object_index_synchronizer import ProductionObjectIndexSynchronizer


ROOT = Path(__file__).resolve().parents[1]


def payload(object_id="OC-0001"):
    return {
        "status": "CMOC_WRITE_ACCEPTED",
        "run_id": "RUN-P8-RT-001",
        "source_id": "SRC-P8-RT-001",
        "batch_id": "BATCH-P8-RT-001",
        "stage_id": "C2_CMOC_WRITE",
        "attempt_id": "ATT-P8-RT-001",
        "result_id": "WRITE-P8-RT-001",
        "cmoc_write_id": "CMOC-WRITE-P8-RT-001",
        "object_id": object_id,
        "provenance": "P8-RUNTIME-PRODUCTION",
        "traceability": "RUN-P8-RT-001/CMOC-WRITE-P8-RT-001",
        "write_verification": True,
    }


def main():
    sync = ProductionObjectIndexSynchronizer(ROOT)

    # P8-RT-01: real deterministic builder check.
    out = sync.synchronize(payload())
    assert out.status == "ALREADY_SYNCHRONIZED"
    assert out.object_id == "OC-0001"
    assert out.verification["builder_check"]["check"] == "PASS"

    # P8-RT-02: identity is physically present in the real index.
    assert out.verification["representation_count"] > 0
    assert out.verification["object_id_match"] is True

    # P8-RT-03: the production index is not mutated by synchronization.
    assert out.verification["index_bytes_unchanged"] is True

    # P8-RT-04: repeat is idempotent.
    repeat = sync.synchronize(payload())
    assert repeat.status == "ALREADY_SYNCHRONIZED"
    assert repeat.verification["builder_check"] == out.verification["builder_check"]

    # P8-RT-05: non-authoritative predecessor is rejected.
    invalid = payload()
    invalid["status"] = "CMOC_WRITE_REJECTED"
    assert sync.synchronize(invalid).status == "INDEX_REJECTED"

    # P8-RT-06: missing write verification is rejected.
    invalid = payload()
    invalid["write_verification"] = False
    assert sync.synchronize(invalid).status == "INDEX_REJECTED"

    # P8-RT-07: wrong predecessor stage is rejected.
    invalid = payload()
    invalid["stage_id"] = "C1_CANONIZATION"
    assert sync.synchronize(invalid).status == "INDEX_REJECTED"

    # P8-RT-08: missing object is distinguishable from semantic NEW.
    missing = sync.synchronize(payload("OBJ-P8-RUNTIME-NOT-IN-INDEX"))
    assert missing.status == "INDEX_MISSING_OBJECT"
    assert "NEW" not in (missing.basis or "")

    # P8-RT-09: foreign RUN lineage is structurally rejected by this boundary.
    invalid = payload()
    invalid["run_id"] = ""
    assert sync.synchronize(invalid).status == "INDEX_REJECTED"

    # P8-RT-10: required traceability is enforced.
    invalid = payload()
    invalid["traceability"] = ""
    assert sync.synchronize(invalid).status == "INDEX_REJECTED"

    # P8-RT-11: no semantic responsibilities are exposed.
    assert not hasattr(sync, "new_decision")
    assert not hasattr(sync, "semantic_compare")
    assert not hasattr(sync, "canonize")
    assert not hasattr(sync, "write_cmoc")

    # P8-RT-12: canonical CMOC remains upstream/authoritative.
    assert not hasattr(sync, "mutate_cmoc")

    print("RUNTIME PRODUCTION OBJECT INDEX SYNCHRONIZATION TEST: PASS")


if __name__ == "__main__":
    main()
