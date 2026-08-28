# GM-007 — Fast Response: Performance Metrics

## Извещение на изменение

**0118+280826**

---

## 0. SOURCE

**Источник:** GM Quality System Basics Overview Supplier Audit.pdf  
**Версия источника:** Quality Systems Basics rev March 2009  
**Диапазон вагонетки:** Fast Response, Performance Metrics / pp. 20–22  
**Режим:** SOURCE → EXTRACTION → DISTINCTIONS → GM → NOMENCLATURE → CLASSIFICATION → PASSPORT → RELATIONS → MECHANISM → CAPABILITY → CORE CANDIDATE → MACHINE → CHAIN → STATUS → CMOC INTERPRETATION

---

## 1. LOCATION

Ключевой фрагмент — **1.2 Fast Response, Performance Metrics**, pp. 20–22.

GM задаёт вопрос: **“How do you know the Fast Response process is working?”**  
Leadership shall ensure that the Fast Response process is effective and that quality status is displayed.

Для визуального контроля допускается любой тип visual management, например calendar или trend charts, представляющие как минимум monthly data:

- number of days Red or Yellow;
- number of issues Closed;
- average days open for closed issues.

Отдельный пример показывает weekly tracking числа закрытых issues и среднего числа дней открытости закрытых issues. fileciteturn80file4turn79file0

---

## 2. TERMS

- Performance Metrics
- Fast Response process effectiveness
- Quality status
- Visual Management
- Calendar
- Trend Charts
- Monthly data
- Number of days Red or Yellow
- Number of issues Closed
- Average days open for closed issues
- Weekly tracking

---

## 3. DISTINCTIONS

### DIS-GM-007-01

**Process effectiveness ≠ наличие самого Fast Response process.**

GM задаёт отдельный вопрос: как узнать, что процесс работает. Следовательно, наличие процесса само по себе не является доказательством его эффективности.

### DIS-GM-007-02

**Quality status ≠ Performance Metric.**

Quality status должен отображаться, а Performance Metrics используются для оценки работы Fast Response во времени.

### DIS-GM-007-03

**Current status ≠ historical performance.**

R/Y/G показывает состояние; число дней Red/Yellow, число закрытых issues и average days open показывают динамику работы процесса.

### DIS-GM-007-04

**Visual Management ≠ конкретный формат.**

GM не требует единственного вида визуализации. Может использоваться calendar, trend chart или другой тип visual management при сохранении минимально требуемых данных.

### DIS-GM-007-05

**Issues Closed ≠ Average Days Open.**

GM предлагает одновременно отслеживать объём закрытия и длительность открытого состояния закрытых issues. Это разные показатели.

### DIS-GM-007-06

**Monthly tracking ≠ Weekly tracking.**

Для visual management GM требует минимум monthly data, а пример дополнительно показывает weekly tracking.

---

## 4. GM-FORMULATIONS

> “Leadership shall ensure that Fast Response process is effective and quality status is displayed.”

> “How do you know the Fast Response process is working?”

> “Any type of visual management can be used such as a calendar, trend charts which represent at minimum monthly data.”

> “The number of days Red or Yellow.”

> “Number of issues Closed.”

> “Average days open for closed issues.”

Пример GM также показывает weekly tracking этих показателей. fileciteturn80file4turn79file0

Все формулировки сохраняются как **SOURCE CLAIMS**.

---

## 5. EXTRACTION — КОНСТРУКЦИЯ

GM строит контур обратной проверки самого Fast Response:

```text
FAST RESPONSE PROCESS
        ↓
QUALITY STATUS / PROCESS RESULTS
        ↓
VISUAL MANAGEMENT
        ↓
PERFORMANCE METRICS
        ↓
LEADERSHIP CAN SEE
        ↓
IS THE PROCESS WORKING?
```

Минимальный набор данных:

```text
Performance Metrics
├── Days Red / Yellow
├── Issues Closed
└── Average Days Open for Closed Issues
```

Пример временной агрегации:

```text
MONTHLY DATA
      +
WEEKLY TRACKING EXAMPLE
```

---

## 6. NOMENCLATURE

Предварительные объекты:

- Performance Metrics
- Fast Response Effectiveness
- Quality Status Display
- Visual Management
- Days Red / Yellow
- Issues Closed
- Average Days Open
- Trend Chart
- Daily Quality Chart

Не превращаем каждый показатель в отдельную Entity или Machine.

---

## 7. CLASSIFICATION

```text
FAST RESPONSE
│
└── PERFORMANCE METRICS
    │
    ├── Quality Status Display
    ├── Days Red / Yellow
    ├── Issues Closed
    ├── Average Days Open
    └── Visual Management
        ├── Calendar
        └── Trend Charts
```

Это классификация материала GM, не каноническая классификация CMOC.

---

## 8. PASSPORT

### Candidate — Fast Response Performance Measurement

**Name:** Fast Response Performance Metrics  
**Type:** CANDIDATE / SINGLE-SOURCE  
**Source role:** visual measurement of Fast Response process effectiveness.

### Source-defined characteristics

- leadership responsibility for process effectiveness;
- quality status displayed;
- visual management;
- minimum monthly data;
- days Red / Yellow;
- issues closed;
- average days open for closed issues;
- example of weekly tracking.

---

## 9. RELATIONS

Подтверждённая SOURCE конструкция:

```text
Fast Response Process
        ↓
Effectiveness
        ↓
Performance Metrics
        ↓
Visual Management
        ↓
Leadership Review
```

И внутри metrics:

```text
Issues
 ↓
Closed Issues
 ↓
Average Days Open
```

Параллельно:

```text
Status
 ↓
Days Red / Yellow
```

---

## 10. MECHANISM

### CANDIDATE — Performance Measurement / Feedback Mechanism

GM задаёт не только показатели, но и функцию их применения:

1. Fast Response должен быть эффективным;
2. качество и состояние должны быть видимыми;
3. effectiveness проверяется через данные;
4. данные визуализируются во времени;
5. leadership получает возможность увидеть, работает ли процесс.

Таким образом Performance Metrics образуют кандидатный контур **проверки функционирования самого управленческого процесса**.

Но GM в этой вагонетке не описывает отдельную процедуру принятия corrective action по ухудшению metrics. Поэтому дальше не додумываем.

---

## 11. CAPABILITY

**NONE**

Пока не выводим отдельную capability.

---

## 12. CORE CANDIDATE

> **Performance Measurement — воспроизводимая фиксация и визуализация данных о работе Fast Response во времени, позволяющая leadership оценивать эффективность процесса.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

Это CMOC interpretation, а не термин GM как канонический объект CMOC.

---

## 13. MACHINE

### CANDIDATE MACHINE — Performance Measurement

Инженерный тест:

```text
INPUT
Operational data from Fast Response
        ↓
TRANSFORMATION
Aggregate / visualize over time
        ↓
OUTPUT
Days Red/Yellow
+ Issues Closed
+ Average Days Open
        ↓
ORGANIZATIONAL EFFECT
Leadership can evaluate
whether Fast Response is working
```

Это более слабый Machine-кандидат, чем Tracking Board или Statusing, потому что GM здесь не задаёт полной процедуры реакции на результат измерения.

Поэтому:

**MACHINE = CANDIDATE / LOW CONFIDENCE**

---

## 14. CHAIN

### CANDIDATE — partial

```text
Fast Response Activity
 → Performance Data
 → Visual Management
 → Leadership Visibility
 → Effectiveness Assessment
```

Последующий переход от плохого показателя к действию SOURCE в этой вагонетке не задаёт.

---

## 15. ASSEMBLY — UPDATE

GM-007 добавляет к Fast Response контур обратной проверки:

```text
Problem Identification
        ↓
Fast Response Meeting
        ↓
Responsibility Allocation
        ↓
Tracking Board
        ↓
Exit Criteria / Statusing
        ↓
Problem Solving
        ↓
Evidence / Validation
        ↓
Leadership Approval
        ↓
Green / Closure
        ↓
Performance Metrics
        ↓
Leadership sees whether process works
```

Это **CANDIDATE ASSEMBLY**, а не Source-defined единая Chain.

---

## 16. STATUS

**CANDIDATE / SINGLE-SOURCE**

### CONFIRM / UPDATE

**UPDATE GM-006:**

GM-006 показал status как состояние отдельного item и Overall Status. GM-007 добавляет другой уровень наблюдения: **метрики процесса во времени**.

```text
Item Status
    ≠
Process Performance
```

**UPDATE GM-002:**

Tracking Board отображает состояние отдельных issues; Performance Metrics позволяют увидеть, как работает весь Fast Response process.

Это различение важно для CMOC: **контроль объекта ≠ контроль эффективности механизма, который этот объект обслуживает.**

Никакого CANON.

---

## 17. CMOC INTERPRETATION

Главная добыча GM-007:

> **Управленческий механизм должен иметь не только внутренний контур управления объектами, но и внешний контур наблюдения за тем, работает ли сам механизм.**

В GM это выражено очень просто:

```text
PROCESS
   ↓
RESULT / STATUS
   ↓
METRICS
   ↓
VISUALIZATION
   ↓
LEADERSHIP
   ↓
“IS THE PROCESS WORKING?”
```

И здесь появляется важное архитектурное различение:

```text
[ISSUE CONTROL]
      ≠
[PROCESS PERFORMANCE CONTROL]
```

Первый контур управляет конкретными проблемами.
Второй позволяет руководству увидеть, насколько работает сам Fast Response.

**Performance Measurement остаётся CANDIDATE / SINGLE-SOURCE.**

---

## SOURCE REFERENCE

Источник: `GM Quality System Basics Overview Supplier Audit.pdf` в File Library; Fast Response → Performance Metrics, pp. 20–22.
