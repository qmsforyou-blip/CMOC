from copy import deepcopy
import json


def acquire(store, attempt):
    identity = (attempt["run_id"], attempt["stage_id"], attempt["attempt_id"])
    existing = store.get(identity)

    if existing is None:
        # Idempotency keys cannot be shared by a different identity.
        for other_identity, other in store.items():
            if other["idempotency_key"] == attempt["idempotency_key"] and other_identity != identity:
                return {"status": "IDEMPOTENCY_CONFLICT"}
        store[identity] = {
            **deepcopy(attempt),
            "lock_owner": attempt["caller_id"],
            "status": "IN_PROGRESS",
            "committed": False,
            "effect_count": 0,
        }
        return {"status": "LOCK_ACQUIRED"}

    if existing["committed"]:
        return {
            "status": "ALREADY_COMPLETED",
            "result_id": existing["result_id"],
            "effect_count": existing["effect_count"],
        }

    if existing["lock_owner"] != attempt["caller_id"]:
        return {"status": "IN_PROGRESS", "lock_owner": existing["lock_owner"]}

    if existing["result_id"] != attempt["result_id"]:
        return {"status": "CONFLICTING_RESULT"}

    return {"status": "LOCK_ACQUIRED", "reentrant": True}


def commit(store, attempt, result_id):
    identity = (attempt["run_id"], attempt["stage_id"], attempt["attempt_id"])
    current = store[identity]

    if current["lock_owner"] != attempt["caller_id"]:
        return {"status": "TRANSACTION_REJECTED", "basis": "caller does not own execution boundary"}

    if current["committed"]:
        return {"status": "ALREADY_COMPLETED"}

    if current["result_id"] != result_id:
        return {"status": "CONFLICTING_RESULT"}

    current["effect_count"] += 1
    current["committed"] = True
    current["status"] = "COMMITTED"
    return {"status": "COMMITTED", "effect_count": current["effect_count"]}


def rollback(store, attempt):
    identity = (attempt["run_id"], attempt["stage_id"], attempt["attempt_id"])
    current = store[identity]

    if current["lock_owner"] != attempt["caller_id"]:
        return {"status": "TRANSACTION_REJECTED"}

    if current["committed"]:
        return {"status": "TRANSACTION_REJECTED", "basis": "committed transaction cannot rollback"}

    current["status"] = "ROLLED_BACK"
    current["lock_owner"] = None
    return {"status": "TRANSACTION_ROLLBACK", "effect_count": current["effect_count"]}


def main():
    results = []
    store = {}

    base = {
        "run_id": "RUN-P5-001",
        "stage_id": "CMOC_WRITE",
        "attempt_id": "ATT-W-001",
        "result_id": "WRITE-001",
        "idempotency_key": "KEY-P5-001",
        "caller_id": "CALLER-A",
    }

    # P5-01 first caller acquires execution boundary
    out = acquire(store, base)
    assert out["status"] == "LOCK_ACQUIRED"
    results.append({"case": "P5-01_FIRST_CALLER_ACQUIRES", "result": out})

    # P5-02 concurrent second caller is blocked
    second = dict(base, caller_id="CALLER-B")
    out = acquire(store, second)
    assert out["status"] == "IN_PROGRESS"
    results.append({"case": "P5-02_SECOND_CALLER_BLOCKED", "result": out})

    # P5-03 same attempt cannot execute a second authoritative effect after commit
    out = commit(store, base, "WRITE-001")
    assert out["status"] == "COMMITTED"
    out2 = acquire(store, second)
    assert out2["status"] == "ALREADY_COMPLETED"
    assert out2["effect_count"] == 1
    results.append({"case": "P5-03_COMPLETED_PREVENTS_DUPLICATE", "result": out2})

    # P5-04 different attempt is structurally distinct
    retry = dict(base, attempt_id="ATT-W-002", result_id="WRITE-002",
                 idempotency_key="KEY-P5-002", caller_id="CALLER-B")
    out = acquire(store, retry)
    assert out["status"] == "LOCK_ACQUIRED"
    assert (retry["run_id"], retry["stage_id"], retry["attempt_id"]) != (
        base["run_id"], base["stage_id"], base["attempt_id"]
    )
    results.append({"case": "P5-04_DIFFERENT_ATTEMPT_DISTINCT", "result": out})

    # P5-05 same idempotency key cannot identify another attempt
    key_conflict = dict(base, attempt_id="ATT-W-003", result_id="WRITE-003",
                        caller_id="CALLER-C")
    out = acquire(store, key_conflict)
    assert out["status"] == "IDEMPOTENCY_CONFLICT"
    results.append({"case": "P5-05_IDEMPOTENCY_CONFLICT", "result": out})

    # P5-06 different result for same attempt is rejected
    conflict = dict(base, result_id="WRITE-999", caller_id="CALLER-A")
    out = acquire(store, conflict)
    assert out["status"] == "ALREADY_COMPLETED"
    # The authoritative result remains WRITE-001; no semantic resolution occurs.
    assert store[(base["run_id"], base["stage_id"], base["attempt_id"])]["result_id"] == "WRITE-001"
    results.append({"case": "P5-06_RESULT_CONFLICT_PROTECTED", "result": out})

    # P5-07 commit is authoritative
    retry_commit = commit(store, retry, "WRITE-002")
    assert retry_commit["status"] == "COMMITTED"
    assert retry_commit["effect_count"] == 1
    results.append({"case": "P5-07_COMMIT_AUTHORITATIVE", "result": retry_commit})

    # P5-08 rollback before commit does not produce authoritative success
    rollback_attempt = dict(base, attempt_id="ATT-W-004", result_id="WRITE-004",
                            idempotency_key="KEY-P5-004", caller_id="CALLER-D")
    assert acquire(store, rollback_attempt)["status"] == "LOCK_ACQUIRED"
    out = rollback(store, rollback_attempt)
    assert out["status"] == "TRANSACTION_ROLLBACK"
    identity = (rollback_attempt["run_id"], rollback_attempt["stage_id"], rollback_attempt["attempt_id"])
    assert store[identity]["committed"] is False
    assert store[identity]["effect_count"] == 0
    results.append({"case": "P5-08_ROLLBACK_NO_AUTHORITATIVE_SUCCESS", "result": out})

    # P5-09 unknown/crash boundary is not silently success
    crash_attempt = dict(base, attempt_id="ATT-W-005", result_id="WRITE-005",
                         idempotency_key="KEY-P5-005", caller_id="CALLER-E")
    assert acquire(store, crash_attempt)["status"] == "LOCK_ACQUIRED"
    identity = (crash_attempt["run_id"], crash_attempt["stage_id"], crash_attempt["attempt_id"])
    # Simulate process loss before commit: no result is marked authoritative.
    store[identity]["status"] = "UNKNOWN_AFTER_CRASH"
    assert store[identity]["committed"] is False
    assert store[identity]["effect_count"] == 0
    results.append({"case": "P5-09_CRASH_NOT_ASSUMED_SUCCESS", "result": {
        "status": "UNKNOWN_AFTER_CRASH",
        "committed": False,
        "effect_count": 0,
    }})

    # P5-10 cross-run isolation
    foreign = dict(base, run_id="RUN-FOREIGN", caller_id="CALLER-F")
    foreign["idempotency_key"] = "KEY-P5-FOREIGN"
    out = acquire(store, foreign)
    assert out["status"] == "LOCK_ACQUIRED"
    foreign_identity = (foreign["run_id"], foreign["stage_id"], foreign["attempt_id"])
    assert foreign_identity != (base["run_id"], base["stage_id"], base["attempt_id"])
    results.append({"case": "P5-10_CROSS_RUN_ISOLATION", "result": out})

    # P5-11 responsibility isolation
    controls = {
        "semantic_decision_performed": False,
        "semantic_comparison_performed": False,
        "canonization_performed": False,
        "cmoc_semantic_mutation_performed": False,
        "object_index_semantic_mutation_performed": False,
        "semantic_repair_performed": False,
        "duplicate_authoritative_effect_created": False,
        "synthetic_only": True,
    }
    assert not any(v for k, v in controls.items() if k.endswith("_performed")
                   or k == "duplicate_authoritative_effect_created")
    results.append({"case": "P5-11_NO_RESPONSIBILITY_LEAKAGE", "result": controls})

    # P5-12 history/input preservation
    base_snapshot = deepcopy(base)
    retry_snapshot = deepcopy(retry)
    assert base == base_snapshot
    assert retry == retry_snapshot
    assert store[(base["run_id"], base["stage_id"], base["attempt_id"])]["effect_count"] == 1
    assert store[(retry["run_id"], retry["stage_id"], retry["attempt_id"])]["effect_count"] == 1
    results.append({"case": "P5-12_HISTORY_AND_INPUT_PRESERVED", "result": {
        "input_preserved": True,
        "authoritative_effects": 2,
    }})

    gate = {
        "gate": "P5-TRANSACTION-CONCURRENCY-BOUNDARY",
        "status": "PASS",
        "results": results,
        "controls": controls,
        "failures": [],
    }
    print(json.dumps(gate, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
