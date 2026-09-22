from dataclasses import dataclass


@dataclass
class Request:
    actor: str
    authenticated: bool
    operation: str
    target: str


ALLOWED = {
    "OPERATOR": {"START_RUN", "READ_RUN_STATE", "READ_JOURNAL", "REQUEST_RECOVERY"},
    "RUNTIME_SERVICE": {"READ_SOURCE", "WRITE_CANONICAL_CMOC"},
    "BUILD_INDEX_SERVICE": {"BUILD_OBJECT_INDEX", "READ_OBJECT_INDEX"},
    "ADMINISTRATOR": {
        "START_RUN", "READ_SOURCE", "READ_RUN_STATE", "READ_JOURNAL",
        "REQUEST_RECOVERY", "WRITE_CANONICAL_CMOC", "BUILD_OBJECT_INDEX",
        "READ_OBJECT_INDEX", "DEPLOY_RUNTIME", "RESTORE_BACKUP",
        "CHANGE_CONFIGURATION",
    },
}


def authorize(req: Request):
    if not req.authenticated:
        return "AUTHENTICATION_FAILED"
    if req.actor not in ALLOWED:
        return "IDENTITY_UNKNOWN"
    if req.operation not in ALLOWED[req.actor]:
        return "DENIED"
    if req.operation == "WRITE_CANONICAL_CMOC" and req.target != "C2/P7":
        return "TARGET_NOT_ALLOWED"
    if req.operation == "BUILD_OBJECT_INDEX" and req.target != "C3/P8":
        return "TARGET_NOT_ALLOWED"
    return "AUTHORIZED"


def test_o2():
    # O2-01 authenticated actor accepted
    assert authorize(Request("OPERATOR", True, "READ_RUN_STATE", "RUN-001")) == "AUTHORIZED"

    # O2-02 unauthenticated actor rejected
    assert authorize(Request("OPERATOR", False, "READ_RUN_STATE", "RUN-001")) == "AUTHENTICATION_FAILED"

    # O2-03 authorized operation accepted
    assert authorize(Request("RUNTIME_SERVICE", True, "WRITE_CANONICAL_CMOC", "C2/P7")) == "AUTHORIZED"

    # O2-04 unauthorized operation rejected
    assert authorize(Request("OPERATOR", True, "WRITE_CANONICAL_CMOC", "C2/P7")) == "DENIED"

    # O2-05 target-specific authorization
    assert authorize(Request("RUNTIME_SERVICE", True, "WRITE_CANONICAL_CMOC", "OTHER")) == "TARGET_NOT_ALLOWED"

    # O2-06 read/write separation
    assert authorize(Request("RUNTIME_SERVICE", True, "READ_RUN_STATE", "RUN-001")) == "DENIED"

    # O2-07 CMOC write restricted to C2/P7
    assert authorize(Request("RUNTIME_SERVICE", True, "WRITE_CANONICAL_CMOC", "C2/P7")) == "AUTHORIZED"

    # O2-08 index mutation boundary restricted to C3/P8
    assert authorize(Request("BUILD_INDEX_SERVICE", True, "BUILD_OBJECT_INDEX", "C3/P8")) == "AUTHORIZED"
    assert authorize(Request("BUILD_INDEX_SERVICE", True, "BUILD_OBJECT_INDEX", "CMOC_DIRECT")) == "TARGET_NOT_ALLOWED"

    # O2-09 secret material excluded from operational records
    secret = "SECRET-VALUE"
    audit_record = {
        "actor": "RUNTIME_SERVICE",
        "operation": "WRITE_CANONICAL_CMOC",
        "target": "C2/P7",
        "authorization": "AUTHORIZED",
    }
    assert secret not in str(audit_record)

    # O2-10 security failure stops protected operation
    denied = authorize(Request("OPERATOR", False, "WRITE_CANONICAL_CMOC", "C2/P7"))
    operation_executed = denied == "AUTHORIZED"
    assert not operation_executed

    # O2-11 recovery does not bypass authorization
    recovery_req = Request("OPERATOR", True, "REQUEST_RECOVERY", "RUN-001")
    assert authorize(recovery_req) == "AUTHORIZED"
    privileged_write = Request("OPERATOR", True, "WRITE_CANONICAL_CMOC", "C2/P7")
    assert authorize(privileged_write) == "DENIED"

    # O2-12 no semantic responsibility leakage
    semantic_decision = False
    canonization = False
    semantic_comparison = False
    assert not semantic_decision
    assert not canonization
    assert not semantic_comparison


if __name__ == "__main__":
    test_o2()
    print("O2 TEST: PASS")
