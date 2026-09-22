import os
import tempfile
import threading

from runtime_transaction_store import TransactionStore


def test_transaction_concurrency():
    fd, path = tempfile.mkstemp(prefix="cmoc-p5-", suffix=".sqlite")
    os.close(fd)
    stores = []

    try:
        store = TransactionStore(path)
        stores.append(store)

        base = {
            "run_id": "RUN-P5-RT-001",
            "stage_id": "CMOC_WRITE",
            "attempt_id": "ATT-001",
            "result_id": "RES-001",
            "idempotency_key": "KEY-001",
        }

        # P5-RT-01: first caller acquires.
        assert store.acquire(**base, owner_id="OWNER-A") == "LOCK_ACQUIRED"

        # P5-RT-02: second caller is blocked by the existing owner.
        assert store.acquire(**base, owner_id="OWNER-B") == "IN_PROGRESS"

        # P5-RT-03: commit creates exactly one authoritative effect.
        assert store.commit(**base, owner_id="OWNER-A") == "COMMITTED"
        record = store.get(base["run_id"], base["stage_id"], base["attempt_id"])
        assert record.committed is True
        assert record.effect_count == 1

        # P5-RT-04: completed attempt cannot execute again.
        assert store.acquire(**base, owner_id="OWNER-B") == "ALREADY_COMPLETED"
        assert store.get(base["run_id"], base["stage_id"], base["attempt_id"]).effect_count == 1

        # P5-RT-05: a different attempt is distinct.
        retry = dict(base, attempt_id="ATT-002", result_id="RES-002",
                     idempotency_key="KEY-002")
        assert store.acquire(**retry, owner_id="OWNER-B") == "LOCK_ACQUIRED"

        # P5-RT-06: same idempotency key cannot create another attempt.
        key_conflict = dict(base, attempt_id="ATT-003", result_id="RES-003")
        assert store.acquire(**key_conflict, owner_id="OWNER-C") == "IDEMPOTENCY_CONFLICT"

        # P5-RT-07: conflicting result for an active attempt is rejected.
        conflict = dict(retry, result_id="RES-999")
        assert store.acquire(**conflict, owner_id="OWNER-B") == "CONFLICTING_RESULT"

        # P5-RT-08: rollback does not create authoritative success.
        rollback_attempt = dict(base, attempt_id="ATT-004", result_id="RES-004",
                                idempotency_key="KEY-004")
        assert store.acquire(**rollback_attempt, owner_id="OWNER-D") == "LOCK_ACQUIRED"
        assert store.rollback(**rollback_attempt, owner_id="OWNER-D") == "TRANSACTION_ROLLBACK"
        rolled = store.get(rollback_attempt["run_id"], rollback_attempt["stage_id"],
                           rollback_attempt["attempt_id"])
        assert rolled.committed is False
        assert rolled.effect_count == 0

        # P5-RT-09: restart/reopen preserves authoritative result.
        store.close()
        stores.pop()
        store = TransactionStore(path)
        stores.append(store)
        assert store.get(base["run_id"], base["stage_id"], base["attempt_id"]).committed
        assert store.get(base["run_id"], base["stage_id"], base["attempt_id"]).effect_count == 1

        # P5-RT-10: concurrent callers for a fresh attempt cannot both acquire.
        concurrent = dict(base, attempt_id="ATT-005", result_id="RES-005",
                          idempotency_key="KEY-005")
        outcomes = []
        barrier = threading.Barrier(2)

        def worker(owner):
            local = TransactionStore(path)
            stores.append(local)
            try:
                barrier.wait()
                outcomes.append(local.acquire(**concurrent, owner_id=owner))
            finally:
                local.close()

        threads = [
            threading.Thread(target=worker, args=("OWNER-E",)),
            threading.Thread(target=worker, args=("OWNER-F",)),
        ]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        assert sorted(outcomes) == ["IN_PROGRESS", "LOCK_ACQUIRED"]

        # P5-RT-11: cross-run isolation.
        foreign = dict(base, run_id="RUN-P5-RT-FOREIGN",
                       attempt_id="ATT-001", result_id="RES-F",
                       idempotency_key="KEY-F")
        assert store.acquire(**foreign, owner_id="OWNER-X") == "LOCK_ACQUIRED"

        # P5-RT-12: no semantic responsibility leaks into P5.
        assert not hasattr(store, "semantic_decision")
        assert not hasattr(store, "semantic_comparison")
        assert not hasattr(store, "canonization")
        assert not hasattr(store, "cmoc_write")
        assert not hasattr(store, "object_index_write")

        print("RUNTIME TRANSACTION CONCURRENCY TEST: PASS")
    finally:
        for item in stores:
            try:
                item.close()
            except Exception:
                pass
        try:
            os.remove(path)
        except FileNotFoundError:
            pass


if __name__ == "__main__":
    test_transaction_concurrency()
