import os
import tempfile

from runtime_attempt_store import AttemptStore


def test_attempt_store():
    fd, path = tempfile.mkstemp(prefix="cmoc-attempt-", suffix=".sqlite")
    os.close(fd)

    try:
        store = AttemptStore(path)

        # P3-RT-01: first attempt accepted
        assert store.register(
            "RUN-P3-001", "CMOC_WRITE", "ATT-001", "RES-001", "KEY-001"
        ) == "ACCEPTED"

        # P3-RT-02: same attempt is in progress, no duplicate authoritative effect
        assert store.register(
            "RUN-P3-001", "CMOC_WRITE", "ATT-001", "RES-001", "KEY-001"
        ) == "IN_PROGRESS"

        # P3-RT-03: authoritative result protects completed attempt
        assert store.mark_authoritative(
            "RUN-P3-001", "CMOC_WRITE", "ATT-001"
        ) == "COMMITTED"
        assert store.register(
            "RUN-P3-001", "CMOC_WRITE", "ATT-001", "RES-001", "KEY-001"
        ) == "ALREADY_COMPLETED"

        # P3-RT-04: same attempt cannot replace its authoritative result
        assert store.register(
            "RUN-P3-001", "CMOC_WRITE", "ATT-001", "RES-CHANGED", "KEY-001"
        ) == "CONFLICTING_ATTEMPT"

        # P3-RT-05: retry is a new attempt and new result
        assert store.register(
            "RUN-P3-001", "CMOC_WRITE", "ATT-002", "RES-002", "KEY-002"
        ) == "ACCEPTED"

        # P3-RT-06: failed attempt remains represented; repeat does not create another
        assert store.register(
            "RUN-P3-001", "RECONCILIATION", "ATT-003", "RES-003", "KEY-003",
            status="FAILED"
        ) == "ACCEPTED"
        assert store.register(
            "RUN-P3-001", "RECONCILIATION", "ATT-003", "RES-003", "KEY-003",
            status="FAILED"
        ) == "DUPLICATE_ATTEMPT"

        # P3-RT-07: lost acknowledgement scenario
        assert store.register(
            "RUN-P3-001", "CMOC_WRITE", "ATT-004", "RES-004", "KEY-004"
        ) == "ACCEPTED"
        assert store.mark_authoritative(
            "RUN-P3-001", "CMOC_WRITE", "ATT-004"
        ) == "COMMITTED"
        assert store.register(
            "RUN-P3-001", "CMOC_WRITE", "ATT-004", "RES-004", "KEY-004"
        ) == "ALREADY_COMPLETED"

        # P3-RT-08: idempotency is isolated by RUN_ID
        assert store.register(
            "RUN-P3-002", "CMOC_WRITE", "ATT-001", "RES-101", "KEY-001"
        ) == "ACCEPTED"

        # P3-RT-09: same key cannot silently bind to another attempt in one run/stage
        assert store.register(
            "RUN-P3-001", "CMOC_WRITE", "ATT-005", "RES-005", "KEY-001"
        ) == "IDEMPOTENCY_KEY_CONFLICT"

        # P3-RT-10: same attempt with another idempotency key is rejected
        assert store.register(
            "RUN-P3-001", "CMOC_WRITE", "ATT-002", "RES-002", "KEY-CHANGED"
        ) == "IDEMPOTENCY_KEY_MISMATCH"

        # P3-RT-11: authoritative record is persisted
        record = store.get("RUN-P3-001", "CMOC_WRITE", "ATT-001")
        assert record is not None
        assert record.authoritative_result is True
        assert record.result_id == "RES-001"

        # P3-RT-12: cross-run history remains distinct after reopen
        store.close()
        store = AttemptStore(path)
        run1 = store.list_run("RUN-P3-001")
        run2 = store.list_run("RUN-P3-002")
        assert any(r.attempt_id == "ATT-001" and r.result_id == "RES-001" for r in run1)
        assert any(r.attempt_id == "ATT-001" and r.result_id == "RES-101" for r in run2)

        # Responsibility boundary: no semantic/canonization/CMOC/index methods.
        assert not hasattr(store, "semantic_decision")
        assert not hasattr(store, "canonization")
        assert not hasattr(store, "cmoc_write")
        assert not hasattr(store, "object_index_write")

        store.close()
        print("RUNTIME ATTEMPT STORE TEST: PASS")

    finally:
        try:
            os.remove(path)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    test_attempt_store()
