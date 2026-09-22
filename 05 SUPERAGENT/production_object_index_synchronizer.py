"""P8 production OBJECT INDEX synchronization runtime boundary."""

from __future__ import annotations

import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class IndexSyncResult:
    status: str
    object_id: str | None = None
    basis: str | None = None
    verification: dict[str, Any] | None = None


class ProductionObjectIndexSynchronizer:
    """Synchronize by invoking the repository's deterministic index builder in check mode."""

    def __init__(self, root: str | Path):
        self.root = Path(root).resolve()
        self.builder = self.root / "05 SUPERAGENT" / "build_cmoc_object_index.py"
        self.index = self.root / "05 SUPERAGENT" / "cmoc_object_index.json"

    def _load_index(self) -> dict[str, Any]:
        return json.loads(self.index.read_text(encoding="utf-8"))

    def _find(self, object_id: str) -> list[dict[str, Any]]:
        return [
            r for r in self._load_index().get("records", [])
            if r.get("object_id") == object_id
        ]

    def synchronize(self, payload: dict[str, Any]) -> IndexSyncResult:
        required = (
            "status", "run_id", "source_id", "batch_id", "stage_id",
            "attempt_id", "result_id", "cmoc_write_id", "object_id",
            "provenance", "traceability", "write_verification",
        )
        missing = [key for key in required if not payload.get(key)]
        if missing:
            return IndexSyncResult("INDEX_REJECTED", basis=f"missing: {missing}")

        if payload["status"] != "CMOC_WRITE_ACCEPTED":
            return IndexSyncResult(
                "INDEX_REJECTED", basis="CMOC write is not authoritative"
            )
        if payload["stage_id"] != "C2_CMOC_WRITE":
            return IndexSyncResult("INDEX_REJECTED", basis="invalid predecessor stage")
        if payload["write_verification"] is not True:
            return IndexSyncResult("INDEX_REJECTED", basis="write verification missing")
        if not self.builder.exists() or not self.index.exists():
            return IndexSyncResult("INDEX_BUILD_FAILED", basis="production index artifacts unavailable")

        before = self.index.read_bytes()

        proc = subprocess.run(
            [sys.executable, str(self.builder), "--check"],
            cwd=self.root,
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            return IndexSyncResult(
                "INDEX_BUILD_FAILED",
                object_id=payload["object_id"],
                basis=proc.stderr.strip() or proc.stdout.strip(),
            )

        try:
            check = json.loads(proc.stdout)
        except json.JSONDecodeError:
            return IndexSyncResult(
                "INDEX_POST_BUILD_VERIFICATION_FAILED",
                object_id=payload["object_id"],
                basis="builder check returned non-JSON output",
            )

        after = self.index.read_bytes()
        if before != after:
            return IndexSyncResult(
                "INDEX_POST_BUILD_VERIFICATION_FAILED",
                object_id=payload["object_id"],
                basis="index changed during --check",
            )

        matches = self._find(payload["object_id"])
        if not matches:
            return IndexSyncResult(
                "INDEX_MISSING_OBJECT",
                object_id=payload["object_id"],
                basis="object_id absent from deterministic index",
                verification=check,
            )

        if any(
            not r.get("provenance") or not r.get("traceability")
            for r in matches
        ):
            return IndexSyncResult(
                "INDEX_POST_BUILD_VERIFICATION_FAILED",
                object_id=payload["object_id"],
                basis="derived record missing provenance or traceability",
                verification=check,
            )

        verification = {
            "builder_check": check,
            "representation_count": len(matches),
            "object_id_match": all(r.get("object_id") == payload["object_id"] for r in matches),
            "index_bytes_unchanged": True,
        }

        return IndexSyncResult(
            "ALREADY_SYNCHRONIZED",
            object_id=payload["object_id"],
            verification=verification,
        )
