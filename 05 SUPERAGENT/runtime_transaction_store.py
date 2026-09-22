"""P5 runtime transaction/concurrency boundary.

SQLite-backed execution ownership and authoritative-result guard.
This component protects execution identity and commit state only.
It does not perform semantic decisions, canonization, CMOC writes, or index writes.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass


@dataclass(frozen=True)
class ExecutionRecord:
    run_id: str
    stage_id: str
    attempt_id: str
    result_id: str
    idempotency_key: str
    owner_id: str
    status: str
    committed: bool
    effect_count: int


class TransactionStore:
    """SQLite-backed P5 execution boundary.

    SQLite transactions provide the local single-host atomicity boundary.
    Cross-process callers should use separate connections to the same DB.
    """

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path, timeout=5.0)
        self.conn.row_factory = sqlite3.Row
        self.conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS executions (
                run_id TEXT NOT NULL,
                stage_id TEXT NOT NULL,
                attempt_id TEXT NOT NULL,
                result_id TEXT NOT NULL,
                idempotency_key TEXT NOT NULL,
                owner_id TEXT NOT NULL,
                status TEXT NOT NULL,
                committed INTEGER NOT NULL DEFAULT 0,
                effect_count INTEGER NOT NULL DEFAULT 0,
                PRIMARY KEY (run_id, stage_id, attempt_id),
                UNIQUE (run_id, stage_id, idempotency_key)
            );
            """
        )
        self.conn.commit()

    def close(self):
        self.conn.close()

    def acquire(
        self,
        run_id: str,
        stage_id: str,
        attempt_id: str,
        result_id: str,
        idempotency_key: str,
        owner_id: str,
    ) -> str:
        if not all([run_id, stage_id, attempt_id, result_id,
                    idempotency_key, owner_id]):
            raise ValueError("execution identity fields are required")

        try:
            self.conn.execute("BEGIN IMMEDIATE")
            row = self.conn.execute(
                """SELECT * FROM executions
                   WHERE run_id=? AND stage_id=? AND attempt_id=?""",
                (run_id, stage_id, attempt_id),
            ).fetchone()

            if row:
                if row["committed"]:
                    self.conn.commit()
                    return "ALREADY_COMPLETED"
                if row["owner_id"] != owner_id:
                    self.conn.commit()
                    return "IN_PROGRESS"
                if row["result_id"] != result_id:
                    self.conn.commit()
                    return "CONFLICTING_RESULT"
                self.conn.commit()
                return "LOCK_ACQUIRED"

            key_owner = self.conn.execute(
                """SELECT * FROM executions
                   WHERE run_id=? AND stage_id=? AND idempotency_key=?""",
                (run_id, stage_id, idempotency_key),
            ).fetchone()
            if key_owner:
                self.conn.commit()
                return "IDEMPOTENCY_CONFLICT"

            self.conn.execute(
                """INSERT INTO executions
                   (run_id,stage_id,attempt_id,result_id,idempotency_key,
                    owner_id,status,committed,effect_count)
                   VALUES (?,?,?,?,?,?,?,0,0)""",
                (run_id, stage_id, attempt_id, result_id,
                 idempotency_key, owner_id, "IN_PROGRESS"),
            )
            self.conn.commit()
            return "LOCK_ACQUIRED"
        except sqlite3.Error:
            self.conn.rollback()
            raise

    def commit(self, run_id: str, stage_id: str, attempt_id: str,
               owner_id: str, result_id: str) -> str:
        try:
            self.conn.execute("BEGIN IMMEDIATE")
            row = self.conn.execute(
                """SELECT * FROM executions
                   WHERE run_id=? AND stage_id=? AND attempt_id=?""",
                (run_id, stage_id, attempt_id),
            ).fetchone()
            if not row:
                self.conn.rollback()
                return "TRANSACTION_REJECTED"
            if row["owner_id"] != owner_id:
                self.conn.rollback()
                return "TRANSACTION_REJECTED"
            if row["committed"]:
                self.conn.commit()
                return "ALREADY_COMPLETED"
            if row["result_id"] != result_id:
                self.conn.rollback()
                return "CONFLICTING_RESULT"

            self.conn.execute(
                """UPDATE executions
                   SET status='COMMITTED', committed=1, effect_count=effect_count+1
                   WHERE run_id=? AND stage_id=? AND attempt_id=?""",
                (run_id, stage_id, attempt_id),
            )
            self.conn.commit()
            return "COMMITTED"
        except sqlite3.Error:
            self.conn.rollback()
            raise

    def rollback(self, run_id: str, stage_id: str, attempt_id: str,
                 owner_id: str) -> str:
        try:
            self.conn.execute("BEGIN IMMEDIATE")
            row = self.conn.execute(
                """SELECT * FROM executions
                   WHERE run_id=? AND stage_id=? AND attempt_id=?""",
                (run_id, stage_id, attempt_id),
            ).fetchone()
            if not row or row["owner_id"] != owner_id:
                self.conn.rollback()
                return "TRANSACTION_REJECTED"
            if row["committed"]:
                self.conn.rollback()
                return "TRANSACTION_REJECTED"

            self.conn.execute(
                """UPDATE executions
                   SET status='ROLLED_BACK', owner_id=''
                   WHERE run_id=? AND stage_id=? AND attempt_id=?""",
                (run_id, stage_id, attempt_id),
            )
            self.conn.commit()
            return "TRANSACTION_ROLLBACK"
        except sqlite3.Error:
            self.conn.rollback()
            raise

    def get(self, run_id: str, stage_id: str,
            attempt_id: str) -> ExecutionRecord | None:
        row = self.conn.execute(
            """SELECT * FROM executions
               WHERE run_id=? AND stage_id=? AND attempt_id=?""",
            (run_id, stage_id, attempt_id),
        ).fetchone()
        if not row:
            return None
        return ExecutionRecord(
            row["run_id"], row["stage_id"], row["attempt_id"],
            row["result_id"], row["idempotency_key"], row["owner_id"],
            row["status"], bool(row["committed"]), row["effect_count"],
        )
