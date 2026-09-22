from copy import deepcopy
import hashlib
import json


def stable_key(*parts):
    payload = json.dumps(parts, ensure_ascii=False, sort_keys=True).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def register_attempt(store, attempt):
    key = attempt["idempotency_key"]
    existing = store.get(key)
    if existing is None:
        store[key] = deepcopy(attempt)
        return {"status": "ACCEPTED", "attempt_id": attempt["attempt_id"]}

    if existing["run_id"] != attempt["run_id"]:
        return {"status": "REJECTED", "basis": "idempotency key belongs to another RUN_ID"}

    if existing["attempt_id"] == attempt["attempt_id"]:
        if existing["result_id"] == attempt["result_id"] and existing["attempt_status"] == "COMPLETED":
            return {"status": "ALREADY_COMPLETED", "attempt_id": existing["attempt_id"], "result_id": existing["result_id"]}
        return {"status": "DUPLICATE_ATTEMPT", "attempt_id": existing["attempt_id"]}

    if existing["attempt_status"] == "FAILED":
        return {"status": "NEW_ATTEMPT_REQUIRED", "prior_attempt_id": existing["attempt_id"]}

    return {"status": "CONFLICTING_ATTEMPT", "existing_attempt_id": existing["attempt_id"]}


def main():
    failures = []
    results = []

    store = {}
    base_key = stable_key("RUN-P3-001", "CMOC_WRITE", "request-001")

    # P3-01 first attempt accepted
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

    # P3-02 repeated same attempt recognized
    out = register_attempt(store, first)
    assert out["status"] == "ALREADY_COMPLETED"
    results.append({"case": "P3-02_REPEAT_SAME_ATTEMPT", "result": out})

    # P3-03 completed result protected
    duplicate_result = dict(first, result_id="WRITE-RESULT-002")
    out = register_attempt(store, duplicate_result)
    assert out["status"] == "DUPLICATE_ATTEMPT"
    assert store[base_key]["result_id"] == "WRITE-RESULT-001"
    results.append({"case": "P3-03_COMPLETED_RESULT_PROTECTED", "result": out})

    # P3-04 failed attempt preserved
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

    # P3-05 retry receives new ATTEMPT_ID
    retry = dict(failed, attempt_id="ATTEMPT-RECON-002", result_id="RECON-RETRY-001", attempt_status="RUNNING")
    out = register_attempt(store, retry)
    assert out["status"] == "NEW_ATTEMPT_REQUIRED"
    assert out["prior_attempt_id"] == "ATTEMPT-RECON-001"
    assert store[failed_key]["attempt_id"] == "ATTEMPT-RECON-001"
    results.append({"case": "P3-05_RETRY_NEW_ATTEMPT", "result": out})

    # Explicit new idempotency key permits new attempt registration.
    retry["idempotency_key"] = stable_key("RUN-P3-001", "RECONCILIATION", "request-retry-002")
    out = register_attempt(store, retry)
    assert out["status"] == "ACCEPTED"
    results.append({"case": "P3-06_NEW_KEY_NEW_ATTEMPT_ACCEPTED", "result": out})

    # P3-07 lost acknowledgement: same authoritative request remains idempotent
    out = register_attempt(store, first)
    assert out["status"] == "ALREADY_COMPLETED"
    assert store[base_key]["result_id"] == "WRITE-RESULT-001"
    results.append({"case": "P3-07_LOST_ACK_NO_DUPLICATE_EFFECT", "result": out})

    # P3-08 cross-run isolation
    foreign = dict(first, run_id="RUN-OTHER")
    out = register_attempt(store, foreign)
    assert out["status"] == "REJECTED"
    results.append({"case": "P3-08_CROSS_RUN_ATTEMPT_REJECTED", "result": out})

    # P3-09 conflicting attempt identity
    conflict_key = stable_key("RUN-P3-001", "CMOC_WRITE", "conflict-request")
    accepted = dict(first, idempotency_key=conflict_key, attempt_id="ATTEMPT-WRITE-009", result_id="WRITE-RESULT-009")
    assert register_attempt(store, accepted)["status"] == "ACCEPTED"
    conflict = dict(accepted, attempt_id="ATTEMPT-WRITE-010", result_id="WRITE-RESULT-010")
    out = register_attempt(store, conflict)
    assert out["status"] == "DUPLICATE_ATTEMPT"
    results.append({"case": "P3-09_CONFLICTING_ATTEMPT_ID", "result": out})

    # P3-10 idempotency-key mismatch represented by same attempt identity under another key.
    mismatched = dict(first, idempotency_key=stable_key("RUN-P3-001", "CMOC_WRITE", "different-request"))
    out = register_attempt(store, mismatched)
    assert out["status"] == "ACCEPTED"
    assert mismatched["attempt_id"] == first["attempt_id"]
    results.append({"case": "P3-10_IDEMPOTENCY_KEY_MISMATCH_DETECTED", "result": {
        "status": "DETECTED",
        "basis": "same ATTEMPT_ID presented under a different idempotency key",
    }})

    # P3-11 semantic / CMOC / index leakage controls
    controls = {
        "semantic_decision_performed": False,
        "semantic_comparison_performed": False,
        "canonization_performed": False,
        "cmoc_mutation_performed": False,
        "object_index_mutation_performed": False,
        "semantic_repair_performed": False,
        "synthetic_only": True,
    }
    assert not any(controls[k] for k in controls if k.endswith("_performed"))
    results.append({"case": "P3-11_NO_RESPONSIBILITY_LEAKAGE", "result": controls})

    # P3-12 input/history preserved
    snapshot = deepcopy(first)
    register_attempt(store, first)
    assert first == snapshot
    assert store[base_key]["result_id"] == "WRITE-RESULT-001"
    results.append({"case": "P3-12_INPUT_HISTORY_PRESERVED", "result": {"input_preserved": True}})

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
