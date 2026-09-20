#!/usr/bin/env python3
"""Read-only adapter: M06 PASSPORT_RECORDS -> RECONCILIATION_INPUT.

This module performs address adaptation only. It does not call CMOC, OBJECT
INDEX, QUERY, or RECONCILIATION and does not infer target_object_type.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict, List


class ReconciliationInputError(ValueError):
    pass


def build_reconciliation_input(
    passport_output: Dict[str, Any],
    query_scope: List[str],
) -> Dict[str, Any]:
    """Adapt one M06 PASSPORT_RECORDS output without semantic enrichment."""
    if not isinstance(passport_output, dict):
        raise ReconciliationInputError("PASSPORT_OUTPUT_NOT_OBJECT")
    if passport_output.get("type") != "PASSPORT_RECORDS":
        raise ReconciliationInputError(
            f"INPUT_OUTPUT_TYPE_MISMATCH: {passport_output.get('type')} != PASSPORT_RECORDS"
        )

    source_id = passport_output.get("source_id")
    input_batch_id = passport_output.get("batch_id")
    records = passport_output.get("records")

    if not source_id:
        raise ReconciliationInputError("MISSING_SOURCE_ID")
    if not input_batch_id:
        raise ReconciliationInputError("MISSING_INPUT_BATCH_ID")
    if not isinstance(records, list):
        raise ReconciliationInputError("PASSPORT_RECORDS_NOT_LIST")
    if not isinstance(query_scope, list):
        raise ReconciliationInputError("QUERY_SCOPE_NOT_LIST")

    adapted_records = []
    for index, passport in enumerate(records, start=1):
        if not isinstance(passport, dict):
            raise ReconciliationInputError(f"PASSPORT_RECORD_NOT_OBJECT: {index}")

        for field in ("id", "term", "source_id", "source_basis"):
            if field not in passport:
                raise ReconciliationInputError(
                    f"MISSING_PASSPORT_FIELD: {field} at record {index}"
                )

        if passport["source_id"] != source_id:
            raise ReconciliationInputError(
                f"PASSPORT_SOURCE_ID_MISMATCH at record {index}"
            )

        traceability = {
            "source_id": source_id,
            "input_batch_id": input_batch_id,
            "passport_id": passport["id"],
            "candidate_id": passport.get("candidate_id"),
            "classification_id": passport.get("classification_id"),
            "source_basis": deepcopy(passport["source_basis"]),
        }

        # Preserve source-package/discovery lineage when supplied by the
        # upstream output. No new semantic information is inferred.
        upstream_traceability = passport_output.get("traceability")
        if isinstance(upstream_traceability, dict):
            for key in ("source_package", "discovery_run", "upstream_batch"):
                if key in upstream_traceability:
                    traceability[key] = deepcopy(upstream_traceability[key])

        # Preserve source-bound boundary only when it is explicitly present
        # in the Passport. It is address information, not query semantics.
        if "object_boundary" in passport:
            traceability["object_boundary"] = deepcopy(passport["object_boundary"])

        adapted_records.append(
            {
                "record_id": passport["id"],
                "value": passport["term"],
                "traceability": traceability,
            }
        )

    return {
        "source_id": source_id,
        "input_batch_id": input_batch_id,
        "input_output_type": "PASSPORT_RECORDS",
        "records": adapted_records,
        "query_scope": deepcopy(query_scope),
    }
