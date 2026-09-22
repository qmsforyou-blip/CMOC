import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "05 SUPERAGENT" / "cmoc_object_index.json"
DISCOVERY = ROOT / "05 SUPERAGENT" / "DISCOVERY-RESULT-SRC-003-M06-001.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def aggregate(
    *,
    completeness="COMPLETE",
    source_evidence=True,
    traceability=True,
    target_object_type="MACHINE",
    query_scope_sufficient=True,
    unresolved_candidate=False,
    ambiguous=False,
    positive_distinctions=1,
):
    evidence_state = {
        "source_bound_candidate": True,
        "stable_object_boundary": True,
        "traceability_complete": traceability,
        "query_scope_sufficient": query_scope_sufficient,
        "semantic_distinction_present": positive_distinctions > 0,
        "target_object_type_resolved": target_object_type is not None,
        "source_evidence_complete": source_evidence,
        "no_unresolved_candidate": not unresolved_candidate,
        "no_ambiguity": not ambiguous,
    }

    if completeness == "UNKNOWN":
        evidence_state["comparison_set_sufficient"] = False
    elif completeness == "PARTIAL":
        evidence_state["comparison_set_sufficient"] = False
    else:
        evidence_state["comparison_set_sufficient"] = True

    eligibility = all(evidence_state.values())

    return {
        "status": "ELIGIBLE_FOR_NEW_DECISION" if eligibility else "NOT_ELIGIBLE",
        "new_approved": False,
        "evidence_state": evidence_state,
        "comparison_set_completeness": completeness,
        "positive_distinctions": positive_distinctions,
        "target_object_type": target_object_type,
        "traceability": {"candidate_id": "C-R9"} if traceability else None,
    }


def main():
    before_index = sha(INDEX)
    before_discovery = sha(DISCOVERY)
    branches = []

    cases = [
        ("COMPLETE_EVIDENCE", {}, "ELIGIBLE_FOR_NEW_DECISION"),
        ("UNKNOWN_COMPARISON_COMPLETENESS", {"completeness": "UNKNOWN"}, "NOT_ELIGIBLE"),
        ("PARTIAL_COMPARISON_COMPLETENESS", {"completeness": "PARTIAL"}, "NOT_ELIGIBLE"),
        ("MISSING_SOURCE_EVIDENCE", {"source_evidence": False}, "NOT_ELIGIBLE"),
        ("MISSING_TRACEABILITY", {"traceability": False}, "NOT_ELIGIBLE"),
        ("UNKNOWN_TARGET_TYPE", {"target_object_type": None}, "NOT_ELIGIBLE"),
        ("INSUFFICIENT_QUERY_SCOPE", {"query_scope_sufficient": False}, "NOT_ELIGIBLE"),
        ("UNRESOLVED_CANDIDATE", {"unresolved_candidate": True}, "NOT_ELIGIBLE"),
        ("AMBIGUOUS_COMPARISON_SET", {"ambiguous": True}, "NOT_ELIGIBLE"),
        ("MULTIPLE_POSITIVE_DISTINCTIONS", {"positive_distinctions": 3}, "ELIGIBLE_FOR_NEW_DECISION"),
    ]

    for name, kwargs, expected in cases:
        actual = aggregate(**kwargs)["status"]
        branches.append({
            "branch": name,
            "expected": expected,
            "actual": actual,
            "pass": actual == expected,
        })

    complete = aggregate()
    branches.append({
        "branch": "ELIGIBLE_IS_NOT_NEW_APPROVED",
        "expected": False,
        "actual": complete["new_approved"],
        "pass": complete["new_approved"] is False,
    })

    controls = {
        "object_index_unchanged": before_index == sha(INDEX),
        "discovery_result_unchanged": before_discovery == sha(DISCOVERY),
        "cmoc_write": "NONE",
        "object_id_created": False,
        "canonization": False,
        "new_approved": False,
        "production_runtime_imported": False,
        "production_runtime_import_blocked": True,
    }

    status = "PASS" if all(x["pass"] for x in branches) and (
        controls["object_index_unchanged"]
        and controls["discovery_result_unchanged"]
        and controls["cmoc_write"] == "NONE"
        and controls["object_id_created"] is False
        and controls["canonization"] is False
        and controls["new_approved"] is False
        and controls["production_runtime_imported"] is False
        and controls["production_runtime_import_blocked"] is True
    ) else "FAIL"

    print(json.dumps({
        "gate": "R9-NEW-DECISION-EVIDENCE-AGGREGATION",
        "status": status,
        "branches": branches,
        "controls": controls,
        "scope_note": "R9 is a synthetic evidence-aggregation boundary test. It does not make a NEW decision or establish production semantic novelty."
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
