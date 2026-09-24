# CMOC-ADMISSION-CONTRACT-001

## Статус
CONTRACT CANDIDATE — v0.1

## Назначение

Зафиксировать границу, на которой принятое DECISION превращается в физически сохраняемый объект CMOC.

## Положение в цепочке

RECONCILIATION_RESULT
→ DECISION
→ ADMISSION
→ CMOC OBJECT
→ OBJECT INDEX

## Главный принцип

ADMISSION — не новое решение.

ADMISSION реализует уже принятое DECISION в пределах отдельного контракта.

Связь:

DECISION → разрешает ADMISSION

ADMISSION → физически реализует решение

DECISION ≠ ADMISSION

## Вход

Основной вход:

- конкретный DECISION;
- ссылка на исходный match_id;
- traceability к RECONCILIATION_RESULT;
- исходный кандидат и его source lineage;
- решение, разрешающее admission.

## Допустимые варианты

### ADMIT_EXISTING

Реализация решения заключается в установлении/сохранении связи кандидата с уже существующим CMOC object.

Не создаётся второй объект только потому, что пришёл новый source record.

### ADMIT_NEW

Реализация решения создаёт новый CMOC object в соответствии с действующим контрактом объекта.

Создание нового объекта должно сохранять происхождение от source candidate и DECISION.

### REJECT

REJECT не создаёт и не изменяет CMOC object.

### DEFER

DEFER не создаёт CMOC object.

## Обязательные свойства Admission

Admission должен сохранять:

- admission_id;
- decision_id;
- match_id;
- source_id;
- source lineage;
- admission_result;
- target CMOC object, если он существует;
- timestamp;
- traceability.

## CMOC write boundary

Именно Admission является первой границей, на которой разрешается:

- cmoc_write;
- object creation;
- object update, если это разрешено конкретным DECISION;
- последующее обновление OBJECT INDEX.

До Admission:

cmoc_write = NONE

object_index_write = NONE

## Защита от двойного создания

ADMIT_NEW не должен приводить к созданию второго CMOC объекта при повторном выполнении того же Admission.

Admission должен иметь идентичность и быть идемпотентным либо явно обнаруживать уже выполненное admission.

## Канонизация

Этот контракт не утверждает, что Admission сам выполняет канонизацию.

Если для создания CMOC object требуется канонизация, она должна быть отдельной явно определённой операцией/контрактом внутри admission pipeline.

Нельзя скрывать канонизацию внутри физической записи.

## OBJECT INDEX

После успешного создания или изменения CMOC object соответствующий OBJECT INDEX должен быть приведён в согласованное состояние отдельным определённым шагом.

Admission не должен молча изменять индекс без фиксируемого результата операции.

## Запрещено

Admission не должен:

- менять DECISION;
- менять RECONCILIATION_RESULT;
- повторно выполнять Reconciliation;
- придумывать новый объект без ADMIT_NEW;
- превращать NEEDS_REVIEW непосредственно в объект;
- создавать CMOC object для REJECT или DEFER;
- скрывать semantic inference внутри записи.

## Минимальная цепочка

DECISION
→ ADMISSION
→ CMOC OBJECT
→ OBJECT INDEX

## Открытые вопросы

1. Какой контракт определяет физический формат CMOC object?
2. Где выполняется канонизация?
3. Как обновляется OBJECT INDEX?
4. Как обрабатывается конфликт при ADMIT_EXISTING?
5. Как обеспечивается идемпотентность Admission?
6. Что является успешным результатом ADMISSION?

До ответа на эти вопросы CMOC Admission остаётся контрактной границей, а не реализованным runtime-компонентом.
