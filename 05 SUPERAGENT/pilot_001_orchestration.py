"""PILOT-001 orchestration: DISCOVERY -> RECONCILIATION -> human-review pause.

Execution control only. No NEW decision, Admission, canonization, CMOC write,
or OBJECT INDEX mutation is performed here.
"""

from __future__ import annotations

from typing import Any

from runtime_state_store import JournalEvent, RuntimeStateStore


def continue_to_reconciliation(
    *,
    store: RuntimeStateStore,
    registry: Any,
    adapter_persistence: Any,
    run_id: str,
    source_package: dict[str, Any],
    discovery_payload: dict[str, Any],
) -> dict[str, Any]:
    source_id = source_package["source_id"]
    package_id = source_package["package_id"]
    attempt_id = f"ATTEMPT-RECONCILIATION-{run_id}"
    result_id = f"RESULT-RECONCILIATION-{run_id}"
    trace = (
        f"RUN_ID={run_id};SOURCE_ID={source_id};"
        f"SOURCE_PACKAGE_ID={package_id};STAGE_ID=RECONCILIATION"
    )

    def append(event_type: str, status: str) -> None:
        seq = store.next_event_seq(run_id)
        store.append(
            JournalEvent(
                run_id=run_id,
                event_id=f"EVENT-{run_id}-{seq:03d}",
                event_seq=seq,
                stage_id="RECONCILIATION",
                event_type=event_type,
                stage_result_id=result_id,
                attempt_id=attempt_id,
                event_status=status,
                traceability=trace,
                source_id=source_id,
                batch_id=package_id,
            ),
            source_id=source_id,
            batch_id=package_id,
        )

    append("STAGE_STARTED", "ACTIVE")
    envelope = {
        "run_id": run_id,
        "source_id": source_id,
        "batch_id": package_id,
        "stage_id": "RECONCILIATION",
        "attempt_id": attempt_id,
        "result_id": result_id,
        "discovery": discovery_payload,
        "query_scope": ["TERMS"],
    }
    adapter_result = registry.invoke(envelope, adapter_persistence)
    if adapter_result.status != "PRODUCTION_ADAPTER_ACCEPTED":
        append("STAGE_FAILED", adapter_result.status)
        return {
            "status": adapter_result.status,
            "run_id": run_id,
            "reconciliation": adapter_result.payload,
        }

    append("STAGE_COMPLETED", "COMPLETED")
    reconciliation = adapter_result.payload["result"]["reconciliation_result"]

    if reconciliation["summary"]["needs_review"] > 0:
        append("HUMAN_REVIEW_REQUIRED", "NEEDS_REVIEW")
        return {
            "status": "HUMAN_REVIEW_REQUIRED",
            "run_id": run_id,
            "source_id": source_id,
            "source_package_id": package_id,
            "reconciliation_result": reconciliation,
        }

    return {
        "status": "RECONCILIATION_COMPLETED",
        "run_id": run_id,
        "source_id": source_id,
        "source_package_id": package_id,
        "reconciliation_result": reconciliation,
    }
