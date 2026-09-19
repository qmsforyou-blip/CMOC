# SPEC-005 — CMOC QUERY v0.3

**Дата:** 19-09-2026  
**Статус:** DESIGN / CONTRACT CANDIDATE  
**Назначение:** исполнимый контракт слоя QUERY поверх CMOC OBJECT INDEX v0.2.

---

## 1. Назначение

QUERY предоставляет RECONCILIATION и другим потребителям read-only интерфейс поиска по адресуемым представлениям CMOC.

QUERY не добывает объекты повторно из INVENTORY и не является вторым INVENTORY.

> **QUERY v0.3 читает карту OBJECT INDEX; он не строит её заново.**

Архитектурная цепочка:

CMOC → INVENTORY → OBJECT INDEX v0.2 → QUERY v0.3 → RECONCILIATION → ASSEMBLY

## 2. Граница QUERY

QUERY отвечает на вопрос: какие индексированные представления удовлетворяют заданному условию поиска в заданном scope?

QUERY:
- принимает запрос;
- проверяет scope;
- ищет по OBJECT INDEX;
- возвращает найденные записи и их адреса;
- возвращает evidence/traceability, уже присутствующие в INDEX;
- фиксирует режим и основание совпадения.

QUERY не:
- создаёт объекты;
- изменяет CMOC;
- изменяет OBJECT INDEX;
- создаёт aliases;
- устанавливает эквивалентность;
- устанавливает конфликт;
- принимает решение NEW;
- принимает решение EXISTING_EQUIVALENT;
- принимает решение EXISTING_RELATED;
- принимает решение NEEDS_REVIEW;
- выполняет canonicalization.

## 3. Источник данных

Единственный нормативный источник QUERY v0.3:

05 SUPERAGENT/cmoc_object_index.json

QUERY не должен извлекать object_id, object_name или другие признаки непосредственно из имени файла, если соответствующая запись отсутствует в OBJECT INDEX.

QUERY не должен повторять логику INVENTORY.

QUERY не должен самостоятельно классифицировать физические файлы.

## 4. Входной запрос

Минимальная форма:

    query_id:
    query_type:
    target_object_type:
    query_value:
    query_scope:
    requested_fields:

query_id — MUST. Уникальный идентификатор запроса в пределах вызывающей операции.

query_type — MUST. MVP поддерживает EXACT, ALIAS, STRUCTURAL, CANDIDATE.

target_object_type — OPTIONAL. Ограничение поиска по object_type. Значение должно соответствовать фактически присутствующему в OBJECT INDEX типу.

query_value — MUST. Значение, заданное вызывающей стороной в соответствии с query_type.

query_scope — MUST. Явно заданная область поиска.

requested_fields — OPTIONAL. Запрашиваемые поля результата. Если поле отсутствует в OBJECT INDEX, QUERY не должен восстанавливать его из догадки.

## 5. Scope

Scope является частью доказательства результата.

Если заданный scope не покрывает необходимую область поиска, результат — SCOPE_INSUFFICIENT.

> **Неполный поиск не является доказательством отсутствия объекта.**

Следовательно: NO_MATCH ≠ NEW.

## 6. Индексируемые поисковые признаки

QUERY v0.3 имеет право использовать только признаки, фактически представленные в OBJECT INDEX.

Базовый набор:
- object_id;
- object_type;
- object_name, если он присутствует;
- indexed_attributes, если они присутствуют;
- structure.fields_present;
- structure.sections_present;
- representation.kind;
- representation.container;
- representation.location;
- значения traceability/provenance в пределах предусмотренного запроса.

QUERY не извлекает новый смысл из содержимого объекта.

## 7. EXACT

Назначение: найти точное индексированное представление по идентификатору или явно индексированному имени.

Минимальные варианты:
1. точное совпадение object_id;
2. точное совпадение object_name, если имя присутствует;
3. точное совпадение другого явно разрешённого indexed attribute.

EXACT не доказывает семантическую эквивалентность.

Результаты: MATCH, NO_MATCH, AMBIGUOUS, SCOPE_INSUFFICIENT.

## 8. ALIAS

Назначение: найти объект по уже зарегистрированному альтернативному обозначению.

> **QUERY v0.3 не создаёт alias и не выводит alias из текста.**

Если alias отсутствует в OBJECT INDEX как явно индексированное значение, QUERY не имеет права считать его alias.

При отсутствии зарегистрированного alias: NO_MATCH либо SCOPE_INSUFFICIENT.

## 9. STRUCTURAL

STRUCTURAL работает только по структурным признакам, реально присутствующим в OBJECT INDEX.

Минимальные признаки v0.3:
- object_type;
- наличие конкретного поля в structure.fields_present;
- наличие конкретной секции в structure.sections_present;
- representation.kind;
- явно индексированные атрибуты.

STRUCTURAL не имеет права самостоятельно извлекать смысл, определение, механизм, семантическое сходство, эквивалентность или конфликт.

Результат структурного совпадения — CANDIDATE, а не EXISTING_EQUIVALENT.

## 10. CANDIDATE

CANDIDATE предназначен для формирования множества возможных объектов для последующей проверки.

QUERY может использовать только индексированные признаки, явно доступные в OBJECT INDEX.

CANDIDATE не является решением RECONCILIATION.

## 11. Match Status

| MATCH_STATUS | Значение |
|---|---|
| MATCH | найдено соответствие заданному поисковому условию |
| NO_MATCH | в проверенном scope соответствие не найдено |
| CANDIDATE | найден кандидат для последующей проверки |
| AMBIGUOUS | найдено несколько допустимых результатов без основания выбрать один |
| SCOPE_INSUFFICIENT | заданная область поиска недостаточна |

QUERY не использует NEW, EXISTING_EQUIVALENT, EXISTING_RELATED, NEEDS_REVIEW или CONFLICT как собственные результаты.

## 12. Query Result

Минимальная форма:

    query_id:
    match_status:
    match_basis:
    scope_checked:
    results:
      - object_id:
        object_type:
        match_mode:
        match_status:
        match_basis:
        object_status:
        representation:
        traceability:

Результат должен позволять определить: какой запрос выполнялся; какой scope был проверен; какой объект найден; каким режимом найден; на каком индексированном признаке основано совпадение; где находится Representation; откуда происходит индексированная запись.

## 13. Representation в результате

QUERY возвращает адрес из OBJECT INDEX без изменения.

Для OBJECT_FILE: location = FILE.

Для REGISTRY_RECORD QUERY сохраняет record_id и физический адрес, включая line, если он присутствует в INDEX.

QUERY не меняет адрес и не объединяет разные физические Representation.

## 14. Duplicate Object IDs

QUERY обязан учитывать, что object_id не равен unique physical representation.

Один object_id может иметь несколько Representation.

QUERY не должен автоматически схлопывать результаты только потому, что у них одинаковый object_id.

Пример: DIS-0155 → LAB-002 / line 1473 и DIS-0155 → LAB-002 / line 1501. Обе Representation должны оставаться адресуемыми.

## 15. UNKNOWN

QUERY не заменяет UNKNOWN восстановленным значением.

Если OBJECT INDEX содержит отсутствие object_name, QUERY не должен получать имя из текста, предположения, похожего объекта или другого Representation без установленного основания.

UNKNOWN является валидным состоянием.

## 16. Traceability

QUERY только передаёт трассировку, присутствующую в OBJECT INDEX.

Минимально сохраняются provenance.repository, provenance.git_sha, provenance.inventory_snapshot, traceability и адрес Representation.

QUERY не создаёт новую семантическую трассировку.

## 17. Правило NO_MATCH

NO_MATCH означает только: в данном query scope и при данном query mode соответствующее индексированное представление не найдено.

Это не означает NEW и не означает, что объекта не существует.

Для такого вывода требуется RECONCILIATION и достаточная область проверки.

## 18. Read-only boundary

QUERY v0.3 является READ ONLY.

Запрещены операции create, update, delete, merge, rename, canonicalize, status change, alias registration, relation creation.

QUERY только читает OBJECT INDEX и возвращает результат.

## 19. Запрет повторной добычи

QUERY v0.3 не должен содержать механизмов: прочитать Inventory → найти файл → угадать object_id из filename → построить object.

Правильная последовательность: OBJECT INDEX → filter/match → candidate representations → QUERY RESULT.

## 20. MVP v0.3

Первая реализация QUERY v0.3 должна поддерживать:
1. загрузку cmoc_object_index.json;
2. явный query scope;
3. EXACT;
4. ALIAS только по явно индексированному alias;
5. STRUCTURAL по индексированной структуре;
6. CANDIDATE;
7. MATCH;
8. NO_MATCH;
9. CANDIDATE;
10. AMBIGUOUS;
11. SCOPE_INSUFFICIENT;
12. полную traceability;
13. сохранение отдельных Representation при одинаковом object_id.

## 21. Acceptance Tests

Q-001 — EXACT TERM: object_type = TERM, object_id = T-0001 → MATCH.

Q-002 — EXACT DISTINCTION: object_id = DIS-000001 → MATCH.

Q-003 — duplicate representation: запрос по DIS-0155 должен сохранить обе физические Representation.

Q-004 — UNKNOWN: запрос к INV-0009 не должен получать имя, которого нет в INDEX.

Q-005 — SCOPE_INSUFFICIENT: запрос MACHINE при scope TERMS → SCOPE_INSUFFICIENT.

Q-006 — NO_MATCH: отсутствующий идентификатор TERM-NOT-IN-CMOC → NO_MATCH; QUERY не создаёт NEW.

Q-007 — STRUCTURAL: поиск по реально существующему структурному признаку при недостаточном основании для точного MATCH → CANDIDATE.

Q-008 — read-only: после выполнения запросов OBJECT INDEX и CMOC не изменены, новые object_id не созданы.

## 22. Главный инвариант

> **QUERY не добывает знание. QUERY извлекает адресуемые представления из уже построенной карты OBJECT INDEX.**

QUERY = retrieval
OBJECT INDEX = address map
RECONCILIATION = comparison + decision

## 23. Связь со SPEC-003

SPEC-003 задаёт концептуальный интерфейс QUERY.

SPEC-005 переводит этот интерфейс на фактическую архитектуру OBJECT INDEX v0.2.

SPEC-005 не отменяет SPEC-003; он конкретизирует его для исполнимого MVP.

## 24. Что НЕ реализуем в v0.3

Не реализуются: embeddings; LLM semantic search; semantic equivalence; automatic reconciliation; automatic conflict resolution; automatic NEW; automatic canonicalization; CMOC mutation; inference of missing relations; самостоятельная добыча объектов из CMOC.

## 25. Критерий готовности

QUERY v0.3 принимается только если OBJECT INDEX v0.2 → QUERY v0.3 → all acceptance tests GREEN → RECONCILIATION can consume QUERY RESULT.

При этом QUERY не должен содержать логики принятия решений RECONCILIATION.

---

**Версия:** v0.3 — CONTRACT CANDIDATE.