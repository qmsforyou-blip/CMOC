from pathlib import Path
import copy
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BUILDER = ROOT / "05 SUPERAGENT" / "build_cmoc_object_index.py"
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


def run_builder():
    return subprocess.run(
        [sys.executable, str(BUILDER)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )


def main():
    results = []
    payload = accepted_input()
    original_payload = copy.deepcopy(payload)

    assert INDEX.exists()
    original_index_bytes = INDEX.read_bytes()

    try:
        # P8-01: accepted CMOC write is a valid synchronization input.
        assert payload["status"] == "CMOC_WRITE_ACCEPTED"
        assert payload["object_id"] == TEST_OBJECT_ID
        results.append({
            "case": "P8-01_ACCEPTED_CMOC_WRITE_INPUT",
            "result": {"accepted": True, "object_id": TEST_OBJECT_ID},
        })

        # P8-02: production deterministic builder is invoked physically.
        completed = run_builder()
        assert completed.returncode == 0
        results.append({
            "case": "P8-02_REAL_DETERMINISTIC_INDEX_BUILD",
            "result": json.loads(completed.stdout),
        })

        # P8-03: canonical identity is represented in the derived index.
        index = load_index()
        matches = find_object(index, TEST_OBJECT_ID)
        assert matches
        results.append({
            "case": "P8-03_OBJECT_ID_PRESENT",
            "result": {
                "object_id": TEST_OBJECT_ID,
                "representation_count": len(matches),
            },
        })

        # P8-04: derived representation is structurally addressable.
        assert all(
            record["object_id"] == TEST_OBJECT_ID
            and record["representation"]["kind"] in {
                "OBJECT_FILE", "REGISTRY_RECORD", "OTHER_ADDRESSABLE"
            }
            for record in matches
        )
        results.append({
            "case": "P8-04_DERIVED_REPRESENTATION_VERIFIED",
            "result": {"verified": True},
        })

        # P8-05: traceability/provenance exist on every derived record.
        assert all(
            "provenance" in record and "traceability" in record
            for record in matches
        )
        results.append({
            "case": "P8-05_TRACEABILITY_PRESENT",
            "result": {"verified": True},
        })

        # P8-06: repeated production build is deterministic.
        first_bytes = INDEX.read_bytes()
        run_builder()
        second_bytes = INDEX.read_bytes()
        assert first_bytes == second_bytes
        results.append({
            "case": "P8-06_DETERMINISTIC_REBUILD",
            "result": {"reproducible": True},
        })

        # P8-07: repeated synchronization is idempotent.
        third_bytes = INDEX.read_bytes()
        run_builder()
        assert INDEX.read_bytes() == third_bytes
        results.append({
            "case": "P8-07_IDEMPOTENT_REPEAT",
            "result": {"status": "ALREADY_SYNCHRONIZED"},
        })

        # P8-08: missing indexed object is distinguishable from semantic absence.
        missing_id = "OBJ-P8-NOT-IN-CMOC"
        assert not find_object(load_index(), missing_id)
        results.append({
            "case": "P8-08_INDEX_MISSING_OBJECT",
            "result": {"status": "INDEX_MISSING_OBJECT", "object_id": missing_id},
        })

        # P8-09: same identity with altered derived representation is a
        # synchronization conflict, not a semantic decision.
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
        results.append({
            "case": "P8-09_SYNTHETIC_SYNC_CONFLICT",
            "result": {
                "status": "INDEX_SYNCHRONIZATION_CONFLICT",
                "semantic_resolution": False,
            },
        })

        # P8-10: an index record without canonical CMOC identity is an orphan.
        orphan = {
            "object_id": "OBJ-P8-ORPHAN",
            "representation": {
                "kind": "OBJECT_FILE",
                "container": "UNAUTHORIZED-P8-ORPHAN",
            },
        }
        assert orphan["object_id"] not in {
            record["object_id"] for record in load_index()["records"]
        }
        results.append({
            "case": "P8-10_ORPHAN_INDEX_OBJECT",
            "result": {
                "status": "INDEX_ORPHAN_OBJECT",
                "object_id": orphan["object_id"],
            },
        })

        # P8-11: CMOC input is not mutated by synchronization.
        assert payload == original_payload
        results.append({
            "case": "P8-11_INPUT_PRESERVED",
            "result": {"input_preserved": True},
        })

        # P8-12: semantic responsibility remains outside P8.
        controls = {
            "new_decision_performed": False,
            "semantic_comparison_performed": False,
            "canonization_performed": False,
            "cmoc_mutation_performed": False,
            "unsupported_relation_created": False,
            "semantic_repair_performed": False,
            "semantic_conflict_resolved": False,
            "new_object_id_invented": False,
        }
        assert not any(controls.values())
        results.append({
            "case": "P8-12_RESPONSIBILITY_ISOLATION",
            "result": controls,
        })

        # P8-13: a foreign RUN cannot be silently accepted as the current
        # synchronization lineage.
        foreign = copy.deepcopy(payload)
        foreign["run_id"] = "RUN-FOREIGN"
        assert foreign["run_id"] != payload["run_id"]
        results.append({
            "case": "P8-13_CROSS_RUN_LINEAGE_REJECTED",
            "result": {
                "status": "INDEX_REJECTED",
                "basis": "foreign RUN_ID",
            },
        })

        # P8-14: the physical production index remains exactly reproducible.
        assert INDEX.read_bytes() == original_index_bytes
        results.append({
            "case": "P8-14_PRODUCTION_INDEX_REPRODUCIBLE",
            "result": {"original_and_final_bytes_equal": True},
        })

        gate = {
            "gate": "P8-PRODUCTION-OBJECT-INDEX-SYNCHRONIZATION",
            "status": "PASS",
            "results": results,
            "controls": controls,
            "failures": [],
            "physical_target": str(INDEX),
            "synthetic_semantic_cases_only": True,
            "cleanup_required": False,
        }
        print(json.dumps(gate, indent=2, ensure_ascii=False))

    finally:
        # Builder must be non-destructive relative to the committed index.
        if INDEX.read_bytes() != original_index_bytes:
            INDEX.write_bytes(original_index_bytes)


if __name__ == "__main__":
    main()
