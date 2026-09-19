from mvp_runner import Contract, Superagent
from m06_llm import build_passports


CLASSIFICATIONS = [
    {"id": "CLS-001", "candidate_id": "NOM-001", "type": "SOURCE_IDENTITY", "status": "PROVISIONAL", "uncertainty": "CLEAR", "source_id": "SRC-002"},
    {"id": "CLS-002", "candidate_id": "NOM-002", "type": "COLLECTION", "status": "PROVISIONAL", "uncertainty": "CLEAR", "source_id": "SRC-002"},
    {"id": "CLS-003", "candidate_id": "NOM-003", "type": "DECISION", "status": "PROVISIONAL", "uncertainty": "CLEAR", "source_id": "SRC-002"},
    {"id": "CLS-004", "candidate_id": "NOM-004", "type": "ACTIVITY", "status": "PROVISIONAL", "uncertainty": "CLEAR", "source_id": "SRC-002"},
    {"id": "CLS-005", "candidate_id": "NOM-005", "type": "CONCEPT_MODEL", "status": "PROVISIONAL", "uncertainty": "CLEAR", "source_id": "SRC-002"},
    {"id": "CLS-006", "candidate_id": "NOM-006", "type": "STRATEGY", "status": "PROVISIONAL", "uncertainty": "CLEAR", "source_id": "SRC-002"},
    {"id": "CLS-007", "candidate_id": "NOM-007", "type": "STRUCTURAL_DISTINCTION", "status": "PROVISIONAL", "uncertainty": "CLEAR", "source_id": "SRC-002"},
]

SOURCE_PACKAGE = {
    "package_id": "SOURCE-002-PACKAGE-001-CONTROLLED-1-6",
    "source_id": "SRC-002",
    "source_name": "GM Quality System Basics Overview — Supplier Audit",
    "source_type": "PDF",
    "source_version": "rev March 2009",
    "source_package_status": "PARTIAL",
    "work_scope": "pages 1-6 only",
    "fragments": [
        {"location": "p1", "text": "Quality Systems Basics rev March 2009."},
        {"location": "p2", "text": "11 QSB strategies: Fast Response; Control of Non-Conforming Product; Verification Station; Standardized Operations; Standardized Operator Training; Error Proofing Verification; Layered Process Audits; RPN Risk Reduction; Contamination Control; Supply Chain Management; Managing Change."},
        {"location": "p3", "text": "Assess supplier per Latest QSB Audit to determine strategies Red and requiring workshop."},
        {"location": "p4", "text": "Quality Systems Basics: Common Principles, Common Methods, Common Processes. Focus — ONE LANGUAGE GLOBALLY."},
        {"location": "p5", "text": "Fast Response: solving problems faster & earlier upstream through visual management."},
        {"location": "p6", "text": "Fast Response separates 1.2 Fast Response from 1.3 Problem Solving."},
    ],
}


def m06(source_input, batch):
    records = build_passports(source_input["records"])
    return {
        "status": "ACCEPT",
        "type": "PASSPORT_RECORDS",
        "source_id": batch.source_id,
        "batch_id": batch.batch_id,
        "records": records,
        "traceability": {
            "source_id": batch.source_id,
            "batch_id": batch.batch_id,
            "source_package": SOURCE_PACKAGE["package_id"],
            "upstream_batch": "BATCH-SRC-002-M05-001",
        },
        "ref": f"{batch.batch_id}:OUTPUT",
    }


runner = Superagent(
    contracts={
        "M06": Contract(
            task="M06",
            accepted_inputs={"CLASSIFICATION_RECORDS"},
            output_type="PASSPORT_RECORDS",
            required_input_fields={"records"},
            required_output_fields={
                "source_id", "batch_id", "records", "traceability", "ref"
            },
        )
    },
    handlers={"M06": m06},
    machine_ids={"M06": "M06-PRODUCTION"},
)

source_input = {
    "type": "CLASSIFICATION_RECORDS",
    "source_id": "SRC-002",
    "source_package": SOURCE_PACKAGE,
    "records": CLASSIFICATIONS,
    "traceability": {
        "source_id": "SRC-002",
        "source_package": SOURCE_PACKAGE["package_id"],
        "upstream_batch": "BATCH-SRC-002-M05-001",
    },
}

result = runner.execute(
    run_id="RUN-SRC-002-M06-001",
    source={"source_id": "SRC-002"},
    task="M06",
    inp=source_input,
)

import json
print(json.dumps(result, ensure_ascii=False, indent=2))
