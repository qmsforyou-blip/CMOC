"""Boundary tests for complete, incomplete, and invalid human review sets."""

from __future__ import annotations

import json
import sqlite3
import tempfile
from pathlib import Path

from pilot_001_review_set_probe import inspect_review_set


RUN = "RUN-REVIEW-TEST"
RECON = "RECON-REVIEW-TEST"
SOURCE = "SRC-TEST"
PACKAGE = "PACKAGE-TEST"


def setup(root: Path) -> tuple[Path, Path]:
    db_path = root / "runtime.sqlite"
    with sqlite3.connect(db_path) as db:
        db.execute("CREATE TABLE run_state (run_id TEXT, run_status TEXT, current_stage_id TEXT)")
        db.execute("INSERT INTO run_state VALUES (?,?,?)", (RUN, "WAITING_HUMAN_REVIEW", "RECONCILIATION"))
        db.execute("CREATE TABLE adapter_results (run_id TEXT, stage_id TEXT, payload_json TEXT)")
        records = [{"match_id": f"MAT-PAS-{i:03d}", "input_record_id": f"PAS-{i:03d}",
                    "input_batch_id": "BATCH-TEST", "traceability": {"source_package": PACKAGE}}
                   for i in (1, 2)]
        payload = {"reconciliation_result": {"reconciliation_id": RECON,
                   "source_id": SOURCE, "records": records}}
        db.execute("INSERT INTO adapter_results VALUES (?,?,?)", (RUN, "RECONCILIATION", json.dumps(payload)))
    folder = root / "human_review_decisions" / RUN
    folder.mkdir(parents=True)
    return db_path, folder


def decision(folder: Path, i: int, result: str, **changes) -> Path:
    match_id = f"MAT-PAS-{i:03d}"
    did = f"DEC-{RUN}-{match_id}"
    payload = {"type": "DECISION", "decision": {
        "decision_id": did, "decision_type": "HUMAN", "decision_result": result,
        "match_id": match_id, "source_id": SOURCE, "cmoc_object_id": None,
        "basis": "Reviewed source", "decided_by": "SG", "decided_at": "2026-09-28T00:00:00Z",
        "traceability": {"source_id": SOURCE, "match_id": match_id,
                         "reconciliation_id": RECON, "passport_id": f"PAS-{i:03d}",
                         "input_batch_id": "BATCH-TEST", "source_package": PACKAGE}}}
    payload["decision"].update(changes)
    path = folder / f"{did}.json"
    path.write_text(json.dumps(payload), encoding="utf-8")
    return path


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        db, folder = setup(root)
        before = db.read_bytes()
        assert inspect_review_set(db, RUN, root / "human_review_decisions")["status"] == "REVIEW_SET_INCOMPLETE"
        decision(folder, 1, "DEFER")
        partial = inspect_review_set(db, RUN, root / "human_review_decisions")
        assert partial["missing_match_ids"] == ["MAT-PAS-002"]
        decision(folder, 2, "REJECT")
        complete = inspect_review_set(db, RUN, root / "human_review_decisions")
        assert complete["status"] == "REVIEW_SET_COMPLETE_NO_ADMISSION"
        assert complete["decision_results"] == {"DEFER": 1, "REJECT": 1}
        assert db.read_bytes() == before

        decision(folder, 2, "REJECT", source_id="SRC-FOREIGN")
        assert inspect_review_set(db, RUN, root / "human_review_decisions")["status"] == "REVIEW_SET_INVALID"
        decision(folder, 2, "REJECT")
        decision(folder, 2, "REJECT", traceability={"source_id": SOURCE})
        assert inspect_review_set(db, RUN, root / "human_review_decisions")["status"] == "REVIEW_SET_INVALID"
        decision(folder, 2, "REJECT")
        extra = folder / f"DEC-{RUN}-MAT-PAS-999.json"
        extra.write_text((folder / f"DEC-{RUN}-MAT-PAS-001.json").read_text(encoding="utf-8"), encoding="utf-8")
        assert inspect_review_set(db, RUN, root / "human_review_decisions")["status"] == "REVIEW_SET_INVALID"
        extra.unlink()
        decision(folder, 2, "ADMIT_NEW")
        assert inspect_review_set(db, RUN, root / "human_review_decisions")["status"] == "REVIEW_SET_COMPLETE_ADMISSION_PENDING"
        assert db.read_bytes() == before
    print("PILOT REVIEW SET PROBE: PASS")


if __name__ == "__main__":
    main()
