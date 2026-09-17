# GM-096 — Production Trial Run (PTR) — Cross-Check

## Извещение на изменение

**0128+170926**

---

## 1. OBJECT OF CHECK

GM-096, section **11.3 Production Trial Run (PTR) process**, pp. 333–335.

Вопрос:

> является ли Production Trial Run (PTR) самостоятельной специализированной Machine либо только отдельным шагом Change Control?

**Working verdict:** `SPECIALIZED MACHINE CANDIDATE / NON-CANON`.

---

## 2. SOURCE-DERIVED PURPOSE

GM требует от поставщика **defined PTR process** с элементами:

- Standardized Communication and Documentation;
- Build Readiness Reviews;
- Quality Reviews before and after the change.

Сам PTR определяется как **limited, controlled and contained production tryout**, используемый для оценки изменения до его полной реализации в производстве.

Источник отдельно указывает, что PTR подтверждает manufacturability изменения в нормальной производственной среде и **не является substitute или extension of the product validation process**.

Также требуется written procedure и flow chart, определяющие PTR process и requirements.

fileciteturn564file0L12-L28

---

## 3. SOURCE-DERIVED CONTROL LOGIC

Из текста источника следует следующая рабочая последовательность:

```text
CHANGE REQUIRING TRIAL
        ↓
PTR REQUEST / INFORMATION
        ↓
PTR REQUIREMENT DECISION
        ↓
PTR DECISION / APPROVAL TO RUN
        ↓
READINESS REVIEW / APPROVAL
        ↓
CONTROLLED PRODUCTION TRYOUT
        ↓
QUALITY REVIEW
        ↓
CUSTOMER EVALUATION (IF APPLICABLE)
```

Важно: источник не даёт в рассмотренном фрагменте универсального алгоритма окончательного решения после PTR. Поэтому не вводим его самостоятельно.

Communication Form должен документировать каждый шаг процесса и все approvals and results.

Предлагаемые source sections формы:

- Change Leader PTR Request and Information;
- PTR Core Team PTR Decision and Approval to Run PTR;
- Customer Contacts;
- Customer / Internal PTR Requirement Decision;
- PTR Readiness Approval;
- Internal PTR Review and Approval;
- Customer Evaluation of PTR.

fileciteturn563file0L12-L23

---

## 4. DISTINCTIONS

### D-01

**PTR ≠ Change Control**

Change Control управляет самим изменением; PTR является контролируемой производственной пробой для оценки изменения перед полной реализацией.

### D-02

**PTR ≠ Product Validation**

Это прямо установлено источником: PTR не является заменой или расширением процесса product validation.

fileciteturn564file0L18-L27

### D-03

**PTR ≠ ordinary production run**

PTR специально определён как limited, controlled and contained production tryout.

### D-04

**PTR Approval ≠ PTR Readiness**

Источник выделяет отдельно решение/approval to run PTR и PTR Readiness Approval. Следовательно, эти состояния нельзя автоматически сводить в одно.

### D-05

**Readiness Review ≠ Quality Review**

Build Readiness Reviews и Quality Reviews before/after the change названы источником как разные элементы PTR process.

### D-06

**PTR Record ≠ PTR Process**

Communication Form фиксирует шаги, approvals и results; форма является record / средством документирования процесса, а не самим процессом.

fileciteturn563file0L12-L22

---

## 5. MACHINE TEST

| Test | Result |
|---|---|
| Explicit trigger / use condition | YES — evaluation of a change prior to full production implementation |
| Defined object | YES — change under controlled production tryout |
| Defined roles / decision points | YES |
| Defined controls | YES |
| Readiness mechanism | YES |
| Controlled execution | YES |
| Quality review before / after | YES |
| Documentation / records | YES |
| Reusable procedure | YES |
| Source explicitly requires defined procedure | YES |

**Result:** sufficient basis for a specialized Machine candidate.

---

## 6. CMOC CLASSIFICATION

**Production Trial Run (PTR):** `SPECIALIZED MACHINE CANDIDATE`

Не Canon.

Не следует автоматически дробить PTR на отдельные Machines:

- Communication and Documentation;
- Build Readiness Review;
- Quality Review;
- Approval;
- Customer Evaluation;
- PTR Form.

В source они образуют составные элементы единого PTR process.

---

## 7. ARCHITECTURAL VALUE

PTR показывает отдельный тип управленческой машины:

```text
PROPOSED / APPROVED CHANGE
          ↓
   CONTROLLED TRIAL
          ↓
  EVIDENCE IN NORMAL
 PRODUCTION ENVIRONMENT
          ↓
  QUALITY REVIEW / EVALUATION
```

Архитектурно существенен переход от **изменения как намерения** к **проверке изменения в реальной производственной среде до полной реализации**.

При этом PTR не следует смешивать с product validation: источник специально проводит эту границу.

---

## 8. RELATION TO OTHER MACHINES

```text
Plant Process Change Control
          ↓
     change requiring
          ↓
Production Trial Run (PTR)
          ↓
 readiness / controlled trial
          ↓
 quality review / evaluation
```

PTR является специализированным механизмом внутри более широкого контекста Managing Change, но source требует для него отдельный defined process, written procedure и flow chart.

---

## 9. FINAL WORKING VERDICT

> **Production Trial Run (PTR) — самостоятельный специализированный Machine candidate, обеспечивающий ограниченную, контролируемую и локализованную производственную пробу изменения до его полной реализации. Его назначение — оценить изменение в нормальной производственной среде; PTR не заменяет product validation.**

**STATUS:** `SPECIALIZED MACHINE CANDIDATE / NON-CANON`

---

## 10. DECISION RECORD

- New Top-Level Machine: NO.
- Specialized Machine candidate: YES — `Production Trial Run (PTR)`.
- Existing CMOC duplication found: NO — repository search for `Production Trial`, `PTR`, `Trial Run`, `Validation` returned no existing candidate.
- REG-001: unchanged.
- Canon: unchanged.
- Source provenance preserved.

**Next check:** финальная сверка блока **GM-096 Managing Change, pp. 323–345** — сопоставить Plant Process Change Control, PTR, Banking, Bypass и итоговые Key Strategies без создания дубликатов.
