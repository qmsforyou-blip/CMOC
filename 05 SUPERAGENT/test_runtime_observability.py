"""Acceptance test for local runtime observability."""

from __future__ import annotations

import tempfile
from pathlib import Path

from runtime_observability import get_run_observation
from runtime_state_store import JournalEvent, RuntimeStateStore


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        db = Path(td) / "runtime.sqlite"
        store = RuntimeStateStore(str(db))
        trace = "RUN_ID=RUN-OBS-001;SOURCE_ID=SRC-OBS-001;SOURCE_PACKAGE_ID=PKG-OBS-001"

        store.append(
            JournalEvent(
                run_id="RUN-OBS-001",
                event_id="EVENT-RUN-OBS-001-001",
                event_seq=1,
                stage_id="RUN",
                event_type="RUN_CREATED",
                stage_result_id="RUN-RESULT-RUN-OBS-001",
                attempt_id="ATTEMPT-RUN-OBS-001",
                event_status="ACTIVE",
                traceability=trace,
                source_id="SRC-OBS-001",
                batch_id="PKG-OBS-001",
            ),
            source_id="SRC-OBS-001",
            batch_id="PKG-OBS-001",
        )
        store.append(
            JournalEvent(
                run_id="RUN-OBS-001",
                event_id="EVENT-RUN-OBS-001-002",
                event_seq=2,
                stage_id="DISCOVERY",
                event_type="STAGE_STARTED",
                stage_result_id="RESULT-DISCOVERY-OBS-001",
                attempt_id="ATTEMPT-DISCOVERY-OBS-001",
                event_status="ACTIVE",
                traceability=trace,
                source_id="SRC-OBS-001",
                batch_id="PKG-OBS-001",
            ),
            source_id="SRC-OBS-001",
            batch_id="PKG-OBS-001",
        )
        store.close()

        observed = get_run_observation(str(db), "RUN-OBS-001")
        assert observed["status"] == "OBSERVED"
        assert observed["projection_valid"] is True
        assert observed["run"]["run_status"] == "ACTIVE"
        assert observed["run"]["current_stage_id"] == "DISCOVERY"
        assert observed["run"]["current_attempt_id"] == "ATTEMPT-DISCOVERY-OBS-001"
        assert observed["run"]["last_event_seq"] == 2
        assert [e["event_type"] for e in observed["journal"]] == [
            "RUN_CREATED",
            "STAGE_STARTED",
        ]

        missing = get_run_observation(str(db), "RUN-DOES-NOT-EXIST")
        assert missing == {
            "status": "RUN_NOT_FOUND",
            "run_id": "RUN-DOES-NOT-EXIST",
        }

    print("RUNTIME OBSERVABILITY TEST: PASS")


if __name__ == "__main__":
    main()
