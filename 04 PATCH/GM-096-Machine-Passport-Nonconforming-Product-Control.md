# GM-096 — Machine Candidate Passport: Nonconforming Product Control

**Source:** GM Quality Systems Basics rev. March 2009
**Provenance:** GM SOURCE → SOURCE-FINAL → Distinctions → Mechanisms → Machine Candidates → Catalog Cross-Check
**Status:** MACHINE-CANDIDATE / NON-CANON
**Candidate:** Nonconforming Product Control

## 1. Identity

**Candidate type:** containment / disposition-control machine candidate

**Primary source realization:** Control of Non-Conforming Product

## 2. Problem

A nonconforming product condition must not result in unintended use or release. Identification alone is insufficient; the organization needs a controlled path from detection through containment, disposition and follow-up.

## 3. Input

A product, lot, component or process output identified or suspected as nonconforming against an applicable requirement/specification.

## 4. Trigger

Detection or identification of nonconformance.

## 5. Operating sequence

`Detection → Identification → Containment / Segregation → Disposition → Release / Rework / Scrap as authorized → Record → Follow-up / Corrective Action where required`

The exact disposition alternatives depend on the applicable GM requirements and local process controls; this passport does not infer alternatives beyond the source-derived architecture.

## 6. Output

A controlled product state in which the nonconforming material is prevented from unintended use/release and receives an authorized disposition.

## 7. State transition

`UNCONTROLLED / SUSPECT PRODUCT → IDENTIFIED NONCONFORMANCE → CONTAINED → DISPOSITIONED → RELEASED / REWORKED / SCRAPPED`

Where corrective action is required, a further transition is initiated from the problem into the appropriate problem-resolution process.

## 8. Owner / responsibility

Responsibility is assigned within the affected process and quality organization according to the applicable control procedure. The precise organizational role names vary by site/process; no unsupported role assignment is made here.

## 9. Evidence

Source-derived evidence can include:

- identification/segregation status;
- nonconforming-product record;
- disposition decision;
- rework/scrap/release record as applicable;
- traceability information;
- follow-up/corrective-action record where required.

## 10. Acceptance condition

The immediate control objective is satisfied when the nonconforming product is under controlled disposition and cannot be unintentionally used or released.

The completion of containment is **not** automatically proof that the systemic cause has been eliminated.

## 11. Failure / STOP conditions

The machine fails its control objective when nonconforming or suspect product can proceed into unintended use/release without the required identification, containment or authorized disposition.

## 12. Distinctions implemented

- Detection ≠ Control
- Problem ≠ Corrective Action
- Identification ≠ Containment
- Containment ≠ Cause Elimination
- Disposition ≠ Corrective Action
- Record ≠ Evidence of Systemic Effectiveness

## 13. Boundary

Nonconforming Product Control does **not**:

- establish the root cause by itself;
- replace systemic problem solving;
- prove process capability merely because product has been segregated;
- authorize arbitrary release of nonconforming material;
- substitute final inspection for process control.

Its precise boundary is:

> **Prevent unintended use or release of nonconforming product and move the affected product through an authorized, traceable disposition path.**

## 14. Relationship to other candidate Machines

### Nonconforming Product Control → Systemic Problem Resolution

Containment/disposition controls the immediate product condition. Systemic Problem Resolution investigates why the condition occurred and whether the management/control system requires correction.

### Nonconforming Product Control ↔ Fast Response

Fast Response may provide the rapid escalation/containment context in which nonconforming-product control is initiated. They should not be collapsed without testing their boundaries.

### Nonconforming Product Control ↔ Process Verification

Verification may detect the nonconformance; this machine controls the affected product after detection.

## 15. Reusability hypothesis

The candidate is potentially reusable for any production or service environment where nonconforming output must be identified, contained, dispositioned and prevented from unintended release.

This broader reuse remains a CMOC hypothesis and requires confirmation from additional sources.

## 16. Canonization assessment

**Candidate strength:** STRONG

**Independent boundary:** YES

**Trigger/input:** YES

**Containment/disposition sequence:** YES

**State transition:** YES

**Responsible role:** YES at process level; exact role mapping varies by implementation

**Evidence:** YES

**Acceptance/closure condition:** YES for immediate product-control objective

**Cross-source confirmation:** NOT YET ESTABLISHED

**Existing-machine duplication:** requires comparison with existing CMOC containment / nonconformity / response Machines before promotion.

**Canon status:** NON-CANON.

## 17. Architectural observation

This candidate demonstrates a critical separation:

`Detection → Containment`

is not the same as:

`Problem → Root Cause → Systemic Corrective Action`

Therefore the product-control Machine and problem-resolution Machine may form a sequence without being the same Machine:

`Nonconformance Detected → Product Controlled → Disposition → Systemic Problem Resolution → Effectiveness Verification`

The source-derived architecture supports this separation but does not by itself establish the final CMOC decomposition.

## 18. Status

**SOURCE-DERIVED / MACHINE-CANDIDATE / NON-CANON**

No REG-001 modification.
No Canon modification.
No existing Machine modified.

**Next candidate:** Systemic Problem Resolution (currently HOLD for comparison with existing CMOC problem-solving architecture).