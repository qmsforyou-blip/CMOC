# GM QSB — Machine Boundary Triangle — Gemba Walk / Audit / Andon

**Notice:** 0149+170926

## 1. Purpose

Проверить, достаточно ли трёх независимых Machine tests, чтобы устойчиво различить три соседних типа bounded execution:

```text
GEMBA WALK
VERIFY / UNDERSTAND / FIND

AUDIT / EXPECTED-vs-ACTUAL CONTROL VERIFICATION
VERIFY / FIND

ANDON
SIGNAL / RESPOND
```

Цель теста — не ранжирование Machines и не канонизация, а проверка различимости их execution boundaries.

---

## 2. Starting hypotheses

### Gemba Walk

`ACTUAL PLACE → DIRECT OBSERVATION → UNDERSTAND → FINDING → HANDOFF`

Identity-bearing mode:

> **DIRECT PRESENCE AT ACTUAL PLACE**

Local capability: получать непосредственное знание о реальном состоянии работы и превращать существенное наблюдение в traceable finding.

### Expected-vs-Actual Control Verification

`EXPECTED STATE → ACTUAL STATE → EVIDENCE → COMPARE → GAP / NEW INFORMATION → FINDING → ACTION HANDOFF → VERIFY`

Identity-bearing relation:

> **COMPARE REALIZED STATE WITH ACCEPTED EXPECTED STATE**

Local capability: верифицировать реализованный контроль относительно принятого ожидаемого состояния и формировать проверяемый finding с последующей re-verification.

### Andon

`ABNORMALITY → SIGNAL → VISIBILITY → RESPONSIBLE RESPONSE → RESOLUTION / ESCALATION`

Identity-bearing relation:

> **MAKE ABNORMALITY VISIBLE AND TRANSFER IT INTO RESPONSIBLE RESPONSE**

Local capability: перевести abnormality в управляемый response loop.

---

## 3. Test A — Same components, different grammar

Все три Machines могут использовать близкие механизмы:

- observation;
- criterion / expected state;
- finding;
- signal;
- response;
- record.

Следовательно, различие нельзя определять по component list.

### Result: PASS

Различие возникает на уровне **execution grammar / invariant relation**.

```text
Gemba:
PLACE → OBSERVE → UNDERSTAND → FIND

Verification:
EXPECTED → ACTUAL → COMPARE → FIND

Andon:
ABNORMALITY → SIGNAL → RESPONSE
```

Это непосредственно подтверждает правило:

> **Machine identity ≠ component list.**

---

## 4. Test B — Replace the identity-bearing element

### Gemba → remote observation

`DATA / REPORT → ANALYSIS → FINDING`

**FAIL** as Gemba Walk.

Исчезает direct presence at actual place.

### Verification → remove expected state

`ACTUAL → OBSERVE → FINDING`

**FAIL** as Expected-vs-Actual Control Verification.

Остаётся observation/finding, но исчезает comparison against accepted expected state.

### Andon → remove signal / visibility

`ABNORMALITY → RESPONSE`

**FAIL** as Andon.

Остаётся response mechanism, но исчезает характерная signal/visibility boundary.

### Result: PASS

Каждая из трёх Machines имеет собственный identity-bearing element/relation.

---

## 5. Test C — Can one Machine absorb another?

### Gemba Walk absorbs Audit

Если Gemba Walk выполняет формальную criterion-based verification, возникает композиция:

`GEMBA → AUDIT-LIKE VERIFICATION → FINDING`

**PASS AS COMPOSITION, FAIL AS IDENTITY MERGE.**

То есть Audit может быть внутренним механизмом или частью Assembly, не уничтожая Gemba boundary.

### Audit absorbs Gemba

`EXPECTED → ACTUAL → COMPARE → FINDING`

**FAIL AS Gemba.**

Можно получить finding на Gemba, но сама audit execution не требует physical presence.

### Gemba absorbs Andon

`GEMBA → ABNORMALITY → SIGNAL → RESPONSE`

**PASS AS ASSEMBLY / CHAIN, FAIL AS IDENTITY MERGE.**

Gemba может обнаружить abnormality и запустить Andon, но это уже последовательность Machines.

### Andon absorbs Gemba

`ABNORMALITY → SIGNAL → RESPONSE`

**FAIL AS Gemba.**

Andon не требует непосредственного исследования места работы.

### Result: PASS

Machines могут быть **composed / chained**, не становясь одной Machine.

Это важное подтверждение границы Machine vs Assembly.

---

## 6. Test D — Same finding, different Machine

Один и тот же объект может породить finding тремя способами.

### Gemba

Руководитель находится на месте, наблюдает реальную работу, понимает контекст и фиксирует finding.

### Verification

Исполнитель сопоставляет realized control state с accepted expected state и получает gap/finding.

### Andon

Обнаруженная abnormality получает signal и переводится в response.

Следовательно:

> **Finding не является Machine identity.**

Один и тот же тип результата может быть downstream output разных Machines.

---

## 7. Test E — Same abnormality, different execution

Предположим, оператор обнаружил неправильную установку детали.

### Andon

`ABNORMALITY → SIGNAL → RESPONSE`

Вопрос:

> «Как немедленно привлечь ответственного и остановить/эскалировать реакцию?»

### Gemba Walk

`ACTUAL PLACE → OBSERVE → UNDERSTAND → FINDING`

Вопрос:

> «Что реально происходит на месте и что здесь важно понять/зафиксировать?»

### Expected-vs-Actual Verification

`EXPECTED CONTROL → ACTUAL CONTROL → COMPARE → GAP`

Вопрос:

> «Соответствует ли фактическое состояние принятому ожидаемому контролю?»

### Result: PASS

Один и тот же domain event не определяет Machine. Machine определяется выполняемой bounded transformation.

---

## 8. Test F — Closure conditions

### Gemba Walk

Локальное завершение:

> **значимое наблюдение преобразовано в traceable finding / handoff.**

Полное решение проблемы не требуется.

### Expected-vs-Actual Verification

Локальное завершение:

> **verification result сформирован и передан/зафиксирован; последующая re-verification — часть собственной полной boundary, если Machine реализуется как verification-to-closure loop.**

### Andon

Локальное завершение:

> **abnormality разрешена / возвращена в normal state либо передана на escalation.**

### Result: PASS WITH QUALIFICATION

Closure conditions различаются и дополнительно помогают отделять Machines.

При этом у конкретных реализаций closure может быть передан downstream. Поэтому closure condition следует определять на уровне конкретной Machine realization, а не требовать универсально одного типа выхода для всех Machines.

---

## 9. Boundary matrix

| Property | Gemba Walk | Expected-vs-Actual Verification | Andon |
|---|---|---|---|
| Direct presence at actual place | **Invariant** | Not required | Not required |
| Accepted expected state | Optional / contextual | **Invariant** | Not required as formal criterion |
| Direct observation | **Invariant** | Required as one possible evidence source, not necessarily physical | Not necessarily |
| Explicit comparison | Optional | **Invariant** | Not required |
| Finding formation | **Invariant local output** | **Invariant local output** | Not primary identity |
| Signal / visibility | Not invariant | Not invariant | **Invariant** |
| Responsible response | Downstream | Downstream / handoff | **Invariant** |
| Re-verification | Optional/downstream | **Core where verification loop is closed** | Resolution confirmation may occur |
| Primary transformation | Reality → understanding/finding | Expected vs actual → verified finding | Abnormality → managed response |
| Identity-bearing element | Mode of access | Comparison relation | Signal/response relation |

### Result: PASS

The three boundaries remain distinguishable despite substantial mechanism overlap.

---

## 10. Test G — Assembly composition

A realistic management Assembly may chain all three:

```text
GEMBA WALK
ACTUAL PLACE → FINDING
        ↓
EXPECTED-vs-ACTUAL VERIFICATION
EXPECTED → ACTUAL → GAP / VERIFIED FINDING
        ↓
ANDON / RESPONSE
ABNORMALITY → SIGNAL → RESPONSE
        ↓
PROBLEM SOLVING / CORRECTIVE ACTION
        ↓
VERIFICATION / CLOSE
```

Это не означает, что Assembly состоит только из этих Machines или что именно такая последовательность обязательна.

Главное наблюдение:

> **Distinct Machines can be composed into one larger control loop without losing their individual identities.**

Следовательно, Assembly действительно является уровнем composition above Machine.

---

## 11. Architectural result

### PASS

Boundary Triangle устойчиво различает три типа bounded execution:

```text
GEMBA WALK
DIRECT REALITY ACCESS
        ↓
UNDERSTAND / FIND

EXPECTED-vs-ACTUAL VERIFICATION
EXPECTED ↔ ACTUAL
        ↓
COMPARE / FIND

ANDON
ABNORMALITY
        ↓
SIGNAL / RESPOND
```

Это не три синонима «контроля».

У них разные identity-bearing structures:

1. **Gemba Walk — execution mode / access to reality**;
2. **Expected-vs-Actual Verification — comparison relation**;
3. **Andon — signal-to-response relation**.

---

## 12. Stronger Machine criterion

Три теста вместе позволяют уточнить рабочую методологическую формулировку:

> **Machine — воспроизводимая bounded execution unit, в которой одна или несколько связанных mechanisms реализуют invariant execution relation или invariant execution mode, преобразующий исходное состояние/доступ к реальности/сигнал в определённый локальный результат; Machine имеет собственную local capability и closure condition. Её identity определяется этой устойчивой boundary, а не перечнем внутренних mechanisms или названием domain practice.**

Дополнительное следствие:

> **Одинаковые mechanisms могут принадлежать разным Machines, а одна Machine может содержать несколько mechanisms.**

---

## 13. Machine vs Assembly — confirmed distinction

После тестов:

```text
MECHANISMS
    ↓ compose
MACHINE
    ↓ chain / compose with other Machines
ASSEMBLY
    ↓ sustains
CAPABILITY
```

При этом Machine сама может быть composition of mechanisms.

Поэтому корректнее:

> **Assembly is not defined simply as “a bigger Machine”. Assembly is a larger-scope composition whose purpose is to coordinate multiple Machines/mechanisms into a broader control capability.**

Machine отвечает:

> «Какую bounded transformation воспроизводит этот execution unit?»

Assembly отвечает:

> «Какие Machines/mechanisms скоординированы для получения более крупной capability?»

---

## 14. Consequence for Pattern

Тест также усиливает различение Pattern и Machine.

Pattern не должен называться по domain mechanism или по конкретному инструменту.

Он должен описывать grammar, допускающую разные bounded realizations.

Пример:

```text
PATTERN: Response to Abnormality
        ↓
MACHINE: Andon
        ↓
DOMAIN REALIZATION: конкретная Andon system
```

Для Gemba Walk и Expected-vs-Actual Verification точное Pattern mapping пока не канонизируется.

Это намеренное ограничение: boundary test подтвердил Machine identity, но сам по себе не доказал уникальный Pattern.

---

## 15. What this test does NOT prove

Тест не доказывает:

- что Gemba Walk уже должен быть в Machine Catalog;
- что Expected-vs-Actual Control Verification должен стать отдельной Catalog Machine;
- что существующие Pattern definitions окончательны;
- что каждая domain practice обязательно должна иметь одну и только одну Machine;
- что все три Machines одинаково универсальны по domains.

Тест доказывает только structural distinction of bounded executions.

---

## 16. Status

- Boundary Triangle: `PASS`
- Gemba Walk vs Monitoring: `DISTINGUISHED`
- Gemba Walk vs Expected-vs-Actual Verification: `DISTINGUISHED`
- Gemba Walk vs Andon: `DISTINGUISHED`
- Expected-vs-Actual Verification vs Andon: `DISTINGUISHED`
- Same components ≠ same Machine: `CONFIRMED`
- Same finding ≠ same Machine: `CONFIRMED`
- Same abnormality ≠ same Machine: `CONFIRMED`
- Machines can be chained/composed: `CONFIRMED`
- Machine may contain multiple mechanisms: `CONFIRMED`
- Machine vs Assembly distinction: `STRENGTHENED`
- Machine criterion: `WORKING METHODOLOGICAL FORMULATION`
- Pattern mapping for Gemba / Verification: `HOLD`
- Canon: `NON-CANON`

No Machine Catalog, Canon or REG-001 changes are made by this patch.

## 17. Next step

После Boundary Triangle дальнейшее тестирование **Machine Atomicity** на каждой новой Machine уже не выглядит необходимым по умолчанию.

Следующий методологический вопрос следует поднять на уровень **Machine Passport**:

> Какие поля паспорта действительно необходимы, чтобы зафиксировать Machine identity, internal composition, boundary, capability, closure и domain realization — без превращения паспорта в фиксированный component list?

Это позволит превратить результаты тестов 096 / Risk Reduction / Andon / Gemba Walk в устойчивый шаблон паспорта Machine.
