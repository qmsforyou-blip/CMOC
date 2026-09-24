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

from discovery_production_adapter import run_discovery_adapter
from durable_adapter_persistence import DurableAdapterPersistence
from production_adapter_runtime import ProductionAdapter, ProductionAdapterRegistry
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
    resume: bool = False,
) -> dict[str, Any]:
    source_package = load_source_package(source_package_path)
    store = RuntimeStateStore(db_path)
    try:
        existing = store.get_state(run_id)
        recovery = False
        if existing is not None:
            if not resume or existing.run_status in {"COMPLETED", "REJECTED", "FAILED"}:
                return {"status": "RUN_ALREADY_EXISTS", "run_id": run_id}
            if existing.current_stage_id != "DISCOVERY":
                return {"status": "RESUME_BLOCKED", "run_id": run_id, "reason": "no resumable DISCOVERY stage"}
            recovery = True

        trace = (
            f"RUN_ID={run_id};"
            f"SOURCE_ID={source_package['source_id']};"
            f"SOURCE_PACKAGE_ID={source_package['package_id']}"
        )
        if not recovery:
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
        else:
            for event_type, status in (("RUN_INCOMPLETE", "INCOMPLETE"), ("RECOVERY_REQUESTED", "REQUESTED"), ("RESUME_ALLOWED", "ALLOWED")):
                seq = store.next_event_seq(run_id)
                store.append(JournalEvent(
                    run_id=run_id,
                    event_id=f"EVENT-{run_id}-{seq:03d}",
                    event_seq=seq,
                    stage_id="DISCOVERY",
                    event_type=event_type,
                    stage_result_id=existing.current_stage_result_id,
                    attempt_id=existing.current_attempt_id,
                    event_status=status,
                    traceability=trace,
                    source_id=source_package["source_id"],
                    batch_id=source_package["package_id"],
                ), source_id=source_package["source_id"], batch_id=source_package["package_id"])

        batches = split_batches(source_package)

        probe = registry.get("DISCOVERY")
        if probe is None:
            return {
                "status": "PRODUCTION_ADAPTER_UNAVAILABLE",
                "run_id": run_id,
                "source_id": source_package["source_id"],
                "source_package_id": source_package["package_id"],
                "batches": batches,
            }

        attempt_id = f"ATTEMPT-DISCOVERY-{run_id}"
        result_id = f"RESULT-DISCOVERY-{run_id}"
        stage_trace = (
            f"RUN_ID={run_id};"
            f"SOURCE_ID={source_package['source_id']};"
            f"SOURCE_PACKAGE_ID={source_package['package_id']};"
            f"STAGE_ID=DISCOVERY"
        )
        store.append(
            JournalEvent(
                run_id=run_id,
                event_id=f"EVENT-{run_id}-{store.next_event_seq(run_id):03d}",
                event_seq=store.next_event_seq(run_id),
                stage_id="DISCOVERY",
                event_type="STAGE_STARTED",
                stage_result_id=result_id,
                attempt_id=attempt_id,
                event_status="ACTIVE",
                traceability=stage_trace,
                source_id=source_package["source_id"],
                batch_id=source_package["package_id"],
            ),
            source_id=source_package["source_id"],
            batch_id=source_package["package_id"],
        )

        envelope = {
            "run_id": run_id,
            "source_id": source_package["source_id"],
            "batch_id": source_package["package_id"],
            "stage_id": "DISCOVERY",
            "attempt_id": attempt_id,
            "result_id": result_id,
            "source_package": source_package,
            "discovery_run_id": f"{run_id}-DISCOVERY",
        }

        adapter_persistence = DurableAdapterPersistence(store.conn)
        adapter_result = registry.invoke(envelope, adapter_persistence)
        if adapter_result.status not in {
            "PRODUCTION_ADAPTER_ACCEPTED",
            "ALREADY_COMPLETED",
        }:
            event_type = (
                "STAGE_REJECTED"
                if adapter_result.status.endswith("REJECTED")
                else "STAGE_FAILED"
            )
            store.append(
                JournalEvent(
                    run_id=run_id,
                    event_id=f"EVENT-{run_id}-003",
                    event_seq=3,
                    stage_id="DISCOVERY",
                    event_type=event_type,
                    stage_result_id=result_id,
                    attempt_id=attempt_id,
                    event_status=adapter_result.status,
                    traceability=stage_trace,
                    source_id=source_package["source_id"],
                    batch_id=source_package["package_id"],
                ),
                source_id=source_package["source_id"],
                batch_id=source_package["package_id"],
            )
            store.append(
                JournalEvent(
                    run_id=run_id,
                    event_id=f"EVENT-{run_id}-004",
                    event_seq=4,
                    stage_id="DISCOVERY",
                    event_type="RUN_FAILED",
                    stage_result_id=result_id,
                    attempt_id=attempt_id,
                    event_status=adapter_result.status,
                    traceability=stage_trace,
                    source_id=source_package["source_id"],
                    batch_id=source_package["package_id"],
                ),
                source_id=source_package["source_id"],
                batch_id=source_package["package_id"],
            )
            return {
                "status": adapter_result.status,
                "run_id": run_id,
                "source_id": source_package["source_id"],
                "source_package_id": source_package["package_id"],
                "batches": batches,
                "adapter": adapter_result.payload,
            }

        store.append(
            JournalEvent(
                run_id=run_id,
                event_id=f"EVENT-{run_id}-003",
                event_seq=3,
                stage_id="DISCOVERY",
                event_type="STAGE_COMPLETED",
                stage_result_id=result_id,
                attempt_id=attempt_id,
                event_status="COMPLETED",
                traceability=stage_trace,
                source_id=source_package["source_id"],
                batch_id=source_package["package_id"],
            ),
            source_id=source_package["source_id"],
            batch_id=source_package["package_id"],
        )
        store.append(
            JournalEvent(
                run_id=run_id,
                event_id=f"EVENT-{run_id}-004",
                event_seq=4,
                stage_id="DISCOVERY",
                event_type="RUN_COMPLETED",
                stage_result_id=result_id,
                attempt_id=attempt_id,
                event_status="COMPLETED",
                traceability=stage_trace,
                source_id=source_package["source_id"],
                batch_id=source_package["package_id"],
            ),
            source_id=source_package["source_id"],
            batch_id=source_package["package_id"],
        )

        return {
            "status": "PIPELINE_COMPLETED",
            "run_id": run_id,
            "source_id": source_package["source_id"],
            "source_package_id": source_package["package_id"],
            "batches": batches,
            "adapter": adapter_result.payload,
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
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume an incomplete DISCOVERY RUN from durable runtime state.",
    )
    args = parser.parse_args()

    try:
        registry = ProductionAdapterRegistry()
        registry.register(
            ProductionAdapter(
                stage_id="DISCOVERY",
                implementation=run_discovery_adapter,
            )
        )
        out = start_run(
            args.source_package,
            args.db,
            args.run_id,
            registry,
            resume=args.resume,
        )
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(json.dumps({
            "status": "START_REJECTED",
            "reason": str(exc),
        }, ensure_ascii=False, indent=2))
        return 2

    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if out["status"] in {
        "PIPELINE_COMPLETED",
        "PIPELINE_READY",
        "PRODUCTION_ADAPTER_UNAVAILABLE",
    } else 1


if __name__ == "__main__":
    raise SystemExit(main())
