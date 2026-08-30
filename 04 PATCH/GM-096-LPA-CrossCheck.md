# GM-096 — LPA Cross-Check

## Извещение на изменение

**0121+300826**

---

## 0. SOURCE

**Источник:** GM Quality System Basics rev. March 2009  
**Basis:** `GM-096-Machine-Candidates.md` + `GM-096-Machine-Candidate-CrossCheck.md` + LPA extraction in `LAB-003` / `REG-001`.

**Status:** SOURCE-DERIVED / CROSS-CHECK / NON-CANON

---

## 1. OBJECT OF CHECK

**Layered / Repeated Verification (LPA)**

GM LPA представляет собой повторяющуюся проверку процесса, выполняемую на нескольких уровнях ответственности, с заданными вопросами, частотой, фиксацией отклонений и последующим действием.

В текущем Machine Candidate cross-check LPA получил статус:

> **HOLD / POSSIBLE EXISTING AUDIT FAMILY**

Причина: механизм может быть специализированной реализацией более общего `Audit` / `Process Verification`.

---

## 2. WHAT IS ACTUALLY DISTINCTIVE

LPA нельзя свести просто к факту проведения аудита.

Его отличительные признаки образуют дополнительную архитектуру поверх проверки:

```text
AUDIT / PROCESS VERIFICATION
        ↓
LAYERING
        ↓
DEFINED FREQUENCY
        ↓
RISK-BASED QUESTIONS
        ↓
DEVIATION RECORD
        ↓
COUNTERMEASURE / FOLLOW-UP
        ↓
ESCALATION / MANAGEMENT REVIEW
```

Следовательно:

**LPA ≠ Audit Event**

и одновременно:

**LPA ≠ доказанно отдельная Top-Level Machine.**

---

## 3. CROSS-CHECK AGAINST EXISTING CMOC ARCHITECTURE

В текущем каталоге уже существует:

- `Audit` — MACHINE / VERIFICATION / STRONG CANDIDATE;
- `Kamishibai` — System Machine, composing `Audit`;
- `Process Verification` — umbrella mechanism, не отдельная Machine.

Следовательно, создание отдельной Machine `LPA` прямо сейчас создаёт риск дублирования.

---

## 4. ARCHITECTURAL HYPOTHESIS

Рабочая гипотеза:

```text
AUDIT
  +
LAYERING
  +
FREQUENCY
  +
RISK SELECTION
  +
ACTION / ESCALATION
        ↓
LPA
```

То есть LPA может быть не новой базовой Machine, а **специализированной System Machine / Assembly**, использующей общий Audit-механизм.

---

## 5. IMPORTANT DISTINCTIONS

Из материала LPA подтверждаются или усиливаются следующие различения:

### D-01

**Audit ≠ LPA**

LPA добавляет к самой проверке архитектуру уровней, частоты, вопросов и последующего действия.

### D-02

**Detection ≠ Control**

Обнаруженное при LPA отклонение не является автоматически устранённым отклонением; предусмотрен переход к countermeasure / follow-up.

### D-03

**Audit Event ≠ Verification System**

Разовая проверка и организованная повторяющаяся система проверок имеют разный архитектурный масштаб.

### D-04

**Finding ≠ Closure**

Факт обнаружения отклонения не является доказательством его устранения.

---

## 6. MACHINE TEST

### Input

Процесс / операция / контрольный объект, подлежащий регулярной проверке.

### Transformation

Проверка по заданным вопросам на определённом уровне и с установленной периодичностью.

### Output

Результат проверки и, при необходимости, зарегистрированное отклонение с последующим действием.

### Evidence

Audit / LPA record, deviation record, countermeasure / follow-up evidence.

### Acceptance / Closure

Не только выполнение проверки, но и предусмотренное закрытие выявленного отклонения.

### Verdict

Граница операционной последовательности достаточно сильна для Machine-подобной конструкции, однако пока не доказано, что эта конструкция должна существовать в CMOC как отдельная Top-Level Machine.

---

## 7. CURRENT CMOC STATUS

**LPA = STRONG SPECIALIZED CANDIDATE / AUDIT FAMILY**

Не создавать отдельную Top-Level Machine.

Не изменять Canon.

Не изменять `REG-001`.

Не дублировать `Audit`.

---

## 8. NEXT ARCHITECTURAL CHECK

Перед возможной канонизацией необходимо сравнить на уровне механизма:

```text
Audit
Process Verification
LPA
Kamishibai
```

Проверяем:

- Input;
- Trigger;
- Frequency;
- Selection logic;
- Layer / Role;
- Verification operation;
- Output;
- Deviation handling;
- Escalation;
- Closure condition.

Цель проверки — определить, является ли LPA:

1. специализированной реализацией `Audit`;
2. System Machine, composing `Audit`;
3. самостоятельной Machine.

Пока наиболее вероятен вариант **№2**.

---

## 9. NON-DUPLICATION RULE

Наличие в новом источнике названия или описания LPA не является основанием для создания новой Machine.

Если LPA использует тот же базовый механизм проверки, что и существующий `Audit`, GM должен быть связан с `Audit` как дополнительная provenance, а отличительные элементы LPA должны быть представлены отдельными Mechanisms / Relations / Assembly.

---

## 10. FINAL WORKING VERDICT

> **Layered / Repeated Verification (LPA) — специализированная архитектура повторяющейся проверки процесса с уровнями ответственности, частотой, риск-ориентированным содержанием, фиксацией отклонений и последующим действием; на текущем этапе не выделяется в отдельную Top-Level Machine и рассматривается как кандидат System Machine / Assembly семейства Audit.**

**STATUS: HOLD / SPECIALIZED AUDIT FAMILY / NON-CANON**

---

**REG-001:** unchanged.  
**Canon:** unchanged.  
**Existing Machine files:** unchanged.
