"""Durable P1/P2 runtime persistence for the single-host baseline.

This module implements only execution history and operational state.
It does not implement semantic decisions, CMOC writes, or OBJECT INDEX writes.
"""

from __future__ import annotations

import sqlite3
from dataclasses import asdict, dataclass
from datetime import datetime, timezone


EVENT_TYPES = {
    "RUN_CREATED", "STAGE_STARTED", "STAGE_COMPLETED", "STAGE_REJECTED",
    "STAGE_FAILED", "RECOVERY_REQUESTED", "RETRY_REQUIRED", "RESUME_ALLOWED",
    "RESUME_BLOCKED", "RUN_COMPLETED", "RUN_REJECTED", "RUN_FAILED",
    "RUN_INCOMPLETE",
}
TERMINAL_STAGE_EVENTS = {
    "STAGE_COMPLETED": "COMPLETED",
    "STAGE_REJECTED": "REJECTED",
    "STAGE_FAILED": "FAILED",
}
RUN_TERMINAL = {"RUN_COMPLETED", "RUN_REJECTED", "RUN_FAILED"}
RECOVERY_EVENTS = {
    "RUN_INCOMPLETE", "RECOVERY_REQUESTED", "RETRY_REQUIRED",
    "RESUME_ALLOWED", "RESUME_BLOCKED",
}


@dataclass(frozen=True)
class JournalEvent:
    run_id: str
    event_id: str
    event_seq: int
    stage_id: str | None
    event_type: str
    stage_result_id: str | None
    attempt_id: str | None
    event_status: str
    traceability: str
    source_id: str | None = None
    batch_id: str | None = None


@dataclass(frozen=True)
class RunState:
    run_id: str
    source_id: str | None
    batch_id: str | None
    run_status: str
    current_stage_id: str | None
    current_stage_result_id: str | None
    current_attempt_id: str | None
    last_event_seq: int
    state_version: str
    traceability: str


class RuntimeStateStore:
    """SQLite-backed append-only journal plus P2 operational projection."""

    STATE_VERSION = "P2.1"

    def __init__(self, db_path: str):
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")
        self._init_schema()

    def close(self):
        self.conn.close()

    def _init_schema(self):
        self.conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS journal_events (
                run_id TEXT NOT NULL,
                event_id TEXT NOT NULL UNIQUE,
                event_seq INTEGER NOT NULL,
                timestamp TEXT NOT NULL,
                stage_id TEXT,
                event_type TEXT NOT NULL,
                stage_result_id TEXT,
                attempt_id TEXT,
                event_status TEXT NOT NULL,
                traceability TEXT NOT NULL,
                source_id TEXT,
                batch_id TEXT,
                PRIMARY KEY (run_id, event_seq)
            );
            CREATE TABLE IF NOT EXISTS run_state (
                run_id TEXT PRIMARY KEY,
                source_id TEXT,
                batch_id TEXT,
                run_status TEXT NOT NULL,
                current_stage_id TEXT,
                current_stage_result_id TEXT,
                current_attempt_id TEXT,
                last_event_seq INTEGER NOT NULL,
                state_version TEXT NOT NULL,
                traceability TEXT NOT NULL
            );
            """
        )
        self.conn.commit()

    def append(self, event: JournalEvent, source_id: str | None = None,
               batch_id: str | None = None) -> RunState:
        self._validate_event(event)
        source_id = source_id if source_id is not None else event.source_id
        batch_id = batch_id if batch_id is not None else event.batch_id

        with self.conn:
            latest = self.conn.execute(
                "SELECT event_seq FROM journal_events "
                "WHERE run_id = ? ORDER BY event_seq DESC LIMIT 1",
                (event.run_id,),
            ).fetchone()
            if latest and event.event_seq <= latest["event_seq"]:
                raise ValueError("EVENT_SEQ must be strictly monotonic within RUN_ID")

            if self.conn.execute(
                "SELECT 1 FROM journal_events WHERE event_id = ?",
                (event.event_id,),
            ).fetchone():
                raise ValueError("duplicate EVENT_ID")

            if event.event_type == "RUN_CREATED" and self._load_state(event.run_id):
                raise ValueError("RUN_ID already exists")

            previous = self._load_state(event.run_id)
            next_state = self._reduce_event(
                previous, event, source_id=source_id, batch_id=batch_id
            )

            self.conn.execute(
                """
                INSERT INTO journal_events
                (run_id,event_id,event_seq,timestamp,stage_id,event_type,
                 stage_result_id,attempt_id,event_status,traceability,
                 source_id,batch_id)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    event.run_id, event.event_id, event.event_seq,
                    datetime.now(timezone.utc).isoformat(),
                    event.stage_id, event.event_type, event.stage_result_id,
                    event.attempt_id, event.event_status, event.traceability,
                    source_id, batch_id,
                ),
            )
            self._persist_state(next_state)
            return next_state

    def _validate_event(self, event: JournalEvent):
        if not event.run_id or not event.event_id:
            raise ValueError("RUN_ID and EVENT_ID are required")
        if event.event_seq < 1:
            raise ValueError("EVENT_SEQ must be positive")
        if event.event_type not in EVENT_TYPES:
            raise ValueError("unknown EVENT_TYPE")
        if not event.traceability:
            raise ValueError("TRACEABILITY is required")

    def _load_state(self, run_id: str) -> RunState | None:
        row = self.conn.execute(
            "SELECT * FROM run_state WHERE run_id = ?", (run_id,)
        ).fetchone()
        if not row:
            return None
        return RunState(
            row["run_id"], row["source_id"], row["batch_id"],
            row["run_status"], row["current_stage_id"],
            row["current_stage_result_id"], row["current_attempt_id"],
            row["last_event_seq"], row["state_version"], row["traceability"],
        )

    def _reduce_event(self, previous: RunState | None, event: JournalEvent,
                      source_id: str | None, batch_id: str | None) -> RunState:
        if previous is None:
            if event.event_type != "RUN_CREATED":
                raise ValueError("RUN must start with RUN_CREATED")
            return RunState(
                event.run_id, source_id, batch_id, "ACTIVE",
                None, None, event.attempt_id, event.event_seq,
                self.STATE_VERSION, event.traceability,
            )

        if event.event_type == "RUN_CREATED":
            raise ValueError("RUN_CREATED cannot repeat")
        if previous.run_status in RUN_TERMINAL and event.event_type not in RECOVERY_EVENTS:
            raise ValueError("terminal RUN cannot receive another event")

        current_stage = previous.current_stage_id
        current_result = previous.current_stage_result_id
        current_attempt = previous.current_attempt_id
        run_status = previous.run_status

        if event.source_id is not None and event.source_id != previous.source_id:
            raise ValueError("SOURCE_ID crosses RUN boundary")
        if event.batch_id is not None and event.batch_id != previous.batch_id:
            raise ValueError("BATCH_ID crosses RUN boundary")

        if event.event_type == "STAGE_STARTED":
            if not event.stage_id or not event.attempt_id:
                raise ValueError("STAGE_STARTED requires stage_id and attempt_id")
            current_stage = event.stage_id
            current_result = event.stage_result_id
            current_attempt = event.attempt_id
        elif event.event_type in TERMINAL_STAGE_EVENTS:
            if not event.stage_id or not event.attempt_id:
                raise ValueError("stage terminal event requires stage_id and attempt_id")
            if current_stage and event.stage_id != current_stage:
                raise ValueError("stage transition crosses current stage")
            current_stage = event.stage_id
            current_result = event.stage_result_id
            current_attempt = event.attempt_id
        elif event.event_type in {
            "RECOVERY_REQUESTED", "RETRY_REQUIRED",
            "RESUME_ALLOWED", "RESUME_BLOCKED",
        }:
            if event.stage_id and current_stage and event.stage_id != current_stage:
                raise ValueError("recovery event crosses current stage")
            if event.attempt_id:
                current_attempt = event.attempt_id
        elif event.event_type == "RUN_INCOMPLETE":
            run_status = "INCOMPLETE"
        elif event.event_type in RUN_TERMINAL:
            run_status = {
                "RUN_COMPLETED": "COMPLETED",
                "RUN_REJECTED": "REJECTED",
                "RUN_FAILED": "FAILED",
            }[event.event_type]

        return RunState(
            previous.run_id, previous.source_id, previous.batch_id,
            run_status, current_stage, current_result, current_attempt,
            event.event_seq, self.STATE_VERSION, event.traceability,
        )

    def _persist_state(self, state: RunState):
        values = (
            state.run_id, state.source_id, state.batch_id, state.run_status,
            state.current_stage_id, state.current_stage_result_id,
            state.current_attempt_id, state.last_event_seq,
            state.state_version, state.traceability,
        )
        self.conn.execute(
            """
            INSERT INTO run_state
            (run_id,source_id,batch_id,run_status,current_stage_id,
             current_stage_result_id,current_attempt_id,last_event_seq,
             state_version,traceability)
            VALUES (?,?,?,?,?,?,?,?,?,?)
            ON CONFLICT(run_id) DO UPDATE SET
              source_id=excluded.source_id,
              batch_id=excluded.batch_id,
              run_status=excluded.run_status,
              current_stage_id=excluded.current_stage_id,
              current_stage_result_id=excluded.current_stage_result_id,
              current_attempt_id=excluded.current_attempt_id,
              last_event_seq=excluded.last_event_seq,
              state_version=excluded.state_version,
              traceability=excluded.traceability
            """,
            values,
        )

    def get_state(self, run_id: str) -> RunState | None:
        return self._load_state(run_id)

    def next_event_seq(self, run_id: str) -> int:
        state = self._load_state(run_id)
        return 1 if state is None else state.last_event_seq + 1

    def read_journal(self, run_id: str) -> list[JournalEvent]:
        rows = self.conn.execute(
            "SELECT * FROM journal_events WHERE run_id = ? ORDER BY event_seq",
            (run_id,),
        ).fetchall()
        return [
            JournalEvent(
                r["run_id"], r["event_id"], r["event_seq"], r["stage_id"],
                r["event_type"], r["stage_result_id"], r["attempt_id"],
                r["event_status"], r["traceability"],
                r["source_id"], r["batch_id"],
            )
            for r in rows
        ]

    def reconstruct_state(self, run_id: str) -> RunState | None:
        events = self.read_journal(run_id)
        state = None
        for event in events:
            state = self._reduce_event(
                state, event, source_id=event.source_id, batch_id=event.batch_id
            )
        return state

    def verify_projection(self, run_id: str) -> bool:
        return self.get_state(run_id) == self.reconstruct_state(run_id)

    def export_state(self, run_id: str) -> dict | None:
        state = self.get_state(run_id)
        return asdict(state) if state else None
