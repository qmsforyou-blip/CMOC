# GM-050 — C.A.R.E. — Customer Acceptance Review & Evaluation

**Извещение на изменение:** 0161+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 3.6 — C.A.R.E. / Verification Station  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

SOURCE определяет **Customer Acceptance Review & Evaluation (C.A.R.E.)** как конструкцию, которая:

- защищает заказчика от non-conforming product, discrepancies и labeling errors;
- проверяет эффективность process controls;
- применяется к part-related customer satisfaction items;
- включает Pass Through Characteristics, Labeling и Past Formal Customer Issues;
- должна проводиться при содействии Plant Manager и Quality Manager;
- имеет Alarm Limit = ONE;
- требует передачи Non-Conforming Data в Fast Response Meeting;
- требует добавления Root Cause / Corrective Action в Layered Process Audit. fileciteturn148file0

## 2. LOCATION

**p. 103 — 3.6 C.A.R.E., Verification Station.**

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Customer Acceptance Review & Evaluation (C.A.R.E.)** | обзор и оценка приемлемости для заказчика |
| **Customer Acceptance** | приемлемость для заказчика |
| **Customer Satisfaction Items** | элементы, влияющие на удовлетворённость заказчика |
| **Part Related** | относящийся к детали / изделию |
| **Pass Through Characteristics** | характеристики, проходящие через процесс к заказчику |
| **Labeling** | маркировка |
| **Past Formal Customer Issues** | прошлые формальные проблемы заказчика |
| **Process Controls** | управления / средства контроля процесса |
| **Non-Conforming Product** | несоответствующая продукция |
| **Discrepancy** | расхождение / несоответствие |
| **Alarm Limit** | порог Alarm |
| **Non-Conforming Data** | данные о несоответствующей продукции |
| **Fast Response Meeting** | совещание Fast Response |
| **Root Cause** | коренная причина |
| **Corrective Action** | корректирующее действие |
| **Layered Process Audit (LPA)** | многоуровневый аудит процесса |
| **Plant Manager** | руководитель предприятия |
| **Quality Manager** | руководитель по качеству |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### 4.1 C.A.R.E. ≠ обычная проверка изделия

SOURCE задаёт одновременно две цели: защита заказчика и проверка эффективности process controls.

### 4.2 Customer Satisfaction Item ≠ любой показатель качества

SOURCE ограничивает область C.A.R.E. part-related customer satisfaction items.

### 4.3 C.A.R.E. ≠ Fast Response

C.A.R.E. обнаруживает / оценивает соответствующие customer-related conditions; Non-Conforming Data затем направляются в Fast Response Meeting.

### 4.4 C.A.R.E. ≠ LPA

Root Cause / Corrective Action должны быть добавлены в LPA. Это связь между конструкциями, а не их тождество.

### 4.5 Alarm Limit ≠ несколько уровней Alarm

Для C.A.R.E. SOURCE прямо устанавливает: **Alarm Limit is Always ONE.**

Это локальное правило C.A.R.E.; не переносим его автоматически на весь GM Alarm framework.

### 4.6 Protection ≠ Effectiveness Verification

Защита заказчика и проверка эффективности process controls — две заявленные функции C.A.R.E.; не смешиваем их в одну без дополнительного SOURCE.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **Protects your customer from non-conforming product, discrepancies and labeling errors.**

> **Verifies that process controls are effective.**

> **The Alarm Limit is Always ONE!**

> **Report Non-Conforming Data to the Fast Response Meeting.**

> **Add the Root Cause/Corrective Action to the Layered Process Audit.** fileciteturn148file0

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
CUSTOMER-RELATED PART CHARACTERISTICS
        ↓
C.A.R.E.
        ↓
REVIEW / EVALUATION
        ↓
PROTECTION OF CUSTOMER
        +
VERIFY PROCESS CONTROL EFFECTIVENESS
        ↓
NON-CONFORMING DATA
        ↓
FAST RESPONSE MEETING
        ↓
ROOT CAUSE / CORRECTIVE ACTION
        ↓
LAYERED PROCESS AUDIT
```

## 7. REL — ОТНОШЕНИЯ

SOURCE поддерживает:

```text
Customer-related items
→ C.A.R.E.
```

```text
C.A.R.E.
→ Process Control Effectiveness Verification
```

```text
C.A.R.E. Non-Conforming Data
→ Fast Response Meeting
```

```text
Root Cause / Corrective Action
→ Layered Process Audit
```

Участие:

```text
Plant Manager + Quality Manager
→ facilitate C.A.R.E. activities
```

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Customer Acceptance Review & Evaluation

**Input:** part-related customer satisfaction items: Pass Through Characteristics, Labeling, Past Formal Customer Issues.

**Transformation:** C.A.R.E. review/evaluation с Alarm Limit = ONE.

**Output:** информация о соответствии / несоответствии и эффективности process controls.

**Организационный эффект:** защита заказчика и передача Non-Conforming Data в Fast Response; Root Cause / Corrective Action связываются с LPA.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — Customer Acceptance Verification

Способность организации проверять customer-related part characteristics и одновременно оценивать эффективность process controls, с заданным механизмом реакции на non-conforming data.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Customer Acceptance Review & Evaluation — воспроизводимая конструкция проверки customer-related characteristics, предназначенная одновременно для защиты заказчика и проверки эффективности process controls, с Alarm Limit = ONE и установленными связями с Fast Response и LPA.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — C.A.R.E. Customer Acceptance Check

```text
INPUT
Customer-related Part Characteristics
(Pass Through / Labeling / Past Formal Issues)
        ↓
[ C.A.R.E. REVIEW / EVALUATION ]
        ↓
ALARM LIMIT = 1
        ↓
OUTPUT
Customer Protection +
Process Control Effectiveness Information
        ↓
IF NON-CONFORMING
        ↓
FAST RESPONSE MEETING
        ↓
ROOT CAUSE / CORRECTIVE ACTION
        ↓
LPA
```

Инженерный тест:

- **INPUT:** определённые customer-related characteristics;
- **OPERATION:** review/evaluation;
- **OUTPUT:** информация о состоянии и эффективности process controls;
- **ORGANIZATIONAL EFFECT:** customer protection и запуск установленного последующего управленческого контура при non-conforming data.

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Оговорка: SOURCE-фрагмент не раскрывает полный operational procedure C.A.R.E.; поэтому машинка признаётся кандидатом на основании явно заданных входа, операции, результата и downstream-связей, но не канонизируется.

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Customer Satisfaction Items
→ C.A.R.E.
→ Review / Evaluation
→ Non-Conforming Data
→ Fast Response Meeting
```

И отдельная связь:

```text
Root Cause / Corrective Action
→ Layered Process Audit
```

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-050 интересна тем, что **внешняя приемлемость заказчика становится объектом встроенной проверки эффективности внутреннего контроля**.

Потенциальная CMOC-конструкция:

```text
CUSTOMER EXPECTATION / CHARACTERISTIC
        ↓
CONTROL CHECK
        ↓
RESULT
        ↓
CUSTOMER PROTECTION
```

При несоответствии:

```text
RESULT
→ NON-CONFORMING DATA
→ FAST RESPONSE
→ ROOT CAUSE / CORRECTIVE ACTION
→ LPA
```

Особенно важное различение:

> **Customer-facing acceptance check может одновременно быть механизмом защиты результата и проверкой способности upstream process controls обеспечивать этот результат.**

Это CMOC INTERPRETATION.

## 15. СВЯЗЬ С GM-043–049

```text
GM-043
Quality Feedback / Feed Forward
→ движение quality information
```

```text
GM-044
Downstream Escape
→ Feedback
```

```text
GM-045
Performance Metrics
→ Effectiveness Check
```

```text
GM-049
Distributed Verification
→ Process Structure
```

```text
GM-050
Customer Acceptance
→ Control Effectiveness
→ Fast Response / LPA
```

Таким образом, C.A.R.E. добавляет **customer-facing контрольную точку** к ранее добытой архитектуре Verification Station.

Эта межвагонеточная связь пока является аналитической интерпретацией, а не канонизированным отношением CMOC.

## 16. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
