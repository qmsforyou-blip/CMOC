# GM-059 — 5S Workplace Organization: Seiri / Organization

**Извещение на изменение:** 0170+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 5 S Workplace Organization  
**Шаг:** 1 — Seiri / Organization  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

GM определяет первый шаг 5S — **Seiri / Organization** — как:

> Determine the purpose of the area and remove all unnecessary items from the workplace.

Назначение шага:

> To prepare the workplace for the next 4 steps and to eliminate items that could cause injury, excessive cost, or any of the forms of wastes.

SOURCE также показывает, что в QSB используются несколько терминологических соответствий для этого шага: Organization / Sift / Tidiness / Clear / Sort. fileciteturn173file0

## 2. LOCATION

**p. 130 — 5 S Workplace Organization.**

Шаг 1 из пяти: **Seiri**.

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Seiri** | сортировка / организация |
| **Organization** | организация |
| **Sift** | отбор / просеивание |
| **Tidiness** | аккуратность |
| **Clear** | освобождение / очистка пространства |
| **Sort** | сортировка |
| **Purpose of the Area** | назначение рабочей зоны |
| **Unnecessary Items** | ненужные предметы |
| **Workplace** | рабочее место |
| **Next 4 Steps** | следующие 4 шага |
| **Injury** | травма |
| **Excessive Cost** | чрезмерные затраты |
| **Waste** | потери |
| **Forms of Waste** | виды потерь |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### Purpose of Area ≠ Items in Area

SOURCE сначала требует определить назначение зоны, а затем удалить unnecessary items. Следовательно, необходимость предмета определяется относительно назначения зоны.

### Required ≠ Unnecessary

Seiri не означает удалить всё. Удаляются именно **unnecessary items**.

### Removal ≠ Organization of Remaining Items

Seiri удаляет ненужное. Следующий шаг Seiton уже отвечает за определение лучшего места для required items. Не смешиваем их.

### Seiri ≠ весь 5S

Seiri — только первый шаг из пяти.

### Waste Elimination ≠ только удаление предметов

SOURCE связывает Seiri с устранением items, способных вызвать injury, excessive cost или формы waste. Но не утверждает, что все виды waste устраняются непосредственно этим шагом.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **Determine the purpose of the area and remove all unnecessary items from the workplace.**

> **To prepare the workplace for the next 4 steps and to eliminate items that could cause injury, excessive cost, or any of the forms of wastes.** fileciteturn173file0

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
WORKPLACE
    ↓
DETERMINE PURPOSE OF AREA
    ↓
IDENTIFY UNNECESSARY ITEMS
    ↓
REMOVE UNNECESSARY ITEMS
    ↓
PREPARE WORKPLACE
FOR NEXT 4 STEPS
```

И SOURCE указывает ожидаемый эффект:

```text
UNNECESSARY ITEMS
    ↓
INJURY / EXCESSIVE COST / WASTE RISK
    ↓
ELIMINATION
```

## 7. REL — ОТНОШЕНИЯ

```text
Area Purpose
→ determines relevance of items
```

```text
Seiri
→ Remove Unnecessary Items
→ Prepare Workplace for next 4S
```

```text
Unnecessary Items
→ Injury / Excessive Cost / Waste Risk
```

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Seiri / Unnecessary Item Removal

**Input:** рабочая зона + её назначение + находящиеся в ней предметы.

**Transformation:** определение ненужных предметов относительно назначения зоны и их удаление.

**Output:** рабочая зона, освобождённая от ненужных предметов.

**Организационный эффект:** подготовка зоны к следующим четырём шагам 5S и устранение источников injury, excessive cost и waste.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — Отделять необходимое от ненужного относительно назначения зоны

Способность организации определять, какие предметы необходимы для данной зоны, а какие являются unnecessary.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Освобождать рабочую зону от ненужных предметов

Способность систематически удалять unnecessary items после определения назначения зоны.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Purpose-Based Workplace Sorting — конструкция определения назначения рабочей зоны и удаления из неё предметов, не необходимых для этого назначения, как подготовки среды к дальнейшей организации и снижения источников injury, excessive cost и waste.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Seiri Sorting / Removal

```text
INPUT
Workplace
+ Purpose of Area
+ Items Present
        ↓
[ CLASSIFY ITEMS BY NECESSITY ]
        ↓
REQUIRED / UNNECESSARY
        ↓
[ REMOVE UNNECESSARY ITEMS ]
        ↓
OUTPUT
Cleared Workplace
        ↓
EFFECT
Prepared Workplace
+ Reduced Sources of Injury / Cost / Waste
```

Инженерный тест:

- **INPUT:** рабочая зона, её назначение и находящиеся предметы;
- **OPERATION:** определить необходимость относительно назначения и удалить unnecessary items;
- **OUTPUT:** зона без ненужных предметов;
- **ORGANIZATIONAL EFFECT:** подготовка к следующим 4S и снижение источников потерь/рисков.

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Это более сильный Machine-кандидат, чем GM-058: SOURCE явно задаёт вход, операцию и изменение состояния рабочего места.

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Purpose of Area
→ Identify Unnecessary Items
→ Remove Unnecessary Items
→ Prepare Workplace for Next 4S
```

### SOURCE-SUPPORTED EFFECT

```text
Unnecessary Items
→ Injury / Excessive Cost / Waste
→ Elimination through Seiri
```

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

CANON не присваивается.

## 14. CMOC INTERPRETATION

Здесь появляется очень сильное различение:

> **Необходимость объекта не является абсолютным свойством самого объекта; она определяется относительно назначения зоны.**

Это **CMOC INTERPRETATION**, а не прямой SOURCE claim.

Из него следует потенциальная инженерная конструкция:

```text
PURPOSE
   ↓
CRITERION OF NECESSITY
   ↓
ITEM CLASSIFICATION
   ↓
REMOVAL
```

То есть Seiri фактически использует **назначение как критерий принятия решения о составе рабочей среды**.

Это важно для CMOC, потому что здесь появляется связка:

**PURPOSE → CRITERION → DECISION → STATE CHANGE.**

Пока — только **CANDIDATE / SINGLE-SOURCE**.

## 15. ГРАНИЦА С GM-060

Seiri заканчивается удалением ненужного.

Следующий шаг **Seiton / Neatness** отвечает уже за:

> Identify the best location for all required items in the workplace.

Поэтому не переносим в GM-059 задачу размещения оставшихся предметов.

## 16. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
