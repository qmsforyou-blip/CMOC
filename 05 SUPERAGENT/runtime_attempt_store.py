"""P3 runtime attempt identity and idempotency.

This component protects execution identity and authoritative-result uniqueness.
It does not perform semantic decisions, canonization, CMOC writes, or index writes.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass


@dataclass(frozen=True)
class AttemptRecord:
    run_id: str
    stage_id: str
    attempt_id: str
    result_id: str
    idempotency_key: str
    status: str
    authoritative_result: bool


class AttemptStore:
    """SQLite-backed P3 attempt identity/idempotency registry."""

    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS attempts (
                run_id TEXT NOT NULL,
                stage_id TEXT NOT NULL,
                attempt_id TEXT NOT NULL,
                result_id TEXT NOT NULL,
                idempotency_key TEXT NOT NULL,
                status TEXT NOT NULL,
                authoritative_result INTEGER NOT NULL,
                PRIMARY KEY (run_id, stage_id, attempt_id),
                UNIQUE (run_id, stage_id, idempotency_key)
            );
            """
        )
        self.conn.commit()

    def close(self):
        self.conn.close()

    def register(
        self,
        run_id: str,
        stage_id: str,
        attempt_id: str,
        result_id: str,
        idempotency_key: str,
        status: str = "IN_PROGRESS",
        authoritative_result: bool = False,
    ) -> str:
        if not all([run_id, stage_id, attempt_id, result_id, idempotency_key]):
            raise ValueError("attempt identity fields are required")

        existing = self.conn.execute(
            """
            SELECT * FROM attempts
            WHERE run_id=? AND stage_id=? AND attempt_id=?
            """,
            (run_id, stage_id, attempt_id),
        ).fetchone()

        if existing:
            if existing["idempotency_key"] != idempotency_key:
                return "IDEMPOTENCY_KEY_MISMATCH"
            if existing["result_id"] != result_id:
                return "CONFLICTING_ATTEMPT"
            if existing["authoritative_result"]:
                return "ALREADY_COMPLETED"
            if existing["status"] == "IN_PROGRESS":
                return "IN_PROGRESS"
            return "DUPLICATE_ATTEMPT"

        key_owner = self.conn.execute(
            """
            SELECT * FROM attempts
            WHERE run_id=? AND stage_id=? AND idempotency_key=?
            """,
            (run_id, stage_id, idempotency_key),
        ).fetchone()

        if key_owner:
            if key_owner["attempt_id"] != attempt_id:
                return "IDEMPOTENCY_KEY_CONFLICT"
            return "DUPLICATE_ATTEMPT"

        self.conn.execute(
            """
            INSERT INTO attempts
            (run_id,stage_id,attempt_id,result_id,idempotency_key,status,authoritative_result)
            VALUES (?,?,?,?,?,?,?)
            """,
            (
                run_id, stage_id, attempt_id, result_id,
                idempotency_key, status, int(authoritative_result),
            ),
        )
        self.conn.commit()
        return "ACCEPTED"

    def mark_failed(self, run_id: str, stage_id: str,
                    attempt_id: str) -> str:
        row = self.conn.execute(
            """
            SELECT * FROM attempts
            WHERE run_id=? AND stage_id=? AND attempt_id=?
            """,
            (run_id, stage_id, attempt_id),
        ).fetchone()

        if not row:
            return "ATTEMPT_NOT_FOUND"
        if row["authoritative_result"]:
            return "ALREADY_COMPLETED"
        if row["status"] == "FAILED":
            return "ALREADY_FAILED"

        self.conn.execute(
            """
            UPDATE attempts
            SET status='FAILED', authoritative_result=0
            WHERE run_id=? AND stage_id=? AND attempt_id=?
            """,
            (run_id, stage_id, attempt_id),
        )
        self.conn.commit()
        return "FAILED_RECORDED"

    def mark_authoritative(self, run_id: str, stage_id: str,
                           attempt_id: str) -> str:
        row = self.conn.execute(
            """
            SELECT * FROM attempts
            WHERE run_id=? AND stage_id=? AND attempt_id=?
            """,
            (run_id, stage_id, attempt_id),
        ).fetchone()

        if not row:
            return "ATTEMPT_NOT_FOUND"

        if row["authoritative_result"]:
            return "ALREADY_COMPLETED"

        self.conn.execute(
            """
            UPDATE attempts
            SET status='COMPLETED', authoritative_result=1
            WHERE run_id=? AND stage_id=? AND attempt_id=?
            """,
            (run_id, stage_id, attempt_id),
        )
        self.conn.commit()
        return "COMMITTED"

    def get(self, run_id: str, stage_id: str,
            attempt_id: str) -> AttemptRecord | None:
        row = self.conn.execute(
            """
            SELECT * FROM attempts
            WHERE run_id=? AND stage_id=? AND attempt_id=?
            """,
            (run_id, stage_id, attempt_id),
        ).fetchone()
        if not row:
            return None
        return AttemptRecord(
            row["run_id"], row["stage_id"], row["attempt_id"],
            row["result_id"], row["idempotency_key"], row["status"],
            bool(row["authoritative_result"]),
        )

    def list_run(self, run_id: str) -> list[AttemptRecord]:
        rows = self.conn.execute(
            "SELECT * FROM attempts WHERE run_id=? ORDER BY stage_id, attempt_id",
            (run_id,),
        ).fetchall()
        return [
            AttemptRecord(
                r["run_id"], r["stage_id"], r["attempt_id"], r["result_id"],
                r["idempotency_key"], r["status"], bool(r["authoritative_result"]),
            )
            for r in rows
        ]
