# GM-096 — Machine Candidate Passport: Production Trial Run

**Source:** GM Quality Systems Basics rev. March 2009
**Provenance:** GM SOURCE → SOURCE-FINAL → Distinctions → Mechanisms → Machine Candidates → Catalog Cross-Check
**Status:** MACHINE-CANDIDATE / NON-CANON
**Candidate:** Production Trial Run (PTR)

## 1. Identity

**Candidate name:** Production Trial Run

**Candidate type:** verification / controlled-trial machine candidate

**Primary source realization:** Managing Change / Production Trial Run

## 2. Problem

A change may be authorized and physically implemented without yet demonstrating that the changed process can manufacture the product acceptably under normal production conditions. A bounded trial provides evidence before the changed process is treated as fully accepted.

## 3. Input

A controlled process change for which a Production Trial Run is required, together with:

- identified Change Leader;
- defined trial scope;
- readiness conditions;
- applicable internal/customer requirements;
- required trial documentation.

## 4. Trigger

A change is identified as requiring a Production Trial Run, and the organization reaches the point at which readiness for the trial must be established.

## 5. Operating sequence

`PTR Required → PTR Readiness → Conduct Trial → Internal PTR Value Review → Customer Plant PTR Evaluation where applicable → Acceptance / Further Action`

The source distinguishes internal PTR evaluation from Customer Plant PTR Evaluation where customer participation is required.

## 6. Output

Evidence about whether the changed process demonstrates acceptable manufacturability/performance in the production environment, together with the resulting evaluation and acceptance decision.

## 7. State transition

`AUTHORIZED / IMPLEMENTED CHANGE → TRIAL STATE → EVALUATED STATE → ACCEPTED / FURTHER ACTION`

PTR does not itself create authorization to change. It creates evidence for evaluating the changed state.

## 8. Owner / responsibility

The source assigns responsibility within the Managing Change structure to the Change Leader and designated participants. Customer evaluation, where applicable, introduces an external acceptance/evaluation role.

## 9. Evidence

Source-derived evidence includes:

- Production Trial Run Form;
- PTR requirement decision;
- readiness information;
- trial results;
- Internal PTR Value Review;
- Customer Plant PTR Evaluation where applicable;
- resulting approval/acceptance or further action.

## 10. Acceptance condition

The trial is complete when the required trial has been conducted and its result has been evaluated by the responsible internal and, where required, customer participants.

The source supports evaluation and acceptance; it does not justify assuming that every PTR automatically produces acceptance.

## 11. Failure / non-acceptance conditions

A trial result that does not demonstrate acceptable performance should prevent treating the changed process as accepted and should lead to further action according to the applicable change process.

The exact reaction path for every possible failed PTR is not fully specified in the extracted pages and is therefore not invented here.

## 12. Distinctions implemented

- Authorization ≠ Verification
- Implementation ≠ Verification
- Trial ≠ Full Validation
- Trial Result ≠ Acceptance
- Internal Evaluation ≠ Customer Evaluation
- Change Decision ≠ Evidence of Changed-State Performance

## 13. Boundary

PTR does **not**:

- decide whether the original change may be proposed;
- replace required change authorization;
- perform the whole change implementation;
- automatically constitute Product Validation;
- automatically constitute final acceptance without evaluation.

Its precise boundary is:

> **Provide controlled production evidence about the performance/manufacturability of a changed process before the changed state is treated as fully accepted.**

## 14. Relationship to other candidate Machines

### Decision Gate → Production Trial Run

Decision Gate controls whether the change/trial path may proceed. PTR then generates evidence about the resulting process state.

### Controlled Change Implementation → Production Trial Run

Implementation creates the changed state. PTR evaluates that state where a trial is required.

### Production Trial Run → Final Acceptance / Closure Gate

PTR provides evidence that can be used by a subsequent acceptance decision. PTR itself is not identical to final acceptance.

### Production Trial Run ↔ Process Verification

PTR is a specialized realization of the broader Process Verification mechanism. It should remain a Machine candidate because its trigger, scope, sequence and evidence boundary are independently recognizable.

## 15. Reusability hypothesis

The candidate may be reusable as a generic controlled-trial pattern wherever a consequential process change must be demonstrated in an operational environment before acceptance.

This broader reuse remains a CMOC hypothesis and requires confirmation from additional sources.

## 16. Canonization assessment

**Candidate strength:** STRONG

**Independent boundary:** YES

**Trigger/input:** YES

**Operating sequence:** YES

**Output/evidence:** YES

**State transition:** YES

**Responsible role:** YES

**Repeatability:** YES

**Acceptance/evaluation condition:** YES

**Cross-source confirmation:** NOT YET ESTABLISHED

**Existing-machine duplication:** no direct duplicate identified in the current cross-check; relationship to generic Process Verification remains to be resolved.

**Canon status:** NON-CANON.

## 17. Architectural observation

PTR completes a particularly clean three-machine chain extracted from Managing Change:

`Decision Gate → Controlled Change Implementation → Production Trial Run`

The three machines answer three different questions:

1. **Decision Gate:** May the transition proceed?
2. **Controlled Change Implementation:** Did the authorized transition actually occur?
3. **Production Trial Run:** Does the changed process demonstrate acceptable performance?

Collapsing these into one generic “change management” machine would destroy precisely the distinctions that make the control architecture effective.

## 18. Status

**SOURCE-DERIVED / MACHINE-CANDIDATE / NON-CANON**

No REG-001 modification.
No Canon modification.
No existing Machine modified.

**Next candidate:** Bypass Process Control.