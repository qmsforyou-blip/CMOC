#!/usr/bin/env python3
"""A5.3 downstream reconciliation for the frozen SRC-003 Discovery M06 result.

Rules:
- consumes frozen DISCOVERY_RESULT only;
- adapts M06 PASSPORT_RECORDS read-only;
- queries CMOC OBJECT INDEX downstream;
- never reruns or mutates Discovery;
- NO_MATCH is not NEW;
- target_object_type is not inferred from working_class.
"""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

from cmoc_query import load_object_index
from reconciliation import reconcile
from reconciliation_input_adapter import build_reconciliation_input
from reconciliation_result import build_reconciliation_result

BASE = Path(__file__).parent
FIXTURE = BASE / "DISCOVERY-RESULT-SRC-003-M06-001.json"
INDEX = BASE / "cmoc_object_index.json"
QUERY_SCOPE = ["TERMS"]


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    fixture_bytes_before = FIXTURE.read_bytes()
    index_bytes_before = INDEX.read_bytes()

    discovery = json.loads(fixture_bytes_before.decode("utf-8"))
    discovery_snapshot = copy.deepcopy(discovery)

    reconciliation_input = build_reconciliation_input(
        discovery,
        QUERY_SCOPE,
    )

    # Explicitly prove that the adapter did not infer CMOC object type.
    if any("target_object_type" in r for r in reconciliation_input["records"]):
        raise RuntimeError("A5.3 CONTROL FAILURE: target_object_type was inferred")

    index = load_object_index(INDEX)

    results = reconcile(
        index,
        reconciliation_input["source_id"],
        reconciliation_input["input_batch_id"],
        reconciliation_input["input_output_type"],
        reconciliation_input["records"],
        reconciliation_input["query_scope"],
    )

    reconciliation_result = build_reconciliation_result(
        source_id=reconciliation_input["source_id"],
        discovery_run=discovery["traceability"]["discovery_run"],
        input_batch_id=reconciliation_input["input_batch_id"],
        input_output_type=reconciliation_input["input_output_type"],
        query_scope=reconciliation_input["query_scope"],
        records=results,
    )

    fixture_bytes_after = FIXTURE.read_bytes()
    index_bytes_after = INDEX.read_bytes()

    if discovery != discovery_snapshot:
        raise RuntimeError("A5.3 CONTROL FAILURE: DISCOVERY RESULT mutated in memory")
    if fixture_bytes_after != fixture_bytes_before:
        raise RuntimeError("A5.3 CONTROL FAILURE: frozen DISCOVERY RESULT file changed")
    if index_bytes_after != index_bytes_before:
        raise RuntimeError("A5.3 CONTROL FAILURE: OBJECT INDEX file changed")

    summary = {}
    for r in results:
        summary[r["match_result"]] = summary.get(r["match_result"], 0) + 1

    print(json.dumps({
        "gate": "A5.3-SRC-003-DOWNSTREAM-RECONCILIATION",
        "status": "PASS",
        "source_id": discovery["source_id"],
        "discovery_run": discovery["traceability"]["discovery_run"],
        "discovery_batch": discovery["batch_id"],
        "input_records": len(reconciliation_input["records"]),
        "query_scope": QUERY_SCOPE,
        "target_object_type_inference": "NONE",
        "result_summary": summary,
        "reconciliation_result": reconciliation_result,
        "controls": {
            "discovery_result_memory_mutation": "NONE",
            "discovery_result_file_mutation": "NONE",
            "object_index_file_mutation": "NONE",
            "cmoc_write": "NONE",
            "query_downstream_only": True,
            "no_match_is_new": False,
            "working_class_to_target_type_mapping": "NOT_PERFORMED",
        },
        "hashes": {
            "discovery_result_sha256_before_after_equal":
                sha256_bytes(fixture_bytes_before) == sha256_bytes(fixture_bytes_after),
            "object_index_sha256_before_after_equal":
                sha256_bytes(index_bytes_before) == sha256_bytes(index_bytes_after),
        },
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
