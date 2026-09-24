"""DISCOVERY_RESULT aggregation for MACHINE-SOURCE-001.

The builder aggregates addresses and lineage of the completed M01-M08
Discovery pass. It does not duplicate semantic records and has no CMOC,
OBJECT INDEX, or QUERY responsibility.
"""

from __future__ import annotations

from typing import Any, Iterable


TASKS = ("M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08")


def build_discovery_result(
    *,
    run_id: str,
    source: dict[str, Any],
    results: Iterable[dict[str, Any]],
) -> dict[str, Any]:
    """Build one source-bound aggregate for a complete M01-M08 pass."""
    results = list(results)

    if not run_id:
        raise ValueError("DISCOVERY_RESULT requires run_id")

    source_id = source.get("source_id")
    package_id = source.get("package_id")
    if not source_id or not package_id:
        raise ValueError(
            "DISCOVERY_RESULT requires source_id and package_id"
        )

    if len(results) != len(TASKS):
        raise ValueError(
            f"DISCOVERY_RESULT requires all {len(TASKS)} M01-M08 outputs"
        )

    outputs: dict[str, dict[str, str]] = {}
    for task, result in zip(TASKS, results):
        if result.get("status") != "ACCEPT":
            raise ValueError(
                f"DISCOVERY_RESULT cannot aggregate {task}: "
                f"status={result.get('status')}"
            )
        for field in ("batch_id", "ref"):
            if not result.get(field):
                raise ValueError(
                    f"DISCOVERY_RESULT {task} missing {field}"
                )

        outputs[task] = {
            "ref": result["ref"],
            "batch_id": result["batch_id"],
        }

    discovery_id = f"DISCOVERY-RESULT-{source_id}-{run_id}"

    return {
        "discovery_result": {
            "discovery_id": discovery_id,
            "source_id": source_id,
            "source_package_id": package_id,
            "run_id": run_id,
            "status": "ACCEPT",
            "outputs": outputs,
            "traceability": {
                "source_id": source_id,
                "source_package_id": package_id,
                "run_id": run_id,
            },
            "boundary": {
                "origin": "SOURCE_BOUND",
                "reconciliation": "NOT_PERFORMED",
            },
        }
    }
