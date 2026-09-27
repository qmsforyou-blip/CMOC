"""Record one explicit human decision while a PILOT-001 RUN waits for review.

Uses the existing DECISION builder and store. Partial review never advances the
RUN or changes RECONCILIATION, CMOC, or OBJECT INDEX.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

from decision import build_decision
from decision_store import DecisionStore
from runtime_state_store import RuntimeStateStore


def record_review(db_path: Path, run_id: str, match_id: str, result: str,
                  basis: str, decided_by: str, output_root: Path) -> dict:
    store = RuntimeStateStore(str(db_path))
    try:
        state = store.get_state(run_id)
        if state is None or state.run_status != "WAITING_HUMAN_REVIEW":
            raise ValueError("RUN_NOT_WAITING_HUMAN_REVIEW")
        if state.current_stage_id != "RECONCILIATION":
            raise ValueError("RUN_NOT_AT_RECONCILIATION")
        row = store.conn.execute(
            "SELECT payload_json FROM adapter_results WHERE run_id=? AND stage_id='RECONCILIATION' ORDER BY rowid DESC LIMIT 1",
            (run_id,),
        ).fetchone()
        if row is None:
            raise ValueError("RECONCILIATION_RESULT_NOT_FOUND")
        reconciliation = json.loads(row[0])["reconciliation_result"]
        records = reconciliation["records"]
        matches = [r for r in records if r["match_id"] == match_id]
        if len(matches) != 1:
            raise ValueError("MATCH_ID_NOT_UNIQUE_IN_RUN")
        if not run_id or any(ch in run_id for ch in "/\\"):
            raise ValueError("INVALID_RUN_ID")
        decision_id = f"DEC-{run_id}-{match_id}"
        destination = output_root / run_id
        decisions = DecisionStore(destination)
        existing_path = destination / f"{decision_id}.json"
        if existing_path.exists():
            existing = decisions.read(decision_id)["decision"]
            if (existing["decision_result"], existing["basis"], existing["decided_by"]) != (result, basis, decided_by):
                raise ValueError("HUMAN_DECISION_CONFLICT")
            return {"status": "ALREADY_PERSISTED", "run_id": run_id,
                    "match_id": match_id, "decision_id": decision_id,
                    "decision_result": result, "decision_path": str(existing_path),
                    "run_status": state.run_status,
                    "projection_valid": store.verify_projection(run_id)}
        decision = build_decision(
            decision_id, "HUMAN", result, matches[0], basis,
            decided_by=decided_by,
            decided_at=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        )
        outcome = decisions.write(decision)
        # DecisionStore is authoritative for this partial review. The runtime
        # journal's aggregate HUMAN_DECISION_RECORDED event is intentionally
        # withheld while other records still need review.
        return {"status": outcome, "run_id": run_id, "match_id": match_id,
                "decision_id": decision_id, "decision_result": result,
                "decision_path": str(destination / f"{decision_id}.json"),
                "run_status": store.get_state(run_id).run_status,
                "projection_valid": store.verify_projection(run_id)}
    finally:
        store.close()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", required=True)
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--match-id", required=True)
    parser.add_argument("--decision", required=True, choices=("ADMIT_EXISTING", "ADMIT_NEW", "REJECT", "DEFER"))
    parser.add_argument("--basis", required=True)
    parser.add_argument("--decided-by", required=True)
    parser.add_argument("--output-root")
    args = parser.parse_args()
    db_path = Path(args.db)
    if not db_path.is_file():
        raise FileNotFoundError(db_path)
    output_root = Path(args.output_root) if args.output_root else db_path.parent / "human_review_decisions"
    print(json.dumps(record_review(db_path, args.run_id, args.match_id,
                                   args.decision, args.basis, args.decided_by,
                                   output_root), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
