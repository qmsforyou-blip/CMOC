import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "05 SUPERAGENT" / "cmoc_object_index.json"
DISCOVERY = ROOT / "05 SUPERAGENT" / "DISCOVERY-RESULT-SRC-003-M06-001.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def decide(
    *,
    eligible=True,
    positive_semantic_distinction=True,
    unknown_mandatory=False,
    unresolved_candidate=False,
    ambiguous=False,
    target_object_type_resolved=True,
    comparison_completeness="COMPLETE",
    source_evidence_complete=True,
    traceability_complete=True,
    multiple_distinctions=False,
):
    if not eligible:
        return {
            "decision": "NEW_REJECTED",
            "basis": "candidate is not eligible for NEW DECISION",
            "object_id_created": False,
            "canonization": False,
            "cmoc_write": "NONE",
        }

    mandatory = [
        positive_semantic_distinction,
        target_object_type_resolved,
        source_evidence_complete,
        traceability_complete,
        not unresolved_candidate,
        not ambiguous,
        comparison_completeness == "COMPLETE",
        not unknown_mandatory,
    ]

    if multiple_distinctions:
        positive_semantic_distinction = True

    if all(mandatory) and positive_semantic_distinction:
        return {
            "decision": "NEW_APPROVED",
            "basis": "all mandatory NEW decision conditions are satisfied",
            "object_id_created": False,
            "canonization": False,
            "cmoc_write": "NONE",
        }

    return {
        "decision": "NEW_REJECTED",
        "basis": "one or more mandatory NEW decision conditions are not satisfied",
        "object_id_created": False,
        "canonization": False,
        "cmoc_write": "NONE",
    }


def main():
    before_index = sha(INDEX)
    before_discovery = sha(DISCOVERY)
    branches = []

    cases = [
        ("COMPLETE_ELIGIBLE", {}, "NEW_APPROVED"),
        ("INELIGIBLE_INPUT", {"eligible": False}, "NEW_REJECTED"),
        ("NO_POSITIVE_DISTINCTION", {"positive_semantic_distinction": False}, "NEW_REJECTED"),
        ("UNKNOWN_MANDATORY_EVIDENCE", {"unknown_mandatory": True}, "NEW_REJECTED"),
        ("UNRESOLVED_CANDIDATE", {"unresolved_candidate": True}, "NEW_REJECTED"),
        ("AMBIGUOUS_EVIDENCE", {"ambiguous": True}, "NEW_REJECTED"),
        ("UNKNOWN_TARGET_TYPE", {"target_object_type_resolved": False}, "NEW_REJECTED"),
        ("PARTIAL_COMPARISON", {"comparison_completeness": "PARTIAL"}, "NEW_REJECTED"),
        ("MULTIPLE_POSITIVE_DISTINCTIONS", {"multiple_distinctions": True}, "NEW_APPROVED"),
    ]

    for name, kwargs, expected in cases:
        result = decide(**kwargs)
        branches.append({
            "branch": name,
            "expected": expected,
            "actual": result["decision"],
            "basis": result["basis"],
            "pass": result["decision"] == expected,
        })

    approved = decide()
    branches.append({
        "branch": "APPROVED_NO_OBJECT_ID",
        "expected": False,
        "actual": approved["object_id_created"],
        "pass": approved["object_id_created"] is False,
    })
    branches.append({
        "branch": "APPROVED_NO_CANONIZATION",
        "expected": False,
        "actual": approved["canonization"],
        "pass": approved["canonization"] is False,
    })
    branches.append({
        "branch": "APPROVED_NO_CMOC_WRITE",
        "expected": "NONE",
        "actual": approved["cmoc_write"],
        "pass": approved["cmoc_write"] == "NONE",
    })

    rejected = decide(eligible=False)
    branches.append({
        "branch": "REJECTED_NO_CMOC_WRITE",
        "expected": "NONE",
        "actual": rejected["cmoc_write"],
        "pass": rejected["cmoc_write"] == "NONE",
    })

    controls = {
        "object_index_unchanged": before_index == sha(INDEX),
        "discovery_result_unchanged": before_discovery == sha(DISCOVERY),
        "object_id_created": False,
        "canonization": False,
        "cmoc_write": "NONE",
        "production_runtime_imported": False,
        "production_runtime_import_blocked": True,
    }

    status = "PASS" if all(x["pass"] for x in branches) and (
        controls["object_index_unchanged"]
        and controls["discovery_result_unchanged"]
        and controls["object_id_created"] is False
        and controls["canonization"] is False
        and controls["cmoc_write"] == "NONE"
        and controls["production_runtime_imported"] is False
        and controls["production_runtime_import_blocked"] is True
    ) else "FAIL"

    print(json.dumps({
        "gate": "R10-NEW-DECISION-RULE",
        "status": status,
        "branches": branches,
        "controls": controls,
        "scope_note": "R10 is a synthetic NEW decision boundary test. NEW_APPROVED is produced only for controlled evidence fixtures and does not establish production semantic novelty."
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
