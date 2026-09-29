"""Immutable human decision amendment."""

from __future__ import annotations

from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path
import tempfile

from decision_store import DecisionStore


class HumanDecisionAmendmentError(ValueError):
    pass


def amend_human_decision(
    original: dict,
    amendment_id: str,
    new_result: str,
    basis: str,
    decided_by: str,
    decided_at: str | None = None,
) -> dict:
    if not isinstance(original, dict) or original.get("type") != "DECISION":
        raise HumanDecisionAmendmentError("DECISION_ARTIFACT_REQUIRED")

    body = original.get("decision")
    if not isinstance(body, dict):
        raise HumanDecisionAmendmentError("DECISION_BODY_MISSING")

    if body.get("decision_type") != "HUMAN":
        raise HumanDecisionAmendmentError("HUMAN_DECISION_REQUIRED")

    if body.get("decision_result") != "DEFER":
        raise HumanDecisionAmendmentError("ONLY_DEFER_CAN_BE_AMENDED")

    if new_result != "ADMIT_NEW":
        raise HumanDecisionAmendmentError("AMENDMENT_MUST_BE_ADMIT_NEW")

    if not amendment_id or not basis or not decided_by:
        raise HumanDecisionAmendmentError("AMENDMENT_FIELDS_REQUIRED")

    amended = deepcopy(original)
    amended_body = amended["decision"]
    original_id = body["decision_id"]

    amended_body["decision_id"] = amendment_id
    amended_body["decision_result"] = "ADMIT_NEW"
    amended_body["basis"] = basis
    amended_body["decided_by"] = decided_by
    amended_body["decided_at"] = decided_at or datetime.now(
        timezone.utc
    ).isoformat(timespec="seconds")
    amended_body["cmoc_object_id"] = None
    amended_body["amendment"] = {
        "supersedes_decision_id": original_id,
        "previous_decision_result": "DEFER",
        "amendment_type": "HUMAN_DECISION_CORRECTION",
    }

    amended["boundary"] = {
        "origin": "DECISION_AMENDMENT",
        "original_decision_mutation": "NONE",
        "reconciliation_mutation": "NONE",
        "admission_execution": "NOT_PERFORMED",
        "cmoc_write": "NONE",
        "object_index_write": "NONE",
    }

    return amended


def acceptance_test():
    original = {
        "type": "DECISION",
        "decision": {
            "decision_id": "DEC-ORIGINAL",
            "decision_type": "HUMAN",
            "decision_result": "DEFER",
            "match_id": "MAT-PAS-021",
            "source_id": "SRC-010",
            "basis": "original basis",
            "decided_by": "СГ",
            "decided_at": "2026-09-29T03:00:00+00:00",
            "cmoc_object_id": None,
            "traceability": {"match_id": "MAT-PAS-021"},
        },
        "boundary": {
            "admission_execution": "NOT_PERFORMED"
        },
    }

    with tempfile.TemporaryDirectory() as tmp:
        store = DecisionStore(Path(tmp))
        assert store.write(original) == "PERSISTED"

        amended = amend_human_decision(
            original,
            "DEC-AMEND-MAT-PAS-021-001",
            "ADMIT_NEW",
            "СГ изменяет решение после дополнительного рассмотрения.",
            "СГ",
            "2026-09-29T03:01:00+00:00",
        )

        assert original["decision"]["decision_result"] == "DEFER"
        assert amended["decision"]["decision_result"] == "ADMIT_NEW"
        assert amended["decision"]["amendment"][
            "supersedes_decision_id"
        ] == "DEC-ORIGINAL"

        assert store.write(amended) == "PERSISTED"
        assert store.write(amended) == "ALREADY_PERSISTED"

        try:
            amend_human_decision(
                original,
                "DEC-BAD",
                "DEFER",
                "invalid",
                "СГ",
            )
        except HumanDecisionAmendmentError:
            pass
        else:
            raise AssertionError("invalid amendment was accepted")

    print("HUMAN DECISION AMENDMENT: PASS")


if __name__ == "__main__":
    acceptance_test()