# GM-073 — S-4: STANDARDIZE / Floor Marking Color Semantics

**Извещение на изменение:** 0182+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** S-4: STANDARDIZE / GMPT FLOOR MARKING COLOR SPEC.  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

SOURCE вводит **GMPT FLOOR MARKING COLOR SPEC.** — таблицу, связывающую цвет напольной разметки с организационной категорией предметов/материалов.

По структуре таблицы:

| Color | Organizational category — English | Русский |
|---|---|---|
| **BLUE** | **QUALITY** | качество |
| **GREEN** | **PRODUCTIVE MATERIAL** | производственный материал |
| **RED** | **SCRAP MATERIAL** | материал scrap / отходы |
| **YELLOW** | **TOOLING AND SUSPECT MATERIAL** | оснастка и подозрительный материал |
| **WHITE** | **ALL OTHER ITEMS** | все остальные предметы |

SOURCE дополнительно перечисляет примеры внутри категорий: quality items включают operation gage tables/carts, quality information displays и last checked/display parts; productive material — raw stock/purchased parts, in-process material, finished material; scrap — scrap bins/carts; yellow — tool carts, tool tables, suspect material; white — trash bins, housekeeping stations и all other items. fileciteturn201file0

## 2. LOCATION

**p. 136 — S-4: STANDARDIZE (continued).**

Это продолжение GM-070/GM-072: после общего принципа визуального кодирования и конкретного способа нанесения разметки SOURCE задаёт семантическое соответствие цветов и организационных категорий.

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Color Specification** | спецификация цветов |
| **Floor Marking Color Specification** | спецификация цветов напольной разметки |
| **Quality** | качество |
| **Quality Items** | объекты / предметы, связанные с качеством |
| **Productive Material** | производственный материал |
| **Raw Stock** | исходный материал / заготовка |
| **Purchased Parts** | покупные детали |
| **In-Process Material** | материал в процессе производства |
| **Finished Material** | готовый материал / готовая продукция |
| **Scrap Material** | scrap-материал / отходы |
| **Scrap Bin** | контейнер для scrap |
| **Scrap Cart** | тележка для scrap |
| **Tooling** | оснастка |
| **Suspect Material** | подозрительный материал |
| **Trash Bin** | контейнер для мусора |
| **Housekeeping Station** | пост / место housekeeping |
| **All Other Items** | все остальные предметы |
| **Color Code** | цветовой код |
| **Organizational Category** | организационная категория |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### Color ≠ Category

Цвет является кодом; организационная категория является тем, что кодируется.

### Category ≠ State

QUALITY, PRODUCTIVE MATERIAL и HOUSEKEEPING STATION не являются одним типом сущности. Поэтому не называем всю таблицу «кодированием состояния» без уточнения.

### Green Productive Material ≠ Green Conforming Product

В данном SOURCE Green относится к **Productive Material**. Не переносим сюда значение Green из раздела Control of Nonconforming Product, где Green имеет другое значение. fileciteturn198file10

### Yellow Tooling/Suspect ≠ Yellow Suspect Product

В данном SOURCE Yellow объединяет **Tooling and Suspect Material**. Это не то же самое, что Yellow = Suspect Product в containment. fileciteturn198file10

### Red Scrap ≠ Red Nonconforming Product

В данном SOURCE Red кодирует **Scrap Material**. В containment Red кодирует nonconforming product. Значение цвета определяется конкретной спецификацией/контекстом.

### White ≠ absence of coding

White — отдельная категория **All Other Items**, а не отсутствие цветового кода.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **GMPT FLOOR MARKING COLOR SPEC.**

> **BLUE — QUALITY**

> **GREEN — PRODUCTIVE MATERIAL**

> **RED — SCRAP MATERIAL**

> **YELLOW — TOOLING AND SUSPECT MATERIAL**

> **WHITE — ALL OTHER ITEMS** fileciteturn201file0

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
ORGANIZATIONAL CATEGORY
        ↓
SELECT STANDARD COLOR CODE
        ↓
BLUE / GREEN / RED / YELLOW / WHITE
        ↓
PHYSICAL SPACE / ITEM
        ↓
VISIBLE CATEGORY
```

Для SOURCE-таблицы:

```text
BLUE   → QUALITY
GREEN  → PRODUCTIVE MATERIAL
RED    → SCRAP MATERIAL
YELLOW → TOOLING + SUSPECT MATERIAL
WHITE  → ALL OTHER ITEMS
```

## 7. REL — ОТНОШЕНИЯ

```text
BLUE → Quality
```

```text
GREEN → Productive Material
```

```text
RED → Scrap Material
```

```text
YELLOW → Tooling + Suspect Material
```

```text
WHITE → All Other Items
```

Иерархия примеров SOURCE:

```text
QUALITY
→ Gage Tables / Gage Carts
→ Quality Information Displays
→ Last Checked / Display Parts
```

```text
PRODUCTIVE MATERIAL
→ Raw Stock / Purchased Parts
→ In-Process Material
→ Finished Material
```

```text
SCRAP MATERIAL
→ Scrap Bins
→ Scrap Carts
```

```text
TOOLING + SUSPECT MATERIAL
→ Tool Carts
→ Tool Tables
→ Suspect Material
```

```text
ALL OTHER ITEMS
→ Trash Bins
→ Housekeeping Stations
→ All Other Items
```

fileciteturn201file6

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Standard Color-to-Category Coding

**Input:** организационная категория + физический объект/зона.

**Transformation:** выбор цвета согласно установленной SOURCE specification.

**Output:** объект/зона получает стандартизированный цветовой код.

**Эффект:** организационная категория становится визуально распознаваемой.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Context-Bound Color Semantics

**Input:** цветовой код + конкретная organizational specification.

**Transformation:** интерпретация цвета в пределах данной спецификации.

**Output:** определённое значение цвета в конкретном контексте.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТИ

### CANDIDATE — Кодировать организационные категории единым цветовым словарём

Способность связывать заданные категории пространства/предметов с установленными цветами.

### CANDIDATE — Распознавать категорию по физическому коду

Способность интерпретировать физическую разметку как организационную информацию.

## 10. CORE CANDIDATE

> **Context-Bound Color Coding — конструкция, в которой стандартизированный цвет физического пространства или предмета является носителем определённой организационной категории в пределах конкретной системы кодирования.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Organizational Category → Physical Color Code

```text
INPUT
Organizational Category
+
Physical Area / Item
        ↓
[ APPLY STANDARD COLOR CODE ]
        ↓
BLUE / GREEN / RED / YELLOW / WHITE
        ↓
OUTPUT
Physically Coded Area / Item
        ↓
EFFECT
Organizational Category
Becomes Visually Recognizable
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Organizational Category
→ Standard Color
→ Physical Coding
```

### SOURCE-SUPPORTED

```text
Color
→ Category
→ Visual Recognition
```

Последняя стрелка — функциональная интерпретация, а не буквальная формулировка SOURCE.

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

Color-to-Category Coding Machine — **CANDIDATE / SINGLE-SOURCE**.

Context-Bound Color Semantics — **CANDIDATE / SINGLE-SOURCE**.

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-070 дала общий принцип:

```text
ORGANIZATIONAL CATEGORY
→ PHYSICAL CODE
```

GM-072 дала физические носители:

```text
FLOOR
SIGN
LABEL
SILHOUETTE
```

GM-073 добавляет **семантический словарь кода**:

```text
PHYSICAL COLOR
→ ORGANIZATIONAL CATEGORY
```

Отсюда сильная CMOC-гипотеза:

> **Физический носитель становится элементом организационной информационной системы, когда его форма или цвет имеют установленное и воспроизводимое значение.**

Это **CMOC INTERPRETATION**, не SOURCE claim.

## 15. КЛЮЧЕВАЯ ЗАЩИТА ОТ ОШИБОЧНОГО ОБОБЩЕНИЯ

Один и тот же цвет может иметь разные значения в разных SOURCE-конструкциях.

Например:

```text
S-4 FLOOR MARKING
GREEN → PRODUCTIVE MATERIAL
```

а в Control of Nonconforming Product:

```text
GREEN → AFTER BREAKPOINT CONFORMING PRODUCT
```

fileciteturn198file10

Следовательно, CMOC не должен фиксировать:

```text
GREEN = GOOD
```

а должен фиксировать:

```text
COLOR
+
CONTEXT / SPECIFICATION
→
MEANING
```

Это особенно важное различение.

## 16. СВЯЗЬ С GM-071

GM-071:

```text
VISUAL CONTROL
→ IDENTIFY PROBLEM
```

GM-073:

```text
STANDARD COLOR CODE
→ ORGANIZATIONAL CATEGORY
```

Таким образом, визуальный контроль может опираться не просто на наличие визуального признака, а на **предварительно стандартизированную семантику признака**.

## 17. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
