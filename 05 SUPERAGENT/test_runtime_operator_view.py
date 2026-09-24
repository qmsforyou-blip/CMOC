"""Acceptance test for the operator-facing runtime observability view."""

from __future__ import annotations

import tempfile
from pathlib import Path

from runtime_observability import format_operator_view, get_run_observation
from runtime_state_store import JournalEvent, RuntimeStateStore


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        db = Path(td) / "runtime.sqlite"
        store = RuntimeStateStore(str(db))
        trace = "RUN_ID=RUN-OBS-002;SOURCE_ID=SRC-OBS-002;SOURCE_PACKAGE_ID=PKG-OBS-002"

        store.append(JournalEvent(
            run_id="RUN-OBS-002", event_id="EVENT-RUN-OBS-002-001",
            event_seq=1, stage_id="RUN", event_type="RUN_CREATED",
            stage_result_id="RUN-RESULT-RUN-OBS-002",
            attempt_id="ATTEMPT-RUN-OBS-002", event_status="ACTIVE",
            traceability=trace, source_id="SRC-OBS-002", batch_id="PKG-OBS-002",
        ), source_id="SRC-OBS-002", batch_id="PKG-OBS-002")
        store.append(JournalEvent(
            run_id="RUN-OBS-002", event_id="EVENT-RUN-OBS-002-002",
            event_seq=2, stage_id="DISCOVERY", event_type="STAGE_STARTED",
            stage_result_id="RESULT-DISCOVERY-OBS-002",
            attempt_id="ATTEMPT-DISCOVERY-OBS-002", event_status="ACTIVE",
            traceability=trace, source_id="SRC-OBS-002", batch_id="PKG-OBS-002",
        ), source_id="SRC-OBS-002", batch_id="PKG-OBS-002")
        store.close()

        observed = get_run_observation(str(db), "RUN-OBS-002")
        view = format_operator_view(observed)

        for line in [
            "RUN: RUN-OBS-002", "STATUS: ACTIVE", "SOURCE: SRC-OBS-002",
            "PACKAGE: PKG-OBS-002", "STAGE: DISCOVERY",
            "ATTEMPT: ATTEMPT-DISCOVERY-OBS-002",
            "RESULT: RESULT-DISCOVERY-OBS-002", "EVENTS: 2",
            "LAST EVENT SEQ: 2", "RECOVERY: NO", "PROJECTION: VALID",
        ]:
            assert line in view, line

        missing = get_run_observation(str(db), "RUN-DOES-NOT-EXIST")
        assert format_operator_view(missing) == (
            "RUN: RUN-DOES-NOT-EXIST\nSTATUS: NOT FOUND"
        )

    print("RUNTIME OPERATOR VIEW TEST: PASS")


if __name__ == "__main__":
    main()
