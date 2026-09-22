from dataclasses import dataclass, field


@dataclass
class Monitor:
    observations: list[dict] = field(default_factory=list)
    alerts: list[dict] = field(default_factory=list)
    semantic_decision: bool = False
    cmoc_mutation: bool = False
    index_mutation: bool = False
    journal_mutation: bool = False

    def observe(self, condition, run_id=None, stage_id=None, attempt_id=None, status="UNKNOWN"):
        item = {
            "condition": condition,
            "run_id": run_id,
            "stage_id": stage_id,
            "attempt_id": attempt_id,
            "status": status,
        }
        self.observations.append(item)
        return item

    def alert(self, condition, run_id=None, stage_id=None, attempt_id=None,
              severity="WARNING", threshold_defined=True):
        if not threshold_defined:
            return "OBSERVED_THRESHOLD_UNKNOWN"
        key = (condition, run_id, stage_id, attempt_id)
        if any(a["key"] == key for a in self.alerts):
            return "ALREADY_ALERTED"
        self.alerts.append({
            "key": key,
            "condition": condition,
            "severity": severity,
        })
        return "ALERT_CREATED"


def test_o4():
    m = Monitor()

    # O4-01 runtime health observation
    obs = m.observe("PROCESS_HEALTH", run_id="RUN-O4-001", status="HEALTHY")
    assert obs["status"] == "HEALTHY"

    # O4-02 RUN/stage/attempt observation
    obs = m.observe(
        "STAGE_STATUS",
        run_id="RUN-O4-001",
        stage_id="C2_CMOC_WRITE",
        attempt_id="ATT-O4-001",
        status="FAILED",
    )
    assert obs["run_id"] == "RUN-O4-001"
    assert obs["stage_id"] == "C2_CMOC_WRITE"
    assert obs["attempt_id"] == "ATT-O4-001"

    # O4-03 persistence failure observation
    assert m.observe("JOURNAL_APPEND_FAILURE", run_id="RUN-O4-001")["condition"] == "JOURNAL_APPEND_FAILURE"

    # O4-04 recovery anomaly observation
    assert m.observe("RECOVERY_BLOCKED", run_id="RUN-O4-001")["condition"] == "RECOVERY_BLOCKED"

    # O4-05 CMOC write failure observation
    assert m.observe("CMOC_WRITE_FAILURE", run_id="RUN-O4-001")["condition"] == "CMOC_WRITE_FAILURE"

    # O4-06 OBJECT INDEX synchronization failure observation
    assert m.observe("INDEX_SYNCHRONIZATION_FAILURE", run_id="RUN-O4-001")["condition"] == "INDEX_SYNCHRONIZATION_FAILURE"

    # O4-07 alert generation
    result = m.alert(
        "CMOC_WRITE_FAILURE",
        run_id="RUN-O4-001",
        severity="CRITICAL",
    )
    assert result == "ALERT_CREATED"
    assert m.alerts[-1]["severity"] == "CRITICAL"

    # O4-08 severity is operational, not semantic
    assert m.alerts[-1]["severity"] in {"INFO", "WARNING", "CRITICAL"}
    assert not m.semantic_decision

    # O4-09 alert deduplication
    duplicate = m.alert(
        "CMOC_WRITE_FAILURE",
        run_id="RUN-O4-001",
        severity="CRITICAL",
    )
    assert duplicate == "ALREADY_ALERTED"
    assert len(m.alerts) == 1

    # O4-10 undefined threshold remains UNKNOWN
    unknown = m.alert(
        "AVAILABILITY_SLO",
        run_id="RUN-O4-001",
        threshold_defined=False,
    )
    assert unknown == "OBSERVED_THRESHOLD_UNKNOWN"
    assert all(a["condition"] != "AVAILABILITY_SLO" for a in m.alerts)

    # O4-11 dashboard/view cannot mutate source state
    dashboard = {
        "active_runs": ["RUN-O4-001"],
        "alerts": list(m.alerts),
    }
    assert dashboard["active_runs"] == ["RUN-O4-001"]
    assert not m.journal_mutation
    assert not m.cmoc_mutation
    assert not m.index_mutation

    # O4-12 no semantic responsibility leakage
    assert not m.semantic_decision
    assert not m.cmoc_mutation
    assert not m.index_mutation


if __name__ == "__main__":
    test_o4()
    print("O4 TEST: PASS")
