"""Runtime -> DISCOVERY adapter wiring gate.

Uses the real production adapter and real MACHINE-SOURCE-001 implementation.
The test deliberately removes LLM credentials so the semantic chain must fail
explicitly at execution; it must not synthesize a semantic result.
"""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path

from discovery_production_adapter import run_discovery_adapter
from production_adapter_runtime import ProductionAdapter, ProductionAdapterRegistry
from run_superagent import start_run


def package():
    return {
        "package_id": "SOURCE-PACKAGE-DISCOVERY-WIRING-001",
        "source_id": "SRC-DISCOVERY-WIRING-001",
        "source_name": "DISCOVERY WIRING TEST SOURCE",
        "source_package_status": "COMPLETE",
        "fragments": [
            {"fragment_id": "F-001", "ref": "fragment-001", "text": "controlled"},
        ],
    }


def main():
    old_key = os.environ.pop("LLM_API_KEY", None)
    old_model = os.environ.pop("LLM_MODEL", None)
    try:
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            source_path = root / "source_package.json"
            db_path = root / "runtime.sqlite"
            source_path.write_text(
                json.dumps(package(), ensure_ascii=False),
                encoding="utf-8",
            )

            registry = ProductionAdapterRegistry()
            registry.register(
                ProductionAdapter(
                    stage_id="DISCOVERY",
                    implementation=run_discovery_adapter,
                )
            )

            out = start_run(
                source_package_path=str(source_path),
                db_path=str(db_path),
                run_id="RUN-DISCOVERY-WIRING-001",
                registry=registry,
            )

            assert out["status"] == "ADAPTER_EXECUTION_FAILED"
            assert out["adapter"]["error_type"] in {
                "M01LLMError",
                "M02LLMError",
                "M03LLMError",
                "M04LLMError",
                "M05LLMError",
                "M06LLMError",
                "M07LLMError",
                "M08LLMError",
            }

            from runtime_state_store import RuntimeStateStore
            store = RuntimeStateStore(str(db_path))
            events = store.read_journal("RUN-DISCOVERY-WIRING-001")
            assert [e.event_type for e in events] == [
                "RUN_CREATED",
                "STAGE_STARTED",
                "STAGE_FAILED",
            ]
            state = store.get_state("RUN-DISCOVERY-WIRING-001")
            assert state is not None
            assert state.run_status == "ACTIVE"
            assert state.current_stage_id == "DISCOVERY"
            store.close()

            print(json.dumps({
                "gate": "RUNTIME-DISCOVERY-ADAPTER-WIRING",
                "status": "PASS",
                "result": out["status"],
                "events": [e.event_type for e in events],
                "synthetic_adapter_used": False,
                "cmoc_access": "NONE",
                "query_access": "NONE",
            }, ensure_ascii=False, indent=2))
    finally:
        if old_key is not None:
            os.environ["LLM_API_KEY"] = old_key
        if old_model is not None:
            os.environ["LLM_MODEL"] = old_model


if __name__ == "__main__":
    main()
