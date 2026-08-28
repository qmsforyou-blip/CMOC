# GM-081 — S-4: STANDARDIZE / React to Audit Findings — Countermeasure Sheet

**Извещение на изменение:** 0190+280826  
**Статус:** CANDIDATE / SINGLE-SOURCE  
**Источник:** GM Quality System Basics rev March 2009, pp. 141–142  

---

## 1. SOURCE

После формы **5S Evaluation** SOURCE вводит следующий элемент:

> **React to Audit Findings**

И показывает форму:

> **5-S Work Place Organization Audit Countermeasure Sheet (Continuous Improvement)**

Форма предназначена для фиксации реакции на выявленные в ходе аудита проблемы организации рабочего места и содержит следующие поля:

| Поле SOURCE | Назначение по форме |
|---|---|
| **Item #** | номер пункта / записи |
| **Date** | дата |
| **Location** | место возникновения / обнаружения |
| **Problem Description** | описание проблемы |
| **Owner** | ответственный |
| **Countermeasure** | контрмера |
| **Target Date** | целевая дата |
| **Initials** | инициалы |
| **Complete Date** | дата завершения |

SOURCE явно помечает конструкцию как **Continuous Improvement**.

---

# 2. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **React to Audit Findings** | реагировать на результаты аудита |
| **Audit Finding** | результат / выявление аудита |
| **Countermeasure Sheet** | лист контрмер |
| **Work Place Organization** | организация рабочего места |
| **Continuous Improvement** | непрерывное улучшение |
| **Item #** | номер пункта |
| **Date** | дата |
| **Location** | место |
| **Problem Description** | описание проблемы |
| **Owner** | ответственный |
| **Countermeasure** | контрмера |
| **Target Date** | целевая дата |
| **Initials** | инициалы |
| **Complete Date** | дата завершения |
| **Finding** | выявление / результат аудита |
| **Problem** | проблема |
| **Action** | действие |
| **Completion** | завершение |

---

# 3. DISTINCTIONS — РАЗЛИЧЕНИЯ

## Audit Finding ≠ Countermeasure

Форма разделяет:

```text
PROBLEM DESCRIPTION
        ↓
COUNTERMEASURE
```

Следовательно, описание выявленной проблемы и способ реагирования — разные информационные объекты.

---

## Problem ≠ Owner

Проблема не является ответственным лицом. Форма специально содержит отдельную колонку **Owner**.

---

## Countermeasure ≠ Target Date

Контрмера отвечает на вопрос **что сделать**, а Target Date — **к какой дате это должно быть выполнено**.

---

## Target Date ≠ Complete Date

Это особенно важное различение:

```text
TARGET DATE
→ ожидаемая дата

COMPLETE DATE
→ фактическая дата завершения
```

Форма позволяет зафиксировать обе.

---

## Finding ≠ Closure

Сам факт обнаружения проблемы ещё не означает её устранение. Наличие **Complete Date** показывает, что завершение действия фиксируется отдельно.

Это — CMOC INTERPRETATION, основанная на структуре формы.

---

# 4. EXTRACTION — ИЗВЛЕЧЕНИЕ

SOURCE задаёт следующую структуру записи:

```text
ITEM #
  ↓
DATE
  ↓
LOCATION
  ↓
PROBLEM DESCRIPTION
  ↓
OWNER
  ↓
COUNTERMEASURE
  ↓
TARGET DATE
  ↓
INITIALS
  ↓
COMPLETE DATE
```

Это **структура полей формы**, а не утверждение о причинно-следственной последовательности.

---

# 5. MECHANISM — МЕХАНИЗМ

## CANDIDATE — Audit Finding Response

**Input:** результат аудита / выявленная проблема организации рабочего места.

**Transformation:** фиксация проблемы, ответственного, контрмеры и сроков.

**Output:** зарегистрированная управляемая запись о реакции на finding.

**CANDIDATE / SINGLE-SOURCE**

---

## CANDIDATE — Countermeasure Tracking

Форма позволяет одновременно фиксировать:

```text
WHAT IS WRONG?
→ Problem Description

WHO OWNS IT?
→ Owner

WHAT WILL BE DONE?
→ Countermeasure

BY WHEN?
→ Target Date

WHEN WAS IT COMPLETED?
→ Complete Date
```

Последняя интерпретация вопросами **what / who / what action / when / completion** — CMOC-реконструкция структуры формы.

**CANDIDATE / SINGLE-SOURCE**

---

# 6. CAPABILITY — СПОСОБНОСТИ

### CANDIDATE — Фиксировать реакцию на audit finding

Создавать отдельную запись, связывающую выявленную проблему с дальнейшей реакцией.

### CANDIDATE — Назначать владельца проблемы

Форма содержит отдельное поле **Owner**.

### CANDIDATE — Фиксировать контрмеру

Форма содержит отдельное поле **Countermeasure**.

### CANDIDATE — Задавать целевой срок

Форма содержит **Target Date**.

### CANDIDATE — Фиксировать завершение

Форма содержит **Complete Date**.

---

# 7. MACHINE — МАШИНКА

## **Audit Finding → Countermeasure → Completion**

```text
INPUT
Audit Finding / Problem
        ↓
[ RECORD ]
Problem Description
        ↓
[ ASSIGN ]
Owner
        ↓
[ DEFINE ]
Countermeasure
        ↓
[ SET ]
Target Date
        ↓
[ COMPLETE ]
Complete Date
        ↓
OUTPUT
TRACEABLE COUNTERMEASURE RECORD
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Важная оговорка: SOURCE показывает **форму**, а не пошаговую процедуру её заполнения. Поэтому последовательность выше — инженерная реконструкция по полям формы.

---

# 8. CHAIN — ЦЕПОЧКА

### SOURCE-SUPPORTED STRUCTURE

```text
Location
→ Problem Description
→ Owner
→ Countermeasure
→ Target Date
→ Complete Date
```

Дополнительно форма сохраняет **Item #, Date и Initials**.

---

# 9. КЛЮЧЕВОЕ РАЗЛИЧЕНИЕ GM-080 → GM-081

GM-080:

```text
STANDARDIZED CRITERIA
        ↓
EVALUATION
        ↓
ITEM SCORE 0–5
        ↓
NOTES FOR NEXT LEVEL OF IMPROVEMENT
```

GM-081:

```text
AUDIT FINDING
        ↓
PROBLEM DESCRIPTION
        ↓
OWNER
        ↓
COUNTERMEASURE
        ↓
TARGET DATE
        ↓
COMPLETE DATE
```

Таким образом, SOURCE непосредственно рядом показывает две разные конструкции:

> **оценить состояние** и **реагировать на выявленную проблему**.

Это **CMOC INTERPRETATION / CANDIDATE**.

---

# 10. CMOC INTERPRETATION — ОТ ОЦЕНКИ К ДЕЙСТВИЮ

GM-080 создаёт запись состояния:

```text
STATE
→ SCORE
```

GM-081 создаёт запись реакции:

```text
FINDING
→ COUNTERMEASURE
→ COMPLETION
```

Потенциальный мост:

```text
OBSERVED CONDITION
        ↓
EVALUATION / FINDING
        ↓
ACTION
        ↓
COMPLETION
```

**STATUS: CMOC INTERPRETATION / CANDIDATE / MULTI-SOURCE**

Не канонизировать до подтверждения другими SOURCE.

---

# 11. TARGET DATE / COMPLETE DATE — ОСОБАЯ ДОБЫЧА

Форма не ограничивается вопросом:

> «Что надо сделать?»

Она содержит два временных поля:

```text
TARGET DATE
        ↓
COMPLETE DATE
```

Это позволяет различать **плановую временную границу** и **факт завершения**.

SOURCE не задаёт отдельного поля **Status** и не описывает правило оценки просрочки. Поэтому такие элементы в GM-081 не добавляем.

---

# 12. CORE CANDIDATE

> **Countermeasure Tracking — конструкция управляемого реагирования на выявленную проблему через фиксацию проблемы, ответственного, контрмеры, целевой даты и фактического завершения.**

**CANDIDATE / SINGLE-SOURCE**

---

# 13. СВЯЗЬ С CMOC

Потенциальная конструкция:

```text
REQUIREMENT / STANDARD
        ↓
OBSERVATION
        ↓
FINDING
        ↓
RESPONSIBILITY
        ↓
ACTION
        ↓
TARGET
        ↓
COMPLETION
```

Но только следующие элементы непосредственно поддержаны формой:

```text
Problem Description
Owner
Countermeasure
Target Date
Complete Date
```

Остальные связи — **CMOC INTERPRETATION**.

---

# 14. STATUS

**GM-081 — CANDIDATE / SINGLE-SOURCE**

**Audit Finding Response — CANDIDATE / SINGLE-SOURCE**

**Countermeasure Tracking — CANDIDATE / SINGLE-SOURCE**

**Finding → Action → Completion — CANDIDATE / MULTI-SOURCE**

**CANON — не присваиваем.**

---

## Источник изображения

Страница 142, **React to Audit Findings: (Example)**, форма **5-S Work Place Organization Audit Countermeasure Sheet (Continuous Improvement)**.

