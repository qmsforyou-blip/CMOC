# GM QSB — Reverse PFMEA — Machine Composition Test

**Notice:** 0146+170926

## 1. Purpose

Проверить, является ли `Expected-vs-Actual Control Verification` самостоятельной Machine abstraction или это только удобное имя для композиции уже известных механизмов:

`Monitoring + Audit + Corrective Action + Verification`.

Это composition test, не канонизация.

Предыдущий Independence Test показал, что структура переносится из PFMEA в maintenance / equipment control domain. Теперь проверяем **структурную самостоятельность** этой abstraction.

---

## 2. Candidate Machine

**Working name:** Expected-vs-Actual Control Verification

**Class:** MACHINE ABSTRACTION CANDIDATE

Working execution boundary:

`EXPECTED STATE → ACTUAL STATE → EVIDENCE → COMPARE → GAP / NEW INFORMATION → FINDING → ACTION HANDOFF → VERIFY`

Working capability:

> Verify a realized control state against an accepted expected state, detect consequential discrepancy or new information, produce a traceable finding and trigger downstream action with subsequent re-verification.

---

## 3. Component mechanisms

Для теста берём четыре механизма/функции:

| Component | Что делает | Роль в Candidate Machine |
|---|---|---|
| Monitoring | собирает фактическое состояние / evidence | OBSERVE / EVIDENCE |
| Audit | сопоставляет evidence с criterion | COMPARE / FINDING |
| Corrective Action | выполняет response to gap | ACTION |
| Verification | проверяет результат response | VERIFY |

В предыдущем Composition Test было установлено, что простое соседство функций не образует Pattern: необходимы explicit relations и state transitions. fileciteturn124file0

---

## 4. Test A — Simple sum

Предположим, что Candidate Machine — всего лишь последовательность существующих механизмов:

`MONITOR → AUDIT → CORRECTIVE ACTION → VERIFICATION`

### Result: FAIL as sufficient Machine definition

Почему:

1. `MONITOR` сам по себе не определяет, **с чем** сравнивается actual state;
2. `AUDIT` может сравнивать с criterion, но не обязан инициировать consequential action;
3. `CORRECTIVE ACTION` может исправлять gap, не будучи источником его обнаружения;
4. `VERIFICATION` может проверять отдельный результат и не обязана замыкать relation с исходным expected state;
5. последовательность не определяет ownership boundary между Machine и downstream action;
6. последовательность не определяет, что делать при **new information**, для которой ещё нет установленного criterion;
7. последовательность не определяет, когда expected representation должна быть пересмотрена.

Следовательно:

> `MONITOR + AUDIT + CORRECTIVE ACTION + VERIFICATION` не равняется Candidate Machine.

---

## 5. Test B — Explicit composition

Теперь связываем компоненты не соседством, а отношениями:

```text
ACCEPTED EXPECTED STATE
          ↓
      REALIZATION
          ↓
       MONITOR
          ↓
       EVIDENCE
          ↓
        AUDIT
          ↓
   COMPARE WITH EXPECTED
          ↓
      GAP / NEW INFO
          ↓
       FINDING
          ↓
 CORRECTIVE ACTION / HANDOFF
          ↓
      VERIFICATION
          ↓
   RESULT CONFIRMED?
      ↙         ↘
    NO           YES
    ↓             ↓
 ACTION /        CLOSE
 RETEST           |
                  ↓
        POSSIBLE EXPECTED-STATE
             REASSESSMENT
```

### Result: PASS as executable composition

Здесь появляется не просто сумма функций, а **bounded execution grammar**.

Критические relations:

- expected state → defines comparison reference;
- realization → supplies actual state;
- evidence → supports comparison;
- comparison → creates gap/new information;
- gap → creates finding;
- finding → authorizes/initiates downstream response;
- response → must be verified;
- verification → determines closure or another iteration;
- repeated/new evidence → may trigger reassessment of expected state.

Именно эти relations превращают набор компонентов в воспроизводимый execution mechanism.

---

## 6. Test C — Remove one component

### Remove Monitoring

`EXPECTED → AUDIT → ACTION → VERIFY`

**FAIL** for the general abstraction: отсутствует собственный источник actual-state evidence.

### Remove Audit / Comparison

`EXPECTED → MONITOR → ACTION → VERIFY`

**FAIL:** неизвестно, почему evidence породило action; исчезает explicit gap decision.

### Remove Corrective Action / Handoff

`EXPECTED → ACTUAL → EVIDENCE → GAP → VERIFY`

**FAIL:** discrepancy обнаруживается, но consequential response отсутствует.

### Remove Verification

`EXPECTED → ACTUAL → EVIDENCE → GAP → ACTION`

**FAIL:** нет подтверждения результата и условия завершения.

### Remove Expected State

`ACTUAL → EVIDENCE → GAP? → ACTION → VERIFY`

**FAIL:** gap теряет reference; это уже не Expected-vs-Actual Verification.

### Result

Все пять structural roles являются существенными для полной Candidate Machine:

`REFERENCE + OBSERVATION + COMPARISON + RESPONSE + RE-VERIFICATION`

---

## 7. Test D — Does the Machine add capability?

Capabilities компонентов:

- Monitoring → know actual status;
- Audit → evaluate against criterion;
- Corrective Action → perform response;
- Verification → confirm result.

Candidate Machine adds a composed capability:

> **Maintain a controlled relationship between an accepted expected control state and the realized state by detecting consequential discrepancy, initiating response and confirming the result.**

### Result: PASS, with qualification

Capability не принадлежит ни одному component mechanism отдельно.

Но эта capability возникает **из их architecture of relations**, а не из нового физического действия.

Это не является проблемой для Machine classification: Machine может быть composite mechanism, если композиция имеет устойчивую execution boundary, собственную capability и определённый handoff/closure.

---

## 8. Machine vs Assembly boundary

Здесь возникает важное уточнение CMOC.

### Если смотреть только на компоненты

`Monitoring + Audit + Corrective Action + Verification`

могут образовать **Assembly**.

### Если смотреть на bounded execution

`Expected-vs-Actual Control Verification`

задаёт собственную операционную единицу:

```text
INPUT
accepted expected control state
+ realized object/process

EXECUTION
observe → compare → decide gap → find → handoff → verify

OUTPUT
verified control state / traceable finding / closure state
```

Это даёт основание рассматривать abstraction как **Machine realized through an internal composition of mechanisms**.

Ключевое различение:

> **Assembly отвечает на вопрос «какие механизмы скомбинированы?»**
>
> **Machine отвечает на вопрос «какое bounded преобразование состояния воспроизводится этой композицией?»**

Поэтому одна и та же структура может быть описана на двух уровнях:

`ASSEMBLY VIEW`

`Monitoring + Audit + Corrective Action + Verification`

↓

`MACHINE VIEW`

`Expected-vs-Actual Control Verification`

Это не противоречие, а разные уровни описания одной реализации.

---

## 9. Negative boundary tests

### Ordinary Audit

`CRITERION → EVIDENCE → FINDING`

**FAIL** — нет обязательного response + re-verification.

### Ordinary Monitoring

`OBSERVE → STATUS`

**FAIL** — нет comparison и consequential response.

### Ordinary Corrective Action

`GAP → ACTION → VERIFY`

**FAIL** — actual-vs-expected discrepancy detection находится вне механизма.

### Verification only

`RESULT → CHECK`

**FAIL** — нет expected-state reconciliation.

### Expected-vs-Actual Control Verification

`EXPECTED → ACTUAL → EVIDENCE → GAP → FINDING → ACTION → VERIFY`

**PASS**.

Следовательно, Candidate Machine имеет различимую границу относительно соседних механизмов.

---

## 10. Relation to Risk Model Feedback Loop Pattern

Pattern:

`INTENDED / EXPECTED STATE → REALIZED STATE → EVIDENCE → GAP / NEW INFORMATION → ACTION → VERIFY → UPDATE`

Candidate Machine:

`EXPECTED CONTROL STATE → ACTUAL CONTROL STATE → EVIDENCE → GAP → FINDING → ACTION HANDOFF → VERIFY`

Machine реализует **локальный фрагмент Pattern**.

`UPDATE` accepted representation не является обязательным прямым output Machine. Оно остаётся downstream effect / responsibility of surrounding Assembly where the accepted control model is changed.

Это сохраняет ранее установленную границу: Machine не должна владеть всей feedback loop. fileciteturn121file0

---

## 11. Result of Composition Test

### Primary result

**PASS — Candidate Machine is not reducible to simple adjacency of component mechanisms.**

### Important qualification

Candidate Machine **is composed of mechanisms**.

Поэтому формулировка должна быть точной:

> **Machine ≠ atomic mechanism.**
>
> **Machine may be a bounded composition of mechanisms when the composition has its own execution boundary, local decisions, evidence, capability and closure condition.**

А Assembly отличается тем, что описывает более крупную композицию implementations / Machines для реализации более крупной capability.

---

## 12. Strengthened architecture

Рабочая иерархия теперь выглядит так:

```text
PATTERN
grammar of composition
        ↓
MACHINE
bounded executable transformation
        ↓
DOMAIN MACHINE
specific realization in a domain
        ↓
ASSEMBLY
composition of Machines / mechanisms at a larger scope
        ↓
CAPABILITY
sustained organizational / operational ability
```

Для текущего случая:

```text
Risk Model Feedback Loop
        ↓
Expected-vs-Actual Control Verification
        ↓
Reverse PFMEA
        ↓
Risk Reduction / PFMEA Management
```

При этом внутри Machine:

```text
Monitoring
   +
Audit / Comparison
   +
Finding / Handoff
   +
Verification
```

---

## 13. Passport implication

Composition Test усиливает следующие обязательные поля Machine Passport:

1. **Execution Boundary**;
2. **Input Reference / Expected State**;
3. **Actual-State Acquisition**;
4. **Local Comparison / Decision Logic**;
5. **Evidence**;
6. **Finding / Handoff**;
7. **Re-verification**;
8. **Closure Condition**;
9. **Internal Mechanisms / Composition**;
10. **Downstream Ownership**.

Особенно важно новое поле:

> **Internal Mechanisms / Composition** — какие механизмы реализуют Machine, не смешивая их с идентичностью самой Machine.

Это пока Passport refinement, не изменение canonical schema.

---

## 14. Status

- Risk Model Feedback Loop: `STRONG PATTERN CANDIDATE`
- Expected-vs-Actual Control Verification: `MACHINE ABSTRACTION CANDIDATE`
- Reverse PFMEA: `DOMAIN MACHINE CANDIDATE`
- Simple component sum: `FAIL`
- Explicit composition: `PASS`
- Component-removal test: `PASS`
- Capability test: `PASS WITH QUALIFICATION`
- Negative boundary: `PASS`
- Machine independence: `PASS`
- Canon: `NON-CANON`

No Machine Catalog, Canon or REG-001 changes are made by this patch.

---

## 15. Architectural conclusion

Тест дал важный результат для CMOC:

> **Machine не обязана быть атомарной.**
>
> **Её идентичность определяется не отсутствием внутренних механизмов, а тем, что их композиция образует воспроизводимую bounded execution unit с собственной capability и closure condition.**

И одновременно:

> **Pattern задаёт grammar of composition; Machine задаёт bounded executable transformation; Assembly задаёт composition at a larger scope.**

Это существенно уточняет границу `PATTERN → MACHINE → ASSEMBLY` и делает её пригодной для дальнейшего извлечения машин из GM QSB.

## 16. Next verification

Следующий шаг — проверить эту новую границу на **другой уже найденной GM Machine**, не связанной с Reverse PFMEA: взять, например, `Andon` или `Gemba Walk` и провести короткий **Machine Atomicity / Composition Test**.

Цель: выяснить, работает ли правило `Machine may be composite, but must have bounded transformation` вне Risk Reduction domain.
