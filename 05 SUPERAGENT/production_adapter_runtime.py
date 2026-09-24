"""P6 runtime production-adapter boundary.

Connects runtime execution to already-established stage implementations without
moving semantic responsibility into the adapter layer.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True)
class AdapterResult:
    status: str
    payload: dict[str, Any]


@dataclass(frozen=True)
class ProductionAdapter:
    stage_id: str
    implementation: Callable[[dict[str, Any]], dict[str, Any]]
    mode: str = "production"

    def invoke(self, envelope: dict[str, Any],
               persistence: dict[tuple[str, str, str], dict[str, Any]]) -> AdapterResult:
        required = (
            "run_id", "source_id", "batch_id",
            "stage_id", "attempt_id", "result_id"
        )
        missing = [key for key in required if not envelope.get(key)]
        if missing:
            return AdapterResult(
                "ADAPTER_INPUT_REJECTED", {"missing": missing}
            )

        if self.mode != "production":
            return AdapterResult("SYNTHETIC_ADAPTER_DETECTED", {})

        if envelope["stage_id"] != self.stage_id:
            return AdapterResult(
                "ADAPTER_INPUT_REJECTED",
                {"basis": "stage mismatch"},
            )

        key = (
            envelope["run_id"],
            envelope["stage_id"],
            envelope["attempt_id"],
        )
        if key in persistence:
            stored = persistence[key]
            if stored.get("result_id") == envelope["result_id"]:
                return AdapterResult(
                    "ALREADY_COMPLETED",
                    {"result": stored},
                )
            return AdapterResult(
                "ADAPTER_OUTPUT_INVALID",
                {"basis": "authoritative result conflict"},
            )

        try:
            output = self.implementation(dict(envelope))
        except Exception as exc:
            return AdapterResult(
                "ADAPTER_EXECUTION_FAILED",
                {
                    "error_type": type(exc).__name__,
                    "error_message": str(exc)[:1000],
                },
            )

        if not isinstance(output, dict):
            return AdapterResult("ADAPTER_OUTPUT_INVALID", {})

        lineage_fields = (
            "run_id", "source_id", "batch_id",
            "stage_id", "attempt_id", "result_id"
        )
        for field in lineage_fields:
            if output.get(field) != envelope[field]:
                return AdapterResult(
                    "ADAPTER_LINEAGE_INVALID",
                    {"field": field},
                )

        persistence[key] = dict(output)
        return AdapterResult("PRODUCTION_ADAPTER_ACCEPTED", {"result": output})


class ProductionAdapterRegistry:
    """Explicit stage-to-production-adapter registry."""

    def __init__(self):
        self._adapters: dict[str, ProductionAdapter] = {}

    def register(self, adapter: ProductionAdapter) -> None:
        if adapter.mode != "production":
            raise ValueError("only production adapters may be registered")
        self._adapters[adapter.stage_id] = adapter

    def get(self, stage_id: str) -> ProductionAdapter | None:
        return self._adapters.get(stage_id)

    def invoke(self, envelope: dict[str, Any],
               persistence: dict[tuple[str, str, str], dict[str, Any]]) -> AdapterResult:
        adapter = self.get(envelope.get("stage_id", ""))
        if adapter is None:
            return AdapterResult(
                "PRODUCTION_ADAPTER_UNAVAILABLE",
                {"stage_id": envelope.get("stage_id")},
            )
        return adapter.invoke(envelope, persistence)
