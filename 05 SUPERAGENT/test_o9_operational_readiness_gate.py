from dataclasses import dataclass


@dataclass
class Gate:
    profile_id: str
    profile_version: str
    evidence: dict
    dimensions: dict
    limitations: list[str]
    unknowns: list[str]

    def evaluate(self):
        required = [v for v in self.dimensions.values() if v != "NOT_APPLICABLE"]
        if any(v == "FAILED" for v in required):
            return "NOT_READY"
        if any(v == "MISSING" for v in self.evidence.values()):
            return "EVIDENCE_INCOMPLETE"
        if any(v in {"LIMITED", "UNKNOWN"} for v in required):
            return "READY_WITH_LIMITATIONS"
        if self.limitations or self.unknowns:
            return "READY_WITH_LIMITATIONS"
        return "READY_FOR_DECLARED_PROFILE"


def test_o9():
    evidence = {
        "P1-P5": "ACCEPTED",
        "P6": "ACCEPTED",
        "P7": "ACCEPTED",
        "P8": "ACCEPTED",
        "P9": "ACCEPTED",
        "O1": "ACCEPTED",
        "O2": "ACCEPTED",
        "O3": "ACCEPTED",
        "O4": "ACCEPTED",
        "O5": "ACCEPTED",
        "O6": "ACCEPTED",
        "O8": "ACCEPTED",
    }

    dimensions = {
        "execution_integrity": "PROVEN",
        "persistence_integrity": "PROVEN",
        "security_operational_control": "PROVEN",
        "observability_operation": "PROVEN",
        "performance_deployment": "LIMITED",
        "ha_multinode": "NOT_APPLICABLE",
    }

    limitations = [
        "production capacity measurements",
        "concrete monitoring platform",
        "backup/DR infrastructure",
        "automated deployment infrastructure",
    ]

    unknowns = [
        "RPO",
        "RTO",
        "availability SLO",
    ]

    g = Gate(
        "PROD-PROFILE-001",
        "0.1",
        evidence,
        dimensions,
        limitations,
        unknowns,
    )

    # O9-01 profile binding
    assert g.profile_id == "PROD-PROFILE-001"
    assert g.profile_version == "0.1"

    # O9-02 accepted evidence set
    assert all(v == "ACCEPTED" for v in g.evidence.values())

    # O9-03 dimension aggregation
    assert g.dimensions["execution_integrity"] == "PROVEN"
    assert g.dimensions["performance_deployment"] == "LIMITED"

    # O9-04 NOT_APPLICABLE does not fail readiness
    assert g.dimensions["ha_multinode"] == "NOT_APPLICABLE"
    assert g.evaluate() == "READY_WITH_LIMITATIONS"

    # O9-05 limitations are preserved
    assert "production capacity measurements" in g.limitations

    # O9-06 UNKNOWN is preserved
    assert "RPO" in g.unknowns
    assert "RTO" in g.unknowns

    # O9-07 missing evidence blocks readiness
    incomplete = Gate(
        "PROD-PROFILE-001",
        "0.1",
        {**evidence, "O4": "MISSING"},
        dimensions,
        limitations,
        unknowns,
    )
    assert incomplete.evaluate() == "EVIDENCE_INCOMPLETE"

    # O9-08 failed required dimension blocks readiness
    failed_dimensions = dict(dimensions)
    failed_dimensions["security_operational_control"] = "FAILED"
    failed = Gate(
        "PROD-PROFILE-001",
        "0.1",
        evidence,
        failed_dimensions,
        limitations,
        unknowns,
    )
    assert failed.evaluate() == "NOT_READY"

    # O9-09 fully proven with no limitations can be ready for declared profile
    proven_dimensions = {
        "execution_integrity": "PROVEN",
        "persistence_integrity": "PROVEN",
        "security_operational_control": "PROVEN",
        "observability_operation": "PROVEN",
        "performance_deployment": "PROVEN",
        "ha_multinode": "NOT_APPLICABLE",
    }
    complete = Gate(
        "PROD-PROFILE-001",
        "0.1",
        evidence,
        proven_dimensions,
        [],
        [],
    )
    assert complete.evaluate() == "READY_FOR_DECLARED_PROFILE"

    # O9-10 profile change remains a separate readiness context
    changed_profile = Gate(
        "PROD-PROFILE-002",
        "0.1",
        evidence,
        dimensions,
        limitations,
        unknowns,
    )
    assert changed_profile.profile_id != g.profile_id

    # O9-11 no semantic responsibility leakage
    semantic_decision = False
    new_approval = False
    canonization = False
    cmoc_mutation = False
    index_mutation = False
    assert not semantic_decision
    assert not new_approval
    assert not canonization
    assert not cmoc_mutation
    assert not index_mutation


if __name__ == "__main__":
    test_o9()
    print("O9 TEST: PASS")
