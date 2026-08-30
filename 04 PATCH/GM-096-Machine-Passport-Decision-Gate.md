# GM-096 — Machine Candidate Passport: Decision Gate

**Source:** GM Quality Systems Basics rev. March 2009
**Provenance chain:** GM SOURCE → SOURCE-FINAL → Distinctions → Mechanisms → Machine Candidates → Catalog Cross-Check
**Status:** MACHINE-CANDIDATE / NON-CANON
**Candidate:** Decision Gate

## 1. Identity

**Candidate name:** Decision Gate

**Candidate type:** control / decision machine candidate

**Primary source realization:** Managing Change / PPCR Process

**CMOC role:** controls admissibility of transition from one process state to another.

## 2. Problem

A proposed change or other controlled transition must not move directly from proposal to execution merely because someone wants it executed. The organization needs an explicit mechanism that determines whether the transition is permitted and stops it when required approval or authorization is absent.

## 3. Input

A proposed change or controlled transition with:

- defined object/scope;
- responsible Change Leader or equivalent owner;
- required review route;
- identified approval participants;
- supporting information/evidence.

## 4. Trigger

A transition requires authorization to move from review/pending state toward implementation or another consequential state.

## 5. Operating sequence

`Proposal → Review → Classification/Route → Required Approvals → Decision → STOP / PROCEED`

For the GM realization, departmental approvals are followed by management review and written direction to proceed. If the required decision is rejection or STOP, the change process stops and concerned parties are notified.

## 6. Output

One of two controlled outcomes:

### PROCEED
The transition becomes authorized for implementation.

### STOP / REJECT
The transition is blocked and the relevant parties are notified.

## 7. State transition

`PENDING / PROPOSED → AUTHORIZED-TO-PROCEED`

or

`PENDING / PROPOSED → STOP / REJECTED`

The Machine therefore governs **permission to transition**, not the transition itself.

## 8. Owner / responsibility

The source realization assigns process responsibility to the Change Leader and designated management authority. The Change Leader coordinates the review and obtains the required approvals; management provides the final written direction to proceed or stop.

## 9. Evidence

Possible source-derived evidence includes:

- PPCR form;
- tracking number;
- review record;
- required departmental signatures;
- written PROCEED / STOP direction;
- notification of rejection where applicable.

## 10. Acceptance condition

The gate is complete when an explicit disposition exists:

`PROCEED` or `STOP / REJECT`.

No ambiguous intermediate condition is treated as authorization to execute.

## 11. Failure / STOP conditions

The transition is stopped when, for example:

- required review rejects the change;
- a required departmental approval is not obtained;
- management does not authorize proceeding;
- the required written direction to proceed is absent.

## 12. Distinctions implemented

- Approval ≠ Authorization
- Authorization ≠ Implementation
- Change ≠ New Accepted State
- Review ≠ Decision
- Decision ≠ Execution

## 13. Relationship to other candidate Machines

### Decision Gate → Controlled Change Implementation

Decision Gate produces authorization. Controlled Change Implementation consumes that authorization and performs the change.

### Decision Gate → Production Trial Run

Where a trial is required, Decision Gate may authorize the change/trial path; PTR then supplies verification/evaluation evidence.

### Decision Gate → Final Acceptance / Closure

Final acceptance may use the same gate pattern, but should not automatically be treated as a separate Machine. It may be a specialized Decision Gate instance.

## 14. Boundary

Decision Gate does **not**:

- perform the physical/process change;
- verify the changed process by itself;
- constitute final acceptance by itself;
- replace the evidence required for the decision.

Its function is narrower and precise:

> **Determine whether a controlled transition may proceed, and block it when the required conditions are not satisfied.**

## 15. Reusability hypothesis

The candidate is likely reusable outside Managing Change wherever CMOC requires a controlled transition with explicit admissibility criteria and a STOP/PROCEED decision.

Potential applications require independent CMOC validation before canonization.

## 16. Canonization assessment

**Candidate strength:** STRONG

**Independent boundary:** YES

**Trigger/input:** YES

**Decision/output:** YES

**State transition:** YES

**Responsible role:** YES

**Repeatable sequence:** YES

**Evidence:** YES

**Acceptance condition:** YES

**Cross-source confirmation:** NOT YET ESTABLISHED

**Existing-machine duplication:** no direct duplicate identified in current cross-check; relationship to generic approval/audit patterns remains to be tested.

**Canon status:** NON-CANON.

## 17. Decision

Retain as a **STRONG MACHINE CANDIDATE**.

Do not canonize yet. First test the candidate against:

1. existing CMOC decision/approval patterns;
2. possible generic State Transition Machine architecture;
3. other sources that may independently realize the same mechanism.

**No REG-001 modification.**
**No Canon modification.**
