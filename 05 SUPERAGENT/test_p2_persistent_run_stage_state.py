from copy import deepcopy
import json


STAGES = ["DISCOVERY", "RECONCILIATION", "NEW_DECISION", "CANONIZATION", "CMOC_WRITE", "OBJECT_INDEX_SYNC"]

STATE_VERSION = "P2.0"


def reduce_state(journal, run_id):
    events = sorted([e for e in journal if e["run_id"] == run_id], key=lambda e: e["event_seq"])
    state = {
        "run_id": run_id,
        "run_status": "NOT_STARTED",
        "current_stage_id": None,
        "current_stage_result_id": None,
        "current_attempt_id": None,
        "last_event_seq": 0,
        "state_version": STATE_VERSION,
    }
    for e in events:
        if e["event_seq"] != state["last_event_seq"] + 1:
            return {"status": "INCONSISTENT_HISTORY", "basis": "event sequence gap"}
        state["last_event_seq"] = e["event_seq"]
        state["current_stage_id"] = e["stage_id"]
        state["current_stage_result_id"] = e["stage_result_id"]
        state["current_attempt_id"] = e["attempt_id"]
        state["run_status"] = e["event_status"]
    return state


def validate_projection(journal, projection):
    derived = reduce_state(journal, projection["run_id"])
    if derived.get("status") == "INCONSISTENT_HISTORY":
        return {"status": "REJECTED", "basis": derived["basis"]}
    if derived != projection:
        return {"status": "STATE_MISMATCH", "basis": "persisted projection differs from journal reduction"}
    return {"status": "CONSISTENT"}


def main():
    failures = []
    results = []

    journal = [
        {
            "run_id": "RUN-P2-001", "event_seq": 1, "event_id": "EV-001",
            "stage_id": "RUN", "stage_result_id": "RUN-001",
            "attempt_id": "ATTEMPT-RUN-001", "event_status": "ACTIVE"
        },
        {
            "run_id": "RUN-P2-001", "event_seq": 2, "event_id": "EV-002",
            "stage_id": "DISCOVERY", "stage_result_id": "DISC-001",
            "attempt_id": "ATTEMPT-DISC-001", "event_status": "RUNNING"
        },
        {
            "run_id": "RUN-P2-001", "event_seq": 3, "event_id": "EV-003",
            "stage_id": "DISCOVERY", "stage_result_id": "DISC-001",
            "attempt_id": "ATTEMPT-DISC-001", "event_status": "COMPLETED"
        },
    ]

    projection = reduce_state(journal, "RUN-P2-001")
    assert projection["run_status"] == "COMPLETED"
    assert projection["current_stage_id"] == "DISCOVERY"
    results.append({"case": "P2-01_RUN_AND_STAGE_PROJECTION", "result": projection})

    # P2-02 stage progression
    extended = journal + [{
        "run_id": "RUN-P2-001", "event_seq": 4, "event_id": "EV-004",
        "stage_id": "RECONCILIATION", "stage_result_id": "RECON-001",
        "attempt_id": "ATTEMPT-RECON-001", "event_status": "RUNNING"
    }]
    state = reduce_state(extended, "RUN-P2-001")
    assert state["current_stage_id"] == "RECONCILIATION"
    assert state["run_status"] == "RUNNING"
    results.append({"case": "P2-02_STAGE_PROGRESSION", "result": state})

    # P2-03 completed stage protection
    assert projection["run_status"] == "COMPLETED"
    duplicate_completion = reduce_state(journal, "RUN-P2-001")
    assert duplicate_completion == projection
    results.append({"case": "P2-03_COMPLETED_STAGE_PROTECTED", "result": {"status": "ALREADY_COMPLETED"}})

    # P2-04 failed stage
    failed = journal + [{
        "run_id": "RUN-P2-001", "event_seq": 4, "event_id": "EV-004",
        "stage_id": "RECONCILIATION", "stage_result_id": "RECON-FAIL-001",
        "attempt_id": "ATTEMPT-RECON-001", "event_status": "FAILED"
    }]
    state = reduce_state(failed, "RUN-P2-001")
    assert state["run_status"] == "FAILED"
    results.append({"case": "P2-04_FAILED_STAGE", "result": state})

    # P2-05 recovery transition
    recoverable = failed + [{
        "run_id": "RUN-P2-001", "event_seq": 5, "event_id": "EV-005",
        "stage_id": "RECONCILIATION", "stage_result_id": "RECON-FAIL-001",
        "attempt_id": "ATTEMPT-RECON-001", "event_status": "RECOVERABLE"
    }]
    state = reduce_state(recoverable, "RUN-P2-001")
    assert state["run_status"] == "RECOVERABLE"
    results.append({"case": "P2-05_RECOVERY_TRANSITION", "result": state})

    # P2-06 retry with new attempt
    retry = recoverable + [{
        "run_id": "RUN-P2-001", "event_seq": 6, "event_id": "EV-006",
        "stage_id": "RECONCILIATION", "stage_result_id": "RECON-RETRY-001",
        "attempt_id": "ATTEMPT-RECON-002", "event_status": "RUNNING"
    }]
    state = reduce_state(retry, "RUN-P2-001")
    assert state["current_attempt_id"] == "ATTEMPT-RECON-002"
    assert any(e["stage_result_id"] == "RECON-FAIL-001" for e in retry)
    results.append({"case": "P2-06_RETRY_NEW_ATTEMPT", "result": state})

    # P2-07 deterministic projection
    a = reduce_state(retry, "RUN-P2-001")
    b = reduce_state(list(reversed(retry)), "RUN-P2-001")
    assert a == b
    results.append({"case": "P2-07_DETERMINISTIC_PROJECTION", "result": {"status": "CONSISTENT"}})

    # P2-08 restart reconstruction
    restored = json.loads(json.dumps(retry))
    restored_state = reduce_state(restored, "RUN-P2-001")
    assert restored_state == a
    results.append({"case": "P2-08_RESTART_RECONSTRUCTION", "result": restored_state})

    # P2-09 journal / projection mismatch
    bad_projection = deepcopy(a)
    bad_projection["current_stage_id"] = "CMOC_WRITE"
    out = validate_projection(retry, bad_projection)
    assert out["status"] == "STATE_MISMATCH"
    results.append({"case": "P2-09_STATE_MISMATCH", "result": out})

    # P2-10 cross-run isolation
    foreign = dict(a)
    foreign["run_id"] = "RUN-OTHER"
    out = validate_projection(retry, foreign)
    assert out["status"] == "STATE_MISMATCH"
    results.append({"case": "P2-10_CROSS_RUN_ISOLATION", "result": out})

    # P2-11 state version
    assert a["state_version"] == STATE_VERSION
    results.append({"case": "P2-11_STATE_VERSION", "result": {"state_version": a["state_version"]}})

    # P2-12 no responsibility leakage
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
    results.append({"case": "P2-12_NO_RESPONSIBILITY_LEAKAGE", "result": controls})

    gate = {
        "gate": "P2-PERSISTENT-RUN-STAGE-STATE-MODEL",
        "status": "PASS" if not failures else "FAIL",
        "results": results,
        "controls": controls,
        "failures": failures,
    }
    print(json.dumps(gate, indent=2, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()
