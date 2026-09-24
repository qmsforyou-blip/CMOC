"""Operational observability view for the local CMOC runtime.

This module exposes execution state only. It does not inspect or reinterpret
semantic CMOC data.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from typing import Any

from runtime_state_store import RuntimeStateStore


def get_run_observation(db_path: str, run_id: str) -> dict[str, Any]:
    store = RuntimeStateStore(db_path)
    try:
        state = store.get_state(run_id)
        if state is None:
            return {"status": "RUN_NOT_FOUND", "run_id": run_id}

        events = store.read_journal(run_id)
        return {
            "status": "OBSERVED",
            "run": asdict(state),
            "journal": [asdict(event) for event in events],
            "projection_valid": store.verify_projection(run_id),
        }
    finally:
        store.close()


def format_run_observation(observation: dict[str, Any]) -> str:
    return json.dumps(observation, ensure_ascii=False, indent=2)


def format_operator_view(observation: dict[str, Any]) -> str:
    if observation["status"] == "RUN_NOT_FOUND":
        return f"RUN: {observation['run_id']}\nSTATUS: NOT FOUND"

    run = observation["run"]
    events = observation["journal"]
    recovery = any(
        event["event_type"] in {
            "RECOVERY_REQUESTED", "RESUME_ALLOWED", "RETRY_REQUIRED"
        }
        for event in events
    )
    projection = "VALID" if observation["projection_valid"] else "INVALID"

    return "\n".join([
        f"RUN: {run['run_id']}",
        f"STATUS: {run['run_status']}",
        "",
        f"SOURCE: {run['source_id']}",
        f"PACKAGE: {run['batch_id']}",
        "",
        f"STAGE: {run['current_stage_id'] or '-'}",
        f"ATTEMPT: {run['current_attempt_id'] or '-'}",
        f"RESULT: {run['current_stage_result_id'] or '-'}",
        "",
        f"EVENTS: {len(events)}",
        f"LAST EVENT SEQ: {run['last_event_seq']}",
        f"RECOVERY: {'YES' if recovery else 'NO'}",
        f"PROJECTION: {projection}",
    ])


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Observe one local CMOC runtime RUN."
    )
    parser.add_argument("--db", default="05 SUPERAGENT/runtime.sqlite")
    parser.add_argument("--run-id", required=True)
    parser.add_argument(
        "--view", choices=("operator", "json"), default="operator",
        help="Human-readable operator view or machine-readable JSON.",
    )
    args = parser.parse_args()

    observation = get_run_observation(args.db, args.run_id)
    print(
        format_operator_view(observation)
        if args.view == "operator"
        else format_run_observation(observation)
    )
    return 0 if observation["status"] == "OBSERVED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
