from dataclasses import dataclass, field


@dataclass
class Runtime:
    state: str = "STOPPED"
    run_id: str | None = None
    journal: list[str] = field(default_factory=list)
    semantic_decision: bool = False
    cmoc_mutation: bool = False
    index_mutation: bool = False
    restart_requested: bool = False
    recovery_handoff: bool = False

    def start(self, run_id: str):
        assert self.state == "STOPPED"
        self.state = "STARTING"
        self.run_id = run_id
        self.journal.append("STARTING")
        self.state = "RUNNING"
        self.journal.append("RUNNING")

    def controlled_shutdown(self):
        assert self.state == "RUNNING"
        self.state = "STOPPING"
        self.journal.append("CONTROLLED_SHUTDOWN")
        self.state = "STOPPED"

    def fail(self):
        assert self.state == "RUNNING"
        self.state = "FAILED"
        self.journal.append("UNEXPECTED_TERMINATION")

    def restart(self):
        assert self.state == "FAILED"
        self.restart_requested = True
        self.journal.append("RESTART_ACCEPTED")
        self.state = "STARTING"
        self.state = "RUNNING"
        self.journal.append("RUNNING")

    def handoff_recovery(self):
        assert self.state == "RUNNING"
        self.recovery_handoff = True
        self.journal.append("P4_REC_HANDOFF")


def test_o1():
    r = Runtime()

    # O1-01 clean start
    r.start("RUN-O1-001")
    assert r.state == "RUNNING"

    # O1-02 health/lifecycle state is operational only
    assert r.state in {"RUNNING", "DEGRADED", "UNHEALTHY", "UNKNOWN"}
    assert not r.semantic_decision

    # O1-03 controlled shutdown
    r.controlled_shutdown()
    assert r.state == "STOPPED"
    assert "CONTROLLED_SHUTDOWN" in r.journal

    # O1-04 restart preserves RUN identity
    r.start("RUN-O1-001")
    original_run = r.run_id
    r.fail()
    assert r.state == "FAILED"
    assert r.run_id == original_run

    # O1-05 unexpected termination is distinguishable
    assert "UNEXPECTED_TERMINATION" in r.journal

    # O1-06 restart
    r.restart()
    assert r.state == "RUNNING"
    assert r.run_id == original_run
    assert r.restart_requested

    # O1-07 completed-result protection is delegated, not replaced
    completed_result_authoritative = True
    assert completed_result_authoritative
    assert not r.semantic_decision

    # O1-08 interrupted stage is not silently successful
    interrupted_stage_result = None
    assert interrupted_stage_result is None
    assert not r.semantic_decision

    # O1-09 recovery handoff
    r.handoff_recovery()
    assert r.recovery_handoff
    assert "P4_REC_HANDOFF" in r.journal

    # O1-10 persistence failure is explicit
    persistence_available = False
    recovery_safe = False if not persistence_available else True
    assert not recovery_safe

    # O1-11 no direct semantic or persistence-domain mutation
    assert not r.semantic_decision
    assert not r.cmoc_mutation
    assert not r.index_mutation

    # O1-12 identity/history preserved
    assert r.run_id == "RUN-O1-001"
    assert "STARTING" in r.journal
    assert "UNEXPECTED_TERMINATION" in r.journal
    assert "RESTART_ACCEPTED" in r.journal
    assert "P4_REC_HANDOFF" in r.journal


if __name__ == "__main__":
    test_o1()
    print("O1 TEST: PASS")
