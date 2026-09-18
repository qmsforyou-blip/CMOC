#!/usr/bin/env python3
"""
CMOC MVP-SUPERAGENT-001
Minimal contract-driven orchestrator.

This runner deliberately does NOT implement M01/M02/M03 semantics.
It validates inputs, creates Batch identities, executes a registered
machine callable, validates output contracts, and performs explicit handoff.
"""

from __future__ import annotations

import argparse
import json
import sys
import uuid
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable


class Reject(Exception):
    def __init__(self, reason: str, gate: str):
        super().__init__(reason)
        self.reason = reason
        self.gate = gate


@dataclass
class TaskContract:
    task: str
    accepted_inputs: tuple[str, ...]
    output_type: str
    required_output_fields: tuple[str, ...]


@dataclass
class Batch:
    run_id: str
    source_id: str
    task: str
    machine_id: str
    batch_id: str
    input_reference: str
    created_at: str


MACHINES: dict[str, Callable[[dict[str, Any]], dict[str, Any]]] = {}
CONTRACTS: dict[str, TaskContract] = {}


def register(task: str, machine_id: str, accepted_inputs: tuple[str, ...],
             output_type: str, required_output_fields: tuple[str, ...]):
    def decorator(fn):
        MACHINES[task] = fn
        CONTRACTS[task] = TaskContract(
            task, accepted_inputs, output_type, required_output_fields
        )
        fn.machine_id = machine_id
        return fn
    return decorator


@register(
    "M01",
    "MACHINE-SOURCE-001",
    ("SOURCE_PACKAGE",),
    "ExtractionBatch",
    ("source_id", "batch_id", "records"),
)
def m01(inp):
    # Semantic production remains outside the generic runner.
    # This stub makes the execution boundary explicit for the MVP.
    return {
        "output_type": "ExtractionBatch",
        "source_id": inp["source_id"],
        "batch_id": inp["batch_id"],
        "records": inp.get("records", []),
    }


@register(
    "M02",
    "MACHINE-SOURCE-001",
    ("ExtractionBatch", "SOURCE_PACKAGE"),
    "DistinctionBatch",
    ("source_id", "batch_id", "records"),
)
def m02(inp):
    return {
        "output_type": "DistinctionBatch",
        "source_id": inp["source_id"],
        "batch_id": inp["batch_id"],
        "records": inp.get("records", []),
    }


@register(
    "M03",
    "MACHINE-SOURCE-001",
    ("DistinctionBatch", "SOURCE_PACKAGE"),
    "FormulationBatch",
    ("source_id", "batch_id", "records"),
)
def m03(inp):
    return {
        "output_type": "FormulationBatch",
        "source_id": inp["source_id"],
        "batch_id": inp["batch_id"],
        "records": inp.get("records", []),
    }


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def new_batch(source_id: str, task: str, machine_id: str,
              input_reference: str, run_id: str) -> Batch:
    suffix = uuid.uuid4().hex[:8]
    return Batch(
        run_id=run_id,
        source_id=source_id,
        task=task,
        machine_id=machine_id,
        batch_id=f"BATCH-{source_id}-{task}-{suffix}",
        input_reference=input_reference,
        created_at=utc_now(),
    )


def input_type(inp: dict[str, Any]) -> str:
    return inp.get("input_type", "UNKNOWN")


def pre_gate(task: str, inp: dict[str, Any]) -> None:
    if task not in CONTRACTS:
        raise Reject("TASK_CONTRACT_NOT_FOUND", "PRE_CONTRACT_CHECK")
    contract = CONTRACTS[task]
    if input_type(inp) not in contract.accepted_inputs:
        raise Reject(
            f"CONTRACT_MISMATCH: got {input_type(inp)}, "
            f"required one of {contract.accepted_inputs}",
            "PRE_CONTRACT_CHECK",
        )
    for field in ("source_id",):
        if field not in inp:
            raise Reject(f"MISSING_INPUT_FIELD: {field}", "PRE_CONTRACT_CHECK")


def post_gate(task: str, output: dict[str, Any]) -> None:
    contract = CONTRACTS[task]
    if output.get("output_type") != contract.output_type:
        raise Reject(
            f"OUTPUT_TYPE_MISMATCH: got {output.get('output_type')}, "
            f"required {contract.output_type}",
            "POST_CONTRACT_CHECK",
        )
    missing = [f for f in contract.required_output_fields if f not in output]
    if missing:
        raise Reject(
            f"MISSING_OUTPUT_FIELDS: {', '.join(missing)}",
            "POST_CONTRACT_CHECK",
        )


def execute(source_id: str, source_package: dict[str, Any],
            tasks: list[str], out_dir: Path) -> dict[str, Any]:
    run_id = f"RUN-{uuid.uuid4().hex[:10]}"
    journal: list[dict[str, Any]] = []
    current = {
        "input_type": "SOURCE_PACKAGE",
        "source_id": source_id,
        "package": source_package,
    }

    for task in tasks:
        contract = CONTRACTS.get(task)
        if contract is None:
            raise Reject("TASK_CONTRACT_NOT_FOUND", "DISPATCH")

        batch = new_batch(
            source_id, task, contract.task,
            current.get("output_reference", "SOURCE_PACKAGE"), run_id
        )

        current["batch_id"] = batch.batch_id

        try:
            pre_gate(task, current)
            machine = MACHINES[task]
            output = machine(current)
            post_gate(task, output)
            output["output_reference"] = f"{run_id}:{task}:{batch.batch_id}"
            output["status"] = "ACCEPTED"

            journal.append({
                **asdict(batch),
                "status": "ACCEPTED",
                "qc_result": "PASS",
                "handoff_result": "DECLARED" if task != tasks[-1] else "FINAL",
                "output_reference": output["output_reference"],
            })

            current = {
                **output,
                "input_type": contract.output_type,
            }

        except Reject as exc:
            journal.append({
                **asdict(batch),
                "status": "REJECT",
                "failed_gate": exc.gate,
                "reason": exc.reason,
            })
            break

    result = {
        "run_id": run_id,
        "source_id": source_id,
        "task_sequence": tasks,
        "journal": journal,
        "final_status": journal[-1]["status"] if journal else "REJECT",
    }

    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{run_id}.json"
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--source-json", required=True)
    parser.add_argument("--tasks", nargs="+", default=["M01", "M02", "M03"])
    parser.add_argument("--out", default="runs")
    args = parser.parse_args()

    source_path = Path(args.source_json)
    package = json.loads(source_path.read_text(encoding="utf-8"))

    result = execute(args.source_id, package, args.tasks, Path(args.out))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["final_status"] == "ACCEPTED" else 2


if __name__ == "__main__":
    sys.exit(main())
