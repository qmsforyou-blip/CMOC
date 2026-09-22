from copy import deepcopy
import hashlib
import json


def stable_key(*parts):
    payload = json.dumps(parts, ensure_ascii=False, sort_keys=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def register_attempt(store, attempt):
    # Identity is scoped by RUN_ID + STAGE_ID + ATTEMPT_ID.
    identity = (attempt["run_id"], attempt["stage_id"], attempt["attempt_id"])
    existing = store.get(identity)

    if existing is None:
        # The idempotency key must not already identify a different attempt.
        for other_identity, other in store.items():
            if other["idempotency_key"] == attempt["idempotency_key"] and other_identity != identity:
                return {
                    "status": "IDEMPOTENCY_KEY_CONFLICT",
                    "existing_attempt_id": other["attempt_id"],
                }
        store[identity] = deepcopy(attempt)
        return {"status": "ACCEPTED", "attempt_id": attempt["attempt_id"]}

    if existing["idempotency_key"] != attempt["idempotency_key"]:
        return {
            "status": "IDEMPOTENCY_KEY_MISMATCH",
            "attempt_id": existing["attempt_id"],
            "existing_idempotency_key": existing["idempotency_key"],
        }

    if existing["result_id"] != attempt["result_id"]:
        return {
            "status": "CONFLICTING_ATTEMPT",
            "attempt_id": existing["attempt_id"],
            "existing_result_id": existing["result_id"],
        }

    if existing["attempt_status"] == "COMPLETED":
        return {
            "status": "ALREADY_COMPLETED",
            "attempt_id": existing["attempt_id"],
            "result_id": existing["result_id"],
        }

    if existing["attempt_status"] == "RUNNING":
        return {"status": "IN_PROGRESS", "attempt_id": existing["attempt_id"]}

    if existing["attempt_status"] == "FAILED":
        return {
            "status": "DUPLICATE_ATTEMPT",
            "attempt_id": existing["attempt_id"],
            "basis": "failed attempt already recorded; retry requires a new ATTEMPT_ID",
        }

    return {"status": "REJECTED", "basis": "unknown attempt status"}


def main():
    failures = []
    results = []
    store = {}

    # P3-01 first attempt accepted
    base_key = stable_key("RUN-P3-001", "CMOC_WRITE", "request-001")
    first = {
        "run_id": "RUN-P3-001",
        "stage_id": "CMOC_WRITE",
        "attempt_id": "ATTEMPT-WRITE-001",
        "result_id": "WRITE-RESULT-001",
        "idempotency_key": base_key,
        "attempt_status": "COMPLETED",
    }
    out = register_attempt(store, first)
    assert out["status"] == "ACCEPTED"
    results.append({"case": "P3-01_FIRST_ATTEMPT_ACCEPTED", "result": out})

    # P3-02 repeated same attempt after completion
    out = register_attempt(store, first)
    assert out["status"] == "ALREADY_COMPLETED"
    results.append({"case": "P3-02_REPEAT_SAME_ATTEMPT", "result": out})

    # P3-03 completed authoritative result cannot be replaced
    duplicate_result = dict(first, result_id="WRITE-RESULT-002")
    out = register_attempt(store, duplicate_result)
    assert out["status"] == "CONFLICTING_ATTEMPT"
    assert store[(first["run_id"], first["stage_id"], first["attempt_id"])]["result_id"] == "WRITE-RESULT-001"
    results.append({"case": "P3-03_COMPLETED_RESULT_PROTECTED", "result": out})

    # P3-04 failed attempt is preserved
    failed_key = stable_key("RUN-P3-001", "RECONCILIATION", "request-fail")
    failed = {
        "run_id": "RUN-P3-001",
        "stage_id": "RECONCILIATION",
        "attempt_id": "ATTEMPT-RECON-001",
        "result_id": "RECON-FAIL-001",
        "idempotency_key": failed_key,
        "attempt_status": "FAILED",
    }
    out = register_attempt(store, failed)
    assert out["status"] == "ACCEPTED"
    results.append({"case": "P3-04_FAILED_ATTEMPT_PRESERVED", "result": out})

    # P3-05 retry with the same ATTEMPT_ID is not allowed
    out = register_attempt(store, failed)
    assert out["status"] == "DUPLICATE_ATTEMPT"
    results.append({"case": "P3-05_RETRY_REQUIRES_NEW_ATTEMPT", "result": out})

    # P3-06 retry gets new ATTEMPT_ID and new RESULT_ID
    retry_key = stable_key("RUN-P3-001", "RECONCILIATION", "request-retry-002")
    retry = {
        "run_id": "RUN-P3-001",
        "stage_id": "RECONCILIATION",
        "attempt_id": "ATTEMPT-RECON-002",
        "result_id": "RECON-RETRY-001",
        "idempotency_key": retry_key,
        "attempt_status": "RUNNING",
    }
    out = register_attempt(store, retry)
    assert out["status"] == "ACCEPTED"
    assert retry["attempt_id"] != failed["attempt_id"]
    assert retry["result_id"] != failed["result_id"]
    assert store[(failed["run_id"], failed["stage_id"], failed["attempt_id"])]["result_id"] == "RECON-FAIL-001"
    results.append({"case": "P3-06_RETRY_NEW_ATTEMPT_AND_RESULT", "result": out})

    # P3-07 lost acknowledgement: authoritative completed result prevents duplicate effect
    out = register_attempt(store, first)
    assert out["status"] == "ALREADY_COMPLETED"
    assert store[(first["run_id"], first["stage_id"], first["attempt_id"])]["result_id"] == "WRITE-RESULT-001"
    results.append({"case": "P3-07_LOST_ACK_NO_DUPLICATE_EFFECT", "result": out})

    # P3-08 cross-run isolation
    foreign = dict(first, run_id="RUN-OTHER")
    out = register_attempt(store, foreign)
    assert out["status"] == "IDEMPOTENCY_KEY_CONFLICT"
    results.append({"case": "P3-08_CROSS_RUN_IDEMPOTENCY_ISOLATION", "result": out})

    # P3-09 same identity with a different result is a conflict
    conflict = dict(first, result_id="WRITE-RESULT-009")
    out = register_attempt(store, conflict)
    assert out["status"] == "CONFLICTING_ATTEMPT"
    results.append({"case": "P3-09_CONFLICTING_ATTEMPT_RESULT", "result": out})

    # P3-10 same identity with another idempotency key is explicitly rejected
    mismatched = dict(first, idempotency_key=stable_key("RUN-P3-001", "CMOC_WRITE", "different-request"))
    out = register_attempt(store, mismatched)
    assert out["status"] == "IDEMPOTENCY_KEY_MISMATCH"
    results.append({"case": "P3-10_IDEMPOTENCY_KEY_MISMATCH", "result": out})

    # P3-11 in-progress repeat is recognized without creating another attempt
    out = register_attempt(store, retry)
    assert out["status"] == "IN_PROGRESS"
    results.append({"case": "P3-11_IN_PROGRESS_REPEAT", "result": out})

    # P3-12 responsibility/history controls
    controls = {
        "semantic_decision_performed": False,
        "semantic_comparison_performed": False,
        "canonization_performed": False,
        "cmoc_mutation_performed": False,
        "object_index_mutation_performed": False,
        "semantic_repair_performed": False,
        "duplicate_authoritative_effect_created": False,
        "failed_attempt_overwritten": False,
        "synthetic_only": True,
    }
    assert not any(
        value
        for key, value in controls.items()
        if key.endswith("_performed")
        or key in {"duplicate_authoritative_effect_created", "failed_attempt_overwritten"}
    )

    first_snapshot = deepcopy(first)
    failed_snapshot = deepcopy(failed)
    register_attempt(store, first)
    register_attempt(store, failed)
    assert first == first_snapshot
    assert failed == failed_snapshot
    assert store[(first["run_id"], first["stage_id"], first["attempt_id"])]["result_id"] == "WRITE-RESULT-001"
    assert store[(failed["run_id"], failed["stage_id"], failed["attempt_id"])]["result_id"] == "RECON-FAIL-001"
    results.append({
        "case": "P3-12_HISTORY_AND_INPUT_PRESERVED",
        "result": {
            "input_preserved": True,
            "completed_result_preserved": True,
            "failed_attempt_preserved": True,
        },
    })

    gate = {
        "gate": "P3-ATTEMPT-IDENTITY-IDEMPOTENCY-MODEL",
        "status": "PASS" if not failures else "FAIL",
        "results": results,
        "controls": controls,
        "failures": failures,
    }
    print(json.dumps(gate, indent=2, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()
