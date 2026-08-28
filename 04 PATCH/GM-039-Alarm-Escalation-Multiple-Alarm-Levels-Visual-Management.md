# GM-039 — Alarm & Escalation: Multiple Alarm Levels / Visual Management

**Извещение на изменение:** 0150+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 3.3 — Defects Entering the Station / Alarm and Escalation, pp. 90–91  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

GM показывает пример **Multiple Alarm Levels – Visual Management**.

На предыдущей странице пример Tally Sheet фиксирует количество каждого типа проблемы по часам, показывает Trigger # и предупреждает оператора при достижении Alarm Limit. При этом в примере отдельно указано: **Trigger an Alarm! 2nd Alarm is Escalated!** и **Alarm by shift not hour.** fileciteturn105file0

На следующей странице показан визуальный пример с:

- **Alarm Trigger Collection Point** в конце assembly process;
- отдельным **2nd alarm Trigger**;
- для Assembly type Defects — пример порога второго Alarm = **3 pieces**;
- при достижении этого уровня **VS operator calls for help**. fileciteturn105file6

Это именно пример реализации, а не универсальная численная норма GM.

## 2. LOCATION

**pp. 90–91 — Verification Station / Alarm and Escalation (Example).**

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Multiple Alarm Levels** | несколько уровней Alarm |
| **Visual Management** | визуальное управление |
| **Alarm Trigger** | условие / точка срабатывания Alarm |
| **2nd Alarm Trigger** | условие срабатывания второго Alarm |
| **Collection Point** | точка накопления / сбора |
| **Assembly Process** | процесс сборки |
| **Assembly Type Defect** | дефект типа сборки |
| **VS Operator** | оператор Verification Station |
| **Call for Help** | обращение за помощью |
| **Tally Sheet** | лист подсчёта / tally sheet |
| **Trigger #** | установленный порог срабатывания |
| **Defects by Hour** | количество дефектов по часам |
| **Alarm by Shift** | Alarm по смене |
| **Escalated** | эскалирован |
| **Visual Management** | визуальное управление |
| **Point of Inspection** | место / точка контроля |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### 4.1 Alarm Level ≠ Alarm Limit

Alarm Limit задаёт условие срабатывания. Multiple Alarm Levels задают несколько уровней реакции/эскалации.

### 4.2 First Alarm ≠ Second Alarm

SOURCE явно различает первоначальный Alarm и **2nd Alarm**, который эскалируется.

### 4.3 Trigger ≠ Response

Trigger определяет момент срабатывания. Response — действие после срабатывания.

### 4.4 Visual Management ≠ просто отображение

В SOURCE визуальная конструкция связана с Trigger и Call for Help. Поэтому она поддерживает действие, а не только показывает данные.

### 4.5 Пример «3 pieces» ≠ универсальный норматив

SOURCE маркирует страницу как **Example**. Поэтому число 3 нельзя переносить в CMOC как общий норматив Alarm.

### 4.6 Hourly count ≠ Alarm by hour

Tally Sheet может записывать количество проблем по часам, но SOURCE отдельно указывает **Alarm by shift not hour**. Не смешиваем интервал учёта данных и интервал действия Alarm.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **Multiple Alarm Levels – Visual Management**

> **Trigger an Alarm! 2nd Alarm is Escalated!**

> **2nd alarm Trigger is 3 pieces for Assembly type Defects – VS operator calls for help.**

> **Alarm by shift not hour.** fileciteturn105file0turn105file6

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
DEFECT COUNT / TYPE
        ↓
ALARM TRIGGER
        ↓
1st ALARM
        ↓
CONTINUE TRACKING
        ↓
2nd ALARM TRIGGER
        ↓
ESCALATION
        ↓
VS OPERATOR CALLS FOR HELP
```

Визуальный слой:

```text
TALLY SHEET / VISUAL DISPLAY
        ↓
CURRENT DEFECT COUNT
        ↓
VISIBLE TRIGGER STATUS
        ↓
OPERATOR KNOWS WHEN TO CALL FOR HELP
```

## 7. REL — ОТНОШЕНИЯ

SOURCE поддерживает следующие связи:

```text
Defect Count / Type
→ Alarm Trigger
→ Alarm
```

```text
Alarm
→ Continued Tracking
→ 2nd Alarm Trigger
→ Escalation
```

```text
2nd Alarm
→ VS Operator
→ Call for Help
```

```text
Tally Sheet
→ Defect Count by Hour
→ Alarm Limit Visibility
```

Не утверждаем, что конкретный внешний вид Tally Sheet является обязательной формой для всех производственных участков.

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Multi-Level Alarm Escalation

**Input:** обнаруженные дефекты, их тип и накопленное количество.

**Transformation:** визуально отслеживать накопление и сопоставлять его с последовательными Alarm Triggers.

**Output:** переход от первого Alarm к следующему уровню и, при достижении второго Trigger, escalation / call for help.

**Организационный эффект:** уровень реакции изменяется в зависимости от состояния проблемы.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — Управление уровнями реакции

Способность организации заранее задавать несколько порогов реакции и делать их визуально различимыми, чтобы оператор мог своевременно инициировать следующий уровень помощи.

**STATUS: CANDIDATE / SINGLE-SOURCE**

Это CMOC-интерпретация структуры SOURCE.

## 10. CORE CANDIDATE

> **Multi-Level Alarm Escalation — воспроизводимая конструкция, в которой несколько порогов Alarm визуально связаны с изменением уровня организационной реакции; достижение следующего порога инициирует escalation и обращение за помощью.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Multi-Level Alarm Escalation

```text
INPUT
Defect Type + Defect Count
        ↓
[ TRACK / VISUALIZE ]
        ↓
ALARM TRIGGER #1
        ↓
[ LEVEL 1 RESPONSE ]
        ↓
CONTINUE TRACKING
        ↓
ALARM TRIGGER #2
        ↓
[ ESCALATE ]
        ↓
CALL FOR HELP
        ↓
HIGHER RESPONSE LEVEL
```

Инженерный тест:

- **INPUT:** тип и количество дефектов;
- **OPERATION:** отслеживание и сравнение с последовательными Trigger;
- **OUTPUT:** смена уровня Alarm / escalation;
- **ORGANIZATIONAL EFFECT:** изменение уровня реакции без ожидания полной эскалации с самого начала.

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Важно: конкретное число **3 pieces** из примера не является частью общего определения Machine.

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Defect Count
→ Alarm Trigger
→ 1st Alarm
→ 2nd Alarm Trigger
→ Escalation
→ Call for Help
```

И визуальный контур:

```text
Defect Tally
→ Visible Trigger Status
→ Operator Recognition
→ Call for Help at Escalation Level
```

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-039 добавляет к GM-038 важное различение:

> **Эскалация может быть не бинарным переходом «нет реакции → реакция», а изменением уровня реакции по мере изменения состояния.**

Получается:

```text
STATE
  ↓
LEVEL 1 TRIGGER
  ↓
LEVEL 1 RESPONSE
  ↓
STATE WORSENS / REPEATS
  ↓
LEVEL 2 TRIGGER
  ↓
ESCALATION
  ↓
LEVEL 2 RESPONSE
```

Это потенциально важный CMOC-механизм **ступенчатой реакции**.

И ещё одна добыча:

> **Visual Management здесь является частью механизма распознавания момента перехода между уровнями реакции.**

Но это именно CMOC interpretation: SOURCE показывает конкретный пример визуального управления, а не формулирует универсальную теорию Visual Management.

## 15. ГРАНИЦА С GM-037 / GM-038

**GM-037:** задаёт Alarm Limit как порог срабатывания.

**GM-038:** задаёт Alarm → Response → Escalation → Problem Solving.

**GM-039:** показывает, что между состоянием и Escalation может существовать **несколько уровней Trigger / Response**.

```text
GM-037
Defect → Alarm Limit → Alarm

GM-038
Alarm → Response → Escalation

GM-039
Alarm Level 1 → Response 1
          ↓
Alarm Level 2 → Response 2 / Escalation
```

## 16. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
