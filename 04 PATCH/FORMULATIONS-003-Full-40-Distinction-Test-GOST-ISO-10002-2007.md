# FORMULATIONS-003 — Full 40-Distinction Test: GOST R ISO 10002-2007

## 1. Назначение

Полный последовательный тест M03 машины `MACHINE-SOURCE-001`: преобразование 40 `Distinction Records` из `DISTINCTIONS-003-Full-40-Extraction-Test-GOST-ISO-10002-2007.md` в 120 `Formulation Records`.

Это **FORMULATIONS**, а не канонизация CMOC. Уровень `CANONICAL_FORM` означает только третью формулировку объекта внутри M03 и не означает `CANONICAL` в смысле CMOC.

## 2. Вход

- `SOURCE_ID`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_ID`: `BATCH-SRC-GOST-ISO-10002-2007`
- Input: 40 `Distinction Records` `DIS-GOST-001` … `DIS-GOST-040`
- Source: `ГОСТ Р ИСО 10002-2007 Менеджмент организации. Удовлетворенность потребителя`
- Input status: `ПРОВЕРЕН`

## 3. Правило M03

Для каждого Distinction Record производятся ровно три формулировки:

1. `INTUITIVE` — понятная смысловая формулировка.
2. `ENGINEERING` — формулировка как инженерного различения.
3. `CANONICAL_FORM` — сжатая третья формулировка; **не CMOC canon**.

Запрещено на этом проходе: добавлять знания от себя, выполнять классификацию, создавать паспорта, отношения или CMOC-канон.

## 4. Formulation Records

### FOR-GOST-001-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-001`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Процесс работы с жалобами — это руководство, а не сертификационное требование.

### FOR-GOST-001-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-001`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Руководство по работе с жалобами задает рекомендации по процессу и не устанавливает требований к сертификации.

### FOR-GOST-001-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-001`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Процесс работы с жалобами: РУКОВОДСТВО ≠ СЕРТИФИКАЦИОННЫЕ ТРЕБОВАНИЯ.

### FOR-GOST-002-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-002`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Стандарт имеет национальное обозначение и одновременно идентифицирует международный документ ISO.

### FOR-GOST-002-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-002`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Обозначение национального стандарта и его связь с ISO являются различными характеристиками идентификации документа.

### FOR-GOST-002-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-002`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Идентификация документа: НАЦИОНАЛЬНОЕ ОБОЗНАЧЕНИЕ ≠ МЕЖДУНАРОДНАЯ ИДЕНТИЧНОСТЬ ISO.

### FOR-GOST-003-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-003`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Процесс жалоб можно применять и в коммерческой, и в некоммерческой деятельности.

### FOR-GOST-003-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-003`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Область применения процесса работы с жалобами не ограничена коммерческими организациями.

### FOR-GOST-003-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-003`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Применимость процесса: КОММЕРЧЕСКАЯ ДЕЯТЕЛЬНОСТЬ + НЕКОММЕРЧЕСКАЯ ДЕЯТЕЛЬНОСТЬ.

### FOR-GOST-004-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-004`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Жалобы дают информацию, которую можно использовать для улучшений.

### FOR-GOST-004-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-004`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Результаты рассмотрения жалоб могут использоваться как вход для действий по улучшению.

### FOR-GOST-004-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-004`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Жалоба → ИНФОРМАЦИЯ ДЛЯ УЛУЧШЕНИЯ.

### FOR-GOST-005-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-005`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Работа с жалобами нужна и для решения конкретной жалобы, и для системного улучшения.

### FOR-GOST-005-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-005`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Процесс имеет два различимых результата применения: разрешение конкретной жалобы и использование информации для улучшения.

### FOR-GOST-005-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-005`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Процесс жалоб: РАЗРЕШЕНИЕ ЖАЛОБЫ + СИСТЕМНОЕ УЛУЧШЕНИЕ.

### FOR-GOST-006-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-006`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Процесс жалоб может быть частью СМК или самостоятельным и не служит процессом сертификации.

### FOR-GOST-006-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-006`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Статус процесса в СМК может быть встроенным или самостоятельным; функция сертификации ему не приписывается.

### FOR-GOST-006-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-006`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Статус процесса: ЭЛЕМЕНТ СМК ИЛИ САМОСТОЯТЕЛЬНЫЙ ПРОЦЕСС; НЕ СЕРТИФИКАЦИЯ.

### FOR-GOST-007-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-007`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Процесс охватывает весь жизненный цикл: от планирования до улучшения.

### FOR-GOST-007-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-007`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Процесс работы с жалобами связан с этапами планирования, разработки, производства, обслуживания и улучшения.

### FOR-GOST-007-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-007`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Охват процесса: ПЛАНИРОВАНИЕ → РАЗРАБОТКА → ПРОИЗВОДСТВО → ОБСЛУЖИВАНИЕ → УЛУЧШЕНИЕ.

### FOR-GOST-008-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-008`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Результативность процесса зависит от ориентации на потребителя, руководства, ресурсов, анализа, аудита и оценки.

### FOR-GOST-008-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-008`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Для оценки результативности процесса предусмотрены взаимосвязанные управленческие условия: ориентация на потребителя, руководство, ресурсы, анализ, аудит и оценка.

### FOR-GOST-008-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-008`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Результативность процесса: ОРИЕНТАЦИЯ НА ПОТРЕБИТЕЛЯ + РУКОВОДСТВО + РЕСУРСЫ + АНАЛИЗ + АУДИТ + ОЦЕНКА.

### FOR-GOST-009-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-009`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Заявитель, потребитель, жалоба, удовлетворенность, обслуживание и обратная связь — не одно и то же.

### FOR-GOST-009-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-009`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Определения ролей и терминов в процессе требуют различать заявителя и потребителя и не смешивать жалобу, удовлетворенность, обслуживание и обратную связь.

### FOR-GOST-009-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-009`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Терминология процесса: ЗАЯВИТЕЛЬ ≠ ПОТРЕБИТЕЛЬ; ЖАЛОБА ≠ УДОВЛЕТВОРЕННОСТЬ ≠ ОБРАТНАЯ СВЯЗЬ.

### FOR-GOST-010-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-010`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Жалоба предполагает ожидание ответа или решения, поэтому отличается от простой неудовлетворенности.

### FOR-GOST-010-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-010`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Критерием отличия жалобы от неудовлетворенности является ожидание ответа или решения.

### FOR-GOST-010-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-010`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Жалоба = НЕУДОВЛЕТВОРЕННОСТЬ + ОЖИДАНИЕ ОТВЕТА/РЕШЕНИЯ.

### FOR-GOST-011-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-011`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Удовлетворенность и обратная связь — разные понятия.

### FOR-GOST-011-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-011`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Удовлетворенность описывает восприятие выполнения требований, тогда как обратная связь представляет собой комментарии, сведения или экспертизу.

### FOR-GOST-011-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-011`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Удовлетворенность ≠ обратная связь.

### FOR-GOST-012-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-012`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Цель, политика и процесс выполняют разные функции в управлении.

### FOR-GOST-012-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-012`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Цель задает намерение, политика — направление, процесс — взаимосвязанные действия, преобразующие входы в выходы.

### FOR-GOST-012-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-012`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** ЦЕЛЬ ≠ ПОЛИТИКА ≠ ПРОЦЕСС.

### FOR-GOST-013-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-013`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Доступный процесс должен быть видимым, понятным и показывать ход работы.

### FOR-GOST-013-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-013`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Доступность процесса обеспечивается видимостью, понятным порядком и информированием о продвижении жалобы.

### FOR-GOST-013-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-013`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Доступность процесса: ВИДИМОСТЬ + ПОНЯТНЫЙ ПОРЯДОК + ИНФОРМАЦИЯ О ХОДЕ.

### FOR-GOST-014-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-014`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** В процессе отдельно различимы объективность, бесплатность, конфиденциальность, ориентация на потребителя, ответственность и улучшение.

### FOR-GOST-014-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-014`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Принципы процесса должны рассматриваться как отдельные условия: объективность, отсутствие платы, конфиденциальность, ориентация на потребителя, ответственность и улучшение.

### FOR-GOST-014-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-014`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Принципы процесса: ОБЪЕКТИВНОСТЬ + БЕСПЛАТНОСТЬ + КОНФИДЕНЦИАЛЬНОСТЬ + ОРИЕНТАЦИЯ НА ПОТРЕБИТЕЛЯ + ОТВЕТСТВЕННОСТЬ + УЛУЧШЕНИЕ.

### FOR-GOST-015-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-015`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Ответственность касается действий и решений и должна сопровождаться отчетностью.

### FOR-GOST-015-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-015`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Для действий и решений должна быть назначена ответственность и установлен способ отчетности.

### FOR-GOST-015-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-015`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Ответственность: ДЕЙСТВИЯ + РЕШЕНИЯ + ОТЧЕТНОСТЬ.

### FOR-GOST-016-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-016`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Руководство отвечает не только за операции, но и за ресурсы и обучение.

### FOR-GOST-016-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-016`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Обязательства руководства проявляются, в частности, в обеспечении ресурсов и обучения, а не только в выполнении операций.

### FOR-GOST-016-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-016`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Обязательства руководства: РЕСУРСЫ + ОБУЧЕНИЕ, а не только операции.

### FOR-GOST-017-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-017`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Политика не равна процедурам и целям.

### FOR-GOST-017-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-017`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Политика задает направление; процедуры описывают порядок; цели задают измеримые ориентиры.

### FOR-GOST-017-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-017`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Политика ≠ процедуры ≠ цели.

### FOR-GOST-018-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-018`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Высшее руководство несет ответственность за процесс на протяжении его жизненного цикла.

### FOR-GOST-018-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-018`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Ответственность высшего руководства распространяется на процесс на всем его жизненном цикле.

### FOR-GOST-018-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-018`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Высшее руководство: ОТВЕТСТВЕННОСТЬ ЗА ПРОЦЕСС НА ВСЕМ ЖИЗНЕННОМ ЦИКЛЕ.

### FOR-GOST-019-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-019`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Представитель руководства является отдельным носителем ответственности.

### FOR-GOST-019-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-019`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Представитель руководства является выделенным носителем определенной ответственности за процесс.

### FOR-GOST-019-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-019`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Представитель руководства: ОТДЕЛЬНЫЙ НОСИТЕЛЬ ОТВЕТСТВЕННОСТИ.

### FOR-GOST-020-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-020`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Руководители подразделений отвечают за внедрение, записи, действия и анализ данных.

### FOR-GOST-020-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-020`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Ответственность руководителей подразделений включает внедрение, управление записями, действия и анализ данных.

### FOR-GOST-020-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-020`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Руководители подразделений: ВНЕДРЕНИЕ + ЗАПИСИ + ДЕЙСТВИЯ + АНАЛИЗ ДАННЫХ.

### FOR-GOST-021-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-021`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Персоналу нужны обучение, определенные роли, ответственность и полномочия.

### FOR-GOST-021-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-021`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Подготовленность персонала поддерживается обучением и ясным распределением ролей, ответственности и полномочий.

### FOR-GOST-021-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-021`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Персонал: ОБУЧЕНИЕ + РОЛЬ + ОТВЕТСТВЕННОСТЬ + ПОЛНОМОЧИЯ.

### FOR-GOST-022-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-022`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Цели процесса должны быть измеримыми и согласованными с политикой и критериями.

### FOR-GOST-022-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-022`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Цели должны иметь измеримость, соответствовать политике и опираться на критерии.

### FOR-GOST-022-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-022`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Цели: ИЗМЕРИМОСТЬ + СОГЛАСОВАННОСТЬ + КРИТЕРИИ.

### FOR-GOST-023-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-023`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Процесс проектируется вместе с ресурсами и связями с другими процессами СМК.

### FOR-GOST-023-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-023`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** При проектировании процесса одновременно определяются необходимые ресурсы и связи с другими процессами СМК.

### FOR-GOST-023-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-023`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Проектирование процесса: ПРОЦЕСС + РЕСУРСЫ + СВЯЗИ С ПРОЦЕССАМИ СМК.

### FOR-GOST-024-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-024`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Информация о процессе сама является объектом управления.

### FOR-GOST-024-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-024`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Информация, необходимая для работы процесса, должна быть доступной и управляемой.

### FOR-GOST-024-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-024`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Информация процесса: УПРАВЛЯЕМЫЙ ЭЛЕМЕНТ.

### FOR-GOST-025-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-025`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Каждая поступившая жалоба получает регистрацию, уникальный идентификатор и необходимые атрибуты.

### FOR-GOST-025-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-025`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Регистрация превращает поступившую жалобу в прослеживаемый объект с уникальным идентификатором и атрибутами.

### FOR-GOST-025-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-025`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Жалоба: РЕГИСТРАЦИЯ + УНИКАЛЬНЫЙ ID + АТРИБУТЫ → ПРОСЛЕЖИВАЕМЫЙ ОБЪЕКТ.

### FOR-GOST-026-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-026`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Нужно прослеживать жалобу от получения до закрытия, а первоначальную оценку проводить отдельно.

### FOR-GOST-026-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-026`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Трасса жалобы должна сохраняться от получения до закрытия; первоначальная оценка является отдельной операцией.

### FOR-GOST-026-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-026`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Прослеживаемость: ПОЛУЧЕНИЕ → ПЕРВОНАЧАЛЬНАЯ ОЦЕНКА → РАССЛЕДОВАНИЕ → ОТВЕТ → ЗАКРЫТИЕ.

### FOR-GOST-027-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-027`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Расследование должно быть по масштабу соразмерно значимости жалобы.

### FOR-GOST-027-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-027`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Масштаб расследования определяется важностью, частотой и серьезностью жалобы и связан с подготовкой ответа.

### FOR-GOST-027-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-027`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Расследование: МАСШТАБ ∝ ВАЖНОСТЬ + ЧАСТОТА + СЕРЬЕЗНОСТЬ.

### FOR-GOST-028-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-028`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Решение и действие различаются; заявителя информируют, а при несогласии жалоба остается открытой.

### FOR-GOST-028-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-028`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Решение и действие фиксируются раздельно; результат сообщается заявителю; несогласие препятствует закрытию.

### FOR-GOST-028-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-028`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Решение ≠ действие; ИНФОРМИРОВАНИЕ; НЕСОГЛАСИЕ → ОТКРЫТЫЙ СТАТУС.

### FOR-GOST-029-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-029`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Закрытие означает выполнение и регистрацию; без согласия процесс остается открытым.

### FOR-GOST-029-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-029`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Закрытие связывает выполненное действие с его регистрацией; при отсутствии согласия статус остается открытым.

### FOR-GOST-029-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-029`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Закрытие: ВЫПОЛНЕНИЕ + РЕГИСТРАЦИЯ; НЕСОГЛАСИЕ → ОТКРЫТЫЙ СТАТУС.

### FOR-GOST-030-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-030`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Записями нужно управлять по установленным правилам жизненного цикла.

### FOR-GOST-030-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-030`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Жизненный цикл записи включает идентификацию, сбор, классификацию, хранение, передачу и уничтожение по установленным правилам.

### FOR-GOST-030-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-030`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Записи: ИДЕНТИФИКАЦИЯ → СБОР → КЛАССИФИКАЦИЯ → ХРАНЕНИЕ → ПЕРЕДАЧА → УНИЧТОЖЕНИЕ.

### FOR-GOST-031-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-031`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Анализ жалоб должен выявлять повторяемость, тенденции и коренные причины.

### FOR-GOST-031-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-031`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Анализ должен различать повторные и единичные случаи и выявлять тенденции и коренные причины.

### FOR-GOST-031-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-031`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Анализ жалоб: ПОВТОРЯЕМОСТЬ + ТЕНДЕНЦИИ + КОРЕННЫЕ ПРИЧИНЫ.

### FOR-GOST-032-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-032`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Удовлетворенность жалобой/процессом и удовлетворенность продуктом — разные вещи.

### FOR-GOST-032-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-032`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Оценка удовлетворенности процессом работы с жалобами не заменяет оценку удовлетворенности продуктом.

### FOR-GOST-032-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-032`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Удовлетворенность процессом жалоб ≠ удовлетворенность продуктом.

### FOR-GOST-033-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-033`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Мониторинг выполняется по заранее установленным критериям и охватывает процесс, ресурсы и данные.

### FOR-GOST-033-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-033`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Критерии мониторинга задаются заранее и применяются к процессу, ресурсам и данным.

### FOR-GOST-033-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-033`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Мониторинг: КРИТЕРИИ + ПРОЦЕСС + РЕСУРСЫ + ДАННЫЕ.

### FOR-GOST-034-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-034`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Аудит проверяет соответствие и пригодность процедуры и требует компетентности и независимости.

### FOR-GOST-034-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-034`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Аудит одновременно проверяет соответствие процедуры и ее пригодность для целей; исполнители аудита должны быть компетентными и независимыми.

### FOR-GOST-034-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-034`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Аудит: СООТВЕТСТВИЕ + ПРИГОДНОСТЬ; КОМПЕТЕНТНОСТЬ + НЕЗАВИСИМОСТЬ.

### FOR-GOST-035-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-035`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** При анализе руководства рассматриваются изменения, данные, аудиты, корректирующие действия и рекомендации.

### FOR-GOST-035-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-035`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Входы анализа руководства включают изменения, данные процесса, результаты аудитов, корректирующие действия и рекомендации.

### FOR-GOST-035-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-035`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Анализ руководства: ИЗМЕНЕНИЯ + ДАННЫЕ + АУДИТЫ + КОРРЕКТИРУЮЩИЕ ДЕЙСТВИЯ + РЕКОМЕНДАЦИИ.

### FOR-GOST-036-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-036`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Результатом анализа руководства становятся решения, действия и записи.

### FOR-GOST-036-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-036`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Выходы анализа руководства включают решения и действия относительно процесса, продукта и ресурсов, а также записи.

### FOR-GOST-036-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-036`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Выходы анализа руководства: РЕШЕНИЯ + ДЕЙСТВИЯ + ЗАПИСИ.

### FOR-GOST-037-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-037`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Постоянное улучшение включает устранение причин и развитие/инновации.

### FOR-GOST-037-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-037`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Улучшение строится на устранении коренных причин и может включать развитие и инновации.

### FOR-GOST-037-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-037`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Улучшение: УСТРАНЕНИЕ КОРЕННЫХ ПРИЧИН + РАЗВИТИЕ/ИННОВАЦИИ.

### FOR-GOST-038-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-038`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Малое предприятие может соразмерять масштаб и ресурсы процесса своим условиям.

### FOR-GOST-038-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-038`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Для малого бизнеса требования к масштабу и ресурсам процесса реализуются с учетом его условий.

### FOR-GOST-038-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-038`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Малый бизнес: МАСШТАБ + РЕСУРСЫ СООБРАЗНЫ УСЛОВИЯМ.

### FOR-GOST-039-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-039`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Форма жалобы фиксирует основные данные о заявителе, продукте, проблеме, ответе, дате и подписи.

### FOR-GOST-039-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-039`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Форма жалобы обеспечивает фиксацию идентификационных и содержательных данных, необходимых для ее рассмотрения и ответа.

### FOR-GOST-039-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-039`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Форма жалобы: ЗАЯВИТЕЛЬ + ПРОДУКТ + ПРОБЛЕМА + СПОСОБ ОТВЕТА + ДАТА + ПОДПИСЬ.

### FOR-GOST-040-INTUITIVE

- `DISTINCTION_REF`: `DIS-GOST-040`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `INTUITIVE`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Мониторинг опирается на измеряемые показатели сроков, статусов, повторных жалоб, улучшений и действий.

### FOR-GOST-040-ENGINEERING

- `DISTINCTION_REF`: `DIS-GOST-040`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `ENGINEERING`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Измеряемые данные мониторинга позволяют отслеживать сроки, статусы, повторяемость жалоб, улучшения и результативность действий.

### FOR-GOST-040-CANONICAL_FORM

- `DISTINCTION_REF`: `DIS-GOST-040`
- `SOURCE_REF`: `SRC-GOST-ISO-10002-2007-001`
- `BATCH_REF`: `BATCH-SRC-GOST-ISO-10002-2007`
- `FORMULATION_TYPE`: `CANONICAL_FORM`
- `STATUS`: `ПРОВЕРЕН`

**Формулировка:** Мониторинг: СРОКИ + СТАТУСЫ + ПОВТОРНЫЕ ЖАЛОБЫ + УЛУЧШЕНИЯ + РЕЗУЛЬТАТИВНОСТЬ ДЕЙСТВИЙ.

## 5. Контроль завершения

| Показатель | Результат |
|---|---:|
| Distinction Records получено | 40 |
| Formulation Records произведено | 120 |
| Формулировок на Distinction | 3 |
| `INTUITIVE` | 40 |
| `ENGINEERING` | 40 |
| `CANONICAL_FORM` | 40 |
| Непроработано | 0 |
| Потеря входных Distinctions | 0 |
| CMOC-канонизация | НЕТ |
| Синтез нового знания | НЕТ |

## 6. Трассировка

`SOURCE_ID → BATCH_ID → EX-GOST-nnn → DIS-GOST-nnn → FOR-GOST-nnn-TYPE`

## 7. Результат теста

**M03 PASS — 40 → 120.** Для каждого из 40 проверенных Distinction Records произведены три формулировки. Кардинальность выдержана полностью. Тест является полным последовательным/interface-тестом, а не доказательством автоматизированного программного запуска.

Дата: 17-09-2026
