# GM-068 — S-4: STANDARDIZE / Visual Standardization & Item Locations

**Извещение на изменение:** 0177+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 5 S Workplace Organization / S-4: STANDARDIZE  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

SOURCE определяет S-4:

> **Standardize the area visually and mark the location of each item.**

Далее перечислены конкретные способы визуальной стандартизации:

- Color coding for designated areas;
- Designate area shapes;
- Consistent label height and color throughout facility;
- Storage containers and storage areas practices.

fileciteturn189file4

На следующем фрагменте S-4 SOURCE добавляет:

- Determine cleaning schedule and methods;
- Standardize cabinet organization;
- Define a simple method to identify problems using visual controls.

Пример показывает, что locations of items должны быть properly identified. fileciteturn189file0

## 2. LOCATION

**p. 134–135 — S-4: STANDARDIZE.**

GM-068 рассматривает первую часть S-4 — визуальную стандартизацию зоны и маркировку мест предметов. Продолжение с cleaning schedule, cabinet organization и visual problem identification будет выделено отдельно.

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **S-4: STANDARDIZE** | S-4: стандартизация |
| **Standardize** | стандартизировать |
| **Visual Standardization** | визуальная стандартизация |
| **Designated Area** | выделенная / назначенная зона |
| **Color Coding** | цветовое кодирование |
| **Area Shape** | форма / контур зоны |
| **Label Height** | высота этикетки |
| **Label Color** | цвет этикетки |
| **Facility** | предприятие / объект |
| **Storage Container** | контейнер хранения |
| **Storage Area** | зона хранения |
| **Location** | место расположения |
| **Identify / Identification** | обозначать / идентификация |
| **Properly Identified** | надлежащим образом обозначенный |
| **Visual Control** | визуальный контроль |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### Standardize ≠ Set in Order

S-2 определяет best location для required items. S-4 делает организацию зоны и locations визуально стандартизированными и идентифицируемыми.

### Location ≠ Location Identification

Место может быть определено; S-4 добавляет его визуальное обозначение.

### Color Coding ≠ Color as Decoration

В SOURCE цвет используется как средство обозначения designated areas. Не приписываем цвету дополнительных значений, которых SOURCE здесь не задаёт.

### Area Shape ≠ Location

Форма/контур зоны является средством визуального обозначения, а не самой организационной логикой выбора места.

### Label ≠ Standard

Этикетка является средством идентификации стандартизированной зоны/места; она не тождественна самому стандарту.

### Standardization ≠ Cleaning

Cleaning schedule and methods перечислены в продолжении S-4, но здесь отдельно фиксируется визуальная стандартизация и обозначение locations.

### Visual Control ≠ Problem Solving

SOURCE говорит о simple method to identify problems using visual controls. Это идентификация проблемы, а не решение проблемы.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **Standardize the area visually and mark the location of each item.**

> **Color coding for designated areas.**

> **Designate area shapes.**

> **Consistent label height and color throughout facility.**

> **Storage containers and storage areas practices.** fileciteturn189file4

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

Основная конструкция SOURCE:

```text
AREA
  ↓
VISUAL STANDARDIZATION
  ↓
COLOR CODING
+ AREA SHAPES
+ CONSISTENT LABELS
+ STORAGE PRACTICES
  ↓
ITEM LOCATIONS IDENTIFIED
```

SOURCE не задаёт здесь полный алгоритм проектирования визуального стандарта. Поэтому указанная последовательность — инженерная реконструкция.

## 7. REL — ОТНОШЕНИЯ

SOURCE поддерживает:

```text
Designated Area
→ Color Coding
```

```text
Area
→ Area Shape
```

```text
Facility
→ Consistent Label Height + Color
```

```text
Storage Container / Storage Area
→ Storage Practices
```

```text
Item Location
→ Proper Identification
```

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Visual Location Standardization

**Input:** рабочая зона + существующие locations предметов.

**Transformation:** визуальное обозначение зон и мест через color coding, area shapes, consistent labels и storage practices.

**Output:** визуально стандартизированная зона, в которой locations предметов обозначены.

**Организационный эффект:** место предмета становится непосредственно идентифицируемым.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Consistent Facility Visual Coding

**Input:** множество зон/мест на предприятии.

**Transformation:** применение согласованных высоты и цвета labels.

**Output:** единообразная визуальная система обозначения.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТИ

### CANDIDATE — Визуально идентифицировать места предметов

Способность сделать location каждого item непосредственно распознаваемым.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Обеспечивать единообразие визуальных обозначений

Способность применять согласованные label height и color throughout facility.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Visual Location Standardization — конструкция визуального обозначения рабочих и складских зон и мест предметов посредством цветового кодирования, форм зон, единообразных этикеток и практик хранения, делающая locations визуально идентифицируемыми.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

### CANDIDATE MACHINE — Visual Location Standardization

```text
INPUT
Existing Area
+
Item Locations
        ↓
[ STANDARDIZE VISUALLY ]
        ↓
COLOR CODING
+
AREA SHAPES
+
CONSISTENT LABELS
+
STORAGE PRACTICES
        ↓
OUTPUT
Visually Identified Locations
        ↓
EFFECT
Location Becomes
Immediately Identifiable
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Инженерный тест проходит: есть объект преобразования, операция визуальной стандартизации, изменённое состояние обозначения и организационный эффект.

Но SOURCE не описывает полный цикл создания/проверки стандарта, поэтому Machine остаётся Candidate.

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Area
→ Visual Standardization
→ Color / Shape / Labels
```

### SOURCE-SUPPORTED

```text
Item
→ Location
→ Identification
```

Не добавляем автоматически «идентификация → обнаружение отклонения»: такая связь раскрывается только в продолжении S-4 через visual controls и будет обработана отдельно.

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

Visual Location Standardization Machine — **CANDIDATE / SINGLE-SOURCE**.

Consistent Facility Visual Coding — **CANDIDATE / SINGLE-SOURCE**.

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-060:

```text
REQUIRED ITEM
→ BEST LOCATION
```

GM-068:

```text
LOCATION
→ VISUAL IDENTIFICATION
```

Отсюда CMOC-гипотеза:

> **Назначенное место становится частью управляемой организационной конструкции только тогда, когда его состояние и границы могут быть непосредственно распознаны участником процесса.**

Это **CMOC INTERPRETATION**, не SOURCE claim.

Вторая гипотеза:

```text
HIDDEN LOCATION
→ VISUALIZED LOCATION
→ LOWER INTERPRETATION COST
```

Последняя связь пока не является SOURCE claim: GM прямо требует визуальной стандартизации и маркировки, но не формулирует здесь измерение interpretation cost.

## 15. СВЯЗЬ С GM-062

GM-062:

```text
ACHIEVED STATE
→ STANDARD
→ MAINTAIN
```

GM-068 конкретизирует один слой стандарта:

```text
STANDARD
→ VISUAL REPRESENTATION
→ IDENTIFIABLE LOCATION
```

То есть визуальный носитель может быть частью механизма, через который стандарт становится непосредственно наблюдаемым.

## 16. ГРАНИЦА С ПРОДОЛЖЕНИЕМ S-4

На следующем фрагменте SOURCE уже появляются:

```text
CLEANING SCHEDULE + METHODS
CABINET ORGANIZATION
VISUAL CONTROLS
→ SIMPLE PROBLEM IDENTIFICATION
```

fileciteturn189file0

Эти элементы намеренно **не включены в основную Machine GM-068**. Они будут добыты отдельно, чтобы не смешивать разные операционные конструкции.

## 17. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
