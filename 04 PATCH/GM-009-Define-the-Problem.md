# GM-009 — Step 1: Define the Problem

## Извещение на изменение

**0120+280826**

---

## 0. SOURCE

**Источник:** GM Quality System Basics Overview Supplier Audit.pdf  
**Версия источника:** Quality Systems Basics rev March 2009  
**Раздел:** FAST RESPONSE → 1.3 Problem Solving → Step 1 — DEFINE THE PROBLEM  
**Основной фрагмент:** p. 28; контекст p. 24–27.

SOURCE также фиксирует общее определение Problem как discrepancy between an existing Standard or Expectation and the Actual Situation. fileciteturn87file6

---

## 1. LOCATION

p. 28 — **Problem Description / Step 1-DEFINE THE PROBLEM**.

GM задаёт две связанные операции:

1. **State the Problem That Is Occurring** — описать происходящую проблему.
2. **Problem Definition — Specifically Define the Situation** через три элемента:
   - **The Standard** — What should be happening?
   - **The Actual or Gap** — What is happening?
   - **The Time Period** — How long has it been happening?

fileciteturn87file0

---

## 2. TERMS

- Problem Description
- Problem Definition
- Standard
- Actual
- Gap
- Time Period
- Situation
- Discrepancy
- Existing Standard
- Expectation

---

## 3. DISTINCTIONS

### DIS-GM-009-01

**Problem Description ≠ Problem Definition.**

GM сначала требует state the problem that is occurring, затем — specifically define the situation.

### DIS-GM-009-02

**Standard ≠ Actual / Gap.**

Standard описывает, что должно происходить; Actual / Gap — что происходит.

### DIS-GM-009-03

**Problem Definition включает Time Period.**

Проблема у GM задаётся не только содержанием расхождения, но и временной характеристикой: how long it has been happening.

### DIS-GM-009-04

**Problem ≠ только факт отклонения.**

В предыдущем фрагменте GM определяет Problem как discrepancy между существующим Standard / Expectation и Actual Situation. Следовательно, для дальнейшей работы требуется установить обе стороны сравнения.

fileciteturn87file6

### DIS-GM-009-05

**Definition ≠ Cause.**

В этом шаге GM определяет ситуацию; причинный анализ появляется позже. Это согласуется с фундаментальным принципом: delay cause analysis until there is a thorough grasp of what is actually happening. fileciteturn87file6

---

## 4. GM-FORMULATIONS

> “State the Problem That Is Occurring.”

> “Problem Definition - Specifically Define the Situation.”

> “The Standard - What should be happening?”

> “The Actual or Gap - What is happening?”

> “The Time Period - How long has it been happening?”

fileciteturn87file0

Все приведённые формулировки сохраняются как **SOURCE CLAIMS**.

---

## 5. EXTRACTION

GM превращает исходное «есть проблема» в структурированное описание ситуации:

```text
PROBLEM
  ↓
PROBLEM DESCRIPTION
  ↓
PROBLEM DEFINITION
  ├── STANDARD
  ├── ACTUAL / GAP
  └── TIME PERIOD
```

Это не причинный анализ. Это **фиксация границ и параметров наблюдаемой ситуации до анализа причины**.

---

## 6. NOMENCLATURE

Предварительные кандидаты:

- Problem Description
- Problem Definition
- Standard
- Actual / Gap
- Time Period
- Discrepancy

Не превращаем автоматически каждый термин в Entity.

---

## 7. CLASSIFICATION

```text
PROBLEM SOLVING
│
└── STEP 1 — DEFINE THE PROBLEM
    │
    ├── Problem Description
    │
    └── Problem Definition
        ├── Standard
        ├── Actual / Gap
        └── Time Period
```

Это классификация материала SOURCE, а не каноническая CMOC-классификация.

---

## 8. PASSPORT

### Candidate — Problem Definition

**Type:** CANDIDATE / SINGLE-SOURCE  
**Source role:** способ конкретизации ситуации через Standard, Actual / Gap и Time Period.

### Candidate — Problem Description

**Type:** CANDIDATE / SINGLE-SOURCE  
**Source role:** фиксация того, какая проблема происходит.

---

## 9. RELATIONS

Подтверждённая локальная связь:

```text
Problem
  ↓
Description
  ↓
Definition
  ├── Standard
  ├── Actual / Gap
  └── Time Period
```

И более общая связь из предыдущих страниц:

```text
Existing Standard / Expectation
          ↓
      Discrepancy
          ↑
    Actual Situation
```

fileciteturn87file6

---

## 10. MECHANISM

### CANDIDATE — Problem Definition Mechanism

Источник даёт достаточно материала для осторожного кандидата:

**INPUT:** неструктурированное описание происходящей проблемы.

**OPERATION:** определить Standard, Actual / Gap и Time Period.

**OUTPUT:** конкретно определённая ситуация.

**EFFECT:** последующий Problem Solving получает объект, границы которого заданы до анализа причины.

Это кандидат на механизм, но не утверждение о полном CMOC-механизме.

---

## 11. CAPABILITY

**NONE**

Источник в этом фрагменте не формулирует самостоятельную организационную Capability.

---

## 12. CORE CANDIDATE

### Candidate A — Problem Definition

> **Problem Definition — структурированное определение происходящей ситуации через Standard, Actual / Gap и Time Period до перехода к причинному анализу.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

### Candidate B — Discrepancy

> **Discrepancy — расхождение между существующим Standard / Expectation и Actual Situation.**

Это подтверждает ранее добытый фрагмент, но не является новым только по факту повторного появления.

**STATUS: CONFIRM / UPDATE**, а не NEW.

---

## 13. MACHINE

### CANDIDATE MACHINE — Problem Definition

```text
INPUT
Problem That Is Occurring
        ↓
TRANSFORMATION
Define:
Standard
+
Actual / Gap
+
Time Period
        ↓
OUTPUT
Specifically Defined Situation
        ↓
ORGANIZATIONAL EFFECT
Cause analysis starts from
an explicitly bounded problem
```

Кандидат сильный, но пока **CANDIDATE / SINGLE-SOURCE**.

Важно: GM не говорит здесь, что эта конструкция является “machine”. Это наша CMOC-классификация на основании описанной SOURCE операции.

---

## 14. CHAIN

### SOURCE-SUPPORTED LOCAL CHAIN

```text
Problem Description
      ↓
Problem Definition
      ↓
Standard + Actual / Gap + Time Period
```

Дальнейшее движение к Point of Cause относится уже к следующему материалу и здесь не присоединяется.

---

## 15. STATUS

**CANDIDATE / SINGLE-SOURCE**

### CONFIRM / UPDATE

**UPDATE GM-008:** GM-008 определил Problem Solving как structured process, который идентифицирует, анализирует и устраняет discrepancy между current situation и existing standard / expectation. GM-009 теперь показывает первую конкретную операцию этого процесса — Definition через Standard, Actual / Gap и Time Period. fileciteturn87file6

**CONFIRM ранее добытого:** Discrepancy как расхождение Standard / Expectation и Actual Situation получает прямое повторное подтверждение в рамках Step 1.

Никакого CANON.

---

## 16. CMOC INTERPRETATION

Главная добыча GM-009:

> **До поиска причины проблема должна быть превращена из общего утверждения “что-то не так” в определённую ситуацию с двумя сторонами сравнения — Standard и Actual / Gap — и временной границей.**

Инженерная форма:

```text
WHAT SHOULD HAPPEN?
        ↓
     STANDARD
        │
        │ discrepancy
        ↓
WHAT IS HAPPENING?
        ↓
 ACTUAL / GAP
        │
        + TIME PERIOD
        ↓
DEFINED PROBLEM
```

Это усиливает важное различение CMOC:

**Problem Definition ≠ Cause Analysis.**

GM сначала делает объект анализа определённым; причина появляется позже. fileciteturn87file6

---

## 17. UPDATE FOR FUTURE MULTI-SOURCE CONFIRMATION

Потенциально сильные кандидаты для межисточникового сопоставления:

- Requirement / Standard как основание сравнения;
- Actual / Gap как зафиксированное расхождение;
- Time Period как граница наблюдения;
- Definition до Cause Analysis.

**Не объявлять подтверждением ISO до отдельной межисточниковой проверки.**
