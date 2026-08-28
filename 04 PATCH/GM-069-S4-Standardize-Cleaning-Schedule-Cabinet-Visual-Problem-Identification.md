# GM-069 — S-4: STANDARDIZE / Cleaning Schedule, Cabinet Organization & Visual Problem Identification

**Извещение на изменение:** 0178+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 5 S Workplace Organization / S-4: STANDARDIZE (continued), p.135  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

SOURCE продолжает S-4: STANDARDIZE тремя требованиями:

- **Determine cleaning schedule and methods.**
- **Standardize cabinet organization.**
- **Define a simple method to identify problems using visual controls.**

На примере той же страницы показано, что locations items должны быть properly identified. fileciteturn190file0

Контекст предыдущей страницы S-4: область стандартизируется визуально, locations предметов маркируются, используются color coding, area shapes, consistent label height/color и practices для storage containers/storage areas. fileciteturn190file6

## 2. LOCATION

**p. 135 — S-4: STANDARDIZE (CONTINUED).**

Это продолжение GM-068. В данной вагонетке выделены три конструкции: стандартизация очистки, стандартизация организации шкафов и простой визуальный способ идентификации проблем.

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **S-4: STANDARDIZE** | S-4: стандартизация |
| **Cleaning Schedule** | график / расписание очистки |
| **Cleaning Method** | метод очистки |
| **Determine** | определить |
| **Standardize** | стандартизировать |
| **Cabinet Organization** | организация шкафов |
| **Cabinet** | шкаф |
| **Visual Control** | визуальный контроль |
| **Identify Problems** | идентифицировать / выявлять проблемы |
| **Simple Method** | простой способ / метод |
| **Item Location** | место расположения предмета |
| **Properly Identified** | надлежащим образом обозначенный |
| **Storage Practice** | практика хранения |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### Cleaning Method ≠ Cleaning Schedule

Method отвечает на вопрос **как очищать**, Schedule — **когда / с какой заданной периодичностью выполнять очистку**.

### Cleaning Schedule ≠ Cleaning Frequency

GM-067 задавала cleaning frequency как элемент инструкции S-3. GM-069 использует отдельную конструкцию **schedule** в рамках S-4. Не утверждаем их тождество без дополнительного SOURCE.

### Standardize Cabinet Organization ≠ Store Items

SOURCE требует стандартизировать именно организацию шкафа, а не просто разместить предметы.

### Visual Control ≠ Problem Solving

Visual control используется для **identify problems**. SOURCE не утверждает, что visual control сам решает проблему.

### Identify Problem ≠ Correct Problem

На этой странице SOURCE говорит об идентификации проблем, но не описывает здесь corrective action.

### Simple Method ≠ Simple Problem

"Simple" относится к способу идентификации проблемы, а не к самой проблеме.

### Visual Identification ≠ Visual Decoration

Визуальный элемент имеет функциональное назначение: сделать проблему идентифицируемой.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **Determine cleaning schedule and methods.**

> **Standardize cabinet organization.**

> **Define a simple method to identify problems using visual controls.** fileciteturn190file0

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

Три самостоятельные конструкции SOURCE:

```text
CLEANING
   ↓
SCHEDULE + METHODS
```

```text
CABINET
   ↓
STANDARDIZE ORGANIZATION
```

```text
VISUAL CONTROL
   ↓
SIMPLE IDENTIFICATION METHOD
   ↓
PROBLEM IDENTIFIED
```

SOURCE не задаёт единой последовательности между этими тремя конструкциями.

## 7. REL — ОТНОШЕНИЯ

SOURCE поддерживает:

```text
Cleaning
→ Schedule + Methods
```

```text
Cabinet
→ Organization
→ Standardization
```

```text
Visual Controls
→ Problem Identification
```

```text
Item Location
→ Proper Identification
```

Не добавляем автоматически:

```text
Problem Identification
→ Problem Solving
```

поскольку в этом фрагменте такая связь не заявлена.

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Cleaning Schedule & Method Definition

**Input:** cleaning operation / workplace.

**Transformation:** определение schedule и methods.

**Output:** заданная организационная конструкция выполнения очистки.

**Эффект:** очистка получает определённые временные и операционные параметры.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Cabinet Organization Standardization

**Input:** cabinet + размещаемые в нём items.

**Transformation:** стандартизация организации шкафа.

**Output:** стандартизированная организация cabinet.

**Эффект:** способ организации шкафа становится единообразным и воспроизводимым.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Visual Problem Identification

**Input:** рабочая зона + потенциальное problem state.

**Transformation:** применение simple visual-control method.

**Output:** problem становится визуально идентифицируемой.

**Эффект:** проблема обнаруживается через визуальный контроль.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТИ

### CANDIDATE — Задавать расписание и метод очистки

Способность определить cleaning schedule и methods.

**CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Стандартизировать организацию шкафа

Способность задать единый способ организации cabinet.

**CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Делать проблемы визуально идентифицируемыми

Способность определить простой visual-control method для идентификации проблем.

**CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Visual Problem Identification — организационная конструкция, в которой простой визуальный контрольный способ делает наличие проблемы непосредственно идентифицируемым.**

**CANDIDATE / SINGLE-SOURCE**

Дополнительные кандидаты:

> **Cleaning Schedule & Method Definition — конструкция определения расписания и методов очистки.**

> **Cabinet Organization Standardization — конструкция стандартизации организации шкафа.**

Оба — **CANDIDATE / SINGLE-SOURCE**.

## 11. MACHINE — МАШИНКИ

### MACHINE 1 — Visual Problem Identification

```text
INPUT
Workplace State
+
Potential Problem
        ↓
[ VISUAL CONTROL ]
        ↓
[ SIMPLE IDENTIFICATION METHOD ]
        ↓
OUTPUT
Problem Identified
        ↓
ORGANIZATIONAL EFFECT
Problem Becomes
Visible / Recognizable
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Это наиболее сильная машинка GM-069: SOURCE явно связывает visual controls с операцией identify problems.

Важно: **следующая операция correction в этой Machine не включается**, потому что SOURCE здесь говорит об идентификации, а не о решении.

### MACHINE 2 — Cleaning Schedule & Method Definition

```text
INPUT
Cleaning Need
        ↓
[ DETERMINE SCHEDULE ]
+
[ DETERMINE METHODS ]
        ↓
OUTPUT
Defined Cleaning Arrangement
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

### MACHINE 3 — Cabinet Organization Standardization

```text
INPUT
Cabinet + Items
        ↓
[ STANDARDIZE ORGANIZATION ]
        ↓
OUTPUT
Standardized Cabinet Organization
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

SOURCE не раскрывает конкретный алгоритм стандартизации шкафа, поэтому Machine остаётся Candidate.

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Cleaning
→ Schedule + Methods
```

### SOURCE-SUPPORTED

```text
Cabinet
→ Standardize Organization
```

### SOURCE-SUPPORTED

```text
Visual Controls
→ Simple Method
→ Identify Problems
```

Последняя цепочка особенно важна: здесь SOURCE непосредственно задаёт переход от **visual control** к **problem identification**. fileciteturn190file0

Но:

```text
Problem Identified
→ Corrected
```

для этой вагонетки SOURCE не подтверждает.

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

Visual Problem Identification — **CANDIDATE / SINGLE-SOURCE — STRONG**.

Cleaning Schedule & Method Definition — **CANDIDATE / SINGLE-SOURCE**.

Cabinet Organization Standardization — **CANDIDATE / SINGLE-SOURCE**.

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-068 показала:

```text
LOCATION
→ VISUAL IDENTIFICATION
```

GM-069 делает следующий шаг:

```text
VISUAL CONTROL
→ PROBLEM IDENTIFICATION
```

То есть визуальный носитель может выполнять не только функцию **показа ожидаемого состояния**, но и функцию **выявления отклонения от ожидаемого состояния**.

Это важное CMOC-различение:

```text
VISUAL STANDARD
→ EXPECTED STATE
```

и:

```text
VISUAL CONTROL
→ IDENTIFIABLE PROBLEM
```

Они связаны, но не тождественны.

Это **CMOC INTERPRETATION**, не SOURCE claim.

### Потенциальная конструкция контура

```text
EXPECTED STATE
      ↓
VISUAL REPRESENTATION
      ↓
CURRENT STATE
      ↓
COMPARISON / RECOGNITION
      ↓
PROBLEM IDENTIFIED
```

Однако SOURCE этой вагонетки **не описывает явно операцию comparison**. Поэтому не регистрируем её как SOURCE Chain или Machine.

## 15. СВЯЗЬ С GM-067

GM-067:

```text
CLEANING
→ METHOD + FREQUENCY
→ RESOURCES
```

GM-069:

```text
CLEANING
→ SCHEDULE + METHODS
```

Это не повод автоматически объединять записи: S-3 и S-4 имеют разный контекст.

Пока сохраняем обе конструкции независимо.

## 16. СВЯЗЬ С GM-068

GM-068:

```text
AREA
→ VISUAL STANDARDIZATION
→ IDENTIFIED LOCATION
```

GM-069:

```text
VISUAL CONTROL
→ PROBLEM IDENTIFICATION
```

Предварительная CMOC-последовательность:

```text
STANDARD
→ VISUAL REPRESENTATION
→ OBSERVABLE STATE
→ PROBLEM IDENTIFICATION
```

**CANDIDATE / SINGLE-SOURCE + CMOC INTERPRETATION.**

Не CANON.

## 17. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
