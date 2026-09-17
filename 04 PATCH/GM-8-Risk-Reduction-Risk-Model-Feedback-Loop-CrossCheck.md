# GM QSB — Risk Reduction — Risk Model Feedback Loop Cross-Check

**Notice:** 0143+170926

## 1. Purpose

Проверить, является ли конструкция **Risk Model Feedback Loop** более общим CMOC Pattern, чем PFMEA / RPN / Reverse PFMEA.

Рабочая гипотеза из GM-8:

`MODEL → FIELD EVIDENCE → GAP / NEW FAILURE MODE → ACTION → VERIFY → REASSESS → MODEL UPDATE`

Это не канонизация, а independent cross-check.

---

## 2. What is actually supported by independent sources

### Source A — GM / Reverse PFMEA lineage

GM-8 связывает PFMEA с фактическим состоянием станции: проверяются существующие failure modes, наличие и эффективность prevention/detection controls, затем выполняется поиск новых failure modes; результаты используются для action plan и последующего PFMEA/RPN reassessment.

**Source-supported loop:**

`PFMEA MODEL → STATION → CONTROL CHECK → GAP / NEW FM → ACTION → REASSESS → PFMEA UPDATE`

### Source B — GM-related later material

GM material reproduced in supplier-quality guidance explicitly connects Reverse PFMEA findings with updates to Process Flow, PFMEA, Control Plan and Work Instructions. Risk review therefore does not terminate at observation; evidence is returned into the management model and associated controlled documents.

### Source C — Nexteer supplier requirements

Nexteer describes two linked feedback directions: root cause and corrective action from problem cases are fed back to PFMEA; high-risk PFMEA items are reviewed and action plans created; reverse PFMEA audits process risk and creates action plans; the purpose of preventive action includes verifying known risk is controlled, identifying sources of potential risk and taking action to lessen negative effects.

This independently supports the general relation:

`FIELD / PROBLEM DATA → RISK MODEL → ACTION → RISK CONTROL`

and, in the reverse direction:

`RISK MODEL → FIELD VERIFICATION → NEW / RESIDUAL RISK → ACTION`

### Source D — automotive Reverse PFMEA guidance

Independent Reverse PFMEA guidance describes the method as a documented continuous-improvement tool used proactively or reactively to find gaps or weaknesses in prevention/detection controls, identify additional failure modes, develop more realistic risk ratings, and feed improvements back into PFMEA and related documents.

The important architectural point is the **feedback**, not the particular scoring system.

---

## 3. Cross-domain test

The candidate Pattern should not depend on the nouns PFMEA, RPN, Failure Mode or manufacturing station.

The generic structure can be expressed as:

`MODEL → REALITY → EVIDENCE → GAP / NEW INFORMATION → ACTION → VERIFY → MODEL UPDATE`

Examples that fit the same grammar:

- risk model ↔ actual process;
- planned control ↔ observed control effectiveness;
- documented process ↔ actual process;
- expected failure modes ↔ newly discovered failure modes;
- corrective action ↔ updated risk/control model.

The evidence found supports these relations, but does **not yet prove** that the same grammar is universal across unrelated management domains.

Therefore the Pattern should not be promoted beyond candidate status on this cross-check alone.

---

## 4. Boundary with existing CMOC constructions

### Not simply Verification

Verification answers whether an object/control satisfies a criterion.

Risk Model Feedback Loop additionally requires that the **result of verification changes or challenges the model**.

### Not simply Problem Solving

Problem Solving can produce corrective action from a detected problem.

The candidate Pattern is broader: the trigger may be routine verification or proactive examination even when no actual defect has occurred.

### Not simply Continuous Improvement

Continuous Improvement is broader and may contain many different feedback structures.

The candidate Pattern is narrower: it specifically describes reconciliation between a representation/model and evidence from the realized system.

### Not simply Record / Traceability

A record preserves evidence. The Pattern requires evidence to feed back into the controlled model and/or its control architecture.

### Not simply Audit

Audit supplies structured evidence against criteria. The Pattern begins when such evidence is used to challenge, update or recalibrate the model.

---

## 5. Candidate identity

### Working name

**Risk Model Feedback Loop**

This is a CMOC working name, not an assertion that the phrase is an established industry-standard term.

### Working formula

`MODEL → REALITY → EVIDENCE → GAP / NEW INFORMATION → ACTION → VERIFY → MODEL UPDATE`

### Core capability

**Maintain alignment between a management model and the realized state of the system through evidence-driven feedback.**

### Preconditions

- существует explicit model / representation of the controlled object;
- существует observable realization of that object;
- evidence can be collected from the realization;
- discrepancy, new information or residual risk can be identified;
- there is a mechanism for changing the model/control architecture.

### Output

One or more of:

- confirmed model;
- corrected model;
- new risk/failure mode;
- changed control;
- revised assessment;
- recorded rationale/evidence.

---

## 6. Status decision

**PATTERN CANDIDATE / STRONG CANDIDATE — MULTI-SOURCE CONFIRMED / NON-CANON**

Why not CANON:

1. The independent evidence strongly confirms the feedback architecture within quality/risk-management contexts.
2. The architecture is clearly broader than Reverse PFMEA itself.
3. However, this cross-check has not yet established a sufficient number of genuinely different domains to prove that the abstraction is not merely an automotive quality-management pattern.

Therefore the correct next status is **STRONG PATTERN CANDIDATE**, not Canon.

---

## 7. Architectural result

The relationship between the constructs can now be represented as:

```text
                    ┌──────────────────────┐
                    │      RISK MODEL      │
                    │ PFMEA / assumptions  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      REAL SYSTEM     │
                    │ station / process    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       EVIDENCE       │
                    │ observation / test   │
                    └──────────┬───────────┘
                               │
                    ┌──────────▼───────────┐
                    │ GAP / NEW INFORMATION│
                    │ residual / new risk  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │        ACTION        │
                    │ control / prevention │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ VERIFY / REASSESS    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    MODEL UPDATE      │
                    └──────────┬───────────┘
                               │
                               └──────→ next cycle
```

**Reverse PFMEA** is therefore best treated as a specialized Machine implementing this feedback pattern, rather than as the Pattern itself.

---

## 8. Important new distinction

The most reusable object may not be **risk reduction** itself.

The deeper construction is:

> **A model is not trusted merely because it exists; it is repeatedly confronted with evidence from the realized system, and the model/control architecture is changed when reality contradicts or enriches it.**

This is a CMOC architectural hypothesis, not a source quotation.

---

## 9. No catalog / canon changes

Do not yet:

- add Risk Model Feedback Loop to Machine Pattern catalog;
- modify Canon;
- modify REG-001;
- create a fundamental Machine from it.

The existing Managed Transition pattern remains unaffected.

---

## 10. Next step

The next verification should be a **blind cross-domain test** on at least two domains where there is no PFMEA vocabulary — for example:

1. software / IT architecture or operations;
2. organizational / regulatory management;
3. engineering design verification.

The question is simple:

> Does the same MODEL → REALITY → EVIDENCE → GAP → ACTION → VERIFY → MODEL UPDATE structure appear without importing PFMEA terminology?

If yes, the Pattern becomes materially stronger. If not, we should narrow it back toward **Risk Model Feedback** as a domain-specific family rather than a general CMOC Pattern.

---

## Evidence used for independent cross-check

- GM-derived Reverse PFMEA material: on-station verification of controls, discovery of new failure modes, action plans and PFMEA/RPN reassessment.
- Nexteer supplier requirements: feedback of root cause/corrective action to PFMEA; high-risk review and action planning; reverse PFMEA to verify known risk, identify potential risk and lessen its impact. External evidence: Nexteer NSRs, section 6.1.2.1–6.1.2.2.
- Automotive Control Plan / Reverse PFMEA guidance: Reverse PFMEA as proactive/reactive continuous improvement; gaps in controls, new failure modes, more realistic risk ratings, and updates to PFMEA and related documents.

All external evidence is used as cross-check evidence; no source is treated as proof of the CMOC nomenclature itself.
