"""Production A5 run M01->M08 for SRC-003 (ISO/DIS 9001:2025 pages 5-6).

Controlled new-SOURCE run:
- production MACHINE adapters M01..M08 are used;
- source package is limited to pages 5-6;
- no CMOC / OBJECT INDEX / QUERY / reconciliation access;
- M07 receives no relation evidence, so M08 is expected to produce no decisions.
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
from m08_llm import decide

SOURCE_ID = "SRC-003"
RUN_ID = "RUN-SRC-003-AUTOMATED-M01-M08-001"
SOURCE_PACKAGE = "SOURCE-003-PACKAGE-001-CONTROLLED-5-6"

SOURCE = {
    "package_id": SOURCE_PACKAGE,
    "source_id": SOURCE_ID,
    "source_name": "ISO/DIS 9001:2025 — Quality management systems — Requirements",
    "source_type": "PDF",
    "source_version": "ISO/DIS 9001:2025(en), sixth edition, draft",
    "source_package_status": "PARTIAL",
    "fragments": [
        {
            "location": "p5",
            "text": (
                "Foreword. ISO draws attention to the possibility that implementation "
                "of this document may involve patents and states that any trade name "
                "used is information for convenience and does not constitute endorsement. "
                "The document was prepared by ISO/TC 176, Quality management and quality "
                "assurance, Subcommittee SC 2, Quality systems. This sixth edition "
                "cancels and replaces the fifth edition (EN ISO 9001:2015)."
            ),
        },
        {
            "location": "p6",
            "text": (
                "Introduction 0.1 General. The adoption of a quality management system "
                "is a strategic decision for an organization that can help improve overall "
                "performance and provide a sound basis for sustainable development initiatives. "
                "Potential benefits listed include consistently providing products and services "
                "that meet customer and applicable statutory and regulatory requirements; "
                "facilitating opportunities to enhance customer satisfaction; addressing risks "
                "and opportunities associated with context and objectives; and demonstrating "
                "conformity to specified quality management system requirements. The document "
                "can be used by internal and external parties. It states that it is not intended "
                "to imply uniformity in the structure of different quality management systems, "
                "alignment of documentation to the clause structure, or use of the specific "
                "terminology of the document within the organization. The document distinguishes "
                "verbal forms: shall indicates a requirement; should a recommendation; may a "
                "permission; can a possibility or capability. NOTE information is for guidance. "
                "Annex A is informative and does not contain additional requirements. Section 0.2 "
                "states that the document is based on quality management principles described in ISO/CD 9000."
            ),
        },
    ],
}

class AutomatedBatchSuperagent(Superagent):
    _seq = 0
    def new_batch(self, source_id, task, input_ref, handoff_id=None):
        self.__class__._seq += 1
        batch_id = f"BATCH-SRC-003-{task}-{self.__class__._seq:03d}"
        batch = Batch(batch_id, source_id, task, input_ref, handoff_id)
        self.batches.append(batch)
        return batch

def wrap_output(batch: Batch, output_type: str, records: list[dict[str, Any]],
                upstream: dict[str, Any], **extra) -> dict[str, Any]:
    return {
        "status": "ACCEPT",
        "type": output_type,
        "source_id": SOURCE_ID,
        "batch_id": batch.batch_id,
        "records": records,
        "traceability": {
            "source_id": SOURCE_ID,
            "batch_id": batch.batch_id,
            "source_package": SOURCE_PACKAGE,
            "upstream_batch": upstream.get("batch_id"),
        },
        "ref": f"{batch.batch_id}:OUTPUT",
        **extra,
    }

def m01(inp, batch):
    return wrap_output(batch, "EXTRACTION_RECORDS", build_m01_handler()(inp, batch)["records"], inp)

def m02(inp, batch):
    return wrap_output(batch, "DISTINCTION_RECORDS", extract_distinctions(inp), inp)

def m03(inp, batch):
    return wrap_output(batch, "FORMULATION_RECORDS", formulate(inp), inp)

def m04(inp, batch):
    return wrap_output(batch, "NOMENCLATURE_CANDIDATES", select_nomenclature(inp), inp)

def m05(inp, batch):
    return wrap_output(batch, "CLASSIFICATION_RECORDS", classify(inp["records"]), inp)

def m06(inp, batch):
    return wrap_output(batch, "PASSPORT_RECORDS", build_passports(inp["records"]), inp)

def m07(inp, batch):
    records = build_relation_candidates(inp["records"], [])
    return wrap_output(
        batch, "RELATION_CANDIDATES", records, inp,
        passports=inp["records"],
        evaluated_passport_ids=[p["id"] for p in inp["records"]],
        relation_evidence=[],
    )

def m08(inp, batch):
    decision_output = decide(inp["passports"], inp["records"], inp.get("relation_evidence", []))
    return wrap_output(
        batch, "DECISION_RECORDS", decision_output.get("records", []), inp,
        upstream_m07_batch=inp.get("batch_id"),
    )

CONTRACTS = {
    "M01": Contract("M01", {"SOURCE_PACKAGE"}, "EXTRACTION_RECORDS",
                    {"source_id","batch_id","records","traceability","ref"}, {"source_package"}),
    "M02": Contract("M02", {"EXTRACTION_RECORDS"}, "DISTINCTION_RECORDS",
                    {"source_id","batch_id","records","traceability","ref"}, {"records"}),
    "M03": Contract("M03", {"DISTINCTION_RECORDS"}, "FORMULATION_RECORDS",
                    {"source_id","batch_id","records","traceability","ref"}, {"records"}),
    "M04": Contract("M04", {"FORMULATION_RECORDS"}, "NOMENCLATURE_CANDIDATES",
                    {"source_id","batch_id","records","traceability","ref"}, {"records"}),
    "M05": Contract("M05", {"NOMENCLATURE_CANDIDATES"}, "CLASSIFICATION_RECORDS",
                    {"source_id","batch_id","records","traceability","ref"}, {"records"}),
    "M06": Contract("M06", {"CLASSIFICATION_RECORDS"}, "PASSPORT_RECORDS",
                    {"source_id","batch_id","records","traceability","ref"}, {"records"}),
    "M07": Contract("M07", {"PASSPORT_RECORDS"}, "RELATION_CANDIDATES",
                    {"source_id","batch_id","records","traceability","ref"}, {"records"}),
    "M08": Contract("M08", {"RELATION_CANDIDATES"}, "DECISION_RECORDS",
                    {"source_id","batch_id","records","traceability","ref"}, {"records"}),
}

HANDLERS = {"M01":m01,"M02":m02,"M03":m03,"M04":m04,"M05":m05,"M06":m06,"M07":m07,"M08":m08}
MACHINE_IDS = {task: f"{task}-PRODUCTION" for task in HANDLERS}
runner = AutomatedBatchSuperagent(CONTRACTS, HANDLERS, MACHINE_IDS)

initial = {
    "type": "SOURCE_PACKAGE",
    "source_id": SOURCE_ID,
    "source_package": SOURCE,
    "traceability": {"source_id": SOURCE_ID, "source_package": SOURCE_PACKAGE},
    "ref": SOURCE_PACKAGE,
}
TASKS = ["M01","M02","M03","M04","M05","M06","M07","M08"]
result = runner.run_chain(RUN_ID, SOURCE, initial, TASKS)
results = result.get("results", [])
m07_result = results[6] if len(results) > 6 else None
m08_result = results[7] if len(results) > 7 else None

if result.get("status") == "ACCEPT":
    if not m07_result or not all(r.get("status") == "NO_RELATION" for r in m07_result.get("records", [])):
        raise RuntimeError("A5 CONTROL FAILURE: M07 did not produce terminal NO_RELATION")
    if not m08_result or m08_result.get("records") != []:
        raise RuntimeError("A5 CONTROL FAILURE: M08 created an unsupported decision")

audit = {
    "status": result.get("status"),
    "run_id": RUN_ID,
    "source_id": SOURCE_ID,
    "source_package": SOURCE_PACKAGE,
    "task_sequence": TASKS,
    "batches": [b.batch_id for b in runner.batches],
    "handoffs": [{"id":h.handoff_id,"from":h.from_task,"to":h.to_task,"status":h.status,
                  "output_ref":h.output_ref,"input_type":h.input_type} for h in runner.handoffs],
    "record_counts": [
        {"task":task,"records":len(results[i].get("records",[]))}
        for i,task in enumerate(TASKS) if i < len(results)
    ],
    "m07_output": m07_result,
    "m08_output": m08_result,
    "machine_ids": MACHINE_IDS,
    "control": {
        "relation_evidence_supplied_to_m07": False,
        "cmoc_access": "NONE",
        "query_access": "NONE",
        "expected_m07_status": "NO_RELATION",
        "expected_m08_records": 0,
    },
}

print(json.dumps(audit, ensure_ascii=False, indent=2))
