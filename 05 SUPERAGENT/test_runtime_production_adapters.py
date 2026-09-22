import copy

from production_adapter_runtime import ProductionAdapter, ProductionAdapterRegistry


def test_production_adapter_runtime():
    registry = ProductionAdapterRegistry()
    persistence = {}
    calls = []

    def production_impl(envelope):
        calls.append(envelope["attempt_id"])
        return {
            **envelope,
            "status": "NEEDS_REVIEW",
            "implementation": "REAL_PRODUCTION_ADAPTER_TARGET",
        }

    registry.register(ProductionAdapter("RECONCILIATION", production_impl))

    base = {
        "run_id": "RUN-P6-RT-001",
        "source_id": "SRC-P6-RT-001",
        "batch_id": "BATCH-P6-RT-001",
        "stage_id": "RECONCILIATION",
        "attempt_id": "ATT-P6-RT-001",
        "result_id": "RESULT-P6-RT-001",
    }

    # P6-RT-01: production implementation is actually invoked.
    out = registry.invoke(base, persistence)
    assert out.status == "PRODUCTION_ADAPTER_ACCEPTED"
    assert calls == ["ATT-P6-RT-001"]

    # P6-RT-02: synthetic adapter is rejected at registration.
    synthetic = ProductionAdapter("RECONCILIATION", production_impl, mode="synthetic")
    try:
        registry.register(synthetic)
        assert False
    except ValueError:
        pass

    # P6-RT-03: required input contract is enforced.
    missing = dict(base)
    del missing["attempt_id"]
    assert registry.invoke(missing, persistence).status == "ADAPTER_INPUT_REJECTED"

    # P6-RT-04: output and lineage are preserved.
    stored = persistence[(
        base["run_id"], base["stage_id"], base["attempt_id"]
    )]
    assert stored["result_id"] == base["result_id"]
    assert stored["run_id"] == base["run_id"]
    assert stored["attempt_id"] == base["attempt_id"]

    # P6-RT-05: semantic result is passed through, not reinterpreted.
    assert stored["status"] == "NEEDS_REVIEW"

    # P6-RT-06: duplicate invocation is idempotent and does not re-execute.
    assert registry.invoke(base, persistence).status == "ALREADY_COMPLETED"
    assert calls == ["ATT-P6-RT-001"]

    # P6-RT-07: different attempt remains distinct.
    retry = dict(base, attempt_id="ATT-P6-RT-002", result_id="RESULT-P6-RT-002")
    assert registry.invoke(retry, persistence).status == "PRODUCTION_ADAPTER_ACCEPTED"
    assert calls == ["ATT-P6-RT-001", "ATT-P6-RT-002"]

    # P6-RT-08: implementation failure is execution failure, not semantic output.
    def failing_impl(envelope):
        raise RuntimeError("adapter failure")

    registry.register(ProductionAdapter("FAIL_STAGE", failing_impl))
    failed = dict(base, stage_id="FAIL_STAGE", attempt_id="ATT-FAIL",
                  result_id="RESULT-FAIL")
    assert registry.invoke(failed, persistence).status == "ADAPTER_EXECUTION_FAILED"

    # P6-RT-09: lineage mutation is rejected.
    def bad_lineage(envelope):
        return {**envelope, "run_id": "RUN-FOREIGN"}

    registry.register(ProductionAdapter("BAD_STAGE", bad_lineage))
    bad = dict(base, stage_id="BAD_STAGE", attempt_id="ATT-BAD",
               result_id="RESULT-BAD")
    assert registry.invoke(bad, persistence).status == "ADAPTER_LINEAGE_INVALID"

    # P6-RT-10: C2 is explicit CMOC-write boundary.
    cmoc_calls = []
    def c2_impl(envelope):
        cmoc_calls.append(envelope["attempt_id"])
        return {**envelope, "status": "CMOC_WRITE_ACCEPTED",
                "cmoc_write_boundary": True}

    registry.register(ProductionAdapter("C2_CMOC_WRITE", c2_impl))
    c2 = dict(base, stage_id="C2_CMOC_WRITE", attempt_id="ATT-C2",
              result_id="RESULT-C2")
    assert registry.invoke(c2, persistence).status == "PRODUCTION_ADAPTER_ACCEPTED"
    assert cmoc_calls == ["ATT-C2"]

    # P6-RT-11: C3 is explicit OBJECT INDEX sync boundary.
    index_calls = []
    def c3_impl(envelope):
        index_calls.append(envelope["attempt_id"])
        return {**envelope, "status": "INDEX_SYNCHRONIZED",
                "object_index_sync_boundary": True}

    registry.register(ProductionAdapter("C3_OBJECT_INDEX_SYNC", c3_impl))
    c3 = dict(base, stage_id="C3_OBJECT_INDEX_SYNC", attempt_id="ATT-C3",
              result_id="RESULT-C3")
    assert registry.invoke(c3, persistence).status == "PRODUCTION_ADAPTER_ACCEPTED"
    assert index_calls == ["ATT-C3"]

    # P6-RT-12: adapter has no semantic/canonization responsibilities.
    adapter = registry.get("RECONCILIATION")
    assert not hasattr(adapter, "semantic_decision")
    assert not hasattr(adapter, "semantic_comparison")
    assert not hasattr(adapter, "canonization")
    assert not hasattr(adapter, "cmoc_write")
    assert not hasattr(adapter, "object_index_write")

    # Input remains unchanged.
    before = copy.deepcopy(base)
    registry.invoke(base, persistence)
    assert base == before

    print("RUNTIME PRODUCTION ADAPTER TEST: PASS")


if __name__ == "__main__":
    test_production_adapter_runtime()
