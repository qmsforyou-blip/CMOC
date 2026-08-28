# GM-048 — Problem Report Out / Status Tracking

**Извещение на изменение:** 0159+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 3.3 — Leadership Support / Daily Management Walk-Through  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

На форме Leadership Support / Daily Management Walk-Through после блока **Weekly Problem Solving-Team Report Out** SOURCE содержит отдельный элемент:

**PROBLEM REPORT OUT — DAY**

Он расположен в непосредственной связи с еженедельным Team Problem Solving Report Out. На этом Review команда представляет текущий шаг Problem Solving, руководство рассматривает roadblocks и дополнительные ресурсы, проверяет актуальность и корректность статуса Tracking Report и определяет необходимость эскалации Problem Solving Assignment. fileciteturn133file0

SOURCE также прямо устанавливает:

> **Problems shall be tracked and the status reviewed weekly.** fileciteturn129file0

Таким образом, в данном фрагменте SOURCE подтверждает не только наличие Problem Report Out, но и его включённость в регулярный weekly status review.

## 2. LOCATION

**p. 95 — Leadership Support / Daily Management Walk-Through.**  
Контекст: Weekly Problem Solving — Team Report Out.

Визуальная форма обозначена как **PROBLEM REPORT OUT / DAY**. Полный набор полей формы в текстовой экстракции SOURCE не раскрывается; поэтому отсутствующие поля не реконструируются.

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Problem Report Out** | представление / отчёт по проблеме |
| **Day** | день |
| **Problem Tracking** | отслеживание проблемы |
| **Status Review** | рассмотрение статуса |
| **Tracking Report** | отчёт отслеживания |
| **Problem Status** | статус проблемы |
| **Weekly Review** | еженедельный обзор |
| **Current Problem Solving Step** | текущий шаг решения проблемы |
| **Team Report Out** | отчёт команды |
| **Roadblock** | препятствие / блокирующий фактор |
| **Resource** | ресурс |
| **Problem Solving Assignment** | поручение по решению проблемы |
| **Escalation** | эскалация |
| **Up to Date** | актуальный |
| **Statused Appropriately** | статус установлен надлежащим образом |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### 4.1 Problem Report Out ≠ Tracking Report

Problem Report Out — событие / форма предъявления проблемы.

Tracking Report — средство удержания и отображения текущего состояния.

### 4.2 Report Out ≠ Problem Solving

Report Out предъявляет текущее состояние работы.

Problem Solving изменяет понимание и/или состояние проблемы посредством соответствующих шагов решения.

### 4.3 Status Review ≠ Status Assignment

SOURCE говорит, что статус должен быть reviewed weekly и что Tracking Report должен быть up to date and statused appropriately. Это не даёт оснований приписывать Review право автоматически изменять статус.

### 4.4 Weekly Review ≠ Weekly Completion

Еженедельный Review не означает, что проблема должна быть решена за неделю. SOURCE прямо говорит о текущем Problem Solving Step.

### 4.5 Problem Report Out ≠ Final Result

Команда докладывает по текущему шагу. Следовательно, Report Out может происходить до завершения Problem Solving.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **PROBLEM REPORT OUT — DAY**

> **Team member reports out to current problem solving step.**

> **Is the Tracking Report up to date and statused appropriately?**

> **Problems shall be tracked and the status reviewed weekly.** fileciteturn133file0turn129file0

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
PROBLEM
   ↓
CURRENT PROBLEM SOLVING STEP
   ↓
PROBLEM REPORT OUT
   ↓
TRACKING REPORT / STATUS
   ↓
WEEKLY REVIEW
   ↓
ROADBLOCK / RESOURCE / ESCALATION REVIEW
```

Отдельно фиксируется временной признак:

```text
PROBLEM
   ↓
TRACKED
   ↓
STATUS REVIEWED
   ↓
WEEKLY CYCLE
```

## 7. REL — ОТНОШЕНИЯ

SOURCE поддерживает:

```text
Problem Solving
→ Current Step
→ Problem Report Out
```

```text
Problem Report Out
→ Tracking Report
→ Status Review
```

```text
Status Review
→ Roadblock Review
→ Resource Need
→ Escalation Decision
```

Не утверждаем конкретную последовательность изменения R/Y/G: в данном фрагменте она не раскрыта.

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Weekly Problem Status Review

**Input:** проблема, текущий шаг Problem Solving и её Tracking Report.

**Transformation:** регулярное предъявление текущего состояния и его Review.

**Output:** проверенное состояние Tracking; выявленные roadblocks, потребности в ресурсах или необходимость эскалации.

**Организационный эффект:** незавершённая проблема остаётся объектом регулярного управленческого внимания.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — Регулярное удержание проблемы в поле управления

Способность организации сохранять незавершённую проблему в Tracking, регулярно предъявлять её текущее состояние и проверять, требуется ли поддержка, ресурс или эскалация.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Weekly Problem Status Review — воспроизводимая организационная конструкция, в которой текущее состояние незавершённой проблемы регулярно предъявляется и проверяется вместе с актуальностью Tracking Report, препятствиями, потребностью в ресурсах и возможностью эскалации.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Weekly Problem Status Review

```text
INPUT
Problem + Current Step + Tracking State
        ↓
[ WEEKLY PROBLEM REPORT OUT ]
        ↓
[ STATUS REVIEW ]
        ↓
ROADBLOCK / RESOURCE / ESCALATION NEED
        ↓
[ MANAGEMENT RESPONSE ]
        ↓
UPDATED PROBLEM STATE
        ↓
NEXT WEEKLY REVIEW
```

Инженерный тест:

- **INPUT:** проблема и её текущее состояние;
- **OPERATION:** Report Out + Status Review;
- **OUTPUT:** проверенное / актуализированное состояние и выявленная потребность в управленческом действии;
- **ORGANIZATIONAL EFFECT:** непрерывность управления незавершённой проблемой во времени.

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Важно: сама надпись **PROBLEM REPORT OUT — DAY** не является машинкой. Машинкой является воспроизводимый контур **предъявление → Review → реакция → следующий цикл**.

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Problem
→ Current Problem Solving Step
→ Problem Report Out
→ Tracking Report / Status Review
→ Roadblock / Resource / Escalation Review
→ Next Review
```

И временной контур:

```text
Problem
→ Tracking
→ Weekly Status Review
→ Updated State
→ Next Weekly Review
```

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-048 усиливает GM-047, но не заменяет её.

GM-047 дала различение:

```text
TRACKING
→ STATUS
→ REVIEW
```

GM-048 показывает, **как это состояние предъявляется в регулярном управленческом цикле**:

```text
CURRENT WORK
→ REPORT OUT
→ STATUS REVIEW
→ MANAGEMENT RESPONSE
→ NEXT REVIEW
```

Поэтому появляется потенциально более общий CMOC-механизм:

> **Состояние незавершённой работы должно не только существовать в записи, но и периодически предъявляться для управленческого Review.**

Это CMOC INTERPRETATION.

SOURCE не утверждает, что любой статусный Review автоматически является управлением; он лишь задаёт конкретную конструкцию для Problem Solving.

## 15. ГРАНИЦА С GM-046 / GM-047 / GM-042

```text
GM-042
ASSIGNMENT
→ CAPTURE
→ NEXT MEETING
```

```text
GM-046
CURRENT PROBLEM SOLVING STEP
→ REPORT OUT
```

```text
GM-047
TRACKING
→ STATUS
→ WEEKLY REVIEW
```

```text
GM-048
PROBLEM REPORT OUT
→ STATUS REVIEW
→ ROADBLOCK / RESOURCE / ESCALATION
→ NEXT CYCLE
```

GM-048 поэтому не создаёт ещё одну независимую сущность рядом с GM-047. Она **связывает предъявление текущей работы с Review её tracked status**.

## 16. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
