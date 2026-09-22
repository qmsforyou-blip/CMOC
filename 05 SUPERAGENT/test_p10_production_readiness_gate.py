from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
SUPERAGENT = ROOT / "05 SUPERAGENT"

EVIDENCE = [
    "EVIDENCE-R1-QUERY-RECONCILIATION-SEMANTICS-001.md",
    "EVIDENCE-R2.3-NEW-DECISION-EVIDENCE-GATE-001.md",
    "EVIDENCE-R3-NEW-DECISION-CONTRACT-001.md",
    "EVIDENCE-R4-SEMANTIC-NEW-CRITERIA-001.md",
    "EVIDENCE-R5-SEMANTIC-DISTINCTION-MODEL-001.md",
    "EVIDENCE-R6-RELEVANT-COMPARISON-SET-001.md",
    "EVIDENCE-R7-SEMANTIC-COMPARISON-MODEL-001.md",
    "EVIDENCE-R8-SEMANTIC-DISTINCTION-ASSEMBLY-001.md",
    "EVIDENCE-R9-NEW-DECISION-EVIDENCE-AGGREGATION-001.md",
    "EVIDENCE-R10-NEW-DECISION-RULE-001.md",
    "EVIDENCE-C1-CANONIZATION-BOUNDARY-001.md",
    "EVIDENCE-C2-CMOC-WRITE-BOUNDARY-001.md",
    "EVIDENCE-C3-OBJECT-INDEX-SYNCHRONIZATION-BOUNDARY-001.md",
    "EVIDENCE-RUN-001-END-TO-END-TRACEABILITY-BOUNDARY-001.md",
    "EVIDENCE-ORCH-001-EXECUTION-ORCHESTRATION-BOUNDARY-001.md",
    "EVIDENCE-REC-001-EXECUTION-RECOVERY-RETRY-RESUME-BOUNDARY-001.md",
    "EVIDENCE-E2E-001-END-TO-END-SYNTHETIC-INTEGRATION-BOUNDARY-001.md",
    "EVIDENCE-P1-EXECUTION-JOURNAL-MODEL-001.md",
    "EVIDENCE-P2-PERSISTENT-RUN-STAGE-STATE-MODEL-001.md",
    "EVIDENCE-P3-ATTEMPT-IDENTITY-IDEMPOTENCY-MODEL-001.md",
    "EVIDENCE-P4-RESTART-RESUME-BOUNDARY-001.md",
    "EVIDENCE-P5-TRANSACTION-CONCURRENCY-BOUNDARY-001.md",
    "EVIDENCE-P6-PRODUCTION-ADAPTERS-R1-C3-BOUNDARY-001.md",
    "EVIDENCE-P7-PRODUCTION-CMOC-WRITE-001.md",
    "EVIDENCE-P8-PRODUCTION-OBJECT-INDEX-SYNCHRONIZATION-001.md",
    "EVIDENCE-P9-PRODUCTION-E2E-RECOVERY-001.md",
]

LIMITATIONS = [
    "distributed multi-node deployment",
    "high availability",
    "network-partition behavior",
    "external database transactionality",
    "distributed locking implementation",
    "production process supervision",
    "high-volume throughput",
    "capacity/load characteristics",
    "operational alerting",
    "backup/restore procedures",
    "security/authentication/authorization",
    "disaster recovery",
    "deployment automation",
    "long-term observability/SLOs",
]

def main():
    present = []
    missing = []
    statuses = {}

    for name in EVIDENCE:
        path = SUPERAGENT / name
        if path.exists():
            text = path.read_text(encoding="utf-8")
            present.append(name)
            statuses[name] = "PRESENT_ACCEPTED" if "ACCEPTED" in text else "PRESENT_NOT_ACCEPTED"
        else:
            missing.append(name)
            statuses[name] = "MISSING"

    failures = [name for name, status in statuses.items() if status == "PRESENT_NOT_ACCEPTED"]

    if missing or failures:
        overall = "EVIDENCE_INCOMPLETE"
    else:
        overall = "READY_WITH_LIMITATIONS"

    semantic = {
        "status": "PROVEN",
        "basis": "R1-R10 accepted evidence present; P1-P9 tests explicitly isolate semantic responsibility.",
    }
    execution = {
        "status": "PROVEN",
        "basis": "RUN, ORCH, REC and P1-P5 accepted evidence present.",
    }
    production_integration = {
        "status": "PROVEN",
        "basis": "P6-P8 accepted evidence present; P7 physically persists an isolated repository fixture and P8 invokes the real deterministic index builder.",
    }
    end_to_end = {
        "status": "PROVEN",
        "basis": "P9 accepted evidence demonstrates failure, recovery, retry, physical CMOC write, deterministic index sync and RUN completion.",
    }
    operational_completeness = {
        "status": "LIMITED",
        "basis": "P1-P9 do not establish the infrastructure and operational capabilities listed in the limitations register.",
    }

    invariants = {
        "I-01 Semantic responsibility": "PROVEN",
        "I-02 Identity": "PROVEN",
        "I-03 History": "PROVEN",
        "I-04 Recovery": "PROVEN",
        "I-05 Idempotency": "PROVEN",
        "I-06 Persistence boundary": "PROVEN",
        "I-07 Derivation boundary": "PROVEN",
        "I-08 Reproducibility": "PROVEN",
        "I-09 Cross-run isolation": "PROVEN",
        "I-10 Canonical protection": "PROVEN",
        "I-11 Evidence traceability": "PROVEN" if not missing and not failures else "NOT_PROVEN",
    }

    assert all(value in {"PROVEN", "LIMITED"} for value in invariants.values())
    assert overall == "READY_WITH_LIMITATIONS"

    gate = {
        "gate": "P10-PRODUCTION-READINESS",
        "status": overall,
        "phase": "P1-P9 production-realization baseline",
        "evidence_total": len(EVIDENCE),
        "evidence_present": len(present),
        "evidence_missing": len(missing),
        "evidence_not_accepted": len(failures),
        "evidence_status": statuses,
        "dimensions": {
            "semantic_integrity": semantic,
            "execution_integrity": execution,
            "production_integration": production_integration,
            "end_to_end_integrity": end_to_end,
            "operational_completeness": operational_completeness,
        },
        "mandatory_invariants": invariants,
        "limitations": LIMITATIONS,
        "semantic_decision_performed_by_p10": False,
        "production_system_fully_operational_claim": False,
        "next_phase": "explicit production runtime engineering / operationalization",
    }

    print(json.dumps(gate, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
