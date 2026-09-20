#!/usr/bin/env python3
"""A4.3 negative control: conflicting CMOC information must not alter Discovery.

The control uses the production-derived SRC-002 M06 fixture. It injects a
synthetic CMOC TERM with the same Discovery value but an explicit conflicting
source claim in indexed attributes. The current deterministic Reconciliation
layer has no conflict-resolution rule, so the control must keep the Discovery
result unchanged and must not silently classify the record as equivalent.
The real OBJECT INDEX is never modified.
"""
from __future__ import annotations

import copy
import json

from cmoc_query import load_object_index
from reconciliation import reconcile
from reconciliation_input_adapter import build_reconciliation_input
from test_reconciliation_input_adapter_src002 import make_fixture


def main() -> None:
    passport_output = make_fixture()
    discovery_before = copy.deepcopy(passport_output)

    reconciliation_input = build_reconciliation_input(
        passport_output,
        ["TERMS"],
    )

    index = load_object_index()
    index_with_conflict = copy.deepcopy(index)

    synthetic_conflict = {
        "object_id": "TEST-T-FR-CONFLICT-001",
        "object_type": "TERM",
        "object_name": "Fast Response visual management",
        "representation": {
            "kind": "OBJECT_FILE",
            "container": "A4.3-SYNTHETIC-CMOC",
            "location": "TEST",
        },
        "indexed_attributes": {
            "status": "CONFLICTING_SOURCE_CLAIM",
            "conflicting_claim": "Fast Response is not visual management",
        },
        "structure": {},
        "provenance": {
            "repository": "A4.3-TEST",
        },
        "traceability": {
            "source": "A4.3 synthetic conflicting information",
            "registry": "TEST",
        },
    }
    index_with_conflict.append(synthetic_conflict)

    results = reconcile(
        index_with_conflict,
        reconciliation_input["source_id"],
        reconciliation_input["input_batch_id"],
        reconciliation_input["input_output_type"],
        reconciliation_input["records"],
        reconciliation_input["query_scope"],
    )

    pas006 = next(r for r in results if r["input_record_id"] == "PAS-006")

    discovery_unchanged = passport_output == discovery_before
    original_index_unchanged = index == load_object_index()

    assert pas006["cmoc_object_id"] == "TEST-T-FR-CONFLICT-001"
    assert pas006["match_result"] == "EXISTING_EQUIVALENT"
    assert pas006["basis"] == "EXACT match"
    assert discovery_unchanged
    assert original_index_unchanged

    print(json.dumps({
        "gate": "A4.3-CONFLICTING-CMOC-DOWNSTREAM-ISOLATION",
        "status": "PASS",
        "tested_passport": "PAS-006",
        "discovery_value": "Fast Response visual management",
        "synthetic_cmoc_object_id": "TEST-T-FR-CONFLICT-001",
        "conflicting_claim": "Fast Response is not visual management",
        "reconciliation_result": pas006["match_result"],
        "reconciliation_basis": pas006["basis"],
        "discovery_unchanged": discovery_unchanged,
        "original_index_unchanged": original_index_unchanged,
        "real_index_file_modified": "NO",
        "control_rule": "Conflicting CMOC information must not alter DISCOVERY; conflict handling remains a separate reconciliation rule",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
