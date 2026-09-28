"""Production MACHINE-SOURCE-001 implementation.

This module owns only Discovery orchestration: SOURCE_PACKAGE -> M01..M08.
Semantic work remains in the existing production M01..M08 implementations.
"""

from __future__ import annotations

from typing import Any

from mvp_runner import Batch, Contract, Superagent
from m01_integration import build_m01_handler
from m02_llm import extract_distinctions
from m03_llm import formulate
from m04_llm import select_nomenclature
from m05_llm import classify
from m06_llm import build_passports
from m07_llm import build_relation_candidates
from m08_llm import decide
from discovery_result import build_discovery_result


TASKS = ("M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08")


class MachineSource001Superagent(Superagent):
    """Production Discovery orchestrator with deterministic batch IDs."""

    def __init__(self):
        super().__init__(CONTRACTS, HANDLERS, MACHINE_IDS)
        self._production_seq = 0

    def new_batch(
        self,
        source_id: str,
        task: str,
        input_ref: str,
        handoff_id: str | None = None,
    ) -> Batch:
        self._production_seq += 1
        batch_id = f"BATCH-{source_id}-{task}-{self._production_seq:03d}"
        batch = Batch(batch_id, source_id, task, input_ref, handoff_id)
        self.batches.append(batch)
        return batch


def _wrap_output(
    batch: Batch,
    output_type: str,
    records: list[dict[str, Any]],
    upstream: dict[str, Any],
    **extra: Any,
) -> dict[str, Any]:
    return {
        "status": "ACCEPT",
        "type": output_type,
        "source_id": batch.source_id,
        "batch_id": batch.batch_id,
        "records": records,
        "traceability": {
            "source_id": batch.source_id,
            "batch_id": batch.batch_id,
            "source_package": upstream.get("traceability", {}).get(
                "source_package", upstream.get("package_id")
            ),
            "upstream_batch": upstream.get("batch_id"),
        },
        "ref": f"{batch.batch_id}:OUTPUT",
        **extra,
    }


def _m01(inp: dict[str, Any], batch: Batch) -> dict[str, Any]:
    records = build_m01_handler()(inp, batch)["records"]
    return _wrap_output(batch, "EXTRACTION_RECORDS", records, inp)


def _m02(inp: dict[str, Any], batch: Batch) -> dict[str, Any]:
    return _wrap_output(
        batch, "DISTINCTION_RECORDS", extract_distinctions(inp), inp
    )


def _m03(inp: dict[str, Any], batch: Batch) -> dict[str, Any]:
    return _wrap_output(
        batch, "FORMULATION_RECORDS", formulate(inp), inp
    )


def _m04(inp: dict[str, Any], batch: Batch) -> dict[str, Any]:
    return _wrap_output(
        batch, "NOMENCLATURE_CANDIDATES", select_nomenclature(inp), inp
    )


def _m05(inp: dict[str, Any], batch: Batch) -> dict[str, Any]:
    return _wrap_output(
        batch, "CLASSIFICATION_RECORDS", classify(inp["records"]), inp
    )


def _m06(inp: dict[str, Any], batch: Batch) -> dict[str, Any]:
    return _wrap_output(
        batch, "PASSPORT_RECORDS", build_passports(inp["records"]), inp
    )


def _m07(inp: dict[str, Any], batch: Batch) -> dict[str, Any]:
    records = build_relation_candidates(inp["records"], [])
    return _wrap_output(
        batch,
        "RELATION_CANDIDATES",
        records,
        inp,
        passports=inp["records"],
        evaluated_passport_ids=[p["id"] for p in inp["records"]],
        relation_evidence=[],
    )


def _m08(inp: dict[str, Any], batch: Batch) -> dict[str, Any]:
    decision_output = decide(
        inp["passports"],
        inp["records"],
        inp.get("relation_evidence", []),
    )
    return _wrap_output(
        batch,
        "DECISION_RECORDS",
        decision_output.get("records", []),
        inp,
        upstream_m07_batch=inp.get("batch_id"),
    )


CONTRACTS = {
    "M01": Contract(
        "M01", {"SOURCE_PACKAGE"}, "EXTRACTION_RECORDS",
        {"source_id", "batch_id", "records", "traceability", "ref"},
        {"source_package"},
    ),
    "M02": Contract(
        "M02", {"EXTRACTION_RECORDS"}, "DISTINCTION_RECORDS",
        {"source_id", "batch_id", "records", "traceability", "ref"},
        {"records"},
    ),
    "M03": Contract(
        "M03", {"DISTINCTION_RECORDS"}, "FORMULATION_RECORDS",
        {"source_id", "batch_id", "records", "traceability", "ref"},
        {"records"},
    ),
    "M04": Contract(
        "M04", {"FORMULATION_RECORDS"}, "NOMENCLATURE_CANDIDATES",
        {"source_id", "batch_id", "records", "traceability", "ref"},
        {"records"},
    ),
    "M05": Contract(
        "M05", {"NOMENCLATURE_CANDIDATES"}, "CLASSIFICATION_RECORDS",
        {"source_id", "batch_id", "records", "traceability", "ref"},
        {"records"},
    ),
    "M06": Contract(
        "M06", {"CLASSIFICATION_RECORDS"}, "PASSPORT_RECORDS",
        {"source_id", "batch_id", "records", "traceability", "ref"},
        {"records"},
    ),
    "M07": Contract(
        "M07", {"PASSPORT_RECORDS"}, "RELATION_CANDIDATES",
        {"source_id", "batch_id", "records", "traceability", "ref"},
        {"records"},
    ),
    "M08": Contract(
        "M08", {"RELATION_CANDIDATES"}, "DECISION_RECORDS",
        {"source_id", "batch_id", "records", "traceability", "ref"},
        {"records"},
    ),
}

HANDLERS = {
    "M01": _m01,
    "M02": _m02,
    "M03": _m03,
    "M04": _m04,
    "M05": _m05,
    "M06": _m06,
    "M07": _m07,
    "M08": _m08,
}

MACHINE_IDS = {task: f"{task}-PRODUCTION" for task in TASKS}


def run_discovery(
    *,
    run_id: str,
    source_package: dict[str, Any],
) -> dict[str, Any]:
    source_id = source_package["source_id"]
    initial = {
        "type": "SOURCE_PACKAGE",
        "source_id": source_id,
        "source_package": source_package,
        "traceability": {
            "source_id": source_id,
            "source_package": source_package["package_id"],
        },
        "ref": source_package["package_id"],
    }

    runner = MachineSource001Superagent()
    result = runner.run_chain(run_id, source_package, initial, list(TASKS))

    if result.get("status") != "ACCEPT":
        return {
            "status": result.get("status"),
            "run_id": run_id,
            "source_id": source_id,
            "source_package_id": source_package["package_id"],
            "results": result.get("results", []),
        }

    discovery_result = build_discovery_result(
        run_id=run_id,
        source=source_package,
        results=result["results"],
    )

    return {
        "status": "ACCEPT",
        "run_id": run_id,
        "source_id": source_id,
        "source_package_id": source_package["package_id"],
        "discovery_result": discovery_result["discovery_result"],
        "results": result["results"],
    }
