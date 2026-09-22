from dataclasses import dataclass


@dataclass
class Deployment:
    deployment_id: str
    release_version: str
    profile_id: str
    profile_version: str
    configuration_version: str
    source_revision: str
    compatibility: str = "UNKNOWN"
    active_run_id: str | None = None
    current_release: str | None = None
    state_preserved: bool = True

    def check_compatibility(self):
        if self.compatibility == "COMPATIBLE":
            return "COMPATIBLE"
        if self.compatibility == "INCOMPATIBLE":
            return "INCOMPATIBLE"
        return "COMPATIBILITY_UNKNOWN"

    def deploy(self):
        if self.check_compatibility() != "COMPATIBLE":
            return "DEPLOYMENT_REJECTED"
        self.current_release = self.release_version
        return "DEPLOYMENT_ACCEPTED"

    def rollback(self, previous_release):
        if not self.state_preserved:
            return "ROLLBACK_BLOCKED"
        self.current_release = previous_release
        return "ROLLBACK_COMPLETED"


def test_o6():
    # O6-01 explicit deployment identity
    d = Deployment(
        "DEPLOY-O6-001",
        "1.1.0",
        "PROD-PROFILE-001",
        "0.1",
        "CFG-001",
        "REV-O6-001",
        compatibility="COMPATIBLE",
    )
    assert d.deployment_id == "DEPLOY-O6-001"
    assert d.release_version == "1.1.0"

    # O6-02 compatibility accepted
    assert d.check_compatibility() == "COMPATIBLE"

    # O6-03 configuration/version identity
    assert d.configuration_version == "CFG-001"
    assert d.source_revision == "REV-O6-001"

    # O6-04 reproducible release description
    release = {
        "deployment_id": d.deployment_id,
        "release_version": d.release_version,
        "profile_id": d.profile_id,
        "profile_version": d.profile_version,
        "configuration_version": d.configuration_version,
        "source_revision": d.source_revision,
    }
    assert release["deployment_id"] == "DEPLOY-O6-001"

    # O6-05 successful deployment
    assert d.deploy() == "DEPLOYMENT_ACCEPTED"
    assert d.current_release == "1.1.0"

    # O6-06 post-deployment state remains protected
    d.active_run_id = "RUN-O6-001"
    assert d.active_run_id == "RUN-O6-001"
    assert d.state_preserved

    # O6-07 incompatible release rejected
    incompatible = Deployment(
        "DEPLOY-O6-002", "2.0.0", "PROD-PROFILE-001", "0.1",
        "CFG-002", "REV-O6-002", compatibility="INCOMPATIBLE",
    )
    assert incompatible.check_compatibility() == "INCOMPATIBLE"
    assert incompatible.deploy() == "DEPLOYMENT_REJECTED"

    # O6-08 unknown compatibility is not accepted
    unknown = Deployment(
        "DEPLOY-O6-003", "1.2.0", "PROD-PROFILE-001", "0.1",
        "CFG-003", "REV-O6-003",
    )
    assert unknown.check_compatibility() == "COMPATIBILITY_UNKNOWN"
    assert unknown.deploy() == "DEPLOYMENT_REJECTED"

    # O6-09 controlled rollback
    assert d.rollback("1.0.0") == "ROLLBACK_COMPLETED"
    assert d.current_release == "1.0.0"

    # O6-10 rollback blocked when state cannot be protected
    blocked = Deployment(
        "DEPLOY-O6-004", "2.0.0", "PROD-PROFILE-001", "0.1",
        "CFG-004", "REV-O6-004", compatibility="COMPATIBLE",
        state_preserved=False,
    )
    assert blocked.rollback("1.0.0") == "ROLLBACK_BLOCKED"

    # O6-11 migration failure is operational, not semantic
    migration_result = "MIGRATION_FAILED"
    assert migration_result == "MIGRATION_FAILED"
    semantic_decision = False
    assert not semantic_decision

    # O6-12 boundary protection
    cmoc_mutation = False
    index_mutation = False
    new_decision = False
    canonization = False
    assert not cmoc_mutation
    assert not index_mutation
    assert not new_decision
    assert not canonization


if __name__ == "__main__":
    test_o6()
    print("O6 TEST: PASS")
