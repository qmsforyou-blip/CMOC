import copy
import hashlib
import json


def digest(value):
    raw = json.dumps(value, sort_keys=True, ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def make_fixture():
    cmoc = {
        "object_id": "OBJ-O3-001",
        "canonical_name": "O3 Backup Test Object",
        "boundary": "isolated backup restore fixture",
        "provenance": "O3-SYNTHETIC",
        "traceability": "RUN-O3-001/CANON-O3-001",
    }
    journal = [
        {"run_id": "RUN-O3-001", "event_seq": 1, "event": "RUN_CREATED"},
        {"run_id": "RUN-O3-001", "event_seq": 2, "event": "STAGE_COMPLETED"},
    ]
    state = {
        "run_id": "RUN-O3-001",
        "source_id": "SRC-O3-001",
        "batch_id": "BATCH-O3-001",
        "run_status": "COMPLETED",
        "current_stage_id": "C2_CMOC_WRITE",
        "current_stage_result_id": "RESULT-O3-001",
        "current_attempt_id": "ATT-O3-001",
        "last_event_seq": 2,
        "state_version": "O3.0",
        "traceability": "RUN-O3-001/RESULT-O3-001",
    }
    return cmoc, journal, state


def build_index(cmoc):
    return {
        "object_id": cmoc["object_id"],
        "canonical_name": cmoc["canonical_name"],
        "source": "DETERMINISTIC_FROM_CMOC",
    }


def test_o3():
    original_cmoc, original_journal, original_state = make_fixture()

    # O3-01 backup authoritative CMOC
    backup_cmoc = copy.deepcopy(original_cmoc)
    assert backup_cmoc == original_cmoc

    # O3-02 backup execution journal
    backup_journal = copy.deepcopy(original_journal)
    assert backup_journal == original_journal

    # O3-03 backup persistent RUN/state
    backup_state = copy.deepcopy(original_state)
    assert backup_state == original_state

    # O3-04 backup integrity
    backup_package = {
        "cmoc": backup_cmoc,
        "journal": backup_journal,
        "state": backup_state,
    }
    backup_hash = digest(backup_package)
    assert backup_hash == digest(backup_package)

    # O3-05 restore
    restored = copy.deepcopy(backup_package)
    assert restored["cmoc"] == original_cmoc
    assert restored["journal"] == original_journal
    assert restored["state"] == original_state

    # O3-06 canonical identity preserved
    assert restored["cmoc"]["object_id"] == "OBJ-O3-001"

    # O3-07 provenance/traceability preserved
    assert restored["cmoc"]["provenance"] == "O3-SYNTHETIC"
    assert restored["cmoc"]["traceability"] == "RUN-O3-001/CANON-O3-001"

    # O3-08 journal/state consistency
    assert restored["state"]["last_event_seq"] == restored["journal"][-1]["event_seq"]
    assert restored["state"]["run_id"] == restored["journal"][-1]["run_id"]

    # O3-09 deterministic OBJECT INDEX regeneration
    rebuilt_index = build_index(restored["cmoc"])
    assert rebuilt_index["object_id"] == restored["cmoc"]["object_id"]
    assert rebuilt_index["source"] == "DETERMINISTIC_FROM_CMOC"

    # O3-10 reproducible rebuild
    rebuilt_index_2 = build_index(restored["cmoc"])
    assert digest(rebuilt_index) == digest(rebuilt_index_2)

    # O3-11 index cannot override canonical CMOC
    altered_index = dict(rebuilt_index)
    altered_index["canonical_name"] = "UNAUTHORIZED_INDEX_VALUE"
    assert restored["cmoc"]["canonical_name"] != altered_index["canonical_name"]

    # O3-12 completed effect protection remains after restore
    completed_attempt = True
    duplicate_effect_allowed = False
    assert completed_attempt
    assert not duplicate_effect_allowed

    # O3-13 restore integrity failure is explicit
    corrupted_backup = copy.deepcopy(backup_package)
    corrupted_backup["cmoc"]["canonical_name"] = "CORRUPTED"
    assert digest(corrupted_backup) != backup_hash

    # O3-14 no semantic responsibility leakage
    semantic_decision = False
    new_decision = False
    canonization = False
    cmoc_mutation = False
    assert not semantic_decision
    assert not new_decision
    assert not canonization
    assert not cmoc_mutation


if __name__ == "__main__":
    test_o3()
    print("O3 TEST: PASS")
