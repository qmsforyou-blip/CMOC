# PATCH-ISO-040

## ISO-040 — 10.2 Nonconformity and corrective action

**Источник:** ISO/DIS 9001:2025(E)-6th-Ed
**Статус:** CANDIDATE / SINGLE-SOURCE
**Извещение на изменение:** 0109+270826

---

## SOURCE CLAIM

10.2.1 устанавливает действия при возникновении nonconformity:

1. React to the nonconformity:
   - take action to control and correct it, as applicable;
   - deal with the consequences.
2. Evaluate the need for action to eliminate the cause(s), чтобы nonconformity не повторилась и не возникла elsewhere, посредством:
   - reviewing the nonconformity;
   - determining the causes;
   - determining whether similar nonconformities exist or can potentially occur.
3. Implement any action needed.
4. Review the effectiveness of corrective action taken.
5. Update risks and opportunities determined during planning, if necessary.
6. Make changes to the QMS, if necessary.

Corrective actions shall be appropriate to the effects of the nonconformities encountered. Customer complaints can be a source of nonconformities.

10.2.2 требует documented information как evidence:
- nature of nonconformities and subsequent actions;
- results of corrective action. fileciteturn98file2

Annex A.10.2 уточняет, что 10.2 охватывает как nonconforming outputs из 8.7, так и другие nonconformities QMS. Nonconformities могут классифицироваться по severity; severity связана с negative consequences для QMS и способности стабильно обеспечивать conformity. Risk-based thinking может использоваться для анализа nonconformity и оценки severity. Не требуется corrective action для каждой nonconformity: организация определяет допустимые пределы recurrence и необходимость действий по причинам. Конкретный метод/техника не предписывается; root cause analysis не является обязательным требованием. fileciteturn98file4

---

## TERMS

- Nonconformity
- Corrective action
- Cause(s)
- Consequence
- Severity
- Recurrence
- Similar nonconformity
- Effectiveness
- Risk / opportunity

---

## DISTINCTIONS

### DIS-001 — NONCONFORMITY ≠ NONCONFORMING OUTPUT

10.2 охватывает и nonconforming outputs из 8.7, и другие nonconformities QMS. Следовательно, scope nonconformity шире operational output.

**STRONG CANDIDATE / SINGLE-SOURCE**

### DIS-002 — REACTION ≠ CORRECTIVE ACTION

Реакция включает control/correction и dealing with consequences; corrective action направлена на elimination of cause(s) и prevention of recurrence.

**STRONG CANDIDATE**

### DIS-003 — CORRECTION ≠ ELIMINATION OF CAUSE

Correction относится к реакции на возникшую nonconformity; corrective action — к причине и recurrence.

**STRONG CANDIDATE**

### DIS-004 — CONSEQUENCE ≠ CAUSE

Организация отдельно deal with consequences и determines causes.

**STRONG CANDIDATE**

### DIS-005 — REVIEWING NONCONFORMITY ≠ DETERMINING CAUSES

Source задаёт их как отдельные действия в последовательности evaluation of need for action.

**CANDIDATE**

### DIS-006 — CAUSE ≠ SIMILAR NONCONFORMITY

Определение causes и проверка существования/potential occurrence similar nonconformities — разные операции.

**STRONG CANDIDATE**

### DIS-007 — CORRECTIVE ACTION ≠ CORRECTIVE ACTION EFFECTIVENESS

Принятие/реализация corrective action и последующий review её effectiveness — разные этапы.

**STRONG CANDIDATE**

### DIS-008 — CORRECTIVE ACTION ≠ MANDATORY RESPONSE TO EVERY NONCONFORMITY

Annex A прямо указывает, что corrective action не требуется для каждой nonconformity; необходимость определяется организацией в установленных пределах recurrence и с учётом обязательных требований.

**STRONG CANDIDATE**

### DIS-009 — SEVERITY ≠ NONCONFORMITY

Severity характеризует уровень negative consequences, а не сам факт non-fulfilment requirement.

**CANDIDATE**

### DIS-010 — ROOT CAUSE ANALYSIS ≠ ISO REQUIREMENT

ISO требует determining causes, но Annex A прямо говорит, что root cause analysis как конкретный метод не является обязательным.

**STRONG CANDIDATE**

### DIS-011 — CORRECTIVE ACTION ≠ PREVENTIVE ACTION

В определении 3.17 corrective action направлена на prevention of recurrence; preventive action — на prevention of occurrence. fileciteturn98file5

**CANDIDATE / SINGLE-SOURCE**

### DIS-012 — NONCONFORMITY RESPONSE ≠ QMS CHANGE

QMS change является отдельным возможным последующим действием, если необходимо.

**STRONG CANDIDATE**

---

## GM

### GM-001

> При возникновении nonconformity сначала реагируй на неё: control/correct и deal with consequences.

### GM-002

> Отдельно оценивай необходимость действий по elimination of cause(s) и prevention of recurrence/occurrence elsewhere.

### GM-003

> Проверяй, существуют ли similar nonconformities или могут ли они возникнуть.

### GM-004

> После реализации corrective action review её effectiveness.

### GM-005

> При необходимости обновляй risks/opportunities и меняй QMS.

### GM-006

> Не применяй corrective action механически к каждой nonconformity; оценивай необходимость действия.

---

## REL

### REL-001

```text
NONCONFORMITY
 ↓
REACTION
 ├── CONTROL / CORRECTION
 └── CONSEQUENCES
```

### REL-002

```text
NONCONFORMITY
 ↓
REVIEW
 ↓
CAUSES
 ↓
SIMILAR / POTENTIAL NONCONFORMITIES
 ↓
NEED FOR ACTION
```

### REL-003

```text
NEED FOR CORRECTIVE ACTION
 ↓
IMPLEMENT ACTION
 ↓
REVIEW EFFECTIVENESS
```

### REL-004

```text
CORRECTIVE ACTION
 ↓
EFFECTIVENESS REVIEW
 ↓
UPDATE RISKS / OPPORTUNITIES, IF NECESSARY
```

### REL-005

```text
NONCONFORMITY
 ↓
CORRECTIVE ACTION
 ↓
QMS CHANGE, IF NECESSARY
```

### REL-006

```text
NONCONFORMITY
 ↓
SEVERITY / EFFECTS
 ↓
APPROPRIATENESS OF CORRECTIVE ACTION
```

### REL-007

```text
NATURE OF NONCONFORMITY
+
SUBSEQUENT ACTIONS
+
CORRECTIVE ACTION RESULTS
 ↓
DOCUMENTED INFORMATION / EVIDENCE
```

Все новые REL — **CANDIDATE / SINGLE-SOURCE**.

---

## MECHANISM

### M-045 — Nonconformity and corrective-action mechanism

```text
NONCONFORMITY OCCURS
        ↓
REACTION
 ├── CONTROL / CORRECT
 └── DEAL WITH CONSEQUENCES
        ↓
REVIEW NONCONFORMITY
        ↓
DETERMINE CAUSES
        ↓
CHECK SIMILAR / POTENTIAL NONCONFORMITIES
        ↓
EVALUATE NEED FOR ACTION
        ↓
IMPLEMENT ACTION, IF NEEDED
        ↓
REVIEW EFFECTIVENESS
        ↓
UPDATE RISKS / OPPORTUNITIES, IF NECESSARY
        ↓
CHANGE QMS, IF NECESSARY
```

Это единый механизм управления возникшей nonconformity, но corrective action является его отдельной ветвью/частью, а не синонимом всей реакции.

**M-045 — CANDIDATE / SINGLE-SOURCE**

---

## CAPABILITY

### CAP-040 — Nonconformity management capability

> Способность организации реагировать на возникшую nonconformity, контролировать и исправлять её последствия, определять причины и необходимость corrective action, проверять effectiveness принятых действий и при необходимости изменять risks/opportunities и QMS.

**CANDIDATE / SINGLE-SOURCE**

---

## CORE CANDIDATES

### CORE-CANDIDATE-113
**Reaction to nonconformity ≠ corrective action**

**STRONG CANDIDATE**

### CORE-CANDIDATE-114
**Cause-oriented action is conditional**

Не каждая nonconformity автоматически требует corrective action.

**STRONG CANDIDATE**

### CORE-CANDIDATE-115
**Effectiveness must be reviewed after corrective action**

**STRONG CANDIDATE**

### CORE-CANDIDATE-116
**Similar/potential recurrence must be considered**

Corrective action выходит за пределы единичного случая.

**STRONG CANDIDATE**

### CORE-CANDIDATE-117
**Corrective action can modify the system**

При необходимости результатом становится изменение QMS.

**CANDIDATE**

### CORE-CANDIDATE-118
**Nonconformity severity influences appropriateness of action**

**CANDIDATE / SINGLE-SOURCE**

---

## MACHINE

### MACHINE-CANDIDATE-008 — Corrective action machine

```text
NONCONFORMITY
 ↓
REACTION / CONTROL
 ↓
CONSEQUENCES
 ↓
CAUSE ANALYSIS
 ↓
SIMILAR / POTENTIAL CASES
 ↓
ACTION DECISION
 ↓
CORRECTIVE ACTION
 ↓
EFFECTIVENESS REVIEW
 ↓
SYSTEM UPDATE, IF NEEDED
```

Конструкция содержит вход, преобразования, условную ветвизацию и feedback через effectiveness review. Но конкретной physical realization Source не задаёт.

**STRONG CANDIDATE / SINGLE-SOURCE**

В `MACHINE-CATALOG` пока не переносится.

---

## CHAIN

### CHAIN-CANDIDATE-063

```text
NONCONFORMITY
 ↓
REACTION
 ↓
CONTROL / CORRECTION
 ↓
CONSEQUENCES
```

### CHAIN-CANDIDATE-064

```text
NONCONFORMITY
 ↓
REVIEW
 ↓
CAUSES
 ↓
SIMILAR / POTENTIAL CASES
 ↓
NEED FOR ACTION
```

### CHAIN-CANDIDATE-065

```text
ACTION
 ↓
EFFECTIVENESS REVIEW
 ↓
UPDATE RISKS / OPPORTUNITIES
 ↓
QMS CHANGE
```

Последние два перехода являются условными (`if necessary`).

**CANDIDATE / SINGLE-SOURCE**

---

## ROLE

**NONE**

## PHYSICAL REALIZATION

**NONE**

---

## DOCUMENT / DOCUMENTED INFORMATION / RECORD

10.2.2 прямо требует documented information как evidence:

```text
NATURE OF NONCONFORMITY
+
SUBSEQUENT ACTIONS
+
CORRECTIVE ACTION RESULTS
        ↓
DOCUMENTED INFORMATION
        ↓
EVIDENCE
```

При этом Source не требует документировать конкретный метод cause analysis. Annex A, напротив, подчёркивает, что specific method/technique не предписан. fileciteturn98file4

И снова сохраняем различение:

```text
DOCUMENTED INFORMATION ≠ автоматически RECORD
```

---

## CMOC INTERPRETATION

### 1. Это важное расширение ISO-035

8.7 управляет **nonconforming output**.

10.2 управляет **nonconformity как более общим событием**, включая nonconforming outputs и другие несоответствия QMS. fileciteturn98file4

Поэтому:

```text
NONCONFORMING OUTPUT
        ⊂
NONCONFORMITY
```

— перспективная CMOC-интерпретация, а не буквальное равенство терминов Source.

### 2. Самая сильная архитектурная граница

```text
REACTION
 ≠
CORRECTIVE ACTION
```

Реакция работает с **возникшим событием и его последствиями**.

Corrective action работает с **причиной и recurrence**.

### 3. Появляется горизонт распространения

```text
ONE NONCONFORMITY
 ↓
SIMILAR CASES
 ↓
POTENTIAL OCCURRENCE ELSEWHERE
```

То есть действие направляется не только назад на конкретный случай, но и **в сторону потенциального распространения проблемы**.

### 4. Effectiveness — замыкает corrective-action loop

```text
ACTION
 ↓
EFFECTIVENESS REVIEW
```

Без этого Source не считает цепочку завершённой.

### 5. Очень важный отрицательный результат

ISO **не требует root cause analysis как конкретного метода**. Он требует determining causes, но способ определения причин оставляет организации. fileciteturn98file4

Следовательно, в CMOC не создаём из ISO-040 Machine `Root Cause Analysis`.

---

## CROSS-CLAUSE

### ISO-035 → ISO-040

```text
8.7
NONCONFORMING OUTPUT
 ↓
CONTROL / CORRECTION
```

затем:

```text
10.2
NONCONFORMITY
 ↓
CAUSE / RECURRENCE
 ↓
CORRECTIVE ACTION
```

### ISO-036 → ISO-040

```text
MONITOR / MEASURE
 ↓
ANALYSIS / EVALUATION
 ↓
NONCONFORMITY
 ↓
CORRECTIVE ACTION
 ↓
EFFECTIVENESS REVIEW
```

### ISO-038 → ISO-040

```text
MANAGEMENT REVIEW
 ↓
NONCONFORMITIES / CORRECTIVE ACTION TRENDS
 ↓
MANAGEMENT DECISION
```

### ISO-039 → ISO-040

```text
IMPROVEMENT OPPORTUNITY
 ↓
ACTION
```

10.2 показывает частный, cause-oriented механизм action для nonconformity.

**MULTI-CONFIRMATION CANDIDATE**

---

## STATUS SUMMARY

- DIS: **12 candidates**
- REL: **7 candidates**
- M: **M-045 NEW**
- CAP: **CAP-040 NEW**
- CORE: **6 candidates**
- MACHINE: **MACHINE-CANDIDATE-008 / STRONG**
- CHAIN: **3 candidates**
- ROLE: **NONE**
- PHYSICAL REALIZATION: **NONE**
- Documented information: **evidence of nature/actions/results**
- Record: **не классифицирован автоматически**
- Overall: **CANDIDATE / SINGLE-SOURCE**

---

## PHYSICAL FIXATION

**Извещение на изменение — 0109+270826**

**Файл:** `04 PATCH/PATCH-ISO-040.md`

**CORE / MACHINE-CATALOG / ROLE-CATALOG / CHAIN-CATALOG:** не изменялись.
