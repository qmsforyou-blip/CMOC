from mvp_runner import Contract, Superagent
from m05_llm import classify


CANDIDATES = [
    {"id": "NOM-001", "distinction_id": "DIS-001", "candidate_term": "Quality Systems Basics source revision", "status": "PROVISIONAL", "uncertainty": "CLEAR", "source_id": "SRC-002"},
    {"id": "NOM-002", "distinction_id": "DIS-002", "candidate_term": "QSB strategy set", "status": "PROVISIONAL", "uncertainty": "CLEAR", "source_id": "SRC-002"},
    {"id": "NOM-003", "distinction_id": "DIS-003", "candidate_term": "Red-rated strategy workshop identification", "status": "PROVISIONAL", "uncertainty": "CLEAR", "source_id": "SRC-002"},
    {"id": "NOM-004", "distinction_id": "DIS-004", "candidate_term": "Red and Yellow Audit question strategy delivery and action planning", "status": "PROVISIONAL", "uncertainty": "CLEAR", "source_id": "SRC-002"},
    {"id": "NOM-005", "distinction_id": "DIS-005", "candidate_term": "QSB common principles, methods, processes, and global language", "status": "PROVISIONAL", "uncertainty": "CLEAR", "source_id": "SRC-002"},
    {"id": "NOM-006", "distinction_id": "DIS-006", "candidate_term": "Fast Response visual management", "status": "PROVISIONAL", "uncertainty": "CLEAR", "source_id": "SRC-002"},
    {"id": "NOM-007", "distinction_id": "DIS-007", "candidate_term": "Fast Response and Problem Solving section separation", "status": "PROVISIONAL", "uncertainty": "CLEAR", "source_id": "SRC-002"},
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


def m05(source_package_input, batch):
    records = classify(source_package_input["records"])
    return {
        "status": "ACCEPT",
        "type": "CLASSIFICATION_RECORDS",
        "source_id": batch.source_id,
        "batch_id": batch.batch_id,
        "records": records,
        "traceability": {
            "source_id": batch.source_id,
            "batch_id": batch.batch_id,
            "source_package": SOURCE_PACKAGE["package_id"],
            "upstream_batch": "BATCH-SRC-002-M04-001",
        },
        "ref": f"{batch.batch_id}:OUTPUT",
    }


runner = Superagent(
    contracts={
        "M05": Contract(
            task="M05",
            accepted_inputs={"NOMENCLATURE_CANDIDATES"},
            output_type="CLASSIFICATION_RECORDS",
            required_input_fields={"records"},
            required_output_fields={
                "source_id", "batch_id", "records", "traceability", "ref"
            },
        )
    },
    handlers={"M05": m05},
    machine_ids={"M05": "M05-PRODUCTION"},
)

source_input = {
    "type": "NOMENCLATURE_CANDIDATES",
    "source_id": "SRC-002",
    "source_package": SOURCE_PACKAGE,
    "records": CANDIDATES,
    "traceability": {
        "source_id": "SRC-002",
        "source_package": SOURCE_PACKAGE["package_id"],
        "upstream_batch": "BATCH-SRC-002-M04-001",
    },
}

result = runner.execute(
    run_id="RUN-SRC-002-M05-001",
    source={"source_id": "SRC-002"},
    task="M05",
    inp=source_input,
)

import json
print(json.dumps(result, ensure_ascii=False, indent=2))
