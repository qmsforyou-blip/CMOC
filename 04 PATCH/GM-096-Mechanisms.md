# GM-096 — Mechanisms extracted for CMOC

**Source:** GM Quality Systems Basics rev. March 2009
**Basis:** SOURCE-FINAL-GM-QSB-2009.md + GM-096-Distinctions.md + page-by-page extraction
**Status:** SOURCE-DERIVED / CANDIDATE / NON-CANON

## Purpose

This file maps source-derived distinctions to operational mechanisms. It does not yet canonize mechanisms and does not declare Machines. A mechanism is retained here when the source demonstrates a repeatable way of making a distinction operational through roles, states, controls, decisions, evidence and/or actions.

## 1. Requirement Operationalization

**Realizes:** D-01 Requirement ≠ Document.

**Function:** Translate an abstract SHALL/requirement into an operational arrangement consisting of procedure/work instruction, responsible role, form or record, tracking, review and communication.

**Source pattern:** SHALL → procedure/work instruction → form/tracking → review → communication → action.

**CMOC interpretation:** A requirement becomes governable when an operational mechanism gives it a place in work, evidence and review.

**Machine candidate:** possible, but not yet declared.

## 2. Measurement-to-Action Control Loop

**Realizes:** D-15 Measurement ≠ Control; D-03 Detection ≠ Control.

**Function:** Connect measurement or detection with criteria, status interpretation, reaction and corrective action.

**Source pattern:** measurement → record/plot → limit/status → reaction plan → corrective action → management/process update.

**Examples:** contamination monitoring, supplier metrics, cleanliness measurement, SPC/U-Charts and reaction plans.

**CMOC interpretation:** Measurement becomes control only when it changes the permitted response or state through an explicit decision/action path.

## 3. Control Means Verification

**Realizes:** D-18 Control Means ≠ Controlled State.

**Function:** Verify that the means intended to maintain a controlled state is itself functioning and maintained.

**Source pattern:** control equipment/process → functionality check → preventive maintenance → evidence of effectiveness.

**Examples:** parts washers, deburring systems, fluid systems, probes/flush stations and other contamination-control means.

**CMOC interpretation:** A control measure cannot be treated as effective merely because it exists; its capability to perform its control function must itself be verified.

## 4. Process Verification

**Realizes:** D-04 Result ≠ Process; D-07 Implementation ≠ Verification.

**Function:** Establish evidence that the process, not merely the final output or the implementation action, is operating acceptably.

**Source pattern:** process requirement → verification activity → evidence → acceptance/reaction.

**Examples:** Verification Station, Production Trial Run, process audits and product/process-specific audits.

## 5. Capability Assessment & Development

**Realizes:** D-02 Compliance ≠ Capability; D-13 Supplier ≠ Purchase Source.

**Function:** Assess the ability of an organization/supplier to meet requirements and develop that ability where gaps exist.

**Source pattern:** assess → classify/status → identify gap → develop → re-assess.

**Examples:** Potential Supplier Assessment, QSB audit, special-process assessment, supplier metrics and supplier development.

## 6. Supplier Performance Monitoring

**Realizes:** D-02 Compliance ≠ Capability; D-17 State ≠ Status Record.

**Function:** Convert supplier performance into an observable, reviewable status using defined metrics and ratings.

**Source pattern:** operational performance → metric → status/rating → management review → supplier action/development.

**Examples:** Supplier Metrics, Six Panel Chart, Bidlist/Supplier Ranking, PPM, CAR, audit score and certification status.

## 7. Systemic Problem Resolution

**Realizes:** D-03 Detection ≠ Control; D-11 Problem ≠ Corrective Action.

**Function:** Move from an observed problem through technical/process causes to failure of planning or control-system causes and then to corrective/system action.

**Source pattern:** problem → root cause → why planning failed → why process allowed defect → why control failed → action/system update.

**Example:** Drill Deep & Wide / 3×5 Why.

## 8. Decision Gate

**Realizes:** D-05 Approval ≠ Authorization; D-14 Change ≠ New Accepted State.

**Function:** Control whether an object/process change may pass from one state to the next.

**Source pattern:** review → approval/rejection → STOP or proceed; and, separately, written authorization to proceed.

**Key property:** rejection is an active state transition to STOP, not merely a negative comment.

## 9. Controlled Implementation

**Realizes:** D-06 Authorization ≠ Implementation; D-17 State ≠ Status Record.

**Function:** Execute an authorized change and create an explicit record of the actual implementation event, including implementation date and breakpoint where applicable.

**Source pattern:** authorization → implementation → actual-date/breakpoint record.

## 10. Trial / Evaluation Mechanism

**Realizes:** D-07 Implementation ≠ Verification; D-16 Record ≠ Evidence of Effectiveness.

**Function:** Establish an intermediate controlled trial and evaluate its result before treating a change as accepted.

**Source pattern:** change → PTR requirement → readiness → trial → internal/customer evaluation → acceptance.

**Example:** Production Trial Run (PTR).

## 11. Final Acceptance / Closure Gate

**Realizes:** D-08 Implementation ≠ Final Approval; D-16 Record ≠ Evidence of Effectiveness.

**Function:** Keep implementation, completion of required records and final acceptance as distinct events.

**Source pattern:** implementation → required documentation/worksheets → final review → final approval.

## 12. Controlled Deviation

**Realizes:** D-09 Temporary Deviation ≠ Uncontrolled Exception.

**Function:** Represent a temporary departure from the normal process as a bounded and governed state with explicit controls and evidence.

**Source pattern:** normal state → authorized deviation → defined controls → monitoring → return.

## 13. Bypass Process Control

**Realizes:** D-10 Bypass ≠ Abandonment of Control.

**Function:** Preserve control requirements when the normal approved process is bypassed by defining an alternative controlled process and controlled return.

**Source pattern:** normal process → entry breakpoint → bypass process + PFMEA/Control Plan/standardized work/inspection/audit → exit breakpoint → verified return.

**Source artifacts:** Backup Worksheet, bypass list, action plan, LPA and return validation.

## 14. State Representation / Statusing

**Realizes:** D-17 State ≠ Status Record.

**Function:** Represent an operational state through a record, status, metric or rating while maintaining traceability to the underlying state.

**Examples:** R/Y/G supplier status, implementation date, breakpoint, audit status and supplier metrics.

**CMOC interpretation:** status is a representation of state, not the state itself.

## 15. Workshop / Action-Plan Conversion

**Realizes:** D-12 Workshop ≠ Training; D-01 Requirement ≠ Document.

**Function:** Convert requirements and identified gaps into proposals, responsibilities, tracking mechanisms and action plans through cross-functional work.

**Source pattern:** SHALL → current status → gap → proposal → form/tracking → management review → Action Plan → implementation.

**CMOC interpretation:** the Workshop is an action-producing mechanism, not merely a knowledge-transfer event.

## 16. Layered / Repeated Verification

**Realizes:** D-03 Detection ≠ Control; D-04 Result ≠ Process.

**Function:** Repeatedly verify process adherence and effectiveness at defined organizational levels, with findings connected to response and action.

**Example:** Layered Process Audit (LPA).

**Note:** retained as a mechanism candidate; its final relationship to Process Verification and other audit mechanisms requires CMOC comparison before Canonization.

## 17. Standardization as Control Mechanism

**Realizes:** D-04 Result ≠ Process.

**Function:** Make the intended process state explicit and reproducible through Standardized Operations, Standardized Work and Standardized Operator Training.

**Source pattern:** defined standard → trained performer → observed execution → verification → reaction to deviation.

**Note:** this may ultimately resolve into several CMOC mechanisms rather than one.

## 18. Error-Proofing Verification

**Realizes:** D-03 Detection ≠ Control; D-04 Result ≠ Process.

**Function:** Verify that error-proofing devices/controls remain present and functional rather than assuming that installed poka-yoke remains effective.

**Source strategy:** Error Proofing Verification.

## 19. Fast Response

**Realizes:** D-03 Detection ≠ Control; D-11 Problem ≠ Corrective Action.

**Function:** Convert a newly identified abnormal condition into rapid containment, communication, ownership and structured follow-up.

**Source strategy:** Fast Response.

## 20. Nonconforming Product Control

**Realizes:** D-03 Detection ≠ Control; D-16 Record ≠ Evidence of Effectiveness.

**Function:** Prevent unintended use/release of nonconforming product and connect identification, segregation, disposition and follow-up.

**Source strategy:** Control of Non-Conforming Product.

## 21. Mechanism Relationship Map

The source-derived mechanisms form several recurring control families:

### A. Requirement-to-action

`Requirement Operationalization → Assessment → Status/Gap → Action Plan → Management Review`

### B. State control

`State Definition → Measurement/Verification → Status → Decision → Response`

### C. Change control

`Change Object → Decision Gate → Authorization → Controlled Implementation → Trial/Evaluation → Final Acceptance`

### D. Deviation control

`Normal State → Controlled Deviation/Bypass → Verification → Return to Normal State`

### E. Problem control

`Detection → Containment/Fast Response → Root Cause → Systemic Cause → Corrective/System Action → Verification`

### F. External capability control

`Supplier Assessment → Requirement Cascade → Performance Monitoring → Problem Resolution → Supplier Development → Reassessment`

## 22. Machine-candidate screening rule

A mechanism is not automatically a Machine.

Before a Machine is declared, the mechanism must demonstrate a sufficiently independent operational boundary:

- defined trigger/input;
- defined output;
- explicit state transition or decision;
- responsible role;
- repeatable procedure;
- evidence/record;
- measurable completion/acceptance condition;
- identifiable reuse outside the single source example.

Where a mechanism is only a component of a larger control loop, it remains a mechanism until CMOC architecture demonstrates otherwise.

## 23. Status

All mechanisms in this file are **SOURCE-DERIVED / CANDIDATE / NON-CANON**.

No new REG-001 entries are created here.

No Machine is canonized here.

**Next step:** screen these mechanisms against existing CMOC Machine criteria and existing Machine catalog; produce `GM-096-Machine-Candidates.md`.