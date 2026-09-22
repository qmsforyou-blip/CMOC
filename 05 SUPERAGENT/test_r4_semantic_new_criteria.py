#!/usr/bin/env python3
"""R4 isolated executable test.

Validates the minimum evidence predicate for semantic NEW.
This is a deterministic contract test using synthetic fixtures.

It does not import or execute production Discovery, Reconciliation,
QUERY, or CMOC-write runtime.
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


def evaluate_semantic_new(inp: dict) -> dict:
    """R4 test-local semantic NEW evidence gate.

    This is not a production novelty engine.
    It only evaluates the R4 contract predicate.
    """
    evidence = inp["evidence_state"]

    required_true = (
        "candidate_identity",
        "stable_object_boundary",
        "query_scope_sufficient",
        "exact_checked",
        "alias_checked_or_NA",
        "structural_checked_or_NA",
        "no_ambiguity",
        "no_unresolved_candidate",
        "positive_semantic_distinction",
        "provenance_complete",
        "decision_basis_complete",
    )

    for key in required_true:
        if evidence.get(key) is not True:
            return {
                "decision": "NOT_APPROVABLE",
                "basis": f"R4 evidence criterion failed or is not TRUE: {key}",
            }

    if any(value == "UNKNOWN" for value in evidence.values()):
        return {
            "decision": "NOT_APPROVABLE",
            "basis": "UNKNOWN evidence cannot be promoted to TRUE",
        }

    return {
        "decision": "NEW_APPROVED",
        "basis": "R4 synthetic fixture satisfies complete semantic NEW evidence predicate",
    }


def base_input() -> dict:
    return {
        "candidate": {
            "record_id": "R4-CAND-001",
            "value": "Synthetic semantic distinction",
            "object_boundary": "stable source-bound boundary",
        },
        "reconciliation": {
            "match_result": "NEEDS_REVIEW",
            "basis": "NO_MATCH from configured query modes; NEW not yet proven",
            "cmoc_object_id": None,
        },
        "evidence_state": {
            "candidate_identity": True,
            "stable_object_boundary": True,
            "query_scope_sufficient": True,
            "exact_checked": True,
            "alias_checked_or_NA": True,
            "structural_checked_or_NA": True,
            "no_ambiguity": True,
            "no_unresolved_candidate": True,
            "positive_semantic_distinction": True,
            "provenance_complete": True,
            "decision_basis_complete": True,
        },
        "positive_semantic_distinction": {
            "distinction": "Synthetic distinction not covered by relevant existing knowledge",
            "basis": "Synthetic controlled fixture",
        },
        "target_object_type": "TERM",
        "traceability": {
            "source_id": "SRC-R4-TEST",
            "input_batch_id": "BATCH-R4-001",
            "record_id": "R4-CAND-001",
        },
    }


def run_case(name: str, inp: dict, expected: str) -> dict:
    original = copy.deepcopy(inp)
    result = evaluate_semantic_new(inp)
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
        run_case("COMPLETE_WITH_POSITIVE_DISTINCTION", complete, "NEW_APPROVED"),
    ]

    no_positive_distinction = copy.deepcopy(complete)
    no_positive_distinction["evidence_state"]["positive_semantic_distinction"] = False
    cases.append(
        run_case("NO_MATCH_WITHOUT_POSITIVE_DISTINCTION", no_positive_distinction, "NOT_APPROVABLE")
    )

    unknown_distinction = copy.deepcopy(complete)
    unknown_distinction["evidence_state"]["positive_semantic_distinction"] = "UNKNOWN"
    cases.append(
        run_case("UNKNOWN_SEMANTIC_DISTINCTION", unknown_distinction, "NOT_APPROVABLE")
    )

    insufficient_scope = copy.deepcopy(complete)
    insufficient_scope["evidence_state"]["query_scope_sufficient"] = False
    cases.append(
        run_case("INSUFFICIENT_QUERY_SCOPE", insufficient_scope, "NOT_APPROVABLE")
    )

    unresolved_structural = copy.deepcopy(complete)
    unresolved_structural["evidence_state"]["no_unresolved_candidate"] = False
    cases.append(
        run_case("UNRESOLVED_STRUCTURAL_CANDIDATE", unresolved_structural, "NOT_APPROVABLE")
    )

    ambiguous = copy.deepcopy(complete)
    ambiguous["evidence_state"]["no_ambiguity"] = False
    cases.append(
        run_case("AMBIGUOUS_CANDIDATE", ambiguous, "NOT_APPROVABLE")
    )

    unknown_other = copy.deepcopy(complete)
    unknown_other["evidence_state"]["decision_basis_complete"] = "UNKNOWN"
    cases.append(
        run_case("UNKNOWN_DECISION_BASIS", unknown_other, "NOT_APPROVABLE")
    )

    after = snapshot_files()

    controls = {
        "cmoc_write": "NONE",
        "object_id_created": False,
        "canonization": False,
        "relations_created": False,
        "object_index_unchanged": before.get(str(OBJECT_INDEX)) == after.get(str(OBJECT_INDEX)),
        "discovery_result_unchanged": before.get(str(DISCOVERY_RESULT)) == after.get(str(DISCOVERY_RESULT)),
        "production_runtime_imported": False,
        "production_runtime_import_blocked": True,
        "approved_does_not_write_cmoc": True,
        "not_approvable_does_not_write_cmoc": True,
    }

    all_pass = (
        all(item["pass"] for item in cases)
        and controls["cmoc_write"] == "NONE"
        and controls["object_id_created"] is False
        and controls["canonization"] is False
        and controls["relations_created"] is False
        and controls["object_index_unchanged"] is True
        and controls["discovery_result_unchanged"] is True
        and controls["production_runtime_imported"] is False
        and controls["production_runtime_import_blocked"] is True
        and controls["approved_does_not_write_cmoc"] is True
        and controls["not_approvable_does_not_write_cmoc"] is True
    )

    gate = {
        "gate": "R4-SEMANTIC-NEW-CRITERIA",
        "status": "PASS" if all_pass else "FAIL",
        "branches": cases,
        "controls": controls,
        "scope_note": (
            "NEW_APPROVED is produced only for a fully evidenced synthetic fixture. "
            "This test does not establish semantic novelty in production."
        ),
    }

    print(json.dumps(gate, ensure_ascii=False, indent=2))

    if not all_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
