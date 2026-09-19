import json
from mvp_runner import Superagent, Contract
from m04_llm import select_nomenclature

FORMULATIONS = [
    {"id":"FORM-001","distinction_id":"DIS-001","level":"INTUITIVE","formulation":"The Quality Systems Basics source is the March 2009 revision.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-002","distinction_id":"DIS-001","level":"ENGINEERING","formulation":"The identified revision of the Quality Systems Basics source is March 2009.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-003","distinction_id":"DIS-001","level":"CANONICAL_FORMULATION","formulation":"Quality Systems Basics source revision: March 2009.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-004","distinction_id":"DIS-002","level":"INTUITIVE","formulation":"QSB has 11 strategies: Fast Response; Control of Non-Conforming Product; Verification Station; Standardized Operations; Standardized Operator Training; Error Proofing Verification; Layered Process Audits; RPN Risk Reduction; Contamination Control; Supply Chain Management; and Managing Change.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-005","distinction_id":"DIS-002","level":"ENGINEERING","formulation":"The defined QSB strategy set contains exactly 11 strategies: Fast Response; Control of Non-Conforming Product; Verification Station; Standardized Operations; Standardized Operator Training; Error Proofing Verification; Layered Process Audits; RPN Risk Reduction; Contamination Control; Supply Chain Management; and Managing Change.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-006","distinction_id":"DIS-002","level":"CANONICAL_FORMULATION","formulation":"QSB comprises 11 strategies: Fast Response; Control of Non-Conforming Product; Verification Station; Standardized Operations; Standardized Operator Training; Error Proofing Verification; Layered Process Audits; RPN Risk Reduction; Contamination Control; Supply Chain Management; and Managing Change.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-007","distinction_id":"DIS-003","level":"INTUITIVE","formulation":"Assess the supplier with the latest QSB Audit to find the Red-rated strategies that require a workshop.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-008","distinction_id":"DIS-003","level":"ENGINEERING","formulation":"Use the latest QSB Audit to assess the supplier, identify each Red-rated strategy, and determine which strategies require a workshop.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-009","distinction_id":"DIS-003","level":"CANONICAL_FORMULATION","formulation":"Assess the supplier using the latest QSB Audit to identify Red-rated strategies requiring a workshop.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-010","distinction_id":"DIS-004","level":"INTUITIVE","formulation":"Deliver the applicable strategies and provide an Action Plan for every Red and Yellow Audit question.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-011","distinction_id":"DIS-004","level":"ENGINEERING","formulation":"For every Audit question rated Red or Yellow, deliver the applicable strategies and an Action Plan.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-012","distinction_id":"DIS-004","level":"CANONICAL_FORMULATION","formulation":"Deliver applicable strategies and an Action Plan for every Red and Yellow Audit question.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-013","distinction_id":"DIS-005","level":"INTUITIVE","formulation":"QSB uses shared principles, methods, and processes while focusing on one global language.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-014","distinction_id":"DIS-005","level":"ENGINEERING","formulation":"QSB applies common principles, methods, and processes with a focus on one global language.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-015","distinction_id":"DIS-005","level":"CANONICAL_FORMULATION","formulation":"QSB uses common principles, methods, and processes with a focus on one global language.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-016","distinction_id":"DIS-006","level":"INTUITIVE","formulation":"Fast Response uses visual management to solve problems faster and earlier upstream.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-017","distinction_id":"DIS-006","level":"ENGINEERING","formulation":"Fast Response applies visual management to solve problems faster and earlier upstream.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-018","distinction_id":"DIS-006","level":"CANONICAL_FORMULATION","formulation":"Fast Response solves problems faster and earlier upstream through visual management.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-019","distinction_id":"DIS-007","level":"INTUITIVE","formulation":"Section 1.2, Fast Response, is separate from section 1.3, Problem Solving.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-020","distinction_id":"DIS-007","level":"ENGINEERING","formulation":"The source presents Fast Response in section 1.2 and Problem Solving separately in section 1.3.","uncertainty":"CLEAR","source_id":"SRC-002"},
    {"id":"FORM-021","distinction_id":"DIS-007","level":"CANONICAL_FORMULATION","formulation":"Section 1.2 Fast Response is separate from section 1.3 Problem Solving.","uncertainty":"CLEAR","source_id":"SRC-002"}
]

contracts = {
    "M04": Contract(
        "M04",
        {"FORMULATION_RECORDS"},
        "NOMENCLATURE_CANDIDATES",
        {"source_id","batch_id","records","traceability","ref"},
        {"records"},
    )
}

runner = Superagent(
    contracts,
    {"M04": lambda inp, batch: {
        "status": "ACCEPT",
        "type": "NOMENCLATURE_CANDIDATES",
        "source_id": batch.source_id,
        "batch_id": batch.batch_id,
        "records": select_nomenclature(inp),
        "traceability": {
            "source_id": batch.source_id,
            "batch_id": batch.batch_id,
            "source_package": "SOURCE-002-PACKAGE-001-CONTROLLED-1-6",
            "upstream_batch": "BATCH-SRC-002-M03-001"
        },
        "ref": f"{batch.batch_id}:OUTPUT"
    }},
    {"M04": "M04-PRODUCTION"}
)

initial = {
    "type":"FORMULATION_RECORDS",
    "source_id":"SRC-002",
    "batch_id":"BATCH-SRC-002-M03-001",
    "records":FORMULATIONS,
    "traceability":{
        "source_id":"SRC-002",
        "source_package":"SOURCE-002-PACKAGE-001-CONTROLLED-1-6",
        "upstream_batch":"BATCH-SRC-002-M02-001"
    },
    "ref":"BATCH-SRC-002-M03-001:OUTPUT"
}

result = runner.execute(
    "RUN-SRC-002-M04-001",
    {"source_id":"SRC-002","source_name":"GM Quality System Basics Overview — Supplier Audit"},
    "M04",
    initial,
)

print(json.dumps(result, ensure_ascii=False, indent=2))
