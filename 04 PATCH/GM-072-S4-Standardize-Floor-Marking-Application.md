# GM-072 — S-4: STANDARDIZE / Floor Marking Application

**Извещение на изменение:** 0181+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 5 S Workplace Organization / S-4: STANDARDIZE (continued), p.137  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

На p.137 SOURCE показывает конкретный пример применения стандарта визуальной разметки:

### FLOOR MARKING

- paint / tape;
- a **blue line 2–4 inches wide** on the floor;
- размер зоны — по размеру стола;
- description должен быть нанесён/обозначен.

### OVERHEAD SIGN

Знак должен указывать:

- department;
- operation #.

Знак крепится к столу или подвешивается сверху — в зависимости от ситуации.

### LABELS & SILHOUETTES

Размещение gauges и documentation должно быть обозначено непосредственно на столе вместе с соответствующим:

- serial number;
- или description.

fileciteturn196file0

## 2. LOCATION

**p.137 — S-4: STANDARDIZE (continued), Example.**

GM-072 является конкретизацией общей конструкции GM-068 и не заменяет её.

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Floor Marking** | напольная разметка |
| **Paint / Tape** | краска / лента |
| **Blue Line** | синяя линия |
| **2–4 inch wide** | шириной 2–4 дюйма |
| **Sized to Suit Tables** | размером по столам / под размер стола |
| **Description** | описание |
| **Overhead Sign** | верхний / подвесной знак |
| **Department** | подразделение / отдел |
| **Operation #** | номер операции |
| **Attach** | прикреплять |
| **Hang from Above** | подвешивать сверху |
| **Labels** | этикетки / обозначения |
| **Silhouettes** | контуры / силуэты |
| **Gage / Gauge** | калибр / средство контроля |
| **Documentation** | документация |
| **Serial Number** | серийный номер |
| **Description** | описание |
| **Marked Surface** | размеченная поверхность |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### Floor Marking ≠ Overhead Sign

Floor marking кодирует физическую зону на полу.

Overhead sign идентифицирует department и operation #.

Это разные носители информации.

### Area Boundary ≠ Area Identity

Линия задаёт/обозначает границу зоны.

Description и sign идентифицируют её содержательно.

### Item Location ≠ Item Identity

Silhouette/placement показывает, где должен находиться item.

Serial number или description идентифицирует сам item.

### Label ≠ Silhouette

Label несёт текстовую идентификацию.

Silhouette показывает форму/место размещения предмета.

### Serial Number ≠ Description

SOURCE допускает serial number **или** description для обозначения gauges и documentation.

Не объединяем их в обязательную пару.

### Standard ≠ Implementation Detail

Общий принцип S-4 — визуально стандартизировать область.

Размер линии 2–4", цвет Blue и конкретные способы маркировки — уже реализация данного принципа в SOURCE-примере.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **Paint / tape a blue line 2–4” wide on the floor sized to suit tables with description labeled.**

> **Sign to indicate department and operation #.**

> **Placement of gages and documentation is to be marked on the table along with the appropriate serial number or description for each.** fileciteturn196file0

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

SOURCE даёт три конкретных носителя:

```text
WORK AREA
   ↓
┌──────────────────────────────┐
│ FLOOR MARKING                │
│ blue line 2–4" + description │
└──────────────────────────────┘

┌──────────────────────────────┐
│ OVERHEAD SIGN                │
│ department + operation #     │
└──────────────────────────────┘

┌──────────────────────────────┐
│ LABELS & SILHOUETTES         │
│ gages + documentation        │
│ serial number / description  │
└──────────────────────────────┘
```

## 7. REL — ОТНОШЕНИЯ

SOURCE поддерживает:

```text
Floor
→ Blue Line
→ Area Boundary / Marking
```

```text
Marked Area
→ Description
```

```text
Department + Operation
→ Overhead Sign
```

```text
Gage / Documentation
→ Placement Marking
→ Serial Number / Description
```

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Physical Area Marking

**Input:** физическая рабочая зона.

**Transformation:** нанесение standardized floor marking и description.

**Output:** физически обозначенная зона.

**Эффект:** граница/назначение зоны становится наблюдаемой.

**CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Operation Point Identification

**Input:** рабочая точка / стол.

**Transformation:** department + operation # через overhead sign.

**Output:** идентифицированная рабочая точка.

**CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Item Placement Identification

**Input:** gauges / documentation + table.

**Transformation:** marking of placement + serial number or description.

**Output:** идентифицированное место и объект.

**CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТИ

### CANDIDATE — Физически обозначать организационные границы

Создавать на полу наблюдаемую границу назначенной зоны.

### CANDIDATE — Идентифицировать рабочую точку

Связывать рабочее место с department и operation number.

### CANDIDATE — Идентифицировать место и объект средства контроля/документации

Связывать placement с serial number или description.

Все: **CANDIDATE / SINGLE-SOURCE**.

## 10. CORE CANDIDATE

> **Floor Marking Application — конкретная реализация визуального стандарта, связывающая физическую рабочую зону, её описание, подразделение и операцию, а также места gauges и documentation с их идентификацией.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Physical Space Coding

```text
INPUT
Physical Work Area
        ↓
[ MARK BOUNDARY ]
        ↓
BLUE LINE 2–4"
        ↓
[ ADD DESCRIPTION ]
        ↓
OUTPUT
Identified Physical Area
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

### CANDIDATE MACHINE — Work Point Identification

```text
INPUT
Work Point
        ↓
[ IDENTIFY DEPARTMENT ]
+
[ IDENTIFY OPERATION # ]
        ↓
OVERHEAD SIGN
        ↓
OUTPUT
Identified Work Point
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

### CANDIDATE MACHINE — Item Placement Identification

```text
INPUT
Gage / Documentation
        ↓
[ MARK PLACEMENT ]
        ↓
[ ADD SERIAL NUMBER / DESCRIPTION ]
        ↓
OUTPUT
Identified Item + Location
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Work Area
→ Floor Marking
→ Description
```

```text
Work Point
→ Department + Operation #
→ Overhead Sign
```

```text
Gage / Documentation
→ Placement Marking
→ Serial Number / Description
```

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

Physical Space Coding Machine — **CANDIDATE / SINGLE-SOURCE**.

Work Point Identification Machine — **CANDIDATE / SINGLE-SOURCE**.

Item Placement Identification Machine — **CANDIDATE / SINGLE-SOURCE**.

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-070 сформулировала общий принцип:

```text
ORGANIZATIONAL CATEGORY
→ PHYSICAL CODE
→ VISIBLE CATEGORY
```

GM-072 показывает его реализацию несколькими физическими носителями:

```text
SPACE
→ FLOOR MARKING
```

```text
WORK POINT
→ OVERHEAD SIGN
```

```text
ITEM + LOCATION
→ LABEL / SILHOUETTE
```

Отсюда CMOC-гипотеза:

> **Одна организационная конструкция может использовать несколько физических носителей, каждый из которых кодирует отдельный аспект организационного состояния.**

Это **CMOC INTERPRETATION**, не SOURCE claim.

## 15. НОВОЕ РАЗЛИЧЕНИЕ: ГРАНИЦА / ИДЕНТИЧНОСТЬ / СОДЕРЖАНИЕ

В GM-072 фактически различаются три информационных слоя:

```text
BOUNDARY
→ где находится зона
```

```text
IDENTITY
→ какая это рабочая точка
```

```text
CONTENT / ITEM IDENTITY
→ что именно находится в обозначенном месте
```

SOURCE не формулирует эту тройку как теоретическую модель. Это **CMOC INTERPRETATION**.

Но для инженерной типологии она потенциально очень полезна.

## 16. СВЯЗЬ С GM-069–071

GM-069:

```text
VISUAL CONTROL
→ IDENTIFY PROBLEM
```

GM-070:

```text
SPACE
→ ORGANIZATIONAL CODE
```

GM-071:

```text
VISUAL CONTROL
→ PROBLEM IDENTIFICATION
```

GM-072 показывает физическую реализацию:

```text
CODE
→ LINE
→ SIGN
→ LABEL
→ SILHOUETTE
```

Следовательно, visual control — это не обязательно отдельная табличка. Он может быть распределён по физической среде.

## 17. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
