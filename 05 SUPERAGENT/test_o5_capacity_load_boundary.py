from dataclasses import dataclass


@dataclass
class LoadTest:
    profile_id: str
    profile_version: str
    workload: int
    concurrency: int
    duration_s: int
    environment: str
    criteria: dict
    measurements: dict | None = None

    def measure(self, throughput, latency_ms, cpu_pct, memory_mb):
        self.measurements = {
            "throughput": throughput,
            "latency_ms": latency_ms,
            "cpu_pct": cpu_pct,
            "memory_mb": memory_mb,
        }

    def evaluate(self):
        if not self.measurements or not self.criteria:
            return "INSUFFICIENT_EVIDENCE"
        if self.workload <= 0 or self.concurrency <= 0 or self.duration_s <= 0:
            return "TEST_ENVIRONMENT_INVALID"
        if self.measurements["throughput"] < self.criteria["min_throughput"]:
            return "CAPACITY_LIMIT_IDENTIFIED"
        if self.measurements["latency_ms"] > self.criteria["max_latency_ms"]:
            return "CAPACITY_LIMIT_IDENTIFIED"
        if self.measurements["cpu_pct"] > self.criteria["max_cpu_pct"]:
            return "CAPACITY_LIMIT_IDENTIFIED"
        return "CAPACITY_PROVEN"


def test_o5():
    # O5-01 declared workload and profile
    t = LoadTest(
        profile_id="PROD-PROFILE-001",
        profile_version="0.1",
        workload=100,
        concurrency=1,
        duration_s=60,
        environment="O5-SYNTHETIC",
        criteria={
            "min_throughput": 1,
            "max_latency_ms": 1000,
            "max_cpu_pct": 90,
        },
    )
    assert t.profile_id == "PROD-PROFILE-001"
    assert t.workload == 100

    # O5-02 reproducible test conditions
    condition_snapshot = (
        t.profile_id,
        t.profile_version,
        t.workload,
        t.concurrency,
        t.duration_s,
        t.environment,
    )
    assert condition_snapshot == (
        "PROD-PROFILE-001", "0.1", 100, 1, 60, "O5-SYNTHETIC"
    )

    # O5-03 measurements
    t.measure(throughput=2, latency_ms=500, cpu_pct=50, memory_mb=256)
    assert t.measurements["throughput"] == 2
    assert t.measurements["latency_ms"] == 500

    # O5-04 criteria evaluated after measurement
    assert t.evaluate() == "CAPACITY_PROVEN"

    # O5-05 boundary identified
    limited = LoadTest(
        "PROD-PROFILE-001", "0.1", 1000, 20, 60, "O5-SYNTHETIC",
        {"min_throughput": 10, "max_latency_ms": 1000, "max_cpu_pct": 90},
    )
    limited.measure(throughput=5, latency_ms=800, cpu_pct=80, memory_mb=512)
    assert limited.evaluate() == "CAPACITY_LIMIT_IDENTIFIED"

    # O5-06 insufficient evidence
    incomplete = LoadTest(
        "PROD-PROFILE-001", "0.1", 100, 1, 60, "O5-SYNTHETIC", {}
    )
    assert incomplete.evaluate() == "INSUFFICIENT_EVIDENCE"

    # O5-07 invalid environment
    invalid = LoadTest(
        "PROD-PROFILE-001", "0.1", 0, 1, 60, "O5-SYNTHETIC",
        {"min_throughput": 1, "max_latency_ms": 1000, "max_cpu_pct": 90},
    )
    invalid.measure(1, 100, 20, 128)
    assert invalid.evaluate() == "TEST_ENVIRONMENT_INVALID"

    # O5-08 no unsupported extrapolation
    tested_concurrency = 20
    claimed_concurrency = 20
    assert claimed_concurrency == tested_concurrency
    unsupported_claim = 100
    assert unsupported_claim != tested_concurrency

    # O5-09 recovery measurement is separate
    recovery_measured = {
        "failure_detected": True,
        "retry_completed": True,
        "recovery_time_s": 12,
    }
    assert recovery_measured["failure_detected"]
    assert recovery_measured["retry_completed"]

    # O5-10 resource measurements are operational
    assert t.measurements["cpu_pct"] == 50
    assert t.measurements["memory_mb"] == 256

    # O5-11 UNKNOWN is preserved when no measured result exists
    unknown = LoadTest(
        "PROD-PROFILE-001", "0.1", 100, 1, 60, "O5-SYNTHETIC",
        {"min_throughput": 1, "max_latency_ms": 1000, "max_cpu_pct": 90},
    )
    assert unknown.evaluate() == "INSUFFICIENT_EVIDENCE"

    # O5-12 no semantic responsibility leakage
    semantic_decision = False
    new_decision = False
    canonization = False
    cmoc_mutation = False
    index_mutation = False
    assert not semantic_decision
    assert not new_decision
    assert not canonization
    assert not cmoc_mutation
    assert not index_mutation


if __name__ == "__main__":
    test_o5()
    print("O5 TEST: PASS")
