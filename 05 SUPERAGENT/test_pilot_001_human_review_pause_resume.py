"""PILOT-001 durable human-review pause/resume boundary."""

from __future__ import annotations

import tempfile
from pathlib import Path

from runtime_state_store import JournalEvent, RuntimeStateStore


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        db = Path(td) / "runtime.sqlite"
        store = RuntimeStateStore(str(db))
        trace = "RUN_ID=RUN-PILOT-001;SOURCE_ID=SRC-PILOT-001;SOURCE_PACKAGE_ID=PKG-PILOT-001"

        def append(seq, stage, event_type, result, attempt, status):
            store.append(JournalEvent(
                run_id="RUN-PILOT-001",
                event_id=f"EVENT-RUN-PILOT-001-{seq:03d}",
                event_seq=seq,
                stage_id=stage,
                event_type=event_type,
                stage_result_id=result,
                attempt_id=attempt,
                event_status=status,
                traceability=trace,
                source_id="SRC-PILOT-001",
                batch_id="PKG-PILOT-001",
            ), source_id="SRC-PILOT-001", batch_id="PKG-PILOT-001")

        append(1, "RUN", "RUN_CREATED", "RUN-RESULT-PILOT-001", "ATT-RUN-PILOT-001", "ACTIVE")
        append(2, "RECONCILIATION", "STAGE_STARTED", "RECON-PILOT-001", "ATT-RECON-PILOT-001", "ACTIVE")
        append(3, "RECONCILIATION", "STAGE_COMPLETED", "RECON-PILOT-001", "ATT-RECON-PILOT-001", "COMPLETED")
        append(4, "RECONCILIATION", "HUMAN_REVIEW_REQUIRED", "RECON-PILOT-001", "ATT-RECON-PILOT-001", "NEEDS_REVIEW")

        waiting = store.get_state("RUN-PILOT-001")
        assert waiting is not None
        assert waiting.run_status == "WAITING_HUMAN_REVIEW"
        assert waiting.current_stage_id == "RECONCILIATION"
        assert waiting.current_stage_result_id == "RECON-PILOT-001"
        assert store.verify_projection("RUN-PILOT-001")

        store.close()
        store = RuntimeStateStore(str(db))
        waiting_after_restart = store.get_state("RUN-PILOT-001")
        assert waiting_after_restart is not None
        assert waiting_after_restart.run_status == "WAITING_HUMAN_REVIEW"
        assert store.verify_projection("RUN-PILOT-001")

        append(5, "RECONCILIATION", "HUMAN_DECISION_RECORDED", "DECISION-PILOT-001", "ATT-DECISION-PILOT-001", "ADMIT_NEW")
        resumed = store.get_state("RUN-PILOT-001")
        assert resumed is not None
        assert resumed.run_status == "ACTIVE"
        assert resumed.current_stage_id == "RECONCILIATION"
        assert resumed.current_stage_result_id == "DECISION-PILOT-001"
        assert store.verify_projection("RUN-PILOT-001")

        events = store.read_journal("RUN-PILOT-001")
        assert [e.event_type for e in events][-2:] == [
            "HUMAN_REVIEW_REQUIRED",
            "HUMAN_DECISION_RECORDED",
        ]
        store.close()

    print("PILOT-001 HUMAN REVIEW PAUSE/RESUME TEST: PASS")


if __name__ == "__main__":
    main()
