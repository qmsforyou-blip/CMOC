# GM-037 — Alarm Limits

**Извещение на изменение:** 0148+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 3.4 — Alarm and Escalation  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

GM задаёт Alarm Limits в зависимости от типа и количества обнаруженных дефектов. Для разных категорий дефектов могут применяться разные уровни Alarm. Отдельно выделяются PR&R-type defects и high-frequency / low-severity defects.

Для ранее выявленных customer defects GM устанавливает Alarm = 1. Для high-frequency / low-severity дефектов при установлении порога учитывается ability to detect. GM рекомендует сохранять небольшое количество уровней Alarm и группировать их так, чтобы было ясно, когда требуется call for help.

Alarm Limits могут изменяться или уменьшаться после намеренного постоянного изменения процесса через Problem Solving / Continuous Improvement либо при special cause variation, которая не устранена и эскалирована через Problem Solving.

Цель для всех Alarm — 1; GM одновременно подчёркивает: **No Alarms = No Improvement**. Слишком высокий Alarm Limit увеличивает риск Escape.

## 2. LOCATION

**pp. 85–86 — 3.4 Alarm and Escalation.**

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Alarm Limit** | порог срабатывания сигнала |
| **Alarm Level** | уровень срабатывания сигнала |
| **Type of Defect** | тип дефекта |
| **Number of Defects** | количество дефектов |
| **PR&R Type Defect** | дефект типа PR&R |
| **High Frequency / Low Severity Defect** | высокочастотный / низкосерьёзный дефект |
| **Past Customer Defect** | ранее выявленный дефект у заказчика |
| **Ability to Detect** | способность обнаруживать |
| **Need** | необходимость |
| **Process** | процесс |
| **Situation** | ситуация |
| **Call for Help** | обращение за помощью |
| **Escape** | выход дефекта за пределы контролируемого процесса |
| **No Alarms = No Improvement** | отсутствие сигналов не означает отсутствия необходимости улучшения |
| **Goal for all Alarms is 1** | целевой уровень для всех Alarm — 1 |
| **Problem Solving** | решение проблем |
| **Continuous Improvement** | непрерывное улучшение |
| **Special Cause Variation** | вариация по специальной причине |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### 4.1 Alarm ≠ Alarm Limit

Alarm — возникший сигнал. Alarm Limit — условие/порог, при достижении которого возникает Alarm.

### 4.2 Alarm Limit ≠ Product Acceptance Limit

SOURCE связывает Alarm Limit с необходимостью реакции системы. Это не следует автоматически трактовать как предел приемки продукта.

### 4.3 Alarm ≠ Escape

Alarm возникает внутри контролируемого процесса. Escape — выход дефекта за пределы такого контроля. Слишком высокий Alarm Limit повышает риск Escape.

### 4.4 Alarm Limit зависит от контекста

Тип дефекта, его количество, ability to detect, need, process и situation влияют на установление уровня.

### 4.5 Alarm ≠ Escalation

Alarm является сигналом. Дальнейшая escalation раскрывается SOURCE в отдельной конструкции.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **Alarm Limits are based on the type and number of defect found.**

> **The Goal for all alarms is ‘1’.**

> **No Alarms = No Improvement.**

> **High Alarm Limits increase the risk of Escape.**

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
DEFECT DETECTED
       ↓
TYPE + NUMBER
       +
PROCESS / SITUATION / NEED
       ↓
ALARM LIMIT
       ↓
COMPARE ACTUAL WITH LIMIT
       ↓
LIMIT REACHED?
    ↙       ↘
  NO         YES
  ↓           ↓
CONTINUE    ALARM
```

После изменения процесса:

```text
PROCESS CHANGE / CI / PROBLEM SOLVING
              ↓
        REVIEW ALARM LIMIT
              ↓
       CHANGE / REDUCE LIMIT
```

## 7. REL — ОТНОШЕНИЯ

```text
Defect Type + Defect Number
        ↓
Alarm Limit
        ↓
Alarm / No Alarm
```

```text
Process Change / CI / Problem Solving
        ↓
Alarm Limit Review
        ↓
Change / Reduction of Limit
```

```text
High Alarm Limit
        ↓
Higher Escape Risk
```

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Alarm Threshold Control

**Input:** обнаруживаемые дефекты, их тип и количество, а также релевантный контекст процесса.

**Transformation:** установление и применение Alarm Limit.

**Output:** состояние Alarm / No Alarm при сравнении фактического обнаружения с порогом.

**Организационный эффект:** система получает формализованную границу, переводящую значимое отклонение в сигнал для дальнейшей реакции.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — Управление порогом реакции

Способность организации устанавливать, применять и при необходимости пересматривать порог Alarm в зависимости от типа/количества дефектов и условий процесса.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Alarm Threshold Control — воспроизводимый механизм установления и применения порога Alarm в зависимости от типа и количества обнаруженных дефектов и контекста процесса, обеспечивающий переход от обнаруженного отклонения к сигналу для реакции и допускающий пересмотр порога после изменения процесса.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Alarm Threshold Machine

```text
INPUT
Defect Type + Defect Count + Context
        ↓
[ APPLY ALARM LIMIT ]
        ↓
ACTUAL COUNT ↔ THRESHOLD
        ↓
LIMIT REACHED?
    ↙          ↘
  NO            YES
  ↓              ↓
CONTINUE       ALARM
                 ↓
          CALL FOR HELP /
          FURTHER RESPONSE
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Defect
 ↓
Type + Number
 ↓
Alarm Limit
 ↓
Limit Reached
 ↓
Alarm
```

```text
Process Change
 ↓
Problem Solving / Continuous Improvement
 ↓
Alarm Limit Review
 ↓
Change / Reduction of Limit
```

Не объединяем Alarm с последующей escalation до отдельной добычи соответствующего SOURCE-фрагмента.

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

## 14. CMOC INTERPRETATION

Alarm Limit можно рассматривать как потенциальный **механизм перехода от состояния к управленческому событию**:

```text
DEFECT
  ↓
DETECTION
  ↓
TYPE / COUNT
  ↓
THRESHOLD
  ↓
SIGNAL
  ↓
REACTION
```

Это CMOC-интерпретация, а не терминология GM.

Важное различение: **порог реакции системы не равен автоматически пределу соответствия продукта**.

## 15. ГРАНИЦА С GM-036

GM-036 фиксирует первичную конструкцию **Check → Defect → Alarm**. GM-037 раскрывает, что между Defect и Alarm может находиться управляемый **Alarm Limit**, зависящий от типа/количества дефектов и контекста.

## 16. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
