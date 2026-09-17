# GM-096 — Final Map → CMOC

**Извещение на изменение:** 0136+170926

## 1. Источник

GM Quality System Basics rev March 2009 — Managing Change, pp. 324–345.

## 2. Итоговая карта

### MACHINE CANDIDATES

| ID | GM construction | CMOC status | Role |
|---|---|---|---|
| MC-CAND-096-01 | Plant Process Change Control | STRONG-CANDIDATE / NON-CANON | Entry / governance of process change |
| MC-CAND-096-02 | Production Trial Run | SPECIALIZED-CANDIDATE / NON-CANON | Controlled production trial |
| MC-CAND-096-03 | Banking Process | SPECIALIZED-CANDIDATE / NON-CANON | Controlled material state outside normal flow |
| MC-CAND-096-04 | Bypass Process Control | SPECIALIZED-CANDIDATE / NON-CANON | Controlled bypass state and return |

### PATTERNS

- Measurement-to-Action
- Response to Abnormality
- Assessment against Criterion
- Controlled Deviation abstraction

### MECHANISMS

- Decision Gate
- Control Means Verification
- Controlled Change Implementation
- Process Verification
- change registration / traceability
- stakeholder notification
- approval before execution
- verification before re-entry

### ASSEMBLIES

- Workshop / Action-Plan Conversion
- broader Managing Change Chain

### EXISTING MACHINES / NEW PROVENANCE

- LPA → `MC-009-15 Audit`
- Fast Response → `MC-009-10 Andon` + `MP-002 Response to Abnormality`
- Systemic Problem Resolution → `MP-003 Problem Solving`
- other quality / contamination / verification constructions remain existing
  architecture or require separate source-level cross-check.

## 3. Managing Change as Chain

CMOC interpretation:

`CHANGE / CHANGE NEED`
→ `PPCR`
→ `DECISION: PTR REQUIRED?`
→ `PTR`
→ `EVALUATION / VERIFICATION`
→ `IMPLEMENTED STATE`
→ one of controlled states / flows:
  - `NORMAL FLOW`
  - `BANKING`
  - `BYPASS`
→ `VERIFICATION / REVIEW`
→ `ACCEPTED / CLOSED`

This is a CMOC architectural interpretation. GM QSB does not present this
exact unified diagram in the reviewed pages.

## 4. Four governing questions

1. **Can we change?** → Plant Process Change Control.
2. **Do we need to test first?** → Production Trial Run.
3. **What happens to material outside the normal flow?** → Banking Process.
4. **What happens when the normal process is temporarily unavailable or bypassed?**
   → Bypass Process Control.

## 5. What GM-096 adds to CMOC

The major contribution of GM-096 is not a large number of independent Machine
names. It provides a coherent example of how a managed system controls
transition between states while preserving:

- identification;
- responsibility;
- decision points;
- evidence;
- authorization;
- verification;
- traceability;
- controlled return / closure.

This strengthens the CMOC distinction between:

`Machine ≠ Mechanism ≠ Pattern ≠ Assembly ≠ Provenance`.

## 6. Catalog decision

Do **not** promote any GM-096 candidate to Canon at this stage.

Do **not** update the main Machine Catalog from this source alone.

The four passports remain candidate passports and require independent-source
cross-check before possible promotion.

## 7. Evidence status

`SINGLE-SOURCE / GM QSB`

The four Machine candidates are not yet multi-source confirmed.

## 8. Governance impact

REG-001: unchanged.

Canon: unchanged.

MACHINE-CATALOG: unchanged.

Candidate passports: four created.

Cross-check patches: completed.

## 9. Final verdict

**GM-096 / Managing Change is best represented in CMOC as a change-control
Chain containing four specialized Machine candidates plus reusable Patterns,
Mechanisms, Assemblies and provenance links to existing Machines.**

**Status: CROSS-CHECK COMPLETE / NON-CANON.**

## 10. Next evidence work

For each of the four candidates, seek independent sources and test:

`bounded identity → reproducibility → distinct output → roles/artifacts →
non-duplication → cross-domain stability`.

Only after that test consider `MULTI-SOURCE CONFIRMED` and subsequent
catalog/canon decisions.
