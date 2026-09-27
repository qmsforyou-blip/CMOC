"""PILOT-001 control: full runtime wiring with recorded M06 fixture.

Discovery is replaced by a test fixture; this does not prove a live LLM run.
Reconciliation uses the production adapter against a valid, empty OBJECT INDEX.
"""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from production_adapter_runtime import ProductionAdapter, ProductionAdapterRegistry
from reconciliation_production_adapter import run_reconciliation_adapter
from run_superagent import start_run
from runtime_state_store import RuntimeStateStore
from test_reconciliation_input_adapter_src002 import make_fixture


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        source_path = root / "source.json"
        db_path = root / "runtime.sqlite"
        index_path = root / "cmoc_object_index.json"
        source_path.write_text(json.dumps({
            "package_id": "SOURCE-002-PACKAGE-001-CONTROLLED-1-6",
            "source_id": "SRC-002",
            "source_name": "QSB recorded control source",
            "source_package_status": "COMPLETE",
            "fragments": [{"fragment_id": "F-001", "ref": "recorded-M06"}],
        }), encoding="utf-8")
        index_path.write_text(json.dumps({
            "schema": "CMOC-OBJECT-INDEX-001", "version": "0.2", "records": [],
        }), encoding="utf-8")

        def recorded_discovery(envelope):
            return {
                **{key: envelope[key] for key in (
                    "run_id", "source_id", "batch_id", "stage_id", "attempt_id", "result_id"
                )},
                "status": "ACCEPT",
                "discovery": {
                    "status": "ACCEPT", "source_id": "SRC-002",
                    "discovery_run_id": "RECORDED-M06-CONTROL",
                    "results": [make_fixture()],
                },
            }

        registry = ProductionAdapterRegistry()
        registry.register(ProductionAdapter("DISCOVERY", recorded_discovery))
        registry.register(ProductionAdapter(
            "RECONCILIATION",
            lambda envelope: run_reconciliation_adapter({
                **envelope, "index_path": str(index_path),
            }),
        ))
        run_id = "RUN-PILOT-001-RECORDED-M06"
        result = start_run(str(source_path), str(db_path), run_id, registry)
        assert result["status"] == "HUMAN_REVIEW_REQUIRED", result
        assert result["reconciliation_result"]["summary"]["needs_review"] == 7

        expected = [
            "RUN_CREATED", "STAGE_STARTED", "STAGE_COMPLETED",
            "STAGE_STARTED", "STAGE_COMPLETED", "HUMAN_REVIEW_REQUIRED",
        ]
        store = RuntimeStateStore(str(db_path))
        assert [e.event_type for e in store.read_journal(run_id)] == expected
        assert store.get_state(run_id).run_status == "WAITING_HUMAN_REVIEW"
        assert store.get_state(run_id).current_stage_id == "RECONCILIATION"
        assert store.verify_projection(run_id)
        store.close()
        store = RuntimeStateStore(str(db_path))
        assert store.get_state(run_id).run_status == "WAITING_HUMAN_REVIEW"
        assert store.verify_projection(run_id)
        store.close()

        # An upstream request failure can resume the same RUN after recovery.
        failed_once = {"value": True}

        def transient_discovery(envelope):
            if failed_once["value"]:
                failed_once["value"] = False
                raise RuntimeError("SIMULATED_M01_HTTP_429")
            return recorded_discovery(envelope)

        retry_registry = ProductionAdapterRegistry()
        retry_registry.register(ProductionAdapter("DISCOVERY", transient_discovery))
        retry_registry.register(ProductionAdapter(
            "RECONCILIATION",
            lambda envelope: run_reconciliation_adapter({
                **envelope, "index_path": str(index_path),
            }),
        ))
        retry_run_id = "RUN-PILOT-001-RETRY-M01"
        first = start_run(str(source_path), str(db_path), retry_run_id, retry_registry)
        assert first["status"] == "ADAPTER_EXECUTION_FAILED", first
        resumed = start_run(
            str(source_path), str(db_path), retry_run_id, retry_registry, resume=True,
        )
        assert resumed["status"] == "HUMAN_REVIEW_REQUIRED", resumed
        store = RuntimeStateStore(str(db_path))
        assert store.get_state(retry_run_id).run_status == "WAITING_HUMAN_REVIEW"
        assert store.verify_projection(retry_run_id)
        store.close()
        print("PILOT-001 RECORDED M06 WIRING: PASS; 7 NEEDS_REVIEW; durable WAITING_HUMAN_REVIEW; retry PASS")


if __name__ == "__main__":
    main()
