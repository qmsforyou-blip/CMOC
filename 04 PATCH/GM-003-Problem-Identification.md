# GM-003 — Fast Response: Problem Identification

## Извещение на изменение

**0114+270826**

---

## 0. SOURCE

**Источник:** GM Quality System Basics Overview Supplier Audit.pdf  
**Версия источника:** Quality Systems Basics rev March 2009  
**Диапазон вагонетки:** p. 10, Fast Response — Problem Identification.  
**Режим:** SOURCE → EXTRACTION → DISTINCTIONS → GM → NOMENCLATURE → CLASSIFICATION → PASSPORT → RELATIONS → CANONIZATION → USE → ASSEMBLIES

---

## 1. LOCATION

p. 10 — **Problem Identification**.

GM задаёт правило: в подготовке к Fast Response meeting, в начале дня, Quality должна идентифицировать значимые quality concerns за последние 24 часа.

Источник разделяет их на **External Concerns** и **Internal Concerns**.

External:
- Customer concerns — PRR's, Liaison Issues, Customer Calls, Warranty;
- Supplier concerns — при необходимости supplier заранее уведомляется о report out на meeting.

Internal:
- Verification Station Findings;
- Layered Process Audit Systemic issues;
- Line stops and Teardown issues;
- Other internal Quality concerns — Dock Audits, containment activity;
- Error Proof device failures.

---

## 2. TERMS

- Problem Identification
- Significant Quality Concerns
- External Concerns
- Internal Concerns
- Customer Concerns
- Supplier Concerns
- Verification Station Findings
- Layered Process Audit Systemic Issues
- Line Stops
- Teardown Issues
- Dock Audits
- Containment Activity
- Error Proof Device Failures
- Quality
- Fast Response Meeting
- Past 24 Hours

---

## 3. DISTINCTIONS

### DIS-GM-003-01

Следует различать **External Concerns** и **Internal Concerns**. GM явно разделяет источники значимых quality concerns на две группы.

### DIS-GM-003-02

Следует различать **источник сигнала** и **сам quality concern**. Customer Call, Warranty, Verification Station Finding, LPA systemic issue и Line Stop являются источниками/каналами обнаружения, а не обязательно разными типами проблемы.

### DIS-GM-003-03

Следует различать **внешнее обнаружение** и **внутреннее обнаружение**. GM специально включает внутренние источники, чтобы обнаруживать проблемы до того, как они проявятся у customer.

### DIS-GM-003-04

Следует различать **временной интервал обнаружения** и момент проведения meeting. Quality собирает concerns за предыдущие 24 часа до начала Fast Response meeting.

### DIS-GM-003-05

Следует различать **Problem Identification** и **Problem Solving**. Этот фрагмент задаёт идентификацию/сбор значимых concerns; решение проблемы здесь не описывается.

### DIS-GM-003-06

Следует различать **сигнал от разных организационных контуров** и единый вход Fast Response. Различные каналы — customer, supplier, verification, LPA, line stop, teardown, dock audit, containment, error proofing — сходятся в один процесс подготовки Fast Response meeting.

---

## 4. GM-FORMULATIONS

> “In preparation for the Fast Response meeting, at the start of the day, Quality shall identify significant quality concerns from the past 24 hours.”

> “External Concerns”

> “Internal Concerns”

> “Customer concerns”

> “Supplier concerns”

> “Verification Station Findings”

> “Layered Process Audit Systemic issues”

> “Line stops and Teardown issues”

> “Other internal Quality concerns (Dock Audits, containment activity)”

> “Error Proof device failures”

Все формулировки сохраняются как **SOURCE CLAIMS**.

---

## 5. EXTRACTION

GM фактически задаёт входной фильтр Fast Response:

```text
PAST 24 HOURS
      ↓
QUALITY
      ↓
IDENTIFY SIGNIFICANT QUALITY CONCERNS
      ↓
┌───────────────────────────────┐
│ EXTERNAL       │ INTERNAL     │
│                │              │
│ Customer       │ Verification │
│ Supplier       │ LPA          │
│                │ Line stops   │
│                │ Teardown     │
│                │ Dock audits  │
│                │ Containment  │
│                │ Error Proof  │
└───────────────────────────────┘
      ↓
FAST RESPONSE MEETING
```

Это уже не просто перечень источников. GM устанавливает правило **сведения разнородных сигналов в единый вход Fast Response**.

---

## 6. NOMENCLATURE

Предварительные объекты:

- Problem Identification
- Significant Quality Concern
- External Concern
- Internal Concern
- Quality Concern Source
- Fast Response Input

Пока не объявляются отдельными CMOC Entity или Mechanism.

---

## 7. CLASSIFICATION

Классификация по Источнику:

```text
FAST RESPONSE
└── Problem Identification
    ├── External Concerns
    │   ├── Customer
    │   └── Supplier
    └── Internal Concerns
        ├── Verification Station
        ├── LPA systemic issues
        ├── Line stops
        ├── Teardown
        ├── Dock Audits
        ├── Containment activity
        └── Error Proof failures
```

---

## 8. PASSPORT

### Candidate Entity

**Name:** Fast Response Problem Identification  
**Type:** CANDIDATE / SINGLE-SOURCE  
**Role in source:** входной этап Fast Response, обеспечивающий ежедневное выявление значимых quality concerns за предыдущие 24 часа.

### Source-defined boundary

Начало: **past 24 hours / available quality signals**.  
Операция: **Quality identifies significant quality concerns**.  
Выход: **identified significant quality concerns for Fast Response meeting**.

---

## 9. RELATIONS

Подтверждённая Источником связь:

```text
Customer / Supplier / Internal Quality Sources
                    ↓
             Quality identifies
                    ↓
       Significant Quality Concerns
                    ↓
        Fast Response Meeting
```

Также:

```text
Past 24 hours
      ↓
Problem Identification
      ↓
Fast Response Meeting
```

GM прямо перечисляет внутренние источники, поэтому связь с Verification Station, LPA, Line Stops, Teardown, Dock Audits, Containment и Error Proof failures фиксируется как **source-supported**.

---

## 10. MECHANISM

### CANDIDATE — входной механизм отбора сигналов

На этом фрагменте есть признаки воспроизводимого механизма:

1. задан временной интервал — past 24 hours;
2. задан исполнитель — Quality;
3. задан объект отбора — significant quality concerns;
4. заданы категории источников — external/internal;
5. задан следующий организационный пункт — Fast Response meeting.

Однако сам фрагмент ещё не описывает критерий, по которому Quality определяет **significant** concern. Поэтому механизм классификации значимости пока не выделяется отдельно.

---

## 11. CAPABILITY

**NONE**.

Наличие ежедневной функции идентификации не является достаточным основанием для отдельной CMOC Capability.

---

## 12. CORE CANDIDATE

> **Fast Response Problem Identification — воспроизводимый входной этап, в котором Quality ежедневно сводит значимые внешние и внутренние quality concerns за предыдущие 24 часа в единый набор для Fast Response meeting.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## 13. MACHINE

### CANDIDATE MACHINE — Problem Identification / Signal Aggregation

Предварительная модель:

```text
INPUT
Quality signals from past 24 hours
        ↓
TRANSFORMATION
Collection + identification
+ source separation
+ significance selection
        ↓
OUTPUT
Set of significant Quality Concerns
        ↓
NEXT STATE
Ready for Fast Response Meeting
```

Но есть важное ограничение:

**критерии “significant” в данной вагонетке не раскрыты.** Поэтому пока точнее считать это **CANDIDATE MACHINE**, а не установленной машиной.

---

## 14. CHAIN

### CANDIDATE — подтверждённая часть

```text
Quality signals
 → Problem Identification
 → Significant Quality Concerns
 → Fast Response Meeting
```

Источники сигналов входят в эту цепь через перечисленные GM внешние и внутренние каналы.

Полная цепь Fast Response будет установлена только после обработки следующих вагонеток.

---

## 15. ASSEMBLY — UPDATE

GM-003 усиливает гипотезу, возникшую в GM-002:

```text
SIGNAL SOURCES
      ↓
[PROBLEM IDENTIFICATION]
      ↓
[SIGNIFICANT QUALITY CONCERNS]
      ↓
[TRACKING BOARD / MEETING]
      ↓
[PROBLEM SOLVING]
```

Но это пока **рабочая сборка**, а не CANON.

Особенно важно: GM-003 показывает, что Tracking Board не является единственным входом Fast Response. До неё уже существует отдельная операция **сведения сигналов**.

---

## 16. STATUS

**CANDIDATE / SINGLE-SOURCE**

### CONFIRM / UPDATE

**UPDATE** относительно GM-002: Fast Response Tracking Board получает не произвольные записи, а набор значимых concerns, сформированный Quality из нескольких внешних и внутренних каналов за заданный 24-часовой интервал.

Старые PATCH и CORE не изменяются.

---

## 17. CMOC INTERPRETATION

Главный результат вагонетки:

> **Fast Response начинается раньше Board.**

Board — кандидат на машинку управления уже идентифицированным issue.

GM-003 обнаруживает перед ней ещё одну потенциальную машинку:

> **сведение разнородных сигналов в единый набор значимых quality concerns.**

И это важное архитектурное различение:

```text
ИСТОЧНИК СИГНАЛА
       ↓
[СВЕДЕНИЕ / ОТБОР]
       ↓
ЗНАЧИМЫЙ CONCERN
       ↓
[TRACKING BOARD]
       ↓
УПРАВЛЯЕМЫЙ ISSUE
```

Следующая вагонетка должна проверить, что происходит с этим набором на **Fast Response Meeting** и как GM разводит коммуникацию, ownership и problem solving.
