#!/usr/bin/env python3
"""Build the explicit RECONCILIATION_RESULT v0.1 artifact.

This module packages already-produced record-level reconciliation results.
It does not query CMOC, mutate Discovery, or make admission decisions.
"""
from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from typing import Any, Dict, List


class ReconciliationResultError(ValueError):
    pass


ALLOWED_RESULTS = {"EXISTING_EQUIVALENT", "NEEDS_REVIEW"}


def _stable_id(source_id: str, discovery_run: str, input_batch_id: str) -> str:
    raw = f"{source_id}|{discovery_run}|{input_batch_id}".encode("utf-8")
    return "RECON-" + hashlib.sha256(raw).hexdigest()[:16]


def build_reconciliation_result(
    source_id: str,
    discovery_run: str,
    input_batch_id: str,
    input_output_type: str,
    query_scope: List[str],
    records: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Package record-level reconciliation output into a v0.1 artifact."""
    if not source_id:
        raise ReconciliationResultError("MISSING_SOURCE_ID")
    if not discovery_run:
        raise ReconciliationResultError("MISSING_DISCOVERY_RUN")
    if not input_batch_id:
        raise ReconciliationResultError("MISSING_INPUT_BATCH_ID")
    if input_output_type != "PASSPORT_RECORDS":
        raise ReconciliationResultError("INPUT_OUTPUT_TYPE_MISMATCH")
    if not isinstance(query_scope, list):
        raise ReconciliationResultError("QUERY_SCOPE_NOT_LIST")
    if not isinstance(records, list):
        raise ReconciliationResultError("RECORDS_NOT_LIST")

    out = []
    for i, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            raise ReconciliationResultError(f"RESULT_RECORD_NOT_OBJECT: {i}")

        for field in (
            "match_id",
            "source_id",
            "input_batch_id",
            "input_record_id",
            "cmoc_object_id",
            "match_result",
            "basis",
            "status",
            "traceability",
        ):
            if field not in record:
                raise ReconciliationResultError(
                    f"MISSING_RESULT_FIELD: {field} at record {i}"
                )

        if record["source_id"] != source_id:
            raise ReconciliationResultError(f"SOURCE_ID_MISMATCH: {i}")
        if record["input_batch_id"] != input_batch_id:
            raise ReconciliationResultError(f"INPUT_BATCH_ID_MISMATCH: {i}")
        if record["match_result"] not in ALLOWED_RESULTS:
            raise ReconciliationResultError(
                f"UNSUPPORTED_MATCH_RESULT: {record['match_result']}"
            )
        if record["status"] != "PROVISIONAL":
            raise ReconciliationResultError(f"STATUS_NOT_PROVISIONAL: {i}")

        if (
            record["match_result"] == "EXISTING_EQUIVALENT"
            and not record["cmoc_object_id"]
        ):
            raise ReconciliationResultError(
                f"EQUIVALENT_WITHOUT_CMOC_OBJECT: {i}"
            )

        if record["match_result"] == "NEEDS_REVIEW" and record["cmoc_object_id"] == "":
            raise ReconciliationResultError(f"INVALID_EMPTY_CMOC_OBJECT: {i}")

        out.append(deepcopy(record))

    existing = sum(
        r["match_result"] == "EXISTING_EQUIVALENT" for r in out
    )
    review = sum(r["match_result"] == "NEEDS_REVIEW" for r in out)

    return {
        "type": "RECONCILIATION_RESULT",
        "reconciliation_id": _stable_id(
            source_id, discovery_run, input_batch_id
        ),
        "source_id": source_id,
        "discovery_run": discovery_run,
        "input_batch_id": input_batch_id,
        "input_output_type": input_output_type,
        "query_scope": deepcopy(query_scope),
        "records": out,
        "summary": {
            "total": len(out),
            "existing_equivalent": existing,
            "needs_review": review,
        },
        "boundary": {
            "origin": "RECONCILIATION",
            "discovery_mutation": "NONE",
            "cmoc_write": "NONE",
            "object_index_write": "NONE",
            "admission_decision": "NOT_PERFORMED",
        },
    }


def main() -> None:
    payload = json.load(__import__("sys").stdin)
    result = build_reconciliation_result(
        payload["source_id"],
        payload["discovery_run"],
        payload["input_batch_id"],
        payload["input_output_type"],
        payload["query_scope"],
        payload["records"],
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
