# GM-065 — S-2: SET IN ORDER / Best Location, Frequency of Use, Shadow Boards & Material Limits

**Извещение на изменение:** 0175+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 5 S Workplace Organization / S-2: SET IN ORDER  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

SOURCE определяет S-2 как:

> **A place for everything and everything in it’s place.**

Конструкция включает четыре группы действий:

1. **Categorize** — определить, как часто используется предмет;
2. **Determine a location** — определить место; SOURCE говорит, что для каждого предмета существует “best” place;
3. учитывать частоту использования: часто используемое — держать рядом, редко используемое — размещать дальше/сзади;
4. **Use Shadow Boards**.

Отдельно SOURCE требует установить ограничения уровней материалов:

- Standard packs;
- Work in process;
- Container size and identification. fileciteturn180file1

## 2. LOCATION

**p. 132 — S-2: SET IN ORDER.**

Контекст: после S-1 SORT и перед S-3 SHINE.

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **S-2: SET IN ORDER** | S-2: упорядочивание / размещение по местам |
| **A place for everything and everything in its place** | для всего своё место и всё на своём месте |
| **Categorize** | классифицировать |
| **Frequency of Use** | частота использования |
| **Determine a Location** | определить место |
| **Best Place** | лучшее место |
| **Frequently Used** | часто используемый |
| **Keep Near** | держать рядом |
| **Place at the Rear** | размещать дальше / сзади |
| **Shadow Board** | теневой стенд / стенд с контурами инструментов |
| **Material Level** | уровень материала |
| **Set Limits** | установить пределы |
| **Standard Pack** | стандартная упаковка / стандартная партия |
| **Work in Process (WIP)** | незавершённое производство |
| **Container Size** | размер контейнера |
| **Identification** | идентификация / обозначение |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### Required Item ≠ Location

S-1 определяет, что предмет нужен. S-2 определяет, где он должен находиться.

### Location ≠ Best Location

SOURCE требует не просто назначения места, а определения **best place**.

### Frequency of Use ≠ Need

Частота использования не определяет саму необходимость предмета; она используется SOURCE для определения места размещения.

### Frequently Used ≠ Always Near

SOURCE связывает frequent use с размещением near, а infrequent use — с rear. Не распространяем это правило дальше указанных условий.

### Shadow Board ≠ Location Decision

Shadow Board — средство организации/визуализации места, но SOURCE не говорит, что именно Shadow Board определяет best location.

### Item Location ≠ Material Level

Место предмета и допустимый уровень материала — разные параметры организации.

### Material Level ≠ Container Size

SOURCE перечисляет Standard Packs, WIP, Container Size and Identification как отдельные элементы контроля уровней материалов.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **S-2: SET IN ORDER – A place for everything and everything in it’s place.**

> **How often do I use this item?**

> **There is a “best” place for every item.**

> **If used frequently – keep near. If not – place at the rear.**

> **Use Shadow Boards.**

> **Set limits for material levels: Standard packs; Work in process; Container size and identification.** fileciteturn180file1

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

Основная конструкция:

```text
REQUIRED ITEM
        ↓
[ CATEGORIZE ]
Frequency of Use
        ↓
[ DETERMINE LOCATION ]
Best Place
        ↓
FREQUENT → NEAR
INFREQUENT → REAR
        ↓
[ VISUALIZE / ORGANIZE ]
Shadow Board
```

Отдельная конструкция для материалов:

```text
MATERIAL
        ↓
[ SET LIMITS ]
        ↓
STANDARD PACK
WIP
CONTAINER SIZE + IDENTIFICATION
```

## 7. REL — ОТНОШЕНИЯ

SOURCE поддерживает:

```text
Required Item
→ Frequency of Use
→ Location
```

```text
Frequency of Use
→ Frequent
→ Near
```

```text
Frequency of Use
→ Not Frequent
→ Rear
```

```text
Item
→ Best Place
```

```text
Location Organization
→ Shadow Board
```

```text
Material Level
→ Standard Pack / WIP / Container Size + Identification
```

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Frequency-Based Location Assignment

**Input:** required item + frequency of use + workplace.

**Transformation:** классифицировать по частоте использования и определить best location.

**Output:** item assigned to a location appropriate to its use frequency.

**Организационный эффект:** required item становится доступным в соответствии с заданной логикой размещения.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Material Level Limiting

**Input:** material / WIP + workplace requirements.

**Transformation:** установить limits через standard packs, WIP, container size and identification.

**Output:** определённый и идентифицируемый уровень/форма хранения материала.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТИ

### CANDIDATE — Размещать необходимые предметы по частоте использования

Способность определять location на основе frequency of use.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Устанавливать пределы материальных уровней

Способность ограничивать и визуально/физически определять material levels через standard packs, WIP и container size/identification.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Frequency-Based Workplace Arrangement — конструкция определения места для необходимого предмета на основе частоты его использования с организацией места посредством, в том числе, Shadow Boards.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

Второй кандидат:

> **Material Level Limiting — конструкция задания и идентификации уровней материалов через Standard Packs, WIP, Container Size and Identification.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКИ

Здесь действительно разумно разделить S-2 минимум на две машинки.

### CANDIDATE MACHINE — Frequency-Based Location Machine

```text
INPUT
Required Item
+ Frequency of Use
        ↓
[ CATEGORIZE ]
        ↓
[ DETERMINE BEST LOCATION ]
        ↓
FREQUENT → NEAR
NOT FREQUENT → REAR
        ↓
OUTPUT
Located Required Item
        ↓
EFFECT
Availability aligned with use frequency
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

### CANDIDATE MACHINE — Material Level Limiting Machine

```text
INPUT
Material / WIP
        ↓
[ SET LIMITS ]
        ↓
Standard Pack
+ WIP
+ Container Size / Identification
        ↓
OUTPUT
Defined Material Level / Container State
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

### Shadow Board

Пока не выделяем как отдельную Machine. SOURCE говорит **Use Shadow Boards**, но не раскрывает достаточную операционную цепочку их создания/поддержания.

**MACHINE = NONE / по текущему фрагменту**

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Required Item
→ Frequency of Use
→ Best Location
→ Near / Rear
```

### SOURCE-SUPPORTED

```text
Material
→ Set Limits
→ Standard Pack / WIP / Container Size + Identification
```

Не добавляем поиск, возврат, контроль наличия или replenishment — SOURCE этой вагонетки их не устанавливает.

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

Frequency-Based Location Machine — **CANDIDATE / SINGLE-SOURCE**.

Material Level Limiting Machine — **CANDIDATE / SINGLE-SOURCE**.

Shadow Board — **NONE как отдельная Machine по данному фрагменту**.

CANON не присваивается.

## 14. CMOC INTERPRETATION

GM-060 дала общий принцип:

```text
REQUIRED ITEM
→ BEST LOCATION
```

GM-065 раскрывает критерий выбора:

```text
FREQUENCY OF USE
→ LOCATION
```

Это важное уточнение:

> **Расположение элемента организационной системы может определяться не самим элементом, а характеристикой его использования в процессе.**

Это **CMOC INTERPRETATION**, не SOURCE claim.

Вторая сильная конструкция:

```text
MATERIAL
→ LEVEL LIMIT
→ VISIBLE / IDENTIFIABLE STATE
```

То есть управление касается не только местоположения, но и **количественного состояния запаса / WIP**.

Также важно различить две оси:

```text
WHERE?
→ LOCATION
```

```text
HOW MUCH?
→ MATERIAL LEVEL
```

Они решаются разными конструкциями.

## 15. СВЯЗЬ С GM-059 и GM-060

```text
GM-059
SEIRI
→ WHAT SHOULD REMAIN?
```

```text
GM-060
SEITON
→ WHERE SHOULD IT BE?
```

```text
GM-065
SEITON DETAIL
→ WHERE, BASED ON FREQUENCY?
→ HOW MUCH MATERIAL?
```

Таким образом, GM-065 не создаёт новый S, а **раскрывает операционную структуру Seiton**.

## 16. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
