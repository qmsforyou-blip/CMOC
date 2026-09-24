#!/usr/bin/env python3
"""Minimal ADMISSION boundary for DECISION-CONTRACT-001 / ADMIT_EXISTING."""
from __future__ import annotations

import hashlib
from copy import deepcopy
from typing import Any, Dict


class AdmissionError(ValueError):
    pass


def _admission_id(decision_id: str, match_id: str, target: str) -> str:
    raw = f"{decision_id}|{match_id}|{target}".encode("utf-8")
    return "ADM-" + hashlib.sha256(raw).hexdigest()[:16]


def admit_existing(decision: Dict[str, Any]) -> Dict[str, Any]:
    """Create an ADMISSION record for an existing CMOC object.

    This MVP branch records the approved relationship only. It does not
    modify the CMOC object or OBJECT INDEX.
    """
    if not isinstance(decision, dict) or decision.get("type") != "DECISION":
        raise AdmissionError("DECISION_ARTIFACT_REQUIRED")

    body = decision.get("decision")
    if not isinstance(body, dict):
        raise AdmissionError("DECISION_BODY_MISSING")

    for field in ("decision_id", "decision_result", "match_id", "source_id",
                  "traceability"):
        if not body.get(field):
            raise AdmissionError(f"MISSING_DECISION_FIELD: {field}")

    if body["decision_result"] != "ADMIT_EXISTING":
        raise AdmissionError("ADMIT_EXISTING_DECISION_REQUIRED")

    traceability = deepcopy(body["traceability"])
    target = body.get("cmoc_object_id")
    if not target:
        raise AdmissionError("TARGET_CMOC_OBJECT_REQUIRED")

    admission_id = _admission_id(body["decision_id"], body["match_id"], target)

    return {
        "type": "ADMISSION",
        "admission": {
            "admission_id": admission_id,
            "decision_id": body["decision_id"],
            "match_id": body["match_id"],
            "source_id": body["source_id"],
            "source_lineage": traceability,
            "admission_result": "ADMIT_EXISTING",
            "target_cmoc_object_id": target,
            "timestamp": body.get("decided_at"),
            "traceability": traceability,
        },
        "boundary": {
            "origin": "ADMISSION",
            "decision_mutation": "NONE",
            "reconciliation_mutation": "NONE",
            "cmoc_write": "NONE",
            "object_index_write": "NONE",
        },
    }


def admit_new(decision: Dict[str, Any]) -> Dict[str, Any]:
    """Register an ADMIT_NEW admission intent without executing C1/C2/C3."""
    if not isinstance(decision, dict) or decision.get("type") != "DECISION":
        raise AdmissionError("DECISION_ARTIFACT_REQUIRED")

    body = decision.get("decision")
    if not isinstance(body, dict):
        raise AdmissionError("DECISION_BODY_MISSING")

    for field in ("decision_id", "decision_result", "match_id", "source_id",
                  "traceability", "basis"):
        if not body.get(field):
            raise AdmissionError(f"MISSING_DECISION_FIELD: {field}")

    if body["decision_result"] != "ADMIT_NEW":
        raise AdmissionError("ADMIT_NEW_DECISION_REQUIRED")

    admission_id = _admission_id(
        body["decision_id"], body["match_id"], "NEW"
    )

    return {
        "type": "ADMISSION",
        "admission": {
            "admission_id": admission_id,
            "decision_id": body["decision_id"],
            "match_id": body["match_id"],
            "source_id": body["source_id"],
            "source_lineage": deepcopy(body["traceability"]),
            "admission_result": "ADMIT_NEW",
            "target_cmoc_object_id": None,
            "timestamp": body.get("decided_at"),
            "traceability": deepcopy(body["traceability"]),
            "pipeline_status": "PENDING_C1",
        },
        "boundary": {
            "origin": "ADMISSION",
            "decision_mutation": "NONE",
            "reconciliation_mutation": "NONE",
            "cmoc_write": "NONE",
            "object_index_write": "NONE",
            "canonization_execution": "NOT_PERFORMED",
            "c1_c2_c3_execution": "NOT_PERFORMED",
        },
    }
