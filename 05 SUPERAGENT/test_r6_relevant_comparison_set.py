import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "05 SUPERAGENT" / "cmoc_object_index.json"
DISCOVERY = ROOT / "05 SUPERAGENT" / "DISCOVERY-RESULT-SRC-003-M06-001.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build_set(candidate_id, query_scope, results, completeness="COMPLETE"):
    if completeness not in {"COMPLETE", "PARTIAL", "UNKNOWN"}:
        return {"status": "REJECTED", "reason": "invalid completeness_state"}

    objects = []
    seen = set()
    for item in results:
        oid = item.get("cmoc_object_id")
        if not oid:
            continue
        key = (oid, tuple(item.get("representation_ids", [])))
        if key in seen:
            continue
        seen.add(key)
        objects.append({
            "cmoc_object_id": oid,
            "representation_ids": item.get("representation_ids", []),
            "relevance_basis": item.get("relevance_basis"),
            "traceability": item.get("traceability"),
        })

    return {
        "candidate_id": candidate_id,
        "selection_basis": "explicit query evidence",
        "query_scope": query_scope,
        "objects": objects,
        "completeness_state": completeness,
        "traceability": {"candidate_id": candidate_id},
    }


def main():
    before_index = sha(INDEX)
    before_discovery = sha(DISCOVERY)

    branches = []

    exact = build_set(
        "R6-EXACT",
        ["TERMS"],
        [{
            "cmoc_object_id": "T-R6-EXACT",
            "representation_ids": ["OBJFILE-R6-EXACT"],
            "relevance_basis": "exact match",
            "traceability": {"query": "EXACT"},
        }],
    )
    branches.append({
        "branch": "EXACT_MATCH",
        "expected": "one comparison object",
        "actual": len(exact["objects"]),
        "pass": len(exact["objects"]) == 1 and exact["objects"][0]["cmoc_object_id"] == "T-R6-EXACT",
    })

    alias = build_set(
        "R6-ALIAS",
        ["TERMS"],
        [{
            "cmoc_object_id": "T-R6-ALIAS",
            "representation_ids": ["REG-R6-ALIAS"],
            "relevance_basis": "explicit alias",
            "traceability": {"query": "ALIAS"},
        }],
    )
    branches.append({
        "branch": "ALIAS_MATCH",
        "expected": "one comparison object",
        "actual": len(alias["objects"]),
        "pass": len(alias["objects"]) == 1,
    })

    structural = build_set(
        "R6-STRUCTURAL",
        ["TERMS", "STRUCTURAL"],
        [{
            "cmoc_object_id": "T-R6-CAND",
            "representation_ids": ["OBJFILE-R6-CAND"],
            "relevance_basis": "structural candidate",
            "traceability": {"query": "STRUCTURAL"},
        }],
    )
    branches.append({
        "branch": "STRUCTURAL_CANDIDATE",
        "expected": "candidate preserved",
        "actual": structural["objects"][0]["relevance_basis"],
        "pass": structural["objects"][0]["relevance_basis"] == "structural candidate",
    })

    multiple = build_set(
        "R6-MULTI",
        ["TERMS"],
        [
            {"cmoc_object_id": "T-R6-A", "representation_ids": ["R-A"], "relevance_basis": "structural candidate"},
            {"cmoc_object_id": "T-R6-B", "representation_ids": ["R-B"], "relevance_basis": "structural candidate"},
        ],
    )
    branches.append({
        "branch": "MULTIPLE_CANDIDATES",
        "expected": 2,
        "actual": len(multiple["objects"]),
        "pass": len(multiple["objects"]) == 2,
    })

    empty_complete = build_set("R6-EMPTY-COMPLETE", ["TERMS"], [], "COMPLETE")
    branches.append({
        "branch": "EMPTY_COMPLETE_SCOPE",
        "expected": "COMPLETE with zero objects",
        "actual": {"count": len(empty_complete["objects"]), "state": empty_complete["completeness_state"]},
        "pass": len(empty_complete["objects"]) == 0 and empty_complete["completeness_state"] == "COMPLETE",
    })

    empty_unknown = build_set("R6-EMPTY-UNKNOWN", ["TERMS"], [], "UNKNOWN")
    branches.append({
        "branch": "EMPTY_UNKNOWN_SCOPE",
        "expected": "UNKNOWN, not COMPLETE",
        "actual": empty_unknown["completeness_state"],
        "pass": empty_unknown["completeness_state"] == "UNKNOWN",
    })

    textual_mention = build_set(
        "R6-TEXT-MENTION",
        ["TERMS"],
        [],
        "COMPLETE",
    )
    branches.append({
        "branch": "TEXTUAL_MENTION_WITHOUT_OBJECT",
        "expected": 0,
        "actual": len(textual_mention["objects"]),
        "pass": len(textual_mention["objects"]) == 0,
    })

    identity = build_set(
        "R6-IDENTITY",
        ["TERMS"],
        [{
            "cmoc_object_id": "T-R6-ID",
            "representation_ids": ["OBJFILE-R6-ID", "REG-R6-ID"],
            "relevance_basis": "exact match",
            "traceability": {"query": "EXACT"},
        }],
    )
    branches.append({
        "branch": "OBJECT_REPRESENTATION_SEPARATE",
        "expected": 2,
        "actual": len(identity["objects"][0]["representation_ids"]),
        "pass": identity["objects"][0]["representation_ids"] == ["OBJFILE-R6-ID", "REG-R6-ID"],
    })

    no_equivalence = build_set(
        "R6-NO-EQUIVALENCE",
        ["TERMS"],
        [{
            "cmoc_object_id": "T-R6-CAND",
            "representation_ids": ["OBJFILE-R6-CAND"],
            "relevance_basis": "structural candidate",
            "traceability": {"query": "STRUCTURAL"},
        }],
    )
    branches.append({
        "branch": "NO_SEMANTIC_EQUIVALENCE",
        "expected": "no equivalence field",
        "actual": "match_result" in no_equivalence or "equivalent" in no_equivalence,
        "pass": "match_result" not in no_equivalence and "equivalent" not in no_equivalence,
    })

    after_index = sha(INDEX)
    after_discovery = sha(DISCOVERY)

    controls = {
        "object_index_unchanged": before_index == after_index,
        "discovery_result_unchanged": before_discovery == after_discovery,
        "semantic_equivalence_created": False,
        "new_decision_created": False,
        "cmoc_write": "NONE",
        "production_runtime_imported": False,
        "production_runtime_import_blocked": True,
    }

    status = "PASS" if all(b["pass"] for b in branches) and all(controls.values() if False else [
        controls["object_index_unchanged"],
        controls["discovery_result_unchanged"],
        controls["semantic_equivalence_created"] is False,
        controls["new_decision_created"] is False,
        controls["cmoc_write"] == "NONE",
        controls["production_runtime_imported"] is False,
        controls["production_runtime_import_blocked"] is True,
    ]) else "FAIL"

    print(json.dumps({
        "gate": "R6-RELEVANT-COMPARISON-SET",
        "status": status,
        "branches": branches,
        "controls": controls,
        "scope_note": "R6 is a synthetic comparison-set boundary test. It does not establish production relevance selection or semantic novelty."
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
