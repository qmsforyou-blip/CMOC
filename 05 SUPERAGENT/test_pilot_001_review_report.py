"""Acceptance test for the human-readable PILOT-001 review report."""
from __future__ import annotations

import json
import sqlite3
import tempfile
from pathlib import Path

from pilot_001_review_report import build_report


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        db_path = Path(td) / "runtime.sqlite"
        with sqlite3.connect(db_path) as db:
            db.execute("CREATE TABLE run_state (run_id TEXT, run_status TEXT, current_stage_id TEXT)")
            db.execute("CREATE TABLE adapter_results (run_id TEXT, stage_id TEXT, payload_json TEXT)")
            db.execute("INSERT INTO run_state VALUES (?, ?, ?)", ("RUN-001", "WAITING_HUMAN_REVIEW", "RECONCILIATION"))
            db.execute("INSERT INTO adapter_results VALUES (?, ?, ?)", ("RUN-001", "DISCOVERY", json.dumps({
                "discovery": {"results": [{"type": "PASSPORT_RECORDS", "records": [{"id": "PAS-001", "term": "Test source"}]}]}
            })))
            db.execute("INSERT INTO adapter_results VALUES (?, ?, ?)", ("RUN-001", "RECONCILIATION", json.dumps({
                "reconciliation_result": {"summary": {"total": 1, "existing_equivalent": 0, "needs_review": 1}, "records": [{
                    "match_id": "MAT-001", "input_record_id": "PAS-001", "match_result": "NEEDS_REVIEW",
                    "status": "PROVISIONAL", "cmoc_object_id": None, "basis": "NO_MATCH",
                    "traceability": {"candidate_id": "NOM-001"}
                }]}
            })))
            db.commit()
        report = build_report(db_path, "RUN-001")
        assert "`RUN-001`" in report
        assert "`MAT-001`" in report
        assert "Test source" in report
        assert "ADMIT_NEW" in report
    print("PILOT-001 HUMAN REVIEW MARKDOWN REPORT: PASS")


if __name__ == "__main__":
    main()
