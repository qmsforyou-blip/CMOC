# GM-096 — Machine Passport v0.3 — Working Application: Plant Process Change Control

**Notice:** 0171+180926  
**Status:** PASS WITH QUALIFICATION / WORKING SPECIFICATION / NON-CANON  
**Source:** GM Quality Systems Basics rev. March 2009, §11.2 Change Process, pp. 327–331; prior Managed Transition architecture.

---

## 1. Purpose

Apply the frozen **Machine Passport v0.3** to the GM-096 candidate **Plant Process Change Control (PPCR)**.

The key question is deliberately narrower than “is PPCR a process?”:

> Does PPCR have an independent bounded Machine identity, or is it primarily an authorization/governance mechanism inside the broader **Managed Transition** Assembly?

No Catalog / Canon / REG-001 changes are made by this trial.

---

## 2. Source-derived architecture

GM QSB states that suppliers shall have a procedure for Plant Process Changes covering planned and emergency changes.

The purpose of PPCR is to:

- maintain a record of changes that may impact final product;
- track system changes that may negatively affect the process even if final-product quality is not necessarily affected;
- ensure key stakeholders are aware of change requirements and have input to control out-of-standard conditions.

The source's PPCR form includes:

- background and change/problem statement;
- description of change / emergency reaction plan;
- aim and verification method;
- determination of required review/approval;
- identification of affected functional groups;
- pre-implementation review and signatures;
- implementation approval;
- post-implementation signature and breakpoint;
- final approval after open issues are resolved/closed.

The source also states that anyone can initiate a PPCR, a Change Leader is assigned, the change type and affected systems are determined, functional groups are identified, management signs off before implementation, the actual implementation and breakpoint are recorded, and final approval follows closure of open issues.

This supports a bounded **change-control execution**, but it also shows substantial governance/authorization content.

---

# 3. Boundary proof

## 3.1 Identity-bearing relation / mode

Working candidate:

`PROPOSED PLANT PROCESS CHANGE → CONTROLLED CHANGE CASE → IMPACT / STAKEHOLDER REVIEW → AUTHORIZATION → IMPLEMENTATION TRACKING → POST-IMPLEMENTATION / FINAL ACCEPTANCE`

More precisely:

> **CONTROL A PROPOSED PLANT PROCESS CHANGE FROM INITIATION THROUGH AUTHORIZED IMPLEMENTATION AND CONTROLLED CLOSURE.**

The identity is therefore not “change” itself and not merely a form.

It is the controlled relationship between:

1. proposed change;
2. assessment of affected systems/functions;
3. authorization;
4. controlled implementation;
5. breakpoint/post-implementation record;
6. final closure.

---

## 3.2 Own execution boundary

Working boundary:

> **Initiate PPCR → assign Change Leader → characterize change and affected systems → obtain required functional review/approval → authorize implementation → record actual implementation/breakpoint → resolve/close open issues → obtain final approval.**

The source explicitly supports this bounded progression.

However, an important boundary issue remains:

> authorization is not an ordinary internal action like identification or status marking; it is also a governance function.

Therefore the Machine boundary must not silently absorb the whole enterprise authorization architecture.

---

## 3.3 Local capability

> **Maintain controlled execution of a plant process change so that affected functions are identified, required approvals are obtained, implementation is traceable, and closure is formally established.**

This is narrower than the capability of the broader Managed Transition Assembly:

> manage a transition from one accepted state to another.

PPCR contributes the **change-control / authorization / traceability** portion of that transition.

---

## 3.4 Closure condition

Working closure:

> actual implementation and breakpoint are recorded; required open issues are resolved/closed; final approval is obtained from the responsible authority.

This is distinct from simply “change implemented”.

It also differs from PTR closure, where the local result is evaluation of a controlled production trial.

---

# 4. Machine Passport v0.3

## CORE

### name

**Plant Process Change Control**

### identity_bearing_relation_or_mode

`PROPOSED PLANT PROCESS CHANGE → CONTROLLED CHANGE CASE → REVIEW / AUTHORIZATION → IMPLEMENTATION TRACEABILITY → FINAL ACCEPTANCE`

### local_capability

Maintain controlled execution of a plant process change through impact/stakeholder review, authorization, implementation traceability and formal closure.

---

## EXECUTION

### trigger

A planned or emergency plant process change that falls within the PPCR scope.

GM QSB examples include changes affecting:

- final piece cost;
- machine/system reliability;
- machine/system capability;
- job instructions;
- training material;
- maintenance procedures;
- calibration procedures;
- operating instructions;
- machine setup targets;
- Process Control Plan;
- approved engineering changes.

### inputs_context

- proposed change;
- affected part/process/station;
- opportunity/problem statement;
- description of change or emergency reaction plan;
- affected systems/functions;
- applicable review/approval requirements;
- required verification method;
- change leader / responsible functions.

### preconditions

- proposed change is sufficiently identified to initiate a PPCR;
- responsible Change Leader can be assigned;
- affected functions can be identified;
- required review/approval route is available.

### execution_boundary

`INITIATE → CLASSIFY / ASSESS IMPACT → ASSIGN / COORDINATE RESPONSIBILITIES → REVIEW / APPROVE → AUTHORIZE IMPLEMENTATION → IMPLEMENT / RECORD BREAKPOINT → RESOLVE OPEN ISSUES → FINAL APPROVAL / CLOSE`

### execution_sequence

1. Initiate PPCR.
2. Obtain tracking number / establish change case.
3. Assign Change Leader.
4. Define type of change and impacted systems.
5. Determine affected functional groups.
6. Complete required reviews and approvals.
7. Authorize implementation.
8. Implement the change.
9. Record actual implementation date and breakpoint.
10. Resolve remaining open issues.
11. Obtain final approval and close.

### evidence

- PPCR number / controlled change record;
- completed PPCR sections;
- identified Change Leader;
- impact / functional-group review;
- approval signatures;
- implementation date;
- breakpoint;
- open-issue closure evidence;
- final approval.

### decision_points_logic

Typical intrinsic decisions:

- Does the proposed change require the change-management route?
- Which systems/functions are impacted?
- Is the required review/approval obtained?
- Is implementation authorized?
- Has the actual implementation/breakpoint been recorded?
- Are open issues resolved?
- Is final approval permitted?

The exact authorization hierarchy remains domain/site dependent.

### local_outputs

- controlled change case;
- identified impact/stakeholder scope;
- authorization status;
- traceable implementation/breakpoint;
- final approval / closed change record.

### closure_condition

**type:** decision + transition + record

**condition:**

`IMPLEMENTATION RECORDED + OPEN ISSUES CLOSED + FINAL APPROVAL OBTAINED`

**evidence:** controlled PPCR record, implementation/breakpoint evidence and final approval.

**downstream_continuation:** allowed.

---

# 5. REALIZATION

## domain

Manufacturing / plant process change control.

## internal_mechanisms

- PPCR form;
- change tracking;
- Change Leader assignment;
- impact/system assessment;
- functional-group review;
- management approval;
- implementation breakpoint;
- open-issue closure;
- final approval.

These are realization mechanisms, not independent Machine identities.

## roles

Source-supported roles include:

- Initiator;
- Change Leader;
- Manufacturing Engineering;
- affected functional groups;
- management / designated approvers.

Exact local role names remain implementation-dependent.

## artifacts

- PPCR form;
- tracking number;
- approval/signature records;
- implementation/breakpoint record;
- supporting review records.

Artifacts are evidence/supporting objects, not the Machine itself.

## domain_specific_conditions

- planned or emergency change;
- potential impact on final product or process/system;
- controlled document/change record;
- required pre-implementation approval;
- post-implementation breakpoint and final approval.

## limitations

PPCR does not itself:

- define the complete enterprise change philosophy;
- perform every technical validation needed for a change;
- replace Production Trial Run where a trial is required;
- execute Bypass Process Control;
- perform systemic problem solving;
- own every downstream process/document/risk-model update.

## downstream_ownership

Depending on change type, downstream ownership may include:

- Production Trial Run;
- Bypass Process Control;
- process/risk-model updates;
- document/work-instruction updates;
- training;
- verification/effectiveness mechanisms;
- normal approved process after transition.

---

# 6. RELATIONS

## pattern

**Managed Transition** — supported as a working structural relationship, not canonized by this trial.

Working composition:

`IDENTIFY / INITIATE CHANGE → PPCR → DECIDE / AUTHORIZE → PTR OR DIRECT IMPLEMENTATION → VERIFY / ACCEPT → CLOSE`

## invokes / uses

- impact assessment;
- technical review;
- approval mechanisms;
- Document Control;
- PTR where required;
- implementation verification.

## feeds

- controlled implementation;
- PTR;
- Bypass;
- updated process documentation;
- PFMEA / Control Plan / training changes where applicable;
- post-implementation verification.

---

# 7. VALIDATION

## 7.1 Identity-bearing relation / mode

**PASS WITH QUALIFICATION**

There is a bounded relation from proposed change through authorization, implementation traceability and closure.

Qualification:

> the authorization component is sufficiently central that PPCR can be viewed either as a specialized Machine or as a change-control mechanism inside Managed Transition, depending on the abstraction level.

## 7.2 Own execution boundary

**PASS WITH QUALIFICATION**

A coherent execution interval exists.

The qualification concerns overlap with the broader Managed Transition Assembly, not the absence of a bounded execution.

## 7.3 Local capability

**PASS**

PPCR independently provides controlled change-case handling, impact/stakeholder coordination, authorization traceability and formal closure.

## 7.4 Closure condition

**PASS**

The source explicitly provides post-implementation recording, breakpoint and final approval after open issues are resolved/closed.

## 7.5 Overall

**PASS WITH QUALIFICATION**

PPCR can be represented by Machine Passport v0.3.

Independent Machine identity is supported at the working level, but the boundary against Managed Transition remains an abstraction-level qualification.

---

# 8. Adversarial boundary tests

## A. Managed Transition

`IDENTIFY → ASSESS → DECIDE / AUTHORIZE → TRANSITION → VERIFY → ACCEPT / RETURN → RECORD / CLOSE`

PPCR realizes the **change-control / authorization / implementation-traceability** segment.

It does not necessarily own every possible transition mechanism.

**Result: DISTINCT BUT COMPOSABLE / QUALIFIED**

PPCR may be a Machine realization within Managed Transition, while Managed Transition remains the broader Assembly/pattern-level architecture.

---

## B. Production Trial Run

PTR:

`PLANNED / REQUIRED CHANGE → CONTROLLED TRIAL → RESULT → EVALUATION / DISPOSITION`

PPCR:

`PROPOSED CHANGE → REVIEW / AUTHORIZATION → IMPLEMENTATION CONTROL → CLOSURE`

A PPCR may invoke PTR.

**Result: DISTINCT / PASS**

---

## C. Bypass Process Control

Bypass controls a temporary alternative process route when the approved process cannot be followed.

PPCR controls the change case and its authorization/traceability.

**Result: DISTINCT / PASS**

---

## D. Banking

Banking controls material outside normal process flow.

PPCR controls a process change.

**Result: DISTINCT / PASS**

---

## E. Nonconforming Product Control

Nonconforming Product Control controls affected product status and disposition.

PPCR controls a change to a plant process.

A nonconformance may trigger a PPCR, but they are not identical.

**Result: DISTINCT / PASS**

---

## F. Decision Gate

A Decision Gate is a decision mechanism:

`INPUT / EVIDENCE → DECISION → AUTHORIZE / REJECT`

PPCR contains decision points and approval steps.

Therefore:

> **Decision Gate can be a mechanism inside PPCR without being identical to PPCR.**

**Result: DISTINCT / COMPOSABLE / PASS**

---

## G. Change Record / PPCR Form

The PPCR form is an artifact.

It carries evidence of the Machine execution.

**Result: NOT A MACHINE / PASS**

---

# 9. Composition test

A realistic composition is:

```
CHANGE / NEED
      ↓
PLANT PROCESS CHANGE CONTROL
      ↓
DECISION / AUTHORIZATION
      ↓
┌───────────────┬──────────────────┐
↓               ↓                  ↓
PTR             DIRECT CHANGE      BYPASS
↓               ↓                  ↓
EVALUATION   IMPLEMENTATION      CONTROLLED
                 ↓              ALTERNATIVE
                 └──────┬───────────┘
                        ↓
              POST-IMPLEMENTATION
                  VERIFICATION
                        ↓
                 FINAL ACCEPTANCE
```

This is a composition test, not a universal GM QSB sequence.

### Result: PASS

PPCR remains bounded without absorbing PTR, Bypass or verification into its identity.

---

# 10. Critical qualification — Machine vs Managed Transition

This is the main unresolved architectural point.

Two valid abstraction views remain:

### View A — PPCR as Machine

`PROPOSED CHANGE → CONTROLLED CHANGE CASE → AUTHORIZATION → IMPLEMENTATION → CLOSURE`

Here PPCR satisfies the working Machine criterion.

### View B — PPCR as specialized mechanism inside Managed Transition

`MANAGED TRANSITION`
→ identify / assess  
→ **PPCR change-control mechanism**  
→ decision/authorization  
→ transition  
→ verification  
→ acceptance/close

Here PPCR is not promoted to an independent top-level Machine.

### Current CMOC position

The Passport trial supports:

> **PPCR = bounded Machine candidate**

but does **not** yet justify:

> **PPCR = independent canonical Machine**

The distinction should remain open until cross-domain evidence or stronger Machine-independence testing establishes that PPCR's identity-bearing relation cannot be reduced to a specialized change-control mechanism inside Managed Transition.

This is a classification qualification, not a Passport-schema problem.

---

# 11. Machine proliferation test

The following are insufficient to create separate Machines:

- PPCR form;
- approval signature;
- change number;
- Change Leader role;
- impact checklist;
- implementation breakpoint;
- final approval.

They are mechanisms, roles or artifacts supporting the bounded execution.

The candidate becomes Machine-relevant because these elements are composed around the invariant relation:

`PROPOSED CHANGE → CONTROLLED AUTHORIZATION / IMPLEMENTATION → FORMAL CLOSURE`

---

# 12. Consequence for Passport v0.3

**No schema change.**

The frozen v0.3 schema represents PPCR without introducing new fields.

In particular, the test confirms the usefulness of separating:

- identity-bearing relation;
- execution boundary;
- local capability;
- closure;
- realization mechanisms;
- downstream ownership.

The authorization function does not require a new Passport field.

---

# 13. Consequence for Catalog / Canon / REG-001

- **Catalog:** NO CHANGE
- **Canon:** NO CHANGE
- **REG-001:** NO CHANGE
- **Passport v0.3:** NO CHANGE

The candidate remains indexed as GM-derived and non-canonical.

---

# 14. Architectural result

**Plant Process Change Control = MACHINE CANDIDATE WITH QUALIFICATION.**

The qualification is precise:

> PPCR has a bounded execution identity at the working level, but its independence from the broader **Managed Transition** architecture is not yet finally established.

This preserves both observations:

1. PPCR is more than a form or approval signature.
2. PPCR must not automatically become another top-level Machine merely because the GM source names a formal process.

---

# 15. Step closure

The Machine Passport v0.3 trial for **Plant Process Change Control** is complete.

**Result: PASS WITH QUALIFICATION.**

Nothing additional needs to be changed now.

The next useful methodological move is a **focused boundary comparison: PPCR ↔ Managed Transition ↔ Decision Gate ↔ Production Trial Run**, because PPCR is the first GM-096 candidate where the distinction between a bounded Machine and a governance mechanism inside a broader Assembly becomes especially important.
