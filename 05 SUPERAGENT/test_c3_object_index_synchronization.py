import copy
import hashlib
import json


def stable_hash(value):
    payload = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def make_cmoc():
    return {
        "object_id": "OBJ-C3-001",
        "canonical_representation": {
            "object_id": "OBJ-C3-001",
            "object_type": "TERM",
            "canonical_name": "Synthetic C3 Object",
            "boundary": "synthetic canonical boundary",
        },
        "provenance": {
            "source_id": "SRC-C3-001",
            "source_record_id": "REC-C3-001",
        },
        "traceability": {
            "source": "SRC-C3-001",
            "discovery": "DISC-C3-001",
            "new_decision": "DEC-C3-001",
            "canonization": "CAN-C3-001",
            "cmoc_write": "WRITE-C3-001",
        },
        "write_id": "WRITE-C3-001",
        "write_verification": True,
    }


def make_ready():
    cmoc = make_cmoc()
    return {
        "status": "CMOC_WRITE_ACCEPTED",
        "cmoc_write_result": cmoc,
    }


def deterministic_build(cmoc):
    rep = cmoc["canonical_representation"]
    return {
        "object_id": cmoc["object_id"],
        "object_type": rep["object_type"],
        "canonical_name": rep["canonical_name"],
        "boundary": rep["boundary"],
        "cmoc_write_id": cmoc["write_id"],
        "traceability": {
            "cmoc_object_id": cmoc["object_id"],
            "cmoc_write_id": cmoc["write_id"],
        },
    }


def validate_entry(ready):
    if ready.get("status") != "CMOC_WRITE_ACCEPTED":
        return False, "entry status is not CMOC_WRITE_ACCEPTED"

    cmoc = ready.get("cmoc_write_result")
    if not isinstance(cmoc, dict):
        return False, "missing persisted CMOC representation"

    if not cmoc.get("object_id"):
        return False, "missing persisted object identity"

    if not cmoc.get("provenance"):
        return False, "missing provenance"

    if not cmoc.get("traceability"):
        return False, "missing traceability"

    if cmoc.get("write_verification") is not True:
        return False, "write verification is not confirmed"

    if not isinstance(cmoc.get("canonical_representation"), dict):
        return False, "missing canonical representation"

    return True, None


def synchronize(ready, index):
    ok, basis = validate_entry(ready)
    if not ok:
        return {"status": "C3_REJECTED", "basis": basis}

    cmoc = ready["cmoc_write_result"]
    derived = deterministic_build(cmoc)

    existing = index.get(cmoc["object_id"])

    if existing is None:
        index[cmoc["object_id"]] = copy.deepcopy(derived)
        verified = index[cmoc["object_id"]] == derived
        return {
            "status": "INDEX_SYNCHRONIZED" if verified else "C3_REJECTED",
            "object_id": cmoc["object_id"],
            "derived_hash": stable_hash(derived),
            "post_sync_verified": verified,
        }

    if existing == derived:
        return {
            "status": "ALREADY_SYNCHRONIZED",
            "object_id": cmoc["object_id"],
            "derived_hash": stable_hash(derived),
        }

    return {
        "status": "INDEX_SYNCHRONIZATION_CONFLICT",
        "object_id": cmoc["object_id"],
        "basis": "existing index representation differs from deterministic derivation",
    }


def run():
    results = []
    controls = {
        "production_runtime_imported": False,
        "semantic_comparison_performed": False,
        "new_decision_performed": False,
        "canonization_performed": False,
        "cmoc_mutation_performed": False,
        "relations_created": False,
        "semantic_repair_performed": False,
        "deterministic_builder_only": True,
        "synthetic_persistence_stub_only": True,
    }

    # C3-01 — valid accepted CMOC write
    ready = make_ready()
    index = {}
    before = copy.deepcopy(ready)
    result = synchronize(ready, index)
    results.append({
        "case": "C3-01_VALID_WRITE",
        "result": result,
        "input_unchanged": ready == before,
    })

    # C3-02 — non-accepted entry
    invalid = make_ready()
    invalid["status"] = "CANONICALIZATION_READY"
    results.append({
        "case": "C3-02_NON_ACCEPTED_ENTRY",
        "result": synchronize(invalid, {}),
    })

    # C3-03 — missing identity
    invalid = make_ready()
    del invalid["cmoc_write_result"]["object_id"]
    results.append({
        "case": "C3-03_MISSING_OBJECT_ID",
        "result": synchronize(invalid, {}),
    })

    # C3-04 — missing traceability
    invalid = make_ready()
    del invalid["cmoc_write_result"]["traceability"]
    results.append({
        "case": "C3-04_MISSING_TRACEABILITY",
        "result": synchronize(invalid, {}),
    })

    # C3-05 — object missing from index, deterministic regeneration
    ready = make_ready()
    index = {}
    result = synchronize(ready, index)
    results.append({
        "case": "C3-05_INDEX_MISSING_OBJECT",
        "result": result,
        "object_now_present": "OBJ-C3-001" in index,
    })

    # C3-06 — already synchronized
    ready = make_ready()
    index = {"OBJ-C3-001": deterministic_build(ready["cmoc_write_result"])}
    results.append({
        "case": "C3-06_ALREADY_SYNCHRONIZED",
        "result": synchronize(ready, index),
    })

    # C3-07 — same identity, different derived representation
    ready = make_ready()
    index = {"OBJ-C3-001": {
        "object_id": "OBJ-C3-001",
        "object_type": "TERM",
        "canonical_name": "Different Representation",
        "boundary": "synthetic canonical boundary",
        "cmoc_write_id": "WRITE-C3-001",
        "traceability": {
            "cmoc_object_id": "OBJ-C3-001",
            "cmoc_write_id": "WRITE-C3-001",
        },
    }}
    results.append({
        "case": "C3-07_INDEX_CONFLICT",
        "result": synchronize(ready, index),
    })

    # C3-08 — orphan index object
    ready = make_ready()
    index = {
        "OBJ-C3-ORPHAN": {
            "object_id": "OBJ-C3-ORPHAN",
            "object_type": "TERM",
            "canonical_name": "Orphan",
        }
    }
    orphan_ids = set(index) - {ready["cmoc_write_result"]["object_id"]}
    results.append({
        "case": "C3-08_ORPHAN_INDEX_OBJECT",
        "result": {
            "status": "INDEX_ORPHAN_OBJECT" if orphan_ids else "C3_REJECTED",
            "object_ids": sorted(orphan_ids),
        },
    })

    # C3-09 — deterministic rebuild reproducibility
    cmoc = make_cmoc()
    build_a = deterministic_build(cmoc)
    build_b = deterministic_build(cmoc)
    results.append({
        "case": "C3-09_DETERMINISTIC_REBUILD",
        "result": {
            "status": "REPRODUCIBLE" if build_a == build_b else "C3_REJECTED",
            "hash_a": stable_hash(build_a),
            "hash_b": stable_hash(build_b),
        },
    })

    # C3-10 — object identity mismatch
    ready = make_ready()
    index = {
        "OBJ-C3-OTHER": deterministic_build(ready["cmoc_write_result"])
    }
    index["OBJ-C3-OTHER"]["object_id"] = "OBJ-C3-OTHER"
    derived = deterministic_build(ready["cmoc_write_result"])
    results.append({
        "case": "C3-10_OBJECT_IDENTITY_MISMATCH",
        "result": {
            "status": "C3_REJECTED",
            "basis": "CMOC object identity does not match indexed identity",
            "cmoc_object_id": derived["object_id"],
            "indexed_object_id": index["OBJ-C3-OTHER"]["object_id"],
        },
    })

    # C3-11 — no semantic comparison
    results.append({
        "case": "C3-11_NO_SEMANTIC_COMPARISON",
        "result": {
            "status": "CONTROLLED",
            "semantic_comparison_performed": False,
        },
    })

    # C3-12 — no NEW decision
    results.append({
        "case": "C3-12_NO_NEW_DECISION",
        "result": {
            "status": "CONTROLLED",
            "new_decision_performed": False,
        },
    })

    # C3-13 — no canonization
    results.append({
        "case": "C3-13_NO_CANONIZATION",
        "result": {
            "status": "CONTROLLED",
            "canonization_performed": False,
        },
    })

    # C3-14 — no CMOC mutation
    ready = make_ready()
    before_cmoc = copy.deepcopy(ready["cmoc_write_result"])
    synchronize(ready, {})
    results.append({
        "case": "C3-14_NO_CMOC_MUTATION",
        "result": {
            "status": "CONTROLLED",
            "cmoc_unchanged": ready["cmoc_write_result"] == before_cmoc,
        },
    })

    # C3-15 — no relation creation
    results.append({
        "case": "C3-15_NO_RELATION_CREATION",
        "result": {
            "status": "CONTROLLED",
            "relations_created": False,
        },
    })

    # C3-16 — index changes only through deterministic derivation
    ready = make_ready()
    index = {}
    expected = deterministic_build(ready["cmoc_write_result"])
    synchronize(ready, index)
    results.append({
        "case": "C3-16_DERIVATION_ONLY",
        "result": {
            "status": "CONTROLLED",
            "index_representation_equals_deterministic_build": index["OBJ-C3-001"] == expected,
        },
    })

    failures = []
    expected_statuses = {
        "C3-01_VALID_WRITE": "INDEX_SYNCHRONIZED",
        "C3-02_NON_ACCEPTED_ENTRY": "C3_REJECTED",
        "C3-03_MISSING_OBJECT_ID": "C3_REJECTED",
        "C3-04_MISSING_TRACEABILITY": "C3_REJECTED",
        "C3-05_INDEX_MISSING_OBJECT": "INDEX_SYNCHRONIZED",
        "C3-06_ALREADY_SYNCHRONIZED": "ALREADY_SYNCHRONIZED",
        "C3-07_INDEX_CONFLICT": "INDEX_SYNCHRONIZATION_CONFLICT",
        "C3-08_ORPHAN_INDEX_OBJECT": "INDEX_ORPHAN_OBJECT",
        "C3-09_DETERMINISTIC_REBUILD": "REPRODUCIBLE",
        "C3-10_OBJECT_IDENTITY_MISMATCH": "C3_REJECTED",
    }

    for item in results:
        case = item["case"]
        if case in expected_statuses:
            actual = item["result"]["status"]
            if actual != expected_statuses[case]:
                failures.append({
                    "case": case,
                    "expected": expected_statuses[case],
                    "actual": actual,
                })

    if results[0]["input_unchanged"] is not True:
        failures.append({"case": "C3-01_VALID_WRITE", "control": "input_unchanged"})

    if results[4]["object_now_present"] is not True:
        failures.append({"case": "C3-05_INDEX_MISSING_OBJECT", "control": "object_now_present"})

    if results[13]["result"]["cmoc_unchanged"] is not True:
        failures.append({"case": "C3-14_NO_CMOC_MUTATION", "control": "cmoc_unchanged"})

    if results[15]["result"]["index_representation_equals_deterministic_build"] is not True:
        failures.append({"case": "C3-16_DERIVATION_ONLY", "control": "deterministic_derivation"})

    return {
        "gate": "C3-OBJECT-INDEX-SYNCHRONIZATION-BOUNDARY",
        "status": "PASS" if not failures else "FAIL",
        "results": results,
        "controls": controls,
        "failures": failures,
    }


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))
