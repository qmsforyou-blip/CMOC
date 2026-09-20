#!/usr/bin/env python3
"""A4.2 negative control: a similar CMOC object must not become equivalence.

The control uses the production-derived SRC-002 M06 fixture. It injects a
synthetic CMOC object that is structurally similar to PAS-006 but has a
different object_name. An explicit structural query may return it as a
CANDIDATE, but RECONCILIATION must keep the result NEEDS_REVIEW rather than
EXISTING_EQUIVALENT. The source-bound Discovery/Passport fixture and the real
OBJECT INDEX remain unchanged.
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
    index_with_similar = copy.deepcopy(index)

    synthetic_similar = {
        "object_id": "TEST-T-FR-SIM-001",
        "object_type": "TERM",
        "object_name": "Fast Response management",
        "representation": {
            "kind": "OBJECT_FILE",
            "container": "A4.2-SYNTHETIC-CMOC",
            "location": "TEST",
        },
        "indexed_attributes": {},
        "structure": {
            "fields_present": ["object_id", "object_name", "representation"],
            "sections_present": ["definition", "traceability"],
        },
        "provenance": {
            "repository": "A4.2-TEST",
        },
        "traceability": {
            "source": "A4.2 synthetic similar object",
            "registry": "TEST",
        },
    }
    index_with_similar.append(synthetic_similar)

    records = copy.deepcopy(reconciliation_input["records"])
    pas006 = next(r for r in records if r["record_id"] == "PAS-006")

    # Explicit structural criteria are supplied by the reconciliation caller.
    # They establish similarity/candidacy only; they do not establish equivalence.
    pas006["structural_query"] = {
        "object_type": "TERM",
        "representation_kind": "OBJECT_FILE",
        "fields_present": ["object_id", "object_name", "representation"],
    }

    results = reconcile(
        index_with_similar,
        reconciliation_input["source_id"],
        reconciliation_input["input_batch_id"],
        reconciliation_input["input_output_type"],
        records,
        reconciliation_input["query_scope"],
    )

    pas006_result = next(r for r in results if r["input_record_id"] == "PAS-006")

    discovery_unchanged = passport_output == discovery_before
    original_index_unchanged = index == load_object_index()

    assert pas006_result["cmoc_object_id"] == "TEST-T-FR-SIM-001"
    assert pas006_result["match_result"] == "NEEDS_REVIEW"
    assert pas006_result["basis"] == "structural candidate; equivalence not established"
    assert discovery_unchanged
    assert original_index_unchanged

    print(json.dumps({
        "gate": "A4.2-SIMILAR-OBJECT-DOWNSTREAM-ISOLATION",
        "status": "PASS",
        "tested_passport": "PAS-006",
        "discovery_value": "Fast Response",
        "synthetic_cmoc_object_id": "TEST-T-FR-SIM-001",
        "reconciliation_result": pas006_result["match_result"],
        "reconciliation_basis": pas006_result["basis"],
        "discovery_unchanged": discovery_unchanged,
        "original_index_unchanged": original_index_unchanged,
        "real_index_file_modified": "NO",
        "control_rule": "Structural similarity/candidacy does not establish equivalence and does not alter DISCOVERY",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
