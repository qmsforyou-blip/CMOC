from mvp_runner import Contract, Superagent, Batch
from m07_llm import build_relation_candidates

RUN_ID = "RUN-SRC-002-M07-002"
BATCH_ID = "BATCH-SRC-002-M07-002"
SOURCE_ID = "SRC-002"
SOURCE_PACKAGE = "SOURCE-002-PACKAGE-001-CONTROLLED-1-6"
UPSTREAM_BATCH = "BATCH-SRC-002-M06-001"

PASSPORTS = [
    {"id":"PAS-001","candidate_id":"NOM-001","source_id":SOURCE_ID,"term":"Quality Systems Basics source revision","working_class":"SOURCE_IDENTITY","source_basis":["FORM-001","FORM-002","FORM-003"]},
    {"id":"PAS-002","candidate_id":"NOM-002","source_id":SOURCE_ID,"term":"QSB 11-strategy set","working_class":"COLLECTION","source_basis":["FORM-004","FORM-005","FORM-006"]},
    {"id":"PAS-003","candidate_id":"NOM-003","source_id":SOURCE_ID,"term":"Red-rated strategy workshop identification","working_class":"DECISION","source_basis":["FORM-007","FORM-008","FORM-009"]},
    {"id":"PAS-004","candidate_id":"NOM-004","source_id":SOURCE_ID,"term":"Red and Yellow Audit question strategy delivery and action planning","working_class":"ACTIVITY","source_basis":["FORM-010","FORM-011","FORM-012"]},
    {"id":"PAS-005","candidate_id":"NOM-005","source_id":SOURCE_ID,"term":"QSB common principles, methods, processes, and global language","working_class":"CONCEPT_MODEL","source_basis":["FORM-013","FORM-014","FORM-015"]},
    {"id":"PAS-006","candidate_id":"NOM-006","source_id":SOURCE_ID,"term":"Fast Response visual management","working_class":"STRATEGY","source_basis":["FORM-016","FORM-017","FORM-018"]},
    {"id":"PAS-007","candidate_id":"NOM-007","source_id":SOURCE_ID,"term":"Fast Response and Problem Solving section separation","working_class":"STRUCTURAL_DISTINCTION","source_basis":["FORM-019","FORM-020","FORM-021"]},
]

RELATION_EVIDENCE = [
    {
        "evidence_id": "EVID-SRC-002-P2-STRATEGY-SET-001",
        "locations": ["p2"],
        "text": "11 QSB strategies: Fast Response; Control of Non-Conforming Product; Verification Station; Standardized Operations; Standardized Operator Training; Error Proofing Verification; Layered Process Audits; RPN Risk Reduction; Contamination Control; Supply Chain Management; Managing Change.",
        "supports": ["PAS-002", "PAS-006"],
    }
]

def m07(source_input, batch):
    records = build_relation_candidates(
        source_input["records"],
        source_input["relation_evidence"],
    )
    return {
        "status": "ACCEPT",
        "type": "RELATION_CANDIDATES",
        "source_id": batch.source_id,
        "batch_id": batch.batch_id,
        "records": records,
        "traceability": {
            "source_id": batch.source_id,
            "batch_id": batch.batch_id,
            "source_package": SOURCE_PACKAGE,
            "upstream_batch": UPSTREAM_BATCH,
            "passport_ids": [p["id"] for p in source_input["records"]],
            "relation_evidence_ids": [e["evidence_id"] for e in source_input["relation_evidence"]],
        },
        "ref": f"{batch.batch_id}:OUTPUT",
    }

contract = Contract(
    task="M07",
    accepted_inputs={"PASSPORT_RECORDS"},
    output_type="RELATION_CANDIDATES",
    required_input_fields={"records", "relation_evidence"},
    required_output_fields={"source_id","batch_id","records","traceability","ref"},
)

class ControlledBatchSuperagent(Superagent):
    def new_batch(self, source_id, task, input_ref, handoff_id=None):
        return Batch(BATCH_ID, source_id, task, input_ref, handoff_id)

runner = ControlledBatchSuperagent(
    contracts={"M07": contract},
    handlers={"M07": m07},
    machine_ids={"M07": "M07-PRODUCTION"},
)

source_input = {
    "type": "PASSPORT_RECORDS",
    "source_id": SOURCE_ID,
    "records": PASSPORTS,
    "relation_evidence": RELATION_EVIDENCE,
    "traceability": {
        "source_id": SOURCE_ID,
        "source_package": SOURCE_PACKAGE,
        "upstream_batch": UPSTREAM_BATCH,
    },
}

result = runner.execute(
    run_id=RUN_ID,
    source={"source_id": SOURCE_ID},
    task="M07",
    inp=source_input,
)

import json
print(json.dumps(result, ensure_ascii=False, indent=2))
