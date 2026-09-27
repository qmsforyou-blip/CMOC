"""Read-only PILOT-001 diagnostic across every existing OBJECT INDEX scope.

This does not replace RECONCILIATION_RESULT or decide equivalence/newness.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

from cmoc_query import TYPE_SCOPE, load_object_index, query


def probe(passport_output: dict, index: list[dict]) -> dict:
    if passport_output.get("type") != "PASSPORT_RECORDS":
        raise ValueError("PASSPORT_RECORDS_REQUIRED")
    scopes = sorted(set(TYPE_SCOPE.values()))
    rows = []
    for passport in passport_output["records"]:
        record_id = passport["id"]
        value = passport["term"]
        exact = query(index, f"PROBE-{record_id}-EXACT", "EXACT", None, value, scopes)
        alias = query(index, f"PROBE-{record_id}-ALIAS", "ALIAS", None, value, scopes)
        rows.append({
            "passport_id": record_id,
            "source_value": value,
            "exact_status": exact["match_status"],
            "exact_hits": [
                {"object_id": hit["object_id"], "object_type": hit["object_type"]}
                for hit in exact["results"]
            ],
            "alias_status": alias["match_status"],
            "alias_hits": [
                {"object_id": hit["object_id"], "object_type": hit["object_type"]}
                for hit in alias["results"]
            ],
        })
    return {
        "status": "READ_ONLY_QUERY_PROBE",
        "source_id": passport_output["source_id"],
        "input_batch_id": passport_output["batch_id"],
        "query_scope": scopes,
        "records": rows,
        "boundary": "No RUN, RECONCILIATION_RESULT, CMOC, or OBJECT INDEX write; no equivalence decision",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--index", default=str(Path(__file__).with_name("cmoc_object_index.json")))
    args = parser.parse_args()
    db_path = Path(args.db)
    if not db_path.is_file():
        raise FileNotFoundError(db_path)
    with sqlite3.connect(str(db_path)) as db:
        db.execute("PRAGMA query_only=ON")
        row = db.execute(
            "SELECT payload_json FROM adapter_results WHERE run_id=? AND stage_id='DISCOVERY' ORDER BY rowid DESC LIMIT 1",
            (args.run_id,),
        ).fetchone()
    if row is None:
        raise ValueError("COMPLETED_DISCOVERY_RESULT_NOT_FOUND")
    discovery = json.loads(row[0])["discovery"]
    m06 = next(
        (item for item in discovery["results"] if item.get("type") == "PASSPORT_RECORDS"),
        None,
    )
    if m06 is None:
        raise ValueError("M06_PASSPORT_RECORDS_NOT_FOUND")
    print(json.dumps(probe(m06, load_object_index(args.index)), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
