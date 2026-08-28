# GM-064 — S-1: SORT / Green–Red–Yellow Tagging

**Извещение на изменение:** 0174+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** 5 S Workplace Organization / S-1: SORT  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

SOURCE определяет S-1: SORT:

> **Divide the needed and unneeded items at the job site, removing any unneeded items.**

Четыре области фокуса:

- Equipment;
- Tools;
- Inventory/Storage;
- Personal items.

Для сортировки используется Tagging:

- **Green tag** — item in regular use;
- **Red tag** — item which is not used or is not in working condition;
- **Yellow tag** — item whose use or condition is not known for sure. fileciteturn179file0

## 2. LOCATION

**p. 131 — S-1: SORT.**

Контекст: после общей конструкции 5S Workplace Organization и перед S-2: SET IN ORDER.

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **S-1: SORT** | S-1: сортировка |
| **Sort** | сортировать / разделять |
| **Needed Item** | необходимый предмет |
| **Unneeded Item** | ненужный предмет |
| **Job Site** | рабочее место / участок |
| **Equipment** | оборудование |
| **Tools** | инструменты |
| **Inventory / Storage** | запасы / хранение |
| **Personal Items** | личные предметы |
| **Tag** | бирка / метка |
| **Tagging** | маркировка бирками |
| **Green Tag** | зелёная бирка |
| **Red Tag** | красная бирка |
| **Yellow Tag** | жёлтая бирка |
| **Regular Use** | регулярное использование |
| **Working Condition** | исправное состояние |
| **Use or Condition** | использование или состояние |
| **Known for Sure** | точно известно |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### Needed ≠ Unneeded ≠ Unknown

SOURCE фактически задаёт не только бинарное разделение needed / unneeded. Yellow tag вводит третью категорию: использование или состояние **не известно с уверенностью**.

```text
KNOWN / REGULAR USE
        ↓
GREEN

NOT USED / NOT WORKING
        ↓
RED

UNKNOWN
        ↓
YELLOW
```

### Unneeded ≠ Unknown

Жёлтая бирка не означает «ненужный предмет». Она означает, что использование или состояние ещё не известно наверняка.

### Not Used ≠ Not Working

SOURCE объединяет эти два основания для Red tag, но они логически различны. Не расширяем классификацию за пределы SOURCE.

### Tag ≠ Decision

Бирка фиксирует категорию объекта по SOURCE-критерию, но эта вагонетка не раскрывает последующее решение по каждому тегу.

### Sort ≠ Remove

SOURCE требует удаления unneeded items, но Tagging предварительно создаёт различимое состояние объектов. Не смешиваем классификацию и последующее удаление в один шаг без оговорки.

## 5. GM-FORMULATIONS — ФОРМУЛИРОВКИ GM

> **S-1: SORT – Divide the needed and unneeded items at the job site, removing any unneeded items.**

> **Place a green tag on any item in regular use.**

> **Place a red tag on any item which isn’t used or is not in working condition.**

> **Place a yellow tag on any item that use or condition isn’t known for sure.** fileciteturn179file0

## 6. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
ITEM AT JOB SITE
        ↓
ASSESS USE / CONDITION
        ↓
┌────────────┬──────────────┬───────────────┐
│ GREEN      │ RED          │ YELLOW        │
│ Regular    │ Not used OR  │ Use/condition │
│ use        │ not working  │ unknown       │
└────────────┴──────────────┴───────────────┘
        ↓
VISIBLE CLASSIFICATION
```

И основная операция S-1:

```text
JOB SITE ITEMS
        ↓
DIVIDE NEEDED / UNNEEDED
        ↓
REMOVE UNNEEDED
```

## 7. REL — ОТНОШЕНИЯ

SOURCE поддерживает:

```text
Item
→ Use / Condition
→ Tag Category
```

```text
Regular Use
→ Green Tag
```

```text
Not Used / Not Working
→ Red Tag
```

```text
Use or Condition Unknown
→ Yellow Tag
```

```text
Needed / Unneeded
→ Sort
→ Remove Unneeded
```

## 8. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Three-Color Sorting / Tagging

**Input:** предмет на рабочем месте + информация о его использовании/состоянии.

**Transformation:** классификация по SOURCE-критерию и присвоение визуальной бирки.

**Output:** визуально различимая категория предмета: Green / Red / Yellow.

**Организационный эффект:** состояние знания о предмете становится непосредственно видимым на рабочем месте.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — S-1 Sort / Removal

**Input:** набор предметов рабочей зоны.

**Transformation:** разделение нужных и ненужных предметов и удаление ненужных.

**Output:** рабочая зона без ненужных предметов.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 9. CAPABILITY — СПОСОБНОСТИ

### CANDIDATE — Визуально классифицировать предметы по известности использования/состояния

Способность быстро различать предметы по трём категориям Green / Red / Yellow.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CANDIDATE — Выделять неопределённость как отдельную категорию

Способность не заставлять неизвестный статус предмета искусственно становиться «нужным» или «ненужным», а обозначать неопределённость Yellow tag.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 10. CORE CANDIDATE

> **Three-Color Sorting / Tagging — визуальная конструкция классификации предметов рабочего места по известности их использования и состояния через Green, Red и Yellow tags, делающая различие между регулярным использованием, неиспользованием/неисправностью и неопределённостью непосредственно видимым.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

## 11. MACHINE — МАШИНКА

Здесь особенно важно разделить **Tagging Machine** и **Removal Machine**.

### CANDIDATE MACHINE — Three-Color Tagging

```text
INPUT
Item at Job Site
+
Known Use / Condition
        ↓
[ CLASSIFY ]
        ↓
GREEN / RED / YELLOW
        ↓
[ TAG ]
        ↓
OUTPUT
Visually Classified Item
        ↓
EFFECT
Category Becomes Visible
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Инженерный тест проходит: есть input, операция классификации/tagging, изменённый визуальный результат и организационный эффект — состояние знания о предмете становится видимым.

### CANDIDATE MACHINE — S-1 Sorting / Removal

```text
INPUT
Items at Job Site
        ↓
[ DIVIDE NEEDED / UNNEEDED ]
        ↓
[ REMOVE UNNEEDED ]
        ↓
OUTPUT
Cleared Job Site
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

## 12. CHAIN — ЦЕПОЧКИ

### SOURCE-SUPPORTED

```text
Item
→ Use / Condition
→ Green / Red / Yellow Tag
```

### SOURCE-SUPPORTED

```text
Items at Job Site
→ Needed / Unneeded
→ Remove Unneeded
```

SOURCE не задаёт дальнейшего disposition для Red или Yellow items на этой странице.

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

Tagging Machine — **CANDIDATE / SINGLE-SOURCE**.

Sorting / Removal Machine — **CANDIDATE / SINGLE-SOURCE**.

CANON не присваивается.

## 14. CMOC INTERPRETATION

Здесь появилась особенно ценная конструкция.

GM-059 давала:

```text
PURPOSE
→ NECESSITY
→ REMOVE
```

GM-064 показывает, **как неопределённость не скрывается внутри бинарного решения**:

```text
ITEM
 ↓
WHAT DO WE KNOW?
 ↓
GREEN / RED / YELLOW
```

Отсюда CMOC-гипотеза:

> **Если состояние объекта не известно достаточно уверенно для принятия бинарного решения, неопределённость может быть превращена в отдельное явно видимое состояние.**

Это **CMOC INTERPRETATION**, не SOURCE claim.

И это важнее самой цветовой схемы.

Цвет — носитель.

Инженерная конструкция — **явное выделение неопределённости**.

Ещё одна гипотеза:

```text
UNKNOWN
 ↓
VISIBLE
 ↓
AVAILABLE FOR FURTHER DECISION
```

Но последний шаг SOURCE этой вагонетки не подтверждает, поэтому оставляем его как гипотезу и не включаем в Machine.

## 15. СВЯЗЬ С ПРЕДЫДУЩИМИ ВАГОНЕТКАМИ

GM-059:

```text
PURPOSE → NECESSITY → REMOVE
```

GM-060:

```text
REQUIRED → LOCATION → AVAILABLE
```

GM-061:

```text
CLEAN → CHECK → EQUIPMENT PROBLEM
```

GM-062:

```text
STATE → STANDARD → MAINTAIN
```

GM-063:

```text
STANDARD → SYSTEM SUPPORT → IMPROVE
```

GM-064 добавляет:

```text
KNOWLEDGE / UNCERTAINTY
        ↓
VISUAL CLASSIFICATION
        ↓
VISIBLE STATE
```

Это ещё один потенциальный тип операции CMOC:

> **не изменение объекта, а изменение доступности знания о его состоянии.**

Статус: **CANDIDATE / SINGLE-SOURCE**.

## 16. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
