"""Read-only completeness check for human decisions of a waiting pilot RUN.

This report is not a journal event, Admission result, or RUN completion.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
from collections import Counter
from pathlib import Path


def inspect_review_set(db_path: Path, run_id: str, output_root: Path) -> dict:
    if not run_id or any(ch in run_id for ch in "/\\"):
        raise ValueError("INVALID_RUN_ID")
    if not db_path.is_file():
        raise ValueError("DB_NOT_FOUND")

    # mode=ro prevents schema creation and accidental changes to the live RUN.
    with sqlite3.connect(db_path.resolve().as_uri() + "?mode=ro", uri=True) as db:
        db.row_factory = sqlite3.Row
        state = db.execute("SELECT * FROM run_state WHERE run_id=?", (run_id,)).fetchone()
        if state is None or state["run_status"] != "WAITING_HUMAN_REVIEW" or state["current_stage_id"] != "RECONCILIATION":
            raise ValueError("RUN_NOT_WAITING_AT_RECONCILIATION")
        rows = db.execute(
            "SELECT payload_json FROM adapter_results WHERE run_id=? AND stage_id='RECONCILIATION' ORDER BY rowid DESC LIMIT 1",
            (run_id,),
        ).fetchall()
        if len(rows) != 1:
            raise ValueError("RECONCILIATION_RESULT_NOT_FOUND")
        result = json.loads(rows[0]["payload_json"])["reconciliation_result"]

    records = result["records"]
    expected = {record["match_id"]: record for record in records}
    if len(expected) != len(records):
        raise ValueError("RECONCILIATION_MATCH_ID_NOT_UNIQUE")
    folder = output_root / run_id
    files = (
        sorted(
            p for p in folder.glob("DEC-*.json")
            if not p.name.startswith("DEC-AMEND-")
        )
        if folder.is_dir()
        else []
    )
    seen: dict[str, str] = {}
    errors: list[str] = []
    for path in files:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            d = payload["decision"]
            match_id = d["match_id"]
            record = expected.get(match_id)
            if payload.get("type") != "DECISION" or d.get("decision_type") != "HUMAN":
                raise ValueError("NOT_HUMAN_DECISION")
            if record is None or match_id in seen:
                raise ValueError("FOREIGN_OR_DUPLICATE_MATCH_ID")
            if path.name != f"DEC-{run_id}-{match_id}.json" or d.get("decision_id") != path.stem:
                raise ValueError("DECISION_ID_MISMATCH")
            trace = d.get("traceability") or {}
            if (d.get("source_id") != result["source_id"] or
                trace.get("source_id") != result["source_id"] or
                trace.get("match_id") != match_id or
                trace.get("reconciliation_id") != result["reconciliation_id"] or
                trace.get("passport_id") != record["input_record_id"] or
                trace.get("input_batch_id") != record["input_batch_id"] or
                trace.get("source_package") != record["traceability"].get("source_package")):
                raise ValueError("DECISION_LINEAGE_MISMATCH")
            decision_result = d.get("decision_result")
            if decision_result not in {"DEFER", "REJECT", "ADMIT_NEW", "ADMIT_EXISTING"}:
                raise ValueError("DECISION_RESULT_INVALID")
            if not d.get("basis") or not d.get("decided_by") or not d.get("decided_at"):
                raise ValueError("HUMAN_DECISION_FIELDS_MISSING")
            if decision_result in {"DEFER", "REJECT"} and d.get("cmoc_object_id") is not None:
                raise ValueError("NON_ADMISSION_HAS_TARGET")
            seen[match_id] = decision_result
        except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
            errors.append(f"{path.name}: {exc}")

    missing = sorted(expected.keys() - seen.keys())
    counts = dict(sorted(Counter(seen.values()).items()))
    if errors:
        status = "REVIEW_SET_INVALID"
    elif missing:
        status = "REVIEW_SET_INCOMPLETE"
    elif any(value.startswith("ADMIT_") for value in seen.values()):
        status = "REVIEW_SET_COMPLETE_ADMISSION_PENDING"
    else:
        status = "REVIEW_SET_COMPLETE_NO_ADMISSION"
    return {
        "status": status, "run_id": run_id,
        "reconciliation_id": result["reconciliation_id"],
        "run_status": state["run_status"],
        "expected_count": len(expected), "decision_count": len(seen),
        "decision_results": counts, "missing_match_ids": missing,
        "errors": errors,
        "boundary": "Read-only verification; no RUN event, Admission, CMOC, or OBJECT INDEX write",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--output-root")
    args = parser.parse_args()
    db_path = Path(args.db)
    output_root = Path(args.output_root) if args.output_root else db_path.parent / "human_review_decisions"
    try:
        report = inspect_review_set(db_path, args.run_id, output_root)
    except (sqlite3.Error, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        report = {"status": "REVIEW_SET_INVALID", "run_id": args.run_id, "errors": [str(exc)]}
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["status"].startswith("REVIEW_SET_COMPLETE_") else 1


if __name__ == "__main__":
    raise SystemExit(main())
