# GM-075 — S-4: STANDARDIZE / GREEN — PRODUCTIVE MATERIAL Floor Marking Specification

**Извещение на изменение:** 0184+280826  
**Источник:** GM Quality System Basics rev. March 2009  
**Раздел:** S-4: STANDARDIZE / GMPT FLOOR MARKING COLOR SPEC.  
**Статус:** CANDIDATE / SINGLE-SOURCE

## 1. SOURCE

На доступной странице GMPT FLOOR MARKING COLOR SPEC. SOURCE задаёт:

**GREEN — PRODUCTIVE MATERIAL**

- RAW STOCK, PURCHASED PARTS
- IN-PROCESS MATERIAL
- FINISHED MATERIAL

На этой странице для GREEN не приведена отдельная детальная спецификация исполнения, аналогичная BLUE — QUALITY. Поэтому PMS-код GREEN, размеры рамки, геометрические параметры, правила текста и иные физические параметры **не реконструируются и не предполагаются**.

## 2. SOURCE BOUNDARY

Доступный материал подтверждает семантику GREEN:

```text
GREEN
↓
PRODUCTIVE MATERIAL
├── RAW STOCK / PURCHASED PARTS
├── IN-PROCESS MATERIAL
└── FINISHED MATERIAL
```

Следующие параметры GREEN остаются **UNRESOLVED**:

- точный PMS / Color Code;
- конкретная ширина линии/рамки;
- геометрия зоны;
- Corner Border / Solid Border;
- требования к label text;
- специальные правила нанесения.

Важно: BLUE-спецификация не переносится автоматически на GREEN.

## 3. TERMS — ТЕРМИНЫ

| English | Русский |
|---|---|
| **GREEN — PRODUCTIVE MATERIAL** | зелёный — производственный материал |
| **Productive Material** | производственный материал |
| **Raw Stock** | исходный материал / заготовка |
| **Purchased Parts** | покупные детали |
| **In-Process Material** | материал в процессе производства |
| **Finished Material** | готовый материал / готовая продукция |
| **Floor Marking** | напольная разметка |
| **Color Code** | цветовой код |
| **Material Category** | категория материала |
| **Physical Area** | физическая зона |
| **Material Flow** | поток материала |

## 4. DISTINCTIONS — РАЗЛИЧЕНИЯ

### GREEN ≠ GOOD

GREEN в данной Floor Marking Color Specification означает **PRODUCTIVE MATERIAL**.

Не переносим на GREEN универсальное значение «соответствует», «разрешено», «хорошо» или иное значение из других визуальных систем.

### Productive Material ≠ Material Status

SOURCE перечисляет категории материала, включая raw stock, purchased parts, in-process material и finished material. Это не следует автоматически трактовать как единый набор статусов.

### In-Process Material ≠ Finished Material

SOURCE различает их как отдельные категории.

### Color Meaning ≠ Physical Implementation

SOURCE здесь подтверждает смысл GREEN, но не предоставляет отдельной детальной спецификации его физического исполнения.

## 5. EXTRACTION — ИЗВЛЕЧЕНИЕ

```text
MATERIAL
↓
PRODUCTIVE MATERIAL
↓
GREEN
↓
PHYSICAL FLOOR MARKING
```

Детализация последнего перехода отсутствует в доступном GREEN-фрагменте.

## 6. MECHANISM — МЕХАНИЗМ

### CANDIDATE — Productive Material Visual Coding

**Input:** материал, относящийся к категории productive material.

**Transformation:** применение GREEN как установленного визуального кода.

**Output:** визуально обозначенная категория productive material.

**STATUS: CANDIDATE / SINGLE-SOURCE**

Полный механизм физического нанесения GREEN **не установлен SOURCE**.

## 7. CAPABILITY — СПОСОБНОСТЬ

### CANDIDATE — Визуально кодировать производственный материал

Способность обозначать через GREEN категорию productive material, включающую raw stock / purchased parts, in-process material и finished material.

**CANDIDATE / SINGLE-SOURCE**

## 8. CORE CANDIDATE

> **Productive Material Visual Coding — конструкция визуального кодирования категории производственного материала через GREEN floor marking, охватывающую raw stock / purchased parts, in-process material и finished material.**

**CANDIDATE / SINGLE-SOURCE**

## 9. MACHINE

### CANDIDATE MACHINE — Productive Material Visual Coding

```text
INPUT
Material
↓
[ CLASSIFY AS PRODUCTIVE MATERIAL ]
↓
GREEN
↓
[ APPLY FLOOR MARKING ]
↓
OUTPUT
VISUALLY CODED PRODUCTIVE MATERIAL AREA
```

**MACHINE = CANDIDATE / SINGLE-SOURCE**

Физические параметры реализации сознательно не включены: они не подтверждены доступным GREEN-фрагментом.

## 10. CHAIN — ЦЕПОЧКА

### SOURCE-SUPPORTED

```text
Raw Stock / Purchased Parts
→ Productive Material
→ GREEN
```

```text
In-Process Material
→ Productive Material
→ GREEN
```

```text
Finished Material
→ Productive Material
→ GREEN
```

Не добавляем переходы:

```text
GREEN → CONFORMING
GREEN → RELEASED
GREEN → GOOD
```

Они SOURCE этой GM не поддерживает.

## 11. CMOC INTERPRETATION

GM-073 установила принцип:

```text
COLOR
+
SPECIFICATION
→
MEANING
```

GM-075 показывает конкретную семантическую область GREEN:

```text
GREEN
→ PRODUCTIVE MATERIAL
→ RAW / IN-PROCESS / FINISHED
```

Отсюда рабочая гипотеза:

> **Один визуальный код может объединять несколько стадий объекта, если они принадлежат одной организационной категории.**

Это **CMOC INTERPRETATION / CANDIDATE**, а не прямое утверждение SOURCE.

## 12. ВАЖНАЯ ОГРАНИЧЕННОСТЬ SOURCE

На доступных пользователем страницах после BLUE-спецификации отдельной страницы GREEN с аналогичной детализацией не обнаружено: следующий показанный фрагмент уже содержит FLOOR LAYOUT Example и 5S Evaluation.

Поэтому GM-075 является **семантической**, а не полной физической спецификацией GREEN.

Это намеренное ограничение точности: недостающие параметры не заменяются предположениями по BLUE.

## 13. STATUS

**CANDIDATE / SINGLE-SOURCE**

Productive Material Visual Coding — **CANDIDATE / SINGLE-SOURCE**.

Полная Reproducible Physical Green Marking Machine — **NOT ESTABLISHED**.

CANON не присваивается.

## 14. FIXATION

PATCH зарегистрирован непосредственно в GitHub.

CORE, каталоги, LAB и предыдущие PATCH не изменялись.
