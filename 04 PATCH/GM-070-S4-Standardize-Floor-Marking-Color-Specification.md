# GM-070 — S-4: STANDARDIZE / Floor Marking Color Specification

**Извещение на изменение:** 0179+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 5 S Workplace Organization / S-4: STANDARDIZE / Floor Marking Color Specification  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

SOURCE приводит **GMPT Floor Marking Color Specification** как средство стандартизации визуального состояния пространства.

Цвет пола/разметки используется для обозначения различных организационных зон и состояний. В спецификации выделяются, в частности, зоны/объекты для:

- material / product flow;
- finished product;
- work in process;
- raw material;
- scrap;
- suspect material;
- housekeeping stations;
- fire equipment / safety-related locations.

**Важно:** в этой вагонетке фиксируется сама SOURCE-конструкция цветового кодирования. Конкретные значения цветов сохраняются только в той мере, в какой они непосредственно заданы SOURCE; цвет не получает универсального CMOC-смысла вне данной спецификации.

SOURCE также связывает визуальную стандартизацию с простотой обнаружения проблем через visual controls. fileciteturn191file0

## 2. LOCATION

**S-4: STANDARDIZE — Floor Marking Color Specification.**

GM-070 выделяет из S-4 именно конструкцию **кодирования пространства посредством цветовой разметки**.

Это продолжение GM-068:

```text
GM-068
VISUAL STANDARDIZATION
→ LOCATION IDENTIFICATION
```

```text
GM-070
FLOOR MARKING
→ ORGANIZATIONAL AREA / STATE CODING
```

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **Floor Marking** | напольная разметка |
| **Floor Marking Color Specification** | спецификация цветов напольной разметки |
| **Color Coding** | цветовое кодирование |
| **Designated Area** | выделенная / назначенная зона |
| **Material Flow** | поток материалов |
| **Product Flow** | поток продукции |
| **Finished Product** | готовая продукция |
| **Work in Process (WIP)** | незавершённое производство |
| **Raw Material** | сырьё / исходный материал |
| **Scrap** | лом / отходы / брак, направленный в scrap |
| **Suspect Material** | подозрительный материал |
| **Housekeeping Station** | пост / место housekeeping |
| **Fire Equipment** | противопожарное оборудование |
| **Safety Location** | место, связанное с безопасностью |
| **Area Identification** | идентификация зоны |
| **Visual Control** | визуальный контроль |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### Floor Marking ≠ Decoration

Разметка используется как информационный и организационный носитель.

### Color ≠ Meaning in General

Цвет получает значение внутри конкретной спецификации. Не превращаем SOURCE-кодировку в универсальный CMOC-словарь цветов.

### Area ≠ State

Некоторые категории относятся к пространственной зоне, другие — к состоянию/категории материала. Не смешиваем их.

### Location Coding ≠ Material Status

Обозначение места и обозначение статуса материала — разные функции, даже если они используют один визуальный носитель.

### Scrap ≠ Suspect Material

SOURCE различает эти категории. Suspect material не объявляется автоматически scrap.

### Visual Coding ≠ Decision

Цвет делает категорию распознаваемой. Он не является сам по себе решением о disposition.

### Flow ≠ Storage

Обозначение material/product flow и обозначение места хранения — разные функции визуальной системы.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

SOURCE использует **Floor Marking Color Specification** как часть визуальной стандартизации S-4 и задаёт цветовое различение организационных зон/категорий.

Ключевая инженерная формула GM:

> **SPACE / AREA → COLOR CODE → ORGANIZATIONAL CATEGORY**

Для категорий материала/продукции:

```text
COLOR
→ MATERIAL / PRODUCT CATEGORY
```

Для пространства:

```text
FLOOR MARKING
→ DESIGNATED AREA
```

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
ORGANIZATIONAL SPACE
        ↓
[ APPLY FLOOR MARKING / COLOR CODE ]
        ↓
DESIGNATED AREA
        ↓
VISIBLE ORGANIZATIONAL CATEGORY
```

И для материальных категорий:

```text
MATERIAL / PRODUCT
        ↓
CATEGORY
        ↓
VISUAL CODE
        ↓
IMMEDIATELY RECOGNIZABLE CATEGORY
```

Это инженерная реконструкция; SOURCE задаёт спецификацию и категории, но не описывает полный алгоритм проектирования системы.

## 7. REL — ОТНОШЕНИЯ

SOURCE поддерживает:

```text
Designated Area
→ Color Coding
```

```text
Floor Marking
→ Area Identification
```

```text
Material / Product Category
→ Visual Code
```

```text
Finished Product / WIP / Raw Material / Scrap / Suspect Material
→ Distinct Organizational Category
```

```text
Housekeeping / Safety Location
→ Designated Visual Area
```

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Organizational Space Coding

**Input:** физическое пространство предприятия.

**Transformation:** нанесение стандартизированной цветовой разметки.

**Output:** визуально закодированная организационная зона.

**Эффект:** функция/категория зоны становится непосредственно распознаваемой.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Material Category Visual Coding

**Input:** material/product category.

**Transformation:** присвоение визуального кода согласно SOURCE specification.

**Output:** категория материала/продукции визуально различима.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТИ

### CANDIDATE — Кодировать организационное пространство

Способность переводить организационные категории зон в единый визуальный носитель.

**CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Визуально различать категории материального состояния

Способность делать различия между finished product, WIP, raw material, scrap и suspect material непосредственно видимыми в пространстве.

**CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Organizational Space Coding — конструкция визуального кодирования пространства предприятия, в которой стандартизированная цветовая разметка связывает физическую зону с заданной организационной категорией.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Organizational Space Coding

```text
INPUT
Physical Space
+
Organizational Category
        ↓
[ ASSIGN / APPLY VISUAL CODE ]
        ↓
FLOOR MARKING / COLOR
        ↓
OUTPUT
VISUALLY CODED AREA
        ↓
EFFECT
AREA CATEGORY
BECOMES RECOGNIZABLE
```

### Инженерный тест

**INPUT:** пространство + организационная категория.

**OPERATION:** визуальное кодирование.

**OUTPUT:** закодированная зона.

**EFFECT:** категория пространства становится наблюдаемой.

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Но SOURCE не задаёт здесь процедуру выбора оптимального цвета для каждой категории. Цвета следует брать из конкретной спецификации, а не реконструировать.

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Organizational Category
→ Floor Marking / Color Code
→ Designated Area
```

### SOURCE-SUPPORTED

```text
Material Category
→ Visual Code
→ Recognizable State / Category
```

Не добавляем автоматически:

```text
COLOR
→ DECISION
```

или:

```text
COLOR
→ DISPOSITION
```

Эти связи требуют отдельного SOURCE.

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

Organizational Space Coding Machine — **CANDIDATE / SINGLE-SOURCE**.

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-068 показала:

```text
LOCATION
→ VISUAL IDENTIFICATION
```

GM-069:

```text
VISUAL CONTROL
→ PROBLEM IDENTIFICATION
```

GM-070 добавляет:

```text
ORGANIZATIONAL CATEGORY
        ↓
PHYSICAL SPACE
        ↓
VISUAL CODE
        ↓
OBSERVABLE ORGANIZATIONAL STATE
```

Отсюда сильная CMOC-гипотеза:

> **Организационное состояние пространства может быть закодировано непосредственно в физической среде так, чтобы категория зоны распознавалась без обращения к отдельному документу.**

Это **CMOC INTERPRETATION**, не SOURCE claim.

### Следующее различение

```text
INFORMATION ABOUT SPACE
        ≠
CODED SPACE
```

В первом случае знание находится вне пространства.

Во втором часть знания встроена в физический носитель.

Статус: **CANDIDATE / SINGLE-SOURCE + CMOC INTERPRETATION**.

## 15. КРИТИЧЕСКОЕ РАЗЛИЧЕНИЕ: STATE VS CATEGORY

Не все цвета в спецификации следует называть «статусами».

Например:

```text
RAW MATERIAL
WIP
FINISHED PRODUCT
```

могут обозначать категорию материального состояния/позиции потока,

а:

```text
SCRAP
SUSPECT MATERIAL
```

уже несут более выраженную информацию о состоянии допустимости/назначения материала.

Поэтому универсальную формулу:

```text
COLOR → STATUS
```

не канонизируем.

Более точная формула:

```text
COLOR
→ ORGANIZATIONAL CATEGORY / STATE
```

**CANDIDATE.**

## 16. СВЯЗЬ С CMOC-ЛОГИКОЙ НАБЛЮДАЕМОСТИ

Предварительная цепочка:

```text
ORGANIZATIONAL RULE
        ↓
PHYSICAL MARKING
        ↓
VISIBLE CATEGORY
        ↓
FASTER RECOGNITION OF STATE
```

Последняя стрелка — только CMOC-гипотеза.

SOURCE подтверждает визуальную стандартизацию и идентификацию, но не измеряет скорость распознавания.

## 17. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
