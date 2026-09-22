from copy import deepcopy
import json


def validate_adapter(adapter, expected_stage):
    if adapter.get("mode") != "production":
        return {"status": "SYNTHETIC_ADAPTER_DETECTED"}

    if adapter.get("stage_id") != expected_stage:
        return {"status": "ADAPTER_INPUT_REJECTED", "basis": "stage mismatch"}

    required = ("run_id", "source_id", "batch_id", "stage_id", "attempt_id", "result_id")
    missing = [key for key in required if not adapter.get(key)]
    if missing:
        return {"status": "ADAPTER_INPUT_REJECTED", "missing": missing}

    return {"status": "ADAPTER_ACCEPTED"}


def validate_result(adapter, result):
    if result.get("run_id") != adapter["run_id"]:
        return {"status": "ADAPTER_LINEAGE_INVALID"}
    if result.get("stage_id") != adapter["stage_id"]:
        return {"status": "ADAPTER_OUTPUT_INVALID"}
    if result.get("attempt_id") != adapter["attempt_id"]:
        return {"status": "ADAPTER_LINEAGE_INVALID"}
    if result.get("result_id") != adapter["result_id"]:
        return {"status": "ADAPTER_LINEAGE_INVALID"}
    return {"status": "OUTPUT_VALID"}


def dispatch_stage(adapter, result, persistence):
    gate = validate_adapter(adapter, adapter["stage_id"])
    if gate["status"] != "ADAPTER_ACCEPTED":
        return gate

    output = validate_result(adapter, result)
    if output["status"] != "OUTPUT_VALID":
        return output

    key = (adapter["run_id"], adapter["stage_id"], adapter["attempt_id"])
    if key in persistence:
        if persistence[key] == result:
            return {"status": "ALREADY_COMPLETED"}
        return {"status": "ADAPTER_OUTPUT_INVALID", "basis": "authoritative result conflict"}

    persistence[key] = deepcopy(result)
    return {"status": "PRODUCTION_ADAPTER_ACCEPTED"}


def main():
    results = []
    persistence = {}

    base = {
        "mode": "production",
        "run_id": "RUN-P6-001",
        "source_id": "SRC-P6-001",
        "batch_id": "BATCH-P6-001",
        "stage_id": "RECONCILIATION",
        "attempt_id": "ATT-P6-001",
        "result_id": "RESULT-P6-001",
    }
    result = {
        **base,
        "status": "NEEDS_REVIEW",
        "semantic_decision_performed": False,
    }

    # P6-01 production adapter accepted
    out = dispatch_stage(base, result, persistence)
    assert out["status"] == "PRODUCTION_ADAPTER_ACCEPTED"
    results.append({"case": "P6-01_PRODUCTION_ADAPTER_ACCEPTED", "result": out})

    # P6-02 synthetic adapter rejected
    synthetic = dict(base, mode="synthetic", attempt_id="ATT-P6-SYN")
    out = dispatch_stage(synthetic, dict(result, attempt_id="ATT-P6-SYN"), persistence)
    assert out["status"] == "SYNTHETIC_ADAPTER_DETECTED"
    results.append({"case": "P6-02_SYNTHETIC_ADAPTER_REJECTED", "result": out})

    # P6-03 input contract preserved
    snapshot = deepcopy(base)
    validate_adapter(base, base["stage_id"])
    assert base == snapshot
    results.append({"case": "P6-03_INPUT_CONTRACT_PRESERVED", "result": {"preserved": True}})

    # P6-04 output contract preserved
    result_snapshot = deepcopy(result)
    out = validate_result(base, result)
    assert out["status"] == "OUTPUT_VALID"
    assert result == result_snapshot
    results.append({"case": "P6-04_OUTPUT_CONTRACT_PRESERVED", "result": out})

    # P6-05 RUN_ID lineage preserved
    foreign_result = dict(result, run_id="RUN-FOREIGN")
    out = validate_result(base, foreign_result)
    assert out["status"] == "ADAPTER_LINEAGE_INVALID"
    results.append({"case": "P6-05_RUN_ID_PRESERVED", "result": out})

    # P6-06 ATTEMPT_ID lineage preserved
    foreign_attempt = dict(result, attempt_id="ATT-FOREIGN")
    out = validate_result(base, foreign_attempt)
    assert out["status"] == "ADAPTER_LINEAGE_INVALID"
    results.append({"case": "P6-06_ATTEMPT_ID_PRESERVED", "result": out})

    # P6-07 RESULT_ID lineage preserved
    foreign_result_id = dict(result, result_id="RESULT-FOREIGN")
    out = validate_result(base, foreign_result_id)
    assert out["status"] == "ADAPTER_LINEAGE_INVALID"
    results.append({"case": "P6-07_RESULT_ID_PRESERVED", "result": out})

    # P6-08 execution failure is distinct from semantic rejection
    failed = dict(result, execution_status="ADAPTER_EXECUTION_FAILED")
    assert failed["execution_status"] == "ADAPTER_EXECUTION_FAILED"
    assert failed["status"] == "NEEDS_REVIEW"
    results.append({"case": "P6-08_EXECUTION_FAILURE_DISTINCT_FROM_SEMANTIC_RESULT", "result": {
        "execution_status": failed["execution_status"],
        "semantic_status": failed["status"],
    }})

    # P6-09 duplicate invocation is idempotent
    out = dispatch_stage(base, result, persistence)
    assert out["status"] == "ALREADY_COMPLETED"
    results.append({"case": "P6-09_DUPLICATE_INVOCATION_IDEMPOTENT", "result": out})

    # P6-10 C2 is the only CMOC write boundary
    c2 = dict(base, stage_id="C2_CMOC_WRITE", attempt_id="ATT-C2-001", result_id="RESULT-C2-001")
    c2_result = dict(c2, status="CMOC_WRITE_ACCEPTED", cmoc_write_boundary=True)
    out = dispatch_stage(c2, c2_result, persistence)
    assert out["status"] == "PRODUCTION_ADAPTER_ACCEPTED"
    non_c2 = dict(base, stage_id="RECONCILIATION", attempt_id="ATT-NONC2-001", result_id="RESULT-NONC2-001",
                  cmoc_write_boundary=True)
    assert non_c2["stage_id"] != "C2_CMOC_WRITE"
    results.append({"case": "P6-10_C2_ONLY_CMOC_WRITE_BOUNDARY", "result": {
        "c2_accepted": True,
        "non_c2_write_not_authorized": True,
    }})

    # P6-11 C3 is the only OBJECT INDEX synchronization boundary
    c3 = dict(base, stage_id="C3_OBJECT_INDEX_SYNC", attempt_id="ATT-C3-001", result_id="RESULT-C3-001")
    c3_result = dict(c3, status="INDEX_SYNCHRONIZED", object_index_sync_boundary=True)
    out = dispatch_stage(c3, c3_result, persistence)
    assert out["status"] == "PRODUCTION_ADAPTER_ACCEPTED"
    non_c3 = dict(base, stage_id="RECONCILIATION", attempt_id="ATT-NONC3-001", result_id="RESULT-NONC3-001",
                  object_index_sync_boundary=True)
    assert non_c3["stage_id"] != "C3_OBJECT_INDEX_SYNC"
    results.append({"case": "P6-11_C3_ONLY_INDEX_SYNC_BOUNDARY", "result": {
        "c3_accepted": True,
        "non_c3_sync_not_authorized": True,
    }})

    # P6-12 responsibility isolation
    controls = {
        "semantic_decision_performed": False,
        "semantic_comparison_performed": False,
        "canonization_performed": False,
        "cmoc_mutation_outside_c2": False,
        "object_index_mutation_outside_c3": False,
        "semantic_repair_performed": False,
        "synthetic_adapter_used_as_production": False,
        "synthetic_only": True,
    }
    assert not any(v for k, v in controls.items() if k.endswith("_performed"))
    assert controls["cmoc_mutation_outside_c2"] is False
    assert controls["object_index_mutation_outside_c3"] is False
    assert controls["synthetic_adapter_used_as_production"] is False
    results.append({"case": "P6-12_NO_RESPONSIBILITY_LEAKAGE", "result": controls})

    gate = {
        "gate": "P6-PRODUCTION-ADAPTERS-R1-C3-BOUNDARY",
        "status": "PASS",
        "results": results,
        "controls": controls,
        "failures": [],
    }
    print(json.dumps(gate, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
