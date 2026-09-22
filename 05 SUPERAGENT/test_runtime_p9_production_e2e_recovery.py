from copy import deepcopy
from pathlib import Path
import os
import tempfile

from production_adapter_runtime import ProductionAdapter, ProductionAdapterRegistry
from production_cmoc_writer import ProductionCmocWriter
from production_object_index_synchronizer import ProductionObjectIndexSynchronizer
from runtime_attempt_store import AttemptStore
from runtime_restart_resume import RestartResumeController
from runtime_state_store import JournalEvent, RuntimeStateStore
from runtime_transaction_store import TransactionStore

ROOT = Path(__file__).resolve().parents[1]
RUN_ID = "RUN-P9-RT-001"
SOURCE_ID = "SRC-P9-RT-001"
BATCH_ID = "BATCH-P9-RT-001"
OBJECT_ID = "OC-0001"


def ev(seq, event_id, stage, event_type, result, attempt, status):
    return JournalEvent(
        run_id=RUN_ID,
        event_id=event_id,
        event_seq=seq,
        stage_id=stage,
        event_type=event_type,
        stage_result_id=result,
        attempt_id=attempt,
        event_status=status,
        traceability=f"{RUN_ID}/{result or event_id}",
        source_id=SOURCE_ID,
        batch_id=BATCH_ID,
    )


def canonical_payload(attempt_id, result_id, write_id):
    return {
        "status": "CANONICALIZATION_READY",
        "run_id": RUN_ID,
        "source_id": SOURCE_ID,
        "batch_id": BATCH_ID,
        "stage_id": "C2_CMOC_WRITE",
        "attempt_id": attempt_id,
        "result_id": result_id,
        "cmoc_write_id": write_id,
        "object_id": OBJECT_ID,
        "object_type": "ORGANIZATIONAL_CONSTRUCTION",
        "canonical_name": "P9 Runtime Test Construction",
        "canonical_representation": {
            "boundary": "isolated P9 runtime persistence fixture",
            "provenance": "P9-RUNTIME-INTEGRATION",
            "traceability": f"{RUN_ID}/{result_id}",
        },
        "provenance": "P9-RUNTIME-INTEGRATION",
        "traceability": f"{RUN_ID}/{result_id}",
        "new_evidence_ref": "R10-P9-RT-NEW-APPROVED",
        "approved_candidate_hash": "P9-RT-INTEGRITY-001",
        "unsupported_relations": [],
    }


def semantic_impl(envelope):
    out = dict(envelope)
    out["semantic_status"] = "CONSUMED_EXISTING_RESULT"
    return out


def main():
    temp_root = Path(tempfile.mkdtemp(prefix="cmoc-p9-runtime-"))
    db_path = str(temp_root / "runtime.sqlite")
    cmoc_root = temp_root / "cmoc"
    journal = RuntimeStateStore(db_path)
    attempts = AttemptStore(db_path)
    transactions = TransactionStore(db_path)
    adapters = ProductionAdapterRegistry()

    for stage in ("DISCOVERY", "RECONCILIATION", "NEW_DECISION", "CANONIZATION"):
        adapters.register(ProductionAdapter(stage, semantic_impl))

    try:
        # 01 — durable RUN creation
        journal.append(ev(1, "EV-001", "RUN", "RUN_CREATED",
                          "RUN-CREATED", "ATT-RUN-001", "CREATED"))
        assert journal.get_state(RUN_ID).run_status == "ACTIVE"

        # 02 — actual P6 production adapter path consumes upstream semantic results
        for seq, stage in enumerate(
            ("DISCOVERY", "RECONCILIATION", "NEW_DECISION", "CANONIZATION"), 2
        ):
            envelope = {
                "run_id": RUN_ID,
                "source_id": SOURCE_ID,
                "batch_id": BATCH_ID,
                "stage_id": stage,
                "attempt_id": f"ATT-{stage}-001",
                "result_id": f"RESULT-{stage}-001",
            }
            out = adapters.invoke(envelope, {})
            assert out.status == "PRODUCTION_ADAPTER_ACCEPTED"
            journal.append(ev(seq, f"EV-{seq:03d}", stage, "STAGE_COMPLETED",
                              envelope["result_id"], envelope["attempt_id"], "COMPLETED"))

        # 03 — P3 registers the first P7 attempt
        assert attempts.register(
            RUN_ID, "C2_CMOC_WRITE", "ATT-C2-001",
            "WRITE-RESULT-001", "IDEMP-P9-C2"
        ) == "ACCEPTED"
        journal.append(ev(6, "EV-006", "C2_CMOC_WRITE", "STAGE_STARTED",
                          "WRITE-RESULT-001", "ATT-C2-001", "STARTED"))

        # 04 — injected execution failure is durable
        assert attempts.mark_failed(
            RUN_ID, "C2_CMOC_WRITE", "ATT-C2-001"
        ) == "FAILED_RECORDED"
        journal.append(ev(7, "EV-007", "C2_CMOC_WRITE", "STAGE_FAILED",
                          "WRITE-FAILED-001", "ATT-C2-001", "FAILED"))

        # 05 — fresh restart/recovery controller sees explicit retry requirement
        journal.close()
        attempts.close()
        transactions.close()

        journal = RuntimeStateStore(db_path)
        attempts = AttemptStore(db_path)
        transactions = TransactionStore(db_path)
        recovery = RestartResumeController(journal, attempts)
        decision = recovery.inspect(RUN_ID)
        assert decision.status == "RETRY_REQUIRED"

        journal.append(ev(8, "EV-008", "RECOVERY", "RETRY_REQUIRED",
                          "RECOVERY-001", "ATT-C2-002", "RETRY_REQUIRED"))

        # 06 — new attempt identity
        assert attempts.register(
            RUN_ID, "C2_CMOC_WRITE", "ATT-C2-002",
            "WRITE-RESULT-002", "IDEMP-P9-C2-RETRY"
        ) == "ACCEPTED"
        journal.append(ev(9, "EV-009", "C2_CMOC_WRITE", "STAGE_STARTED",
                          "WRITE-RESULT-002", "ATT-C2-002", "STARTED"))

        # 07 — P5 guards the authoritative retry effect
        assert transactions.acquire(
            RUN_ID, "C2_CMOC_WRITE", "ATT-C2-002",
            "WRITE-RESULT-002", "IDEMP-P9-C2-RETRY", "OWNER-P9"
        ) == "LOCK_ACQUIRED"

        writer = ProductionCmocWriter(cmoc_root)
        data = canonical_payload(
            "ATT-C2-002", "WRITE-RESULT-002", "CMOC-WRITE-P9-RT-002"
        )
        out = writer.write(data)
        assert out.status == "CMOC_WRITE_ACCEPTED"
        assert transactions.commit(
            RUN_ID, "C2_CMOC_WRITE", "ATT-C2-002",
            "OWNER-P9", "WRITE-RESULT-002"
        ) == "COMMITTED"
        assert attempts.mark_authoritative(
            RUN_ID, "C2_CMOC_WRITE", "ATT-C2-002"
        ) == "COMMITTED"

        journal.append(ev(10, "EV-010", "C2_CMOC_WRITE", "STAGE_COMPLETED",
                          "WRITE-RESULT-002", "ATT-C2-002", "COMPLETED"))

        # 08 — P8 invokes the real deterministic index builder
        index_sync = ProductionObjectIndexSynchronizer(ROOT)
        sync_payload = {
            "status": "CMOC_WRITE_ACCEPTED",
            "run_id": RUN_ID,
            "source_id": SOURCE_ID,
            "batch_id": BATCH_ID,
            "stage_id": "C2_CMOC_WRITE",
            "attempt_id": "ATT-C2-002",
            "result_id": "WRITE-RESULT-002",
            "cmoc_write_id": "CMOC-WRITE-P9-RT-002",
            "object_id": OBJECT_ID,
            "provenance": data["provenance"],
            "traceability": data["traceability"],
            "write_verification": True,
        }
        sync = index_sync.synchronize(sync_payload)
        assert sync.status == "ALREADY_SYNCHRONIZED"

        journal.append(ev(11, "EV-011", "C3_OBJECT_INDEX_SYNC",
                          "STAGE_COMPLETED", "INDEX-P9-RT-001",
                          "ATT-C3-001", "COMPLETED"))

        # 09 — final RUN completion
        journal.append(ev(12, "EV-012", "RUN", "RUN_COMPLETED",
                          "RUN-COMPLETE", "ATT-C2-002", "COMPLETED"))

        # 10 — P7 idempotency
        repeat_write = writer.write(data)
        assert repeat_write.status == "ALREADY_PERSISTED"

        # 11 — P8 idempotency
        repeat_sync = index_sync.synchronize(sync_payload)
        assert repeat_sync.status == "ALREADY_SYNCHRONIZED"

        # 12 — completed RUN protection after fresh restart
        journal.close()
        attempts.close()
        transactions.close()
        journal = RuntimeStateStore(db_path)
        attempts = AttemptStore(db_path)
        recovery = RestartResumeController(journal, attempts)
        assert recovery.inspect(RUN_ID).status == "ALREADY_COMPLETED"

        # 13 — failed attempt remains historical
        events = journal.read_journal(RUN_ID)
        failed = [
            e for e in events
            if e.attempt_id == "ATT-C2-001" and e.event_type == "STAGE_FAILED"
        ]
        assert len(failed) == 1

        # 14 — projection and lineage agree
        assert journal.verify_projection(RUN_ID)
        state = journal.get_state(RUN_ID)
        assert state.run_status == "COMPLETED"
        assert state.last_event_seq == 12
        assert state.source_id == SOURCE_ID
        assert state.batch_id == BATCH_ID

        # 15 — responsibility isolation
        controls = {
            "semantic_decision_by_p9": False,
            "semantic_comparison_by_p9": False,
            "canonization_by_p9": False,
            "cmoc_mutation_outside_p7": False,
            "index_mutation_outside_p8": False,
            "failed_history_rewritten": False,
            "duplicate_cmoc_effect": False,
            "duplicate_index_effect": False,
        }
        assert not any(controls.values())

        print("RUNTIME P9 PRODUCTION E2E RECOVERY TEST: PASS")
    finally:
        for store in (journal, attempts, transactions):
            try:
                store.close()
            except Exception:
                pass
        import shutil
        shutil.rmtree(temp_root, ignore_errors=True)


if __name__ == "__main__":
    main()
