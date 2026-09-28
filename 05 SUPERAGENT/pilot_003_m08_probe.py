"""Read-only M08 diagnostic on reviewed M07 transcript and persisted M06 passports.

--validate-only makes no LLM call. Normal mode calls M08 but writes no RUN result.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

from m08_llm import decide
from pilot_003_relation_probe import inspect


def probe(db_path: Path, run_id: str, original: dict, controlled: dict,
          binding: dict, transcript: dict, validate_only: bool = False) -> dict:
    validated = inspect(db_path, run_id, original, controlled, binding, validate_only=True)
    if any(transcript.get(key) != validated.get(key) for key in
           ("run_id", "source_package_id", "evidence_package_id")):
        raise ValueError("M07_TRANSCRIPT_LINEAGE_MISMATCH")
    if transcript.get("source_id") != original["source_id"]:
        raise ValueError("M07_TRANSCRIPT_SOURCE_MISMATCH")
    if (transcript.get("excluded_relation", {}).get("id") != "REL-001" or
        not transcript["excluded_relation"].get("reason")):
        raise ValueError("REL_001_REVIEW_REQUIRED")
    records = transcript.get("records")
    if not isinstance(records, list) or [r.get("id") for r in records] != ["REL-002", "REL-003"]:
        raise ValueError("M07_REVIEWED_RELATION_SET_MISMATCH")
    evidence_by_id = {e["evidence_id"]: e for e in validated["relation_evidence"]}
    for record in records:
        refs = record.get("basis_refs")
        if (record.get("source_id") != original["source_id"] or
            record.get("status") != "RELATION_CANDIDATE" or
            record.get("epistemic_status") != "PROVISIONAL" or
            record.get("relation_type") != "ACTIVITY_OCCURS_WITHIN_ACTIVITY" or
            record.get("evidence_gap") is not None or
            not isinstance(refs, list) or len(refs) != 1 or refs[0] not in evidence_by_id):
            raise ValueError("M07_REVIEWED_RELATION_INVALID")
        endpoints = {record.get("from_passport_id"), record.get("to_passport_id")}
        if endpoints != set(evidence_by_id[refs[0]]["supports"]):
            raise ValueError("M07_REVIEWED_ENDPOINT_MISMATCH")
    with sqlite3.connect(f"file:{db_path.resolve()}?mode=ro", uri=True) as db:
        db.execute("PRAGMA query_only=ON")
        row = db.execute(
            "SELECT payload_json FROM adapter_results WHERE run_id=? AND stage_id='DISCOVERY' ORDER BY rowid DESC LIMIT 1",
            (run_id,),
        ).fetchone()
    discovery = json.loads(row[0])["discovery"]
    passports = next(x["records"] for x in discovery["results"] if x.get("type") == "PASSPORT_RECORDS")
    decisions = [] if validate_only else decide(passports, records, validated["relation_evidence"])["records"]
    return {
        "status": "M08_INPUT_VALIDATED" if validate_only else "READ_ONLY_M08_PROBE",
        "run_id": run_id,
        "reviewed_relations": [r["id"] for r in records],
        "excluded_relation": transcript["excluded_relation"],
        "records": decisions,
        "boundary": "No LLM call; no writes" if validate_only else
                    "M08 diagnostic only; no RUN, human decision, Admission, CMOC, or index write",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True, type=Path)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--validate-only", action="store_true")
    here = Path(__file__).resolve().parent
    parser.add_argument("--original", type=Path, default=here / "SOURCE-PACKAGE-SRC-005-IMAI-CH13-P6.example.json")
    parser.add_argument("--evidence", type=Path, default=here / "SOURCE-PACKAGE-SRC-005-IMAI-CH13-P6-REL.example.json")
    parser.add_argument("--binding", type=Path, default=here / "PILOT-003-SRC-005-RELATION-BINDING.json")
    parser.add_argument("--transcript", type=Path, default=here / "PILOT-003-M07-REVIEWED-TRANSCRIPT.json")
    args = parser.parse_args()
    inputs = [json.loads(p.read_text(encoding="utf-8")) for p in
              (args.original, args.evidence, args.binding, args.transcript)]
    print(json.dumps(probe(args.db, args.run_id, *inputs, validate_only=args.validate_only),
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
