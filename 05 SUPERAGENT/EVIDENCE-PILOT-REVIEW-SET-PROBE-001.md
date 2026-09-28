# EVIDENCE — Pilot human review set verification

**Извещение на изменение:** `0231+280926`  
**Названия файлов:** `05 SUPERAGENT/pilot_001_review_set_probe.py`, `05 SUPERAGENT/test_pilot_001_review_set_probe.py`, `05 SUPERAGENT/EVIDENCE-PILOT-REVIEW-SET-PROBE-001.md`  
**Дата:** 28-09-2026  
**Статус:** read-only проверка набора решений; не завершение RUN

## Architecture lookup

Существующие `pilot_001_record_review.py` и `DecisionStore` сохраняют отдельные решения человека. `runtime_state_store.py` имеет событие `HUMAN_DECISION_RECORDED`, переводящее `WAITING_HUMAN_REVIEW` в `ACTIVE`, но поштучная запись намеренно не посылает событие, пока есть другие записи для review. `pilot_001_orchestration.py` останавливается на `HUMAN_REVIEW_REQUIRED`. Проверка полного множества `match_id` без движения RUN отсутствовала. Новый скрипт дополняет эту границу, не дублируя DecisionStore и не вводя semantic decision.

## Реализация и проверка

`pilot_001_review_set_probe.py` открывает SQLite с `mode=ro`, читает сохранённый Reconciliation и проекцию RUN, сопоставляет каждый ожидаемый `match_id` с JSON-решением в папке RUN, проверяет идентификаторы, source/package/reconciliation/passport/batch lineage и обязательные поля HUMAN. Обнаруживает отсутствующие и посторонние/некорректные файлы. Выдаёт `REVIEW_SET_INCOMPLETE`, `REVIEW_SET_INVALID`, `REVIEW_SET_COMPLETE_NO_ADMISSION` или `REVIEW_SET_COMPLETE_ADMISSION_PENDING`.

Локально выполнен `python3 test_pilot_001_review_set_probe.py`: `PASS`. Проверены пустой и частичный набор, два решения `DEFER/REJECT`, несовпадающий SOURCE, оборванная lineage, посторонний файл и набор с `ADMIT_NEW`. Байты тестовой SQLite до и после проверки совпали. Компиляция обоих скриптов прошла.

## Граница

`REVIEW_SET_COMPLETE_NO_ADMISSION` означает только полноту и структурную согласованность сохранённых решений относительно конкретного Reconciliation. Это не переводит RUN в `COMPLETED`, не посылает `HUMAN_DECISION_RECORDED`, не подтверждает семантическую обоснованность решений и не создаёт Admission. `REVIEW_SET_COMPLETE_ADMISSION_PENDING` также не является разрешением физической записи: для `ADMIT_NEW/EXISTING` нужны отдельные контрактные проверки. На момент первой фиксации живые базы RUN-001…007 ещё не проверялись этим скриптом; ниже приведён последующий живой результат RUN-007.

## Живое свидетельство RUN-007

**Извещение на изменение:** `0232+280926`  
**Название файла:** `05 SUPERAGENT/EVIDENCE-PILOT-REVIEW-SET-PROBE-001.md`

После fast-forward ветки пользователь выполнил probe на `pilot_007.sqlite`. Результат: `REVIEW_SET_COMPLETE_NO_ADMISSION`, `expected_count=4`, `decision_count=4`, `decision_results={DEFER:3, REJECT:1}`, `missing_match_ids=[]`, `errors=[]`. Проекция RUN остаётся `WAITING_HUMAN_REVIEW`. Команда не вызывала LLM и не писала в журнал/CMOC/индекс. Этим доказана read-only проверка комплектности **одного живого набора**; не доказаны агрегированное завершение RUN и физический Admission.

## Проверка шести живых наборов

**Извещение на изменение:** `0233+280926`  
**Название файла:** `05 SUPERAGENT/EVIDENCE-PILOT-REVIEW-SET-PROBE-001.md`

Пользователь выполнил тот же read-only probe на ещё пяти сохранённых базах. Все результаты — `REVIEW_SET_COMPLETE_NO_ADMISSION`, `missing_match_ids=[]`, `errors=[]`, `run_status=WAITING_HUMAN_REVIEW`.

| RUN | Ожидалось / найдено | DEFER | REJECT |
|---|---:|---:|---:|
| PILOT-001 SRC-002 | 6 / 6 | 6 | 0 |
| PILOT-002 SRC-004 | 2 / 2 | 2 | 0 |
| PILOT-003 SRC-005 | 4 / 4 | 4 | 0 |
| PILOT-005 SRC-005-WHOLE | 5 / 5 | 4 | 1 |
| PILOT-006 SRC-002-ASSIGNMENT | 2 / 2 | 1 | 1 |
| PILOT-007 SRC-002-PERFORMANCE | 4 / 4 | 3 | 1 |
| **Всего** | **23 / 23** | **20** | **3** |

Доказана структурная комплектность решений относительно сохранённых Reconciliation во всех шести живых RUN. Никакое решение о `NEW`, Admission или CMOC write из этой сводки не следует. Поскольку скрипт не посылает событие в журнал, все шесть RUN корректно сохраняют `WAITING_HUMAN_REVIEW`; термин `REVIEW_SET_COMPLETE` относится к набору JSON решений, а не к жизненному циклу RUN.
