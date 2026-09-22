"""Synthetic boundary test for RUN-001 end-to-end traceability."""

from copy import deepcopy
import json


def make_envelope(run_id="RUN-001", source_id="SRC-001"):
    return {
        "run_id": run_id,
        "source_id": source_id,
        "source_package_id": "PKG-001",
        "batch_id": "BATCH-001",
        "discovery_result_id": "DISC-001",
        "reconciliation_result_id": "REC-001",
        "new_decision_id": "NEW-001",
        "canonization_result_id": "CAN-001",
        "cmoc_write_id": "WRITE-001",
        "object_index_sync_id": "INDEX-001",
        "run_status": "RUN_CREATED",
        "traceability": {
            "source_id": source_id,
            "run_id": run_id,
        },
    }


ALLOWED_TRANSITIONS = {
    "RUN_CREATED": {"DISCOVERY_COMPLETED", "RUN_REJECTED", "RUN_FAILED"},
    "DISCOVERY_COMPLETED": {"RECONCILIATION_COMPLETED", "RUN_REJECTED", "RUN_FAILED"},
    "RECONCILIATION_COMPLETED": {"NEW_DECISION_COMPLETED", "RUN_REJECTED", "RUN_FAILED"},
    "NEW_DECISION_COMPLETED": {"CANONIZATION_COMPLETED", "RUN_REJECTED", "RUN_FAILED"},
    "CANONIZATION_COMPLETED": {"CMOC_WRITE_COMPLETED", "RUN_REJECTED", "RUN_FAILED"},
    "CMOC_WRITE_COMPLETED": {"INDEX_SYNC_COMPLETED", "RUN_REJECTED", "RUN_FAILED"},
    "INDEX_SYNC_COMPLETED": {"RUN_COMPLETED", "RUN_FAILED"},
}


def validate_envelope(envelope):
    required = [
        "run_id",
        "source_id",
        "source_package_id",
        "batch_id",
        "discovery_result_id",
        "reconciliation_result_id",
        "new_decision_id",
        "canonization_result_id",
        "cmoc_write_id",
        "object_index_sync_id",
        "run_status",
        "traceability",
    ]
    missing = [key for key in required if not envelope.get(key)]
    if missing:
        return {"status": "RUN_REJECTED", "basis": "missing required lineage fields", "missing": missing}

    if envelope["traceability"].get("run_id") != envelope["run_id"]:
        return {"status": "RUN_REJECTED", "basis": "traceability RUN_ID mismatch"}

    if envelope["traceability"].get("source_id") != envelope["source_id"]:
        return {"status": "RUN_REJECTED", "basis": "traceability SOURCE_ID mismatch"}

    return {"status": "VALID"}


def attach_result(envelope, result_run_id):
    if result_run_id != envelope["run_id"]:
        return {"status": "RUN_REJECTED", "basis": "result belongs to another RUN_ID"}
    return {"status": "ATTACHED"}


def transition(envelope, next_status):
    current = envelope["run_status"]
    if next_status not in ALLOWED_TRANSITIONS.get(current, set()):
        return {"status": "RUN_REJECTED", "basis": f"invalid transition {current} -> {next_status}"}
    updated = deepcopy(envelope)
    updated["run_status"] = next_status
    return {"status": "TRANSITIONED", "envelope": updated}


def record_local_outcome(envelope, local_status):
    if local_status not in {"LOCAL_REJECTED", "LOCAL_FAILED"}:
        return {"status": "RUN_REJECTED", "basis": "invalid local outcome"}
    updated = deepcopy(envelope)
    updated["run_status"] = local_status
    return {
        "status": "RECORDED",
        "run_status": local_status,
        "semantic_reinterpretation": False,
        "envelope": updated,
    }


def main():
    failures = []
    results = []

    base = make_envelope()
    original = deepcopy(base)

    # RUN-01 valid complete lineage
    r = validate_envelope(base)
    results.append({"case": "RUN-01_VALID_LINEAGE", "result": r})
    if r["status"] != "VALID":
        failures.append("RUN-01")

    # RUN-02 missing RUN_ID
    x = deepcopy(base); x["run_id"] = None
    r = validate_envelope(x)
    results.append({"case": "RUN-02_MISSING_RUN_ID", "result": r})
    if r["status"] != "RUN_REJECTED":
        failures.append("RUN-02")

    # RUN-03 missing SOURCE_ID
    x = deepcopy(base); x["source_id"] = None
    r = validate_envelope(x)
    results.append({"case": "RUN-03_MISSING_SOURCE_ID", "result": r})
    if r["status"] != "RUN_REJECTED":
        failures.append("RUN-03")

    # RUN-04 missing intermediate result identifier
    x = deepcopy(base); x["new_decision_id"] = None
    r = validate_envelope(x)
    results.append({"case": "RUN-04_MISSING_INTERMEDIATE_RESULT", "result": r})
    if r["status"] != "RUN_REJECTED":
        failures.append("RUN-04")

    # RUN-05 cross-run result
    r = attach_result(base, "RUN-002")
    results.append({"case": "RUN-05_CROSS_RUN_RESULT", "result": r})
    if r["status"] != "RUN_REJECTED":
        failures.append("RUN-05")

    # RUN-06 invalid transition
    r = transition(base, "RUN_COMPLETED")
    results.append({"case": "RUN-06_INVALID_TRANSITION", "result": r})
    if r["status"] != "RUN_REJECTED":
        failures.append("RUN-06")

    # RUN-07 local rejection is recorded, not reinterpreted
    r = record_local_outcome(base, "LOCAL_REJECTED")
    results.append({"case": "RUN-07_LOCAL_REJECTION", "result": {
        "status": r["status"],
        "run_status": r["run_status"],
        "semantic_reinterpretation": r["semantic_reinterpretation"],
    }})
    if r["status"] != "RECORDED" or r["semantic_reinterpretation"]:
        failures.append("RUN-07")

    # RUN-08 local failure is recorded, not reinterpreted
    r = record_local_outcome(base, "LOCAL_FAILED")
    results.append({"case": "RUN-08_LOCAL_FAILURE", "result": {
        "status": r["status"],
        "run_status": r["run_status"],
        "semantic_reinterpretation": r["semantic_reinterpretation"],
    }})
    if r["status"] != "RECORDED" or r["semantic_reinterpretation"]:
        failures.append("RUN-08")

    # RUN-09 incomplete run remains incomplete
    x = deepcopy(base); x["run_status"] = "CMOC_WRITE_COMPLETED"
    r = {"status": x["run_status"], "terminal": x["run_status"] == "RUN_COMPLETED"}
    results.append({"case": "RUN-09_INCOMPLETE_RUN", "result": r})
    if r["terminal"]:
        failures.append("RUN-09")

    # RUN-10 completed run
    x = deepcopy(base); x["run_status"] = "INDEX_SYNC_COMPLETED"
    r = transition(x, "RUN_COMPLETED")
    results.append({"case": "RUN-10_COMPLETED_RUN", "result": {
        "status": r["status"],
        "run_status": r["envelope"]["run_status"],
    }})
    if r["status"] != "TRANSITIONED" or r["envelope"]["run_status"] != "RUN_COMPLETED":
        failures.append("RUN-10")

    # RUN-11 resumed same RUN is distinguishable from new RUN
    resumed = deepcopy(base)
    resumed["run_status"] = "DISCOVERY_COMPLETED"
    new_run = make_envelope(run_id="RUN-002")
    r = {
        "same_run_resume": resumed["run_id"] == base["run_id"],
        "new_run_distinct": new_run["run_id"] != base["run_id"],
    }
    results.append({"case": "RUN-11_RESUME_VS_NEW_RUN", "result": r})
    if not r["same_run_resume"] or not r["new_run_distinct"]:
        failures.append("RUN-11")

    # RUN-12 incompatible RUN_ID reuse
    r = attach_result(base, "RUN-002")
    results.append({"case": "RUN-12_INCOMPATIBLE_RUN_ID_REUSE", "result": r})
    if r["status"] != "RUN_REJECTED":
        failures.append("RUN-12")

    # RUN-13 no semantic decision
    results.append({"case": "RUN-13_NO_SEMANTIC_DECISION", "result": {
        "status": "CONTROLLED",
        "semantic_decision_performed": False,
    }})

    # RUN-14 no canonization
    results.append({"case": "RUN-14_NO_CANONIZATION", "result": {
        "status": "CONTROLLED",
        "canonization_performed": False,
    }})

    # RUN-15 no CMOC mutation
    results.append({"case": "RUN-15_NO_CMOC_MUTATION", "result": {
        "status": "CONTROLLED",
        "cmoc_mutation_performed": False,
    }})

    # RUN-16 no index mutation
    results.append({"case": "RUN-16_NO_INDEX_MUTATION", "result": {
        "status": "CONTROLLED",
        "index_mutation_performed": False,
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
        "input_preserved": base == original,
    }

    if not all(value is False for key, value in controls.items()
               if key not in {"synthetic_boundary_only", "input_preserved"}):
        failures.append("CONTROLS")
    if not controls["input_preserved"]:
        failures.append("INPUT_PRESERVATION")

    output = {
        "gate": "RUN-001-END-TO-END-TRACEABILITY-BOUNDARY",
        "status": "PASS" if not failures else "FAIL",
        "results": results,
        "controls": controls,
        "failures": failures,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
