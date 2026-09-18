# CAN-001 — Canonization Decision Record

- SOURCE_ID: SRC-002
- BATCH_ID: BATCH-SRC-002-M08-001
- TASK: M08 CANONIZATION DECISION
- INPUT: REL-001
- DECISION: NEEDS_EVIDENCE
- EXTERNAL_KNOWLEDGE: NONE

## Decision basis

Object boundary is not unambiguous: p.2 supports that strategies form a set, but the direction `STRATEGY_SET MEMBER_OF STRATEGY` conflicts with the ordinary set/member direction; exact relation semantics require clarification.

## Evidence gap

EVIDENCE_GAP: exact direction/semantics of the MEMBER_OF relation must be established before treating the candidate as an established relation.

## Rule

Source evidence → Object Boundary → Type Assignment → decision.

CANONICAL is not assigned merely because one source supports a candidate.

## Traceability

SRC-002 → M07 REL-001 → M08 CAN-001
