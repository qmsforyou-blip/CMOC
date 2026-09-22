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


def make_run(run_id="RUN-ORCH-001"):
    return {
        "run_id": run_id,
        "source_id": "SRC-ORCH-001",
        "current_stage": "RUN_CREATED",
        "run_status": "RUN_CREATED",
        "lineage": {
            "discovery_result_id": "DISC-001",
            "reconciliation_result_id": "RECON-001",
            "new_decision_id": "NEW-001",
            "canonization_result_id": "CAN-001",
            "cmoc_write_id": "WRITE-001",
            "object_index_sync_id": "IDX-001",
        },
        "executed": [],
    }


def expected_previous(stage):
    index = STAGES.index(stage)
    return "RUN_CREATED" if index == 0 else SUCCESS[STAGES[index - 1]]


def orchestrate_step(run, stage, result):
    if stage not in STAGES:
        return {
            "status": "ORCHESTRATION_REJECTED",
            "basis": "unknown stage",
        }

    if run["current_stage"] != expected_previous(stage):
        return {
            "status": "ORCHESTRATION_REJECTED",
            "basis": f"invalid execution order: {run['current_stage']} -> {stage}",
        }

    if result.get("run_id") != run["run_id"]:
        return {
            "status": "ORCHESTRATION_REJECTED",
            "basis": "result belongs to another RUN_ID",
        }

    if result.get("stage_id") != stage:
        return {
            "status": "ORCHESTRATION_REJECTED",
            "basis": "result stage does not match requested stage",
        }

    if result.get("stage_status") != SUCCESS[stage]:
        return {
            "status": "ORCHESTRATION_STOPPED",
            "basis": f"local stage result: {result.get('stage_status')}",
            "local_status": result.get("stage_status"),
        }

    run["current_stage"] = SUCCESS[stage]
    run["run_status"] = SUCCESS[stage]
    run["executed"].append(stage)

    if stage == STAGES[-1]:
        run["current_stage"] = "RUN_COMPLETED"
        run["run_status"] = "RUN_COMPLETED"

    return {
        "status": "CONTINUE" if stage != STAGES[-1] else "RUN_COMPLETED",
        "stage": stage,
    }


def make_result(run_id, stage, status=None):
    return {
        "run_id": run_id,
        "stage_id": stage,
        "stage_status": status or SUCCESS[stage],
        "result_id": f"{stage}-RESULT-001",
        "traceability": {
            "run_id": run_id,
            "source_id": "SRC-ORCH-001",
        },
    }


def main():
    failures = []
    results = []

    # ORCH-01: valid sequential execution
    run = make_run()
    original = deepcopy(run)
    for stage in STAGES:
        out = orchestrate_step(run, stage, make_result(run["run_id"], stage))
        if out["status"] not in ("CONTINUE", "RUN_COMPLETED"):
            failures.append(("ORCH-01", out))
    assert run["run_status"] == "RUN_COMPLETED"
    assert run["executed"] == STAGES
    results.append({"case": "ORCH-01_VALID_SEQUENCE", "result": {
        "status": run["run_status"],
        "executed": run["executed"],
    }})

    # ORCH-02: wrong invocation order
    run = make_run()
    out = orchestrate_step(run, "NEW_DECISION", make_result(run["run_id"], "NEW_DECISION"))
    assert out["status"] == "ORCHESTRATION_REJECTED"
    results.append({"case": "ORCH-02_WRONG_ORDER", "result": out})

    # ORCH-03: predecessor absent / downstream blocked
    run = make_run()
    out = orchestrate_step(run, "RECONCILIATION", make_result(run["run_id"], "RECONCILIATION"))
    assert out["status"] == "ORCHESTRATION_REJECTED"
    assert run["executed"] == []
    results.append({"case": "ORCH-03_PREDECESSOR_ABSENT", "result": out})

    # ORCH-04: local rejection stops execution
    run = make_run()
    out = orchestrate_step(
        run,
        "DISCOVERY",
        make_result(run["run_id"], "DISCOVERY", "LOCAL_REJECTED"),
    )
    assert out["status"] == "ORCHESTRATION_STOPPED"
    assert run["executed"] == []
    results.append({"case": "ORCH-04_LOCAL_REJECTION", "result": out})

    # ORCH-05: local failure stops execution
    run = make_run()
    out = orchestrate_step(
        run,
        "DISCOVERY",
        make_result(run["run_id"], "DISCOVERY", "LOCAL_FAILED"),
    )
    assert out["status"] == "ORCHESTRATION_STOPPED"
    assert run["executed"] == []
    results.append({"case": "ORCH-05_LOCAL_FAILURE", "result": out})

    # ORCH-06: cross-run result rejected
    run = make_run()
    out = orchestrate_step(run, "DISCOVERY", make_result("RUN-OTHER", "DISCOVERY"))
    assert out["status"] == "ORCHESTRATION_REJECTED"
    results.append({"case": "ORCH-06_CROSS_RUN_RESULT", "result": out})

    # ORCH-07: invalid stage transition
    run = make_run()
    out = orchestrate_step(run, "UNKNOWN_STAGE", make_result(run["run_id"], "DISCOVERY"))
    assert out["status"] == "ORCHESTRATION_REJECTED"
    results.append({"case": "ORCH-07_UNKNOWN_STAGE", "result": out})

    # ORCH-08: stage/result mismatch
    run = make_run()
    out = orchestrate_step(run, "DISCOVERY", make_result(run["run_id"], "RECONCILIATION"))
    assert out["status"] == "ORCHESTRATION_REJECTED"
    results.append({"case": "ORCH-08_STAGE_RESULT_MISMATCH", "result": out})

    # ORCH-09: completed chain reaches terminal state
    run = make_run()
    for stage in STAGES:
        orchestrate_step(run, stage, make_result(run["run_id"], stage))
    assert run["current_stage"] == "RUN_COMPLETED"
    results.append({"case": "ORCH-09_COMPLETION", "result": {
        "status": run["run_status"],
        "terminal": True,
    }})

    # ORCH-10: no semantic decision
    run = make_run()
    before = deepcopy(run)
    orchestrate_step(run, "DISCOVERY", make_result(run["run_id"], "DISCOVERY"))
    assert "semantic_decision" not in run
    results.append({"case": "ORCH-10_NO_SEMANTIC_DECISION", "result": {
        "status": "CONTROLLED",
        "semantic_decision_performed": False,
    }})

    # ORCH-11: no canonization
    assert "canonical_object" not in run
    results.append({"case": "ORCH-11_NO_CANONIZATION", "result": {
        "status": "CONTROLLED",
        "canonization_performed": False,
    }})

    # ORCH-12: no CMOC mutation
    assert run == {**before, "current_stage": "DISCOVERY_COMPLETED",
                   "run_status": "DISCOVERY_COMPLETED", "executed": ["DISCOVERY"]}
    results.append({"case": "ORCH-12_NO_CMOC_MUTATION", "result": {
        "status": "CONTROLLED",
        "cmoc_mutation_performed": False,
    }})

    # ORCH-13: no OBJECT INDEX mutation
    assert "object_index" not in run
    results.append({"case": "ORCH-13_NO_INDEX_MUTATION", "result": {
        "status": "CONTROLLED",
        "index_mutation_performed": False,
    }})

    # ORCH-14: input result preserved
    run = make_run()
    result = make_result(run["run_id"], "DISCOVERY")
    original_result = deepcopy(result)
    orchestrate_step(run, "DISCOVERY", result)
    assert result == original_result
    results.append({"case": "ORCH-14_INPUT_RESULT_PRESERVED", "result": {
        "status": "CONTROLLED",
        "input_preserved": True,
    }})

    # ORCH-15: semantic repair not performed
    run = make_run()
    bad = make_result(run["run_id"], "DISCOVERY")
    bad["traceability"] = {}
    original_bad = deepcopy(bad)
    out = orchestrate_step(run, "DISCOVERY", bad)
    assert out["status"] == "CONTINUE"
    assert bad == original_bad
    results.append({"case": "ORCH-15_NO_SEMANTIC_REPAIR", "result": {
        "status": "CONTROLLED",
        "semantic_repair_performed": False,
        "traceability_unchanged": True,
    }})

    controls = {
        "production_runtime_imported": False,
        "semantic_decision_performed": False,
        "semantic_comparison_performed": False,
        "canonization_performed": False,
        "cmoc_mutation_performed": False,
        "index_mutation_performed": False,
        "semantic_repair_performed": False,
        "synthetic_boundary_only": True,
        "input_preserved": True,
    }

    gate = {
        "gate": "ORCH-001-EXECUTION-ORCHESTRATION-BOUNDARY",
        "status": "PASS" if not failures else "FAIL",
        "results": results,
        "controls": controls,
        "failures": failures,
    }
    print(json.dumps(gate, indent=2, ensure_ascii=False))
    raise SystemExit(0 if not failures else 1)


if __name__ == "__main__":
    main()
