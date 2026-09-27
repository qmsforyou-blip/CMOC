"""Read-only M07 probe using persisted Discovery passports and controlled evidence.

The LLM request may incur a charge. This command does not change the RUN,
human decisions, CMOC, or OBJECT INDEX.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

from machine_source_001 import bind_relation_evidence
from m07_llm import build_relation_candidates


def inspect(db_path: Path, run_id: str, original: dict, controlled: dict) -> dict:
    if original["source_id"] != controlled["source_id"] or original["fragments"] != controlled["fragments"]:
        raise ValueError("SOURCE_MISMATCH: controlled evidence must use identical source fragments")
    with sqlite3.connect(f"file:{db_path.resolve()}?mode=ro", uri=True) as db:
        db.execute("PRAGMA query_only=ON")
        row = db.execute(
            "SELECT payload_json FROM adapter_results WHERE run_id=? AND stage_id='DISCOVERY' ORDER BY rowid DESC LIMIT 1",
            (run_id,),
        ).fetchone()
    if row is None:
        raise ValueError("COMPLETED_DISCOVERY_RESULT_NOT_FOUND")
    discovery = json.loads(row[0])["discovery"]
    if discovery["source_package_id"] != original["package_id"]:
        raise ValueError("SOURCE_PACKAGE_MISMATCH")
    m06 = next((x for x in discovery["results"] if x.get("type") == "PASSPORT_RECORDS"), None)
    if m06 is None or m06["source_id"] != original["source_id"]:
        raise ValueError("M06_PASSPORT_RECORDS_NOT_FOUND")
    evidence = bind_relation_evidence(controlled, m06["records"])
    records = build_relation_candidates(m06["records"], evidence)
    return {
        "status": "READ_ONLY_RELATION_PROBE",
        "run_id": run_id,
        "source_package_id": original["package_id"],
        "evidence_package_id": controlled["package_id"],
        "relation_evidence": evidence,
        "records": records,
        "boundary": "M07 diagnostic only; no RUN, decisions, CMOC, or OBJECT INDEX write",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True, type=Path)
    parser.add_argument("--run-id", required=True)
    here = Path(__file__).resolve().parent
    parser.add_argument("--original", type=Path, default=here / "SOURCE-PACKAGE-SRC-005-IMAI-CH13-P6.example.json")
    parser.add_argument("--evidence", type=Path, default=here / "SOURCE-PACKAGE-SRC-005-IMAI-CH13-P6-REL.example.json")
    args = parser.parse_args()
    original = json.loads(args.original.read_text(encoding="utf-8"))
    controlled = json.loads(args.evidence.read_text(encoding="utf-8"))
    print(json.dumps(inspect(args.db, args.run_id, original, controlled), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
