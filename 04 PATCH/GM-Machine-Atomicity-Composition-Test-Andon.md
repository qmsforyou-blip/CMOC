# GM QSB — Machine Atomicity / Composition Test — Andon

**Notice:** 0147+170926

## 1. Purpose

Проверить новую границу CMOC на уже выделенной GM Machine `Andon` вне Risk Reduction domain:

> **Machine may be composite, but must have a bounded executable transformation.**

Тест не проверяет, является ли Andon лучшей классификацией; он проверяет именно Machine boundary.

---

## 2. Candidate Machine

**Name:** Andon  
**Class:** DOMAIN MACHINE / existing candidate  
**Pattern:** Response to Abnormality

Рабочая execution structure:

`ABNORMALITY → SIGNAL → VISIBILITY → RESPONSE → NORMAL / ESCALATION`

Andon рассматривается здесь как конкретная доменная реализация механизма управляемого реагирования на обнаруженную abnormality.

---

## 3. Component mechanisms

Для composition test условно выделяем внутренние функции:

- abnormality detection / trigger;
- signal activation;
- visual / audible indication;
- response initiation;
- escalation;
- abnormality status / resolution indication.

Важно: это аналитическое разложение, а не утверждение, что GM называет каждый элемент отдельной Machine.

---

## 4. Test A — Simple component sum

Простая сумма:

`DETECT + SIGNAL + DISPLAY + RESPONSE + ESCALATE`

сама по себе не определяет:

- какой сигнал является входом Andon;
- кому он становится видимым;
- какое состояние считается abnormal;
- какое событие переводит систему в response;
- когда response считается достаточным;
- когда происходит escalation;
- какое событие возвращает объект в normal state.

### Result: FAIL

Набор функций ещё не является Machine.

---

## 5. Test B — Explicit bounded composition

Задаём последовательность:

```text
NORMAL STATE
     ↓
ABNORMALITY DETECTED
     ↓
ANDON SIGNAL ACTIVATED
     ↓
ABNORMALITY MADE VISIBLE / KNOWN
     ↓
RESPONSIBLE RESPONSE INITIATED
     ↓
┌───────────────────────┐
│ abnormality resolved? │
└───────────┬───────────┘
       NO   │   YES
       ↓    │    ↓
 ESCALATION │ NORMAL / RELEASE
       │
       └──→ RESPONSE
```

Здесь возникает bounded transformation:

> **неизвестная/необработанная abnormality → видимая, адресованная и находящаяся в контуре response abnormality.**

### Result: PASS

Это уже не сумма функций, а воспроизводимая execution boundary.

---

## 6. Test C — Remove one structural role

### Remove detection / trigger

`SIGNAL → DISPLAY → RESPONSE`

**FAIL:** отсутствует основание запуска Machine.

### Remove signal / visibility

`ABNORMALITY → RESPONSE`

**FAIL:** исчезает характерная функция Andon — немедленное создание видимого сигнала abnormality.

### Remove response initiation

`ABNORMALITY → SIGNAL → DISPLAY`

**FAIL:** получается визуализация, но не bounded response mechanism.

### Remove escalation

`ABNORMALITY → SIGNAL → RESPONSE → CLOSE`

**PASS WITH QUALIFICATION:** если escalation не является обязательной частью конкретной реализации Andon, Machine сохраняется. Значит escalation — не invariant identity, а optional branch.

### Remove return / closure condition

`ABNORMALITY → SIGNAL → RESPONSE`

**PASS AS PARTIAL, FAIL AS COMPLETE BOUNDARY:** невозможно определить, когда Machine завершает обработку abnormality.

### Result

В отличие от Risk Model Feedback Loop, здесь не все внутренние функции являются обязательными атомами. Некоторые являются **ветвями реализации**.

Это важное уточнение: composition test не требует, чтобы каждый компонент был invariant.

---

## 7. Test D — Capability

Компоненты по отдельности дают:

- detection → обнаружение;
- signal → передача сигнала;
- display → visibility;
- response → действие;
- escalation → усиление response.

Композиция даёт более целостную способность:

> **Сделать abnormality немедленно видимой для ответственного контура и перевести её в управляемый response до восстановления normal state либо escalation.**

### Result: PASS

Capability возникает из связки trigger → visibility → response → closure/escalation, а не из одного display/signalling element.

---

## 8. Machine vs Assembly

Здесь особенно хорошо видно различие уровней.

### Component / mechanism view

```text
Detection
+
Signal
+
Visualisation
+
Response
+
Escalation
```

### Machine view

```text
ABNORMALITY
    ↓
VISIBLE SIGNAL
    ↓
RESPONSIBLE RESPONSE
    ↓
RESOLUTION / ESCALATION
```

### Assembly view

В более крупной системе управления abnormality Andon может входить в Assembly вместе с:

- problem identification;
- containment;
- fast response;
- problem solving;
- escalation;
- verification;
- lessons learned.

Следовательно:

> **Andon остаётся Machine не потому, что внутри нет других механизмов, а потому, что их композиция имеет собственную bounded transformation.**

---

## 9. Boundary test against neighbouring mechanisms

### Visualisation only

`ABNORMALITY → DISPLAY`

**FAIL** as Andon Machine.

### Monitoring only

`OBSERVE → STATUS`

**FAIL**.

### Escalation only

`GAP → ESCALATE`

**FAIL**.

### Response mechanism only

`ABNORMALITY → ACTION`

**FAIL** as Andon identity: отсутствует characteristic signal/visibility boundary.

### Andon

`ABNORMALITY → SIGNAL → VISIBILITY → RESPONSE → RESOLUTION / ESCALATION`

**PASS**.

---

## 10. Relation to Pattern

Existing Pattern:

**Response to Abnormality**

можно выразить как более общую grammar:

`ABNORMALITY → VISIBILITY → RESPONSE → VERIFY / RESTORE`

Andon реализует её специализированным способом:

`ABNORMALITY → SIGNAL → VISIBILITY → RESPONSIBLE RESPONSE → NORMAL / ESCALATE`

Таким образом:

```text
PATTERN
Response to Abnormality
        ↓
MACHINE
Andon
        ↓
DOMAIN REALIZATION
specific Andon implementation
```

Pattern задаёт grammar, Machine — bounded executable realization.

---

## 11. Important qualification — Machine identity is not a fixed list of components

Composition Test выявил более точное правило.

У Machine могут быть:

- invariant structural roles;
- optional branches;
- implementation-specific components;
- repeated internal mechanisms.

Поэтому нельзя определять Machine через формулу:

> «Machine = обязательный набор механизмов A+B+C+D».

Более устойчивый критерий:

> **Machine identity = invariant execution relation + boundary + local capability + closure condition.**

В Andon invariant является не конкретный display, horn, light или escalation step, а отношение:

`abnormality → immediate signal/visibility → responsible response → resolution/escalation`.

---

## 12. Comparison with Expected-vs-Actual Control Verification

| Property | Expected-vs-Actual Control Verification | Andon |
|---|---|---|
| Internal composition | Yes | Yes |
| Simple component sum sufficient | No | No |
| Explicit relations required | Yes | Yes |
| Own execution boundary | Yes | Yes |
| Local capability | Yes | Yes |
| Closure condition | Yes | Yes |
| Optional branches | Limited | Yes |
| Domain-independent abstraction | Candidate | Domain-specific realization |
| Pattern realization | Risk Model Feedback Loop | Response to Abnormality |

### Result

Тест показывает, что новое правило работает не только для risk-control Machine.

---

## 13. Architectural result

### PASS

`Andon` подтверждает:

> **Machine may be composite.**

Но одновременно:

> **Machine is not defined by its internal components.**

Она определяется устойчивой execution boundary:

`trigger → signal/visibility → response → closure/escalation`.

Это усиливает общее различение:

```text
PATTERN
= grammar of composition

MACHINE
= bounded executable transformation

ASSEMBLY
= larger-scope composition
```

---

## 14. Consequence for CMOC

Предлагаемая формулировка Machine criterion после двух независимых тестов:

> **Machine — воспроизводимая bounded execution unit, которая через одну или несколько связанных mechanisms преобразует входное состояние в определённое выходное состояние/результат, имеет собственную локальную capability и условие завершения; внутренние mechanisms не определяют её идентичность сами по себе.**

Это пока **working methodological formulation**, не изменение Canon.

Также подтверждается необходимость различать:

1. Machine identity;
2. internal composition;
3. domain realization;
4. pattern realized;
5. downstream Assembly;
6. closure condition.

---

## 15. Status

- Andon: `DOMAIN MACHINE CANDIDATE`
- Machine Atomicity / Composition Test: `PASS`
- Simple component sum: `FAIL`
- Explicit composition: `PASS`
- Component-removal: `PASS WITH QUALIFICATION`
- Capability: `PASS`
- Negative boundary: `PASS`
- Machine may be composite: `CONFIRMED`
- Machine identity ≠ component list: `CONFIRMED`
- Canon: `NON-CANON`

No Machine Catalog, Canon or REG-001 changes are made by this patch.

## 16. Next verification

После этого теста имеет смысл не идти сразу к новой Machine, а сделать **третью проверку границы** на `Gemba Walk`: выяснить, отличается ли Machine, ориентированная на **обнаружение/проверку состояния**, от Andon, ориентированной на **немедленный перевод abnormality в response**.

Это позволит проверить не только композиционность Machine, но и различие двух типов bounded execution:

`VERIFY / FIND` versus `SIGNAL / RESPOND`.
