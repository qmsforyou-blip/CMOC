# AUTOMATED-RUN-001 — M07 Relations

**Input:** AUTOMATED-RUN-001-M06-PASSPORT.md only  
**Output:** Relation Records  
**Purpose:** automated generation of source-bound semantic relations from passports.

## CONTRACT

- Input: 40 Passport Records.
- Operation: identify explicitly supported functional/semantic relations among the passported objects.
- Output: Relation Records.
- No prior Run A/B M07 relations are used as input.
- Relations are generated from PAS-AUTO passports only.
- No CMOC Canon is introduced.
- Relation status is `ПРОВЕРЕН` as a production artifact; epistemic canonization is not performed.
- Endpoint identity must remain traceable to Passport IDs.

## RELATION RECORDS

| ID | Source | Relation | Target |
|---|---|---|---|
| REL-AUTO-001 | Область применимости процесса жалоб | CONSTRAINS | Функции процесса работы с жалобами |
| REL-AUTO-002 | Информация из жалоб | FEEDS | Анализ жалоб |
| REL-AUTO-003 | Информация из жалоб | FEEDS | Постоянное улучшение |
| REL-AUTO-004 | Интеграция процесса в СМК | RELATES_TO | Управление записями |
| REL-AUTO-005 | Условия эффективности процесса | ENABLES | Функции процесса работы с жалобами |
| REL-AUTO-006 | Жалоба | BECOMES_TRACEABLE_THROUGH | Регистрация жалобы |
| REL-AUTO-007 | Удовлетворённость и обратная связь | IS_MEASURED_BY | Удовлетворённость процессом жалоб |
| REL-AUTO-008 | Ответственность в процессе | APPLIES_TO | Решение и действие по жалобе |
| REL-AUTO-009 | Обязательства руководства | ENABLES | Проектирование процесса |
| REL-AUTO-010 | Ответственность высшего руководства | COVERS | Постоянное улучшение |
| REL-AUTO-011 | Требования к персоналу процесса | APPLIES_TO | Ответственность в процессе |
| REL-AUTO-012 | Цели и критерии процесса | GUIDE | Мониторинг процесса |
| REL-AUTO-013 | Информация о процессе | SUPPORTS | Регистрация жалобы |
| REL-AUTO-014 | Регистрация жалобы | ENABLES | Прослеживаемость жалобы |
| REL-AUTO-015 | Прослеживаемость жалобы | EXTENDS_TO | Закрытие жалобы |
| REL-AUTO-016 | Первоначальная оценка жалобы | GUIDES | Расследование жалобы |
| REL-AUTO-017 | Расследование жалобы | INFORMS | Решение и действие по жалобе |
| REL-AUTO-018 | Решение и действие по жалобе | PRECEDES | Закрытие жалобы |
| REL-AUTO-019 | Закрытие жалобы | REQUIRES_RECORD | Управление записями |
| REL-AUTO-020 | Управление записями | SUPPORTS | Прослеживаемость жалобы |
| REL-AUTO-021 | Анализ жалоб | SUPPORTS | Постоянное улучшение |
| REL-AUTO-022 | Мониторинг процесса | FEEDS | Входы рассмотрения руководством |
| REL-AUTO-023 | Аудит процесса | FEEDS | Входы рассмотрения руководством |
| REL-AUTO-024 | Входы рассмотрения руководством | INFORMS | Выходы рассмотрения руководством |
| REL-AUTO-025 | Выходы рассмотрения руководством | SUPPORTS | Постоянное улучшение |

## TRACE

Each relation endpoint is identified by its Passport Record and therefore traces through the complete production lineage:

**RELATION → PASSPORT(source/target) → CLASSIFICATION → NOMENCLATURE → FORMULATION → DISTINCTION → EXTRACTION → BATCH → SOURCE**

## QC

- Input passports: 40
- Passports used: 40
- Output relations: 25
- Unprocessed passports: 0
- Relation endpoints mapped to Passport IDs: 50/50
- Relation status: ПРОВЕРЕН
- Prior Run A/B M07 relations used as input: NO
- Manual reconstruction: NO
- Classification fields added: 0
- New passport objects: 0
- Canonization: NONE
- Endpoint traceability: PASS
- Stage boundary: PASS

## RESULT

**PASS** — M07 automated relation stage completed. 25 source-bound relations were produced from the automated M06 passports with complete endpoint traceability and without canonization.
