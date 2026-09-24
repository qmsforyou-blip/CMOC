"""PROD-ENTRY-001 — local manual-start runtime entry point.

The CLI establishes a durable RUN and structurally splits the supplied
SOURCE_PACKAGE. It then checks the production-adapter boundary.

It deliberately does not invent semantic execution when a contracted
production adapter is unavailable.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from production_adapter_runtime import ProductionAdapterRegistry
from runtime_state_store import JournalEvent, RuntimeStateStore


def load_source_package(path: str) -> dict[str, Any]:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    required = {"package_id", "source_id", "source_name", "fragments"}
    missing = sorted(required - set(payload))
    if missing:
        raise ValueError(f"SOURCE_PACKAGE_INVALID: missing {missing}")
    if not isinstance(payload["fragments"], list):
        raise ValueError("SOURCE_PACKAGE_INVALID: fragments must be a list")
    if payload.get("source_package_status", "UNKNOWN") not in {
        "COMPLETE", "PARTIAL", "UNKNOWN"
    }:
        raise ValueError("SOURCE_PACKAGE_INVALID: invalid status")
    return payload


def split_batches(source_package: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "batch_id": f"BATCH-{source_package['source_id']}-{index:03d}",
            "source_id": source_package["source_id"],
            "source_package_id": source_package["package_id"],
            "fragment_id": fragment.get("fragment_id", f"FRAGMENT-{index:03d}"),
            "input_ref": fragment.get("ref", fragment.get("fragment_id", "")),
        }
        for index, fragment in enumerate(source_package["fragments"], start=1)
    ]


def start_run(
    source_package_path: str,
    db_path: str,
    run_id: str,
    registry: ProductionAdapterRegistry,
) -> dict[str, Any]:
    source_package = load_source_package(source_package_path)
    store = RuntimeStateStore(db_path)
    try:
        if store.get_state(run_id) is not None:
            return {
                "status": "RUN_ALREADY_EXISTS",
                "run_id": run_id,
            }

        trace = (
            f"RUN_ID={run_id};"
            f"SOURCE_ID={source_package['source_id']};"
            f"SOURCE_PACKAGE_ID={source_package['package_id']}"
        )
        store.append(
            JournalEvent(
                run_id=run_id,
                event_id=f"EVENT-{run_id}-001",
                event_seq=1,
                stage_id="RUN",
                event_type="RUN_CREATED",
                stage_result_id=f"RUN-RESULT-{run_id}",
                attempt_id=f"ATTEMPT-RUN-{run_id}",
                event_status="ACTIVE",
                traceability=trace,
                source_id=source_package["source_id"],
                batch_id=source_package["package_id"],
            ),
            source_id=source_package["source_id"],
            batch_id=source_package["package_id"],
        )

        batches = split_batches(source_package)

        # The first gate checks the next required production boundary without
        # inventing a semantic result when the adapter is absent.
        probe = registry.get("DISCOVERY")
        if probe is None:
            return {
                "status": "PRODUCTION_ADAPTER_UNAVAILABLE",
                "run_id": run_id,
                "source_id": source_package["source_id"],
                "source_package_id": source_package["package_id"],
                "batches": batches,
            }

        return {
            "status": "PIPELINE_READY",
            "run_id": run_id,
            "source_id": source_package["source_id"],
            "source_package_id": source_package["package_id"],
            "batches": batches,
        }
    finally:
        store.close()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Start a local CMOC/Superagent RUN."
    )
    parser.add_argument("--source-package", required=True)
    parser.add_argument("--db", default="05 SUPERAGENT/runtime.sqlite")
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()

    try:
        out = start_run(
            args.source_package,
            args.db,
            args.run_id,
            ProductionAdapterRegistry(),
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({
            "status": "START_REJECTED",
            "reason": str(exc),
        }, ensure_ascii=False, indent=2))
        return 2

    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if out["status"] in {"PIPELINE_READY", "PRODUCTION_ADAPTER_UNAVAILABLE"} else 1


if __name__ == "__main__":
    raise SystemExit(main())
