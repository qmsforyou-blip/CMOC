"""Backup -> restore gate for the local production runtime."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from durable_adapter_persistence import DurableAdapterPersistence
from runtime_backup import backup_runtime, restore_runtime
from runtime_state_store import JournalEvent, RuntimeStateStore


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        db_path = root / "runtime.sqlite"
        backup_path = root / "runtime.backup.sqlite"
        restored_path = root / "runtime.restored.sqlite"

        store = RuntimeStateStore(str(db_path))
        trace = "RUN_ID=RUN-BACKUP-001;SOURCE_ID=SRC-BACKUP-001;SOURCE_PACKAGE_ID=PKG-BACKUP-001"
        store.append(
            JournalEvent(
                run_id="RUN-BACKUP-001", event_id="EVENT-RUN-BACKUP-001-001",
                event_seq=1, stage_id="RUN", event_type="RUN_CREATED",
                stage_result_id="RUN-RESULT-RUN-BACKUP-001",
                attempt_id="ATTEMPT-RUN-BACKUP-001", event_status="ACTIVE",
                traceability=trace, source_id="SRC-BACKUP-001", batch_id="PKG-BACKUP-001",
            ), source_id="SRC-BACKUP-001", batch_id="PKG-BACKUP-001"
        )
        store.append(
            JournalEvent(
                run_id="RUN-BACKUP-001", event_id="EVENT-RUN-BACKUP-001-002",
                event_seq=2, stage_id="DISCOVERY", event_type="STAGE_STARTED",
                stage_result_id="RESULT-DISCOVERY-BACKUP-001",
                attempt_id="ATTEMPT-DISCOVERY-BACKUP-001", event_status="ACTIVE",
                traceability=trace, source_id="SRC-BACKUP-001", batch_id="PKG-BACKUP-001",
            ), source_id="SRC-BACKUP-001", batch_id="PKG-BACKUP-001"
        )
        persistence = DurableAdapterPersistence(store.conn)
        key = ("RUN-BACKUP-001", "DISCOVERY", "ATTEMPT-DISCOVERY-BACKUP-001")
        persistence[key] = {
            "run_id": "RUN-BACKUP-001", "source_id": "SRC-BACKUP-001",
            "batch_id": "PKG-BACKUP-001", "stage_id": "DISCOVERY",
            "attempt_id": "ATTEMPT-DISCOVERY-BACKUP-001",
            "result_id": "RESULT-DISCOVERY-BACKUP-001", "status": "ACCEPT",
        }
        store.close()

        backup_runtime(str(db_path), str(backup_path))
        restored_path.write_bytes(b"not a sqlite database")
        restore_runtime(str(backup_path), str(restored_path))

        restored = RuntimeStateStore(str(restored_path))
        events = restored.read_journal("RUN-BACKUP-001")
        assert [event.event_type for event in events] == ["RUN_CREATED", "STAGE_STARTED"]
        state = restored.get_state("RUN-BACKUP-001")
        assert state is not None
        assert state.current_stage_id == "DISCOVERY"
        assert state.last_event_seq == 2
        assert restored.verify_projection("RUN-BACKUP-001")
        restored_persistence = DurableAdapterPersistence(restored.conn)
        assert key in restored_persistence
        assert restored_persistence[key]["result_id"] == "RESULT-DISCOVERY-BACKUP-001"
        restored.close()

    print("RUNTIME BACKUP/RESTORE TEST: PASS")


if __name__ == "__main__":
    main()
