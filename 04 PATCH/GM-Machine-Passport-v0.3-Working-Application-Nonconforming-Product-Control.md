# GM-096 — Machine Passport v0.3 — Working Application: Nonconforming Product Control

**Notice:** 0169+180926  
**Status:** PASS / WORKING SPECIFICATION SUPPORTED / NON-CANON  
**Source:** GM Quality Systems Basics rev. March 2009, Control of Nonconforming Product, pp. 52–56; GM-096 candidate architecture.

---

## 1. Purpose

Apply the frozen **Machine Passport v0.3** to **Nonconforming Product Control**.

The test asks:

> Does control of nonconforming product have an independent bounded execution identity, distinct from Detection/Inspection, Banking, Fast Response and Systemic Problem Resolution?

No Catalog / Canon / REG-001 changes are made by this trial.

---

## 2. Source-derived execution

The working source architecture is:

`DETECTION → IDENTIFICATION → CONTAINMENT / SEGREGATION → AUTHORIZED DISPOSITION → RELEASE / REWORK / SCRAP → RECORD / FOLLOW-UP`

The immediate control objective is:

> prevent unintended use or release of nonconforming product and move the affected product through an authorized, traceable disposition path.

Important source-derived distinction:

> containment/disposition of the affected product is not the same as systemic elimination of the cause.

---

# 3. Passport v0.3 — CORE

## 3.1 Name

**Nonconforming Product Control**

## 3.2 Identity-bearing relation / mode

`NONCONFORMING / SUSPECT PRODUCT → CONTROLLED PRODUCT STATE → AUTHORIZED DISPOSITION`

More precisely:

> **CONTROL THE STATUS AND MOVEMENT OF AFFECTED PRODUCT SO THAT UNINTENDED USE/RELEASE IS PREVENTED UNTIL AUTHORIZED DISPOSITION.**

## 3.3 Local capability

Prevent unintended use or release of nonconforming/suspect product while preserving identification, status and traceability through disposition.

---

# 4. EXECUTION

## 4.1 Trigger

Detection or identification of actual or suspected nonconformance.

## 4.2 Inputs / context

- affected product, lot, component or process output;
- applicable requirement/specification;
- nonconformance information;
- identification/traceability information;
- applicable disposition authority/rules.

## 4.3 Preconditions

- nonconforming or suspect condition has been identified sufficiently to initiate control;
- affected material can be identified/segregated;
- applicable disposition authority/process is available.

## 4.4 Execution boundary

`DETECTION / IDENTIFICATION → CONTAINMENT / SEGREGATION → STATUS CONTROL → AUTHORIZED DISPOSITION → CONTROLLED RELEASE / REWORK / SCRAP → RECORD / HANDOFF`

The Machine begins when affected product enters the nonconformance-control path and ends when its controlled disposition is completed or transferred with status/traceability preserved.

## 4.5 Execution sequence

```
S0 READY / DETECTION
    ↓
S1 NONCONFORMANCE IDENTIFIED
    ↓
S2 PRODUCT IDENTIFIED / STATUS MARKED
    ↓
S3 CONTAINED / SEGREGATED
    ↓
S4 DISPOSITION AUTHORITY / DECISION
    ↓
S5 AUTHORIZED DISPOSITION EXECUTED
    ↓
S6 RELEASE / REWORK / SCRAP / CONTROLLED TRANSFER
    ↓
S7 RECORD / HANDOFF
    ↓
S8 CLOSE
```

## 4.6 Evidence

- product/lot identification;
- segregation or containment status;
- nonconformance record;
- disposition decision;
- traceability record;
- release/rework/scrap record where applicable.

## 4.7 Decision logic

Typical intrinsic decision points:

- nonconforming/suspect product identified?
- affected scope identified?
- containment adequate?
- disposition authorized?
- which authorized disposition applies?
- is release permitted after disposition?

The exact disposition rules are domain/site dependent and are not expanded beyond source-supported architecture.

## 4.8 Local outputs

- controlled product status;
- contained/segregated affected material;
- authorized disposition result;
- traceable record/handoff.

## 4.9 Closure condition

Machine closure occurs when the affected product has reached an authorized terminal disposition or a controlled downstream handoff with identification, status and traceability preserved.

**Important:** closure of product control does not imply closure of systemic problem resolution.

---

# 5. REALIZATION

## Domain

Production / service output control; nonconforming material/product.

## Internal mechanisms

- identification;
- status marking;
- segregation/containment;
- disposition authorization;
- controlled release/rework/scrap;
- traceability/recording.

These mechanisms are implementation components, not Machine identity.

## Roles

Responsible process and quality personnel according to applicable local procedure and disposition authority.

Exact role names remain implementation-dependent.

## Artifacts

Potential realization artifacts:

- nonconformance record;
- identification/status marker;
- segregation location;
- disposition record;
- traceability record.

Artifacts are evidence/supporting objects, not the Machine itself.

## Domain-specific conditions

- definition of nonconformance;
- applicable product/process requirements;
- authorized disposition rules;
- traceability requirements.

## Limitations

The Machine does not by itself:

- establish root cause;
- eliminate systemic cause;
- prove process capability;
- replace process verification;
- authorize arbitrary release.

## Downstream ownership

Systemic problem resolution, corrective action, process change and effectiveness verification remain downstream/adjacent mechanisms unless explicitly incorporated into a larger Assembly.

---

# 6. RELATIONS

## Pattern

Candidate relationship to **Response to Abnormality** and/or **Assessment/Control** remains HOLD.

No Pattern remapping is canonized by this trial.

## Invokes / uses

May invoke:

- detection/verification mechanisms;
- disposition decision mechanisms;
- problem-solving mechanisms where systemic action is required.

## Feeds

May feed:

- Systemic Problem Resolution;
- corrective action;
- process change;
- risk/PFMEA update;
- effectiveness verification.

---

# 7. VALIDATION

## 7.1 Machine boundary test

### Identity-bearing relation

**PASS**

The defining relation is not merely detection:

`AFFECTED PRODUCT → CONTROLLED STATUS → AUTHORIZED DISPOSITION`

### Own execution boundary

**PASS**

The execution has a bounded beginning (identified/suspect nonconformance) and bounded completion (authorized disposition or controlled handoff).

### Local capability

**PASS**

It independently prevents unintended use/release of affected product while controlling status and disposition.

### Closure condition

**PASS**

Closure is tied to controlled disposition/handoff, not to solving the underlying systemic cause.

### Overall

**PASS**

The candidate satisfies the working Machine criterion:

`identity-bearing relation + own execution boundary + local capability + closure condition`

---

# 8. Adversarial boundary tests

## A. Detection / Inspection

`OBSERVE → IDENTIFY NONCONFORMANCE`

**FAIL as the same Machine.**

Detection can initiate Nonconforming Product Control but does not itself contain, disposition or control subsequent release.

## B. Banking

`OUT-OF-NORMAL-FLOW MATERIAL → CONTROLLED BANKING STATE → DISPOSITION`

**DISTINCT / PASS.**

Banking controls material deliberately placed in a banking state; Nonconforming Product Control is triggered by nonconformance and specifically prevents unintended use/release through containment and authorized disposition.

There can be implementation overlap, and Banking may be used as one physical/control realization for affected material, but the identity-bearing purpose is different.

## C. Fast Response

`ABNORMALITY → SIGNAL / ESCALATION → RAPID RESPONSE`

**DISTINCT / PASS.**

Fast Response may initiate or coordinate rapid containment, but does not become identical to the product-status/disposition Machine.

## D. Systemic Problem Resolution

`PROBLEM → CAUSE → CORRECTIVE ACTION → VERIFY`

**DISTINCT / PASS.**

Nonconforming Product Control controls the affected product immediately. Systemic Problem Resolution addresses why the condition occurred and whether recurrence must be prevented.

## E. Audit / Expected-vs-Actual Verification

`EXPECTED / CRITERION → EVIDENCE → EVALUATION / GAP`

**DISTINCT / PASS.**

Verification may detect the nonconformance; product control acts on the affected product after detection.

---

# 9. Composition test

A realistic larger control architecture can be:

```
DETECT / VERIFY NONCONFORMANCE
          ↓
NONCONFORMING PRODUCT CONTROL
          ↓
AUTHORIZED DISPOSITION
          ↓
SYSTEMIC PROBLEM RESOLUTION
          ↓
CORRECTIVE ACTION
          ↓
EFFECTIVENESS VERIFICATION
```

This is a **composition**, not one Machine.

The distinction is especially important:

> **Containment/disposition is not cause elimination.**

Therefore the downstream problem-solving Machine does not need to be absorbed into Nonconforming Product Control.

---

# 10. Passport anti-duplication test

## Machine ≠ artifact

Nonconformance record, tag, hold label, segregation location and disposition form are artifacts/evidence carriers.

**PASS.**

## Machine ≠ SOP

The procedure may prescribe who, when and how to execute the control.

The Machine Passport captures invariant bounded execution, not the full SOP.

**PASS.**

## Machine ≠ Assembly

A broader nonconformance-management Assembly may contain:

`Detection → Product Control → Problem Solving → Corrective Action → Verification`

Nonconforming Product Control is one bounded component.

**PASS.**

---

# 11. Architectural result

The trial provides stronger evidence than the earlier source-only candidate passport.

**Nonconforming Product Control qualifies as an independent Machine candidate.**

Its identity is not:

> “dealing with defects”

and not:

> “inspection plus quarantine”.

Its identity is:

> **maintain controlled status and movement of nonconforming/suspect product until authorized disposition, preventing unintended use or release.**

This distinguishes it from:

- Detection/Inspection;
- Audit;
- Expected-vs-Actual Verification;
- Banking;
- Fast Response;
- Systemic Problem Resolution.

---

# 12. Status

- Passport v0.3 application: **PASS**
- Machine boundary proof: **PASS**
- Local capability: **PASS**
- Closure: **PASS**
- Banking distinction: **PASS**
- Detection/Inspection distinction: **PASS**
- Fast Response distinction: **PASS**
- Systemic Problem Resolution distinction: **PASS**
- Audit / Expected-vs-Actual distinction: **PASS**
- Machine vs Assembly: **PASS**
- Machine vs Artifact/SOP: **PASS**
- Pattern mapping: **HOLD**
- Catalog promotion: **NOT YET**
- Canon: **NON-CANON**
- REG-001: **NO CHANGE**

## 13. Step closure

The Machine Passport v0.3 trial is complete.

**Conclusion: Nonconforming Product Control = MACHINE CANDIDATE, structurally supported.**

No Catalog / Canon / REG-001 change is justified by this trial alone.

The next methodological step is not another Passport trial immediately. The useful next test is a focused **Boundary Comparison: Nonconforming Product Control ↔ Banking ↔ Bypass ↔ Fast Response**, because these four all operate around abnormal/out-of-normal material or process states and could otherwise become a source of Machine proliferation.

