# SPEC-003 — CMOC QUERY Interface v0.1

## 1. Назначение
SPEC-003 определяет минимальный интерфейс, через который RECONCILIATION получает данные из ядра CMOC для сопоставления с результатами DISCOVERY.
CMOC QUERY — это интерфейс чтения и поиска. Он не изменяет ядро.

## 2. Принцип
RECONCILIATION → CMOC QUERY → QUERY RESULT → MATCH / DECISION
RECONCILIATION не должна читать произвольное содержимое репозитория без заданного scope.

## 3. Вход запроса
Минимальная форма: QUERY_ID, QUERY_TYPE, TARGET_OBJECT_TYPE, QUERY_VALUE, QUERY_SCOPE, REQUESTED_FIELDS.
QUERY_TYPE на MVP: EXACT, ALIAS, STRUCTURAL, CANDIDATE.

## 4. TARGET_OBJECT_TYPE
Минимально: TERM / NOMENCLATURE; DISTINCTION; FORMULATION; CLASSIFICATION; PASSPORT; RELATION; CANON.

## 5. QUERY_SCOPE
Scope должен быть явным. Примеры: TERMS; DISTINCTIONS; TERMS + DISTINCTIONS; FULL CMOC READABLE INDEX.
Если scope не позволяет сделать вывод, результат не должен автоматически классифицироваться как NEW.

## 6. EXACT
Цель — найти точное совпадение идентификатора, имени или нормализованной строки.
EXACT возвращает MATCH или NO_MATCH. EXACT не доказывает эквивалентность смысла, если совпадение основано только на строке.

## 7. ALIAS
Цель — проверить известные альтернативные обозначения объекта. Результат: MATCH или NO_MATCH. Найденный alias должен иметь собственную трассировку к объекту CMOC.

## 8. STRUCTURAL
Цель — сравнить структурные признаки объекта. Минимальные признаки: object type; class; relation pattern; required fields; lifecycle status; epistemic status.
STRUCTURAL MATCH является кандидатом на сопоставление и не означает автоматическую эквивалентность.

## 9. CANDIDATE
Используется, когда точного или структурного совпадения недостаточно и требуется сформировать набор объектов для последующей проверки. Результат: CANDIDATE_SET. Он передаётся RECONCILIATION, а не считается решением.

## 10. Query Result
Минимальная форма: QUERY_ID, OBJECT_ID, OBJECT_TYPE, MATCH_MODE, MATCH_STATUS, MATCH_BASIS, OBJECT_STATUS, TRACEABILITY.
MATCH_STATUS: MATCH; NO_MATCH; CANDIDATE; AMBIGUOUS; SCOPE_INSUFFICIENT.

## 11. Правило NEW
NO_MATCH ≠ автоматически NEW.
Для вывода NEW должны быть выполнены: необходимый QUERY_SCOPE задан; предусмотренные scope query modes выполнены; получен NO_MATCH; отсутствует известный alias/equivalent candidate в проверенном scope.
Иначе: SCOPE_INSUFFICIENT или NEEDS_REVIEW.

## 12. Дубликаты
Если Discovery выдаёт FAST_RESPONSE, а QUERY находит существующий объект, RECONCILIATION может подготовить EXISTING_EQUIVALENT.
Исходный Discovery Record не удаляется.

## 13. Конфликт
Если QUERY выявляет несовместимые существующие основания, формируется CONFLICT CANDIDATE. QUERY только обнаруживает и возвращает материал для решения.
Разрешение конфликта относится к RECONCILIATION/операторскому решению.

## 14. Read-only boundary
CMOC QUERY читает, ищет, возвращает кандидатов и evidence/traceability.
CMOC QUERY не создаёт canonical objects, не удаляет объекты, не переписывает историю, не разрешает конфликты и не меняет статусы.

## 15. Минимальный MVP
Первый исполнимый вариант должен поддерживать EXACT → ALIAS → STRUCTURAL → CANDIDATE и возвращать MATCH, NO_MATCH, CANDIDATE, AMBIGUOUS, SCOPE_INSUFFICIENT.

## 16. Архитектурное место
CMOC CORE / INDEX ← CMOC QUERY ← RECONCILIATION ← DISCOVERY OUTPUT

## Evidence boundary
SPEC-003 является спецификацией интерфейса. Runtime CMOC QUERY ещё не реализован и не прошёл контрольный прогон.