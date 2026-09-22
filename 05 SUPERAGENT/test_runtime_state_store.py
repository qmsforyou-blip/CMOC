import os
import tempfile

from runtime_state_store import JournalEvent, RuntimeStateStore


def event(run_id, seq, event_id, event_type, stage_id=None,
          result_id=None, attempt_id=None, source_id="SRC-RT-001",
          batch_id="BATCH-RT-001", status="RECORDED"):
    return JournalEvent(
        run_id=run_id,
        event_id=event_id,
        event_seq=seq,
        stage_id=stage_id,
        event_type=event_type,
        stage_result_id=result_id,
        attempt_id=attempt_id,
        event_status=status,
        traceability=f"{run_id}/{event_id}",
        source_id=source_id,
        batch_id=batch_id,
    )


def test_runtime_store():
    fd, path = tempfile.mkstemp(prefix="cmoc-runtime-", suffix=".sqlite")
    os.close(fd)

    try:
        store = RuntimeStateStore(path)

        # RT-01: durable RUN creation
        state = store.append(
            event("RUN-RT-001", 1, "EV-001", "RUN_CREATED",
                  attempt_id="ATT-001")
        )
        assert state.run_status == "ACTIVE"
        assert state.last_event_seq == 1

        # RT-02: stage execution and result lineage
        state = store.append(
            event("RUN-RT-001", 2, "EV-002", "STAGE_STARTED",
                  stage_id="DISCOVERY", result_id="DISC-001",
                  attempt_id="ATT-001")
        )
        assert state.current_stage_id == "DISCOVERY"

        state = store.append(
            event("RUN-RT-001", 3, "EV-003", "STAGE_COMPLETED",
                  stage_id="DISCOVERY", result_id="DISC-001",
                  attempt_id="ATT-001")
        )
        assert state.current_stage_result_id == "DISC-001"

        # RT-03: deterministic projection agrees with persisted state
        assert store.verify_projection("RUN-RT-001")

        # RT-04: failed attempt is retained
        store.append(
            event("RUN-RT-001", 4, "EV-004", "STAGE_STARTED",
                  stage_id="RECONCILIATION", result_id="RECON-001",
                  attempt_id="ATT-002")
        )
        state = store.append(
            event("RUN-RT-001", 5, "EV-005", "STAGE_FAILED",
                  stage_id="RECONCILIATION", result_id="RECON-001",
                  attempt_id="ATT-002")
        )
        assert state.current_attempt_id == "ATT-002"
        assert len(store.read_journal("RUN-RT-001")) == 5

        # RT-05: explicit recovery/retry uses a new attempt
        store.append(
            event("RUN-RT-001", 6, "EV-006", "RECOVERY_REQUESTED",
                  stage_id="RECONCILIATION", attempt_id="ATT-002")
        )
        state = store.append(
            event("RUN-RT-001", 7, "EV-007", "STAGE_STARTED",
                  stage_id="RECONCILIATION", result_id="RECON-002",
                  attempt_id="ATT-003")
        )
        assert state.current_attempt_id == "ATT-003"
        assert state.current_stage_result_id == "RECON-002"

        # RT-06: terminal completion is persisted
        state = store.append(
            event("RUN-RT-001", 8, "EV-008", "STAGE_COMPLETED",
                  stage_id="RECONCILIATION", result_id="RECON-002",
                  attempt_id="ATT-003")
        )
        assert state.current_stage_result_id == "RECON-002"

        # RT-07: duplicate EVENT_ID rejected
        try:
            store.append(
                event("RUN-RT-001", 9, "EV-008", "STAGE_COMPLETED",
                      stage_id="RECONCILIATION", result_id="RECON-002",
                      attempt_id="ATT-003")
            )
            assert False
        except ValueError as exc:
            assert "EVENT_ID" in str(exc)

        # RT-08: sequence regression rejected
        try:
            store.append(
                event("RUN-RT-001", 7, "EV-009", "STAGE_STARTED",
                      stage_id="RECONCILIATION", attempt_id="ATT-004")
            )
            assert False
        except ValueError as exc:
            assert "monotonic" in str(exc)

        # RT-09: cross-run/source identity rejected
        try:
            store.append(
                event("RUN-RT-001", 9, "EV-009", "STAGE_STARTED",
                      stage_id="OTHER", attempt_id="ATT-004",
                      source_id="FOREIGN-SOURCE")
            )
            assert False
        except ValueError as exc:
            assert "SOURCE_ID" in str(exc)

        # RT-10: terminal RUN is protected
        state = store.append(
            event("RUN-RT-001", 9, "EV-009", "RUN_COMPLETED")
        )
        assert state.run_status == "COMPLETED"
        try:
            store.append(
                event("RUN-RT-001", 10, "EV-010", "STAGE_STARTED",
                      stage_id="OTHER", attempt_id="ATT-005")
            )
            assert False
        except ValueError as exc:
            assert "terminal RUN" in str(exc)

        # RT-11: restart from a fresh connection
        store.close()
        store = RuntimeStateStore(path)
        assert store.verify_projection("RUN-RT-001")
        restored = store.get_state("RUN-RT-001")
        assert restored.run_status == "COMPLETED"
        assert restored.current_attempt_id == "ATT-003"
        assert restored.last_event_seq == 9

        # RT-12: semantic boundaries untouched
        assert not hasattr(store, "semantic_decision")
        assert not hasattr(store, "canonization")
        assert not hasattr(store, "cmoc_write")
        assert not hasattr(store, "object_index_write")

        store.close()
        print("RUNTIME STATE STORE TEST: PASS")

    finally:
        try:
            os.remove(path)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    test_runtime_store()
