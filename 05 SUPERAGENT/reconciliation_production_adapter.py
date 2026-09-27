"""Production RECONCILIATION adapter for PILOT-001.

Consumes the already-produced M06 PASSPORT_RECORDS from DISCOVERY and performs
read-only reconciliation against OBJECT INDEX. It does not decide NEW,
Admission, canonization, CMOC write, or index mutation.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from cmoc_query import load_object_index
from reconciliation import reconcile
from reconciliation_input_adapter import build_reconciliation_input
from reconciliation_result import build_reconciliation_result


def _m06_output(discovery: dict[str, Any]) -> dict[str, Any]:
    for item in discovery.get("results", []):
        if isinstance(item, dict) and item.get("type") == "PASSPORT_RECORDS":
            return item
    raise ValueError("RECONCILIATION_INPUT_M06_MISSING")


def run_reconciliation_adapter(envelope: dict[str, Any]) -> dict[str, Any]:
    required = (
        "run_id", "source_id", "batch_id", "stage_id",
        "attempt_id", "result_id", "discovery",
    )
    missing = [field for field in required if not envelope.get(field)]
    if missing:
        raise ValueError(f"RECONCILIATION_ADAPTER_INPUT_INVALID: missing {missing}")
    if envelope["stage_id"] != "RECONCILIATION":
        raise ValueError("RECONCILIATION_ADAPTER_STAGE_MISMATCH")

    discovery = envelope["discovery"]
    if discovery.get("source_id") != envelope["source_id"]:
        raise ValueError("RECONCILIATION_ADAPTER_SOURCE_ID_MISMATCH")

    m06 = _m06_output(discovery)
    query_scope = envelope.get("query_scope", ["TERMS"])
    adapted = build_reconciliation_input(m06, query_scope)

    index_path = envelope.get(
        "index_path",
        str(Path(__file__).with_name("cmoc_object_index.json")),
    )
    index = load_object_index(index_path)
    records = reconcile(
        index,
        adapted["source_id"],
        adapted["input_batch_id"],
        adapted["input_output_type"],
        adapted["records"],
        adapted["query_scope"],
    )
    result = build_reconciliation_result(
        source_id=adapted["source_id"],
        discovery_run=discovery.get("discovery_run_id")
            or discovery.get("run_id")
            or f"{envelope['run_id']}-DISCOVERY",
        input_batch_id=adapted["input_batch_id"],
        input_output_type=adapted["input_output_type"],
        query_scope=adapted["query_scope"],
        records=records,
    )

    return {
        "run_id": envelope["run_id"],
        "source_id": envelope["source_id"],
        "batch_id": envelope["batch_id"],
        "stage_id": envelope["stage_id"],
        "attempt_id": envelope["attempt_id"],
        "result_id": envelope["result_id"],
        "status": "ACCEPT",
        "reconciliation_result": result,
    }
