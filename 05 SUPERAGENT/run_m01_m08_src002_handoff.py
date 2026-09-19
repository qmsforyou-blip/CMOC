"""Controlled true-handoff M01->M08 run for SRC-002.

Purpose:
- execute the production adapters in one process;
- pass the actual output object of each TASK to the next TASK;
- use the Superagent contract gate and Handoff mechanism;
- keep the controlled SRC-002 relation evidence fixture explicit for M07/M08.

This is a handoff-chain test. It must not be called a universal automated run.
"""

from __future__ import annotations

import json
import os
import sys
from typing import Any, Dict

sys.path.insert(0, os.path.dirname(__file__))

from mvp_runner import Batch, Contract, Superagent
from m01_integration import build_m01_handler
from m02_llm import extract_distinctions
from m03_llm import formulate
from m04_llm import select_nomenclature
from m05_llm import classify
from m06_llm import build_passports
from m07_llm import build_relation_candidates
from m08_llm import decide


SOURCE_ID = "SRC-002"
RUN_ID = "RUN-SRC-002-HANDOFF-001"
SOURCE_PACKAGE = "SOURCE-002-PACKAGE-001-CONTROLLED-1-6"
MACHINE_IDS = {
    "M01": "M01-PRODUCTION",
    "M02": "M02-PRODUCTION",
    "M03": "M03-PRODUCTION",
    "M04": "M04-PRODUCTION",
    "M05": "M05-PRODUCTION",
    "M06": "M06-PRODUCTION",
    "M07": "M07-PRODUCTION",
    "M08": "M08-PRODUCTION",
}

SOURCE = {
    "package_id": SOURCE_PACKAGE,
    "source_id": SOURCE_ID,
    "source_name": "GM Quality System Basics Overview — Supplier Audit",
    "source_type": "PDF",
    "source_version": "rev March 2009",
    "source_package_status": "PARTIAL",
    "fragments": [
        {"location": "p1", "text": "Quality Systems Basics rev March 2009."},
        {"location": "p2", "text": "11 QSB strategies: Fast Response; Control of Non-Conforming Product; Verification Station; Standardized Operations; Standardized Operator Training; Error Proofing Verification; Layered Process Audits; RPN Risk Reduction; Contamination Control; Supply Chain Management; Managing Change."},
        {"location": "p3", "text": "Rules of Engagement: assess supplier per Latest QSB Audit to determine strategies Red and requiring workshop; deliver strategies as required and obtain Action Plan for all Red and Yellow Audit questions."},
        {"location": "p4", "text": "Quality Systems Basics: Common Principles, Common Methods, Common Processes. Focus — ONE LANGUAGE GLOBALLY."},
        {"location": "p5", "text": "1.0 FAST RESPONSE: solving problems faster & earlier upstream through visual management."},
        {"location": "p6", "text": "Fast Response separates 1.2 Fast Response from 1.3 Problem Solving."},
    ],
}

RELATION_EVIDENCE = [
    {
        "evidence_id": "EVID-SRC-002-P2-STRATEGY-SET-001",
        "locations": ["p2"],
        "text": SOURCE["fragments"][1]["text"],
        "supports": ["PAS-002", "PAS-006"],
    }
]


class ControlledBatchSuperagent(Superagent):
    _seq = 0

    def new_batch(self, source_id, task, input_ref, handoff_id=None):
        self.__class__._seq += 1
        batch_id = f"BATCH-SRC-002-{task}-{self.__class__._seq:03d}"
        return Batch(batch_id, source_id, task, input_ref, handoff_id)


def wrap_output(batch: Batch, output_type: str, records: list[dict[str, Any]], upstream: dict[str, Any], **extra) -> dict:
    trace = {
        "source_id": SOURCE_ID,
        "batch_id": batch.batch_id,
        "source_package": SOURCE_PACKAGE,
        "upstream_batch": upstream.get("batch_id"),
    }
    return {
        "status": "ACCEPT",
        "type": output_type,
        "source_id": SOURCE_ID,
        "batch_id": batch.batch_id,
        "records": records,
        "traceability": trace,
        "ref": f"{batch.batch_id}:OUTPUT",
        **extra,
    }


def m01(inp, batch):
    records = build_m01_handler()(inp, batch)["records"]
    return wrap_output(batch, "EXTRACTION_RECORDS", records, inp)


def m02(inp, batch):
    records = extract_distinctions(inp)
    return wrap_output(batch, "DISTINCTION_RECORDS", records, inp)


def m03(inp, batch):
    records = formulate(inp)
    return wrap_output(batch, "FORMULATION_RECORDS", records, inp)


def m04(inp, batch):
    records = select_nomenclature(inp)
    return wrap_output(batch, "NOMENCLATURE_CANDIDATES", records, inp)


def m05(inp, batch):
    records = classify(inp["records"])
    return wrap_output(batch, "CLASSIFICATION_RECORDS", records, inp)


def m06(inp, batch):
    records = build_passports(inp["records"])
    return wrap_output(batch, "PASSPORT_RECORDS", records, inp)


def m07(inp, batch):
    records = build_relation_candidates(inp["records"], RELATION_EVIDENCE)
    return wrap_output(
        batch,
        "RELATION_CANDIDATES",
        records,
        inp,
        relation_evidence=RELATION_EVIDENCE,
        passports=inp["records"],
        evaluated_passport_ids=[p["id"] for p in inp["records"]],
        relation_evidence_ids=[e["evidence_id"] for e in RELATION_EVIDENCE],
    )


def m08(inp, batch):
    records = decide(
        inp["passports"],
        inp["records"],
        inp.get("relation_evidence", RELATION_EVIDENCE),
    )
    return wrap_output(
        batch,
        "DECISION_RECORDS",
        records,
        inp,
        upstream_m07_batch=inp.get("batch_id"),
        relation_evidence_ids=[e["evidence_id"] for e in inp.get("relation_evidence", RELATION_EVIDENCE)],
    )


CONTRACTS = {
    "M01": Contract("M01", {"SOURCE_PACKAGE"}, "EXTRACTION_RECORDS", {"source_id","batch_id","records","traceability","ref"}, {"source_package"}),
    "M02": Contract("M02", {"EXTRACTION_RECORDS"}, "DISTINCTION_RECORDS", {"source_id","batch_id","records","traceability","ref"}, {"records"}),
    "M03": Contract("M03", {"DISTINCTION_RECORDS"}, "FORMULATION_RECORDS", {"source_id","batch_id","records","traceability","ref"}, {"records"}),
    "M04": Contract("M04", {"FORMULATION_RECORDS"}, "NOMENCLATURE_CANDIDATES", {"source_id","batch_id","records","traceability","ref"}, {"records"}),
    "M05": Contract("M05", {"NOMENCLATURE_CANDIDATES"}, "CLASSIFICATION_RECORDS", {"source_id","batch_id","records","traceability","ref"}, {"records"}),
    "M06": Contract("M06", {"CLASSIFICATION_RECORDS"}, "PASSPORT_RECORDS", {"source_id","batch_id","records","traceability","ref"}, {"records"}),
    "M07": Contract("M07", {"PASSPORT_RECORDS"}, "RELATION_CANDIDATES", {"source_id","batch_id","records","traceability","ref"}, {"records"}),
    "M08": Contract("M08", {"RELATION_CANDIDATES"}, "DECISION_RECORDS", {"source_id","batch_id","records","traceability","ref"}, {"records"}),
}

HANDLERS = {
    "M01": m01, "M02": m02, "M03": m03, "M04": m04,
    "M05": m05, "M06": m06, "M07": m07, "M08": m08,
}

runner = ControlledBatchSuperagent(CONTRACTS, HANDLERS, MACHINE_IDS)

initial = {
    "type": "SOURCE_PACKAGE",
    "source_id": SOURCE_ID,
    "source_package": SOURCE,
    "traceability": {
        "source_id": SOURCE_ID,
        "source_package": SOURCE_PACKAGE,
    },
    "ref": SOURCE_PACKAGE,
}

tasks = ["M01","M02","M03","M04","M05","M06","M07","M08"]\n\nresult = runner.run_chain(
    run_id=RUN_ID,
    source=SOURCE,
    initial=initial,
    tasks=tasks,
)

audit = {
    "status": result["status"],
    "run_id": RUN_ID,
    "task_batches": [
        {
            "task": tasks[i] if i < len(tasks) else None,
            "batch_id": r.get("batch_id"),
            "input_ref": r.get("traceability", {}).get("upstream_batch") if isinstance(r, dict) else None,
            "output_ref": r.get("ref") if isinstance(r, dict) else None,
        }
        for r in result.get("results", [])
    ],
    "handoffs": [
        {
            "id": h.handoff_id,
            "from": h.from_task,
            "to": h.to_task,
            "output_ref": h.output_ref,
            "input_type": h.input_type,
            "status": h.status,
        }
        for h in runner.handoffs
    ],
    "m07_result": m07_result,\n    "final_result": result.get("results", [])[-1] if result.get("results") else None,
}

print(json.dumps(audit, ensure_ascii=False, indent=2))
