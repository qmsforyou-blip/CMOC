# WORK-PLAN — A5 NEW SOURCE

**ID:** WORK-PLAN-A5-NEW-SOURCE-001  
**Дата:** 20-09-2026  
**Статус:** ACTIVE  
**Область:** CMOC / MACHINE-SOURCE-001 / SUPERAGENT  
**Основание:** WORK-PLAN-DISCOVERY-RECONCILIATION-001 / A4 CLOSED

## 1. Цель

Провести первый контролируемый проход **нового SOURCE** после закрытия A4.

A5 должен проверить сохранение архитектурной границы на новом источнике:

```
NEW SOURCE
    ↓
SOURCE_PACKAGE
    ↓
MACHINE-SOURCE-001
    ↓
M01 → M02 → M03 → M04 → M05 → M06 → M07 → M08
    ↓
DISCOVERY RESULT
    ↓
RECONCILIATION
    ↓
CMOC
```

> **Новый SOURCE сначала добывается независимо. Только после получения DISCOVERY RESULT выполняется RECONCILIATION.**

## 2. STOP-GATE перед запуском

До создания production run должны быть определены:
- SOURCE_ID;
- SOURCE_NAME;
- SOURCE_TYPE;
- SOURCE_VERSION, если известна;
- SOURCE_PACKAGE_ID;
- состав SOURCE_PACKAGE;
- статус COMPLETE / PARTIAL / UNKNOWN;
- scope источника;
- TASK;
- RUN_ID;
- expected traceability.

Не допускается запускать A5 с неформализованным источником.

## 3. Выбор нового SOURCE

### Предварительное направление

Рассматривается:
**ISO/DIS 9001:2025(E)**

Однако это пока **кандидат источника**, а не утверждённый SOURCE.

Существующие результаты предыдущей ISO-добычи не являются входом A5.

## 4. SOURCE_PACKAGE

Минимальный пакет:

```
source_package:
  package_id:
  source_id:
  source_name:
  source_type:
  source_version:
  source_package_status:
  work_scope:
  fragments:
    - location:
      text:
```

### Правило

SOURCE_PACKAGE — логическая единица входа.

## 5. A5.1 — SOURCE isolation

Проверить, что новый DISCOVERY pass получает только SOURCE_PACKAGE и не использует накопленный CMOC как скрытый источник.

**STOP-GATE A5.1:** DISCOVERY input определяется только SOURCE_PACKAGE и контрактом TASK.

## 6. A5.2 — DISCOVERY RESULT

Выполняется полный production pass M01 → M02 → M03 → M04 → M05 → M06 → M07 → M08.

Формируется DISCOVERY_RESULT с трассировкой SOURCE → SOURCE_PACKAGE → RUN → BATCH → M01...M08 → DISCOVERY_RESULT.

**STOP-GATE A5.2:** полный production pass завершён, результат трассируем и отделён от RECONCILIATION.

## 7. A5.3 — RECONCILIATION

Только после фиксации DISCOVERY RESULT выполняется downstream RECONCILIATION через CMOC / OBJECT INDEX / QUERY.

Контролируемые свойства:
- Discovery result не изменяется;
- QUERY работает только downstream;
- CMOC используется только downstream;
- MATCH не переписывает source-derived value;
- NO_MATCH не означает NEW;
- AMBIGUOUS приводит к NEEDS_REVIEW;
- structural candidate не становится автоматически equivalent.

**STOP-GATE A5.3:** RECONCILIATION завершён без мутации DISCOVERY RESULT.

## 8. A5.4 — Evidence

После A5.1–A5.3 создать EVIDENCE-A5-NEW-SOURCE-001.md с SOURCE identity, SOURCE_PACKAGE identity, RUN_ID, BATCH lineage, M01–M08 results, DISCOVERY_RESULT, RECONCILIATION result и ограничениями эксперимента.

## 9. Запреты A5

До закрытия A5:
- не добавлять CMOC lookup внутрь M01–M08;
- не использовать старый Discovery output как input нового Discovery;
- не смешивать старые ISO results с новым SOURCE_PACKAGE;
- не считать совпадение термина доказательством equivalence;
- не считать NO_MATCH доказательством NEW;
- не изменять DISCOVERY RESULT после RECONCILIATION.

## 10. Definition of Done

A5 считается закрытым, когда:
- [ ] новый SOURCE формально идентифицирован;
- [ ] SOURCE_PACKAGE создан;
- [ ] A5.1 SOURCE isolation пройден;
- [ ] A5.2 полный M01–M08 production pass пройден;
- [ ] DISCOVERY_RESULT зафиксирован;
- [ ] A5.3 RECONCILIATION выполнен downstream;
- [ ] DISCOVERY RESULT не изменён;
- [ ] Evidence создан;
- [ ] ограничения зафиксированы;
- [ ] WORK-PLAN-DISCOVERY-RECONCILIATION-001 синхронизирован.

## 11. Текущий статус

```
A4 — CLOSED
 ↓
A5 — ACTIVE
 ↓
A5.1 — WAITING FOR SOURCE
```

Следующая операция — **утвердить конкретный SOURCE и собрать SOURCE_PACKAGE**.

До этого production run не запускается.