# GM QSB — Machine Atomicity / Composition Test — Gemba Walk

**Notice:** 0148+170926

## 1. Purpose

Проверить новую границу CMOC на уже выделенной GM Machine `Gemba Walk` вне Risk Reduction domain:

> **Machine may be composite, but must have a bounded executable transformation.**

Дополнительная цель — проверить, действительно ли Gemba Walk является отдельной Machine по отношению к соседним bounded executions:

- `VERIFY / FIND` — Expected-vs-Actual Control Verification / Audit;
- `SIGNAL / RESPOND` — Andon;
- `OBSERVE / STATUS` — Monitoring.

Тест не решает вопрос о канонизации Gemba Walk; он проверяет именно Machine boundary.

---

## 2. Candidate Machine

**Name:** Gemba Walk  
**Class:** DOMAIN MACHINE / existing candidate  
**Pattern:** Assessment against Criterion / Visual Control-related practice, pending exact Pattern mapping

Рабочая execution structure:

`GO TO ACTUAL PLACE → OBSERVE REAL WORK → UNDERSTAND / QUESTION → IDENTIFY FINDING → RECORD / HANDOFF → FOLLOW-UP`

Здесь принципиально важно: Gemba Walk — это не просто «посмотреть на производство». Для Machine test требуется воспроизводимая последовательность, в которой непосредственное присутствие в месте выполнения работы приводит к проверяемому finding и его передаче в последующий контур.

---

## 3. Component mechanisms

Для composition test условно выделяем внутренние функции:

- go to actual place / point of work;
- direct observation of actual work;
- comparison with expected condition / standard where applicable;
- asking questions / understanding the work;
- identification of abnormality, gap or improvement opportunity;
- recording the finding;
- assigning / handing off action;
- follow-up / revisit.

Важно: это аналитическое разложение, а не утверждение, что каждый элемент является отдельной Machine CMOC или что все элементы обязательны в каждой реализации Gemba Walk.

---

## 4. Test A — Simple component sum

Простая сумма:

`GO + OBSERVE + ASK + FIND + RECORD + FOLLOW-UP`

сама по себе не определяет:

- что именно является предметом наблюдения;
- какое состояние считается значимым;
- как observation превращается в finding;
- чем finding отличается от простого замечания;
- где заканчивается собственно Gemba Walk;
- что является его непосредственным результатом;
- принадлежит ли corrective action самому Gemba Walk или последующему Assembly.

### Result: FAIL

Набор действий ещё не задаёт Machine.

---

## 5. Test B — Explicit bounded composition

Задаём execution boundary:

```text
EXPECTED / WORKING CONTEXT
          ↓
GO TO ACTUAL PLACE
          ↓
DIRECT OBSERVATION OF REAL WORK
          ↓
UNDERSTAND / QUESTION
          ↓
SIGNIFICANT CONDITION / GAP / OPPORTUNITY IDENTIFIED?
          ↓
       ┌──┴──┐
      NO     YES
      ↓       ↓
CONTINUE   FINDING FORMATION
OBSERVATION     ↓
            RECORD / HANDOFF
                 ↓
              FOLLOW-UP?
             ┌──┴──┐
            NO     YES
            ↓       ↓
          CLOSE   REVISIT / VERIFY
```

Важное уточнение: `EXPECTED / WORKING CONTEXT` здесь не обязательно означает формальный нормативный критерий. Gemba Walk может исходить из стандарта работы, целевого состояния, производственного потока, известной проблемы, вопроса руководителя или другой принятой рамки наблюдения.

Bounded transformation можно сформулировать так:

> **реальное состояние работы в месте её выполнения → непосредственно наблюдённое и понятое состояние с оформленным значимым finding для последующего действия / follow-up.**

### Result: PASS WITH QUALIFICATION

Возникает воспроизводимая execution boundary, но её closure не обязательно совпадает с закрытием выявленной проблемы. Gemba Walk может завершаться передачей finding в другой контур; follow-up является отдельной или последующей ветвью.

Это не разрушает Machine boundary, если непосредственный output Gemba Walk определён как verified/traceable finding, а не как завершённое corrective action.

---

## 6. Test C — Remove one structural role

### Remove going to actual place

`REMOTE DATA → ANALYSIS → FINDING`

**FAIL** as Gemba Walk.

Теряется отличительный execution boundary — непосредственное посещение места реального выполнения работы.

### Remove direct observation

`GO TO PLACE → ASK → FINDING`

**FAIL** as complete Gemba Walk.

Разговор без непосредственного наблюдения превращает механизм в интервью / information gathering.

### Remove questioning / understanding

`GO → OBSERVE → FINDING`

**PASS WITH QUALIFICATION.**

Наблюдение может быть достаточным для части Gemba Walk. Следовательно, questioning — не invariant identity, а поддерживающий механизм.

### Remove finding formation

`GO → OBSERVE → RECORD STATUS`

**FAIL** as complete Gemba Walk Machine.

Получается observation / monitoring, но не характерная управленческая трансформация Gemba Walk.

### Remove recording / handoff

`GO → OBSERVE → UNDERSTAND → FIND`

**PASS AS PARTIAL, FAIL AS COMPLETE BOUNDARY.**

Без traceable output невозможно устойчиво передать результат в последующий контур управления.

### Remove follow-up

`GO → OBSERVE → UNDERSTAND → FIND → HANDOFF`

**PASS.**

Follow-up может быть отдельной downstream activity. Следовательно, он не является обязательным элементом Machine identity.

### Result

Как и в Andon, не все внутренние функции являются invariant. Для Gemba Walk особенно ясно проявляется различие между:

- invariant execution roles;
- supporting mechanisms;
- optional branches;
- downstream activities.

---

## 7. Test D — Capability

Компоненты по отдельности дают:

- presence at place → access to actual work;
- observation → direct evidence;
- questioning → contextual understanding;
- finding → identified condition/opportunity;
- recording/handoff → traceable transfer;
- follow-up → subsequent confirmation.

Композиция даёт более целостную способность:

> **Получать непосредственное знание о реальном состоянии работы на месте её выполнения и превращать существенное наблюдение в traceable finding, пригодный для последующего управленческого действия.**

### Result: PASS

Capability возникает не из факта «руководитель пришёл в цех», а из связки:

`ACTUAL PLACE → DIRECT OBSERVATION → UNDERSTANDING → FINDING → TRACEABLE HANDOFF`.

---

## 8. Machine vs neighbouring mechanisms

### 8.1 Gemba Walk vs Monitoring

Monitoring:

`OBSERVE / MEASURE → STATUS`

Gemba Walk:

`GO TO ACTUAL PLACE → OBSERVE REAL WORK → UNDERSTAND → FINDING → HANDOFF`

Monitoring отвечает прежде всего на вопрос:

> «Каково состояние?»

Gemba Walk добавляет непосредственное исследование реальной работы и формирование управленчески значимого finding.

### 8.2 Gemba Walk vs Expected-vs-Actual Control Verification / Audit

Expected-vs-Actual Control Verification:

`EXPECTED STATE → ACTUAL STATE → EVIDENCE → COMPARE → GAP → FINDING → ACTION / HANDOFF → VERIFY`

Gemba Walk:

`ACTUAL PLACE → DIRECT OBSERVATION → UNDERSTAND → FINDING → HANDOFF`

Здесь есть пересечение: Gemba Walk может использовать standard/expected condition и выполнять comparison.

Но comparison against criterion не является обязательным invariant Gemba Walk. Его distinctive boundary — **direct presence in the place of work + direct observation/understanding of actual work + finding formation**.

Следовательно, Gemba Walk не следует растворять в Audit / Expected-vs-Actual Control Verification.

### 8.3 Gemba Walk vs Andon

Andon:

`ABNORMALITY → SIGNAL → VISIBILITY → RESPONSIBLE RESPONSE → RESOLUTION / ESCALATION`

Gemba Walk:

`ACTUAL PLACE → OBSERVATION → UNDERSTANDING → FINDING → HANDOFF`

Andon переводит уже обнаруженную abnormality в немедленный response loop.

Gemba Walk создаёт знание/finding непосредственно из наблюдения реальной работы.

### Result

Различие можно выразить как:

> **Gemba Walk = VERIFY / UNDERSTAND / FIND**  
> **Andon = SIGNAL / RESPOND**  
> **Monitoring = OBSERVE / STATUS**

При этом Gemba Walk и Audit могут пересекаться по finding, но имеют различную execution boundary.

---

## 9. Test E — Can Gemba Walk be reduced to Audit?

Попытка заменить Gemba Walk:

`CRITERION → OBSERVE → RECORD NONCONFORMITY`

**FAIL** as equivalent Machine.

Почему:

1. не требуется непосредственное посещение места выполнения работы;
2. observation может быть документальным или дистанционным;
3. criterion-based audit не обязан включать contextual understanding реальной работы;
4. audit closure может включать formal conformity decision, тогда как Gemba Walk может завершаться observation/finding без formal audit conclusion.

Следовательно, Gemba Walk может содержать audit-like comparison, но не исчерпывается им.

---

## 10. Test F — Can Gemba Walk be reduced to Monitoring?

`OBSERVE → STATUS`

**FAIL.**

Monitoring не требует:

- посещения места;
- понимания контекста реальной работы;
- формирования finding из непосредственного наблюдения;
- передачи finding в downstream action loop.

Следовательно, Gemba Walk не является просто human monitoring.

---

## 11. Test G — Can Gemba Walk be reduced to Problem Solving?

`PROBLEM → ROOT CAUSE → CORRECTIVE ACTION → VERIFY`

**FAIL.**

Gemba Walk может инициировать Problem Solving, но не обязан выполнять root-cause analysis, corrective action или effectiveness verification внутри собственной execution boundary.

Следовательно:

> **Gemba Walk supplies findings; Problem Solving consumes selected findings and performs a different bounded transformation.**

---

## 12. Machine vs Assembly

### Component / mechanism view

```text
Presence at actual place
+
Direct observation
+
Questioning / understanding
+
Finding formation
+
Recording / handoff
+
Optional follow-up
```

### Machine view

```text
ACTUAL PLACE
    ↓
DIRECT OBSERVATION
    ↓
UNDERSTAND REAL WORK
    ↓
SIGNIFICANT FINDING
    ↓
TRACEABLE HANDOFF
```

### Assembly view

В более крупной системе Gemba Walk может входить в Assembly вместе с:

- Visual Control;
- Monitoring;
- Audit;
- Problem Identification;
- Fast Response;
- Problem Solving;
- Corrective Action;
- Follow-up / Verification;
- Lessons Learned.

Следовательно:

> **Gemba Walk остаётся Machine не потому, что внутри нет других механизмов, а потому, что direct presence + observation + understanding + finding/handoff образуют собственную bounded execution.**

---

## 13. Relation to Pattern

На текущем уровне наиболее естественно рассматривать Gemba Walk как возможную доменную реализацию более общей assessment/learning grammar, но точное сопоставление с существующим Pattern не следует фиксировать без отдельного Pattern test.

Рабочая локальная grammar:

`ACTUAL PLACE → OBSERVE → UNDERSTAND → FIND → HANDOFF`

Она отличается от:

`ABNORMALITY → SIGNAL → RESPONSE → NORMAL / ESCALATION`

у Andon и от:

`EXPECTED STATE → ACTUAL STATE → EVIDENCE → COMPARE → GAP → FINDING → ACTION → VERIFY`

у Expected-vs-Actual Control Verification.

### Result

Pattern mapping пока **HOLD**. Machine boundary test не требует преждевременного выбора Pattern.

---

## 14. Important qualification — direct presence is identity-bearing

В предыдущем Andon test выяснилось, что Machine identity определяется не фиксированным списком компонентов, а invariant execution relation + boundary + local capability + closure condition.

Gemba Walk даёт полезное уточнение этого критерия:

> **Machine identity может включать invariant mode of access to reality, если именно этот mode является необходимым условием bounded transformation.**

Для Gemba Walk таким identity-bearing element является:

> **direct presence at the actual place of work.**

Если убрать его, остаётся audit, monitoring, interview или data analysis — но уже не тот же Machine.

При этом конкретные способы observation, вопросы, чек-лист, формат записи и follow-up могут изменяться без потери Machine identity.

---

## 15. Architectural result

### PASS

Gemba Walk подтверждает:

> **Machine may be composite.**

И дополнительно показывает:

> **Machine identity may depend on an invariant execution mode, not only on a state-transition sequence.**

Рабочая bounded execution:

`ACTUAL PLACE → DIRECT OBSERVATION → UNDERSTAND → FINDING → TRACEABLE HANDOFF`

Рабочая capability:

> **Получать непосредственное знание о реальном состоянии работы и превращать существенное наблюдение в traceable finding для последующего управленческого действия.**

Это отличает Gemba Walk от:

- Monitoring — `OBSERVE / STATUS`;
- Audit / Expected-vs-Actual Control Verification — `VERIFY / FIND`;
- Andon — `SIGNAL / RESPOND`.

При этом overlap с Audit реален: Gemba Walk может использовать критерии и выполнять comparison, но это не является достаточным определением Machine.

---

## 16. Consequence for CMOC

После трёх тестов можно усилить working Machine criterion:

> **Machine — воспроизводимая bounded execution unit, которая через одну или несколько связанных mechanisms преобразует входное состояние, доступ к реальности или управленческий сигнал в определённый локальный результат, имеет собственную local capability и условие завершения; её identity определяется invariant execution relation / execution mode, boundary и closure condition, а не фиксированным списком внутренних mechanisms.**

Для Gemba Walk особенно полезно разделять:

1. identity-bearing execution mode — direct presence at actual place;
2. internal mechanisms — observation, questioning, finding formation;
3. optional branches — follow-up;
4. direct output — traceable finding / handoff;
5. downstream Assembly — action, problem solving, verification;
6. Pattern mapping — пока HOLD.

Это **working methodological formulation**, не изменение Canon.

---

## 17. Status

- Gemba Walk: `DOMAIN MACHINE CANDIDATE`
- Machine Atomicity / Composition Test: `PASS`
- Simple component sum: `FAIL`
- Explicit bounded composition: `PASS WITH QUALIFICATION`
- Component-removal: `PASS WITH QUALIFICATION`
- Capability: `PASS`
- Negative boundary vs Monitoring: `PASS`
- Negative boundary vs Audit / Expected-vs-Actual Control Verification: `PASS`
- Negative boundary vs Problem Solving: `PASS`
- Machine may be composite: `CONFIRMED`
- Machine identity ≠ component list: `CONFIRMED`
- Identity-bearing execution mode: `DIRECT PRESENCE AT ACTUAL PLACE`
- Pattern mapping: `HOLD`
- Canon: `NON-CANON`

No Machine Catalog, Canon or REG-001 changes are made by this patch.

## 18. Next verification

Следующим шагом целесообразно проверить не ещё одну отдельную Machine, а **Boundary Triangle**:

`GEMBA WALK = VERIFY / UNDERSTAND / FIND`  
`AUDIT / EXPECTED-vs-ACTUAL = VERIFY / FIND`  
`ANDON = SIGNAL / RESPOND`

Цель — выяснить, достаточно ли этих трёх тестов, чтобы устойчиво различить **assessment/finding**, **abnormality response** и **direct-observation learning** как разные Machine boundaries.
