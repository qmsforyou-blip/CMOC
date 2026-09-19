#!/usr/bin/env python3
"""TASK-CONTRACT-002 RECONCILIATION — deterministic MVP.

This layer consumes explicit DISCOVERY records and a read-only CMOC QUERY
result. It never mutates the source-bound record or the CMOC index.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

from cmoc_query import load_object_index, query


def reconcile(index, source_id, input_batch_id, input_output_type,
              records, query_scope):
    out = []
    for record in records:
        rid = record["record_id"]
        value = record["value"]

        q_exact = query(
            index, f"Q-{rid}-EXACT", "EXACT",
            record.get("target_object_type"), value, query_scope
        )

        if q_exact["match_status"] == "MATCH":
            hit = q_exact["results"][0]
            result = "EXISTING_EQUIVALENT"
            basis = "EXACT match"
            cmoc_id = hit["object_id"]
        elif q_exact["match_status"] in {"AMBIGUOUS", "SCOPE_INSUFFICIENT"}:
            result = "NEEDS_REVIEW"
            basis = q_exact["match_basis"]
            cmoc_id = None
        else:
            q_alias = query(
                index, f"Q-{rid}-ALIAS", "ALIAS",
                record.get("target_object_type"), value, query_scope
            )

            if q_alias["match_status"] == "MATCH":
                hit = q_alias["results"][0]
                result = "EXISTING_EQUIVALENT"
                basis = "registered ALIAS match"
                cmoc_id = hit["object_id"]
            elif q_alias["match_status"] in {"AMBIGUOUS", "SCOPE_INSUFFICIENT"}:
                result = "NEEDS_REVIEW"
                basis = q_alias["match_basis"]
                cmoc_id = None
            else:
                # STRUCTURAL requires explicit structural criteria. RECONCILIATION
                # must not turn an arbitrary source string into a structural
                # interpretation. If no structural query is supplied, the
                # result remains NEEDS_REVIEW.
                structural_query = record.get("structural_query")
                if structural_query is None:
                    q_struct = None
                else:
                    q_struct = query(
                        index, f"Q-{rid}-STRUCT", "STRUCTURAL",
                        record.get("target_object_type"), structural_query, query_scope
                    )

                if q_struct and q_struct["match_status"] == "CANDIDATE":
                    result = "NEEDS_REVIEW"
                    basis = "structural candidate; equivalence not established"
                    cmoc_id = q_struct["results"][0]["object_id"]
                elif q_struct and q_struct["match_status"] in {"AMBIGUOUS", "SCOPE_INSUFFICIENT"}:
                    result = "NEEDS_REVIEW"
                    basis = q_struct["match_basis"]
                    cmoc_id = None
                else:
                    result = "NEEDS_REVIEW"
                    basis = "NO_MATCH from configured query modes; NEW not yet proven"
                    cmoc_id = None

        out.append({
            "match_id": f"MAT-{rid}",
            "source_id": source_id,
            "input_batch_id": input_batch_id,
            "input_record_id": rid,
            "cmoc_object_id": cmoc_id,
            "match_result": result,
            "basis": basis,
            "status": "PROVISIONAL",
            "traceability": record["traceability"],
        })
    return out


def main():
    payload = json.load(sys.stdin)
    index = load_object_index(payload.get(
        "index_path",
        str(Path(__file__).with_name("cmoc_object_index.json"))
    ))
    result = reconcile(
        index,
        payload["source_id"],
        payload["input_batch_id"],
        payload["input_output_type"],
        payload["records"],
        payload.get("query_scope", ["TERMS"]),
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
