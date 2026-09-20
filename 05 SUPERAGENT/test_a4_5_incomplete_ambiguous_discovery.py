#!/usr/bin/env python3
"""A4.5 negative control: incomplete/ambiguous Discovery input is not rewritten.

This is a controlled Reconciliation test. It verifies two cases:
1) an incomplete-but-contract-valid reconciliation record is left unchanged;
2) an ambiguous CMOC match produces NEEDS_REVIEW and does not rewrite the
   source-bound input record.

The real OBJECT INDEX is never modified. No Discovery machine is rerun.
"""
from __future__ import annotations

import copy
import json

from cmoc_query import load_object_index
from reconciliation import reconcile


SOURCE_ID = "SRC-A4.5"
BATCH_ID = "BATCH-A4.5-001"


def main() -> None:
    index = load_object_index()
    original_index = copy.deepcopy(index)

    # Case 1: minimal/incomplete semantic input. Reconciliation is allowed to
    # receive only the minimal record contract; it must not enrich or rewrite it.
    incomplete_records = [
        {
            "record_id": "A4.5-INCOMPLETE-001",
            "value": "A4.5 incomplete discovery value",
            "traceability": {
                "source_id": SOURCE_ID,
                "passport_id": "A4.5-INCOMPLETE-001",
            },
        }
    ]
    incomplete_before = copy.deepcopy(incomplete_records)

    incomplete_results = reconcile(
        index,
        SOURCE_ID,
        BATCH_ID,
        "PASSPORT_RECORDS",
        incomplete_records,
        ["TERMS"],
    )

    assert incomplete_records == incomplete_before
    assert incomplete_results[0]["match_result"] == "NEEDS_REVIEW"
    assert incomplete_results[0]["cmoc_object_id"] is None
    assert incomplete_results[0]["basis"] == (
        "NO_MATCH from configured query modes; NEW not yet proven"
    )

    # Case 2: two non-canonical physical representations with the same exact
    # object_name. QUERY must report AMBIGUOUS; Reconciliation must not choose
    # one and must not mutate the source-bound input.
    ambiguous_index = copy.deepcopy(index)
    for suffix in ("001", "002"):
        ambiguous_index.append(
            {
                "object_id": f"TEST-T-A45-AMB-{suffix}",
                "object_type": "TERM",
                "object_name": "A4.5 ambiguous term",
                "representation": {
                    "kind": "REGISTRY_RECORD",
                    "container": "A4.5-SYNTHETIC-CMOC",
                    "location": f"TEST-{suffix}",
                },
                "indexed_attributes": {},
                "structure": {},
                "provenance": {
                    "repository": "A4.5-TEST",
                },
                "traceability": {
                    "source": "A4.5 synthetic ambiguity",
                },
            }
        )

    ambiguous_records = [
        {
            "record_id": "A4.5-AMBIGUOUS-001",
            "value": "A4.5 ambiguous term",
            "traceability": {
                "source_id": SOURCE_ID,
                "passport_id": "A4.5-AMBIGUOUS-001",
            },
        }
    ]
    ambiguous_before = copy.deepcopy(ambiguous_records)

    ambiguous_results = reconcile(
        ambiguous_index,
        SOURCE_ID,
        BATCH_ID,
        "PASSPORT_RECORDS",
        ambiguous_records,
        ["TERMS"],
    )

    ambiguous_result = ambiguous_results[0]

    assert ambiguous_records == ambiguous_before
    assert ambiguous_result["match_result"] == "NEEDS_REVIEW"
    assert ambiguous_result["cmoc_object_id"] is None
    assert ambiguous_result["basis"] == "exact object_name"

    assert index == original_index
    assert load_object_index() == original_index

    print(json.dumps({
        "gate": "A4.5-INCOMPLETE-AMBIGUOUS-DISCOVERY-ISOLATION",
        "status": "PASS",
        "incomplete": {
            "record_id": "A4.5-INCOMPLETE-001",
            "reconciliation_result": incomplete_results[0]["match_result"],
            "cmoc_object_id": incomplete_results[0]["cmoc_object_id"],
            "input_unchanged": incomplete_records == incomplete_before,
        },
        "ambiguous": {
            "record_id": "A4.5-AMBIGUOUS-001",
            "reconciliation_result": ambiguous_result["match_result"],
            "reconciliation_basis": ambiguous_result["basis"],
            "cmoc_object_id": ambiguous_result["cmoc_object_id"],
            "input_unchanged": ambiguous_records == ambiguous_before,
        },
        "original_index_unchanged": index == original_index,
        "real_index_file_modified": "NO",
        "control_rule": (
            "Incomplete or ambiguous Discovery input may produce NEEDS_REVIEW, "
            "but RECONCILIATION must not rewrite DISCOVERY or select an "
            "unresolved CMOC object"
        ),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
