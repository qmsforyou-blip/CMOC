import os
import tempfile

from runtime_state_store import JournalEvent, RuntimeStateStore
from runtime_attempt_store import AttemptStore
from runtime_restart_resume import RestartResumeController


def ev(run_id, seq, eid, typ, stage=None, result=None, attempt=None,
       source="SRC-P4-001", batch="BATCH-P4-001"):
    return JournalEvent(
        run_id, eid, seq, stage, typ, result, attempt, "RECORDED",
        f"{run_id}/{eid}", source, batch
    )


def test_restart_resume():
    fd, path = tempfile.mkstemp(prefix="cmoc-p4-", suffix=".sqlite")
    os.close(fd)

    try:
        state = RuntimeStateStore(path)
        attempts = AttemptStore(path)
        controller = RestartResumeController(state, attempts)

        # P4-RT-01: interrupted RUNNING attempt can resume.
        state.append(ev("RUN-P4-001", 1, "EV-001", "RUN_CREATED",
                        attempt="ATT-RUN-001"))
        state.append(ev("RUN-P4-001", 2, "EV-002", "STAGE_STARTED",
                        "CMOC_WRITE", "RES-001", "ATT-C2-001"))
        assert attempts.register(
            "RUN-P4-001", "CMOC_WRITE", "ATT-C2-001",
            "RES-001", "KEY-001"
        ) == "ACCEPTED"
        decision = controller.inspect("RUN-P4-001")
        assert decision.status == "RESUME_ALLOWED"

        # P4-RT-02: failed attempt requires explicit retry.
        state.append(ev("RUN-P4-001", 3, "EV-003", "STAGE_FAILED",
                        "CMOC_WRITE", "RES-001", "ATT-C2-001"))
        attempts.close()
        attempts = AttemptStore(path)
        controller = RestartResumeController(state, attempts)
        decision = controller.inspect("RUN-P4-001")
        assert decision.status == "RETRY_REQUIRED"

        # P4-RT-03: completed authoritative attempt is protected.
        assert attempts.mark_authoritative(
            "RUN-P4-001", "CMOC_WRITE", "ATT-C2-001"
        ) == "COMMITTED"
        decision = controller.inspect("RUN-P4-001")
        assert decision.status == "ALREADY_COMPLETED"

        # P4-RT-04: terminal RUN remains protected after restart.
        state.append(ev("RUN-P4-001", 4, "EV-004", "RUN_COMPLETED"))
        state.close()
        attempts.close()

        state = RuntimeStateStore(path)
        attempts = AttemptStore(path)
        controller = RestartResumeController(state, attempts)
        decision = controller.inspect("RUN-P4-001")
        assert decision.status == "ALREADY_COMPLETED"

        # P4-RT-05: unknown RUN is rejected.
        decision = controller.inspect("RUN-P4-UNKNOWN")
        assert decision.status == "RUN_REJECTED"

        # P4-RT-06: interrupted attempt missing from P3 registry is not invented.
        state.append(ev("RUN-P4-002", 1, "EV-101", "RUN_CREATED",
                        attempt="ATT-RUN-002"))
        state.append(ev("RUN-P4-002", 2, "EV-102", "STAGE_STARTED",
                        "RECONCILIATION", "RES-201", "ATT-R-001"))
        decision = controller.inspect("RUN-P4-002")
        assert decision.status == "RECOVERY_REQUIRES_REVIEW"

        # P4-RT-07: a failed attempt stays in history; retry identity is explicit.
        assert attempts.register(
            "RUN-P4-002", "RECONCILIATION", "ATT-R-001",
            "RES-201", "KEY-R-001", status="FAILED"
        ) == "ACCEPTED"
        assert controller.inspect("RUN-P4-002").status == "RETRY_REQUIRED"
        assert attempts.register(
            "RUN-P4-002", "RECONCILIATION", "ATT-R-002",
            "RES-202", "KEY-R-002"
        ) == "ACCEPTED"

        # P4-RT-08: cross-run identity is rejected by P2/P3.
        try:
            state.append(ev("RUN-P4-002", 3, "EV-103", "STAGE_STARTED",
                            "RECONCILIATION", "RES-203", "ATT-R-003",
                            source="FOREIGN-SOURCE"))
            assert False
        except ValueError as exc:
            assert "SOURCE_ID" in str(exc)

        # P4-RT-09: projection remains deterministic.
        assert state.verify_projection("RUN-P4-001")
        assert state.verify_projection("RUN-P4-002")

        # P4-RT-10: no semantic/runtime leakage.
        assert not hasattr(controller, "semantic_decision")
        assert not hasattr(controller, "canonization")
        assert not hasattr(controller, "cmoc_write")
        assert not hasattr(controller, "object_index_write")

        # P4-RT-11: restart/reopen preserves decisions.
        state.close()
        attempts.close()
        state = RuntimeStateStore(path)
        attempts = AttemptStore(path)
        controller = RestartResumeController(state, attempts)
        assert controller.inspect("RUN-P4-001").status == "ALREADY_COMPLETED"
        assert controller.inspect("RUN-P4-002").status == "RETRY_REQUIRED"

        # P4-RT-12: source of truth remains journal + attempt registry.
        assert len(state.read_journal("RUN-P4-001")) == 4
        assert state.get_state("RUN-P4-001").last_event_seq == 4

        state.close()
        attempts.close()
        print("RUNTIME RESTART RESUME TEST: PASS")

    finally:
        try:
            os.remove(path)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    test_restart_resume()
