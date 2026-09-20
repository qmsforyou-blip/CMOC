#!/usr/bin/env python3
"""R1 control: QUERY result branches -> current RECONCILIATION semantics."""
from __future__ import annotations

import copy
import sys
from pathlib import Path

BASE = Path(__file__).parent
sys.path.insert(0, str(BASE))

from reconciliation import reconcile


def rec(object_id, object_name, kind="OBJECT_FILE", indexed=None, structure=None):
    return {
        "object_id": object_id,
        "object_name": object_name,
        "object_type": "TERM",
        "representation": {"kind": kind},
        "indexed_attributes": indexed or {},
        "structure": structure or {},
        "traceability": {"fixture": "R1"},
    }


def inp(record_id, value, structural_query=None):
    d = {
        "record_id": record_id,
        "value": value,
        "traceability": {"source_id": "R1-SRC", "record_id": record_id},
    }
    if structural_query is not None:
        d["structural_query"] = structural_query
    return d


def run():
    # Four isolated branches:
    # 1) EXACT MATCH — canonical OBJECT_FILE.
    # 2) NO_MATCH — absent object_name.
    # 3) CANDIDATE — explicit structural query finds one indexed record.
    # 4) AMBIGUOUS — same object_name exists in two non-canonical representations.
    index = [
        rec("T-R1-MATCH", "R1 Exact Object"),
        rec("T-R1-CAND", "R1 Structural Candidate",
            kind="REGISTRY_RECORD",
            structure={"fields_present": ["candidate_marker"]}),
        rec("T-R1-AMB-A", "R1 Ambiguous Object", kind="REGISTRY_RECORD"),
        rec("T-R1-AMB-B", "R1 Ambiguous Object", kind="REGISTRY_RECORD"),
    ]

    original_index = copy.deepcopy(index)

    records = [
        inp("R1-MATCH-001", "R1 Exact Object"),
        inp("R1-NOMATCH-001", "R1 Object Absent"),
        inp("R1-CANDIDATE-001", "R1 No Exact Name",
             {"fields_present": ["candidate_marker"]}),
        inp("R1-AMBIGUOUS-001", "R1 Ambiguous Object"),
    ]

    results = reconcile(
        index,
        "R1-SRC",
        "R1-BATCH-001",
        "PASSPORT_RECORDS",
        records,
        ["TERMS"],
    )

    expected = [
        ("R1-MATCH-001", "EXISTING_EQUIVALENT", "EXACT match", "T-R1-MATCH"),
        ("R1-NOMATCH-001", "NEEDS_REVIEW",
         "NO_MATCH from configured query modes; NEW not yet proven", None),
        ("R1-CANDIDATE-001", "NEEDS_REVIEW",
         "structural candidate; equivalence not established", "T-R1-CAND"),
        ("R1-AMBIGUOUS-001", "NEEDS_REVIEW", "exact object_name", None),
    ]

    checks = []
    for got, exp in zip(results, expected):
        checks.append({
            "record_id": got["input_record_id"],
            "pass": (
                got["match_result"] == exp[1]
                and got["basis"] == exp[2]
                and got["cmoc_object_id"] == exp[3]
            ),
            "actual": {
                "match_result": got["match_result"],
                "basis": got["basis"],
                "cmoc_object_id": got["cmoc_object_id"],
            },
        })

    index_unchanged = index == original_index
    no_match_is_new = results[1]["match_result"] == "NEW"
    candidate_equivalent = results[2]["match_result"] == "EXISTING_EQUIVALENT"
    ambiguous_equivalent = results[3]["match_result"] == "EXISTING_EQUIVALENT"

    status = (
        "PASS"
        if all(x["pass"] for x in checks)
        and index_unchanged
        and not no_match_is_new
        and not candidate_equivalent
        and not ambiguous_equivalent
        else "FAIL"
    )

    print(__import__("json").dumps({
        "gate": "R1-QUERY-RECONCILIATION-SEMANTICS",
        "status": status,
        "branches": checks,
        "controls": {
            "object_index_memory_mutation": index_unchanged,
            "cmoc_write": "NONE",
            "no_match_is_new": no_match_is_new,
            "candidate_is_equivalent": candidate_equivalent,
            "ambiguous_is_equivalent": ambiguous_equivalent,
        },
        "expected_rule": {
            "MATCH": "EXISTING_EQUIVALENT",
            "NO_MATCH": "NEEDS_REVIEW",
            "CANDIDATE": "NEEDS_REVIEW",
            "AMBIGUOUS": "NEEDS_REVIEW",
        },
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    run()
