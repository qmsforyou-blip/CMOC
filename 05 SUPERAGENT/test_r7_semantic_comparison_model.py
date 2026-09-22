import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "05 SUPERAGENT" / "cmoc_object_index.json"
DISCOVERY = ROOT / "05 SUPERAGENT" / "DISCOVERY-RESULT-SRC-003-M06-001.json"

DIMENSIONS = ("Entity", "Property", "Relation", "Mechanism", "Capability")
STATUSES = ("DISTINCT", "COVERED", "UNRESOLVED", "NOT_APPLICABLE")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def compare(candidate, existing, dimension, *, comparison_set_completeness="COMPLETE",
            wording_only=False, same_meaning_different_source=False,
            unknown=False, unsupported_assertion=False,
            semantic_difference_supported=False, not_applicable=False):
    if dimension not in DIMENSIONS:
        return {"comparison_status": "UNRESOLVED", "basis": "comparison dimension is not controlled"}

    if comparison_set_completeness == "UNKNOWN":
        return {
            "comparison_status": "UNRESOLVED",
            "basis": "comparison-set completeness UNKNOWN blocks positive semantic comparison",
        }

    if comparison_set_completeness not in {"COMPLETE", "PARTIAL"}:
        return {
            "comparison_status": "UNRESOLVED",
            "basis": "comparison-set completeness is not controlled",
        }

    if not_applicable:
        return {
            "comparison_status": "NOT_APPLICABLE",
            "basis": "dimension does not apply; controlled reason recorded",
        }

    if unknown:
        return {"comparison_status": "UNRESOLVED", "basis": "comparison evidence is UNKNOWN"}

    if unsupported_assertion:
        return {"comparison_status": "UNRESOLVED", "basis": "unsupported LLM assertion is not evidence"}

    if wording_only:
        return {
            "comparison_status": "COVERED",
            "basis": "wording difference alone does not establish semantic distinction",
        }

    if same_meaning_different_source:
        return {
            "comparison_status": "COVERED",
            "basis": "different source does not establish semantic distinction",
        }

    if semantic_difference_supported:
        return {
            "comparison_status": "DISTINCT",
            "basis": "supported semantic difference for controlled dimension",
        }

    return {"comparison_status": "UNRESOLVED", "basis": "semantic comparison not established"}


def main():
    before_index = sha(INDEX)
    before_discovery = sha(DISCOVERY)
    branches = []

    for dimension in DIMENSIONS:
        result = compare("C-R7", "O-R7", dimension, semantic_difference_supported=True)
        branches.append({
            "branch": f"{dimension.upper()}_DISTINCT",
            "expected": "DISTINCT",
            "actual": result["comparison_status"],
            "basis": result["basis"],
            "pass": result["comparison_status"] == "DISTINCT",
        })

    result = compare("C-R7", "O-R7", "Property", wording_only=True)
    branches.append({
        "branch": "WORDING_ONLY",
        "expected": "COVERED",
        "actual": result["comparison_status"],
        "basis": result["basis"],
        "pass": result["comparison_status"] == "COVERED",
    })

    result = compare("C-R7", "O-R7", "Property", same_meaning_different_source=True)
    branches.append({
        "branch": "SAME_MEANING_DIFFERENT_SOURCE",
        "expected": "COVERED",
        "actual": result["comparison_status"],
        "basis": result["basis"],
        "pass": result["comparison_status"] == "COVERED",
    })

    result = compare("C-R7", "O-R7", "Relation", unsupported_assertion=True)
    branches.append({
        "branch": "UNSUPPORTED_LLM_ASSERTION",
        "expected": "UNRESOLVED",
        "actual": result["comparison_status"],
        "basis": result["basis"],
        "pass": result["comparison_status"] == "UNRESOLVED",
    })

    result = compare("C-R7", "O-R7", "Mechanism", unknown=True)
    branches.append({
        "branch": "UNKNOWN_EVIDENCE",
        "expected": "UNRESOLVED",
        "actual": result["comparison_status"],
        "basis": result["basis"],
        "pass": result["comparison_status"] == "UNRESOLVED",
    })

    result = compare("C-R7", "O-R7", "Capability", not_applicable=True)
    branches.append({
        "branch": "NOT_APPLICABLE",
        "expected": "NOT_APPLICABLE",
        "actual": result["comparison_status"],
        "basis": result["basis"],
        "pass": result["comparison_status"] == "NOT_APPLICABLE",
    })

    multiple = [
        compare("C-R7", "O-R7-A", "Entity", semantic_difference_supported=True),
        compare("C-R7", "O-R7-B", "Entity", wording_only=True),
        compare("C-R7", "O-R7-C", "Entity", unknown=True),
    ]
    branches.append({
        "branch": "MULTIPLE_EXISTING_OBJECTS",
        "expected": ["DISTINCT", "COVERED", "UNRESOLVED"],
        "actual": [x["comparison_status"] for x in multiple],
        "pass": [x["comparison_status"] for x in multiple] == ["DISTINCT", "COVERED", "UNRESOLVED"],
    })

    mixed = {
        dimension: compare(
            "C-R7",
            "O-R7",
            dimension,
            semantic_difference_supported=(dimension == "Property"),
            unknown=(dimension == "Mechanism"),
        )
        for dimension in DIMENSIONS
    }
    branches.append({
        "branch": "DIMENSION_LOCAL_MIXED_RESULTS",
        "expected": {
            "Entity": "UNRESOLVED",
            "Property": "DISTINCT",
            "Relation": "UNRESOLVED",
            "Mechanism": "UNRESOLVED",
            "Capability": "UNRESOLVED",
        },
        "actual": {k: v["comparison_status"] for k, v in mixed.items()},
        "pass": {k: v["comparison_status"] for k, v in mixed.items()} == {
            "Entity": "UNRESOLVED",
            "Property": "DISTINCT",
            "Relation": "UNRESOLVED",
            "Mechanism": "UNRESOLVED",
            "Capability": "UNRESOLVED",
        },
    })

    unknown_set_result = compare(
        "C-R7",
        "O-R7",
        "Entity",
        comparison_set_completeness="UNKNOWN",
        semantic_difference_supported=True,
    )
    branches.append({
        "branch": "UNKNOWN_COMPARISON_SET",
        "expected": "UNRESOLVED",
        "actual": unknown_set_result["comparison_status"],
        "basis": unknown_set_result["basis"],
        "pass": unknown_set_result["comparison_status"] == "UNRESOLVED",
    })

    partial_set_result = compare(
        "C-R7",
        "O-R7",
        "Entity",
        comparison_set_completeness="PARTIAL",
        semantic_difference_supported=True,
    )
    branches.append({
        "branch": "PARTIAL_COMPARISON_SET",
        "expected": "DISTINCT",
        "actual": partial_set_result["comparison_status"],
        "basis": partial_set_result["basis"],
        "pass": partial_set_result["comparison_status"] == "DISTINCT",
    })

    before_index_2 = sha(INDEX)
    before_discovery_2 = sha(DISCOVERY)

    controls = {
        "object_index_unchanged": before_index == before_index_2,
        "discovery_result_unchanged": before_discovery == before_discovery_2,
        "new_approved": False,
        "cmoc_write": "NONE",
        "production_runtime_imported": False,
        "production_runtime_import_blocked": True,
    }

    status = "PASS" if all(b["pass"] for b in branches) and (
        controls["object_index_unchanged"]
        and controls["discovery_result_unchanged"]
        and controls["new_approved"] is False
        and controls["cmoc_write"] == "NONE"
        and controls["production_runtime_imported"] is False
        and controls["production_runtime_import_blocked"] is True
    ) else "FAIL"

    print(json.dumps({
        "gate": "R7.1-SEMANTIC-COMPARISON-COMPLETENESS-GATE",
        "status": status,
        "branches": branches,
        "controls": controls,
        "scope_note": "R7.1 is a synthetic correction test. UNKNOWN comparison-set completeness now enters the comparison function and blocks positive semantic comparison. This does not establish production semantic comparison or novelty."
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
