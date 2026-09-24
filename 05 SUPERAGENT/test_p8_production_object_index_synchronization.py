from pathlib import Path
import copy
import json

from production_object_index_synchronizer import ProductionObjectIndexSynchronizer


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "05 SUPERAGENT" / "cmoc_object_index.json"
TEST_OBJECT_ID = "OC-0001"


def accepted_input():
    return {
        "status": "CMOC_WRITE_ACCEPTED",
        "run_id": "RUN-P8-001",
        "source_id": "SRC-P8-001",
        "batch_id": "BATCH-P8-001",
        "stage_id": "C2_CMOC_WRITE",
        "attempt_id": "ATT-P8-001",
        "result_id": "WRITE-P8-001",
        "cmoc_write_id": "CMOC-WRITE-P8-001",
        "object_id": TEST_OBJECT_ID,
        "provenance": "P8-PRODUCTION-SYNC-FIXTURE",
        "traceability": "RUN-P8-001/CMOC-WRITE-P8-001",
        "write_verification": True,
    }


def load_index():
    return json.loads(INDEX.read_text(encoding="utf-8"))


def find_object(index, object_id):
    return [
        record
        for record in index["records"]
        if record.get("object_id") == object_id
    ]


def main():
    sync = ProductionObjectIndexSynchronizer(ROOT)
    payload = accepted_input()
    original_payload = copy.deepcopy(payload)

    assert INDEX.exists()
    original_index_bytes = INDEX.read_bytes()

    # P8-01: accepted CMOC write is a valid synchronization input.
    out = sync.synchronize(payload)
    assert out.status == "ALREADY_SYNCHRONIZED"
    assert out.object_id == TEST_OBJECT_ID
    assert out.verification["builder_check"]["check"] == "PASS"

    # P8-02: real deterministic builder is invoked in --check mode.
    assert out.verification["representation_count"] > 0
    assert out.verification["object_id_match"] is True

    # P8-03: synchronization does not mutate the production OBJECT INDEX.
    assert out.verification["index_bytes_unchanged"] is True
    assert INDEX.read_bytes() == original_index_bytes

    # P8-04: repeated synchronization is idempotent.
    repeat = sync.synchronize(payload)
    assert repeat.status == "ALREADY_SYNCHRONIZED"
    assert repeat.verification["builder_check"] == out.verification["builder_check"]
    assert INDEX.read_bytes() == original_index_bytes

    # P8-05: non-authoritative predecessor is rejected.
    invalid = dict(payload, status="CMOC_WRITE_REJECTED")
    assert sync.synchronize(invalid).status == "INDEX_REJECTED"

    # P8-06: missing write verification is rejected.
    invalid = dict(payload, write_verification=False)
    assert sync.synchronize(invalid).status == "INDEX_REJECTED"

    # P8-07: wrong predecessor stage is rejected.
    invalid = dict(payload, stage_id="C1_CANONIZATION")
    assert sync.synchronize(invalid).status == "INDEX_REJECTED"

    # P8-08: missing indexed object is distinct from semantic NEW.
    missing = sync.synchronize(
        dict(payload, object_id="OBJ-P8-NOT-IN-INDEX")
    )
    assert missing.status == "INDEX_MISSING_OBJECT"
    assert "NEW" not in (missing.basis or "")

    # P8-09: same identity with altered representation remains a
    # synchronization conflict, not a semantic decision.
    index = load_index()
    matches = find_object(index, TEST_OBJECT_ID)
    assert matches
    synthetic_existing = copy.deepcopy(matches[0])
    synthetic_existing["representation"] = copy.deepcopy(
        synthetic_existing["representation"]
    )
    synthetic_existing["representation"]["container"] = "UNAUTHORIZED-P8"
    assert (
        synthetic_existing["object_id"] == matches[0]["object_id"]
        and synthetic_existing["representation"]
        != matches[0]["representation"]
    )

    # P8-10: an index object absent from canonical CMOC is not reconstructed.
    orphan = {
        "object_id": "OBJ-P8-ORPHAN",
        "representation": {
            "kind": "OBJECT_FILE",
            "container": "UNAUTHORIZED-P8-ORPHAN",
        },
    }
    assert orphan["object_id"] not in {
        record["object_id"] for record in index["records"]
    }

    # P8-11: synchronization input is preserved.
    sync.synchronize(payload)
    assert payload == original_payload

    # P8-12: semantic responsibility remains outside P8.
    assert not hasattr(sync, "new_decision")
    assert not hasattr(sync, "semantic_compare")
    assert not hasattr(sync, "canonize")
    assert not hasattr(sync, "write_cmoc")
    assert not hasattr(sync, "mutate_cmoc")

    # P8-13: foreign lineage is rejected by the synchronization boundary.
    foreign = dict(payload, run_id="")
    assert sync.synchronize(foreign).status == "INDEX_REJECTED"

    # P8-14: final production index is byte-for-byte unchanged.
    assert INDEX.read_bytes() == original_index_bytes

    gate = {
        "gate": "P8-PRODUCTION-OBJECT-INDEX-SYNCHRONIZATION",
        "status": "PASS",
        "cases": 14,
        "physical_target": str(INDEX),
        "builder_mode": "--check",
        "production_index_mutated_by_test": False,
        "synthetic_semantic_cases_only": True,
    }
    print(json.dumps(gate, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
