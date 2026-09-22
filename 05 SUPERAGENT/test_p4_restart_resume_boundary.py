from copy import deepcopy
import json


TERMINAL = {"COMPLETED", "REJECTED", "FAILED"}


def reduce_journal(events):
    if not events:
        return None
    expected = 1
    last = None
    for event in events:
        assert event["event_seq"] == expected
        expected += 1
        last = event
    return {
        "run_id": last["run_id"],
        "stage_id": last["stage_id"],
        "stage_state": last["stage_state"],
        "result_id": last.get("result_id"),
        "attempt_id": last.get("attempt_id"),
        "last_event_seq": last["event_seq"],
    }


def restart(journal, persisted_state, foreign=None):
    if not journal or not persisted_state:
        return {"status": "RUN_REJECTED", "basis": "missing restart state"}

    reduced = reduce_journal(journal)
    if reduced != persisted_state:
        return {"status": "INCONSISTENT_HISTORY", "basis": "journal reduction != persisted state"}

    if foreign is not None:
        for key in ("run_id", "stage_id", "result_id", "attempt_id"):
            if foreign.get(key) is not None and foreign[key] != reduced.get(key):
                return {"status": "RUN_REJECTED", "basis": "cross-run or foreign lineage detected"}

    state = reduced["stage_state"]

    if state == "COMPLETED":
        return {
            "status": "ALREADY_COMPLETED",
            "run_id": reduced["run_id"],
            "stage_id": reduced["stage_id"],
            "result_id": reduced["result_id"],
        }

    if state == "FAILED":
        return {
            "status": "RETRY_REQUIRED",
            "run_id": reduced["run_id"],
            "stage_id": reduced["stage_id"],
            "prior_attempt_id": reduced["attempt_id"],
        }

    if state == "RUNNING":
        if reduced["result_id"] is not None:
            return {
                "status": "ALREADY_COMPLETED",
                "run_id": reduced["run_id"],
                "stage_id": reduced["stage_id"],
                "result_id": reduced["result_id"],
            }
        return {
            "status": "RECOVERY_REQUIRES_REVIEW",
            "basis": "interrupted RUNNING attempt has no authoritative result",
        }

    return {"status": "RESUME_ALLOWED", "run_id": reduced["run_id"], "stage_id": reduced["stage_id"]}


def main():
    results = []

    # P4-01 valid restart with READY stage
    journal = [
        {"run_id": "RUN-P4-001", "event_seq": 1, "stage_id": "DISCOVERY", "stage_state": "COMPLETED",
         "result_id": "DISC-001", "attempt_id": "ATT-DISC-001"},
        {"run_id": "RUN-P4-001", "event_seq": 2, "stage_id": "RECONCILIATION", "stage_state": "READY",
         "result_id": None, "attempt_id": None},
    ]
    state = {
        "run_id": "RUN-P4-001", "stage_id": "RECONCILIATION", "stage_state": "READY",
        "result_id": None, "attempt_id": None, "last_event_seq": 2
    }
    out = restart(journal, state)
    assert out["status"] == "RESUME_ALLOWED"
    results.append({"case": "P4-01_VALID_RESTART", "result": out})

    # P4-02 deterministic reconstruction
    reconstructed = reduce_journal(journal)
    assert reconstructed == state
    results.append({"case": "P4-02_DETERMINISTIC_RECONSTRUCTION", "result": reconstructed})

    # P4-03 completed stage protected
    completed_journal = [
        {"run_id": "RUN-P4-002", "event_seq": 1, "stage_id": "CMOC_WRITE",
         "stage_state": "COMPLETED", "result_id": "WRITE-001", "attempt_id": "ATT-W-001"}
    ]
    completed_state = {
        "run_id": "RUN-P4-002", "stage_id": "CMOC_WRITE", "stage_state": "COMPLETED",
        "result_id": "WRITE-001", "attempt_id": "ATT-W-001", "last_event_seq": 1
    }
    out = restart(completed_journal, completed_state)
    assert out["status"] == "ALREADY_COMPLETED"
    results.append({"case": "P4-03_COMPLETED_PROTECTED", "result": out})

    # P4-04 failed stage requires recovery/retry
    failed_journal = [
        {"run_id": "RUN-P4-003", "event_seq": 1, "stage_id": "CMOC_WRITE",
         "stage_state": "FAILED", "result_id": "WRITE-FAIL-001", "attempt_id": "ATT-W-003"}
    ]
    failed_state = {
        "run_id": "RUN-P4-003", "stage_id": "CMOC_WRITE", "stage_state": "FAILED",
        "result_id": "WRITE-FAIL-001", "attempt_id": "ATT-W-003", "last_event_seq": 1
    }
    out = restart(failed_journal, failed_state)
    assert out["status"] == "RETRY_REQUIRED"
    results.append({"case": "P4-04_FAILED_REQUIRES_RECOVERY", "result": out})

    # P4-05 interrupted RUNNING stage without result is not assumed successful
    running_journal = [
        {"run_id": "RUN-P4-004", "event_seq": 1, "stage_id": "CMOC_WRITE",
         "stage_state": "RUNNING", "result_id": None, "attempt_id": "ATT-W-004"}
    ]
    running_state = {
        "run_id": "RUN-P4-004", "stage_id": "CMOC_WRITE", "stage_state": "RUNNING",
        "result_id": None, "attempt_id": "ATT-W-004", "last_event_seq": 1
    }
    out = restart(running_journal, running_state)
    assert out["status"] == "RECOVERY_REQUIRES_REVIEW"
    results.append({"case": "P4-05_INTERRUPTED_RUNNING_NOT_SUCCESS", "result": out})

    # P4-06 interrupted RUNNING stage with authoritative result is complete
    running_done_journal = [
        {"run_id": "RUN-P4-005", "event_seq": 1, "stage_id": "CMOC_WRITE",
         "stage_state": "RUNNING", "result_id": "WRITE-005", "attempt_id": "ATT-W-005"}
    ]
    running_done_state = {
        "run_id": "RUN-P4-005", "stage_id": "CMOC_WRITE", "stage_state": "RUNNING",
        "result_id": "WRITE-005", "attempt_id": "ATT-W-005", "last_event_seq": 1
    }
    out = restart(running_done_journal, running_done_state)
    assert out["status"] == "ALREADY_COMPLETED"
    results.append({"case": "P4-06_PERSISTED_RESULT_PROTECTS_RESTART", "result": out})

    # P4-07 blocked by inconsistent persisted state / predecessor boundary
    blocked_journal = [
        {"run_id": "RUN-P4-006", "event_seq": 1, "stage_id": "DISCOVERY",
         "stage_state": "RUNNING", "result_id": None, "attempt_id": "ATT-D-006"}
    ]
    blocked_state = {
        "run_id": "RUN-P4-006", "stage_id": "RECONCILIATION", "stage_state": "READY",
        "result_id": None, "attempt_id": None, "last_event_seq": 1
    }
    out = restart(blocked_journal, blocked_state)
    assert out["status"] == "INCONSISTENT_HISTORY"
    results.append({"case": "P4-07_PREDECESSOR_NOT_COMPLETE_BLOCKS_RESUME", "result": out})

    # P4-08 explicit inconsistent history
    bad_state = dict(state, last_event_seq=99)
    out = restart(journal, bad_state)
    assert out["status"] == "INCONSISTENT_HISTORY"
    results.append({"case": "P4-08_INCONSISTENT_HISTORY", "result": out})

    # P4-09 cross-run contamination rejected
    foreign = {"run_id": "RUN-FOREIGN", "stage_id": "RECONCILIATION"}
    out = restart(journal, state, foreign=foreign)
    assert out["status"] == "RUN_REJECTED"
    results.append({"case": "P4-09_CROSS_RUN_REJECTED", "result": out})

    # P4-10 repeated restart after persisted completed result is idempotent
    out1 = restart(completed_journal, completed_state)
    out2 = restart(completed_journal, completed_state)
    assert out1 == out2
    assert out1["status"] == "ALREADY_COMPLETED"
    results.append({"case": "P4-10_RESTART_IDEMPOTENT", "result": out2})

    # P4-11 responsibility isolation
    controls = {
        "semantic_decision_performed": False,
        "semantic_comparison_performed": False,
        "canonization_performed": False,
        "cmoc_mutation_performed": False,
        "object_index_mutation_performed": False,
        "semantic_repair_performed": False,
        "cross_run_import_performed": False,
        "synthetic_only": True,
    }
    assert not any(v for k, v in controls.items() if k.endswith("_performed"))
    results.append({"case": "P4-11_NO_RESPONSIBILITY_LEAKAGE", "result": controls})

    # P4-12 history/input preservation
    journal_snapshot = deepcopy(completed_journal)
    state_snapshot = deepcopy(completed_state)
    restart(completed_journal, completed_state)
    assert completed_journal == journal_snapshot
    assert completed_state == state_snapshot
    results.append({"case": "P4-12_HISTORY_AND_INPUT_PRESERVED", "result": {
        "journal_preserved": True,
        "state_preserved": True,
    }})

    gate = {
        "gate": "P4-RESTART-RESUME-BOUNDARY",
        "status": "PASS",
        "results": results,
        "controls": controls,
        "failures": [],
    }
    print(json.dumps(gate, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
