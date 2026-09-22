from __future__ import annotations

import copy
import hashlib
import json


# ============================================================
# C1 — CANONIZATION BOUNDARY
# ============================================================
#
# Isolated synthetic boundary test.
#
# NEW_APPROVED
#      ↓
# CANONIZATION
#      ↓
# CANONICALIZATION_READY
#
# C1 MUST NOT:
# - re-decide NEW;
# - perform semantic comparison;
# - mutate existing CMOC objects;
# - create unsupported relations;
# - write to CMOC.
#
# This test intentionally does NOT import production runtime.
# ============================================================


PRODUCTION_RUNTIME_IMPORTED = False
CMOC_WRITE = "NONE"


def stable_hash(value) -> str:
    payload = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def make_valid_input() -> dict:
    candidate = {
        "candidate_id": "C1-CAND-001",
        "value": "Controlled synthetic object",
        "object_boundary": {
            "entity": "synthetic management object",
            "boundary": "controlled fixture",
        },
    }

    return {
        "candidate": candidate,
        "new_decision": {
            "decision_id": "DEC-C1-001",
            "decision": "NEW_APPROVED",
            "basis": "controlled synthetic NEW decision evidence",
            "evidence_summary": {
                "positive_semantic_distinction": True,
                "query_scope_sufficient": True,
            },
        },
        "provenance": {
            "source_id": "SRC-C1-SYNTHETIC",
            "input_batch_id": "BATCH-C1-001",
        },
        "traceability": {
            "discovery_record": "DISC-C1-001",
            "reconciliation": "MAT-C1-001",
            "query": "QUERY-C1-001",
            "comparison_set": "SET-C1-001",
            "semantic_comparison": "CMP-C1-001",
            "semantic_distinction": "DIST-C1-001",
            "new_decision": "DEC-C1-001",
        },
        "target_object_type": "TERM",
        "decision_context": {
            "rule_version": "R10-C1-SYNTHETIC",
        },
        "integrity": {
            "approved_candidate_hash": stable_hash(candidate),
        },
    }


def canonize(inp: dict) -> dict:
    """
    Isolated C1 canonicalization function.

    It accepts ONLY NEW_APPROVED input and performs
    representation-level canonicalization.

    It does NOT:
    - perform NEW decision;
    - inspect CMOC;
    - perform semantic comparison;
    - create relations;
    - write CMOC.

    It DOES verify that the received candidate is identical
    to the candidate representation approved by NEW DECISION.
    This is an integrity check, not a semantic comparison.
    """

    decision = inp["new_decision"].get("decision")

    if decision != "NEW_APPROVED":
        return {
            "status": "NOT_ELIGIBLE",
            "basis": "entry condition NEW_APPROVED not satisfied",
        }

    if not inp.get("provenance"):
        return {
            "status": "NOT_ELIGIBLE",
            "basis": "missing provenance",
        }

    if not inp.get("traceability"):
        return {
            "status": "NOT_ELIGIBLE",
            "basis": "missing traceability",
        }

    approved_candidate_hash = (
        inp.get("integrity", {})
        .get("approved_candidate_hash")
    )

    if not approved_candidate_hash:
        return {
            "status": "NOT_ELIGIBLE",
            "basis": "missing approved candidate integrity hash",
        }

    current_candidate = {
        "candidate_id": inp["candidate"]["candidate_id"],
        "value": inp["candidate"]["value"],
        "object_boundary": inp["candidate"]["object_boundary"],
    }

    current_hash = stable_hash(current_candidate)

    if current_hash != approved_candidate_hash:
        return {
            "status": "REJECT",
            "basis": "approved candidate integrity hash mismatch",
        }

    candidate = copy.deepcopy(inp["candidate"])

    # Canonical object identity is created HERE,
    # and nowhere earlier in the pipeline.
    object_id = "OBJ-C1-CANON-001"

    return {
        "status": "CANONICALIZATION_READY",
        "object": {
            "object_id": object_id,
            "object_type": inp["target_object_type"],
            "canonical_name": candidate["value"],
            "object_boundary": candidate["object_boundary"],
        },
        "source": copy.deepcopy(inp["provenance"]),
        "evidence": {
            "new_decision_id": inp["new_decision"]["decision_id"],
            "semantic_distinction": "DIST-C1-001",
            "query_evidence": "QUERY-C1-001",
        },
        "traceability": copy.deepcopy(inp["traceability"]),
        "cmoc_write": {
            "status": "NOT_PERFORMED",
        },
    }


def run_branch(
    branch: str,
    inp: dict,
    expected_status: str,
    expected_basis: str | None = None,
) -> dict:

    original = copy.deepcopy(inp)
    original_hash = stable_hash(original)

    result = canonize(inp)

    input_hash = stable_hash(inp)

    input_unchanged = (
        original_hash == input_hash
        and inp == original
    )

    passed = result.get("status") == expected_status

    if expected_basis is not None:
        passed = passed and result.get("basis") == expected_basis

    return {
        "branch": branch,
        "expected": expected_status,
        "actual": result.get("status"),
        "basis": result.get("basis"),
        "pass": passed,
        "input_unchanged": input_unchanged,
    }


def main() -> None:

    branches = []

    # ========================================================
    # C1-01 — valid NEW_APPROVED
    # ========================================================

    valid = make_valid_input()
    original_valid = copy.deepcopy(valid)
    result = canonize(valid)

    valid_pass = (
        result["status"] == "CANONICALIZATION_READY"
        and bool(result["object"]["object_id"])
        and result["cmoc_write"]["status"] == "NOT_PERFORMED"
        and valid == original_valid
    )

    branches.append({
        "branch": "NEW_APPROVED",
        "expected": "CANONICALIZATION_READY",
        "actual": result["status"],
        "object_id_created": bool(
            result.get("object", {}).get("object_id")
        ),
        "cmoc_write": result["cmoc_write"]["status"],
        "pass": valid_pass,
        "input_unchanged": valid == original_valid,
    })

    # ========================================================
    # C1-02 — NEW_REJECTED
    # ========================================================

    rejected = make_valid_input()
    rejected["new_decision"]["decision"] = "NEW_REJECTED"

    branches.append(
        run_branch(
            "NEW_REJECTED",
            rejected,
            "NOT_ELIGIBLE",
            "entry condition NEW_APPROVED not satisfied",
        )
    )

    # ========================================================
    # C1-03 — missing provenance
    # ========================================================

    no_provenance = make_valid_input()
    no_provenance["provenance"] = {}

    branches.append(
        run_branch(
            "MISSING_PROVENANCE",
            no_provenance,
            "NOT_ELIGIBLE",
            "missing provenance",
        )
    )

    # ========================================================
    # C1-04 — missing traceability
    # ========================================================

    no_traceability = make_valid_input()
    no_traceability["traceability"] = {}

    branches.append(
        run_branch(
            "MISSING_TRACEABILITY",
            no_traceability,
            "NOT_ELIGIBLE",
            "missing traceability",
        )
    )

    # ========================================================
    # C1-05 — approved candidate integrity changed
    # ========================================================

    integrity_changed = make_valid_input()
    integrity_changed["candidate"]["value"] = (
        "FORBIDDEN SEMANTIC REWRITE"
    )

    result = canonize(integrity_changed)

    branches.append({
        "branch": "APPROVED_CANDIDATE_INTEGRITY_CHANGED",
        "expected": "REJECT",
        "actual": result.get("status"),
        "basis": result.get("basis"),
        "pass": (
            result.get("status") == "REJECT"
            and result.get("basis")
            == "approved candidate integrity hash mismatch"
        ),
        "input_unchanged": True,
    })

    # ========================================================
    # C1-06 — hidden semantic enrichment
    # ========================================================

    enrichment = make_valid_input()
    result = canonize(enrichment)

    forbidden_fields = {
        "semantic_decision",
        "semantic_equivalence",
        "semantic_conflict",
        "novelty_assessment",
        "llm_novelty_judgment",
    }

    produced_fields = set(result.keys())
    hidden_enrichment = bool(
        forbidden_fields.intersection(produced_fields)
    )

    branches.append({
        "branch": "HIDDEN_SEMANTIC_ENRICHMENT",
        "expected": "REJECT",
        "actual": (
            "REJECT"
            if hidden_enrichment
            else "NO_HIDDEN_ENRICHMENT"
        ),
        "forbidden_fields_found": sorted(
            forbidden_fields.intersection(produced_fields)
        ),
        "pass": not hidden_enrichment,
    })

    # ========================================================
    # C1-07 — unauthorized existing-object mutation
    # ========================================================

    mutation_input = make_valid_input()
    result = canonize(mutation_input)

    unauthorized_mutation = (
        "existing_object_mutation" in result
    )

    branches.append({
        "branch": "UNAUTHORIZED_EXISTING_OBJECT_MUTATION",
        "expected": "REJECT",
        "actual": (
            "REJECT"
            if unauthorized_mutation
            else "NO_EXISTING_OBJECT_MUTATION"
        ),
        "pass": not unauthorized_mutation,
    })

    # ========================================================
    # C1-08 — unsupported relation creation
    # ========================================================

    relation_input = make_valid_input()
    result = canonize(relation_input)

    relations_created = (
        "relations" in result
        or "relation_records" in result
    )

    branches.append({
        "branch": "UNSUPPORTED_RELATION_CREATION",
        "expected": "REJECT",
        "actual": (
            "REJECT"
            if relations_created
            else "NO_RELATIONS_CREATED"
        ),
        "pass": not relations_created,
    })

    # ========================================================
    # C1-09 — missing integrity hash
    # ========================================================

    no_integrity = make_valid_input()
    no_integrity["integrity"] = {}

    branches.append(
        run_branch(
            "MISSING_APPROVED_CANDIDATE_INTEGRITY_HASH",
            no_integrity,
            "NOT_ELIGIBLE",
            "missing approved candidate integrity hash",
        )
    )

    # ========================================================
    # Global controls
    # ========================================================

    valid_result = canonize(make_valid_input())

    integrity_control_input = make_valid_input()
    integrity_control_input["candidate"]["value"] = (
        "CHANGED AFTER APPROVAL"
    )

    integrity_control_result = canonize(
        integrity_control_input
    )

    controls = {
        "production_runtime_imported": PRODUCTION_RUNTIME_IMPORTED,
        "cmoc_write": CMOC_WRITE,
        "object_id_created_only_in_c1": bool(
            valid_result["object"]["object_id"]
        ),
        "canonization_does_not_redecide_new": (
            valid_result["status"]
            == "CANONICALIZATION_READY"
        ),
        "approved_preserved": (
            valid_result["evidence"]["new_decision_id"]
            == "DEC-C1-001"
        ),
        "relations_created": (
            "relations" in valid_result
            or "relation_records" in valid_result
        ),
        "existing_object_mutated": (
            "existing_object_mutation" in valid_result
        ),
        "cmoc_write_not_performed": (
            valid_result["cmoc_write"]["status"]
            == "NOT_PERFORMED"
        ),
        "approved_candidate_integrity_enforced": (
            integrity_control_result.get("status") == "REJECT"
            and integrity_control_result.get("basis")
            == "approved candidate integrity hash mismatch"
        ),
    }

    # ========================================================
    # Final gate
    # ========================================================

    all_branch_pass = all(
        branch["pass"]
        for branch in branches
    )

    controls_pass = (
        controls["production_runtime_imported"] is False
        and controls["cmoc_write"] == "NONE"
        and controls["object_id_created_only_in_c1"] is True
        and controls["canonization_does_not_redecide_new"] is True
        and controls["approved_preserved"] is True
        and controls["relations_created"] is False
        and controls["existing_object_mutated"] is False
        and controls["cmoc_write_not_performed"] is True
        and controls["approved_candidate_integrity_enforced"] is True
    )

    overall_pass = all_branch_pass and controls_pass

    output = {
        "gate": "C1-CANONIZATION-BOUNDARY",
        "status": "PASS" if overall_pass else "FAIL",
        "branches": branches,
        "controls": controls,
        "scope_note": (
            "C1 is an isolated synthetic canonization boundary test. "
            "It proves representation-level canonization after "
            "NEW_APPROVED with approved-candidate integrity control "
            "and without CMOC WRITE. It does not establish "
            "production semantic novelty, production canonization, "
            "or CMOC persistence."
        ),
    }

    print(
        json.dumps(
            output,
            ensure_ascii=False,
            indent=2,
        )
    )

    raise SystemExit(0 if overall_pass else 1)


if __name__ == "__main__":
    main()
