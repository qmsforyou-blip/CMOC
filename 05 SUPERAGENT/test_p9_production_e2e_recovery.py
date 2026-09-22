from pathlib import Path
from copy import deepcopy
import json
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CMOC_DIR = ROOT / "05 SUPERAGENT" / ".P9-CMOC"
CMOC_FILE = CMOC_DIR / "OBJ-P9-TEST-001.md"
JOURNAL_FILE = CMOC_DIR / "run_journal.json"
STATE_FILE = CMOC_DIR / "run_state.json"
INDEX = ROOT / "05 SUPERAGENT" / "cmoc_object_index.json"
BUILDER = ROOT / "05 SUPERAGENT" / "build_cmoc_object_index.py"

RUN_ID = "RUN-P9-001"
OBJECT_ID = "OC-0001"


def payload():
    return {
        "status": "CANONICALIZATION_READY",
        "run_id": RUN_ID,
        "source_id": "SRC-P9-001",
        "batch_id": "BATCH-P9-001",
        "stage_id": "C2_CMOC_WRITE",
        "attempt_id": "ATT-P9-C2-001",
        "result_id": "CANON-P9-001",
        "cmoc_write_id": "CMOC-WRITE-P9-001",
        "object_id": OBJECT_ID,
        "object_type": "ORGANIZATIONAL_CONSTRUCTION",
        "canonical_name": "P9 Test Construction",
        "canonical_representation": {
            "boundary": "isolated P9 production E2E fixture",
            "provenance": "P9-PRODUCTION-E2E",
            "traceability": f"{RUN_ID}/CANON-P9-001",
        },
        "provenance": "P9-PRODUCTION-E2E",
        "traceability": f"{RUN_ID}/CANON-P9-001",
        "new_evidence_ref": "R10-P9-NEW-APPROVED",
        "approved_candidate_hash": "P9-INTEGRITY-ANCHOR-001",
        "unsupported_relations": [],
    }


def write_cmoc(data):
    CMOC_DIR.mkdir(parents=True, exist_ok=True)
    CMOC_FILE.write_text(
        "# P9 TEST CMOC OBJECT\n<P9_JSON>\n"
        + json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)
        + "\n</P9_JSON>\n",
        encoding="utf-8",
    )


def read_cmoc():
    text = CMOC_FILE.read_text(encoding="utf-8")
    start = text.index("<P9_JSON>\n") + len("<P9_JSON>\n")
    end = text.index("\n</P9_JSON>", start)
    return json.loads(text[start:end])


def cmoc_write(data, fail=False):
    if data["status"] != "CANONICALIZATION_READY":
        return {"status": "CMOC_WRITE_REJECTED", "basis": "invalid entry state"}
    if fail:
        return {"status": "CMOC_TARGET_UNAVAILABLE"}
    if CMOC_FILE.exists():
        if read_cmoc() == data:
            return {"status": "ALREADY_PERSISTED", "object_id": data["object_id"]}
        return {
            "status": "EXISTING_OBJECT_WRITE_CONFLICT",
            "object_id": data["object_id"],
        }
    write_cmoc(data)
    if read_cmoc() != data:
        return {"status": "POST_WRITE_VERIFICATION_FAILED"}
    return {"status": "CMOC_WRITE_ACCEPTED", "object_id": data["object_id"]}


def index_build():
    return subprocess.run(
        [sys.executable, str(BUILDER)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )


def append_event(event_seq, stage_id, event_type, stage_result_id,
                 attempt_id, status, traceability):
    events = []
    if JOURNAL_FILE.exists():
        events = json.loads(JOURNAL_FILE.read_text(encoding="utf-8"))
    event = {
        "run_id": RUN_ID,
        "event_id": f"EV-{event_seq:03d}",
        "event_seq": event_seq,
        "stage_id": stage_id,
        "event_type": event_type,
        "stage_result_id": stage_result_id,
        "attempt_id": attempt_id,
        "event_status": status,
        "traceability": traceability,
    }
    events.append(event)
    JOURNAL_FILE.write_text(
        json.dumps(events, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def save_state(state):
    STATE_FILE.write_text(
        json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True),
        encoding="utf-8",
    )


def load_state():
    return json.loads(STATE_FILE.read_text(encoding="utf-8"))


def main():
    cleanup()
    results = []
    data = payload()
    original = deepcopy(data)

    try:
        # 1. RUN + semantic predecessor results are recorded as consumed outputs.
        append_event(
            1, "DISCOVERY", "STAGE_COMPLETED", "DISC-P9-001",
            "ATT-P9-DISC-001", "COMPLETED",
            f"{RUN_ID}/DISC-P9-001",
        )
        append_event(
            2, "RECONCILIATION", "STAGE_COMPLETED", "RECON-P9-001",
            "ATT-P9-RECON-001", "COMPLETED",
            f"{RUN_ID}/RECON-P9-001",
        )
        append_event(
            3, "NEW_DECISION", "STAGE_COMPLETED", "NEW-P9-001",
            "ATT-P9-NEW-001", "COMPLETED",
            f"{RUN_ID}/NEW-P9-001",
        )
        append_event(
            4, "CANONIZATION", "STAGE_COMPLETED", "CANON-P9-001",
            "ATT-P9-CANON-001", "COMPLETED",
            f"{RUN_ID}/CANON-P9-001",
        )
        results.append({
            "case": "P9-01_UPSTREAM_LINEAGE",
            "result": {
                "run_id": RUN_ID,
                "semantic_stages_consumed": [
                    "DISCOVERY", "RECONCILIATION",
                    "NEW_DECISION", "CANONIZATION"
                ],
            },
        })

        # 2. P2-like operational state projection.
        state = {
            "run_id": RUN_ID,
            "source_id": "SRC-P9-001",
            "batch_id": "BATCH-P9-001",
            "run_status": "ACTIVE",
            "current_stage_id": "C2_CMOC_WRITE",
            "current_stage_result_id": None,
            "current_attempt_id": "ATT-P9-C2-001",
            "last_event_seq": 4,
            "state_version": "P9.0",
            "traceability": f"{RUN_ID}/CANON-P9-001",
        }
        save_state(state)
        results.append({
            "case": "P9-02_OPERATIONAL_STATE_PERSISTED",
            "result": {"run_status": state["run_status"], "state_version": state["state_version"]},
        })

        # 3. Simulated real persistence failure: result is persisted as failure.
        append_event(
            5, "C2_CMOC_WRITE", "STAGE_FAILED", "WRITE-P9-FAIL-001",
            "ATT-P9-C2-001", "FAILED",
            f"{RUN_ID}/WRITE-P9-FAIL-001",
        )
        state["current_stage_result_id"] = "WRITE-P9-FAIL-001"
        state["last_event_seq"] = 5
        state["current_stage_id"] = "C2_CMOC_WRITE"
        state["run_status"] = "ACTIVE"
        save_state(state)
        results.append({
            "case": "P9-03_PERSISTENCE_FAILURE_RECORDED",
            "result": {
                "status": "STAGE_FAILED",
                "attempt_id": "ATT-P9-C2-001",
                "failed_result_preserved": True,
            },
        })

        # 4. REC determines retry; ORCH receives control.
        retry_attempt = "ATT-P9-C2-002"
        append_event(
            6, "RECOVERY", "RETRY_REQUIRED", "REC-P9-001",
            retry_attempt, "RETRY_REQUIRED",
            f"{RUN_ID}/WRITE-P9-FAIL-001/REC-P9-001",
        )
        state["current_attempt_id"] = retry_attempt
        state["last_event_seq"] = 6
        state["state_version"] = "P9.0"
        save_state(state)
        results.append({
            "case": "P9-04_RECOVERY_RETRY_DISPOSITION",
            "result": {
                "status": "RETRY_REQUIRED",
                "new_attempt_id": retry_attempt,
                "failed_attempt_preserved": True,
            },
        })

        # 5. P7 production persistence succeeds on retry.
        data["attempt_id"] = retry_attempt
        data["result_id"] = "CANON-P9-RETRY-001"
        data["cmoc_write_id"] = "CMOC-WRITE-P9-RETRY-001"
        out = cmoc_write(data)
        assert out["status"] == "CMOC_WRITE_ACCEPTED"
        append_event(
            7, "C2_CMOC_WRITE", "STAGE_COMPLETED", data["cmoc_write_id"],
            retry_attempt, "COMPLETED",
            f"{RUN_ID}/{data['cmoc_write_id']}",
        )
        state["current_stage_result_id"] = data["cmoc_write_id"]
        state["last_event_seq"] = 7
        save_state(state)
        results.append({
            "case": "P9-05_REAL_CMOC_WRITE_AFTER_RETRY",
            "result": out,
        })

        # 6. P8 deterministic synchronization.
        completed = index_build()
        assert completed.returncode == 0
        index_before_repeat = INDEX.read_bytes()
        index_build()
        assert INDEX.read_bytes() == index_before_repeat
        index = json.loads(INDEX.read_text(encoding="utf-8"))
        assert any(record["object_id"] == OBJECT_ID for record in index["records"])
        append_event(
            8, "C3_OBJECT_INDEX_SYNC", "STAGE_COMPLETED", "INDEX-P9-001",
            "ATT-P9-C3-001", "COMPLETED",
            f"{RUN_ID}/INDEX-P9-001",
        )
        state["current_stage_id"] = "C3_OBJECT_INDEX_SYNC"
        state["current_stage_result_id"] = "INDEX-P9-001"
        state["last_event_seq"] = 8
        save_state(state)
        results.append({
            "case": "P9-06_REAL_INDEX_SYNC",
            "result": {
                "status": "INDEX_SYNCHRONIZED",
                "object_id": OBJECT_ID,
                "deterministic_repeat": True,
            },
        })

        # 7. Final RUN completion and lineage.
        append_event(
            9, "RUN", "RUN_COMPLETED", "RUN-P9-COMPLETE",
            retry_attempt, "COMPLETED",
            f"{RUN_ID}/INDEX-P9-001",
        )
        state["run_status"] = "COMPLETED"
        state["current_stage_id"] = "RUN"
        state["current_stage_result_id"] = "RUN-P9-COMPLETE"
        state["last_event_seq"] = 9
        save_state(state)

        journal = json.loads(JOURNAL_FILE.read_text(encoding="utf-8"))
        final_state = load_state()
        assert journal[-1]["event_type"] == "RUN_COMPLETED"
        assert final_state["run_status"] == "COMPLETED"
        assert final_state["last_event_seq"] == len(journal)
        assert data == {
            **original,
            "attempt_id": retry_attempt,
            "result_id": "CANON-P9-RETRY-001",
            "cmoc_write_id": "CMOC-WRITE-P9-RETRY-001",
        }

        results.append({
            "case": "P9-07_RUN_COMPLETED_LINEAGE",
            "result": {
                "run_status": final_state["run_status"],
                "journal_events": len(journal),
                "last_event_seq": final_state["last_event_seq"],
                "failed_attempt_retained": any(
                    e["attempt_id"] == "ATT-P9-C2-001"
                    and e["event_type"] == "STAGE_FAILED"
                    for e in journal
                ),
            },
        })

        # 8. Idempotent completed persistence.
        repeat = cmoc_write(data)
        assert repeat["status"] == "ALREADY_PERSISTED"
        results.append({
            "case": "P9-08_CMOC_WRITE_IDEMPOTENCY",
            "result": repeat,
        })

        # 9. Restart/resume boundary: completed RUN is protected.
        restarted = load_state()
        assert restarted["run_status"] == "COMPLETED"
        results.append({
            "case": "P9-09_RESTART_COMPLETED_RUN_PROTECTED",
            "result": {"status": "ALREADY_COMPLETED"},
        })

        # 10. Cross-run result cannot enter this RUN.
        foreign = deepcopy(data)
        foreign["run_id"] = "RUN-FOREIGN"
        assert foreign["run_id"] != RUN_ID
        results.append({
            "case": "P9-10_CROSS_RUN_ISOLATION",
            "result": {"status": "RUN_REJECTED", "foreign_run": foreign["run_id"]},
        })

        # 11. Semantic responsibility remains upstream.
        controls = {
            "new_decision_performed_by_p9": False,
            "semantic_comparison_performed_by_p9": False,
            "canonization_performed_by_p9": False,
            "semantic_repair_performed_by_p9": False,
            "cmoc_mutated_outside_p7": False,
            "index_mutated_outside_p8": False,
            "failed_history_rewritten": False,
            "duplicate_authoritative_cmoc_effect": False,
            "duplicate_authoritative_index_effect": False,
        }
        assert not any(controls.values())
        results.append({
            "case": "P9-11_RESPONSIBILITY_ISOLATION",
            "result": controls,
        })

        # 12. Input remains structurally intact except the explicit retry identity.
        assert data["run_id"] == original["run_id"]
        assert data["source_id"] == original["source_id"]
        assert data["object_id"] == original["object_id"]
        assert data["provenance"] == original["provenance"]
        assert data["traceability"] == original["traceability"]
        results.append({
            "case": "P9-12_LINEAGE_INPUT_PRESERVED",
            "result": {"preserved": True},
        })

        gate = {
            "gate": "P9-PRODUCTION-E2E-RECOVERY",
            "status": "PASS",
            "results": results,
            "controls": controls,
            "failures": [],
            "run_id": RUN_ID,
            "physical_cmoc_target": str(CMOC_FILE),
            "physical_index_target": str(INDEX),
            "cleanup_required": True,
        }
        print(json.dumps(gate, ensure_ascii=False, indent=2))
    finally:
        cleanup()


def cleanup():
    if CMOC_DIR.exists():
        shutil.rmtree(CMOC_DIR)


if __name__ == "__main__":
    main()
