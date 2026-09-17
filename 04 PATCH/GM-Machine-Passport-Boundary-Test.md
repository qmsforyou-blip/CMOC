# GM QSB — Machine Passport Boundary Test v0.1

**Notice:** 0153+170926  
**Status:** TEST PATCH / NON-CANON

## 1. Purpose

Проверить обратную сторону Machine Passport: способен ли паспорт отличить Machine от объекта, который лишь используется внутри управленческой системы, но не имеет собственной bounded execution.

Тестовые отрицательные кандидаты:

- checklist;
- document / record;
- meeting;
- KPI / metric;
- monitoring;
- отдельный mechanism.

Гипотеза:

> Если Machine Passport действительно фиксирует ontological boundary Machine, то объект без собственной bounded execution, local capability и closure condition не должен получать полноценный Machine Passport только потому, что у него есть входы, выходы или последовательность действий.

Это не канонизация schema.

## 2. Boundary criterion

Рабочий критерий Machine:

> Machine — воспроизводимая bounded execution unit, в которой одна или несколько связанных mechanisms реализуют invariant execution relation или invariant execution mode, преобразующий исходное состояние / доступ к реальности / сигнал в определённый локальный результат; Machine имеет собственную local capability и closure condition.

Паспорт должен выявлять минимум:

```text
IDENTITY
  ↓
IDENTITY-BEARING RELATION / MODE
  ↓
BOUNDARY
  ↓
EXECUTION
  ↓
LOCAL CAPABILITY
  ↓
CLOSURE
```

Наличие только одного из элементов недостаточно.

## 3. Negative Candidate A — Checklist

### Что есть

Checklist может иметь:

- название;
- набор пунктов;
- критерии;
- входной контекст;
- артефактный output — заполненный checklist.

### Что отсутствует

Checklist сам по себе:

- не выполняет observation;
- не сравнивает actual с expected;
- не формирует самостоятельное finding как execution result;
- не инициирует response;
- не имеет собственной execution boundary независимо от пользователя.

Identity-bearing relation отсутствует: checklist — representation / artifact.

Local capability отсутствует как capability самой Machine; capability принадлежит выполняющему mechanism / Machine.

Closure checklist = заполнение документа не является closure Machine.

**Result: FAIL — не Machine.**

Checklist может быть `artifact` внутри Machine Passport, но не обязан иметь собственный Passport.

## 4. Negative Candidate B — Document / Record

Document или record может фиксировать:

- expected state;
- result;
- decision;
- history;
- evidence.

Но запись сама не выполняет bounded execution.

Она может быть:

- input;
- evidence;
- output;
- artifact;
- provenance carrier.

Identity-bearing relation отсутствует как execution relation.

**Result: FAIL — не Machine.**

Важное различение:

```text
Machine → produces / consumes Record
Record ≠ Machine
```

## 5. Negative Candidate C — Meeting

Meeting выглядит сильнее, потому что имеет:

- trigger;
- participants;
- agenda;
- inputs;
- discussion;
- decisions;
- outputs.

Но эти признаки сами по себе не делают meeting Machine.

При проверке Passport возникает проблема identity:

`meeting` как организационная форма не имеет одного invariant execution relation, который сохранялся бы независимо от содержания встречи.

Встреча может реализовывать разные Machines:

- assessment;
- decision;
- problem solving;
- knowledge transfer;
- review;
- planning.

Следовательно, meeting — организационная container/form, внутри которой могут исполняться Machines.

Closure `meeting ended` не равен closure одной определённой Machine.

**Result: FAIL as generic Machine; possible host/container for Machines.**

## 6. Negative Candidate D — KPI / Metric

KPI имеет:

- definition;
- target / expected value;
- actual value;
- calculation;
- status.

Но metric itself не обязательно выполняет response loop.

Его функция — representation / measurement / status.

Даже если KPI автоматически рассчитывается, вычисление значения ещё не означает наличие полной Machine boundary.

Например:

```text
MEASURE → VALUE
```

может быть внутренним mechanism внутри Monitoring Machine.

Если появляется bounded execution:

```text
EXPECTED → ACTUAL → EVIDENCE → COMPARE → DECIDE → ACTION → VERIFY
```

то Machine возникает не из KPI, а из соответствующей execution architecture.

**Result: FAIL as generic Machine; may be input / artifact / mechanism inside a Machine.**

## 7. Negative Candidate E — Monitoring

Monitoring является наиболее важным отрицательным тестом, поскольку ранее оно выступало компонентом других Machines.

Минимальная форма:

```text
OBSERVE / MEASURE → STATUS
```

Monitoring может иметь:

- trigger / periodicity;
- input signal;
- observation / measurement;
- evidence;
- status output.

Но при таком определении отсутствует обязательная bounded response relation.

Monitoring не обязан:

- сравнивать с accepted expected state;
- формировать finding;
- инициировать action;
- verify effectiveness;
- закрывать более широкий control loop.

Поэтому Monitoring может быть самостоятельным mechanism или Machine candidate только при доказательстве собственной execution boundary и local capability, а generic `Monitoring` как наблюдение → статус недостаточен для Machine.

**Result: FAIL for generic Monitoring Machine; mechanism / component of other Machines.**

Это важно не путать с утверждением, что никакая monitoring realization не может быть Machine. Конкретная bounded monitoring system может пройти отдельный Machine test.

## 8. Negative Candidate F — Single Mechanism

Пример:

`Signal activation`

или

`Measurement`

или

`Record creation`.

Каждый механизм может иметь:

- input;
- operation;
- output.

Но input → operation → output ещё не доказывает Machine identity.

Проверка требует:

- invariant relation / mode;
- own boundary;
- local capability;
- closure.

Следовательно:

> Mechanism ≠ Machine автоматически.

Однако bounded composition of mechanisms может стать Machine, если композиция приобретает собственную identity, capability, boundary и closure.

**Result: FAIL as generic Machine; composition may pass.**

## 9. Cross-boundary matrix

| Candidate | Identity-bearing relation/mode | Own boundary | Local capability | Closure | Machine? |
|---|---|---:|---:|---:|---|
| Checklist | — | — | — | — | FAIL |
| Document / Record | representation | — | — | — | FAIL |
| Meeting | generic container form | partial | content-dependent | end of meeting | FAIL as generic Machine |
| KPI / Metric | measurement/status representation | partial | — | value calculated | FAIL as generic Machine |
| Monitoring | observe/measure → status | partial | limited | status produced | FAIL as generic Machine |
| Single mechanism | operation relation | local operation only | mechanism-level | operation complete | FAIL as generic Machine |
| Bounded Machine | invariant relation/mode | YES | YES | YES | PASS |

## 10. Passport failure modes revealed by the test

Тест выявил, что следующие поля сами по себе недостаточны:

- `trigger` — есть у meeting, monitoring, document workflow;
- `inputs` — есть почти у любого artifact;
- `outputs` — есть почти у любого mechanism;
- `states_actions` — можно искусственно описать у любого процесса;
- `evidence` — может быть просто stored record;
- `closure_condition` — формальное завершение не равно Machine closure.

Следовательно, Passport не должен принимать объект как Machine по принципу заполнения всех полей.

Критическим становится сочетание:

```text
IDENTITY-BEARING RELATION / MODE
        +
OWN EXECUTION BOUNDARY
        +
LOCAL CAPABILITY
        +
CLOSURE CONDITION
```

А остальные поля описывают воспроизводимость этой bounded execution.

## 11. Machine vs Artifact / Container / Mechanism

Рабочее различение:

### Artifact

Носитель representation / evidence / record.

### Container / organizational form

Форма, внутри которой могут исполняться различные Machines.

### Mechanism

Локальный способ воздействия / преобразования / получения результата.

### Machine

Bounded composition or mechanism with its own invariant execution relation or mode, local capability and closure.

Это не иерархия «лучше–хуже»; это разные ontological roles.

## 12. Architectural result

Boundary Test усиливает предыдущие результаты:

```text
PATTERN
  ↓ grammar of composition
MACHINE
  ↓ bounded executable transformation
DOMAIN MACHINE
  ↓ concrete realization
ASSEMBLY
  ↓ larger-scope composition
CAPABILITY
```

И одновременно:

```text
ARTIFACT / RECORD ─┐
MEETING / CONTAINER ├─ may host / support Machine
MECHANISM ──────────┘

but

supporting object ≠ Machine
```

Главное следствие:

> **Machine Passport не должен превращать любой объект с входом, действием и выходом в Machine. Паспорт должен сначала доказать существование Machine boundary, а уже затем описывать её реализацию.**

## 13. Schema implication

В Passport следует добавить явное поле / проверку:

```yaml
identity:
  machine_boundary_test:
    identity_bearing_relation_or_mode:
    own_execution_boundary:
    local_capability:
    closure_condition:
    result:
```

Это пока рабочая schema implication, не каноническое изменение.

Также сохраняется ранее выявленное требование поддерживать значения:

- `N/A`;
- `HOLD`;
- `distributed`.

Важно различать:

```text
schema completeness
≠
instance completeness
```

## 14. Status

- Passport Boundary Test: `PASS`
- Checklist as Machine: `FAIL`
- Document/Record as Machine: `FAIL`
- Meeting as generic Machine: `FAIL`
- KPI/Metric as generic Machine: `FAIL`
- Monitoring as generic Machine: `FAIL`
- Single mechanism as Machine: `FAIL`
- Mechanism composition → Machine possibility: `CONFIRMED`
- Machine boundary criterion: `STRENGTHENED`
- Passport schema: `WORKING v0.1 + boundary test`
- Canon: `NON-CANON`

No Machine Catalog, Canon or REG-001 changes are made by this patch.

## 15. Next step

Следующий методологический шаг — **Machine Passport Closure Test**: проверить, не является ли `closure_condition` слишком слабым полем, и отделить:

- completion of operation;
- closure of Machine;
- closure of Assembly;
- return to normal;
- handoff to downstream Machine.

Это позволит окончательно проверить нижнюю границу Machine перед переходом к формализации Passport v0.2.
