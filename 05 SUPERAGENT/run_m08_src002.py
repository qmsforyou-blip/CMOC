import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from mvp_runner import Batch, Contract, Superagent
from m08_llm import decide


SOURCE_ID = "SRC-002"
RUN_ID = "RUN-SRC-002-M08-001"
BATCH_ID = "BATCH-SRC-002-M08-001"
MACHINE_ID = "M08-PRODUCTION"
SOURCE_PACKAGE = "SOURCE-002-PACKAGE-001-CONTROLLED-1-6"
UPSTREAM_M06 = "BATCH-SRC-002-M06-001"
UPSTREAM_M07 = "BATCH-SRC-002-M07-002"


PASSPORTS = [
    {"id": "PAS-001", "candidate_id": "NOM-001", "source_id": SOURCE_ID, "term": "Quality Systems Basics source revision", "working_class": "SOURCE_IDENTITY", "lifecycle_status": "ЧЕРНОВИК", "epistemic_status": "PROVISIONAL", "source_basis": ["FORM-001", "FORM-002", "FORM-003"]},
    {"id": "PAS-002", "candidate_id": "NOM-002", "source_id": SOURCE_ID, "term": "QSB 11-strategy set", "working_class": "COLLECTION", "lifecycle_status": "ЧЕРНОВИК", "epistemic_status": "PROVISIONAL", "source_basis": ["FORM-004", "FORM-005", "FORM-006"]},
    {"id": "PAS-003", "candidate_id": "NOM-003", "source_id": SOURCE_ID, "term": "Red-rated strategy workshop identification", "working_class": "DECISION", "lifecycle_status": "ЧЕРНОВИК", "epistemic_status": "PROVISIONAL", "source_basis": ["FORM-007", "FORM-008", "FORM-009"]},
    {"id": "PAS-004", "candidate_id": "NOM-004", "source_id": SOURCE_ID, "term": "Red and Yellow Audit question strategy delivery and action planning", "working_class": "ACTIVITY", "lifecycle_status": "ЧЕРНОВИК", "epistemic_status": "PROVISIONAL", "source_basis": ["FORM-010", "FORM-011", "FORM-012"]},
    {"id": "PAS-005", "candidate_id": "NOM-005", "source_id": SOURCE_ID, "term": "QSB common principles, methods, processes, and global language", "working_class": "CONCEPT_MODEL", "lifecycle_status": "ЧЕРНОВИК", "epistemic_status": "PROVISIONAL", "source_basis": ["FORM-013", "FORM-014", "FORM-015"]},
    {"id": "PAS-006", "candidate_id": "NOM-006", "source_id": SOURCE_ID, "term": "Fast Response visual management", "working_class": "STRATEGY", "lifecycle_status": "ЧЕРНОВИК", "epistemic_status": "PROVISIONAL", "source_basis": ["FORM-016", "FORM-017", "FORM-018"]},
    {"id": "PAS-007", "candidate_id": "NOM-007", "source_id": SOURCE_ID, "term": "Fast Response and Problem Solving section separation", "working_class": "STRUCTURAL_DISTINCTION", "lifecycle_status": "ЧЕРНОВИК", "epistemic_status": "PROVISIONAL", "source_basis": ["FORM-019", "FORM-020", "FORM-021"]},
]

RELATION_CANDIDATES = [
    {
        "id": "REL-001",
        "source_id": SOURCE_ID,
        "from_passport_id": "PAS-006",
        "to_passport_id": "PAS-002",
        "relation_type": "MEMBER_OF",
        "status": "RELATION_CANDIDATE",
        "epistemic_status": "PROVISIONAL",
        "basis_refs": ["EVID-SRC-002-P2-STRATEGY-SET-001"],
        "evidence_gap": None,
    }
]

RELATION_EVIDENCE = [
    {
        "evidence_id": "EVID-SRC-002-P2-STRATEGY-SET-001",
        "locations": ["p2"],
        "text": "11 QSB strategies: Fast Response; Control of Non-Conforming Product; Verification Station; Standardized Operations; Standardized Operator Training; Error Proofing Verification; Layered Process Audits; RPN Risk Reduction; Contamination Control; Supply Chain Management; Managing Change.",
        "supports": ["PAS-002", "PAS-006"],
    }
]


class ControlledBatchSuperagent(Superagent):
    def new_batch(self, source_id, task, input_ref, handoff_id=None):
        return Batch(BATCH_ID, source_id, task, input_ref, handoff_id)


def m08_handler(inp, batch):
    records = decide(
        inp["records"],
        inp["relation_candidates"],
        inp["relation_evidence"],
    )
    return {
        "status": "ACCEPT",
        "type": "DECISION_RECORDS",
        "source_id": batch.source_id,
        "batch_id": batch.batch_id,
        "records": records["records"],
        "traceability": {
            "source_id": batch.source_id,
            "batch_id": batch.batch_id,
            "source_package": SOURCE_PACKAGE,
            "upstream_m06_batch": UPSTREAM_M06,
            "upstream_m07_batch": UPSTREAM_M07,
            "passport_ids": [p["id"] for p in PASSPORTS],
            "relation_ids": [r["id"] for r in RELATION_CANDIDATES],
            "relation_evidence_ids": [e["evidence_id"] for e in RELATION_EVIDENCE],
        },
        "ref": f"{batch.batch_id}:OUTPUT",
    }


contracts = {
    "M08": Contract(
        task="M08",
        accepted_inputs={"PASSPORT_RECORDS"},
        output_type="DECISION_RECORDS",
        required_output_fields={
            "source_id",
            "batch_id",
            "records",
            "traceability",
            "ref",
        },
        required_input_fields={
            "records",
            "relation_candidates",
            "relation_evidence",
        },
    )
}

runner = ControlledBatchSuperagent(
    contracts=contracts,
    handlers={"M08": m08_handler},
    machine_ids={"M08": MACHINE_ID},
)

source = {
    "package_id": SOURCE_PACKAGE,
    "source_id": SOURCE_ID,
    "source_name": "GM Quality System Basics Overview — Supplier Audit",
    "source_type": "PDF",
    "source_version": "rev March 2009",
    "source_package_status": "PARTIAL",
    "fragments": [{"location": "p1-6", "text": "Controlled source package pages 1-6"}],
}

inp = {
    "type": "PASSPORT_RECORDS",
    "source_id": SOURCE_ID,
    "records": PASSPORTS,
    "relation_candidates": RELATION_CANDIDATES,
    "relation_evidence": RELATION_EVIDENCE,
    "traceability": {
        "source_id": SOURCE_ID,
        "source_package": SOURCE_PACKAGE,
        "upstream_batch": UPSTREAM_M06,
    },
}

result = runner.execute(
    run_id=RUN_ID,
    source=source,
    task="M08",
    inp=inp,
)

print(json.dumps(result, ensure_ascii=False, indent=2))
