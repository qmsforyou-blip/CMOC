# GM-076 — S-4: STANDARDIZE / RED — SCRAP MATERIAL Floor Marking Specification

**Извещение на изменение:** 0185+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** S-4: STANDARDIZE  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

В GMPT FLOOR MARKING COLOR SPEC. SOURCE задаёт:

**RED — SCRAP MATERIAL**

Применение:
- **SCRAP BINS** — контейнеры для scrap;
- **SCRAP CARTS** — тележки для scrap;
- **OTHER SCRAP RELATED ITEMS** — другие объекты, связанные со scrap.

В общей таблице пример кода Livia CRIB для RED указан как **M-2309**.

Источник тем самым связывает RED не с абстрактным значением «плохой» или «несоответствующий», а с конкретной организационной категорией **SCRAP MATERIAL**.

## 2. ВАЖНАЯ ГРАНИЦА SOURCE

На предоставленном пользователем фрагменте SOURCE отдельной детальной страницы RED со своими PMS-кодом, геометрией, шириной рамки и правилами нанесения **нет**. После страницы BLUE SOURCE переходит к Floor Layout Example и затем к 5S Evaluation.

Поэтому параметры BLUE из GM-074 в GM-076 **не переносятся автоматически**.

Не утверждаем для RED:
- PMS-код;
- ширину линии;
- размеры corner border;
- размеры solid border;
- конкретные требования к label text;
- отдельную геометрию зоны.

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **RED — SCRAP MATERIAL** | красный — scrap-материал |
| **Scrap Material** | scrap-материал / отходы |
| **Scrap Bin** | контейнер для scrap |
| **Scrap Cart** | тележка для scrap |
| **Other Scrap Related Items** | другие объекты, связанные со scrap |
| **Floor Marking** | напольная разметка |
| **Color Code** | цветовой код |
| **Organizational Category** | организационная категория |
| **Material Category** | категория материала |
| **Physical Coding** | физическое кодирование |
| **Disposition** | решение о дальнейшем обращении с несоответствующим продуктом |
| **Nonconforming Product** | несоответствующая продукция |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### RED ≠ BAD

SOURCE не формулирует RED как «плохое».

```text
RED
↓
SCRAP MATERIAL
```

### SCRAP MATERIAL ≠ NONCONFORMING PRODUCT

Это особенно важно для CMOC.

```text
SCRAP MATERIAL
≠
NONCONFORMING PRODUCT
```

Scrap — категория материала / физического потока в данной Floor Marking Specification.

Nonconforming Product — отдельная организационная категория в блоках контроля несоответствующего продукта.

Не объединяем их без дополнительного SOURCE.

### SCRAP ≠ SUSPECT

SOURCE явно разделяет:

```text
RED → SCRAP MATERIAL
YELLOW → TOOLING AND SUSPECT MATERIAL
```

Следовательно, suspect material не должен автоматически кодироваться RED.

### RED ≠ UNIVERSAL SEMANTICS

В другом контексте SOURCE может использовать красный для иной категории. Поэтому:

```text
COLOR
+
SPECIFICATION / CONTEXT
→
MEANING
```

остаётся рабочим правилом.

## 5. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
SCRAP RELATED OBJECT
        ↓
ORGANIZATIONAL CATEGORY
        ↓
SCRAP MATERIAL
        ↓
RED
        ↓
FLOOR MARKING / VISUAL CODE
```

SOURCE-supported категории объектов:

```text
SCRAP BINS
SCRAP CARTS
OTHER SCRAP RELATED ITEMS
```

## 6. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Scrap Area Visual Coding

**Input:** физическая зона / объект, относящийся к scrap.

**Transformation:** применение RED как установленного визуального кода Floor Marking Color Specification.

**Output:** визуально закодированный scrap-related object/area.

**Эффект:** принадлежность объекта к категории SCRAP MATERIAL становится визуально распознаваемой.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Scrap Container Identification

```text
SCRAP BIN / SCRAP CART
→ RED
→ VISUAL IDENTIFICATION
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 7. CAPABILITY — СПОСОБНОСТИ

### CANDIDATE — Визуально идентифицировать scrap-related объекты

Способность кодировать контейнеры, тележки и другие связанные со scrap объекты единым цветовым признаком.

### CANDIDATE — Различать scrap и suspect material

В рамках данной спецификации:

```text
RED → SCRAP MATERIAL
YELLOW → TOOLING + SUSPECT MATERIAL
```

Это различение SOURCE-supported.

## 8. CORE CANDIDATE

> **Scrap Material Visual Coding — конструкция визуального кодирования объектов, относящихся к scrap material, посредством RED floor marking.**

**CANDIDATE / SINGLE-SOURCE**

## 9. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Scrap Category Visual Coding

```text
INPUT
Scrap-Related Object / Area
        ↓
[ CLASSIFY AS SCRAP MATERIAL ]
        ↓
[ APPLY RED VISUAL CODE ]
        ↓
OUTPUT
VISUALLY CODED SCRAP OBJECT / AREA
        ↓
EFFECT
SCRAP CATEGORY
BECOMES RECOGNIZABLE
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Параметры физического исполнения не включены, поскольку SOURCE их для RED в доступном фрагменте не задаёт.

## 10. CHAIN — ЦЕПОЧКА

### SOURCE-SUPPORTED

```text
Scrap Bin
→ Scrap Material
→ RED
```

```text
Scrap Cart
→ Scrap Material
→ RED
```

```text
Other Scrap Related Item
→ Scrap Material
→ RED
```

## 11. CMOC INTERPRETATION

GM-075 дала:

```text
RAW / PURCHASED
IN-PROCESS
FINISHED
        ↓
PRODUCTIVE MATERIAL
        ↓
GREEN
```

GM-076 даёт другую конструкцию:

```text
SCRAP-RELATED OBJECT
        ↓
SCRAP MATERIAL
        ↓
RED
```

Получаем важное различение:

```text
PRODUCTIVE MATERIAL
≠
SCRAP MATERIAL
```

И обе категории могут быть представлены физическим визуальным кодом.

### CMOC-гипотеза

> **Визуальное кодирование может разделять не только местоположение объектов, но и организационные категории материального потока.**

**CMOC INTERPRETATION / CANDIDATE**

## 12. СВЯЗЬ С CONTROL OF NONCONFORMING PRODUCT

Здесь требуется особая осторожность.

SOURCE в другом контексте различает:

```text
NONCONFORMING PRODUCT
SUSPECT PRODUCT
CONFORMING PRODUCT
```

и использует визуальные цвета для containment.

Поэтому нельзя построить универсальное правило:

```text
RED = NONCONFORMING
```

Для GM-076 корректно только:

```text
RED
+
FLOOR MARKING SPECIFICATION
→
SCRAP MATERIAL
```

## 13. MACHINE FAMILY

Теперь GM-075 и GM-076 можно рассматривать как два экземпляра одного кандидата более высокого класса:

```text
MATERIAL CATEGORY
        ↓
COLOR CODE
        ↓
PHYSICAL VISUAL REPRESENTATION
```

### Instance A

```text
PRODUCTIVE MATERIAL
→ GREEN
```

### Instance B

```text
SCRAP MATERIAL
→ RED
```

**Higher-level Machine Family = CANDIDATE / MULTI-SOURCE**

## 14. STATUS

**GM-076: CANDIDATE / SINGLE-SOURCE**

**Scrap Material Visual Coding Machine: CANDIDATE / SINGLE-SOURCE**

**Material Category → Color Code → Physical Representation: CANDIDATE / MULTI-SOURCE**

CANON не присваивается.

## 15. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
