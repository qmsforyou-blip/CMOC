# EVIDENCE-R3 — NEW DECISION CONTRACT

**Status:** ACCEPTED  
**Contract:** `R3-NEW-DECISION-CONTRACT-001.md`  
**Scope:** synthetic / architecture-boundary validation

## Result

The R3 test gate passed the required NEW decision branches:

- complete eligible candidate → `NEW_APPROVED`;
- insufficient scope → `NEW_REJECTED`;
- unknown target type → `NEW_REJECTED`;
- unresolved structural candidate → `NEW_REJECTED`;
- ambiguous candidate → `NEW_REJECTED`;
- eligible candidate with unknown evidence → `NEW_REJECTED`.

## Boundary controls

The gate verified:

- no object ID creation;
- no canonization;
- no relation creation;
- no CMOC write;
- production runtime remains blocked;
- eligibility does not itself constitute canonization or persistence.

R3 therefore establishes the NEW decision boundary without absorbing C1/C2 responsibilities.

**Evidence status: ACCEPTED.**
