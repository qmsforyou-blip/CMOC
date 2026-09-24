#!/usr/bin/env python3
"""Build and validate DECISION-CONTRACT-001 v0.1 artifacts.

The builder consumes an already-produced RECONCILIATION_RESULT record.
It does not query CMOC, mutate reconciliation, execute Admission, or write
CMOC / OBJECT INDEX.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any, Dict


class DecisionContractError(ValueError):
    pass


ALLOWED_RESULTS = {"ADMIT_EXISTING", "ADMIT_NEW", "REJECT", "DEFER"}
ALLOWED_TYPES = {"HUMAN", "RULE"}
ALLOWED_MATCH_RESULTS = {"EXISTING_EQUIVALENT", "NEEDS_REVIEW"}


def build_decision(
    decision_id: str,
    decision_type: str,
    decision_result: str,
    reconciliation_record: Dict[str, Any],
    basis: str,
    decided_by: str | None = None,
    decided_at: str | None = None,
    rule_id: str | None = None,
    rule_version: str | None = None,
) -> Dict[str, Any]:
    """Create a minimal DECISION artifact from one reconciliation record."""
    if not decision_id:
        raise DecisionContractError("MISSING_DECISION_ID")
    if decision_type not in ALLOWED_TYPES:
        raise DecisionContractError(f"UNSUPPORTED_DECISION_TYPE: {decision_type}")
    if decision_result not in ALLOWED_RESULTS:
        raise DecisionContractError(
            f"UNSUPPORTED_DECISION_RESULT: {decision_result}"
        )
    if not isinstance(reconciliation_record, dict):
        raise DecisionContractError("RECONCILIATION_RECORD_NOT_OBJECT")

    for field in (
        "match_id",
        "source_id",
        "cmoc_object_id",
        "match_result",
        "traceability",
    ):
        if field not in reconciliation_record:
            raise DecisionContractError(
                f"MISSING_RECONCILIATION_FIELD: {field}"
            )

    if reconciliation_record["match_result"] not in ALLOWED_MATCH_RESULTS:
        raise DecisionContractError(
            f"UNSUPPORTED_UPSTREAM_MATCH_RESULT: "
            f"{reconciliation_record['match_result']}"
        )
    if not reconciliation_record["match_id"]:
        raise DecisionContractError("MISSING_MATCH_ID")
    if not reconciliation_record["source_id"]:
        raise DecisionContractError("MISSING_SOURCE_ID")
    if not basis:
        raise DecisionContractError("MISSING_BASIS")
    if not reconciliation_record["traceability"]:
        raise DecisionContractError("MISSING_TRACEABILITY")

    if decision_type == "HUMAN" and not decided_by:
        raise DecisionContractError("HUMAN_DECISION_MISSING_DECIDED_BY")
    if decision_type == "HUMAN" and not decided_at:
        raise DecisionContractError("HUMAN_DECISION_MISSING_DECIDED_AT")

    if decision_type == "RULE":
        if not rule_id:
            raise DecisionContractError("RULE_DECISION_MISSING_RULE_ID")
        if not rule_version:
            raise DecisionContractError("RULE_DECISION_MISSING_RULE_VERSION")
        if not decided_at:
            raise DecisionContractError("RULE_DECISION_MISSING_DECIDED_AT")

    if decision_result == "ADMIT_EXISTING":
        if reconciliation_record["match_result"] != "EXISTING_EQUIVALENT":
            raise DecisionContractError(
                "ADMIT_EXISTING_REQUIRES_EXISTING_EQUIVALENT"
            )
        if not reconciliation_record["cmoc_object_id"]:
            raise DecisionContractError(
                "ADMIT_EXISTING_REQUIRES_CMOC_OBJECT_ID"
            )

    if decision_result == "ADMIT_NEW":
        # Contract requires an explicit basis; absence of equivalence alone is
        # not sufficient. The builder does not define a novelty algorithm.
        if reconciliation_record["match_result"] != "NEEDS_REVIEW":
            raise DecisionContractError("ADMIT_NEW_REQUIRES_NEEDS_REVIEW")

    upstream_traceability = deepcopy(reconciliation_record["traceability"])
    traceability = {
        "source_id": reconciliation_record["source_id"],
        "discovery_run": upstream_traceability.get("discovery_run"),
        "reconciliation_id": upstream_traceability.get("reconciliation_id"),
        "match_id": reconciliation_record["match_id"],
    }
    for key, value in upstream_traceability.items():
        if key not in traceability:
            traceability[key] = deepcopy(value)

    result = {
        "type": "DECISION",
        "decision": {
            "decision_id": decision_id,
            "decision_type": decision_type,
            "decision_result": decision_result,
            "match_id": reconciliation_record["match_id"],
            "basis": basis,
            "cmoc_object_id": (
                reconciliation_record["cmoc_object_id"]
                if decision_result == "ADMIT_EXISTING" else None
            ),
            "source_id": reconciliation_record["source_id"],
            "traceability": traceability,
            "decided_by": decided_by,
            "decided_at": decided_at,
            "rule_id": rule_id,
            "rule_version": rule_version,
        },
        "boundary": {
            "origin": "DECISION",
            "reconciliation_mutation": "NONE",
            "cmoc_write": "NONE",
            "object_index_write": "NONE",
            "admission_execution": "NOT_PERFORMED",
        },
    }

    return result


if __name__ == "__main__":
    raise SystemExit("DECISION builder is a library; use the acceptance test.")
