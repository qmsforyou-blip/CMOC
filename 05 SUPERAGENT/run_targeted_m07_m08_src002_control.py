"""Targeted M07->M08 negative control for SRC-002.

Purpose:
- run production M01-M06 to obtain current passport output;
- pass the actual M06 output to M07;
- provide NO relation evidence to M07 (no prepared relation fixture);
- pass the actual M07 output to M08;
- verify that insufficient relation evidence produces a controlled negative branch.

This is a targeted control, not an Automated Run claim.
"""

from __future__ import annotations

import json
import os
import sys
from typing import Any

sys.path.insert(0, os.path.dirname(__file__))

from mvp_runner import Batch, Contract, Superagent
from m01_integration import build_m01_handler
from m02_llm import extract_distinctions
from m03_llm import formulate
from m04_llm import select_nomenclature
from m05_llm import classify
from m06_llm import build_passports
from m07_llm import build_relation_candidates

SOURCE_ID = "SRC-002"
RUN_ID = "RUN-SRC-002-TARGETED-M07-M08-001"
SOURCE_PACKAGE = "SOURCE-002-PACKAGE-001-CONTROLLED-1-6"

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

def wrap(batch: Batch, output_type: str, records: list[dict[str, Any]], upstream: dict[str, Any]) -> dict:
    return {
        "status": "ACCEPT",
        "type": output_type,
        "source_id": SOURCE_ID,
        "batch_id": batch.batch_id,
        "records": records,
        "traceability": {
            "source_id": SOURCE_ID,
            "source_package": SOURCE_PACKAGE,
            "upstream_batch": upstream.get("batch_id"),
        },
        "ref": f"{batch.batch_id}:OUTPUT",
    }

class Runner(Superagent):
    seq = 0
    def new_batch(self, source_id, task, input_ref, handoff_id=None):
        type(self).seq += 1
        return Batch(
            f"BATCH-SRC-002-{task}-{type(self).seq:03d}",
            source_id, task, input_ref, handoff_id
        )

def m01(inp, batch):
    return wrap(batch, "EXTRACTION_RECORDS", build_m01_handler()(inp, batch)["records"], inp)

def m02(inp, batch):
    return wrap(batch, "DISTINCTION_RECORDS", extract_distinctions(inp), inp)

def m03(inp, batch):
    return wrap(batch, "FORMULATION_RECORDS", formulate(inp), inp)

def m04(inp, batch):
    return wrap(batch, "NOMENCLATURE_CANDIDATES", select_nomenclature(inp), inp)

def m05(inp, batch):
    return wrap(batch, "CLASSIFICATION_RECORDS", classify(inp["records"]), inp)

def m06(inp, batch):
    return wrap(batch, "PASSPORT_RECORDS", build_passports(inp["records"]), inp)

def m07(inp, batch):
    # Deliberately NO relation evidence.
    records = build_relation_candidates(inp["records"], [])
    return wrap(batch, "RELATION_CANDIDATES", records, inp)

def m08(inp, batch):
    # M08 receives the actual M07 output.
    records = inp["records"]
    if records and all(r.get("status") == "NO_RELATION" for r in records):
        decisions = []
    else:
        raise RuntimeError(
            "CONTROL FAILURE: M07 produced relation candidates without relation evidence."
        )
    return wrap(batch, "DECISION_RECORDS", decisions, inp)

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

runner = Runner(
    CONTRACTS,
    {"M01":m01,"M02":m02,"M03":m03,"M04":m04,"M05":m05,"M06":m06,"M07":m07,"M08":m08},
    {f"M{i:02d}":f"M{i:02d}-PRODUCTION" for i in range(1,9)}
)

initial = {
    "type": "SOURCE_PACKAGE",
    "source_id": SOURCE_ID,
    "source_package": SOURCE,
    "traceability": {"source_id": SOURCE_ID, "source_package": SOURCE_PACKAGE},
    "ref": SOURCE_PACKAGE,
}

result = runner.run_chain(
    run_id=RUN_ID,
    source=SOURCE,
    initial=initial,
    tasks=["M01","M02","M03","M04","M05","M06","M07","M08"],
)

print(json.dumps({
    "status": result["status"],
    "run_id": RUN_ID,
    "batches": [r.get("batch_id") for r in result.get("results", [])],
    "handoffs": [
        {"id": h.handoff_id, "from": h.from_task, "to": h.to_task, "status": h.status}
        for h in runner.handoffs
    ],
    "m07_output": result.get("results", [])[6] if len(result.get("results", [])) > 6 else None,
    "m08_output": result.get("results", [])[7] if len(result.get("results", [])) > 7 else None,
}, ensure_ascii=False, indent=2))
