"""P7 production CMOC writer.

Persists an already approved/canonically prepared representation into an
isolated physical CMOC repository target. It performs no semantic decisions.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class CmocWriteResult:
    status: str
    object_id: str | None = None
    basis: str | None = None


class ProductionCmocWriter:
    """Concrete P7 persistence boundary for canonical CMOC representations."""

    REQUIRED = (
        "status", "run_id", "source_id", "batch_id", "stage_id",
        "attempt_id", "result_id", "object_id", "object_type",
        "canonical_name", "canonical_representation", "provenance",
        "traceability", "new_evidence_ref", "approved_candidate_hash",
    )

    def __init__(self, target_root: str | Path):
        self.target_root = Path(target_root)

    def _target(self, object_id: str) -> Path:
        safe_id = str(object_id)
        if not safe_id or safe_id in {".", ".."} or "/" in safe_id or "\\" in safe_id:
            raise ValueError("invalid object_id for CMOC target")
        return self.target_root / f"{safe_id}.md"

    @staticmethod
    def _encode(payload: dict[str, Any]) -> str:
        return (
            "# CMOC CANONICAL OBJECT — P7 TEST TARGET\n"
            "<CMOC_JSON>\n"
            + json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
            + "\n</CMOC_JSON>\n"
        )

    @staticmethod
    def _decode(text: str) -> dict[str, Any]:
        start_marker = "<CMOC_JSON>\n"
        end_marker = "\n</CMOC_JSON>"
        start = text.index(start_marker) + len(start_marker)
        end = text.index(end_marker, start)
        return json.loads(text[start:end])

    def write(self, payload: dict[str, Any]) -> CmocWriteResult:
        missing = [key for key in self.REQUIRED if not payload.get(key)]
        if missing:
            return CmocWriteResult("CMOC_WRITE_REJECTED", basis=f"missing: {missing}")

        if payload["status"] != "CANONICALIZATION_READY":
            return CmocWriteResult(
                "CMOC_WRITE_REJECTED", basis="invalid entry state"
            )

        if payload.get("unsupported_relations"):
            return CmocWriteResult(
                "CMOC_WRITE_REJECTED", basis="unsupported relations"
            )

        try:
            target = self._target(payload["object_id"])
        except ValueError as exc:
            return CmocWriteResult("CMOC_WRITE_REJECTED", basis=str(exc))

        self.target_root.mkdir(parents=True, exist_ok=True)

        if target.exists():
            existing = self._decode(target.read_text(encoding="utf-8"))
            if existing.get("object_id") == payload["object_id"]:
                if existing == payload:
                    return CmocWriteResult(
                        "ALREADY_PERSISTED", object_id=payload["object_id"]
                    )
                return CmocWriteResult(
                    "EXISTING_OBJECT_WRITE_CONFLICT",
                    object_id=payload["object_id"],
                )
            return CmocWriteResult(
                "EXISTING_OBJECT_WRITE_CONFLICT",
                object_id=payload["object_id"],
            )

        target.write_text(self._encode(payload), encoding="utf-8")

        persisted = self._decode(target.read_text(encoding="utf-8"))
        if persisted != payload:
            return CmocWriteResult(
                "POST_WRITE_VERIFICATION_FAILED",
                object_id=payload["object_id"],
            )

        return CmocWriteResult(
            "CMOC_WRITE_ACCEPTED", object_id=payload["object_id"]
        )
