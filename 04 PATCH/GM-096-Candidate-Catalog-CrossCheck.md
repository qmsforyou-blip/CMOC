# GM-096 Candidate Catalog Cross-Check

> Извещение на изменение: **0130+170926**
>
> Файл: `04 PATCH/GM-096-Candidate-Catalog-CrossCheck.md`
>
> Статус: **WORKING / CROSS-CHECK / NON-CANON**
>
> Предыдущий подтверждённый commit: `2f62d43aeaea67a5a078983d17cd8b21015757b4` — `CMOC: final cross-check GM-096 Managing Change`.

---

## 1. Purpose

Провести сверку кандидатов, выявленных при разборе **GM Quality System Basics Overview Supplier Audit**, раздел **11 Managing Change**, с существующей архитектурой `MACHINE-CATALOG` CMOC.

Цель этапа — разделить:

- новую Machine;
- существующую Machine / новую provenance;
- Mechanism;
- Pattern;
- Assembly;
- специализацию существующей архитектуры;
- HOLD / требуется дополнительная проверка.

Ключевое правило:

> **SOURCE CLAIM ≠ CMOC INTERPRETATION.**

Наличие отдельного термина в GM не создаёт автоматически новую Machine.

GM-096 на уровне CMOC рассматривается не как плоский набор независимых Machines, а как возможная **грамматика управляемого изменения**. Это именно CMOC-интерпретация, а не утверждение, что GM QSB буквально представляет единую такую схему.

На этой стадии:

- не выполняется канонизация;
- не создаются дубли существующих Machines;
- `REG-001` не изменяется;
- Canon не изменяется;
- `MACHINE-CATALOG` данным PATCH не изменяется;
- паспорта новых кандидатов не создаются.

---

## 2. Source Basis

Основной источник: **GM Quality System Basics rev March 2009**, раздел **11 Managing Change**.

Source pages:

| Page | Content |
|---:|---|
| 324 | Outline: Introduction, Benefits, Change Process, PTR, Banking, Bypass, Summary |
| 325–326 | Purpose / Benefits |
| 327–329 | Plant Process Change / PPCR |
| 330–332 | продолжение Change Process / переход к PTR |
| 333–335 | Production Trial Run (PTR) |
| 336–339 | Banking Process |
| 340–343 | Bypass Process / Manufacturing Process Backup Worksheet |
| 344 | Summary, Shalls |

Источник требует систему управления planned/unplanned plant process changes, документирование PPCR и запись изменений; отдельно определяет PTR, Banking Process и Bypass Process. fileciteturn5file2L73-L104 fileciteturn5file1L20-L66 fileciteturn7file0L20-L75 fileciteturn7file1L100-L114

Для Bypass источник дополнительно фиксирует breakpoints, tooling/inspection/audit requirements, LPA, training/certification, verification перед возвратом и approval. fileciteturn4file4L94-L120

---

## 3. Candidate Map

| GM concept | CMOC classification | Existing CMOC ID | Decision | Rationale |
|---|---|---|---|---|
| **Plant Process Change Control (PPCR)** | Machine candidate | — | **NEW MACHINE CANDIDATE / STRONG** | Бounded repeatable construction: procedure, form, stakeholder review, approvals, records; covers planned and emergency changes. pp. 327–329, 344. fileciteturn5file2L85-L104 |
| **Production Trial Run (PTR)** | Specialized change-validation Machine candidate | — | **SPECIALIZED MACHINE CANDIDATE / NON-CANON** | Отдельная PTR procedure, communication form, decision/approval, customer/internal requirement decision and evaluation. pp. 333–335. fileciteturn5file1L20-L52 |
| **Banking Process** | Specialized material-state control Machine candidate | — | **SPECIALIZED MACHINE CANDIDATE / NON-CANON** | Идентификация, защита, retrieval, traceability, FIFO, storage and quality requirements for banked material. pp. 336–339. fileciteturn7file0L20-L75 |
| **Bypass Process Control** | Specialized implementation of Controlled Deviation | — | **SPECIALIZED MACHINE CANDIDATE / NON-CANON** | Контролируемый выход за approved process с defined entry/exit, verification and return requirements. pp. 340–343. fileciteturn7file1L100-L114 |
| **Supplier Capability Assessment** | Assessment pattern / adjacent architecture | — | **HOLD** | В reviewed pages 324–344 отдельная Machine identity не установлена. Не переносить термин в новую Machine без проверки исходной provenance. |
| **Nonconforming Product Control** | Existing quality-control architecture | — | **EXISTING ARCHITECTURE / NEW PROVENANCE** | QSB выделяет Control of Non-Conforming Product как отдельную strategy; GM-096 не даёт основания создавать ещё одну Machine поверх этой архитектуры. fileciteturn6file6L136-L156 |
| **LPA** | Audit family / verification mechanism | **MC-009-15 Audit** | **EXISTING MACHINE / NEW PROVENANCE** | GM-096 использует LPA для bypass и banking. Это новая application context существующего Audit, не новая top-level Machine. fileciteturn4file4L94-L120 |
| **Fast Response** | Response architecture / Pattern | **MC-009-10 Andon; MP-002 Response to Abnormality** | **EXISTING ARCHITECTURE / NEW PROVENANCE** | Active bypass reviewed at daily Fast Response meeting. Это provenance существующей response architecture. fileciteturn4file4L94-L104 |
| **Systemic Problem Resolution** | Existing problem-solving architecture | **MP-003 Problem Solving** | **HOLD** | Сильное пересечение с существующей Problem Solving architecture; distinct Machine identity не доказана. |
| **Workshop / Action-Plan Conversion** | Assembly / Pattern | — | **ASSEMBLY / PATTERN / NON-CANON** | Workshop produces starting points and action development; это не отдельная bounded Machine. fileciteturn4file4L165-L180 |
| **Measurement-to-Action** | Fundamental action Pattern | — | **PATTERN / NON-CANON** | Generic evidence → decision/action transformation; самостоятельная Machine не требуется. |
| **Control Means Verification** | Verification mechanism | — | **MECHANISM** | Verification of process parameters/settings and validation before return from bypass. fileciteturn4file4L100-L104 |
| **Error-Proofing Verification** | Specialized verification mechanism | — | **SPECIALIZED MECHANISM / HOLD** | QSB separately defines EPV as assuring error-proof/detection devices work as intended; GM-096 overlap не создаёт отдельной Machine. fileciteturn7file3L159-L197 |
| **Controlled Deviation** | Generic deviation / bypass mechanism | — | **MECHANISM / PATTERN** | Generic parent; Bypass Process Control — specialized realization. fileciteturn7file1L100-L114 |
| **Decision Gate** | Decision mechanism | — | **MECHANISM / PATTERN** | PTR содержит decision/approval steps; generic Gate is an abstraction, not a separate Machine. fileciteturn5file1L30-L44 |
| **Controlled Change Implementation** | Change-execution mechanism | — | **MECHANISM / PATTERN** | Распределён между PPCR, PTR, bypass, documentation, approval and verification; distinct Machine identity не установлена. |
| **Process Verification** | Verification mechanism / existing architecture | **MC-009-15 Audit** (partial overlap) | **MECHANISM / EXISTING ARCHITECTURE** | Embedded verification step in change/bypass re-entry; no basis for new top-level Machine. |
| **Contamination Control** | Existing specialized control architecture | — | **EXISTING ARCHITECTURE / NEW PROVENANCE** | Banking guidance explicitly considers environmental conditions causing rust, contamination, mold or distortion. fileciteturn7file0L46-L67 |

---

## 4. Duplicate / Specialization Check

### Andon — `MC-009-10`

Fast Response concerns structured response to quality/process abnormalities. It overlaps with `Andon` and `MP-002 Response to Abnormality`, but does not establish a separate Machine identity.

**Decision:** existing architecture / new provenance.

### Gemba Walk — `MC-009-11`

GM-096 does not establish Gemba Walk as the realization of Managing Change. No duplicate.

**Decision:** no new Machine.

### Asaichi — `MC-009-12`

Fast Response review may share a meeting function with Asaichi, but the source does not equate them.

**Decision:** no duplicate; relationship may be recorded later if evidence requires it.

### Audit — `MC-009-15`

LPA is the strongest direct overlap. GM-096 adds application context for bypass and banked material.

**Decision:** existing Audit / new provenance.

### Kamishibai — `MC-009-16`

No evidence that GM-096 requires a Kamishibai construction.

**Decision:** no duplicate.

### Problem Solving — `MP-003`

Systemic Problem Resolution overlaps the existing Problem Solving family. Workshop/action-plan conversion is better treated as Assembly/Pattern.

**Decision:** HOLD for Systemic Problem Resolution; no new top-level Machine.

### MP-002 Response to Abnormality

Fast Response and bypass management concern response to abnormal process conditions.

**Decision:** retain existing Pattern; GM-096 supplies provenance/application context.

### MP-005 Assessment against Criterion

PTR evaluation, process verification and Supplier Capability Assessment can instantiate assessment against criteria, but this alone does not establish a new Machine.

**Decision:** HOLD / existing Pattern relationship.

---

## 5. Architectural Interpretation

### 5.1 Patterns

Reusable Patterns identified or reinforced by GM-096:

- **Measurement-to-Action** — evidence → decision/action;
- **Controlled Deviation** — controlled departure from approved state;
- **Decision Gate** — evidence/requirements → authorization decision;
- **Response to Abnormality** — abnormal state → structured response;
- **Assessment against Criterion** — state/evidence → criterion-based judgment.

### 5.2 Mechanisms

GM-096 contributes mechanisms such as:

- change registration;
- stakeholder notification;
- approval before execution;
- trial/no-trial decision;
- breakpoint definition;
- material status separation;
- verification before re-entry;
- documented return to approved state;
- traceability;
- management authorization.

### 5.3 Machines

The current evidence supports four Machine directions:

```text
PPCR
→ NEW MACHINE CANDIDATE / STRONG

PTR
→ SPECIALIZED MACHINE CANDIDATE / NON-CANON

Banking Process
→ SPECIALIZED MACHINE CANDIDATE / NON-CANON

Bypass Process Control
→ SPECIALIZED MACHINE CANDIDATE / NON-CANON
```

### 5.4 Assembly

Workshop / Action-Plan Conversion is an **Assembly / Pattern** combining existing mechanisms and outputs.

### 5.5 Chain

The strongest CMOC interpretation is:

```text
CHANGE / CHANGE NEED
        ↓
PLANT PROCESS CHANGE CONTROL
        ↓
NORMAL CHANGE OR TRIAL REQUIRED?
        ↓
      ┌─┴───────────────┐
      │                 │
   NORMAL            PTR REQUIRED
      │                 ↓
      │          PTR / EVALUATION
      │                 ↓
      └───────→ IMPLEMENTED STATE
                         ↓
              ┌──────────┴──────────┐
              │                     │
        NORMAL FLOW          TEMPORARY / EXCEPTION
              │                     │
              │          BANKING / BYPASS CONTROL
              │                     ↓
              │               VERIFICATION
              └──────────────→ REVIEW / APPROVAL
                                   ↓
                              ACCEPTED / CLOSED
```

Это **CMOC interpretation**, а не буквальная схема GM QSB. Source отдельно defines Change Process, PTR, Banking and Bypass. fileciteturn7file0L4-L12

### 5.6 Four principal questions

| GM-096 question | CMOC element |
|---|---|
| **Can we change?** | Plant Process Change Control |
| **Do we need to test first?** | Production Trial Run |
| **What to do with material outside normal flow?** | Banking Process |
| **What to do if normal process is temporarily unavailable?** | Bypass Process Control |

---

## 6. Decisions

### NEW MACHINE CANDIDATE

**Plant Process Change Control (PPCR)** — **STRONG / NON-CANON**.

### SPECIALIZED MACHINE CANDIDATE

1. **Production Trial Run (PTR)** — NON-CANON.
2. **Banking Process** — NON-CANON.
3. **Bypass Process Control** — NON-CANON.

### EXISTING MACHINE / NEW PROVENANCE

- **LPA → MC-009-15 Audit**
- **Fast Response → MC-009-10 Andon / MP-002 Response to Abnormality**
- **Nonconforming Product Control → existing quality-control architecture**
- **Contamination Control → existing contamination-control architecture**
- **Process Verification → existing verification/audit architecture**

### MECHANISM

- Controlled Deviation;
- Control Means Verification;
- Decision Gate;
- Controlled Change Implementation;
- Process Verification.

### PATTERN

- Measurement-to-Action;
- Response to Abnormality;
- Assessment against Criterion;
- Controlled Deviation as reusable abstraction.

### ASSEMBLY

- Workshop / Action-Plan Conversion.

### HOLD

- Supplier Capability Assessment;
- Systemic Problem Resolution;
- Error-Proofing Verification as an independent Machine;
- any attempt to promote LPA, Fast Response or Process Verification to new top-level Machines.

---

## 7. Impact on CMOC Core

### REG-001

**No change.** No contradiction requiring an append-only correction was found.

### Canon

**No change.** No GM-096 element reaches the evidence threshold for canonization in this PATCH.

### MACHINE-CATALOG

**No direct update in this PATCH.**

The candidate catalog must not be expanded merely because the cross-check produced candidate classifications. Any catalog update is a separate next-stage PATCH after candidate passport work and/or additional provenance confirmation.

### Required next evidence

1. Passport the PPCR candidate and test whether its identity remains distinct from broader change-control mechanisms.
2. Compare PTR, Banking and Bypass candidates to determine whether they remain independent Machines or specialized realizations of a common change-control architecture.
3. Resolve provenance of Supplier Capability Assessment.
4. Keep LPA, Fast Response and Problem Solving attached to existing architecture unless new evidence demonstrates a distinct reproducible construction.

---

## VERDICT

GM-096 is better represented in CMOC as a **change-control grammar / Chain** than as a collection of independent Machines.

Current cross-check result:

```text
1 NEW MACHINE CANDIDATE
3 SPECIALIZED MACHINE CANDIDATES
multiple EXISTING ARCHITECTURE / NEW PROVENANCE links
several MECHANISMS
several PATTERNS
1 ASSEMBLY
several HOLD items

REG-001: UNCHANGED
CANON: UNCHANGED
MACHINE-CATALOG: UNCHANGED
```

## STATUS

`CROSS-CHECK COMPLETE / NON-CANON`

## NEXT CHECK

Only if the next evidence review confirms distinct Machine identity: update `03_MACHINE-CATALOG/MACHINE-CATALOG.md.md` and/or proceed to passports for the new candidates. Do not skip the passport/cross-check stage.
