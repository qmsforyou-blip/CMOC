# RELATIONS-003 — Full 40-Passport Test — GOST ISO 10002-2007

## Контракт M07
- INPUT: 40 Passport Records
- OUTPUT: Relation Candidates
- CARDINALITY: `40 → 25`
- TASK: `RELATIONS`
- TEST_TYPE: `FULL SEQUENTIAL TEST`

## Relation Candidates

| ID | Source | Relation | Target | Status |
|---|---|---|---|---|
| REL-GOST-001 | Область применимости (`PAS-GOST-003`) | CONSTRAINS | Функции процесса (`PAS-GOST-005`) | PROVISIONAL |
| REL-GOST-002 | Информация из жалоб (`PAS-GOST-004`) | FEEDS | Анализ жалоб (`PAS-GOST-032`) | PROVISIONAL |
| REL-GOST-003 | Информация из жалоб (`PAS-GOST-004`) | FEEDS | Постоянное улучшение (`PAS-GOST-038`) | PROVISIONAL |
| REL-GOST-004 | Интеграция в СМК (`PAS-GOST-006`) | RELATES_TO | Управление записями (`PAS-GOST-031`) | PROVISIONAL |
| REL-GOST-005 | Условия эффективности (`PAS-GOST-008`) | ENABLES | Функции процесса (`PAS-GOST-005`) | PROVISIONAL |
| REL-GOST-006 | Жалоба (`PAS-GOST-010`) | BECOMES_TRACEABLE_THROUGH | Регистрация жалобы (`PAS-GOST-025`) | PROVISIONAL |
| REL-GOST-007 | Удовлетворённость и обратная связь (`PAS-GOST-011`) | IS_MEASURED_BY | Удовлетворённость процессом (`PAS-GOST-033`) | PROVISIONAL |
| REL-GOST-008 | Ответственность в процессе (`PAS-GOST-015`) | APPLIES_TO | Решение и действие (`PAS-GOST-029`) | PROVISIONAL |
| REL-GOST-009 | Обязательства руководства (`PAS-GOST-016`) | ENABLES | Проектирование процесса (`PAS-GOST-023`) | PROVISIONAL |
| REL-GOST-010 | Ответственность высшего руководства (`PAS-GOST-018`) | COVERS | Постоянное улучшение (`PAS-GOST-038`) | PROVISIONAL |
| REL-GOST-011 | Требования к персоналу (`PAS-GOST-021`) | APPLIES_TO | Ответственность в процессе (`PAS-GOST-015`) | PROVISIONAL |
| REL-GOST-012 | Цели и критерии (`PAS-GOST-022`) | GUIDE | Мониторинг процесса (`PAS-GOST-034`) | PROVISIONAL |
| REL-GOST-013 | Информация о процессе (`PAS-GOST-024`) | SUPPORTS | Регистрация жалобы (`PAS-GOST-025`) | PROVISIONAL |
| REL-GOST-014 | Регистрация жалобы (`PAS-GOST-025`) | ENABLES | Прослеживаемость жалобы (`PAS-GOST-026`) | PROVISIONAL |
| REL-GOST-015 | Прослеживаемость жалобы (`PAS-GOST-026`) | EXTENDS_TO | Закрытие жалобы (`PAS-GOST-030`) | PROVISIONAL |
| REL-GOST-016 | Первичная оценка (`PAS-GOST-027`) | GUIDES | Расследование жалобы (`PAS-GOST-028`) | PROVISIONAL |
| REL-GOST-017 | Расследование жалобы (`PAS-GOST-028`) | INFORMS | Решение и действие (`PAS-GOST-029`) | PROVISIONAL |
| REL-GOST-018 | Решение и действие (`PAS-GOST-029`) | PRECEDES | Закрытие жалобы (`PAS-GOST-030`) | PROVISIONAL |
| REL-GOST-019 | Закрытие жалобы (`PAS-GOST-030`) | REQUIRES_RECORD | Управление записями (`PAS-GOST-031`) | PROVISIONAL |
| REL-GOST-020 | Управление записями (`PAS-GOST-031`) | SUPPORTS | Прослеживаемость жалобы (`PAS-GOST-026`) | PROVISIONAL |
| REL-GOST-021 | Анализ жалоб (`PAS-GOST-032`) | SUPPORTS | Постоянное улучшение (`PAS-GOST-038`) | PROVISIONAL |
| REL-GOST-022 | Мониторинг процесса (`PAS-GOST-034`) | FEEDS | Входы рассмотрения руководством (`PAS-GOST-036`) | PROVISIONAL |
| REL-GOST-023 | Аудит процесса (`PAS-GOST-035`) | FEEDS | Входы рассмотрения руководством (`PAS-GOST-036`) | PROVISIONAL |
| REL-GOST-024 | Входы рассмотрения руководством (`PAS-GOST-036`) | INFORMS | Выходы рассмотрения руководством (`PAS-GOST-037`) | PROVISIONAL |
| REL-GOST-025 | Выходы рассмотрения руководством (`PAS-GOST-037`) | SUPPORTS | Постоянное улучшение (`PAS-GOST-038`) | PROVISIONAL |

## Правило

Связь фиксируется только там, где её направление и смысл следуют из материала источника. Наличие паспорта само по себе не создаёт связь. Связи пока `PROVISIONAL` и не являются каноном CMOC.

Трассировка: `SOURCE_ID → BATCH_ID → EX-GOST-nnn → DIS-GOST-nnn → FOR-GOST-nnn → NOM-GOST-nnn → CLS-GOST-nnn → PAS-GOST-nnn → REL-GOST-nnn`.

## QC
- Passport Records received: **40**
- Relation Candidates produced: **25**
- Passport records lost: **0**
- Traceability: **PASS**
- Directionality explicitly recorded: **PASS**
- Relations not asserted merely because objects coexist: **PASS**
- CMOC canonization: **NO**
- New synthesis: **NO**

## Completion

M07 завершён. Из 40 паспортов выделено 25 source-supported relation candidates. Все связи имеют направление и остаются `PROVISIONAL` до M08.

Это `FULL SEQUENTIAL TEST`, а не доказательство автоматического программного прогона.