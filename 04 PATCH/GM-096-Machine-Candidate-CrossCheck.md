# GM-096 — Machine Candidate Cross-Check

**Source:** GM Quality Systems Basics rev. March 2009
**Basis:** `GM-096-Machine-Candidates.md` + current `03_MACHINE-CATALOG/MACHINES/MACHINE-CANDIDATES.md`
**Status:** SOURCE-DERIVED / CROSS-CHECK / NON-CANON

## Purpose

This patch records the comparison of GM-derived Machine Candidates against the current CMOC Machine Candidate catalog before any new Machine is admitted.

The current catalog contains, among others, `MC-CAND-012-01 — Upstream Quality Stabilization`, `MC-CAND-013-02 — Day-One Kaizen Launch` and `MC-CAND-013-03 — Transformation Role Installation`. The catalog also preserves source status and provenance rather than treating candidates as Canon. 

## Cross-check results

### 1. Decision Gate

**Result: NEW / STRONG CANDIDATE**

No direct equivalent was identified in the current Machine-Candidates catalog.

The GM PPCR flow provides a sufficiently independent mechanism: review → approval/rejection → required approvals → written proceed/stop.

**Action:** retain as a new GM-derived candidate. Do not canonize yet.

### 2. Controlled Change Implementation

**Result: NEW / STRONG CANDIDATE, with parent-relation question**

The candidate is distinct from Decision Gate because it begins after authorization and concerns execution plus recording of the actual implementation event.

However, before canonization, test whether it is better represented as a state-transition submachine of a broader Change Machine rather than an independent top-level Machine.

**Action:** retain as candidate; do not canonize yet.

### 3. Production Trial Run

**Result: NEW / STRONG CANDIDATE**

No direct equivalent was identified in the current catalog.

GM gives PTR a clear boundary: requirement for trial → readiness → controlled trial → evaluation → acceptance/rejection.

**Action:** retain as new candidate.

### 4. Bypass Process Control

**Result: NEW / STRONG CANDIDATE**

No direct equivalent was identified in the current catalog.

The GM source provides a distinctive bounded process state with entry and exit breakpoints, alternative controls, inspection/audit and verified return.

**Action:** retain as new candidate.

### 5. Supplier Capability Assessment

**Result: NEW / STRONG CANDIDATE**

The current candidate `Upstream Quality Stabilization` is related but not equivalent. Upstream Quality Stabilization addresses input conformance stabilization / upstream cause elimination, whereas Supplier Capability Assessment determines and develops supplier capability through assessment, gap/status, action and reassessment.

**Action:** retain as separate candidate; later test whether both belong under a broader External Capability Management architecture.

### 6. Systemic Problem Resolution

**Result: HOLD / RELATIONSHIP CHECK**

GM's Drill Deep & Wide / 3×5 Why is strong evidence for systemic problem resolution. However, existing CMOC candidate and mechanism families around response, problem solving and transformation may overlap.

**Action:** do not create a new catalog entry until existing problem-solving candidates are compared at mechanism/state-transition level.

### 7. Nonconforming Product Control

**Result: NEW / STRONG CANDIDATE**

No direct equivalent was identified in the current candidate catalog.

The mechanism has an independent operational boundary around identification, control/segregation, disposition and follow-up of nonconforming product.

**Action:** retain as new candidate; later compare against any existing NCR/NCP mechanisms before canonization.

### 8. Workshop / Action-Plan Conversion

**Result: HOLD / ARCHITECTURAL CHECK**

The existing catalog contains transformation-oriented candidates such as Day-One Kaizen Launch and Transformation Role Installation. These are not proven duplicates, but the GM Workshop mechanism may overlap with the broader transformation/action architecture.

**Action:** keep as provisional candidate; compare purpose, input, output and state transition before creating a separate catalog object.

### 9. Layered / Repeated Verification

**Result: HOLD / POSSIBLE EXISTING AUDIT FAMILY**

GM LPA is a repeated verification mechanism with defined levels and action follow-up. It may be a specialized implementation of a broader Audit or Process Verification Machine.

**Action:** do not create a duplicate until existing Audit-family objects are checked at mechanism level.

### 10. Error-Proofing Verification

**Result: HOLD / SUBMECHANISM**

The mechanism may be a specialized implementation of Control Means Verification rather than an independent Machine.

**Action:** retain in GM mechanism/candidate layer; no new top-level Machine yet.

### 11. Measurement-to-Action Control Loop

**Result: PATTERN / NOT A MACHINE**

The loop occurs across multiple QSB strategies and therefore appears to be a reusable CMOC control pattern rather than an independently instantiated Machine.

**Action:** keep at Mechanism/Pattern level.

### 12. Control Means Verification

**Result: PATTERN / SUBMECHANISM**

Potentially fundamental, but currently more naturally treated as a reusable submechanism inside Verification, Error-Proofing and Contamination Control.

**Action:** no separate Machine.

### 13. Fast Response

**Result: HOLD / POSSIBLE RESPONSE FAMILY**

The source strategy is composite: detection, containment, communication, ownership, escalation and follow-up. It may overlap existing response/Andon architecture.

**Action:** no new Machine until mechanism decomposition and comparison are complete.

### 14. Contamination Control

**Result: MECHANISM FAMILY / NOT A MACHINE**

The section contains multiple distinct controls rather than one independent Machine boundary.

**Action:** retain as mechanism family.

## Preliminary Tier A after cross-check

The GM source currently produces five clean new candidates that should proceed to passportization:

1. **Decision Gate**
2. **Controlled Change Implementation**
3. **Production Trial Run**
4. **Bypass Process Control**
5. **Supplier Capability Assessment**
6. **Nonconforming Product Control**

Six candidates, not five. The numbered list is authoritative.

## Tier B — require architectural comparison

- Systemic Problem Resolution
- Workshop / Action-Plan Conversion
- Layered / Repeated Verification
- Error-Proofing Verification
- Fast Response
- Controlled Deviation

## Mechanism / Pattern — do not promote to Machine now

- Requirement Operationalization
- Measurement-to-Action Control Loop
- Control Means Verification
- Process Verification
- Supplier Performance Statusing
- State Representation / Statusing
- Standardization as Control
- Contamination Control as a whole
- Final Acceptance / Closure Gate as a separate Machine

## Important correction to the working discussion

The earlier preliminary table used a seven-item Tier A. After the explicit catalog cross-check, the clean new set is **six**: Decision Gate, Controlled Change Implementation, Production Trial Run, Bypass Process Control, Supplier Capability Assessment and Nonconforming Product Control.

`Systemic Problem Resolution` is intentionally held because duplication/relationship with existing problem-solving architecture must be resolved before catalog admission.

## Non-duplication rule

A GM source confirmation does not justify creating a duplicate Machine. If an existing CMOC Machine implements the same mechanism with materially the same input, transition, output and acceptance logic, GM becomes additional provenance for that Machine.

## Next step

Passportize the six clean candidates one by one, beginning with **Decision Gate**, while keeping all candidate status explicitly NON-CANON until comparison and multi-source confirmation justify promotion.

**REG-001:** unchanged.
**Canon:** unchanged.
**Existing Machine files:** unchanged.
