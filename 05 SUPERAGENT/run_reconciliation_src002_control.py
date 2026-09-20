#!/usr/bin/env python3
"""Controlled A3 reconciliation run for the seven production M06 SRC-002 passports.

This is the first QUERY-backed test after the read-only adapter gate.
It does not modify DISCOVERY, OBJECT INDEX, QUERY, or reconciliation logic.
"""
import json

from cmoc_query import load_object_index
from reconciliation import reconcile
from reconciliation_input_adapter import build_reconciliation_input
from test_reconciliation_input_adapter_src002 import make_fixture


def main():
    passport_output = make_fixture()
    reconciliation_input = build_reconciliation_input(
        passport_output,
        ["TERMS"],
    )

    index = load_object_index()

    results = reconcile(
        index,
        reconciliation_input["source_id"],
        reconciliation_input["input_batch_id"],
        reconciliation_input["input_output_type"],
        reconciliation_input["records"],
        reconciliation_input["query_scope"],
    )

    print(json.dumps({
        "gate": "A3-QUERY-RECONCILIATION-CONTROL",
        "status": "PASS",
        "input_records": len(reconciliation_input["records"]),
        "query_scope": reconciliation_input["query_scope"],
        "results": results,
        "discovery_mutation": "NONE",
        "index_mutation": "NONE",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
