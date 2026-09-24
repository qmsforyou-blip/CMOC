# INVENTORY-BUILDER-CONTRACT-001 — Контракт восстановления Inventory из Repository

**Status:** CONTRACT CANDIDATE  
**Layer:** SUPERAGENT / INVENTORY  
**Branch:** `work/discovery-result-builder`  
**Purpose:** зафиксировать границу между тем, что доказано существующим CMOC, и тем, что необходимо ввести как новую производственную норму для восстановления Inventory из состояния Repository.

---

## 1. Назначение

`INVENTORY-BUILDER-001` должен преобразовывать структурное состояние репозитория CMOC в детерминированный снимок `CMOC-INVENTORY-001`.

Цепочка:

`CMOC Repository → INVENTORY BUILDER → CMOC-INVENTORY-001 → OBJECT INDEX → QUERY`

Builder является **структурным**, а не семантическим механизмом.

Он не должен:
- извлекать инженерное знание;
- принимать решения о содержательном сходстве объектов;
- канонизировать объекты;
- создавать CMOC-объекты;
- изменять Repository;
- строить OBJECT INDEX;
- выполнять Query.

---

## 2. Что доказано существующим состоянием CMOC (EVIDENCED)

### 2.1. Inventory существует как отдельный артефакт

В репозитории существует:

`05 SUPERAGENT/cmoc_inventory.json`

с контрактом:

- schema: `CMOC-INVENTORY-001`;
- version: `0.1`;
- inventory содержит структурные записи;
- присутствуют `object_counts` и `file_class_counts`.

Исторически snapshot был добавлен отдельным commit `1541ec0e2f46d99eb28b970ce9a159792f7313e1`.

**Не доказано:** каким именно производственным механизмом этот snapshot первоначально был построен.

---

### 2.2. Набор существующих классов

Текущий `build_cmoc_object_index.py` использует следующие классы Inventory:

- `TERM_FILE` → `TERM`
- `DISTINCTION_FILE` → `DISTINCTION`
- `GM_FORMULATION_FILE` → `GM_FORMULATION`
- `MACHINE` → `MACHINE`
- `CHAIN` → `CHAIN`
- `PATTERN` → `PATTERN`
- `LAW` → `LAW`
- `OBSERVATION` → `OBSERVATION`
- `ORGANIZATIONAL_CONSTRUCTION` → `ORGANIZATIONAL_CONSTRUCTION`

В Inventory snapshot также зафиксированы инфраструктурные классы, в частности:

- `MACHINE_RUNTIME`
- `PATCH`
- `STANDARD`
- `SUPERAGENT`
- `CMOC_CORE_REGISTRY`
- `REPOSITORY_OTHER`

Следовательно, Inventory шире, чем набор индексируемых CMOC object types.

---

### 2.3. Существующие правила addressability

В `build_cmoc_object_index.py` зафиксированы следующие идентификаторы и шаблоны:

- `T-\\d{4}`
- `DIS-\\d+`
- `LAB-\\d+`
- `MC-[A-Z0-9-]+`
- `CHAIN-[A-Z0-9-]+`
- `MP-[A-Z0-9-]+`
- `LAW-\\d+`
- `OBS-\\d+`
- `OC-\\d+`

Для object files также используется explicit identity из frontmatter:
- `id`
- `machine_id`
- `chain_id`
- `pattern_id`
- `law_id`
- `observation_id`
- `construction_id`

При невозможности разрешить `object_id` текущий Object Index Builder выдаёт ошибку.

---

### 2.4. Существующие исключения

Текущий Object Index Builder явно исключает:

- `000 База/01 Термины/01 База Термины.base`
- `000 База/02 Различения/02 база различения.base`
- `000 База/02 Различения/Без названия.md`
- `000 База/03 GM-формулировки/03 GM формулировки.base`
- `03_MACHINE-CATALOG/MACHINES/MACHINE-CANDIDATES.md`
- `07 К/LAW/Реестр LAW.md.md`

Эти исключения являются существующей структурной нормой и должны быть учтены Builder'ом.

---

### 2.5. CMOC Core registry — это контейнеры, а не автоматически один объект

Текущий `build_cmoc_object_index.py` отдельно разбирает содержимое CMOC Core registry:

- LAB-000 → записи терминов `T-xxxx`;
- LAB-002 → записи различений `DIS-...`;
- LAB-004 → записи инвариантов;
- LAB-005 → записи организационных конструкций.

Следовательно, нельзя считать:

> один registry-файл = один addressable CMOC object.

Inventory Builder должен различать:

**REGISTRY CONTAINER**  
и  
**REGISTRY RECORD**.

На уровне Inventory фиксируется структурный registry-файл как `CMOC_CORE_REGISTRY`.

Декомпозиция его содержимого на addressable records остаётся ответственностью downstream-механизма Object Index, если отдельный контракт не установит иное.

---

## 3. Что НЕ доказано и не должно быть выдано за существующую норму

Не найден сохранённый production Builder, который первоначально породил `cmoc_inventory.json`.

Поэтому следующие вещи **не являются EVIDENCED**:

1. точный алгоритм классификации каждого файла Repository;
2. точный порядок применения classification rules;
3. точное правило выбора между несколькими возможными классами;
4. точная причина, по которой конкретный файл исторического snapshot получил конкретный класс;
5. существование обязательного `inventory_class` в frontmatter production-объектов;
6. правило `.md = object`;
7. правило, по которому registry records создавались непосредственно Inventory Builder'ом.

---

## 4. Новая производственная норма (NEW PRODUCTION RULE)

Поскольку исторический классификатор не сохранён, новый Builder **не должен притворяться восстановлением старого алгоритма**.

Вводится явная граница:

> **Inventory Builder воспроизводит не исторический алгоритм, а контракт CMOC-INVENTORY-001 по явно версионированным структурным правилам классификации.**

То есть классификация должна быть:

- явной;
- детерминированной;
- проверяемой;
- версионируемой;
- независимой от семантического содержания;
- отдельно тестируемой.

Версия classification rules должна быть частью provenance Inventory.

---

## 5. Минимальная модель Inventory Record

Каждая запись Inventory должна позволять определить как минимум:

- `path`
- `class`
- при наличии — `object_id`
- при наличии — `object_type`
- при необходимости — `source_kind` / structural role
- provenance Builder'а.

Для snapshot должны быть доступны:

- `schema`
- `version`
- `generated_at`
- `repository`
- `branch`
- `source_commit`
- `builder_version`
- `classification_rules_version`

Точный набор полей должен быть закреплён следующим production schema/acceptance test; настоящий контракт не предполагает молча менять исторический JSON.

---

## 6. Правила детерминизма

При одинаковом:

- Repository state;
- source commit;
- classification rules version;
- Builder version;

набор структурных Inventory records должен быть одинаковым.

`generated_at` является metadata provenance и не должен влиять на состав и классификацию записей.

Builder не должен зависеть от:
- порядка обхода файловой системы;
- случайности;
- LLM;
- внешнего semantic search;
- ручного выбора отдельного файла во время выполнения.

---

## 7. Неопределённость классификации

Если файл нельзя однозначно классифицировать по утверждённым структурным правилам, Builder не должен угадывать.

Допустимые исходы должны быть явно определены:

- классифицирован;
- исключён по explicit exclusion;
- инфраструктурный / non-object class;
- unresolved / needs review.

**UNRESOLVED не должен автоматически превращаться в OBJECT.**

---

## 8. Граница ответственности Builder → Object Index

### Inventory Builder

Отвечает за:

`Repository → structural Inventory`

### Object Index Builder

Отвечает за:

`Inventory + repository content → addressable Object Index`

В частности, Object Index уже содержит downstream-логику:

- mapping Inventory class → object type;
- resolution `object_id`;
- parsing отдельных registry records;
- duplicate addressability checks;
- формирование `CMOC-OBJECT-INDEX-001`.

Inventory Builder не должен дублировать эту семантику без отдельного принятого контракта.

---

## 9. Запреты

Inventory Builder не должен:

- создавать файлы объектов;
- изменять существующие паспорта;
- изменять REG;
- изменять LAB;
- изменять CMOC Core;
- изменять Object Index;
- принимать `NEW / EXISTING / REJECT / DEFER`;
- выполнять reconciliation;
- выполнять canonicalization;
- создавать semantic relations;
- считать содержательно похожие файлы одним объектом.

---

## 10. Acceptance criteria для production implementation

Production Builder может считаться принятым только если тесты доказывают:

1. чтение Repository без его изменения;
2. deterministic structural output;
3. корректную классификацию каждого класса, для которого существует утверждённое structural rule;
4. корректное применение explicit exclusions;
5. корректную обработку CMOC Core registry как container;
6. отсутствие автоматического превращения unresolved файла в object;
7. отсутствие semantic/index mutations;
8. наличие provenance:
   - source commit;
   - builder version;
   - classification rules version;
9. совместимость выходного Inventory с текущим `build_cmoc_object_index.py`;
10. отсутствие зависимости от `inventory_class` frontmatter, пока такое правило отдельно не будет принято как production classification rule.

---


## 12. Production rebuild boundary

Для production rebuild вводится отдельная операция:

Repository state → INVENTORY-BUILDER-001 → CMOC-INVENTORY-001 → OBJECT INDEX BUILDER

Production rebuild должен использовать один и тот же зафиксированный Repository state.
Поэтому runner обязан получить и передать в Inventory provenance:

- current branch/state;
- current Git HEAD commit;
- builder version;
- classification rules version.

Если Repository имеет незакоммиченные изменения, runner не должен выдавать такой результат за snapshot конкретного commit. Production rebuild в этом случае останавливается до фиксации состояния.

### 12.1. Derived-output boundary

cmoc_inventory.json и cmoc_object_index.json являются производными артефактами данной цепочки и не должны становиться входными объектами собственного Inventory.

Иначе следующий rebuild изменял бы сам Inventory только потому, что предыдущий Inventory уже существует, а Object Index создавал бы циклическую зависимость.

Поэтому эти пути являются explicit derived-output exclusions для Inventory Builder:

- 05 SUPERAGENT/cmoc_inventory.json
- 05 SUPERAGENT/cmoc_object_index.json

Это структурное исключение, а не semantic classification.

### 12.2. Production rebuild acceptance

Production rebuild считается принятым, если:

1. runner получает branch и HEAD непосредственно из Git;
2. runner останавливается на dirty worktree;
3. Builder не индексирует собственный cmoc_inventory.json;
4. Builder не индексирует производный cmoc_object_index.json;
5. Inventory записывается только после успешного построения;
6. Object Index строится из этого же Inventory;
7. provenance Inventory и Object Index согласован;
8. повторный rebuild на неизменённом commit даёт одинаковый structural Inventory records.

generated_at может изменяться и не считается частью structural identity snapshot.

