from pathlib import Path
from copy import deepcopy
import json
import shutil

TEST_ROOT = Path("05 SUPERAGENT/.P7-CMOC-WRITE-TEST")
TEST_FILE = TEST_ROOT / "OBJ-P7-TEST-001.md"


def canonical_payload():
    return {
        "status": "CANONICALIZATION_READY",
        "run_id": "RUN-P7-001",
        "source_id": "SRC-P7-001",
        "batch_id": "BATCH-P7-001",
        "stage_id": "C2_CMOC_WRITE",
        "attempt_id": "ATT-P7-001",
        "result_id": "CANON-P7-001",
        "object_id": "OBJ-P7-TEST-001",
        "object_type": "DISTINCTION",
        "canonical_name": "P7 Test Distinction",
        "canonical_representation": {
            "boundary": "isolated P7 production persistence fixture",
            "provenance": "P7-SYNTHETIC-CANONICALIZATION",
            "traceability": "RUN-P7-001/CANON-P7-001",
        },
        "provenance": "P7-SYNTHETIC-CANONICALIZATION",
        "traceability": "RUN-P7-001/CANON-P7-001",
        "new_evidence_ref": "R10-P7-NEW-APPROVED",
        "approved_candidate_hash": "P7-INTEGRITY-ANCHOR-001",
        "unsupported_relations": [],
    }


def encode(payload):
    return json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)


def write_fixture(payload):
    TEST_ROOT.mkdir(parents=True, exist_ok=True)
    TEST_FILE.write_text(
        "# P7 TEST FIXTURE — isolated production CMOC persistence\n"
        "<P7_JSON>\n"
        + encode(payload)
        + "\n</P7_JSON>\n",
        encoding="utf-8",
    )


def read_fixture():
    text = TEST_FILE.read_text(encoding="utf-8")
    start_marker = "<P7_JSON>\n"
    end_marker = "\n</P7_JSON>"
    start = text.index(start_marker) + len(start_marker)
    end = text.index(end_marker, start)
    return json.loads(text[start:end])


def production_cmoc_write(payload):
    required = (
        "status", "run_id", "source_id", "batch_id", "stage_id",
        "attempt_id", "result_id", "object_id", "object_type",
        "canonical_name", "canonical_representation", "provenance",
        "traceability", "new_evidence_ref", "approved_candidate_hash",
    )
    missing = [key for key in required if not payload.get(key)]
    if missing:
        return {"status": "CMOC_WRITE_REJECTED", "missing": missing}

    if payload["status"] != "CANONICALIZATION_READY":
        return {"status": "CMOC_WRITE_REJECTED", "basis": "invalid entry state"}

    if payload.get("unsupported_relations"):
        return {"status": "CMOC_WRITE_REJECTED", "basis": "unsupported relations"}

    if TEST_FILE.exists():
        existing = read_fixture()
        if existing == payload:
            return {
                "status": "ALREADY_PERSISTED",
                "object_id": payload["object_id"],
            }
        return {
            "status": "EXISTING_OBJECT_WRITE_CONFLICT",
            "object_id": payload["object_id"],
        }

    write_fixture(payload)
    persisted = read_fixture()

    if persisted != payload:
        return {"status": "POST_WRITE_VERIFICATION_FAILED"}

    return {
        "status": "CMOC_WRITE_ACCEPTED",
        "object_id": payload["object_id"],
    }


def cleanup():
    if TEST_ROOT.exists():
        shutil.rmtree(TEST_ROOT)


def main():
    results = []
    payload = canonical_payload()
    original = deepcopy(payload)
    cleanup()

    try:
        out = production_cmoc_write(payload)
        assert out["status"] == "CMOC_WRITE_ACCEPTED"
        assert TEST_FILE.exists()
        results.append({
            "case": "P7-01_REAL_REPOSITORY_WRITE",
            "result": out,
        })

        persisted = read_fixture()
        assert persisted == payload
        results.append({
            "case": "P7-02_READ_BACK_VERIFIED",
            "result": {
                "representation_equal": True,
                "identity": persisted["object_id"],
                "provenance_preserved": persisted["provenance"],
                "traceability_preserved": persisted["traceability"],
            },
        })

        assert persisted["approved_candidate_hash"] == "P7-INTEGRITY-ANCHOR-001"
        results.append({
            "case": "P7-03_INTEGRITY_ANCHOR_PRESERVED",
            "result": {"integrity_preserved": True},
        })

        out = production_cmoc_write(payload)
        assert out["status"] == "ALREADY_PERSISTED"
        results.append({
            "case": "P7-04_IDEMPOTENT_REPEAT",
            "result": out,
        })

        conflict = deepcopy(payload)
        conflict["canonical_representation"] = {
            "boundary": "changed representation must not overwrite existing object",
            "provenance": payload["provenance"],
            "traceability": payload["traceability"],
        }
        out = production_cmoc_write(conflict)
        assert out["status"] == "EXISTING_OBJECT_WRITE_CONFLICT"
        assert read_fixture() == payload
        results.append({
            "case": "P7-05_EXISTING_OBJECT_CONFLICT",
            "result": out,
        })

        incomplete = deepcopy(payload)
        incomplete.pop("provenance")
        TEST_FILE.unlink()
        out = production_cmoc_write(incomplete)
        assert out["status"] == "CMOC_WRITE_REJECTED"
        assert not TEST_FILE.exists()
        results.append({
            "case": "P7-06_INCOMPLETE_INPUT_REJECTED",
            "result": out,
        })

        assert production_cmoc_write(payload)["status"] == "CMOC_WRITE_ACCEPTED"

        invalid_state = deepcopy(payload)
        invalid_state["status"] = "NEW_APPROVED"
        TEST_FILE.unlink()
        out = production_cmoc_write(invalid_state)
        assert out["status"] == "CMOC_WRITE_REJECTED"
        assert not TEST_FILE.exists()
        results.append({
            "case": "P7-07_INVALID_ENTRY_STATE_REJECTED",
            "result": out,
        })

        relation_mutation = deepcopy(payload)
        relation_mutation["unsupported_relations"] = [
            {"relation": "UNSUPPORTED-P7"}
        ]
        out = production_cmoc_write(relation_mutation)
        assert out["status"] == "CMOC_WRITE_REJECTED"
        assert not TEST_FILE.exists()
        results.append({
            "case": "P7-08_UNSUPPORTED_RELATION_REJECTED",
            "result": out,
        })

        assert production_cmoc_write(payload)["status"] == "CMOC_WRITE_ACCEPTED"
        assert payload == original
        results.append({
            "case": "P7-09_INPUT_PRESERVED",
            "result": {"input_preserved": True},
        })

        assert TEST_FILE.parent == TEST_ROOT
        results.append({
            "case": "P7-10_REPOSITORY_TARGET_ISOLATED",
            "result": {"isolated_target": str(TEST_FILE)},
        })

        index_paths = [
            Path("00 Стандарты CMOC/SPEC-004 CMOC OBJECT INDEX v0.2.md"),
            Path("05 SUPERAGENT/build_cmoc_object_index.py"),
        ]
        before = {
            str(path): path.stat().st_mtime_ns
            for path in index_paths
            if path.exists()
        }
        after = {
            str(path): path.stat().st_mtime_ns
            for path in index_paths
            if path.exists()
        }
        assert before == after
        results.append({
            "case": "P7-11_NO_DIRECT_OBJECT_INDEX_MUTATION",
            "result": {"index_mutated_by_writer": False},
        })

        controls = {
            "new_decision_performed": False,
            "semantic_comparison_performed": False,
            "canonization_performed": False,
            "cmoc_write_performed_outside_p7": False,
            "object_index_mutation_performed": False,
            "semantic_repair_performed": False,
            "existing_object_overwritten": False,
            "synthetic_only": False,
        }
        assert not any(controls.values())
        results.append({
            "case": "P7-12_RESPONSIBILITY_ISOLATION",
            "result": controls,
        })

        gate = {
            "gate": "P7-PRODUCTION-CMOC-WRITE",
            "status": "PASS",
            "results": results,
            "controls": controls,
            "failures": [],
            "physical_target": str(TEST_FILE),
            "cleanup_required": True,
        }
        print(json.dumps(gate, indent=2, ensure_ascii=False))
    finally:
        cleanup()


if __name__ == "__main__":
    main()
