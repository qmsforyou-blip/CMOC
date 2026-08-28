# GM-071 — S-4: STANDARDIZE / Visual Controls & Problem Identification

**Извещение на изменение:** 0180+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 5 S Workplace Organization / S-4: STANDARDIZE  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

SOURCE в продолжении S-4 требует:

> **Define a simple method to identify problems using visual controls.**

В том же блоке указано, что cleaning schedule and methods должны быть определены, а cabinet organization — стандартизирована. Пример показывает визуально обозначенные места предметов. fileciteturn192file0

На странице 133 SOURCE формулирует общий результат S-3:

> **Out-of-standard conditions can be easily identified and corrected.** fileciteturn192file6

Важно: GM-071 фиксирует именно **visual identification of problems**. Сама корректировка в формулировке S-4 не является частью отдельной операции этой вагонетки.

## 2. LOCATION

**p. 135 — S-4: STANDARDIZE (CONTINUED).**

Контекст:

```text
VISUAL STANDARDIZATION
→ IDENTIFIED LOCATIONS
→ VISUAL CONTROLS
→ SIMPLE PROBLEM IDENTIFICATION
```

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Visual Control** | визуальный контроль |
| **Visual Controls** | визуальные средства контроля |
| **Identify Problems** | выявлять / идентифицировать проблемы |
| **Simple Method** | простой способ |
| **Problem Identification** | идентификация проблемы |
| **Out-of-Standard Condition** | состояние вне стандарта |
| **Standard Condition** | стандартное состояние |
| **Current Condition** | текущее состояние |
| **Visual Standardization** | визуальная стандартизация |
| **Location Identification** | идентификация места |
| **Standardize** | стандартизировать |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### Visual Control ≠ Visual Standardization

Visual Standardization задаёт визуальное представление стандарта. Visual Control используется для идентификации проблем.

### Identify ≠ Correct

SOURCE в S-4 говорит об идентификации проблем. Она не задаёт здесь операцию correction.

### Problem ≠ Out-of-Standard Condition

На p.133 SOURCE связывает out-of-standard conditions с возможностью их identification and correction. В GM-071 не утверждаем, что всякая визуально обнаруженная проблема обязательно является именно out-of-standard condition.

### Simple Method ≠ Trivial Method

Simple означает простоту способа идентификации; не делаем вывод, что проблема сама по себе проста.

### Visual Control ≠ Measurement

SOURCE не требует числового измерения. Визуальный контроль может быть визуальным признаком/правилом идентификации.

### Identification ≠ Diagnosis

Обнаружить наличие проблемы не означает определить её причину.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **Define a simple method to identify problems using visual controls.** fileciteturn192file0

Контекст SOURCE:

> **Out-of-standard conditions can be easily identified and corrected.** fileciteturn192file6

Вторая формулировка относится к общему результату S-3 и не переносится как полная формулировка GM-071.

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

SOURCE задаёт:

```text
VISUAL CONTROLS
        ↓
SIMPLE METHOD
        ↓
IDENTIFY PROBLEMS
```

CMOC-реконструкция возможного операционного смысла:

```text
CURRENT CONDITION
        ↓
[ VISUAL CONTROL ]
        ↓
IDENTIFIABLE DIFFERENCE / PROBLEM
```

Последняя схема — **CMOC INTERPRETATION**, а не буквальная SOURCE Chain.

## 7. REL — ОТНОШЕНИЯ

SOURCE поддерживает:

```text
Visual Controls
→ Simple Method
→ Problem Identification
```

Также SOURCE в более широком контексте связывает:

```text
Out-of-Standard Conditions
→ Identification
→ Correction
```

Но последняя связь относится к общему S-3 результату; correction не включается в Machine GM-071.

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Visual Problem Identification

**Input:** наблюдаемое состояние рабочего места/объекта.

**Transformation:** применение простого визуального способа контроля.

**Output:** проблема становится идентифицируемой.

**Организационный эффект:** наличие проблемы может быть распознано посредством визуального контроля.

**STATUS: CANDIDATE / SINGLE-SOURCE**

Важно: SOURCE не определяет конкретный алгоритм построения visual control и не задаёт критерий для каждой разновидности проблемы.

## 9. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — Делать проблемы визуально идентифицируемыми

Способность определить простой visual-control method, позволяющий распознавать проблемы.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Встраивать идентификацию проблемы в физическую среду

Способность использовать визуальные средства как часть организационной среды, а не только как отдельный документ.

**STATUS: CANDIDATE / CMOC INTERPRETATION**

## 10. CORE CANDIDATE

> **Visual Problem Identification — конструкция, в которой простой визуальный контроль превращает наличие проблемы в непосредственно идентифицируемое состояние.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Visual Problem Identification

```text
INPUT
Current Workplace / Object Condition
        ↓
[ APPLY VISUAL CONTROL ]
        ↓
[ SIMPLE IDENTIFICATION METHOD ]
        ↓
OUTPUT
PROBLEM IDENTIFIED
        ↓
EFFECT
PROBLEM BECOMES RECOGNIZABLE
```

**MACHINE = CANDIDATE / SINGLE-SOURCE — STRONG**

Инженерный тест:

- **INPUT:** текущее состояние;
- **OPERATION:** visual control + identification method;
- **OUTPUT:** идентифицированная проблема;
- **EFFECT:** проблема становится распознаваемой.

Но не добавляем:

```text
PROBLEM IDENTIFIED
→ ROOT CAUSE
→ CORRECTION
```

Этого в данной SOURCE-формулировке нет.

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Visual Controls
→ Simple Method
→ Identify Problems
```

### CONTEXT-SUPPORTED, NOT GM-071 CORE

```text
Out-of-Standard Condition
→ Identified
→ Corrected
```

Эта вторая цепочка дана SOURCE в контексте S-3. fileciteturn192file6

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

Visual Problem Identification Machine — **CANDIDATE / SINGLE-SOURCE — STRONG**.

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-068:

```text
LOCATION
→ VISUAL IDENTIFICATION
```

GM-069:

```text
VISUAL CONTROL
→ PROBLEM IDENTIFICATION
```

GM-071 позволяет сделать более строгий переход:

```text
STANDARD / EXPECTED ORGANIZATION
        ↓
VISUAL CONTROL
        ↓
OBSERVABLE PROBLEM
```

Но только первые две части непосредственно поддержаны SOURCE. Связь с Standard/Expected State — **CMOC INTERPRETATION**.

### Ключевое различение

> **Визуальный контроль не обязательно управляет состоянием непосредственно; его первой функцией может быть превращение проблемы из скрытой в идентифицируемую.**

Это **CMOC INTERPRETATION**.

Отсюда потенциальная универсальная конструкция:

```text
HIDDEN CONDITION
        ↓
VISUAL CONTROL
        ↓
VISIBLE / IDENTIFIABLE CONDITION
```

Статус: **CANDIDATE / CMOC INTERPRETATION**.

## 15. СВЯЗЬ С GM-070

GM-070:

```text
ORGANIZATIONAL CATEGORY
→ PHYSICAL CODE
→ VISIBLE CATEGORY
```

GM-071:

```text
VISUAL CONTROL
→ PROBLEM IDENTIFICATION
```

Таким образом, визуальное кодирование может выполнять по меньшей мере две разные функции:

```text
1. IDENTIFY THE EXPECTED / DESIGNATED ORGANIZATION

2. IDENTIFY A PROBLEM
```

Это различение важно: **Visual Management ≠ одна функция.**

## 16. СВЯЗЬ С CMOC: ОБЪЕКТ ПРЕОБРАЗОВАНИЯ

В GM-064 объектом преобразования частично было состояние знания:

```text
UNKNOWN
→ VISIBLE CATEGORY
```

В GM-071:

```text
UNIDENTIFIED PROBLEM
→ IDENTIFIED PROBLEM
```

Поэтому обе конструкции можно рассматривать как кандидаты на один класс:

> **Knowledge-State Transformation — изменение доступности знания о состоянии объекта через физический/визуальный носитель.**

**STATUS: CANDIDATE / CMOC INTERPRETATION**

Не CANON.

## 17. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
