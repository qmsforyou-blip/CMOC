# MVP-SUPERAGENT-001 — Минимальный суперагент обработки Источников v0.1

**Дата:** 18-09-2026  
**Статус:** MVP DESIGN  
**Основание:** INV-001, INV-002, ARCH-001, ARCH-002, STD-007, SPEC-002, PROMPT-001, TASK-CONTRACT-001 v0.2.

---

## 1. Цель MVP

Собрать минимально работающий суперагент, который не содержит знания конкретного Источника, а исполняет уже определённые MACHINE/TASK по явным контрактам.

MVP должен доказать практическую цепочку:

SOURCE_PACKAGE → TASK → MACHINE → BATCH → OUTPUT → QC → HANDOFF.

---

## 2. Что входит в MVP

В первую версию входят только:

1. приём SOURCE_PACKAGE;
2. приём TASK;
3. проверка обязательных параметров;
4. выбор соответствующей MACHINE;
5. создание BATCH_ID;
6. выполнение одного TASK;
7. структурированный OUTPUT;
8. CONTRACT CHECK перед следующим TASK;
9. ACCEPT / REJECT;
10. явный HANDOFF;
11. журнал прохода.

Не входят:

- автоматический выбор оптимальной цепочки;
- автоматическая канонизация;
- самостоятельное изменение машин;
- самостоятельное изменение CMOC;
- скрытая память между проходами;
- универсальная семантическая проверка.

---

## 3. Минимальный вход

SOURCE_ID  
SOURCE_NAME  
SOURCE_TYPE  
SOURCE_VERSION  
SOURCE_PACKAGE  
SOURCE_PACKAGE_STATUS  
TASK  
BATCH_ID  
INPUT

BATCH_ID создаётся для нового прохода, если не передан существующий Batch в рамках разрешённого продолжения.

---

## 4. Dispatcher

Суперагент сначала определяет:

SOURCE / TASK / INPUT / MACHINE / CONTRACT / BATCH.

Он не выполняет производственную операцию сам, если для неё существует MACHINE.

Логика:

получить TASK → найти TASK CONTRACT → определить допустимый INPUT → выбрать MACHINE → создать/проверить BATCH → EXECUTE.

---

## 5. Contract Gate №1 — до выполнения

Проверить:

- TASK задан;
- MACHINE существует;
- контракт TASK известен;
- INPUT разрешён контрактом;
- SOURCE_PACKAGE доступен, если он требуется;
- обязательные поля присутствуют;
- traceability может быть сохранена.

Если проверка не пройдена:

REJECT + REASON + NO OUTPUT.

---

## 6. Production

После ACCEPT машина выполняет ровно один назначенный TASK.

Она не должна:

- самостоятельно переходить к следующему TASK;
- использовать скрытый предыдущий результат;
- изменять SOURCE;
- изменять TASK;
- канонизировать результат без соответствующего задания.

---

## 7. Contract Gate №2 — после выполнения

Проверить OUTPUT:

- тип;
- обязательные поля;
- статус;
- traceability;
- соответствие выходу TASK CONTRACT.

Если OUTPUT не проходит проверку:

QC_FAIL / CONTRACT_FAIL + REASON + CHAIN STOP.

---

## 8. Handoff Gate

Если следующий TASK задан:

OUTPUT₁ → DECLARED HANDOFF → CONTRACT CHECK → ACCEPT → INPUT₂.

Без явного HANDOFF предыдущий OUTPUT не становится автоматически INPUT следующей машины.

---

## 9. Reject

Минимальный объект отказа:

STATUS: REJECT  
REASON:  
FAILED_GATE:  
CURRENT_BATCH:  
SOURCE_ID:  
TASK:  
INPUT:  
NEXT_ACTION:

NEXT_ACTION не должен содержать самостоятельно придуманное производственное решение. Допустимы:

- REQUEST_MISSING_INPUT;
- REQUEST_CONTRACT;
- RETURN_TO_PREVIOUS_TASK;
- HUMAN_REVIEW;
- STOP.

---

## 10. Journal

Каждый проход оставляет запись:

RUN_ID  
SOURCE_ID  
TASK  
MACHINE_ID  
BATCH_ID  
INPUT_REFERENCE  
OUTPUT_REFERENCE  
STATUS  
QC_RESULT  
HANDOFF_RESULT  
REASON

Журнал должен позволять восстановить:

что запускалось → на каком Источнике → какой машиной → с каким TASK → каким Batch → какой результат получен → почему цепочка продолжилась или остановилась.

---

## 11. Первый MVP-маршрут

Использовать уже доказанный маршрут:

SRC-002 → M01 EXTRACTION → M02 DISTINCTIONS → M03 FORMULATIONS.

На первом запуске не добавлять M04–M08.

Причина: MVP должен проверять оркестрацию на уже наиболее устойчивом участке, а не одновременно расширять evidence boundary.

---

## 12. Acceptance Test

MVP считается рабочим, если один и тот же суперагент:

### Test 1 — sequential

самостоятельно выполняет M01 → M02 → M03 с явными Batch и Handoff.

### Test 2 — reject

пытается передать несовместимый OUTPUT в следующий TASK и получает:

CONTRACT_MISMATCH → STOP.

### Test 3 — missing field

получает OUTPUT правильного типа, но с отсутствующим обязательным полем и не принимает его автоматически.

### Test 4 — trace

после цепочки восстанавливается путь:

OUTPUT → BATCH → TASK → SOURCE.

### Test 5 — source swap

тот же суперагент запускается с другим SOURCE_PACKAGE без изменения его базовой логики.

---

## 13. Definition of Done

- [ ] единый входной интерфейс;
- [ ] TASK dispatcher;
- [ ] MACHINE selection;
- [ ] BATCH creation;
- [ ] pre-execution Contract Gate;
- [ ] TASK execution;
- [ ] post-execution QC Gate;
- [ ] explicit HANDOFF;
- [ ] reject path;
- [ ] journal;
- [ ] Test 1 PASS;
- [ ] Test 2 PASS;
- [ ] Test 3 PASS;
- [ ] Test 4 PASS;
- [ ] Test 5 PASS.

---

## 14. Архитектурное ограничение MVP

MVP не должен становиться новым монолитным PROMPT.

Правило:

> Суперагент оркестрирует существующие машины; он не поглощает их.

SUPERAGENT
├── MACHINE
├── TASK CONTRACT
├── SOURCE INTERFACE
├── BATCH
├── QC
└── HANDOFF

---

## 15. Следующий производственный шаг

Не писать ещё один слой теории.

Создать первый исполняемый control prompt / runner для:

SRC-002 → M01 → M02 → M03

и прогнать его как MVP CONTROL-RUN-001.

После запуска изменения в архитектуру вносить только по обнаруженным отказам.
