# GM-096 — Machine Candidate Passport: Controlled Change Implementation

**Source:** GM Quality Systems Basics rev. March 2009
**Provenance:** GM SOURCE → SOURCE-FINAL → Distinctions → Mechanisms → Machine Candidates → Catalog Cross-Check
**Status:** MACHINE-CANDIDATE / NON-CANON

## 1. Identity

**Candidate name:** Controlled Change Implementation

**Candidate type:** execution / state-transition machine candidate

**Primary source realization:** Managing Change / PPCR Process

## 2. Problem

An approved change must be translated into an actual controlled process transition. Authorization alone does not establish that the change occurred, and implementation without an explicit record leaves the organization unable to establish when and where the new state began.

## 3. Input

An approved and explicitly authorized change containing:

- defined change scope;
- responsible Change Leader;
- affected functions/participants;
- required approvals;
- written direction to proceed.

## 4. Trigger

Receipt of authorization to proceed with the change.

## 5. Operating sequence

`Authorized Change → Execute Change → Confirm Actual Implementation → Record Date / Breakpoint → Complete Required Worksheets → Submit for Final Approval`

## 6. Output

A changed process state together with evidence that the change was actually implemented and traceable to its implementation event.

## 7. State transition

`AUTHORIZED-TO-PROCEED → IMPLEMENTED / NEW PROCESS STATE`

The implementation machine performs the transition. It does not itself decide whether the change was authorized and does not by itself establish that the new state is acceptable.

## 8. Owner / responsibility

The source assigns implementation to the Change Leader together with designated parties involved in the change. The Change Leader records the actual implementation information and coordinates the required documentation.

## 9. Evidence

Source-derived evidence includes:

- PPCR form;
- actual implementation date;
- breakpoint where applicable;
- completed worksheets;
- PPCR log entry;
- subsequent final-approval record.

## 10. Acceptance condition

Implementation is operationally complete when the authorized change has actually been executed and the fact of implementation is recorded with the required traceability information.

This is **not** equivalent to final acceptance of the changed process.

## 11. Failure conditions

The candidate should treat the following as incomplete implementation control:

- implementation without prior authorization;
- inability to establish the actual implementation date;
- missing breakpoint where required;
- missing required implementation documentation;
- inability to trace the implementation to the approved PPCR.

The source supports the requirement for authorization and subsequent recording; it does not define every possible implementation failure mode, so no additional failure logic is inferred here.

## 12. Distinctions implemented

- Authorization ≠ Implementation
- Implementation ≠ Verification
- Implementation ≠ Final Approval
- Decision ≠ Execution
- Record of Implementation ≠ Evidence of Effectiveness

## 13. Relationship to other candidate Machines

### Decision Gate → Controlled Change Implementation

Decision Gate produces the authorization required by this machine. Controlled Change Implementation consumes that authorization.

### Controlled Change Implementation → Production Trial Run

Where PTR is required, the implemented change becomes the subject of a controlled trial/evaluation. PTR provides a verification/evaluation layer that this machine does not provide.

### Controlled Change Implementation → Final Acceptance / Closure Gate

Implementation produces the fact and record of transition; final acceptance is a subsequent control event.

### Controlled Change Implementation ↔ Bypass Process Control

A bypass may itself constitute a controlled process-state transition. Whether Bypass Process Control should be treated as a specialized implementation of this generic machine requires later CMOC comparison.

## 14. Boundary

This machine does **not**:

- decide whether a change is allowed;
- replace required approvals;
- independently verify effectiveness;
- perform final acceptance;
- redefine the change after authorization.

Its boundary is:

> **Execute an authorized change and establish an auditable record of the actual transition.**

## 15. Reusability hypothesis

The candidate may be reusable for controlled organizational transitions beyond GM process changes, wherever authorization must be followed by an explicit implementation event and traceable record.

This broader reuse remains a CMOC hypothesis and is not claimed as a fact of the source.

## 16. Canonization assessment

**Candidate strength:** STRONG

**Independent boundary:** YES

**Trigger/input:** YES

**Execution/output:** YES

**State transition:** YES

**Responsible role:** YES

**Repeatable sequence:** YES

**Evidence:** YES

**Acceptance/closure condition:** YES, with final acceptance deliberately separated

**Cross-source confirmation:** NOT YET ESTABLISHED

**Existing-machine duplication:** requires final comparison with generic State Transition / implementation patterns.

**Canon status:** NON-CANON.

## 17. Architectural observation

The strongest reason to retain this as a separate candidate is the clean separation between:

`permission to change` and `fact of change`.

The Decision Gate answers:

> **May the transition proceed?**

Controlled Change Implementation answers:

> **Did the authorized transition actually occur, and can we prove when it occurred?**

The next layer, Production Trial Run, answers a different question:

> **Does the changed process demonstrate acceptable performance?**

These three questions should not be collapsed into one Machine.

## 18. Status

**SOURCE-DERIVED / MACHINE-CANDIDATE / NON-CANON**

No REG-001 modification.
No Canon modification.
No existing Machine modified.

**Next candidate:** Production Trial Run.