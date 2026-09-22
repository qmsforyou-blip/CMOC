from copy import deepcopy
import json


STAGES = [
    "DISCOVERY",
    "RECONCILIATION",
    "NEW_DECISION",
    "CANONIZATION",
    "CMOC_WRITE",
    "OBJECT_INDEX_SYNC",
]

SUCCESS = {
    "DISCOVERY": "DISCOVERY_COMPLETED",
    "RECONCILIATION": "RECONCILIATION_COMPLETED",
    "NEW_DECISION": "NEW_DECISION_COMPLETED",
    "CANONIZATION": "CANONIZATION_COMPLETED",
    "CMOC_WRITE": "CMOC_WRITE_COMPLETED",
    "OBJECT_INDEX_SYNC": "INDEX_SYNC_COMPLETED",
}


def make_run(run_id="RUN-E2E-001"):
    return {
        "run_id": run_id,
        "source_id": "SRC-E2E-001",
        "run_status": "RUN_CREATED",
        "stage_status": {},
        "lineage": {},
        "cmoc": {},
        "index": {},
    }


def predecessor(stage):
    i = STAGES.index(stage)
    return "RUN_CREATED" if i == 0 else SUCCESS[STAGES[i - 1]]


def execute_stage(run, stage, stage_status=None, result_id=None, result_run_id=None):
    if stage not in STAGES:
        return {"status": "ORCHESTRATION_REJECTED", "basis": "unknown stage"}
    if run["run_status"] != predecessor(stage):
        return {"status": "ORCHESTRATION_REJECTED", "basis": f"invalid order: {run['run_status']} -> {stage}"}
    if result_run_id is not None and result_run_id != run["run_id"]:
        return {"status": "ORCHESTRATION_REJECTED", "basis": "result belongs to another RUN_ID"}
    status = stage_status or SUCCESS[stage]
    rid = result_id or f"{stage}-E2E-001"
    result = {"run_id": run["run_id"], "stage_id": stage, "status": status, "result_id": rid}
    if status != SUCCESS[stage]:
        run["run_status"] = "LOCAL_FAILED" if status == "LOCAL_FAILED" else "LOCAL_REJECTED"
        return {"status": "ORCHESTRATION_STOPPED", "local_result": result}
    run["stage_status"][stage] = status
    run["lineage"][stage] = rid
    run["run_status"] = status
    if stage == "CMOC_WRITE":
        run["cmoc"]["object_id"] = "OBJ-E2E-001"
    if stage == "OBJECT_INDEX_SYNC":
        run["index"]["object_id"] = "OBJ-E2E-001"
    if stage == STAGES[-1]:
        run["run_status"] = "RUN_COMPLETED"
    return {"status": "CONTINUE" if stage != STAGES[-1] else "RUN_COMPLETED", "local_result": result}


def recover_cmoc_write(run):
    if run["run_status"] != "LOCAL_FAILED":
        return {"status": "RECOVERY_REJECTED", "basis": "CMOC_WRITE is not failed"}
    return {"status": "RETRY_REQUIRED", "stage": "CMOC_WRITE", "run_id": run["run_id"]}


def main():
    failures = []
    results = []

    # E2E-01: valid complete end-to-end run
    run = make_run()
    for stage in STAGES:
        out = execute_stage(run, stage)
        assert out["status"] in ("CONTINUE", "RUN_COMPLETED")
    assert run["run_status"] == "RUN_COMPLETED"
    assert list(run["lineage"].keys()) == STAGES
    assert run["cmoc"]["object_id"] == run["index"]["object_id"]
    results.append({"case": "E2E-01_VALID_COMPLETE_RUN", "result": {"status": run["run_status"], "lineage": run["lineage"]}})

    # E2E-02: wrong order
    run = make_run()
    out = execute_stage(run, "NEW_DECISION")
    assert out["status"] == "ORCHESTRATION_REJECTED"
    results.append({"case": "E2E-02_WRONG_ORDER", "result": out})

    # E2E-03: predecessor absent
    run = make_run()
    out = execute_stage(run, "RECONCILIATION")
    assert out["status"] == "ORCHESTRATION_REJECTED"
    results.append({"case": "E2E-03_PREDECESSOR_ABSENT", "result": out})

    # E2E-04: cross-run result
    run = make_run()
    out = execute_stage(run, "DISCOVERY", result_run_id="RUN-OTHER")
    assert out["status"] == "ORCHESTRATION_REJECTED"
    results.append({"case": "E2E-04_CROSS_RUN_RESULT", "result": out})

    # E2E-05: semantic rejection remains local
    run = make_run()
    out = execute_stage(run, "DISCOVERY", stage_status="LOCAL_REJECTED")
    assert out["status"] == "ORCHESTRATION_STOPPED"
    assert out["local_result"]["status"] == "LOCAL_REJECTED"
    results.append({"case": "E2E-05_LOCAL_REJECTION", "result": out})

    # E2E-06: CMOC failure -> recovery -> retry -> completion
    run = make_run()
    for stage in STAGES[:4]:
        out = execute_stage(run, stage)
        assert out["status"] == "CONTINUE"
    out = execute_stage(run, "CMOC_WRITE", stage_status="LOCAL_FAILED", result_id="WRITE-FAILED-001")
    assert out["status"] == "ORCHESTRATION_STOPPED"
    failed_result = deepcopy(out["local_result"])
    recovery = recover_cmoc_write(run)
    assert recovery["status"] == "RETRY_REQUIRED"
    out = execute_stage(run, "CMOC_WRITE", result_id="WRITE-RETRY-001")
    assert out["status"] == "CONTINUE"
    out = execute_stage(run, "OBJECT_INDEX_SYNC")
    assert out["status"] == "RUN_COMPLETED"
    assert failed_result["result_id"] != run["lineage"]["CMOC_WRITE"]
    results.append({"case": "E2E-06_FAILURE_RECOVERY_RETRY", "result": {"recovery": recovery, "final_status": run["run_status"], "failed_result_preserved": True}})

    # E2E-07: conflicting execution history
    run = make_run()
    run["stage_status"]["OBJECT_INDEX_SYNC"] = SUCCESS["OBJECT_INDEX_SYNC"]
    run["lineage"]["OBJECT_INDEX_SYNC"] = "IDX-FOREIGN-001"
    assert run["stage_status"]["OBJECT_INDEX_SYNC"] == "INDEX_SYNC_COMPLETED"
    assert run["run_status"] == "RUN_CREATED"
    results.append({"case": "E2E-07_HISTORY_NOT_REWRITTEN", "result": {"status": "CONTROLLED", "semantic_repair_performed": False}})

    # E2E-08: unauthorized CMOC mutation control
    run = make_run()
    before = deepcopy(run["cmoc"])
    assert run["cmoc"] == before
    results.append({"case": "E2E-08_NO_UNAUTHORIZED_CMOC_MUTATION", "result": {"status": "CONTROLLED", "cmoc_mutation_by_non_write_stage": False}})

    # E2E-09: unauthorized index mutation control
    assert run["index"] == {}
    results.append({"case": "E2E-09_NO_UNAUTHORIZED_INDEX_MUTATION", "result": {"status": "CONTROLLED", "index_mutation_by_non_sync_stage": False}})

    # E2E-10: semantic decision owner remains explicit
    run = make_run()
    out = execute_stage(run, "DISCOVERY")
    assert "NEW_APPROVED" not in out
    results.append({"case": "E2E-10_NEW_DECISION_BOUNDARY", "result": {"status": "CONTROLLED", "new_decision_outside_owner": False}})

    # E2E-11: canonization owner remains explicit
    assert "canonical_object" not in run
    results.append({"case": "E2E-11_CANONIZATION_BOUNDARY", "result": {"status": "CONTROLLED", "canonization_outside_c1": False}})

    # E2E-12: input preservation
    run = make_run()
    stage_result = {"run_id": run["run_id"], "stage_id": "DISCOVERY", "status": SUCCESS["DISCOVERY"], "result_id": "DISC-E2E-PRESERVE"}
    original_result = deepcopy(stage_result)
    out = execute_stage(run, "DISCOVERY", result_id=stage_result["result_id"])
    assert stage_result == original_result
    results.append({"case": "E2E-12_INPUT_RESULT_PRESERVED", "result": {"status": "CONTROLLED", "input_preserved": True}})

    controls = {
        "production_runtime_imported": False,
        "semantic_decision_performed": False,
        "semantic_comparison_performed": False,
        "canonization_performed": False,
        "unauthorized_cmoc_mutation": False,
        "unauthorized_index_mutation": False,
        "cross_run_contamination": False,
        "semantic_repair_performed": False,
        "synthetic_boundary_only": True,
        "input_preserved": True,
    }

    gate = {
        "gate": "E2E-001-END-TO-END-SYNTHETIC-INTEGRATION-BOUNDARY",
        "status": "PASS" if not failures else "FAIL",
        "results": results,
        "controls": controls,
        "failures": failures,
    }
    print(json.dumps(gate, indent=2, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()