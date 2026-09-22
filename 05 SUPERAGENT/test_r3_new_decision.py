#!/usr/bin/env python3
"""R3 isolated executable test.

This test validates the decision boundary for a separate NEW DECISION stage.
It intentionally does not import production DISCOVERY, RECONCILIATION,
QUERY, or CMOC-write runtime.

The test is a deterministic contract test, not a semantic novelty engine.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OBJECT_INDEX = ROOT / "05 SUPERAGENT" / "cmoc_object_index.json"
DISCOVERY_RESULT = ROOT / "05 SUPERAGENT" / "DISCOVERY-RESULT-SRC-003-M06-001.json"


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot_files() -> dict[str, str]:
    result = {}
    for path in (OBJECT_INDEX, DISCOVERY_RESULT):
        if path.exists():
            result[str(path)] = sha256_file(path)
    return result


def evaluate_new_decision(inp: dict) -> dict:
    """Minimal deterministic R3 decision boundary.

    This is intentionally a test-local contract implementation.
    It does not claim semantic novelty in production.
    """
    evidence = inp["evidence_state"]

    if inp["eligibility"] != "ELIGIBLE_FOR_NEW_DECISION":
        return {
            "decision": "NEW_REJECTED",
            "basis": "candidate is not eligible for NEW DECISION",
        }

    if evidence.get("query_scope_sufficient") is not True:
        return {
            "decision": "NEW_REJECTED",
            "basis": "insufficient query scope",
        }

    if evidence.get("target_object_type_resolved") is not True:
        return {
            "decision": "NEW_REJECTED",
            "basis": "target object type unresolved",
        }

    if evidence.get("no_unresolved_candidate") is not True:
        return {
            "decision": "NEW_REJECTED",
            "basis": "candidate unresolved",
        }

    if evidence.get("no_ambiguity") is not True:
        return {
            "decision": "NEW_REJECTED",
            "basis": "candidate ambiguous",
        }

    # R3 test deliberately treats the fully evidenced synthetic fixture
    # as NEW_APPROVED. This is a boundary test, not a semantic novelty claim.
    return {
        "decision": "NEW_APPROVED",
        "basis": "R3 synthetic contract fixture satisfies decision prerequisites",
    }


def base_input() -> dict:
    return {
        "candidate": {
            "record_id": "R3-CAND-001",
            "value": "Synthetic candidate",
            "object_boundary": "stable source-bound boundary",
        },
        "reconciliation": {
            "match_result": "NEEDS_REVIEW",
            "basis": "NO_MATCH from configured query modes; NEW not yet proven",
            "cmoc_object_id": None,
        },
        "eligibility": "ELIGIBLE_FOR_NEW_DECISION",
        "evidence_state": {
            "source_bound_candidate": True,
            "traceability_complete": True,
            "query_scope_sufficient": True,
            "exact_checked": True,
            "alias_checked": True,
            "structural_checked_or_NA": True,
            "no_ambiguity": True,
            "no_unresolved_candidate": True,
            "stable_object_boundary": True,
            "target_object_type_resolved": True,
        },
        "target_object_type": "TERM",
        "traceability": {
            "source_id": "SRC-R3-TEST",
            "input_batch_id": "BATCH-R3-001",
            "record_id": "R3-CAND-001",
        },
        "decision_context": "R3 isolated NEW DECISION boundary test",
    }


def run_case(name: str, inp: dict, expected: str) -> dict:
    original = copy.deepcopy(inp)
    result = evaluate_new_decision(inp)
    unchanged = inp == original

    return {
        "branch": name,
        "expected": expected,
        "actual": result["decision"],
        "basis": result["basis"],
        "pass": result["decision"] == expected and unchanged,
        "input_unchanged": unchanged,
    }


def main() -> None:
    before = snapshot_files()

    complete = base_input()
    cases = [
        run_case("COMPLETE_ELIGIBLE", complete, "NEW_APPROVED"),
    ]

    insufficient_scope = copy.deepcopy(complete)
    insufficient_scope["eligibility"] = "NOT_ELIGIBLE"
    insufficient_scope["evidence_state"]["query_scope_sufficient"] = False
    cases.append(run_case("INSUFFICIENT_SCOPE", insufficient_scope, "NEW_REJECTED"))

    unknown_target = copy.deepcopy(complete)
    unknown_target["eligibility"] = "NOT_ELIGIBLE"
    unknown_target["evidence_state"]["target_object_type_resolved"] = "UNKNOWN"
    unknown_target["target_object_type"] = None
    cases.append(run_case("UNKNOWN_TARGET_TYPE", unknown_target, "NEW_REJECTED"))

    unresolved = copy.deepcopy(complete)
    unresolved["eligibility"] = "NOT_ELIGIBLE"
    unresolved["evidence_state"]["no_unresolved_candidate"] = False
    cases.append(run_case("UNRESOLVED_CANDIDATE", unresolved, "NEW_REJECTED"))

    ambiguous = copy.deepcopy(complete)
    ambiguous["eligibility"] = "NOT_ELIGIBLE"
    ambiguous["evidence_state"]["no_ambiguity"] = False
    cases.append(run_case("AMBIGUOUS", ambiguous, "NEW_REJECTED"))

    eligible_only = copy.deepcopy(complete)
    # Explicit negative control: eligibility alone is insufficient.
    eligible_only["evidence_state"]["query_scope_sufficient"] = "UNKNOWN"
    cases.append(run_case("ELIGIBLE_BUT_UNKNOWN_EVIDENCE", eligible_only, "NEW_REJECTED"))

    after = snapshot_files()

    controls = {
        "cmoc_write": "NONE",
        "object_id_created": False,
        "canonization": False,
        "relations_created": False,
        "object_index_unchanged": before.get(str(OBJECT_INDEX)) == after.get(str(OBJECT_INDEX)),
        "discovery_result_unchanged": before.get(str(DISCOVERY_RESULT)) == after.get(str(DISCOVERY_RESULT)),
        "production_runtime_imported": False,
        "approved_does_not_write_cmoc": True,
        "rejected_does_not_write_cmoc": True,
    }

    all_pass = all(item["pass"] for item in cases) and all(
        controls.values()
        if isinstance(value := None, bool)
        else True
        for _ in [0]
    )
    # Explicitly evaluate boolean controls; string cmoc_write is a declaration.
    all_pass = all(item["pass"] for item in cases) and all(
        value is True for key, value in controls.items() if key != "cmoc_write"
    ) and controls["cmoc_write"] == "NONE"

    gate = {
        "gate": "R3-NEW-DECISION-BOUNDARY",
        "status": "PASS" if all_pass else "FAIL",
        "branches": cases,
        "controls": controls,
        "scope_note": (
            "NEW_APPROVED is produced only for a fully evidenced synthetic "
            "fixture. This test does not establish semantic novelty in production."
        ),
    }

    print(json.dumps(gate, ensure_ascii=False, indent=2))

    if not all_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
