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

Admission фиксирует принятую связь source candidate с существующим CMOC object через Admission record, содержащий `target CMOC object` и полную traceability.

Не создаётся второй объект только потому, что пришёл новый source record.

Если DECISION не разрешает отдельное изменение существующего объекта, `cmoc_write = NONE` и `object_index_write = NONE`.

### ADMIT_NEW

Реализация решения создаёт новый CMOC object в соответствии с действующим контрактом объекта.

Создание нового объекта должно сохранять происхождение от source candidate и DECISION.

Для `ADMIT_NEW` Admission разрешает отдельный pipeline физического создания объекта; текущая реализация этого pipeline остаётся C1 → C2/P7 → C3/P8.

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

Для `ADMIT_EXISTING`:

DECISION
→ ADMISSION RECORD
→ существующий CMOC OBJECT

Для `ADMIT_NEW`:

DECISION
→ ADMISSION
→ C1
→ C2/P7
→ C3/P8

Для `REJECT/DEFER`:

DECISION
→ ADMISSION RECORD
→ без CMOC write

## Открытые вопросы

1. Какой контракт определяет физический формат CMOC object для `ADMIT_NEW`?
2. Где выполняется канонизация внутри `ADMIT_NEW` pipeline?
3. Как обновляется OBJECT INDEX после создания нового объекта?
4. Требуется ли отдельный контракт для `UPDATE_EXISTING`?
5. Как обеспечивается идемпотентность Admission?
6. Что является успешным результатом ADMISSION?

Для `ADMIT_EXISTING` физическая форма минимально определена: идемпотентный Admission record с `target CMOC object` и traceability.

Для `ADMIT_NEW` Admission остаётся контрактной границей до реализации и acceptance runtime pipeline.
