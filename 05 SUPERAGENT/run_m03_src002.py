import json
from mvp_runner import Superagent, Contract
from m03_llm import formulate

records = [
    {
        "id": "DIS-001",
        "extraction_id": "EX-001",
        "distinction": "Identifies the Quality Systems Basics source as the March 2009 revision.",
        "uncertainty": "CLEAR",
        "source_id": "SRC-002"
    },
    {
        "id": "DIS-002",
        "extraction_id": "EX-002",
        "distinction": "Defines 11 QSB strategies: Fast Response; Control of Non-Conforming Product; Verification Station; Standardized Operations; Standardized Operator Training; Error Proofing Verification; Layered Process Audits; RPN Risk Reduction; Contamination Control; Supply Chain Management; and Managing Change.",
        "uncertainty": "CLEAR",
        "source_id": "SRC-002"
    },
    {
        "id": "DIS-003",
        "extraction_id": "EX-003",
        "distinction": "Requires assessment of the supplier using the latest QSB Audit to identify Red-rated strategies requiring a workshop.",
        "uncertainty": "CLEAR",
        "source_id": "SRC-002"
    },
    {
        "id": "DIS-004",
        "extraction_id": "EX-004",
        "distinction": "Requires delivery of applicable strategies and an Action Plan for every Red and Yellow Audit question.",
        "uncertainty": "CLEAR",
        "source_id": "SRC-002"
    },
    {
        "id": "DIS-005",
        "extraction_id": "EX-005",
        "distinction": "Defines QSB as using common principles, methods, and processes with a focus on one global language.",
        "uncertainty": "CLEAR",
        "source_id": "SRC-002"
    },
    {
        "id": "DIS-006",
        "extraction_id": "EX-006",
        "distinction": "Defines Fast Response as solving problems faster and earlier upstream through visual management.",
        "uncertainty": "CLEAR",
        "source_id": "SRC-002"
    },
    {
        "id": "DIS-007",
        "extraction_id": "EX-007",
        "distinction": "Separates section 1.2 Fast Response from section 1.3 Problem Solving.",
        "uncertainty": "CLEAR",
        "source_id": "SRC-002"
    }
]

contracts = {
    "M03": Contract(
        "M03",
        {"DISTINCTION_RECORDS"},
        "FORMULATION_RECORDS",
        {"source_id", "batch_id", "records", "traceability", "ref"},
    )
}

runner = Superagent(
    contracts,
    {
        "M03": lambda inp, batch: {
            "status": "ACCEPT",
            "type": "FORMULATION_RECORDS",
            "source_id": batch.source_id,
            "batch_id": batch.batch_id,
            "records": formulate(inp),
            "traceability": {
                "source_id": batch.source_id,
                "batch_id": batch.batch_id,
                "from": inp["traceability"],
            },
            "ref": f"{batch.batch_id}:OUTPUT",
        }
    },
    {"M03": "M03-PRODUCTION"},
)

initial = {
    "type": "DISTINCTION_RECORDS",
    "source_id": "SRC-002",
    "records": records,
    "traceability": {
        "source_id": "SRC-002",
        "source_package": "SOURCE-002-PACKAGE-001-CONTROLLED-1-6",
        "upstream_batch": "BATCH-SRC-002-M02-001",
    },
    "ref": "BATCH-SRC-002-M02-001:OUTPUT",
}

result = runner.execute(
    "RUN-SRC-002-M03-001",
    {"source_id": "SRC-002", "source_name": "GM Quality System Basics Overview — Supplier Audit"},
    "M03",
    initial,
)

print(json.dumps(result, ensure_ascii=False, indent=2))
