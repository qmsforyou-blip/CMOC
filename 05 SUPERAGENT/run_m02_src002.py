import json
from mvp_runner import Superagent, Contract
from m02_llm import extract_distinctions

# Production M01 output, recorded from RUN-SRC-002-M01-001
records = [
    {
        "id": "EX-001",
        "location": "p1",
        "observation": "The Quality Systems Basics source is identified as revision March 2009.",
        "source_quote_or_evidence": "Quality Systems Basics rev March 2009.",
        "uncertainty": "CLEAR",
        "source_id": "SRC-002"
    },
    {
        "id": "EX-002",
        "location": "p2",
        "observation": "Quality Systems Basics defines 11 strategies: Fast Response; Control of Non-Conforming Product; Verification Station; Standardized Operations; Standardized Operator Training; Error Proofing Verification; Layered Process Audits; RPN Risk Reduction; Contamination Control; Supply Chain Management; and Managing Change.",
        "source_quote_or_evidence": "11 QSB Strategies: Fast Response; Control of Non-Conforming Product; Verification Station; Standardized Operations; Standardized Operator Training; Error Proofing Verification; Layered Process Audits; RPN Risk Reduction; Contamination Control; Supply Chain Management; Managing Change.",
        "uncertainty": "CLEAR",
        "source_id": "SRC-002"
    },
    {
        "id": "EX-003",
        "location": "p3",
        "observation": "The supplier is assessed using the latest QSB Audit to identify strategies rated Red that require a workshop.",
        "source_quote_or_evidence": "assess supplier per Latest QSB Audit to determine strategies Red and requiring workshop",
        "uncertainty": "CLEAR",
        "source_id": "SRC-002"
    },
    {
        "id": "EX-004",
        "location": "p3",
        "observation": "Required strategies are delivered, and an Action Plan is obtained for all Red and Yellow Audit questions.",
        "source_quote_or_evidence": "deliver strategies as required and obtain Action Plan for all Red and Yellow Audit questions",
        "uncertainty": "CLEAR",
        "source_id": "SRC-002"
    },
    {
        "id": "EX-005",
        "location": "p4",
        "observation": "Quality Systems Basics uses common principles, common methods, and common processes, with a focus on one global language.",
        "source_quote_or_evidence": "Common Principles, Common Methods, Common Processes. Focus — ONE LANGUAGE GLOBALLY.",
        "uncertainty": "CLEAR",
        "source_id": "SRC-002"
    },
    {
        "id": "EX-006",
        "location": "p5",
        "observation": "Fast Response is intended to solve problems faster and earlier upstream through visual management.",
        "source_quote_or_evidence": "solving problems faster & earlier upstream through visual management",
        "uncertainty": "CLEAR",
        "source_id": "SRC-002"
    },
    {
        "id": "EX-007",
        "location": "p6",
        "observation": "Fast Response separates section 1.2 Fast Response from section 1.3 Problem Solving.",
        "source_quote_or_evidence": "Fast Response separates 1.2 Fast Response from 1.3 Problem Solving.",
        "uncertainty": "CLEAR",
        "source_id": "SRC-002"
    }
]

contracts = {
    "M02": Contract(
        "M02",
        {"EXTRACTION_RECORDS"},
        "DISTINCTION_RECORDS",
        {"source_id", "batch_id", "records", "traceability", "ref"},
    )
}

runner = Superagent(
    contracts,
    {
        "M02": lambda inp, batch: {
            "status": "ACCEPT",
            "type": "DISTINCTION_RECORDS",
            "source_id": batch.source_id,
            "batch_id": batch.batch_id,
            "records": extract_distinctions(inp),
            "traceability": {
                "source_id": batch.source_id,
                "batch_id": batch.batch_id,
                "from": inp["traceability"],
            },
            "ref": f"{batch.batch_id}:OUTPUT",
        }
    },
    {"M02": "M02-PRODUCTION"},
)

initial = {
    "type": "EXTRACTION_RECORDS",
    "source_id": "SRC-002",
    "records": records,
    "traceability": {
        "source_id": "SRC-002",
        "source_package": "SOURCE-002-PACKAGE-001-CONTROLLED-1-6",
        "upstream_batch": "BATCH-SRC-002-M01-001",
    },
    "ref": "BATCH-SRC-002-M01-001:OUTPUT",
}

result = runner.execute(
    "RUN-SRC-002-M02-001",
    {"source_id": "SRC-002", "source_name": "GM Quality System Basics Overview — Supplier Audit"},
    "M02",
    initial,
)

print(json.dumps(result, ensure_ascii=False, indent=2))
