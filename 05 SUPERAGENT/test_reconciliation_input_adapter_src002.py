#!/usr/bin/env python3
"""A3-IMPLEMENTATION-GATE control test for the read-only adapter.

The seven records reproduce the production M06 SRC-002 identity/basis fields
confirmed by EVIDENCE-M06-SRC-002-001. The test does not invoke LLM, QUERY,
OBJECT INDEX, or reconciliation.py.
"""
from copy import deepcopy

from reconciliation_input_adapter import build_reconciliation_input


PASSPORT_CLASSES = ["SOURCE_IDENTITY", "COLLECTION", "DECISION", "ACTIVITY", "CONCEPT_MODEL", "STRATEGY", "STRUCTURAL_DISTINCTION"]

PASSPORT_TERMS = [
    ("PAS-001", "NOM-001", "CLS-001", "Quality Systems Basics source revision", ["FORM-001", "FORM-002", "FORM-003"]),
    ("PAS-002", "NOM-002", "CLS-002", "QSB 11-strategy set", ["FORM-004", "FORM-005", "FORM-006"]),
    ("PAS-003", "NOM-003", "CLS-003", "Red-rated strategy workshop identification", ["FORM-007", "FORM-008", "FORM-009"]),
    ("PAS-004", "NOM-004", "CLS-004", "Red and Yellow Audit question strategy delivery and action planning", ["FORM-010", "FORM-011", "FORM-012"]),
    ("PAS-005", "NOM-005", "CLS-005", "QSB common principles, methods, processes, and global language", ["FORM-013", "FORM-014", "FORM-015"]),
    ("PAS-006", "NOM-006", "CLS-006", "Fast Response visual management", ["FORM-016", "FORM-017", "FORM-018"]),
    ("PAS-007", "NOM-007", "CLS-007", "Fast Response and Problem Solving section separation", ["FORM-019", "FORM-020", "FORM-021"]),
]


def make_fixture():
    return {
        "status": "ACCEPT",
        "type": "PASSPORT_RECORDS",
        "source_id": "SRC-002",
        "batch_id": "BATCH-SRC-002-M06-006",
        "records": [
            {
                "id": passport_id,
                "candidate_id": candidate_id,
                "classification_id": classification_id,
                "source_id": "SRC-002",
                "term": term,
                "working_class": "PRODUCTION_CONFIRMED",
                "lifecycle_status": "ЧЕРНОВИК",
                "epistemic_status": "PROVISIONAL",
                "source_basis": basis,
            }
            for (passport_id, candidate_id, classification_id, term, basis), working_class in zip(PASSPORT_TERMS, PASSPORT_CLASSES)
        ],
        "traceability": {
            "source_id": "SRC-002",
            "source_package": "SOURCE-002-PACKAGE-001-CONTROLLED-1-6",
            "discovery_run": "RUN-SRC-002-AUTOMATED-M01-M08-001",
            "upstream_batch": "BATCH-SRC-002-M05-001",
        },
        "ref": "BATCH-SRC-002-M06-006:OUTPUT",
    }


def main():
    source = make_fixture()
    before = deepcopy(source)

    result = build_reconciliation_input(source, ["TERMS"])

    assert result["source_id"] == "SRC-002"
    assert result["input_batch_id"] == "BATCH-SRC-002-M06-006"
    assert result["input_output_type"] == "PASSPORT_RECORDS"
    assert result["query_scope"] == ["TERMS"]
    assert len(result["records"]) == 7

    for adapted, (_, _, _, term, basis) in zip(result["records"], PASSPORT_TERMS):
        assert adapted["value"] == term
        assert adapted["traceability"]["source_basis"] == basis
        assert "target_object_type" not in adapted
        assert "cmoc_object_id" not in adapted
        assert "match_result" not in adapted
        assert "decision" not in adapted

    assert source == before, "Adapter mutated source-bound Passport output"

    print("A3-IMPLEMENTATION-GATE: PASS")
    print("records: 7")
    print("source_id: SRC-002")
    print("input_batch_id: BATCH-SRC-002-M06-006")
    print("query_invocation: NONE")
    print("cmoc_access: NONE")
    print("source_mutation: NONE")
    print("target_object_type_inference: NONE")


if __name__ == "__main__":
    main()
