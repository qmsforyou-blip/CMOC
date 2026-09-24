"""Durable production-adapter result persistence.

Stores adapter outputs in the same local SQLite runtime database so a
process restart does not erase completed attempt results.
"""

from __future__ import annotations

import json
import sqlite3
from typing import Any


class DurableAdapterPersistence:
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS adapter_results (
                run_id TEXT NOT NULL,
                stage_id TEXT NOT NULL,
                attempt_id TEXT NOT NULL,
                result_id TEXT NOT NULL,
                payload_json TEXT NOT NULL,
                PRIMARY KEY (run_id, stage_id, attempt_id)
            )
            """
        )
        self.conn.commit()

    def __contains__(self, key: tuple[str, str, str]) -> bool:
        return self._load(key) is not None

    def __getitem__(self, key: tuple[str, str, str]) -> dict[str, Any]:
        value = self._load(key)
        if value is None:
            raise KeyError(key)
        return value

    def __setitem__(
        self, key: tuple[str, str, str], value: dict[str, Any]
    ) -> None:
        run_id, stage_id, attempt_id = key
        self.conn.execute(
            """
            INSERT INTO adapter_results
            (run_id, stage_id, attempt_id, result_id, payload_json)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                run_id,
                stage_id,
                attempt_id,
                value["result_id"],
                json.dumps(value, ensure_ascii=False, sort_keys=True),
            ),
        )
        self.conn.commit()

    def _load(
        self, key: tuple[str, str, str]
    ) -> dict[str, Any] | None:
        row = self.conn.execute(
            """
            SELECT payload_json
            FROM adapter_results
            WHERE run_id = ? AND stage_id = ? AND attempt_id = ?
            """,
            key,
        ).fetchone()
        if row is None:
            return None
        return json.loads(row[0])
