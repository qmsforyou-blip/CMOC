# GM-047 — Problem Tracking / Status Review

**Извещение на изменение:** 0158+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 3.3 — Leadership Support / Daily Management Walk-Through  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

GM включает в еженедельный Team Problem Solving Report Out отдельную проверку:

> **Is the Tracking Report up to date and statused appropriately?**

Эта проверка выполняется вместе с рассмотрением текущего шага Problem Solving, roadblocks, потребности в дополнительных ресурсах и необходимости эскалации Problem Solving Assignment. fileciteturn127file5

В общей схеме Shop Floor Management Tracking R/Y/G указан рядом с еженедельным Team Report Out и Review for roadblocks / problem escalation. fileciteturn125file0

SOURCE, таким образом, поддерживает две характеристики Tracking Report:

1. он должен быть **up to date**;
2. его status должен быть **appropriate**.

## 2. LOCATION

**p. 95 — Daily Management Walk-Through / Leadership Support.**  
Контекст: Weekly Problem Solving — Team Report Out.

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Problem Tracking** | отслеживание проблемы |
| **Tracking Report** | отчёт отслеживания |
| **Status** | статус |
| **Up to Date** | актуальный / обновлённый |
| **Statused Appropriately** | статус установлен надлежащим образом |
| **R/Y/G** | Red / Yellow / Green — красный / жёлтый / зелёный статус |
| **Problem Solving Status** | статус решения проблемы |
| **Current Problem Solving Step** | текущий шаг решения проблемы |
| **Roadblock** | препятствие / блокирующий фактор |
| **Problem Solving Assignment** | поручение по решению проблемы |
| **Escalation** | эскалация |
| **Team Report Out** | отчёт команды |
| **Weekly Review** | еженедельный обзор |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### 4.1 Tracking Report ≠ Report Out

Tracking Report — средство удержания и представления состояния проблемы.

Report Out — событие, на котором это состояние предъявляется и рассматривается.

### 4.2 Status ≠ Activity

Сам факт выполнения действий не заменяет статуса проблемы.

### 4.3 Status ≠ Result

SOURCE не утверждает, что статус равен результату. Статус характеризует состояние работы / проблемы в Tracking.

### 4.4 Up to Date ≠ Appropriately Statused

Это два самостоятельных требования SOURCE:

- информация должна быть актуальной;
- установленный статус должен соответствовать состоянию.

### 4.5 R/Y/G ≠ универсальная семантика

SOURCE показывает R/Y/G как Tracking-инструмент, но в данном фрагменте не задаёт полного универсального определения каждого цвета. Не переносим собственные значения CMOC в SOURCE.

### 4.6 Tracking ≠ Escalation

Tracking обеспечивает видимость состояния. Эскалация — отдельное управленческое действие, необходимость которого рассматривается при Review.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **Is the Tracking Report up to date and statused appropriately?**

> **Tracking R, Y, G Reviewed for roadblocks, problem escalation.**

Первая формулировка прямо устанавливает объект проверки. Вторая показывает связь Tracking со статусами R/Y/G и Review. fileciteturn127file5turn125file0

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
PROBLEM SOLVING
      ↓
CURRENT STATE
      ↓
TRACKING REPORT
      ↓
STATUS R / Y / G
      ↓
WEEKLY REVIEW
      ↓
┌───────────────┬──────────────────┐
↓               ↓                  ↓
ROADBLOCK       RESOURCE NEED      ESCALATION
```

Критерий качества Tracking:

```text
TRACKING REPORT
   ├→ UP TO DATE?
   └→ STATUS APPROPRIATE?
```

## 7. REL — ОТНОШЕНИЯ

```text
Problem Solving
→ Tracking Report
→ Status
→ Weekly Review
```

```text
Tracking Status
→ Roadblock Review
→ Resource / Escalation Decision
```

```text
Current Problem Solving Step
→ Tracking Status
```

Не утверждаем SOURCE-связь Status → конкретное действие без дополнительного доказательства.

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Problem Status Tracking

**Input:** проблема и её текущее состояние в Problem Solving.

**Transformation:** поддержание Tracking Report в актуальном состоянии и присвоение/обновление статуса; последующий Review.

**Output:** видимое актуальное состояние проблемы для управленческого Review.

**Организационный эффект:** руководство и команда могут видеть, где находится работа и требуется ли снятие препятствий, ресурс или эскалация.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — Удержание актуального статуса проблемы

Способность организации поддерживать актуальное состояние Problem Solving в Tracking Report и предъявлять его для регулярного Review.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Problem Status Tracking — воспроизводимая конструкция поддержания актуального статуса незавершённой проблемы в Tracking Report с последующим регулярным Review состояния для выявления roadblocks, потребности в ресурсах и необходимости эскалации.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Problem Status Tracking Machine

```text
INPUT
Problem + Current Problem Solving State
        ↓
[ UPDATE TRACKING REPORT ]
        ↓
[ ASSIGN / UPDATE STATUS ]
        ↓
R / Y / G
        ↓
[ PERIODIC REVIEW ]
        ↓
ROADBLOCK / RESOURCE / ESCALATION NEED
        ↓
MANAGEMENT RESPONSE
```

Инженерный тест:

- **INPUT:** проблема и её текущее состояние;
- **OPERATION:** актуализация Tracking + status + Review;
- **OUTPUT:** актуальное видимое состояние;
- **ORGANIZATIONAL EFFECT:** возможность своевременной управленческой реакции.

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Оговорка: SOURCE подтверждает Tracking + Status + Review, но не раскрывает в данном фрагменте полный формат или все правила перехода R/Y/G. Поэтому машинка зафиксирована на уровне механизма, а не конкретной реализации цветовой шкалы.

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Problem Solving
→ Current Step / State
→ Tracking Report
→ Status R/Y/G
→ Weekly Review
→ Roadblock / Resource / Escalation Review
```

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-047 позволяет отделить **состояние работы** от **самой работы**.

```text
WORK
 ↓
CURRENT STATE
 ↓
STATUS
 ↓
VISIBLE / TRACKABLE STATE
 ↓
REVIEW
 ↓
MANAGEMENT RESPONSE
```

Отсюда кандидат на более общий CMOC-принцип:

> **Управляемой становится не только работа, но и её состояние, если состояние может быть актуально зафиксировано и предъявлено для Review.**

Это CMOC interpretation.

Особенно важна пара:

**UP TO DATE + APPROPRIATELY STATUSed**.

То есть одного наличия записи недостаточно: система требует одновременно **актуальности** и **корректного статуса**. Но критерии «appropriately» SOURCE здесь не раскрывает — их не додумываем.

## 15. ГРАНИЦА С GM-046

**GM-046:** Report Out — регулярное предъявление текущего шага Problem Solving.

**GM-047:** Tracking Report — удержание актуального состояния проблемы между Report Out и к моменту Review.

```text
GM-046
CURRENT WORK
 ↓
REPORT OUT

GM-047
CURRENT WORK
 ↓
TRACKING
 ↓
STATUS
 ↓
REVIEW
```

Следовательно, **Tracking Report не заменяет Report Out**, а обеспечивает ему актуальный объект рассмотрения.

## 16. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
