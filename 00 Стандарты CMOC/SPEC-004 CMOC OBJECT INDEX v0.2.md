# SPEC-004 — CMOC OBJECT INDEX v0.2

**Дата:** 19-09-2026  
**Статус:** DESIGN / CONTRACT CANDIDATE  
**Назначение:** контракт машинно-читаемой карты адресуемых представлений знания CMOC.

---

## 1. Назначение

OBJECT INDEX не является копией CMOC и не заменяет CMOC как источник знания.

Его назначение:

1. зарегистрировать обнаруженные адресуемые единицы знания;
2. обеспечить быстрый поиск и навигацию к ним;
3. сохранить происхождение индексной записи;
4. предоставить QUERY структурированную карту для работы;
5. поддержать последующие RECONCILIATION и ASSEMBLY.

Главный принцип:

> **CMOC хранит знание. OBJECT INDEX хранит карту доступа к адресуемым представлениям этого знания.**

---

## 2. Граница

Архитектурная цепочка:

```
CMOC
  ↓
INVENTORY
  ↓
OBJECT INDEX
  ↓
QUERY
  ↓
RECONCILIATION
  ↓
ASSEMBLY
```

### INVENTORY

Отвечает:

> Какие физические файлы и структурные контейнеры существуют?

### OBJECT INDEX

Отвечает:

> Какие адресуемые представления объектов обнаружены и где их найти?

### QUERY

Отвечает:

> Какие объекты удовлетворяют заданному поисковому условию?

### RECONCILIATION

Отвечает:

> Как найденное знание соотносится с уже накопленным знанием CMOC?

### ASSEMBLY

Отвечает:

> Как собрать выбранное знание в требуемое представление?

---

## 3. Определения

### 3.1 Object

**CMOC Object** — идентифицируемая единица знания, обнаруженная в существующем CMOC и имеющая достаточную структуру для отдельной адресации.

OBJECT INDEX не создаёт объект.

### 3.2 Representation

**Representation** — конкретное представление объекта в CMOC.

Примеры:

- отдельный файл;
- запись внутри реестра;
- иное явно адресуемое представление.

### 3.3 Container

**Container** — физический файл или иной структурный носитель Representation.

Следствие:

> FILE ≠ OBJECT.

Один файл может содержать несколько объектов.

---

## 4. Representation kinds

Минимальный словарь:

- `OBJECT_FILE`
- `REGISTRY_RECORD`
- `OTHER_ADDRESSABLE`

`OTHER_ADDRESSABLE` не используется без фактического обнаружения соответствующего представления.

---

## 5. Модель OBJECT INDEX RECORD

Минимальная структура:

```yaml
schema: CMOC-OBJECT-INDEX-RECORD
version: "0.2"

object_id:
object_type:
object_name:

representation:
  kind:
  container:
  location:

indexed_attributes:
  <attribute>:
    value:
    origin:

structure:
  fields_present:
  sections_present:

provenance:
  repository:
  git_sha:
  inventory_snapshot:

traceability:
  source:
  registry:

discovery:
  basis:

count_basis:
```

---

## 6. Поля

### 6.1 Identity

#### `object_id` — MUST

Явно обнаруженный идентификатор объекта.

Index не должен придумывать ID.

#### `object_type` — MUST

Класс объекта, подтверждённый структурой CMOC.

Неизвестный класс не должен маскироваться под известный.

#### `object_name` — OPTIONAL

Имя объекта, если оно явно обнаружено.

---

## 7. Representation

### `representation` — MUST

#### `kind` — MUST

Одно из обнаруженных representation kinds.

#### `container` — MUST

Путь к физическому контейнеру.

#### `location` — MUST

Адрес внутри контейнера.

Для OBJECT_FILE допустимо:

```yaml
location: FILE
```

Для REGISTRY_RECORD:

```yaml
location:
  record_id: INV-0001
```

Если точная позиция не установлена, используется `UNKNOWN`, а не догадка.

---

## 8. Indexed Attributes

### `indexed_attributes` — OPTIONAL

Это ограниченный набор коротких значений, полезных для навигации и поиска.

Допустимые значения должны быть:

1. явно обнаружены в Representation;
2. механически извлекаемы;
3. ограничены по структуре;
4. полезны для поиска или фильтрации.

Пример:

```yaml
indexed_attributes:
  status:
    value: P0
    origin: FRONTMATTER
  source:
    value: unknown
    origin: FRONTMATTER
  patch:
    value: PATCH-004
    origin: FRONTMATTER
```

### Запрещено

Индексировать как semantic knowledge:

- definition;
- interpretation;
- meaning;
- mechanism;
- semantic summary;
- semantic similarity;
- equivalence;
- conflict;
- reconciliation decision.

---

## 9. Structure

### `structure` — MUST

Фиксирует не смысл, а наличие структурных элементов.

#### `fields_present` — MUST

Список явно обнаруженных полей.

#### `sections_present` — OPTIONAL

Список явно обнаруженных структурных секций.

Пример:

```yaml
structure:
  fields_present:
    - id
    - status
    - source
    - basis
    - tags
  sections_present:
    - Relations
    - Source
```

---

## 10. Provenance

### `provenance` — MUST

#### `repository` — MUST

Источник репозитория.

#### `git_sha` — MUST

Git snapshot, по которому создана индексная запись.

#### `inventory_snapshot` — MUST

Версия Inventory, на основании которого обнаружено представление.

OBJECT INDEX является производным артефактом и не должен маскироваться под первичный источник.

---

## 11. Traceability

### `traceability` — MUST

Контейнер трассировки.

Допустимые элементы:

- `source`
- `registry`

Каждый элемент OPTIONAL.

Если происхождение не установлено:

```yaml
source: UNKNOWN
```

Нельзя заменять отсутствие доказательства догадкой.

---

## 12. Discovery

### `discovery` — OPTIONAL

Техническая информация о том, на основании чего Representation было обнаружено.

Она не является семантической интерпретацией.

---

## 13. Count Basis

### `count_basis` — MUST для агрегированных подсчётов

Фиксирует основание количественного подсчёта.

Минимальные значения:

- `OBJECT_FILE`
- `REGISTRY_RECORD`
- `OTHER_ADDRESSABLE`
- `UNKNOWN`

Это необходимо, чтобы не смешивать:

> количество файлов и количество объектов.

Например:

```
LAB-005 = 1 файл
C-* = множество registry records
```

---

## 14. UNKNOWN

`UNKNOWN` является допустимым результатом наблюдения.

Правило:

> **Неизвестное значение регистрируется как UNKNOWN, а не восстанавливается предположением.**

UNKNOWN не означает ошибку Index.

---

## 15. MUST / OPTIONAL / FORBIDDEN

### MUST

- object_id
- object_type
- representation
- representation.kind
- representation.container
- representation.location
- structure
- structure.fields_present
- provenance
- provenance.repository
- provenance.git_sha
- provenance.inventory_snapshot
- traceability
- count_basis для агрегатов

### OPTIONAL

- object_name
- indexed_attributes
- structure.sections_present
- traceability.source
- traceability.registry
- discovery

### FORBIDDEN

OBJECT INDEX не должен самостоятельно создавать:

- semantic meaning;
- semantic summary;
- semantic equivalence;
- semantic similarity;
- conflict;
- reconciliation decision;
- NEW;
- EXISTING_EQUIVALENT;
- EXISTING_RELATED;
- NEEDS_REVIEW;
- canonicalization decision.

---

## 16. Read-only principle

OBJECT INDEX v0.2 является READ ONLY относительно CMOC.

Создание Index Record:

```
CMOC → INVENTORY → OBJECT INDEX
```

не изменяет:

- исходный объект;
- его статус;
- его содержимое;
- историю;
- отношения;
- канонический статус.

---

## 17. Object Index не является вторым CMOC

Запрещается переносить в Index содержательное знание только ради удобства.

Допускается денормализация ограниченных навигационных атрибутов.

Правило:

> **Если значение необходимо для понимания смысла объекта, оно должно оставаться в CMOC. Если значение необходимо прежде всего для обнаружения и навигации, оно может быть indexed_attribute при наличии явного происхождения.**

---

## 18. Multiple Representations

Модель допускает:

```
OBJECT
 ├── REPRESENTATION 1
 └── REPRESENTATION 2
```

Но наличие нескольких Representation не означает автоматически, что они относятся к одному объекту.

Установление эквивалентности относится к RECONCILIATION, а не к OBJECT INDEX.

---

## 19. Связь с QUERY

QUERY использует OBJECT INDEX как навигационный слой.

```
QUERY
  ↓
OBJECT INDEX
  ↓
candidate addresses
  ↓
CMOC Representation
```

`NO_MATCH` не означает `NEW`.

Недостаточная область проверки должна сохраняться как:

```
SCOPE_INSUFFICIENT
```

в соответствии со SPEC-003.

---

## 20. Связь с RECONCILIATION

RECONCILIATION может использовать OBJECT INDEX для обнаружения существующих объектов и их Representation.

OBJECT INDEX не принимает решение:

```
EXISTING_EQUIVALENT
EXISTING_RELATED
CONFLICT
NEEDS_REVIEW
NEW
```

Эти результаты принадлежат RECONCILIATION.

---

## 21. Связь с INVENTORY

INVENTORY является входным структурным наблюдением для построения OBJECT INDEX.

```
INVENTORY
  ↓
discover addressable representations
  ↓
OBJECT INDEX
```

OBJECT INDEX не должен пересказывать весь Inventory.

Он использует его для построения адресуемой карты.

---

## 22. Что пока НЕ реализуем

На этапе v0.2 не реализуются:

1. semantic embeddings;
2. semantic similarity;
3. LLM-based matching;
4. automatic equivalence;
5. automatic conflict detection;
6. automatic canonicalization;
7. automatic CMOC mutation;
8. CORE UPDATE;
9. automatic inference of missing relations.

Эти функции относятся к следующим производственным слоям.

---

## 23. Главный инвариант

```
CMOC ≠ INVENTORY ≠ OBJECT INDEX ≠ QUERY ≠ RECONCILIATION
```

Их функции различны:

```
INVENTORY
  = physical/structural observation

OBJECT INDEX
  = addressable knowledge map

QUERY
  = retrieval

RECONCILIATION
  = comparison and decision

CMOC
  = accumulated knowledge
```

---

## 24. Критерий готовности v0.2

OBJECT INDEX v0.2 считается реализованным только после проверки на реальных представителях как минимум:

- TERM;
- DISTINCTION;
- GM_FORMULATION;
- MACHINE;
- INVARIANT;
- ORGANIZATIONAL_CONSTRUCTION;
- CHAIN/PATTERN;
- одного неоднозначного или ещё не классифицированного представления.

Для каждого должны быть проверены:

1. Identity;
2. Representation;
3. Structure;
4. Indexed Attributes;
5. Provenance;
6. Traceability;
7. UNKNOWN behavior;
8. отсутствие семантической подмены;
9. корректность count basis.

---

## 25. Архитектурная формула

> **OBJECT INDEX = карта адресуемых представлений накопленного знания, а не само знание.**

Версия: **v0.2 — CONTRACT CANDIDATE**.
