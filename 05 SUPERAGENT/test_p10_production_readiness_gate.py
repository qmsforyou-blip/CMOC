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
    "EVIDENCE-C3-OBJECT-INDEX-SYNCHRONIZATION-001.md",
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


def accepted(name, statuses):
    return statuses.get(name) == "PRESENT_ACCEPTED"


def all_accepted(names, statuses):
    return all(accepted(name, statuses) for name in names)


def main():
    statuses = {}

    for name in EVIDENCE:
        path = SUPERAGENT / name
        if not path.exists():
            statuses[name] = "MISSING"
            continue
        text = path.read_text(encoding="utf-8")
        statuses[name] = (
            "PRESENT_ACCEPTED"
            if "ACCEPTED" in text
            else "PRESENT_NOT_ACCEPTED"
        )

    present = [name for name, status in statuses.items()
               if status != "MISSING"]
    missing = [name for name, status in statuses.items()
               if status == "MISSING"]
    failures = [name for name, status in statuses.items()
                if status == "PRESENT_NOT_ACCEPTED"]

    semantic_names = EVIDENCE[:10]
    execution_names = [
        "EVIDENCE-RUN-001-END-TO-END-TRACEABILITY-BOUNDARY-001.md",
        "EVIDENCE-ORCH-001-EXECUTION-ORCHESTRATION-BOUNDARY-001.md",
        "EVIDENCE-REC-001-EXECUTION-RECOVERY-RETRY-RESUME-BOUNDARY-001.md",
        "EVIDENCE-P1-EXECUTION-JOURNAL-MODEL-001.md",
        "EVIDENCE-P2-PERSISTENT-RUN-STAGE-STATE-MODEL-001.md",
        "EVIDENCE-P3-ATTEMPT-IDENTITY-IDEMPOTENCY-MODEL-001.md",
        "EVIDENCE-P4-RESTART-RESUME-BOUNDARY-001.md",
        "EVIDENCE-P5-TRANSACTION-CONCURRENCY-BOUNDARY-001.md",
    ]
    production_names = [
        "EVIDENCE-P6-PRODUCTION-ADAPTERS-R1-C3-BOUNDARY-001.md",
        "EVIDENCE-P7-PRODUCTION-CMOC-WRITE-001.md",
        "EVIDENCE-P8-PRODUCTION-OBJECT-INDEX-SYNCHRONIZATION-001.md",
    ]
    e2e_names = [
        "EVIDENCE-E2E-001-END-TO-END-SYNTHETIC-INTEGRATION-BOUNDARY-001.md",
        "EVIDENCE-P9-PRODUCTION-E2E-RECOVERY-001.md",
    ]

    semantic = {
        "status": "PROVEN" if all_accepted(semantic_names, statuses) else "NOT_PROVEN",
        "basis": "R1-R10 accepted evidence is required.",
    }
    execution = {
        "status": "PROVEN" if all_accepted(execution_names, statuses) else "NOT_PROVEN",
        "basis": "RUN, ORCH, REC and P1-P5 accepted evidence is required.",
    }
    production_integration = {
        "status": "PROVEN" if all_accepted(production_names, statuses) else "NOT_PROVEN",
        "basis": "P6-P8 accepted evidence is required.",
    }
    end_to_end = {
        "status": "PROVEN" if all_accepted(e2e_names, statuses) else "NOT_PROVEN",
        "basis": "E2E and P9 accepted evidence is required.",
    }
    operational_completeness = {
        "status": "LIMITED",
        "basis": "P1-P9 do not establish the infrastructure and operational capabilities listed in the limitations register.",
    }

    invariants = {
        "I-01 Semantic responsibility": semantic["status"],
        "I-02 Identity": execution["status"],
        "I-03 History": execution["status"],
        "I-04 Recovery": execution["status"],
        "I-05 Idempotency": execution["status"],
        "I-06 Persistence boundary": production_integration["status"],
        "I-07 Derivation boundary": production_integration["status"],
        "I-08 Reproducibility": production_integration["status"],
        "I-09 Cross-run isolation": execution["status"],
        "I-10 Canonical protection": production_integration["status"],
        "I-11 Evidence traceability": (
            "PROVEN" if not missing and not failures else "NOT_PROVEN"
        ),
    }

    if failures:
        overall = "NOT_READY"
    elif missing:
        overall = "EVIDENCE_INCOMPLETE"
    else:
        overall = "READY_WITH_LIMITATIONS"

    gate = {
        "gate": "P10-PRODUCTION-READINESS",
        "status": overall,
        "phase": "P1-P9 production-realization baseline",
        "evidence_total": len(EVIDENCE),
        "evidence_present": len(present),
        "evidence_missing": len(missing),
        "evidence_not_accepted": len(failures),
        "missing_evidence": missing,
        "not_accepted_evidence": failures,
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
