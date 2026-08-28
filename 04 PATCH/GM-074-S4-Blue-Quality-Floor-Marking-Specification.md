# GM-074 — S-4: STANDARDIZE / BLUE — QUALITY Floor Marking Specification

**Извещение на изменение:** 0183+280826  
**Источник:** GM Quality System Basics rev. March 2009, pp. 136–138  
**Раздел:** S-4: STANDARDIZE / GMPT FLOOR MARKING COLOR SPEC.  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

SOURCE задаёт детальную спецификацию для **BLUE — QUALITY**.

### BLUE — #2 PMS286

**QUALITY ITEMS:**
- Operation Gage Tables;
- Operation Gage Carts;
- Stands or Displays for Quality Information;
- Last Checked Parts and Display Parts;
- Any Other Quality Related Items.

### SPECIFICATIONS
- GM Color Specifications to be used;
- All marked surfaces will be labeled;
- Area is rectangular, slightly larger than item footprint;
- Corner Border or Solid Border use optional.

### CORNER BORDER
- 2" (50 mm) – 4" (100 mm) border to be applied to (4) corners;
- corners to be at least 8" (200 mm) on each side;
- use BLUE #2 PMS286 paint for label text.

### SOLID BORDER
- 2" (50 mm) – 4" (100 mm) border to outline object;
- use WHITE #GMP01 paint for label text.

SOURCE также показывает пример оформления зоны Gage Cart с соответствующей синей разметкой и обозначением.

## 2. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **BLUE — #2 PMS286** | синий — №2 PMS286 |
| **QUALITY ITEMS** | объекты / предметы качества |
| **Operation Gage Table** | стол операционного средства контроля |
| **Operation Gage Cart** | тележка операционного средства контроля |
| **Quality Information Display** | стенд / дисплей информации о качестве |
| **Last Checked Parts** | последние проверенные детали |
| **Display Parts** | демонстрационные детали |
| **Quality Related Items** | прочие объекты, связанные с качеством |
| **GM Color Specifications** | спецификации цветов GM |
| **Marked Surface** | размеченная поверхность |
| **Label** | обозначение / этикетка |
| **Item Footprint** | габаритный след предмета / занимаемая площадь |
| **Corner Border** | угловая рамка |
| **Solid Border** | сплошная рамка |
| **Border Width** | ширина рамки |
| **Label Text** | текст обозначения |
| **Paint** | краска |
| **PMS286** | цветовой код PMS286 |

## 3. DISTINCTIONS — РАЗЛИЧЕНИЯ

### BLUE ≠ QUALITY как универсальное значение

В данной **Floor Marking Color Specification** BLUE кодирует QUALITY. Это значение относится к конкретной спецификации.

### Color Code ≠ Physical Specification

PMS286 задаёт цвет; размеры рамки и геометрия зоны задают физическое исполнение. Это разные свойства одной визуальной конструкции.

### Area ≠ Border

Area — прямоугольная зона, немного больше footprint предмета. Border — способ визуального обозначения этой зоны.

### Corner Border ≠ Solid Border

SOURCE допускает оба варианта; применение corner или solid border является отдельным параметром реализации.

### Border Width ≠ Corner Length

Для corner border SOURCE задаёт:
- ширину рамки 2–4";
- длину каждого угла не менее 8".

Это разные размеры.

### Label ≠ Label Text

Все размеченные поверхности должны быть обозначены; отдельно задаётся цвет текста обозначения.

### Quality Item ≠ Gage

Gage tables/carts — только часть перечисленных QUALITY ITEMS. SOURCE также включает quality information displays, last checked/display parts и любые другие quality-related items.

## 4. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **BLUE — #2 PMS286**

> **ALL MARKED SURFACES WILL BE LABELED.**

> **AREA IS RECTANGULAR, SLIGHTLY LARGER THAN ITEM FOOTPRINT.**

> **CORNER BORDER OR SOLID BORDER USE OPTIONAL.**

> **2" (50 MM) – 4" (100 MM) BORDER TO BE APPLIED TO (4) CORNERS.**

> **CORNERS TO BE AT LEAST 8" (200 MM) ON EACH SIDE.**

> **USE BLUE #2 PMS286 PAINT FOR LABEL TEXT.**

> **2" (50 MM) – 4" (100 MM) BORDER TO OUTLINE OBJECT.**

> **USE WHITE #GMP01 PAINT FOR LABEL TEXT.**

## 5. EXTRACTION — ИЗВЛЕЧЕНИЕ

SOURCE даёт уже не только семантику цвета, но и воспроизводимую физическую спецификацию:

```text
QUALITY ITEM
    ↓
BLUE #2 PMS286
    ↓
RECTANGULAR AREA
SLIGHTLY LARGER THAN FOOTPRINT
    ↓
CORNER BORDER OR SOLID BORDER
    ↓
DEFINED BORDER DIMENSIONS
    ↓
LABEL
    ↓
REPRODUCIBLE BLUE QUALITY AREA
```

Для corner border:

```text
2–4" BORDER
+
4 CORNERS
+
≥ 8" EACH SIDE
```

Для solid border:

```text
2–4" CONTINUOUS BORDER
→ OUTLINE OBJECT
```

Последовательность выше является инженерной реконструкцией требований SOURCE.

## 6. REL — ОТНОШЕНИЯ

SOURCE поддерживает:

```text
BLUE #2 PMS286
→ QUALITY ITEMS
```

```text
QUALITY ITEM
→ RECTANGULAR AREA
```

```text
AREA
→ SLIGHTLY LARGER THAN ITEM FOOTPRINT
```

```text
AREA
→ CORNER BORDER OR SOLID BORDER
```

```text
CORNER BORDER
→ 2–4" WIDTH
→ 4 CORNERS
→ ≥8" EACH SIDE
```

```text
SOLID BORDER
→ 2–4" WIDTH
→ OUTLINE OBJECT
```

```text
MARKED SURFACE
→ LABEL
```

## 7. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Quality Area Physical Coding

**Input:** quality-related item + physical workplace area.

**Transformation:** применение BLUE #2 PMS286 и установленной геометрии floor marking.

**Output:** физически закодированная QUALITY area.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Reproducible Border Application

**Input:** item footprint / designated area.

**Transformation:** применение corner или solid border с заданными размерами.

**Output:** воспроизводимо размеченная зона.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 8. CAPABILITY — СПОСОБНОСТИ

### CANDIDATE — Воспроизводимо размечать зоны качества

Способность реализовать QUALITY area по единому цветовому и геометрическому стандарту.

### CANDIDATE — Воспроизводимо применять рамочную разметку

Способность применять corner или solid border с установленными размерами.

### CANDIDATE — Связывать физическую зону с её категорией

BLUE #2 PMS286 + label превращают физическую зону в визуально идентифицируемую QUALITY area.

## 9. CORE CANDIDATE

> **Reproducible Physical Visual Coding — конструкция, в которой семантически заданная организационная категория переводится в воспроизводимый физический стандарт посредством установленного цвета, геометрии зоны, размеров рамки и обязательного обозначения.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 10. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Quality Area Physical Coding

```text
INPUT
Quality-Related Item
+
Item Footprint
        ↓
[ APPLY COLOR STANDARD ]
BLUE #2 PMS286
        ↓
[ DEFINE AREA ]
Rectangular
Slightly Larger Than Footprint
        ↓
[ APPLY BORDER ]
Corner OR Solid
        ↓
[ APPLY LABEL ]
        ↓
OUTPUT
STANDARDIZED QUALITY AREA
        ↓
EFFECT
QUALITY CATEGORY
BECOMES PHYSICALLY
RECOGNIZABLE AND REPRODUCIBLE
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Это существенно сильнее GM-070/072: SOURCE задаёт конкретные параметры воспроизведения, включая цветовой код и геометрию.

## 11. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
QUALITY ITEM
→ BLUE #2 PMS286
→ MARKED AREA
→ LABEL
```

### SOURCE-SUPPORTED

```text
ITEM FOOTPRINT
→ RECTANGULAR AREA
→ SLIGHTLY LARGER AREA
```

### SOURCE-SUPPORTED

```text
AREA
→ CORNER BORDER OR SOLID BORDER
→ DEFINED DIMENSIONS
```

## 12. CMOC INTERPRETATION

GM-073:

```text
ORGANIZATIONAL CATEGORY
→ COLOR CODE
```

GM-072:

```text
COLOR CODE
→ PHYSICAL REPRESENTATION
```

GM-074:

```text
COLOR CODE
→ GEOMETRY
→ DIMENSION
→ LABEL
→ REPRODUCIBLE PHYSICAL STATE
```

Отсюда появляется сильная CMOC-гипотеза:

> **Визуальный организационный код становится воспроизводимым механизмом только тогда, когда его семантика дополнена физическими параметрами исполнения.**

Это **CMOC INTERPRETATION**, не SOURCE claim.

Ещё одна гипотеза:

```text
SEMANTIC CODE
→ PHYSICAL SPECIFICATION
→ REPEATABLE IMPLEMENTATION
```

То есть SOURCE переводит «BLUE = QUALITY» в инженерно воспроизводимую конструкцию.

## 13. ОСОБОЕ РАЗЛИЧЕНИЕ: SEMANTICS → SPECIFICATION

GM-073 дала:

```text
BLUE
→ QUALITY
```

GM-074 добавляет:

```text
BLUE
→ PMS286
→ AREA GEOMETRY
→ BORDER DIMENSIONS
→ LABEL RULE
```

Таким образом, для CMOC потенциально различаются два уровня стандарта:

### Semantic Standard

```text
CODE → MEANING
```

### Physical Implementation Standard

```text
CODE → HOW TO MATERIALIZE
```

Это **CMOC INTERPRETATION / CANDIDATE**.

## 14. STATUS

**CANDIDATE / SINGLE-SOURCE**

Quality Area Physical Coding Machine — **CANDIDATE / SINGLE-SOURCE**.

Reproducible Border Application — **CANDIDATE / SINGLE-SOURCE**.

Reproducible Physical Visual Coding — **CANDIDATE / SINGLE-SOURCE**.

CANON не присваивается.

## 15. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
