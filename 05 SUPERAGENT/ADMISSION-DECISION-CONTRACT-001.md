# ADMISSION-DECISION-CONTRACT-001

## Статус
CONTRACT CANDIDATE — v0.1

## Назначение

Зафиксировать границу между результатом Reconciliation и последующим решением о дальнейшей судьбе кандидата.

Контракт не выполняет само сопоставление и не выполняет запись в CMOC.

## Положение в цепочке

SOURCE → DISCOVERY → RECONCILIATION_INPUT → QUERY → RECONCILIATION_RESULT → ADMISSION_DECISION → CMOC ADMISSION

## Вход

Единственный основной вход — RECONCILIATION_RESULT.

Решение должно ссылаться на конкретный match_id из результата Reconciliation.

NEEDS_REVIEW не означает NEW и не является решением о включении в CMOC.

## Назначение слоя

Admission Decision отвечает на вопрос:

> Что принято сделать с конкретным результатом сопоставления?

Это отличается от вопроса Reconciliation:

> Что известно о соответствии кандидата существующему CMOC?

## Минимальные поля решения

- decision_id
- match_id
- source_id
- input_batch_id
- decision
- basis
- decided_by
- traceability

## Кандидатные значения decision

На уровне CONTRACT CANDIDATE фиксируются следующие минимальные варианты:

- ADMIT_EXISTING
- ADMIT_NEW
- REJECT
- DEFER

Окончательная семантика и условия применимости этих значений должны быть установлены отдельным решением архитектуры до реализации.

## Границы

Admission Decision:

- не изменяет Discovery Result;
- не изменяет исходные source-bound records;
- не изменяет результат Reconciliation;
- не выполняет скрытое сопоставление;
- не объявляет NEEDS_REVIEW автоматически новым объектом;
- не является записью CMOC;
- не выполняет CMOC admission без отдельного принятого решения/контракта admission.

## Важное различение

EXISTING_EQUIVALENT — результат сопоставления.

ADMIT_EXISTING — решение о дальнейшей судьбе кандидата.

Это разные семантические события и они не должны сливаться в одно состояние.

Аналогично:

NEEDS_REVIEW — результат Reconciliation.

ADMIT_NEW — решение после Review.

## Запрет автоматического вывода

Запрещено преобразование:

NEEDS_REVIEW → ADMIT_NEW

без явного основания, предусмотренного следующим контрактом/правилом принятия решения.

## CMOC boundary

До принятия Admission Decision:

- cmoc_write = NONE
- object_index_write = NONE

Сам факт наличия Admission Decision ещё не означает физическую запись объекта в CMOC. Физический admission является отдельной операцией следующей границы.

## Открытые вопросы

1. Какие типы решений окончательно входят в контракт?
2. Кто/что может быть decided_by: человек, правило, машина?
3. Какие доказательства обязательны для ADMIT_NEW?
4. Какие условия обязательны для ADMIT_EXISTING?
5. Как оформляется конфликт?
6. Какой отдельный контракт управляет физическим CMOC admission?

До ответа на эти вопросы реализация Admission Decision не считается принятой архитектурой.
