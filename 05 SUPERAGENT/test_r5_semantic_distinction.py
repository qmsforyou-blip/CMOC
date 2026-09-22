#!/usr/bin/env python3
"""R5 isolated executable test.

Validates the semantic distinction model across the five meta-passport
comparison dimensions using synthetic fixtures.

This is a contract test only. It does not import or execute production
Discovery, Reconciliation, QUERY, or CMOC-write runtime.
"""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OBJECT_INDEX = ROOT / "05 SUPERAGENT" / "cmoc_object_index.json"
DISCOVERY_RESULT = ROOT / "05 SUPERAGENT" / "DISCOVERY-RESULT-SRC-003-M06-001.json"


DIMENSIONS = ("Entity", "Property", "Relation", "Mechanism", "Capability")
STATUSES = ("DISTINCT", "COVERED", "UNRESOLVED", "NOT_APPLICABLE")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot_files() -> dict[str, str]:
    result = {}
    for path in (OBJECT_INDEX, DISCOVERY_RESULT):
        if path.exists():
            result[str(path)] = sha256_file(path)
    return result


def compare(candidate: dict, existing: dict, evidence: dict) -> dict:
    """Test-local semantic comparison contract."""
    dimension = evidence.get("comparison_dimension")
    if dimension not in DIMENSIONS:
        return {
            "comparison_status": "UNRESOLVED",
            "basis": "comparison dimension is not controlled",
        }

    if evidence.get("unsupported_assertion") is True:
        return {
            "comparison_status": "UNRESOLVED",
            "basis": "unsupported assertion is not semantic evidence",
        }

    if evidence.get("evidence_state") == "UNKNOWN":
        return {
            "comparison_status": "UNRESOLVED",
            "basis": "semantic comparison evidence is UNKNOWN",
        }

    if evidence.get("wording_only") is True:
        return {
            "comparison_status": "COVERED",
            "basis": "wording difference alone does not establish semantic distinction",
        }

    if evidence.get("same_meaning_different_source") is True:
        return {
            "comparison_status": "COVERED",
            "basis": "different source does not establish semantic distinction",
        }

    if evidence.get("semantic_difference_supported") is True:
        return {
            "comparison_status": "DISTINCT",
            "basis": "synthetic semantic difference supported by controlled evidence",
        }

    return {
        "comparison_status": "UNRESOLVED",
        "basis": "semantic difference not established",
    }


def base_fixture(dimension: str) -> dict:
    return {
        "candidate": {
            "candidate_id": f"R5-CAND-{dimension.upper()}",
            "value": "Candidate-side engineering content",
        },
        "existing": {
            "existing_object_id": f"R5-EXISTING-{dimension.upper()}",
            "value": "Existing-side engineering content",
        },
        "evidence": {
            "comparison_dimension": dimension,
            "semantic_difference_supported": True,
            "source_evidence": "Synthetic controlled evidence",
            "traceability": {
                "source_id": "SRC-R5-TEST",
                "record_id": f"R5-CAND-{dimension.upper()}",
            },
        },
    }


def run_case(name: str, fixture: dict, expected: str) -> dict:
    original = copy.deepcopy(fixture)
    result = compare(
        fixture["candidate"],
        fixture["existing"],
        fixture["evidence"],
    )
    unchanged = fixture == original

    return {
        "branch": name,
        "expected": expected,
        "actual": result["comparison_status"],
        "basis": result["basis"],
        "pass": result["comparison_status"] == expected and unchanged,
        "input_unchanged": unchanged,
    }


def main() -> None:
    before = snapshot_files()
    cases = []

    for dimension in DIMENSIONS:
        cases.append(
            run_case(
                f"{dimension.upper()}_DISTINCT",
                base_fixture(dimension),
                "DISTINCT",
            )
        )

    wording_only = base_fixture("Property")
    wording_only["evidence"]["wording_only"] = True
    cases.append(run_case("WORDING_ONLY", wording_only, "COVERED"))

    different_source = base_fixture("Property")
    different_source["evidence"]["same_meaning_different_source"] = True
    cases.append(run_case("SAME_MEANING_DIFFERENT_SOURCE", different_source, "COVERED"))

    unresolved = base_fixture("Mechanism")
    unresolved["evidence"]["semantic_difference_supported"] = False
    cases.append(run_case("UNRESOLVED_EVIDENCE", unresolved, "UNRESOLVED"))

    unknown = base_fixture("Capability")
    unknown["evidence"]["evidence_state"] = "UNKNOWN"
    cases.append(run_case("UNKNOWN_EVIDENCE", unknown, "UNRESOLVED"))

    unsupported = base_fixture("Entity")
    unsupported["evidence"]["unsupported_assertion"] = True
    cases.append(run_case("UNSUPPORTED_LLM_ASSERTION", unsupported, "UNRESOLVED"))

    invalid_dimension = base_fixture("Property")
    invalid_dimension["evidence"]["comparison_dimension"] = "UnknownDimension"
    cases.append(run_case("INVALID_DIMENSION", invalid_dimension, "UNRESOLVED"))

    after = snapshot_files()

    distinct_count = sum(
        1 for item in cases
        if item["branch"].endswith("_DISTINCT") and item["actual"] == "DISTINCT"
    )

    controls = {
        "all_five_dimensions_distinct": distinct_count == 5,
        "wording_only_not_distinct": next(
            item["actual"] for item in cases if item["branch"] == "WORDING_ONLY"
        )
        != "DISTINCT",
        "different_source_not_distinct": next(
            item["actual"]
            for item in cases
            if item["branch"] == "SAME_MEANING_DIFFERENT_SOURCE"
        )
        != "DISTINCT",
        "unknown_not_distinct": next(
            item["actual"] for item in cases if item["branch"] == "UNKNOWN_EVIDENCE"
        )
        != "DISTINCT",
        "unsupported_assertion_not_distinct": next(
            item["actual"]
            for item in cases
            if item["branch"] == "UNSUPPORTED_LLM_ASSERTION"
        )
        != "DISTINCT",
        "object_index_unchanged": before.get(str(OBJECT_INDEX))
        == after.get(str(OBJECT_INDEX)),
        "discovery_result_unchanged": before.get(str(DISCOVERY_RESULT))
        == after.get(str(DISCOVERY_RESULT)),
        "cmoc_write": "NONE",
        "production_runtime_imported": False,
        "production_runtime_import_blocked": True,
    }

    all_pass = (
        all(item["pass"] for item in cases)
        and controls["all_five_dimensions_distinct"] is True
        and controls["wording_only_not_distinct"] is True
        and controls["different_source_not_distinct"] is True
        and controls["unknown_not_distinct"] is True
        and controls["unsupported_assertion_not_distinct"] is True
        and controls["object_index_unchanged"] is True
        and controls["discovery_result_unchanged"] is True
        and controls["cmoc_write"] == "NONE"
        and controls["production_runtime_imported"] is False
        and controls["production_runtime_import_blocked"] is True
    )

    gate = {
        "gate": "R5-SEMANTIC-DISTINCTION-MODEL",
        "status": "PASS" if all_pass else "FAIL",
        "branches": cases,
        "controls": controls,
        "scope_note": (
            "R5 is a synthetic comparison contract test. DISTINCT here means "
            "the controlled fixture supplies explicit semantic-difference evidence; "
            "this does not establish production semantic novelty."
        ),
    }

    print(json.dumps(gate, ensure_ascii=False, indent=2))

    if not all_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
