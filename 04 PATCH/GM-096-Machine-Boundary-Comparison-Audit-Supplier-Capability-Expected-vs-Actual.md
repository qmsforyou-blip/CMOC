# GM-096 — Machine Boundary Comparison — Audit / Supplier Capability Assessment / Expected-vs-Actual Control Verification

**Notice:** 0168+180926  
**Status:** PASS WITH QUALIFICATION / WORKING SPECIFICATION / NON-CANON  
**Purpose:** проверить, является ли Supplier Capability Assessment самостоятельной Machine либо domain-specific realization существующей Assessment/Audit Machine, и отделить обе от Expected-vs-Actual Control Verification.

---

## 1. Starting point

После применения Machine Passport v0.3 к Supplier Capability Assessment возникла важная граница:

> GM QSB называет конкретную реализацию **Potential Supplier Assessment Audit (PSA)**.

Поэтому одного наличия bounded execution недостаточно, чтобы объявлять Supplier Capability Assessment новой универсальной Machine.

Тест сравнивает три структуры:

### A. Audit

`OBJECT / SCOPE → CRITERION → EVIDENCE → EVALUATION → FINDING / STATUS → RECORD / HANDOFF`

Identity-bearing relation:

> **EVALUATE AN OBJECT / SCOPE AGAINST AN ACCEPTED CRITERION**

Local capability:

> получить проверяемое суждение о соответствии объекта принятому критерию и сформировать finding/status.

### B. Supplier Capability Assessment

`SUPPLIER → REQUIREMENTS / CAPABILITY CRITERIA → EVIDENCE → CAPABILITY / GAP / RISK CHARACTERIZATION → SOURCING INPUT`

Identity-bearing relation under test:

> **CHARACTERIZE SUPPLIER CAPABILITY AND SOURCING RISK FROM STRUCTURED ASSESSMENT EVIDENCE**

Local capability:

> характеризовать способность поставщика выполнять заданные требования и дать evidence-based input для supplier selection/evaluation.

### C. Expected-vs-Actual Control Verification

`EXPECTED STATE → ACTUAL STATE → EVIDENCE → COMPARE → GAP / NEW INFORMATION → FINDING → ACTION HANDOFF → VERIFY`

Identity-bearing relation:

> **COMPARE REALIZED STATE WITH ACCEPTED EXPECTED STATE**

Local capability:

> выявить discrepancy между expected и actual control state и обеспечить проверяемый finding с последующей verification boundary.

---

## 2. Test A — Same assessment grammar

Supplier Capability Assessment и Audit имеют общую основу:

`SCOPE → CRITERIA → EVIDENCE → EVALUATION → FINDING`

PSA может быть реализован как audit, использующий supplier-specific criteria.

### Result: PASS WITH QUALIFICATION

Общая execution grammar очень велика.

Следовательно:

> наличие supplier-specific предмета само по себе не создаёт новую Machine.

---

## 3. Test B — What is invariant?

### Audit

Invariant:

`OBJECT / SCOPE ↔ ACCEPTED CRITERION`

Результат:

`EVALUATION / FINDING / STATUS`

### Supplier Capability Assessment

В PSA supplier-specific criteria оценивают способность поставщика; результат используется для характеристики capability/gaps/risk и supplier-selection input.

Но:

> **capability/risk characterization может быть semantic specialization of the Audit output, а не отдельной execution relation.**

Это ключевая оговорка.

### Expected-vs-Actual Verification

Здесь invariant другой:

`EXPECTED STATE ↔ REALIZED STATE`

Причём comparison itself является identity-bearing relation.

### Result: PASS

Expected-vs-Actual Control Verification остаётся structurally distinct.

Audit и Supplier Capability Assessment пока не доказали независимые identity-bearing relations.

---

## 4. Test C — Replacement test

### Replace supplier with another assessed object

`SUPPLIER → REQUIREMENTS → EVIDENCE → EVALUATION → FINDING`

Структура продолжает работать как Audit.

**Result: PASS**

Это показывает, что supplier object не является достаточным основанием для отдельной Machine.

### Replace supplier-specific capability criteria with generic criteria

`OBJECT → CRITERION → EVIDENCE → EVALUATION → FINDING`

Структура становится обычным Audit.

**Result: PASS**

### Replace supplier assessment with equipment-control assessment

`EQUIPMENT → CONTROL CRITERION → EVIDENCE → EVALUATION → FINDING`

Получается Audit / Control Verification family, а не Supplier Capability Assessment.

**Result: PASS**

### Replace evaluation with explicit expected-vs-actual comparison and re-verification

`EXPECTED → ACTUAL → EVIDENCE → COMPARE → GAP → ACTION → VERIFY`

Получается Expected-vs-Actual Control Verification.

**Result: PASS**

---

## 5. Test D — Output semantics versus execution identity

Это главный тест.

Supplier Capability Assessment имеет дополнительные outputs:

- capability characterization;
- gaps;
- sourcing risk;
- sourcing decision input.

Но дополнительные outputs сами по себе не доказывают отдельную Machine.

Возможны две архитектуры:

### Architecture 1 — Audit realization

`AUDIT / ASSESSMENT MACHINE
        ↓
SUPPLIER-SPECIFIC CRITERIA
        ↓
PSA
        ↓
CAPABILITY / GAP / RISK CHARACTERIZATION
`

Здесь Supplier Capability Assessment — domain-specific realization / specialization Audit.

### Architecture 2 — Independent Machine

`SUPPLIER CAPABILITY
        ↓
SPECIALIZED EVIDENCE
        ↓
CAPABILITY / RISK CHARACTERIZATION
        ↓
SOURCING INPUT
`

Для Architecture 2 необходимо доказать, что characterization of capability/risk является не просто output semantics Audit, а самостоятельной invariant execution relation.

### Result: NOT YET PROVEN

Текущих GM QSB evidence достаточно для bounded PSA, но недостаточно для уверенного отделения универсальной Supplier Capability Assessment Machine от Audit.

---

## 6. Test E — Boundary with Expected-vs-Actual Verification

| Property | Audit | Supplier Capability Assessment / PSA | Expected-vs-Actual Verification |
|---|---|---|---|
| Primary object | object/scope | supplier | realized control/process state |
| Criterion | accepted criterion | supplier requirements/capability criteria | accepted expected state |
| Evidence | required | required | required |
| Core relation | criterion-based evaluation | capability/risk characterization | expected ↔ actual comparison |
| Finding | local output | local output | local output |
| Capability/risk characterization | possible | central output | not identity |
| Sourcing decision input | possible downstream | central downstream use | not identity |
| Re-verification | contextual/downstream | contextual/downstream | core in closed verification realization |
| Physical presence | not required | not required | not required |
| Identity-bearing element | evaluation against criterion | **not yet independently proven** | expected-vs-actual comparison |

### Result: PASS

Expected-vs-Actual Verification is clearly separated from both Audit and PSA.

---

## 7. Test F — Machine versus Domain Realization

The comparison supports the following hierarchy as the more conservative current architecture:

```
PATTERN
  ↓
ASSESSMENT AGAINST CRITERION
  ↓
MACHINE: Audit
  ↓
DOMAIN REALIZATION / SPECIALIZATION
  ├─ Supplier Capability / PSA
  ├─ QSB Audit
  ├─ Process Control Plan Audit
  ├─ Labeling Audit
  └─ Special Process Audit
```

This does **not** mean that all named audits are automatically identical Machines.

It means:

> the current evidence does not justify creating a new top-level Machine merely because the audited object and the downstream decision context differ.

A separate Machine becomes justified only when its own identity-bearing relation, boundary, local capability and closure condition are independently demonstrated.

---

## 8. Important qualification

The previous Passport trial established:

> **Supplier Capability Assessment is a MACHINE CANDIDATE WITH QUALIFICATION.**

This boundary comparison does not delete that result.

It refines it:

> **PSA is a valid bounded execution candidate, but its independence from Audit is NOT YET PROVEN.**

Therefore the current status should be read as:

`BOUNDED EXECUTION = SUPPORTED`

`DOMAIN REALIZATION = SUPPORTED`

`INDEPENDENT MACHINE IDENTITY = HOLD`

`AUDIT SPECIALIZATION / REALIZATION = STRONG HYPOTHESIS`

---

## 9. Consequence for Machine Passport

No schema change is required.

Passport v0.3 correctly separates:

- invariant identity;
- execution boundary;
- local capability;
- domain realization;
- downstream ownership.

The comparison demonstrates why **domain** and **output semantics** must not be mistaken for Machine identity.

---

## 10. Consequence for Machine Catalog

Do **not** add another top-level Machine on the basis of this test.

Existing:

`MC-009-15 Audit`

remains the relevant existing Machine candidate.

`MC-CAND-096-05 Supplier Capability Assessment`

remains a GM-derived candidate, but its status should remain **NON-CANON / HOLD FOR MACHINE-INDEPENDENCE** until another source or a stronger cross-domain realization demonstrates a distinct identity-bearing execution relation.

No Catalog modification is made by this patch.

---

## 11. Architectural finding

This test produces a useful general rule:

> **A domain-specific assessment is not a new Machine merely because it has a different assessed object, terminology, score, or downstream decision use.**

To establish independent Machine identity, the domain realization must preserve a distinct:

`identity-bearing relation/mode + own execution boundary + local capability + closure condition`

that cannot be reduced to a specialization of an already established Machine.

This is particularly important for CMOC because otherwise the Catalog will proliferate with named audits that differ primarily by object/domain.

---

## 12. Status

- Audit ↔ Supplier Capability Assessment: **DISTINGUISHED AS DOMAIN / SEMANTIC SPECIALIZATION, INDEPENDENCE NOT PROVEN**
- Supplier Capability Assessment bounded execution: **SUPPORTED**
- PSA as domain realization: **SUPPORTED**
- Supplier Capability Assessment as independent Machine: **HOLD**
- Audit ↔ Expected-vs-Actual Verification: **DISTINGUISHED**
- Supplier Capability Assessment ↔ Expected-vs-Actual Verification: **DISTINGUISHED**
- Machine vs Domain Realization boundary: **STRENGTHENED**
- Machine Passport v0.3: **NO CHANGE**
- Catalog: **NO CHANGE**
- Canon: **NO CHANGE**
- REG-001: **NO CHANGE**

## 13. Step closure

The focused Boundary Comparison is complete.

**Nothing additional needs to be changed now.**

The next GM-096 candidate can be tested through Passport v0.3, while Supplier Capability Assessment remains on **HOLD for independent Machine identity** rather than being prematurely promoted.

