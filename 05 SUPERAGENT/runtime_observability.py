"""Operational observability view for the local CMOC runtime.

This module exposes execution state only. It does not inspect or reinterpret
semantic CMOC data.
"""

from __future__ import annotations

import json
from dataclasses import asdict
from typing import Any

from runtime_state_store import RuntimeStateStore


def get_run_observation(db_path: str, run_id: str) -> dict[str, Any]:
    store = RuntimeStateStore(db_path)
    try:
        state = store.get_state(run_id)
        if state is None:
            return {
                "status": "RUN_NOT_FOUND",
                "run_id": run_id,
            }

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


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Observe one local CMOC runtime RUN.")
    parser.add_argument("--db", default="05 SUPERAGENT/runtime.sqlite")
    parser.add_argument("--run-id", required=True)
    args = parser.parse_args()

    print(format_run_observation(get_run_observation(args.db, args.run_id)))
