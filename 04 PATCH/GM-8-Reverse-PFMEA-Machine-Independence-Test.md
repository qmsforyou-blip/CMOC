# GM QSB — Reverse PFMEA — Machine Independence Test

**Notice:** 0145+170926

## 1. Purpose

Проверить, сохраняет ли структура Machine `Reverse PFMEA` свою идентичность при удалении доменных терминов PFMEA / RPN / Failure Mode и переносе в другой operational domain.

Это тест независимости Machine abstraction, не канонизация.

Исходная рабочая структура Reverse PFMEA:

`EXPECTED FAILURE / CONTROL STATE → ACTUAL STATION → EVIDENCE → GAP → FINDING → ACTION → VERIFY`

Тестовая замена домена: **maintenance / equipment control**.

---

## 2. Domain-neutral reconstruction

Вместо PFMEA задаём другой accepted representation:

**EXPECTED EQUIPMENT CONTROL STATE**

Например:

- требуемый статус защитного устройства;
- требуемый режим смазки;
- требуемая настройка параметра;
- требуемый статус preventive-maintenance control;
- требуемый результат контрольной проверки.

Realized object:

**ACTUAL EQUIPMENT / ACTUAL STATION STATE**

Evidence:

- непосредственное наблюдение;
- измерение;
- запись maintenance;
- результат функциональной проверки;
- диагностический тест.

Comparison:

**EXPECTED → ACTUAL → EVIDENCE → GAP**

Finding:

- отсутствующий контроль;
- контроль существует, но не работает;
- фактическое состояние отличается от требуемого;
- обнаружен ранее не предусмотренный режим отказа / проблема.

Action:

- зарегистрировать finding;
- назначить owner;
- определить срок;
- выполнить corrective / preventive action.

Verify:

- повторно проверить фактическое состояние;
- подтвердить устранение gap;
- при необходимости пересмотреть accepted control state.

Таким образом сохраняется та же архитектурная грамматика:

`EXPECTED STATE → REALIZED STATE → EVIDENCE → GAP → FINDING → ACTION → VERIFY`

---

## 3. Blind test — maintenance example

### Scenario

Для оборудования существует установленное требование:

> защитное устройство должно находиться в рабочем состоянии и проходить функциональную проверку по установленному графику.

### Machine execution

`S0 READY`
→ оборудование и критерий проверки доступны

`S1 REVIEW CONTROL`
→ проверяется конкретный maintenance control

`S2 CONTROL EXISTENCE CHECK`
→ предусмотрена ли требуемая проверка?

`S3 CONTROL EFFECTIVENESS CHECK`
→ реально ли защитное устройство и сама проверка работают?

`S4 EVIDENCE VALIDATION`
→ подтверждается ли состояние наблюдением / измерением / записью?

`S5 NEXT CONTROL`
→ переход к следующему контролю

`S6 NEW GAP / FAILURE DISCOVERY`
→ контролируемая проверка выявляет ранее не предусмотренную проблему

`S7 FINDING / ACTION`
→ результат фиксируется, назначаются owner и срок

`S8 HANDOFF / CLOSE`
→ результат передаётся в maintenance / equipment-management mechanism

Все ключевые операционные состояния Reverse PFMEA сохранились без использования PFMEA, RPN и production Failure Mode как обязательных терминов.

---

## 4. Independence criteria

Machine считается независимой от исходного домена, если сохраняются одновременно:

1. **accepted expected state** — существует внешне заданное состояние/критерий;
2. **realized state** — имеется конкретный объект/процесс, подлежащий проверке;
3. **evidence generation** — Machine получает фактические свидетельства;
4. **comparison** — evidence сопоставляется с expected state;
5. **local gap decision** — определяется наличие отклонения / новой информации;
6. **finding formation** — результат превращается в traceable finding;
7. **action handoff** — инициируется последующее действие, но его полное выполнение не принадлежит Machine;
8. **re-verification** — результат действия может быть повторно проверен;
9. **same execution boundary** — Machine сохраняет автономную последовательность `review → verify → find → record → handoff`.

### Result

**PASS.**

Все девять критериев выполняются в maintenance / equipment-control domain.

---

## 5. What exactly transferred

Перенеслось не название `Reverse PFMEA` и не набор PFMEA-терминов.

Перенеслась более абстрактная Machine structure:

> **Проверка реализованного состояния объекта/процесса относительно принятого ожидаемого состояния с формированием проверяемого finding и передачей его в механизм последующего действия.**

Рабочее domain-neutral имя кандидата:

**Expected-vs-Actual Control Verification / Проверка фактического состояния относительно требуемого контроля**

или, короче:

**Control Verification Review / Проверка работоспособности контроля**

Это пока candidate abstraction, не каноническое имя.

---

## 6. Important boundary finding

Тест показал важное различие между:

### Domain realization

`Reverse PFMEA`

— специализированная реализация структуры в domain process-risk / PFMEA.

### Machine abstraction

`Expected-vs-Actual Control Verification`

— переносимая структура исполнения.

То есть более точная архитектура может быть представлена так:

`PATTERN`

`Risk Model Feedback Loop`

↓

`MACHINE ABSTRACTION`

`Expected-vs-Actual Control Verification`

↓

`DOMAIN MACHINE`

`Reverse PFMEA`

↓

`ASSEMBLY`

`Risk Reduction / PFMEA Management`

Это не означает, что новый Machine abstraction уже должен быть внесён в Catalog. Требуется дополнительная проверка на других domains.

---

## 7. Negative independence test

Проверяем, не является ли структура слишком общей и не теряет ли она Machine boundary.

### A. Simple audit

`CRITERION → OBSERVE → RECORD`

**FAIL** — отсутствует обязательная consequential action / handoff и re-verification.

### B. Monitoring

`OBSERVE → STATUS`

**FAIL** — нет explicit comparison-to-expected и finding/action boundary.

### C. Corrective Action

`GAP → ACTION → VERIFY`

**FAIL** как полная Machine — отсутствует собственная проверочная стадия формирования gap из actual-vs-expected evidence.

### D. Maintenance inspection

`EXPECTED CONTROL → ACTUAL EQUIPMENT → EVIDENCE → GAP → FINDING → ACTION → VERIFY`

**PASS** — сохраняется вся execution boundary.

Следовательно, abstraction не сводится к любому аудиту, мониторингу или corrective action.

---

## 8. Architectural result

### Independence Test

**PASS**

Reverse PFMEA не является уникальной структурой, полностью привязанной к PFMEA.

При переносе в maintenance / equipment-control сохраняются:

- expected-state reference;
- actual-state observation;
- evidence;
- comparison;
- gap/new information;
- finding;
- action handoff;
- verification;
- внешняя граница ownership downstream action.

Поэтому Reverse PFMEA следует рассматривать как **domain-specific Machine realization** более абстрактной Machine structure.

### Stronger hypothesis

> **Machine identity определяется не предметной терминологией, а устойчивой execution boundary и последовательностью действий, которая сохраняет capability при переносе между domains.**

Это существенно усиливает различение `PATTERN → MACHINE`:

- Pattern переносится как **grammar of composition**;
- Machine переносится как **executable realization with stable boundary**;
- domain terminology является частью конкретной реализации, а не обязательно идентичности Machine.

---

## 9. Consequence for CMOC Machine Passport

Independence Test усиливает необходимость разделять в Passport:

1. **Machine abstraction / identity**;
2. **Domain realization**;
3. **Supplied representation / expected-state source**;
4. **Execution boundary**;
5. **Evidence**;
6. **Downstream ownership**.

Это подтверждает ранее предложенную Passport refinement, но **не изменяет пока canonical schema**.

---

## 10. Status

- Risk Model Feedback Loop: `STRONG PATTERN CANDIDATE`
- Expected-vs-Actual Control Verification: `MACHINE ABSTRACTION CANDIDATE`
- Reverse PFMEA: `DOMAIN MACHINE CANDIDATE`
- Pattern → Machine decomposition: `PASS`
- Machine Independence Test: `PASS`
- Negative boundary test: `PASS`
- Canon: `NON-CANON`

No Machine Catalog, Canon or REG-001 changes are made by this patch.

---

## 11. Next verification

Следующий логичный тест — **Machine Composition Test** для нового abstraction:

проверить, действительно ли `Expected-vs-Actual Control Verification` является самостоятельной Machine, а не просто удобным названием для композиции уже существующих механизмов `Audit + Monitoring + Corrective Action + Verification`.

Критерий тот же: если простая сумма механизмов не воспроизводит execution boundary и локальную capability, а отдельная последовательность делает это — Machine abstraction получает дополнительное основание.
