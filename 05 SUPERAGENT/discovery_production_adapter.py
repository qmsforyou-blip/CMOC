"""Production DISCOVERY adapter for the local runtime.

The adapter is intentionally thin: it maps the runtime envelope to the
existing MACHINE-SOURCE-001 production implementation and returns its
source-bound DISCOVERY_RESULT. It does not perform reconciliation or CMOC
lookup.
"""

from __future__ import annotations

from typing import Any

from machine_source_001 import run_discovery


def run_discovery_adapter(envelope: dict[str, Any]) -> dict[str, Any]:
    required = (
        "run_id",
        "source_id",
        "batch_id",
        "stage_id",
        "attempt_id",
        "result_id",
        "source_package",
    )
    missing = [field for field in required if not envelope.get(field)]
    if missing:
        raise ValueError(
            f"DISCOVERY_ADAPTER_INPUT_INVALID: missing {missing}"
        )

    if envelope["stage_id"] != "DISCOVERY":
        raise ValueError("DISCOVERY_ADAPTER_STAGE_MISMATCH")

    source_package = envelope["source_package"]
    if source_package.get("source_id") != envelope["source_id"]:
        raise ValueError("DISCOVERY_ADAPTER_SOURCE_ID_MISMATCH")

    discovery_run_id = envelope.get(
        "discovery_run_id",
        f"{envelope['run_id']}-DISCOVERY",
    )

    result = run_discovery(
        run_id=discovery_run_id,
        source_package=source_package,
    )

    if result.get("status") != "ACCEPT":
        return {
            "run_id": envelope["run_id"],
            "source_id": envelope["source_id"],
            "batch_id": envelope["batch_id"],
            "stage_id": envelope["stage_id"],
            "attempt_id": envelope["attempt_id"],
            "result_id": envelope["result_id"],
            "status": result.get("status"),
            "source_package_id": source_package["package_id"],
            "discovery_run_id": discovery_run_id,
            "discovery": result,
        }

    return {
        "run_id": envelope["run_id"],
        "source_id": envelope["source_id"],
        "batch_id": envelope["batch_id"],
        "stage_id": envelope["stage_id"],
        "attempt_id": envelope["attempt_id"],
        "result_id": envelope["result_id"],
        "status": "ACCEPT",
        "source_package_id": source_package["package_id"],
        "discovery_run_id": discovery_run_id,
        "discovery": result,
    }
