# GM-096 — Candidate Catalog Cross-Check

## Извещение на изменение — `0130+170926`

**Название файла:** `GM-096-Candidate-Catalog-CrossCheck.md`

---

## 1. Назначение

Провести сверку Machine Candidates, извлечённых из `GM Quality System Basics Overview Supplier Audit`, с текущим `MACHINE-CATALOG` CMOC.

Цель этапа — не канонизация, а разделение:

- новых Machine Candidates;
- уже существующих Machine / Machine Families;
- механизмов и паттернов;
- Assemblies / Chains;
- элементов, требующих дополнительного cross-check.

Правило: наличие отдельного термина в источнике само по себе не создаёт новую Machine.

---

## 2. База сравнения

Текущий каталог содержит Machine Patterns:

- MP-001 Visual Control;
- MP-002 Response to Abnormality;
- MP-003 Problem Solving;
- MP-004 Knowledge Transfer;
- MP-005 Assessment against Criterion.

И существующие Machines:

- MC-008-03 Визуализация производственного потока;
- MC-008-05 Стандарт на рабочем месте;
- MC-008-06 Цель–факт;
- MC-008-07 Визуальная карта разработки;
- MC-009-10 Andon;
- MC-009-11 Gemba Walk;
- MC-009-12 Asaichi;
- MC-009-15 Audit;
- MC-009-17 Yokoten.

System Machines:

- MC-009-14 Двойной цикл мастера;
- MC-009-16 Kamishibai;
- MC-009-13 Сертификация лучшей линии.

Каталог является WORKING / NON-CANON; канонизация выполняется отдельно.

---

## 3. Сверка кандидатов GM-096

| GM element | CMOC classification | Existing CMOC relation | Decision |
|---|---|---|---|
| Plant Process Change Control (PPCR) | MACHINE CANDIDATE | Exact existing Machine not identified | KEEP as new candidate |
| Production Trial Run (PTR) | SPECIALIZED MACHINE CANDIDATE | Exact existing Machine not identified | KEEP as specialized candidate |
| Banking Process | SPECIALIZED MACHINE CANDIDATE | Exact existing Machine not identified | KEEP as specialized candidate |
| Bypass Process Control | SPECIALIZED MACHINE CANDIDATE | Parent mechanism: Controlled Deviation | KEEP candidate; do not duplicate parent mechanism |
| Supplier Capability Assessment | MACHINE CANDIDATE | No exact existing Machine identified | KEEP as candidate |
| Nonconforming Product Control | MACHINE CANDIDATE | No exact existing Machine identified | KEEP as candidate |
| LPA | SPECIALIZED AUDIT FAMILY / PATTERN | MC-009-15 Audit | DO NOT create top-level duplicate |
| Fast Response | RESPONSE PATTERN / CHAIN | MC-009-10 Andon + MP-002 Response to Abnormality | HOLD; further evidence required |
| Systemic Problem Resolution | PROBLEM-SOLVING PATTERN / EXISTING ARCHITECTURE | MP-003 + MC-009-12 Asaichi | DO NOT create duplicate |
| Workshop / Action-Plan Conversion | ASSEMBLY / PATTERN | composes problem-solving actions | DO NOT create Machine |
| Measurement-to-Action | FUNDAMENTAL PATTERN / MECHANISM | supports Control / Response / Decision | DO NOT create Machine |
| Control Means Verification | SPECIALIZED MECHANISM / MACHINE-SUBCANDIDATE | related to Verification / Audit | HOLD below top-level Machine |
| Error-Proofing Verification | SPECIALIZATION of Control Means Verification | related to Verification | DO NOT create separate top-level Machine |
| Controlled Deviation | GENERIC MECHANISM / PATTERN | parent for Bypass specialization | DO NOT create Machine |
| Decision Gate | MECHANISM | supports approval / release decisions | HOLD pending wider architecture cross-check |
| Controlled Change Implementation | MECHANISM / SUBPROCESS | part of PPCR architecture | DO NOT create separate Machine |

---

## 4. Candidate identity test

### 4.1 Plant Process Change Control

Source architecture describes a controlled procedure for planned, emergency and other plant process changes, with a Plant Process Change Request, review/approval, implementation recording and final approval.

CMOC interpretation:

`REQUEST → REVIEW → APPROVAL → IMPLEMENTATION → POST-IMPLEMENTATION → FINAL APPROVAL`

This is sufficiently structured to remain a Machine Candidate.

**Status:** MACHINE CANDIDATE / NON-CANON.

---

### 4.2 Production Trial Run

PTR is described as a limited, controlled and contained production tryout used to evaluate a change before full production implementation, with readiness reviews, communication, approvals and evaluation.

PTR is not treated as a generic "test" term. Its identity is the controlled organizational construction around a production trial.

**Status:** SPECIALIZED MACHINE CANDIDATE / NON-CANON.

---

### 4.3 Banking Process

Banking is a controlled process for identification, protection, retrieval and quality control of parts/material stored for extended periods, including traceability, FIFO, environmental protection, LPA and quality requirements before shipment.

It is not reduced to ordinary storage because the source defines a specific controlled process with responsibilities, records and release-related checks.

**Status:** SPECIALIZED MACHINE CANDIDATE / NON-CANON.

---

### 4.4 Bypass Process Control

The source defines a controlled procedure for temporary operation outside an approved documented Control Plan, including authorization, documented bypasses, PFMEA/Control Plan inclusion, standardized work, training, monitoring, breakpoint records and verified return to the original process.

Generic parent:

`Controlled Deviation`

Specialized realization:

`Bypass Process Control`

**Status:** SPECIALIZED MACHINE CANDIDATE / NON-CANON.

---

### 4.5 Supplier Capability Assessment

The candidate is retained because the GM material describes a structured assessment of supplier capability rather than merely naming an assessment criterion.

At this stage no exact existing Machine identity in the current catalog has been established.

**Status:** MACHINE CANDIDATE / NON-CANON.

---

### 4.6 Nonconforming Product Control

The candidate is retained as a controlled organizational construction around identification, containment, disposition and control of nonconforming product.

It should not be collapsed into the generic Problem Solving or Response patterns: those may be invoked by the machine, but they are not identical to the machine's control purpose.

**Status:** MACHINE CANDIDATE / NON-CANON.

---

## 5. Existing architecture absorbs the following GM elements

### LPA

LPA is retained as source provenance and specialized Audit realization. The current catalog already contains `MC-009-15 Audit`; therefore a second top-level Machine would risk duplication.

### Fast Response

Fast Response is not promoted independently at this stage. In the existing architecture it can be realized as a chain involving `Andon` and `Response to Abnormality` and should not automatically become a duplicate Machine.

### Systemic Problem Resolution

The existing `MP-003 Problem Solving` and `MC-009-12 Asaichi` already cover the problem-solving family. GM-096 adds useful source evidence and specialization, but no independent top-level Machine identity is established by this cross-check.

### Workshop / Action-Plan Conversion

This is better understood as an Assembly / Pattern that converts a problem-solving workshop output into controlled actions. It is not itself a single Machine.

### Measurement-to-Action

The previously established GM-096 cross-check classified this as a fundamental pattern/mechanism:

`Observe → Compare → Interpret → Decide → Act → Verify`

No separate Machine is created.

### Control Means Verification

This remains below top-level Machine level as a specialized mechanism / Machine-subcandidate. `Error-Proofing Verification` is treated as its specialization, not as a separate Machine.

### Controlled Deviation

Generic mechanism/pattern. `Bypass Process Control` is the specialized Machine candidate.

---

## 6. Architectural consequence

GM-096 should not be represented in CMOC as a flat list of independent Machines.

Its stronger architectural reading is a managed-change grammar:

```text
CHANGE / CHANGE NEED
        ↓
PLANT PROCESS CHANGE CONTROL
        ↓
NORMAL CHANGE or TRIAL REQUIRED
        ↓
PTR
        ↓
QUALITY / EVALUATION
        ↓
IMPLEMENTED STATE
        ↓
 ┌───────────────┬─────────────────┐
 ↓               ↓                 ↓
NORMAL FLOW    BANKING          BYPASS STATE
                 MATERIAL
 └───────────────┴─────────────────┘
        ↓
VERIFICATION / REVIEW
        ↓
ACCEPTED / CLOSED
```

This is a CMOC architectural interpretation, not a claim that the GM source presents the above as one literal flow chart.

The four principal operational questions are:

1. **Can we change?** → Plant Process Change Control.
2. **Do we need to test first?** → Production Trial Run.
3. **What do we do with material outside normal flow?** → Banking Process.
4. **What do we do when the normal process is temporarily unavailable?** → Bypass Process Control.

---

## 7. What is deliberately NOT changed

At this stage:

- `REG-001` is not modified;
- Canon is not modified;
- existing Machine passports are not rewritten;
- no GM term is canonized;
- no existing Machine is renamed merely to absorb GM terminology;
- no new Machine ID is assigned yet.

The catalog update should follow this cross-check, not precede it.

---

## VERDICT

GM-096 yields **six retained new Machine Candidates**:

- Plant Process Change Control;
- Production Trial Run;
- Banking Process;
- Bypass Process Control;
- Supplier Capability Assessment;
- Nonconforming Product Control.

The remaining significant elements are absorbed as existing Machines, Patterns, Mechanisms or Assemblies, or remain on HOLD.

## STATUS

`CROSS-CHECK COMPLETE / NON-CANON`

No Canon or REG-001 changes.

## NEXT CHECK

Update `03_MACHINE-CATALOG/MACHINE-CATALOG.md.md` with the six retained candidates, preserving their NON-CANON / CANDIDATE status and without assigning premature canonical IDs.
