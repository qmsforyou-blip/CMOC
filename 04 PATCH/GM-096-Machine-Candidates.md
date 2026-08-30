# GM-096 — Machine Candidates

**Source:** GM Quality Systems Basics rev. March 2009
**Basis:** SOURCE-FINAL-GM-QSB-2009.md → GM-096-Distinctions.md → GM-096-Mechanisms.md
**Status:** SOURCE-DERIVED / MACHINE-CANDIDATE / NON-CANON

## Purpose

This file screens the mechanisms extracted from GM QSB for possible CMOC Machine status.

A Machine candidate must have an independently recognizable operational boundary: trigger/input, transformation or decision, output/state transition, responsible role, repeatable operating sequence, evidence, and an acceptance/closure condition.

The candidate is not yet a canonical CMOC Machine.

---

## MC-01 — Decision Gate

**Candidate:** YES — strong.

**Mechanism:** controls whether a proposed change may move from review/approval to execution.

**GM implementation:** PPCR review → approval/rejection → required signatures → written PROCEED/STOP.

**Input:** proposed change requiring disposition.

**Output:** authorized-to-proceed state or STOP/rejected state.

**Owner:** Change Leader / designated management authority.

**Evidence:** PPCR approvals, signatures, written direction.

**Acceptance:** explicit proceed or stop decision.

**CMOC potential:** high. Likely reusable beyond Change Management.

---

## MC-02 — Controlled Change Implementation

**Candidate:** YES — strong.

**Mechanism:** executes an authorized process change and records the actual transition.

**Input:** authorized change.

**Output:** implemented change + recorded implementation event.

**Evidence:** PPCR implementation date, breakpoint, worksheets.

**Acceptance:** implementation completed and recorded, followed by final approval where required.

**CMOC potential:** high, but must be tested against a more general State Transition Machine before canonization.

---

## MC-03 — Production Trial Run

**Candidate:** YES — strong.

**Mechanism:** performs a bounded trial of a changed process before acceptance.

**Input:** authorized change for which PTR is required.

**Sequence:** readiness review → trial → internal value review → customer evaluation where applicable.

**Output:** evidence of trial performance and acceptance/rejection.

**Evidence:** PTR form, readiness/review results, evaluation.

**CMOC potential:** high. Strong independent boundary and reusable logic.

---

## MC-04 — Bypass Process Control

**Candidate:** YES — strong.

**Mechanism:** controls a temporary alternative to the normal approved process.

**Input:** need/authorization for bypass.

**Sequence:** entry breakpoint → alternative controlled process → inspection/audit/control → exit breakpoint → verified return.

**Output:** controlled bypass state or controlled return to normal state.

**Evidence:** Backup Worksheet, PFMEA/Control Plan/standardized work, inspection/audit records, return validation.

**CMOC potential:** high. Particularly valuable as a generic controlled-deviation pattern.

---

## MC-05 — Supplier Capability Assessment

**Candidate:** YES — strong.

**Mechanism:** determines and develops the capability of an external supplier to meet requirements.

**Input:** candidate/existing supplier + requirements.

**Sequence:** assessment → rating/gap → action/development → reassessment.

**Output:** supplier capability/status and development actions.

**Evidence:** assessment, score/rating, action plan, reassessment.

**CMOC potential:** high for extended-enterprise / external capability management.

---

## MC-06 — Supplier Performance Statusing

**Candidate:** MAYBE — mechanism candidate; Machine boundary not yet sufficiently independent.

Supplier Metrics, Six Panel Chart and Bidlist/R-Y-G representations may be components of a broader Supplier Capability Management Machine rather than separate Machines.

**Decision:** retain as mechanism, do not canonize as Machine yet.

---

## MC-07 — Systemic Problem Resolution

**Candidate:** YES — strong.

**Mechanism:** moves from observed problem to systemic cause and corrective/system action.

**Input:** problem/nonconformity.

**Sequence:** containment/problem definition → root cause → process cause → control-system cause → action → verification.

**Output:** systemic corrective action with evidence of effectiveness.

**Evidence:** root-cause analysis, action record, verification.

**CMOC potential:** high. Reusable across quality, operations and diagnostic work.

---

## MC-08 — Fast Response

**Candidate:** MAYBE — likely a composite control loop rather than a single Machine.

Fast Response includes detection, containment, communication, ownership, escalation and follow-up. It may decompose into Response/Containment and Decision/Action mechanisms.

**Decision:** retain as mechanism family until CMOC decomposition is completed.

---

## MC-09 — Contamination Control

**Candidate:** NO as a single Machine.

The source section contains multiple mechanisms: source prevention, measurement, limits/reaction, control-means verification, maintenance and environmental controls.

**Decision:** retain as mechanism family. Do not canonize the whole QSB section as one Machine.

---

## MC-10 — Requirement Operationalization

**Candidate:** NO as a single Machine at this stage.

It is a cross-cutting architecture present inside many Machines and mechanisms.

**Decision:** retain as foundational mechanism/pattern.

---

## MC-11 — Measurement-to-Action Control Loop

**Candidate:** MAYBE — potentially fundamental CMOC pattern.

It appears across contamination, supplier metrics, verification and other controls. Because it is highly reusable but also embedded in many mechanisms, it should first be tested as a generic CMOC control-loop pattern rather than immediately canonized as a Machine.

---

## MC-12 — Control Means Verification

**Candidate:** MAYBE.

The mechanism has a clear repeatable sequence: identify control means → verify functionality → maintain → verify effectiveness. However, it may be a reusable submechanism inside larger Machines rather than a standalone Machine.

---

## MC-13 — Process Verification

**Candidate:** NO as a single Machine.

It is an umbrella mechanism realized through Verification Station, PTR, audits and other verification practices.

---

## MC-14 — Final Acceptance / Closure Gate

**Candidate:** YES — but likely as a reusable subtype of Decision Gate rather than a separate top-level Machine.

**Decision:** do not create a separate canonical Machine until relationship to Decision Gate is resolved.

---

## MC-15 — Controlled Deviation

**Candidate:** YES as a generic Machine candidate, but likely closely related to Bypass Process Control.

**Decision:** preserve as a candidate pattern; resolve whether it is the parent mechanism and Bypass is an implementation.

---

## MC-16 — State Representation / Statusing

**Candidate:** NO as a Machine.

Status is a representation of state and should remain an ontological/control primitive or mechanism, not automatically a Machine.

---

## MC-17 — Workshop / Action-Plan Conversion

**Candidate:** YES — provisional.

**Input:** requirement/gap/current status.

**Sequence:** cross-functional assessment → proposal → management review → action plan → responsibility/tracking.

**Output:** managed action plan.

**Evidence:** presentation, forms/tracking, Action Plan.

**CMOC potential:** high for diagnostics and organizational development, but its boundary differs from shop-floor control Machines. Needs separate testing against CMOC diagnostic architecture.

---

## MC-18 — Layered / Repeated Verification

**Candidate:** MAYBE.

LPA has a clear repeated execution pattern and escalation to action, but may be a specialized implementation of the broader Process Verification mechanism.

**Decision:** candidate retained; relationship to Process Verification unresolved.

---

## MC-19 — Standardized Operations / Work

**Candidate:** NO as a single Machine.

Standardization is a control architecture used by many Machines. It may produce supporting mechanisms such as Standardized Work and Training, but the QSB strategy itself should not be canonized as one Machine.

---

## MC-20 — Error-Proofing Verification

**Candidate:** MAYBE — strong submachine candidate.

It verifies that error-proofing remains present and functional. Independent trigger, procedure and evidence exist, but it may be a specialized form of Control Means Verification.

**Decision:** retain for comparison before canonization.

---

## MC-21 — Nonconforming Product Control

**Candidate:** YES — strong candidate.

The QSB strategy provides an independent operational boundary around identification, segregation/control, disposition and follow-up of nonconforming product.

**CMOC potential:** high, but must be compared with existing CMOC control mechanisms before creating a duplicate Machine.

---

# Candidate ranking

## Tier A — strong Machine candidates

1. Decision Gate
2. Controlled Change Implementation
3. Production Trial Run
4. Bypass Process Control
5. Supplier Capability Assessment
6. Systemic Problem Resolution
7. Nonconforming Product Control

## Tier B — provisional candidates requiring decomposition/relationship analysis

8. Workshop / Action-Plan Conversion
9. Controlled Deviation
10. Layered / Repeated Verification
11. Error-Proofing Verification
12. Measurement-to-Action Control Loop
13. Control Means Verification
14. Fast Response

## Tier C — retain as mechanisms / primitives, not standalone Machines for now

15. Requirement Operationalization
16. Contamination Control as a whole
17. Process Verification as an umbrella
18. Final Acceptance / Closure Gate as separate Machine
19. Supplier Performance Statusing
20. State Representation / Statusing
21. Standardized Operations / Work

# Key architectural finding

The screening confirms that the most valuable Machine candidates are not necessarily the named QSB strategies. Several of the strongest candidates are **submechanisms that GM embeds inside larger strategies**.

Examples:

- Decision Gate is embedded in Managing Change.
- Production Trial Run is a specialized verification mechanism inside Managing Change.
- Bypass Process Control is embedded in Bypass Management.
- Supplier Capability Assessment is embedded in Supply Chain Management.
- Systemic Problem Resolution is embedded in Fast Response / Supply Chain problem resolution.

Therefore CMOC should not mirror the GM table of contents. It should extract reusable mechanisms and Machines from underneath the source's organizational packaging.

# Non-duplication rule

Before any candidate is promoted to canonical Machine, compare it against existing CMOC Machines. If an existing Machine already implements the same mechanism with the same state transition and acceptance logic, the GM source should be linked as additional provenance rather than creating a duplicate Machine.

# Status

**SOURCE-DERIVED / MACHINE-CANDIDATE / NON-CANON**

No REG-001 modification.
No Canon modification.
No existing Machine modified.

**Next step:** compare Tier A/B candidates with the existing CMOC Machine catalog and identify true new Machines versus existing Machines receiving additional GM provenance.