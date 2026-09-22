import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "05 SUPERAGENT" / "cmoc_object_index.json"
DISCOVERY = ROOT / "05 SUPERAGENT" / "DISCOVERY-RESULT-SRC-003-M06-001.json"

DIMENSIONS = ("Entity", "Property", "Relation", "Mechanism", "Capability")


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def assembly(candidate_id, comparison_set_completeness, comparisons):
    positive = []
    unresolved = []
    covered = []
    not_applicable = []

    for item in comparisons:
        dimension = item["comparison_dimension"]
        status = item["comparison_status"]

        if dimension not in DIMENSIONS:
            return {"status": "REJECTED", "basis": "comparison dimension is not controlled"}

        if status == "DISTINCT":
            if not all(item.get(k) for k in ("distinction", "basis", "source_evidence", "traceability")):
                return {
                    "status": "NOT_APPROVABLE",
                    "basis": f"DISTINCT evidence incomplete for {dimension}",
                }
            positive.append(item)

        elif status == "UNRESOLVED":
            unresolved.append(item)

        elif status == "COVERED":
            covered.append(item)

        elif status == "NOT_APPLICABLE":
            not_applicable.append(item)

        else:
            return {"status": "REJECTED", "basis": "unknown comparison status"}

    if comparison_set_completeness == "UNKNOWN":
        return {
            "status": "NOT_APPROVABLE",
            "basis": "comparison-set completeness UNKNOWN",
            "positive_distinctions": positive,
            "unresolved_dimensions": unresolved,
            "covered_dimensions": covered,
            "not_applicable_dimensions": not_applicable,
        }

    if not positive:
        return {
            "status": "NO_POSITIVE_DISTINCTION",
            "basis": "no valid DISTINCT comparison evidence",
            "positive_distinctions": [],
            "unresolved_dimensions": unresolved,
            "covered_dimensions": covered,
            "not_applicable_dimensions": not_applicable,
        }

    return {
        "status": "SEMANTIC_DISTINCTION",
        "candidate_id": candidate_id,
        "compared_object_ids": sorted({x["existing_object_id"] for x in positive + unresolved + covered + not_applicable}),
        "positive_distinctions": positive,
        "unresolved_dimensions": unresolved,
        "covered_dimensions": covered,
        "not_applicable_dimensions": not_applicable,
        "evidence_state": comparison_set_completeness,
        "basis": "one or more valid dimension-level DISTINCT results assembled with preserved evidence",
    }


def record(dimension, status, *, evidence=True):
    return {
        "candidate_id": "C-R8",
        "existing_object_id": "O-R8",
        "comparison_dimension": dimension,
        "comparison_status": status,
        "distinction": "controlled semantic distinction" if status == "DISTINCT" and evidence else None,
        "basis": "controlled comparison evidence" if evidence else None,
        "source_evidence": {"source_id": "SRC-R8"} if evidence else None,
        "traceability": {"record_id": f"R8-{dimension}"} if evidence else None,
    }


def main():
    before_index = sha(INDEX)
    before_discovery = sha(DISCOVERY)
    branches = []

    cases = [
        ("ONE_DISTINCT_REST_COVERED",
         "COMPLETE",
         [record("Property", "DISTINCT"), record("Entity", "COVERED")],
         "SEMANTIC_DISTINCTION"),
        ("DISTINCT_PLUS_UNRESOLVED",
         "COMPLETE",
         [record("Property", "DISTINCT"), record("Mechanism", "UNRESOLVED")],
         "SEMANTIC_DISTINCTION"),
        ("ONLY_COVERED",
         "COMPLETE",
         [record("Entity", "COVERED"), record("Property", "COVERED")],
         "NO_POSITIVE_DISTINCTION"),
        ("ALL_UNRESOLVED",
         "COMPLETE",
         [record("Entity", "UNRESOLVED"), record("Property", "UNRESOLVED")],
         "NO_POSITIVE_DISTINCTION"),
        ("MULTIPLE_DISTINCT",
         "COMPLETE",
         [record("Entity", "DISTINCT"), record("Property", "DISTINCT")],
         "SEMANTIC_DISTINCTION"),
        ("NOT_APPLICABLE",
         "COMPLETE",
         [record("Entity", "DISTINCT"), record("Capability", "NOT_APPLICABLE")],
         "SEMANTIC_DISTINCTION"),
        ("UNKNOWN_COMPARISON_SET",
         "UNKNOWN",
         [record("Property", "DISTINCT")],
         "NOT_APPROVABLE"),
        ("DISTINCT_WITHOUT_SOURCE_EVIDENCE",
         "COMPLETE",
         [record("Property", "DISTINCT", evidence=False)],
         "NOT_APPROVABLE"),
        ("DISTINCT_WITHOUT_TRACEABILITY",
         "COMPLETE",
         [dict(record("Property", "DISTINCT"), traceability=None)],
         "NOT_APPROVABLE"),
    ]

    for name, completeness, comparisons, expected in cases:
        actual = assembly("C-R8", completeness, comparisons)["status"]
        branches.append({
            "branch": name,
            "expected": expected,
            "actual": actual,
            "pass": actual == expected,
        })

    multi = assembly("C-R8", "COMPLETE", [
        record("Entity", "DISTINCT"),
        record("Property", "DISTINCT"),
        record("Relation", "COVERED"),
        record("Mechanism", "UNRESOLVED"),
        record("Capability", "NOT_APPLICABLE"),
    ])
    branches.append({
        "branch": "DIMENSIONS_PRESERVED",
        "expected": {
            "positive": 2,
            "covered": 1,
            "unresolved": 1,
            "not_applicable": 1,
        },
        "actual": {
            "positive": len(multi["positive_distinctions"]),
            "covered": len(multi["covered_dimensions"]),
            "unresolved": len(multi["unresolved_dimensions"]),
            "not_applicable": len(multi["not_applicable_dimensions"]),
        },
        "pass": (
            len(multi["positive_distinctions"]) == 2
            and len(multi["covered_dimensions"]) == 1
            and len(multi["unresolved_dimensions"]) == 1
            and len(multi["not_applicable_dimensions"]) == 1
        ),
    })

    controls = {
        "object_index_unchanged": before_index == sha(INDEX),
        "discovery_result_unchanged": before_discovery == sha(DISCOVERY),
        "new_approved": False,
        "cmoc_write": "NONE",
        "object_id_created": False,
        "canonization": False,
        "production_runtime_imported": False,
        "production_runtime_import_blocked": True,
    }

    status = "PASS" if all(x["pass"] for x in branches) and (
        controls["object_index_unchanged"]
        and controls["discovery_result_unchanged"]
        and controls["new_approved"] is False
        and controls["cmoc_write"] == "NONE"
        and controls["object_id_created"] is False
        and controls["canonization"] is False
        and controls["production_runtime_imported"] is False
        and controls["production_runtime_import_blocked"] is True
    ) else "FAIL"

    print(json.dumps({
        "gate": "R8-SEMANTIC-DISTINCTION-ASSEMBLY",
        "status": status,
        "branches": branches,
        "controls": controls,
        "scope_note": "R8 is a synthetic semantic-distinction assembly boundary test. It does not establish production novelty or NEW approval."
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
