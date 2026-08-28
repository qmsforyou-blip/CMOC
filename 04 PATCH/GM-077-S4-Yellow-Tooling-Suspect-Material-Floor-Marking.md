# GM-077 — S-4: STANDARDIZE / YELLOW — TOOLING & SUSPECT MATERIAL

**Извещение на изменение:** 0186+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** S-4: STANDARDIZE / GMPT FLOOR MARKING COLOR SPEC.  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

В таблице **GMPT FLOOR MARKING COLOR SPEC.** цвет **YELLOW** соответствует категории:

> **TOOLING AND SUSPECT MATERIAL**

В качестве Floor Marking Application указаны:

- **TOOL CARTS**;
- **TOOL TABLES**;
- **SUSPECT MATERIAL**.

В колонке примера **LIVONIA CRIB CODE** для YELLOW указан **M-2310**.

На показанном SOURCE отдельной детальной страницы YELLOW, аналогичной BLUE — QUALITY, нет. Поэтому PMS-код, точные размеры, геометрию рамки и правила нанесения YELLOW здесь не реконструируем.

## 2. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **YELLOW** | жёлтый |
| **Tooling** | оснастка |
| **Suspect Material** | подозрительный материал |
| **Tool Cart** | тележка для оснастки |
| **Tool Table** | стол для оснастки |
| **Scrap Material** | scrap-материал / отходы |
| **Productive Material** | производственный материал |
| **Floor Marking** | напольная разметка |
| **Color Code** | цветовой код |
| **Organizational Category** | организационная категория |
| **Material Category** | категория материала |
| **Visual Coding** | визуальное кодирование |
| **Physical Representation** | физическое представление |
| **LIVONIA CRIB CODE** | код Livonia Crib |

## 3. DISTINCTIONS — РАЗЛИЧЕНИЯ

### YELLOW ≠ SUSPECT MATERIAL

YELLOW кодирует более широкую категорию:

```text
YELLOW
→ TOOLING AND SUSPECT MATERIAL
```

То есть tooling и suspect material находятся под одним визуальным кодом, хотя являются разными по природе объектами.

### TOOLING ≠ MATERIAL

Tool carts / tool tables относятся к tooling.
Suspect material относится к material.

Общий код не означает тождество сущностей.

### SCRAP ≠ SUSPECT

SOURCE разделяет:

```text
RED → SCRAP MATERIAL
YELLOW → TOOLING AND SUSPECT MATERIAL
```

Suspect material не объявляется scrap.

### YELLOW ≠ UNKNOWN

SOURCE на данной странице не определяет YELLOW как «неизвестное». Такое обобщение не допускается.

### COLOR ≠ UNIVERSAL STATUS

Значение YELLOW задаётся именно данной Floor Marking Color Specification.

## 4. EXTRACTION — ИЗВЛЕЧЕНИЕ

Основная SOURCE-конструкция:

```text
TOOL CART / TOOL TABLE / SUSPECT MATERIAL
        ↓
TOOLING AND SUSPECT MATERIAL
        ↓
YELLOW
        ↓
FLOOR MARKING / VISUAL CODE
```

SOURCE здесь задаёт семантическую категорию и примеры применения, но не отдельную физическую спецификацию YELLOW.

## 5. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Yellow Category Visual Coding

**Input:** tooling-related object или suspect material.

**Transformation:** отнесение объекта к категории **TOOLING AND SUSPECT MATERIAL** и применение YELLOW как визуального кода.

**Output:** визуально закодированный объект/зона.

**Эффект:** организационная категория становится визуально распознаваемой.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Tooling Visual Identification

```text
TOOL CART / TOOL TABLE
→ TOOLING
→ YELLOW
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Suspect Material Visual Identification

```text
SUSPECT MATERIAL
→ TOOLING AND SUSPECT MATERIAL
→ YELLOW
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 6. CAPABILITY — СПОСОБНОСТИ

### CANDIDATE — Визуально идентифицировать tooling-related зоны/объекты

Использовать YELLOW как код категории tooling в рамках данной спецификации.

### CANDIDATE — Визуально идентифицировать suspect material

Выделять suspect material визуальным кодом YELLOW.

### CANDIDATE — Объединять разные типы объектов под общей организационной категорией

SOURCE показывает, что tooling и suspect material могут иметь общий визуальный код.

**Важно:** это не означает, что они становятся одной сущностью.

## 7. CORE CANDIDATE

> **Common Visual Category Coding — конструкция, в которой различные по природе объекты получают общий визуальный код, если SOURCE относит их к одной организационной категории.**

Применительно к GM-077:

```text
TOOLING
+
SUSPECT MATERIAL
        ↓
TOOLING AND SUSPECT MATERIAL
        ↓
YELLOW
```

**CANDIDATE / SINGLE-SOURCE**

## 8. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Yellow Category Coding

```text
INPUT
Tooling Object / Suspect Material
        ↓
[ CLASSIFY BY SOURCE CATEGORY ]
        ↓
TOOLING AND SUSPECT MATERIAL
        ↓
[ APPLY YELLOW CODE ]
        ↓
OUTPUT
VISUALLY CODED OBJECT / AREA
        ↓
EFFECT
CATEGORY BECOMES
VISUALLY RECOGNIZABLE
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Физические параметры нанесения YELLOW не включены, поскольку в доступном SOURCE они не показаны.

## 9. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Tool Cart
→ Tooling
→ YELLOW
```

```text
Tool Table
→ Tooling
→ YELLOW
```

```text
Suspect Material
→ Tooling and Suspect Material
→ YELLOW
```

## 10. CMOC INTERPRETATION

GM-075:

```text
PRODUCTIVE MATERIAL
→ GREEN
```

GM-076:

```text
SCRAP MATERIAL
→ RED
```

GM-077:

```text
TOOLING AND SUSPECT MATERIAL
→ YELLOW
```

Получается:

```text
ORGANIZATIONAL CATEGORY
        ↓
COLOR CODE
        ↓
PHYSICAL / VISUAL REPRESENTATION
```

Но GM-077 добавляет новое различение:

```text
DIFFERENT OBJECT TYPES
        ↓
COMMON ORGANIZATIONAL CATEGORY
        ↓
COMMON VISUAL CODE
```

Это **CMOC INTERPRETATION / CANDIDATE**.

## 11. ОСОБО ВАЖНАЯ ОГОВОРКА

Не следует делать вывод:

```text
YELLOW = SUSPECT
```

Правильнее:

```text
YELLOW
→ TOOLING AND SUSPECT MATERIAL
```

И тем более не следует делать вывод:

```text
YELLOW = UNKNOWN
```

или

```text
YELLOW = NONCONFORMING
```

Семантика определяется конкретной спецификацией.

## 12. СВЯЗЬ С GM-073

GM-073 установила принцип:

```text
COLOR
+
SPECIFICATION
↓
MEANING
```

GM-077 даёт конкретный пример:

```text
YELLOW
+
GMPT FLOOR MARKING COLOR SPEC.
↓
TOOLING AND SUSPECT MATERIAL
```

Таким образом, **YELLOW не является самостоятельным онтологическим значением**. Значение возникает из связи **Code + Specification/Context**.

## 13. СТАТУС

**CANDIDATE / SINGLE-SOURCE**

Common Visual Category Coding — **CANDIDATE / SINGLE-SOURCE**.

CANON не присваивается.

## 14. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
