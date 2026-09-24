#!/usr/bin/env python3
"""Minimal idempotent storage for ADMISSION artifacts."""
from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict


class AdmissionStoreError(ValueError):
    pass


class AdmissionStore:
    """Filesystem-backed MVP store: one JSON artifact per admission_id."""

    def __init__(self, root: str | Path):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def _path(self, admission_id: str) -> Path:
        if not admission_id or "/" in admission_id or "\\" in admission_id:
            raise AdmissionStoreError("INVALID_ADMISSION_ID")
        return self.root / f"{admission_id}.json"

    def write(self, admission: Dict[str, Any]) -> str:
        if not isinstance(admission, dict):
            raise AdmissionStoreError("ADMISSION_NOT_OBJECT")
        if admission.get("type") != "ADMISSION":
            raise AdmissionStoreError("ADMISSION_TYPE_MISMATCH")

        body = admission.get("admission")
        if not isinstance(body, dict):
            raise AdmissionStoreError("ADMISSION_BODY_MISSING")

        admission_id = body.get("admission_id")
        path = self._path(admission_id)

        payload = deepcopy(admission)
        encoded = json.dumps(
            payload, ensure_ascii=False, indent=2, sort_keys=True
        ) + "\n"

        if path.exists():
            existing = path.read_text(encoding="utf-8")
            if existing == encoded:
                return "ALREADY_PERSISTED"
            raise AdmissionStoreError("ADMISSION_WRITE_CONFLICT")

        path.write_text(encoded, encoding="utf-8")
        return "PERSISTED"

    def read(self, admission_id: str) -> Dict[str, Any]:
        path = self._path(admission_id)
        if not path.exists():
            raise AdmissionStoreError("ADMISSION_NOT_FOUND")
        return json.loads(path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    raise SystemExit("ADMISSION store is a library; use the acceptance test.")
