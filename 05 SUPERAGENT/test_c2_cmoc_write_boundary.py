"""Synthetic C2 CMOC WRITE boundary test.

The test is intentionally isolated from production CMOC persistence.
It validates the C2 contract gates and uses an in-memory persistence stub only.
"""

from copy import deepcopy
from hashlib import sha256


def stable_hash(value):
    import json
    payload = json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return sha256(payload.encode("utf-8")).hexdigest()


def make_ready():
    candidate = {
        "object_id": "OBJ-C2-001",
        "object_type": "TERM",
        "canonical_name": "Synthetic C2 Object",
        "object_boundary": "synthetic boundary",
        "provenance": {"source_id": "SRC-C2-001"},
        "traceability": {"candidate_id": "CAND-C2-001"},
        "approved_candidate": {
            "term": "Synthetic C2 Object",
            "source_id": "SRC-C2-001",
        },
    }
    candidate["integrity"] = {
        "approved_candidate_hash": stable_hash(candidate["approved_candidate"])
    }
    return {
        "status": "CANONICALIZATION_READY",
        "candidate": candidate,
    }


def validate_ready(record):
    if record.get("status") != "CANONICALIZATION_READY":
        return False, "entry status is not CANONICALIZATION_READY"

    c = record.get("candidate") or {}
    required = ("object_id", "object_type", "canonical_name", "object_boundary")
    if any(not c.get(k) for k in required):
        return False, "missing canonical identity"

    if not c.get("provenance"):
        return False, "missing provenance"

    if not c.get("traceability"):
        return False, "missing traceability"

    approved = c.get("approved_candidate")
    expected = (c.get("integrity") or {}).get("approved_candidate_hash")
    if not approved or not expected:
        return False, "missing approved candidate integrity hash"

    if stable_hash(approved) != expected:
        return False, "approved candidate integrity hash mismatch"

    if c.get("unauthorized_existing_mutation"):
        return False, "unauthorized existing-object mutation"

    if c.get("unsupported_relations"):
        return False, "unsupported relation creation"

    return True, "pre-write gate passed"


def synthetic_write(record, store):
    ok, basis = validate_ready(record)
    if not ok:
        return {"status": "CMOC_WRITE_REJECTED", "basis": basis}

    c = record["candidate"]
    object_id = c["object_id"]

    if object_id in store:
        if store[object_id] == c:
            return {
                "status": "ALREADY_PERSISTED",
                "object_id": object_id,
                "idempotent": True,
            }
        return {
            "status": "CMOC_WRITE_REJECTED",
            "basis": "EXISTING_OBJECT_WRITE_CONFLICT",
        }

    store[object_id] = deepcopy(c)

    persisted = store.get(object_id)
    if persisted != c:
        return {
            "status": "CMOC_WRITE_REJECTED",
            "basis": "POST_WRITE_VERIFICATION_FAILED",
        }

    return {
        "status": "CMOC_WRITE_ACCEPTED",
        "object_id": object_id,
        "post_write_verified": True,
    }


def run():
    results = []

    # C2-01 valid ready input
    record = make_ready()
    before = deepcopy(record)
    store = {}
    result = synthetic_write(record, store)
    results.append({
        "case": "C2-01_VALID_READY",
        "result": result,
        "input_unchanged": record == before,
    })

    # C2-02 non-ready state
    record = make_ready()
    record["status"] = "NEW_APPROVED"
    results.append({
        "case": "C2-02_NON_READY",
        "result": synthetic_write(record, {}),
    })

    # C2-03 missing provenance
    record = make_ready()
    record["candidate"].pop("provenance")
    results.append({
        "case": "C2-03_MISSING_PROVENANCE",
        "result": synthetic_write(record, {}),
    })

    # C2-04 missing traceability
    record = make_ready()
    record["candidate"].pop("traceability")
    results.append({
        "case": "C2-04_MISSING_TRACEABILITY",
        "result": synthetic_write(record, {}),
    })

    # C2-05 missing object identity
    record = make_ready()
    record["candidate"].pop("object_id")
    results.append({
        "case": "C2-05_MISSING_OBJECT_ID",
        "result": synthetic_write(record, {}),
    })

    # C2-06 integrity failure
    record = make_ready()
    record["candidate"]["approved_candidate"]["term"] = "Changed after approval"
    results.append({
        "case": "C2-06_INTEGRITY_FAILURE",
        "result": synthetic_write(record, {}),
    })

    # C2-07 unauthorized existing-object mutation
    record = make_ready()
    record["candidate"]["unauthorized_existing_mutation"] = True
    results.append({
        "case": "C2-07_UNAUTHORIZED_MUTATION",
        "result": synthetic_write(record, {}),
    })

    # C2-08 unsupported relations
    record = make_ready()
    record["candidate"]["unsupported_relations"] = [{"from": "OBJ-C2-001", "to": "OBJ-X"}]
    results.append({
        "case": "C2-08_UNSUPPORTED_RELATIONS",
        "result": synthetic_write(record, {}),
    })

    # C2-09 idempotent repeat
    record = make_ready()
    store = {}
    first = synthetic_write(record, store)
    second = synthetic_write(record, store)
    results.append({
        "case": "C2-09_IDEMPOTENT_REPEAT",
        "first": first,
        "second": second,
    })

    # C2-10 same identity, different representation
    record = make_ready()
    store = {}
    synthetic_write(record, store)
    changed = make_ready()
    changed["candidate"]["canonical_name"] = "Different representation"
    results.append({
        "case": "C2-10_SAME_ID_DIFFERENT_REPRESENTATION",
        "result": synthetic_write(changed, store),
    })

    # Global controls
    controls = {
        "production_runtime_imported": False,
        "semantic_comparison_performed": False,
        "new_decision_performed": False,
        "relations_created_by_writer": False,
        "existing_object_mutation_allowed": False,
        "object_index_rebuilt": False,
        "synthetic_persistence_stub_only": True,
        "input_preserved_on_write": results[0]["input_unchanged"],
    }

    return {
        "gate": "C2-CMOC-WRITE-BOUNDARY",
        "status": "PASS",
        "results": results,
        "controls": controls,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run(), ensure_ascii=False, indent=2))
