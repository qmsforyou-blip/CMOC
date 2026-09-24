"""Crash -> recovery -> resume gate for the local production runtime."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from durable_adapter_persistence import DurableAdapterPersistence
from production_adapter_runtime import ProductionAdapter, ProductionAdapterRegistry
from run_superagent import load_source_package, start_run
from runtime_state_store import JournalEvent, RuntimeStateStore


def source_package() -> dict:
    return {
        "package_id": "SOURCE-PACKAGE-RECOVERY-001",
        "source_id": "SRC-RECOVERY-001",
        "source_name": "RECOVERY TEST SOURCE",
        "source_package_status": "COMPLETE",
        "fragments": [{"fragment_id": "F-001", "ref": "fragment-001"}],
    }


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        source_path = root / "source_package.json"
        db_path = root / "runtime.sqlite"
        source_path.write_text(
            json.dumps(source_package(), ensure_ascii=False),
            encoding="utf-8",
        )

        registry = ProductionAdapterRegistry()
        calls: list[str] = []

        def implementation(envelope):
            calls.append(envelope["attempt_id"])
            return {
                **envelope,
                "status": "ACCEPT",
                "implementation": "RECOVERY_TEST_PRODUCTION_ADAPTER",
            }

        registry.register(ProductionAdapter("DISCOVERY", implementation))

        package = load_source_package(str(source_path))
        store = RuntimeStateStore(str(db_path))
        trace = (
            "RUN_ID=RUN-RECOVERY-001;"
            "SOURCE_ID=SRC-RECOVERY-001;"
            "SOURCE_PACKAGE_ID=SOURCE-PACKAGE-RECOVERY-001"
        )
        store.append(JournalEvent(
            run_id="RUN-RECOVERY-001",
            event_id="EVENT-RUN-RECOVERY-001-001",
            event_seq=1,
            stage_id="RUN",
            event_type="RUN_CREATED",
            stage_result_id="RUN-RESULT-RUN-RECOVERY-001",
            attempt_id="ATTEMPT-RUN-RECOVERY-001",
            event_status="ACTIVE",
            traceability=trace,
            source_id=package["source_id"],
            batch_id=package["package_id"],
        ), source_id=package["source_id"], batch_id=package["package_id"])
        store.append(JournalEvent(
            run_id="RUN-RECOVERY-001",
            event_id="EVENT-RUN-RECOVERY-001-002",
            event_seq=2,
            stage_id="DISCOVERY",
            event_type="STAGE_STARTED",
            stage_result_id="RESULT-DISCOVERY-RUN-RECOVERY-001",
            attempt_id="ATTEMPT-DISCOVERY-RUN-RECOVERY-001",
            event_status="ACTIVE",
            traceability=trace,
            source_id=package["source_id"],
            batch_id=package["package_id"],
        ), source_id=package["source_id"], batch_id=package["package_id"])
        state = store.get_state("RUN-RECOVERY-001")
        assert state is not None
        assert state.run_status == "ACTIVE"
        assert state.current_stage_id == "DISCOVERY"

        # Simulated process crash: close the process-owned store without
        # writing STAGE_FAILED or RUN_FAILED.
        store.close()

        out = start_run(
            source_package_path=str(source_path),
            db_path=str(db_path),
            run_id="RUN-RECOVERY-001",
            registry=registry,
            resume=True,
        )
        assert out["status"] == "PIPELINE_COMPLETED"
        assert calls == ["ATTEMPT-DISCOVERY-RUN-RECOVERY-001"]
        
        store = RuntimeStateStore(str(db_path))
        events = store.read_journal("RUN-RECOVERY-001")
        event_types = [event.event_type for event in events]
        assert event_types == [
            "RUN_CREATED",
            "STAGE_STARTED",
            "RUN_INCOMPLETE",
            "RECOVERY_REQUESTED",
            "RESUME_ALLOWED",
            "STAGE_STARTED",
            "STAGE_COMPLETED",
            "RUN_COMPLETED",
        ]
        assert store.verify_projection("RUN-RECOVERY-001")
        assert store.get_state("RUN-RECOVERY-001").run_status == "COMPLETED"

        # Prove the adapter result survived a fresh persistence object.
        persistence = DurableAdapterPersistence(store.conn)
        key = (
            "RUN-RECOVERY-001",
            "DISCOVERY",
            "ATTEMPT-DISCOVERY-RUN-RECOVERY-001",
        )
        assert key in persistence
        assert persistence[key]["result_id"] == "RESULT-DISCOVERY-RUN-RECOVERY-001"
        store.close()

    print("RUNTIME RECOVERY TEST: PASS")


if __name__ == "__main__":
    main()
