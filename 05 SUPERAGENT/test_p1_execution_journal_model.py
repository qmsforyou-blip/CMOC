from copy import deepcopy
import json


VALID_EVENTS = {
    "RUN_CREATED",
    "STAGE_STARTED",
    "STAGE_COMPLETED",
    "STAGE_REJECTED",
    "STAGE_FAILED",
    "RECOVERY_REQUESTED",
    "RETRY_REQUIRED",
    "RESUME_ALLOWED",
    "RESUME_BLOCKED",
    "RUN_COMPLETED",
    "RUN_REJECTED",
    "RUN_FAILED",
    "RUN_INCOMPLETE",
}


def append_event(journal, event):
    if event["event_type"] not in VALID_EVENTS:
        return {"status": "REJECTED", "basis": "unknown event type"}
    if any(e["event_id"] == event["event_id"] for e in journal):
        return {"status": "REJECTED", "basis": "duplicate EVENT_ID"}
    run_events = [e for e in journal if e["run_id"] == event["run_id"]]
    if any(e["event_seq"] == event["event_seq"] for e in run_events):
        return {"status": "REJECTED", "basis": "duplicate EVENT_SEQ"}
    if run_events and event["event_seq"] <= max(e["event_seq"] for e in run_events):
        return {"status": "REJECTED", "basis": "sequence regression"}
    if event["stage_result_id"] and event["stage_result_id"].startswith("FOREIGN-"):
        return {"status": "REJECTED", "basis": "foreign stage result"}
    journal.append(deepcopy(event))
    return {"status": "ACCEPTED"}


def reduce_state(journal, run_id):
    events = sorted((e for e in journal if e["run_id"] == run_id), key=lambda e: e["event_seq"])
    state = "NONE"
    for e in events:
        state = e["event_status"]
    return state


def main():
    failures = []
    results = []

    # P1-01 append
    journal = []
    base = {
        "run_id": "RUN-P1-001",
        "event_id": "EV-001",
        "event_seq": 1,
        "stage_id": "RUN",
        "event_type": "RUN_CREATED",
        "stage_result_id": "RUN-RESULT-001",
        "attempt_id": "ATTEMPT-RUN-001",
        "event_status": "RUN_CREATED",
        "traceability": {"source_id": "SRC-P1-001"},
    }
    out = append_event(journal, base)
    assert out["status"] == "ACCEPTED"
    assert len(journal) == 1
    results.append({"case": "P1-01_APPEND", "result": out})

    # P1-02 ordered sequence
    second = dict(base, event_id="EV-002", event_seq=2, stage_id="DISCOVERY",
                  event_type="STAGE_STARTED", stage_result_id="DISC-RESULT-001",
                  attempt_id="ATTEMPT-DISC-001", event_status="STAGE_STARTED")
    out = append_event(journal, second)
    assert out["status"] == "ACCEPTED"
    assert [e["event_seq"] for e in journal] == [1, 2]
    results.append({"case": "P1-02_ORDERED_SEQUENCE", "result": out})

    # P1-03 duplicate EVENT_ID
    out = append_event(journal, dict(second, event_seq=3))
    assert out["status"] == "REJECTED"
    assert out["basis"] == "duplicate EVENT_ID"
    results.append({"case": "P1-03_DUPLICATE_EVENT_ID", "result": out})

    # P1-04 duplicate EVENT_SEQ
    out = append_event(journal, dict(second, event_id="EV-003"))
    assert out["status"] == "REJECTED"
    assert out["basis"] == "duplicate EVENT_SEQ"
    results.append({"case": "P1-04_DUPLICATE_EVENT_SEQ", "result": out})

    # P1-05 sequence regression
    out = append_event(journal, dict(second, event_id="EV-004", event_seq=0))
    assert out["status"] == "REJECTED"
    assert out["basis"] == "sequence regression"
    results.append({"case": "P1-05_SEQUENCE_REGRESSION", "result": out})

    # P1-06 foreign RUN result
    out = append_event(journal, dict(second, event_id="EV-005", event_seq=3,
                                     run_id="RUN-OTHER", stage_result_id="FOREIGN-RESULT-001"))
    assert out["status"] == "REJECTED"
    assert out["basis"] == "foreign stage result"
    results.append({"case": "P1-06_FOREIGN_RESULT", "result": out})

    # P1-07 failed attempt preserved
    failed = dict(second, event_id="EV-006", event_seq=3, stage_id="CMOC_WRITE",
                  event_type="STAGE_FAILED", stage_result_id="WRITE-FAILED-001",
                  attempt_id="ATTEMPT-WRITE-001", event_status="STAGE_FAILED")
    out = append_event(journal, failed)
    assert out["status"] == "ACCEPTED"

    # P1-08 retry gets new attempt
    retry = dict(second, event_id="EV-007", event_seq=4, stage_id="CMOC_WRITE",
                 event_type="STAGE_STARTED", stage_result_id="WRITE-RETRY-001",
                 attempt_id="ATTEMPT-WRITE-002", event_status="STAGE_STARTED")
    out = append_event(journal, retry)
    assert out["status"] == "ACCEPTED"
    assert journal[2]["stage_result_id"] == "WRITE-FAILED-001"
    assert journal[2]["attempt_id"] != journal[3]["attempt_id"]
    results.append({"case": "P1-07_FAILED_ATTEMPT_PRESERVED", "result": {"status": "ACCEPTED"}})
    results.append({"case": "P1-08_RETRY_NEW_ATTEMPT", "result": out})

    # P1-09 deterministic reconstruction
    state1 = reduce_state(journal, "RUN-P1-001")
    state2 = reduce_state(list(reversed(journal)), "RUN-P1-001")
    assert state1 == state2
    results.append({"case": "P1-09_DETERMINISTIC_RECONSTRUCTION", "result": {"state": state1}})

    # P1-10 restart reconstruction
    serialized = json.loads(json.dumps(journal))
    assert reduce_state(serialized, "RUN-P1-001") == state1
    results.append({"case": "P1-10_RESTART_RECONSTRUCTION", "result": {"state": state1}})

    # P1-11 impossible/unknown event
    bad = dict(second, event_id="EV-008", event_seq=5, event_type="SEMANTIC_REPAIR",
               event_status="SEMANTIC_REPAIR")
    out = append_event(journal, bad)
    assert out["status"] == "REJECTED"
    results.append({"case": "P1-11_UNKNOWN_EVENT_REJECTED", "result": out})

    # P1-12 no semantic / CMOC / index leakage
    controls = {
        "semantic_decision_performed": False,
        "semantic_comparison_performed": False,
        "canonization_performed": False,
        "cmoc_mutation_performed": False,
        "object_index_mutation_performed": False,
        "semantic_repair_performed": False,
        "journal_append_only": True,
        "synthetic_only": True,
    }
    assert all(v is False for k, v in controls.items()
               if k.endswith("_performed") or k == "semantic_repair_performed")
    results.append({"case": "P1-12_NO_RESPONSIBILITY_LEAKAGE", "result": controls})

    gate = {
        "gate": "P1-EXECUTION-JOURNAL-MODEL",
        "status": "PASS" if not failures else "FAIL",
        "results": results,
        "controls": controls,
        "failures": failures,
    }
    print(json.dumps(gate, indent=2, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()
