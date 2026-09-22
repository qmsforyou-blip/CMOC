"""P4 restart/resume runtime boundary.

Reads durable P1/P2/P3 state and determines whether an interrupted execution
may resume or must remain blocked/retried. No semantic repair is performed.
"""

from __future__ import annotations

from dataclasses import dataclass

from runtime_state_store import RuntimeStateStore


@dataclass(frozen=True)
class ResumeDecision:
    status: str
    run_id: str
    stage_id: str | None
    attempt_id: str | None
    reason: str


class RestartResumeController:
    def __init__(self, state_store: RuntimeStateStore, attempt_store):
        self.state_store = state_store
        self.attempt_store = attempt_store

    def inspect(self, run_id: str) -> ResumeDecision:
        state = self.state_store.get_state(run_id)
        if state is None:
            return ResumeDecision(
                "RUN_REJECTED", run_id, None, None, "RUN_ID not found"
            )

        if not self.state_store.verify_projection(run_id):
            return ResumeDecision(
                "INCONSISTENT_HISTORY", run_id,
                state.current_stage_id, state.current_attempt_id,
                "journal and persisted state projection differ",
            )

        if state.run_status in {"COMPLETED", "REJECTED", "FAILED"}:
            return ResumeDecision(
                "ALREADY_COMPLETED", run_id,
                state.current_stage_id, state.current_attempt_id,
                "terminal RUN is protected",
            )

        stage_id = state.current_stage_id
        attempt_id = state.current_attempt_id

        if not stage_id or not attempt_id:
            return ResumeDecision(
                "RESUME_BLOCKED", run_id, stage_id, attempt_id,
                "no identifiable interrupted stage/attempt",
            )

        attempt = self.attempt_store.get(
            run_id, stage_id, attempt_id
        )
        if attempt is None:
            return ResumeDecision(
                "RECOVERY_REQUIRES_REVIEW", run_id,
                stage_id, attempt_id,
                "attempt identity not found",
            )

        if attempt.authoritative_result:
            return ResumeDecision(
                "ALREADY_COMPLETED", run_id,
                stage_id, attempt_id,
                "authoritative attempt result already exists",
            )

        if attempt.status == "FAILED":
            return ResumeDecision(
                "RETRY_REQUIRED", run_id,
                stage_id, attempt_id,
                "failed attempt requires explicit retry",
            )

        if attempt.status == "IN_PROGRESS":
            return ResumeDecision(
                "RESUME_ALLOWED", run_id,
                stage_id, attempt_id,
                "interrupted attempt remains identifiable and non-authoritative",
            )

        return ResumeDecision(
            "RECOVERY_REQUIRES_REVIEW", run_id,
            stage_id, attempt_id,
            "attempt state is not safely resumable",
        )
