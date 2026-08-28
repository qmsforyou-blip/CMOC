# GM-045 — Performance Metrics

**Извещение на изменение:** 0156+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 3.4 — Defects Leaving the Station / Performance Metrics  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

GM определяет **Check** в Implementing a Verification Station как измерение effectiveness и получение результатов.

Для этого предлагается простой line graph, показывающий количество **red days** для каждого upstream customer, а также отслеживание внутренних метрик, включая:

- scrap;
- direct run;
- internal ppm;
- efficiency;
- uptime.

Таким образом, Performance Metrics используются для проверки того, что Verification Station работает, и для наблюдения результатов её работы. fileciteturn121file0

В более раннем описании VS SOURCE дополнительно указывает, что performance tracked based on internal metrics, discrepancies identified for correction, data drives teams in Problem Solving with Leadership Support, а VS calibrated by downstream data. fileciteturn121file5

## 2. LOCATION

**p. 100 — Performance Metrics, 3.4 Defects Leaving the Station.**

Связанный SOURCE-фрагмент: **p. 80 — Description, Roles & Responsibility.**

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Performance Metrics** | показатели результативности / эффективности |
| **Check** | проверка |
| **Effectiveness** | результативность |
| **Results** | результаты |
| **Line Graph** | линейный график |
| **Red Days** | дни с красным статусом |
| **Upstream Customer** | предшествующий потребитель / процесс |
| **Scrap** | списание / брак |
| **Direct Run** | прямой выпуск / проход без дополнительной обработки |
| **Internal PPM** | внутренний PPM, количество дефектов на миллион |
| **Efficiency** | эффективность |
| **Uptime** | время доступности / безотказной работы |
| **Internal Metrics** | внутренние показатели |
| **Discrepancy** | несоответствие / расхождение |
| **Downstream Data** | данные последующего процесса |
| **Calibrated by Downstream Data** | калибруется / проверяется по данным downstream |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### 4.1 Metric ≠ Result

Metric — средство измерения/представления. Result — наблюдаемое состояние/результат процесса.

### 4.2 Measurement ≠ Effectiveness

SOURCE говорит, что Check состоит в measuring effectiveness and seeing results. Само измерение не тождественно результативности.

### 4.3 Internal Metric ≠ Downstream Data

SOURCE различает внутренние метрики и downstream data как источники проверки работы VS.

### 4.4 Red Day ≠ конкретный дефект

Red Day — агрегированный показатель состояния/результата. Не превращаем его автоматически в отдельную сущность дефекта.

### 4.5 Metric ≠ Decision

SOURCE этого фрагмента говорит об измерении и проверке, но не устанавливает здесь полного механизма принятия решения по каждому показателю.

### 4.6 Performance Tracking ≠ Problem Solving

Данные могут drive teams in Problem Solving, но tracking performance и Problem Solving — разные конструкции.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **The check portion of Implementing a Verification Station is measuring the effectiveness and seeing results.**

> **Performance is tracked based on internal metrics.**

> **Verifies that the Verification Station is working.**

> **VS is calibrated by “downstream” data.** fileciteturn121file0turn121file5

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
VERIFICATION STATION
        ↓
MEASURE EFFECTIVENESS
        ↓
SEE RESULTS
        ↓
PERFORMANCE METRICS
        ↓
┌───────────────────────────────────────┐
│ Red Days                              │
│ Scrap                                 │
│ Direct Run                            │
│ Internal PPM                          │
│ Efficiency                            │
│ Uptime                                │
└───────────────────────────────────────┘
        ↓
CHECK IF VS IS WORKING
```

Отдельный feedback-контур:

```text
DOWNSTREAM DATA
      ↓
CHECK / CALIBRATE VS
      ↓
DISCREPANCY
      ↓
CORRECTION / PROBLEM SOLVING
```

Последняя часть связывает GM-045 с ранее добытым SOURCE p.80, но не расширяет p.100 сверх того, что там сказано.

## 7. REL — ОТНОШЕНИЯ

```text
Verification Station
→ Performance Metrics
→ Effectiveness / Results
```

```text
Performance Metrics
→ Verify VS is Working
```

```text
Downstream Data
→ VS Calibration / Verification
```

```text
Discrepancy
→ Correction
```

```text
Data
→ Problem Solving Team
```

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Verification Station Performance Check

**Input:** результаты работы VS и измеряемые внутренние показатели.

**Transformation:** измерение и представление performance metrics.

**Output:** информация о результативности и состоянии работы VS.

**Организационный эффект:** появляется возможность проверить, выполняет ли Verification Station свою функцию и увидеть результаты.

**STATUS: CANDIDATE / SINGLE-SOURCE**

Важно: в этой вагонетке SOURCE не даёт полного правила принятия решения по каждому значению метрики. Поэтому механизм не расширяем до «метрика → обязательное решение».

## 9. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — Проверка результативности VS

Способность организации измерять результативность Verification Station через внутренние показатели и видеть результаты её работы.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Verification Station Performance Check — воспроизводимая конструкция проверки результативности Verification Station посредством измерения effectiveness и отслеживания внутренних performance metrics, включая scrap, direct run, internal ppm, efficiency и uptime, с использованием red days как визуального представления результата для upstream customers.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Performance Check Machine

```text
INPUT
VS Results / Internal Performance Data
        ↓
[ MEASURE / TRACK ]
        ↓
PERFORMANCE METRICS
        ↓
[ REVIEW ]
        ↓
OUTPUT
Visibility of VS Effectiveness
        ↓
EFFECT
Verification that VS is working
```

Инженерный тест:

- **INPUT:** результаты и performance data;
- **OPERATION:** measurement / tracking;
- **OUTPUT:** показатели и визуальное представление результата;
- **ORGANIZATIONAL EFFECT:** возможность проверить работу VS.

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Однако не считаем каждую метрику отдельной машинкой.

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
VS
→ Measure Effectiveness
→ Performance Metrics
→ See Results
→ Verify VS is Working
```

Связанный downstream-контур:

```text
Downstream Data
→ VS Calibration
→ Discrepancy Identification
→ Correction / Problem Solving
```

Вторая цепь опирается на связанный SOURCE p.80 и не приписывается исключительно странице Performance Metrics.

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-045 даёт важное различение:

> **Контроль должен иметь собственную проверку результативности.**

Получается:

```text
CONTROL / VERIFICATION
        ↓
MEASURE
        ↓
RESULT
        ↓
CHECK WHETHER CONTROL WORKS
```

Особенно интересна связка с downstream data:

```text
UPSTREAM CONTROL
      ↓
CLAIMED PERFORMANCE
      ↓
DOWNSTREAM REALITY
      ↓
DATA
      ↓
VERIFY / CALIBRATE CONTROL
```

Это потенциально важный CMOC-механизм **внешней проверки эффективности контроля**.

Но SOURCE не даёт здесь универсальной формулы «внешние данные всегда выше внутренних». Поэтому такого вывода не делаем.

## 15. ГРАНИЦА С GM-044

**GM-044** показывает, как downstream escape становится feedback.

**GM-045** показывает, как измерения и downstream data используются для проверки того, что сама Verification Station работает.

```text
GM-044
ESCAPE
→ DOWNSTREAM DETECTION
→ FEEDBACK

GM-045
PERFORMANCE DATA
→ EFFECTIVENESS CHECK
→ VERIFY VS
```

Таким образом, feedback от downstream — не только сообщение о конкретном дефекте, но потенциальный источник проверки эффективности upstream-контроля.

## 16. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
