# CONTROL-RUN-012 — Contract Reject Test M02→M04 SRC-002 v0.1

**Дата:** 18-09-2026  
**Статус:** CONTROL TEST  
**Machine:** AGENT-SOURCE-001 / MACHINE-SOURCE-001  
**Prompt:** PROMPT-001 v0.3  
**SOURCE:** SRC-002  
**Intent:** проверить отказ цепочки при несовместимом входе следующего TASK.

---

## 1. Гипотеза

Если OUTPUT предыдущего TASK не соответствует INPUT-контракту следующего TASK, оркестратор не должен продолжать цепочку по предположению.

Ожидаемый результат:

`OUTPUT(M02) + TASK(M04) → CONTRACT_MISMATCH → STOP`

---

## 2. Корректные контракты

M02:

`Extraction Record OR SOURCE_PACKAGE` when explicitly contracted  
→ Distinction Record

M04:

`Formulation Records`  
→ Nomenclature Candidates

Следовательно:

`Distinction Record ≠ Formulation Records`

и результат M02 не может быть молча принят M04 как вход.

---

## 3. Тестовый запуск

SOURCE_PACKAGE: SRC-002, страницы 1–5.

M02:

`TASK=M02`

`BATCH=BATCH-SRC-002-TEST-012-M02`

Результат:

`OUTPUT-M02 = Distinction Records`

Следующая операция намеренно задана:

`TASK=M04`

`BATCH=BATCH-SRC-002-TEST-012-M04`

Передача:

`OUTPUT-M02 → INPUT-M04`

---

## 4. Контрактная проверка

M04 требует:

`Formulation Records`

Фактически передано:

`Distinction Records`

Результат проверки:

**CONTRACT_MISMATCH**

Причина:

`INPUT_TYPE(Distinction Record) ≠ REQUIRED_INPUT_TYPE(Formulation Records)`

---

## 5. Ожидаемое поведение

Цепочка должна остановиться.

M04 не должен:

- интерпретировать Distinction как Formulation;
- самостоятельно выполнять отсутствующий M03;
- использовать предыдущий скрытый M03;
- обращаться к SOURCE для неявного восстановления недостающего этапа;
- создавать Nomenclature Candidate.

Допустимый результат:

`M02 OUTPUT → CONTRACT CHECK → REJECT → STOP`

---

## 6. Архитектурный результат

Тест поддерживает принцип:

> Handoff передаёт OUTPUT, но Handoff не отменяет INPUT-контракт следующей MACHINE.

То есть:

`HANDOFF ≠ AUTOMATIC ACCEPTANCE`

и:

`OUTPUT₁ + HANDOFF → CONTRACT CHECK → INPUT₂`

только если контракт совместим.

---

## 7. Evidence boundary

Этот тест проверяет архитектурное правило отрицательного перехода.

Он **не доказывает**:

- универсальную автоматическую проверку всех контрактов;
- корректность всех TASK-CONTRACT;
- автоматический выбор альтернативного маршрута;
- автоматическое восстановление пропущенного TASK.

---

## 8. Expected verdict

**PASS — если оркестратор фиксирует CONTRACT_MISMATCH и останавливает M04 без производства downstream output.**

**FAIL — если M04 принимает Distinction Record, сам достраивает отсутствующий M03 или использует скрытое состояние.**

---

## 9. Следующий шаг

После положительного теста можно формализовать:

`CONTRACT CHECK`

как обязательный orchestration gate между любыми двумя MACHINE.

Связанные документы:

- ARCH-001
- ARCH-002
- INV-001
- STD-008
- TASK-CONTRACT-001
- CONTROL-RUN-011
