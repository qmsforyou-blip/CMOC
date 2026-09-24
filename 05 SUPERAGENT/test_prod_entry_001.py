"""PROD-ENTRY-001 local runtime entry-point gate.

Proves the real manual-start boundary without pretending that missing
production semantic adapters already exist.
"""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from runtime_state_store import JournalEvent, RuntimeStateStore
from production_adapter_runtime import ProductionAdapterRegistry
from run_superagent import start_run


def package(source_id="SRC-ENTRY-001"):
    return {
        "package_id": "SOURCE-PACKAGE-ENTRY-001",
        "source_id": source_id,
        "source_name": "ENTRY TEST SOURCE",
        "source_package_status": "COMPLETE",
        "fragments": [
            {"fragment_id": "F-001", "ref": "fragment-001"},
            {"fragment_id": "F-002", "ref": "fragment-002"},
        ],
    }


def main():
    results = []

    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        source_path = root / "source_package.json"
        db_path = root / "runtime.sqlite"
        source_path.write_text(
            json.dumps(package(), ensure_ascii=False),
            encoding="utf-8",
        )

        registry = ProductionAdapterRegistry()

        out = start_run(
            source_package_path=str(source_path),
            db_path=str(db_path),
            run_id="RUN-ENTRY-001",
            registry=registry,
        )

        assert out["status"] == "PRODUCTION_ADAPTER_UNAVAILABLE"
        assert out["run_id"] == "RUN-ENTRY-001"
        assert out["source_id"] == "SRC-ENTRY-001"
        assert len(out["batches"]) == 2
        results.append({
            "case": "ENTRY-01_MANUAL_START_VALIDATION_AND_SPLIT",
            "status": out["status"],
            "batches": out["batches"],
        })

        store = RuntimeStateStore(str(db_path))
        state = store.get_state("RUN-ENTRY-001")
        assert state is not None
        assert state.source_id == "SRC-ENTRY-001"
        assert state.batch_id == "SOURCE-PACKAGE-ENTRY-001"
        assert state.run_status == "ACTIVE"
        events = store.read_journal("RUN-ENTRY-001")
        assert [e.event_type for e in events] == ["RUN_CREATED"]
        results.append({
            "case": "ENTRY-02_DURABLE_RUN_CREATED",
            "status": "PASS",
            "event_count": len(events),
        })

        out2 = start_run(
            source_package_path=str(source_path),
            db_path=str(db_path),
            run_id="RUN-ENTRY-001",
            registry=registry,
        )
        assert out2["status"] == "RUN_ALREADY_EXISTS"
        results.append({
            "case": "ENTRY-03_RUN_ID_REUSE_BLOCKED",
            "status": out2["status"],
        })

        store.close()

    controls = {
        "semantic_decision_performed": False,
        "semantic_comparison_performed": False,
        "new_decision_performed": False,
        "canonization_performed": False,
        "cmoc_write_performed": False,
        "object_index_write_performed": False,
        "synthetic_adapter_used": False,
        "automatic_semantic_bypass": False,
    }
    assert not any(controls.values())

    gate = {
        "gate": "PROD-ENTRY-001",
        "status": "PASS",
        "results": results,
        "controls": controls,
        "production_semantic_chain_available": False,
        "note": "The gate proves the entry boundary; it does not claim full R1-R10 production implementation.",
    }
    print(json.dumps(gate, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
