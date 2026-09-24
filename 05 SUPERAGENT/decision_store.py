#!/usr/bin/env python3
"""Minimal idempotent storage for DECISION-CONTRACT-001 artifacts."""
from __future__ import annotations

import json
from copy import deepcopy
from pathlib import Path
from typing import Any, Dict


class DecisionStoreError(ValueError):
    pass


class DecisionStore:
    """Filesystem-backed MVP store: one JSON artifact per decision_id."""

    def __init__(self, root: str | Path):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def _path(self, decision_id: str) -> Path:
        if not decision_id or "/" in decision_id or "\\" in decision_id:
            raise DecisionStoreError("INVALID_DECISION_ID")
        return self.root / f"{decision_id}.json"

    def write(self, decision: Dict[str, Any]) -> str:
        if not isinstance(decision, dict):
            raise DecisionStoreError("DECISION_NOT_OBJECT")
        if decision.get("type") != "DECISION":
            raise DecisionStoreError("DECISION_TYPE_MISMATCH")
        body = decision.get("decision")
        if not isinstance(body, dict):
            raise DecisionStoreError("DECISION_BODY_MISSING")

        decision_id = body.get("decision_id")
        path = self._path(decision_id)

        payload = deepcopy(decision)
        encoded = json.dumps(
            payload, ensure_ascii=False, indent=2, sort_keys=True
        ) + "\n"

        if path.exists():
            existing = path.read_text(encoding="utf-8")
            if existing == encoded:
                return "ALREADY_PERSISTED"
            raise DecisionStoreError("DECISION_WRITE_CONFLICT")

        path.write_text(encoded, encoding="utf-8")
        return "PERSISTED"

    def read(self, decision_id: str) -> Dict[str, Any]:
        path = self._path(decision_id)
        if not path.exists():
            raise DecisionStoreError("DECISION_NOT_FOUND")
        return json.loads(path.read_text(encoding="utf-8"))
