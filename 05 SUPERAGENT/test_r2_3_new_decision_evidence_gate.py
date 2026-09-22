#!/usr/bin/env python3
"""R2.3 isolated executable test.

This test does NOT import or execute production Discovery/Reconciliation code.
It validates only the evidence gate defined by R2.3:
NEW_DECISION_INPUT -> ELIGIBLE_FOR_NEW_DECISION / NOT_ELIGIBLE.

The test is intentionally synthetic and read-only with respect to CMOC,
OBJECT INDEX, DISCOVERY RESULT, and production runtime.
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


def evaluate_evidence_gate(inp: dict) -> str:
    """R2.3 evidence gate only; not a NEW decision and not a CMOC write."""
    evidence = inp["evidence_state"]
    required = {
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
    }

    for key, expected in required.items():
        if evidence.get(key) is not expected:
            return "NOT_ELIGIBLE"

    # UNKNOWN is never promoted to TRUE by the gate.
    if any(value == "UNKNOWN" for value in evidence.values()):
        return "NOT_ELIGIBLE"

    return "ELIGIBLE_FOR_NEW_DECISION"


def base_input() -> dict:
    return {
        "id": "R2.3-NEW-DECISION-INPUT-001",
        "candidate": {
            "record_id": "PAS-TEST-001",
            "value": "Synthetic candidate",
            "object_boundary": "source-bound boundary",
        },
        "reconciliation": {
            "match_result": "NEEDS_REVIEW",
            "basis": "NO_MATCH from configured query modes; NEW not yet proven",
            "cmoc_object_id": None,
        },
        "query_evidence": {
            "query_scope": ["TERMS"],
            "modes": {
                "exact": {"status": "NO_MATCH"},
                "alias": {"status": "NO_MATCH"},
                "structural": {"status": "NOT_APPLICABLE"},
            },
            "results": [],
        },
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
            "source_id": "SRC-TEST",
            "input_batch_id": "BATCH-R2.3-001",
            "record_id": "PAS-TEST-001",
        },
        "decision_context": "R2.3 isolated evidence-gate test",
    }


def main() -> None:
    before = snapshot_files()

    cases = []

    complete = base_input()
    cases.append(("COMPLETE", complete, "ELIGIBLE_FOR_NEW_DECISION"))

    insufficient_scope = copy.deepcopy(complete)
    insufficient_scope["evidence_state"]["query_scope_sufficient"] = False
    cases.append(("INSUFFICIENT_SCOPE", insufficient_scope, "NOT_ELIGIBLE"))

    unknown_target = copy.deepcopy(complete)
    unknown_target["evidence_state"]["target_object_type_resolved"] = "UNKNOWN"
    unknown_target["target_object_type"] = None
    cases.append(("UNKNOWN_TARGET_TYPE", unknown_target, "NOT_ELIGIBLE"))

    unresolved_candidate = copy.deepcopy(complete)
    unresolved_candidate["evidence_state"]["no_unresolved_candidate"] = False
    cases.append(("UNRESOLVED_CANDIDATE", unresolved_candidate, "NOT_ELIGIBLE"))

    ambiguous = copy.deepcopy(complete)
    ambiguous["evidence_state"]["no_ambiguity"] = False
    cases.append(("AMBIGUOUS", ambiguous, "NOT_ELIGIBLE"))

    results = []
    for name, inp, expected in cases:
        original = copy.deepcopy(inp)
        actual = evaluate_evidence_gate(inp)
        unchanged = inp == original
        results.append(
            {
                "branch": name,
                "expected": expected,
                "actual": actual,
                "pass": actual == expected and unchanged,
                "input_unchanged": unchanged,
            }
        )

    after = snapshot_files()
    all_pass = all(item["pass"] for item in results)

    gate = {
        "gate": "R2.3-NEW-DECISION-EVIDENCE-GATE",
        "status": "PASS" if all_pass else "FAIL",
        "branches": results,
        "controls": {
            "cmoc_write": "NONE",
            "object_id_created": False,
            "new_approved": False,
            "new_rejected": False,
            "canonization": False,
            "production_reconciliation_imported": False,
            "object_index_unchanged": before.get(str(OBJECT_INDEX)) == after.get(str(OBJECT_INDEX)),
            "discovery_result_unchanged": before.get(str(DISCOVERY_RESULT)) == after.get(str(DISCOVERY_RESULT)),
            "unknown_not_promoted_to_true": True,
            "eligible_is_not_new_approved": True,
        },
    }

    print(json.dumps(gate, ensure_ascii=False, indent=2))

    if not all_pass:
        raise SystemExit(1)

    if gate["controls"]["object_index_unchanged"] is False:
        raise SystemExit("OBJECT INDEX changed unexpectedly")
    if gate["controls"]["discovery_result_unchanged"] is False:
        raise SystemExit("DISCOVERY RESULT changed unexpectedly")


if __name__ == "__main__":
    main()
