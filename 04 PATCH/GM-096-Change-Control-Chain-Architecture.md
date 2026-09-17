# GM-096 — Change-Control Chain Architecture

**Извещение на изменение:** 0139+170926

## 1. Цель

После multi-source cross-check четырёх GM-096 Machine-кандидатов определить,
какая архитектурная конструкция связывает их между собой, не превращая
четыре специализированные Machine в одну универсальную «Change Management
Machine».

---

## 2. Исходная гипотеза

GM-096 даёт четыре bounded construction:

- `MC-CAND-096-01 PPCR` — управление самим изменением;
- `MC-CAND-096-02 PTR` — контролируемое производственное испытание;
- `MC-CAND-096-03 Banking` — управление специальным состоянием материала;
- `MC-CAND-096-04 Bypass` — управление специальным состоянием процесса.

Их нельзя считать одной Machine, поскольку у каждой есть собственный trigger,
input, actions, output и boundary.

Следовательно, проверяется гипотеза:

> **четыре Machine являются узлами воспроизводимой Chain с условными ветвлениями состояния.**

---

## 3. Инвариант Chain

Общий инвариант не равен названию GM «Managing Change».

Он выражается как управление переходом объекта из одного допустимого
состояния в другое с сохранением:

`IDENTITY + RESPONSIBILITY + DECISION + EVIDENCE + AUTHORIZATION + VERIFICATION + TRACEABILITY`

Минимальная абстракция:

```text
STATE / NEED FOR CHANGE
        ↓
IDENTIFY & REGISTER
        ↓
DECIDE / AUTHORIZE
        ↓
CONTROLLED TRANSITION
        ↓
VERIFY RESULT / STATE
        ↓
ACCEPT / RETURN / CLOSE
```

Это **Assembly-level invariant**, а не новая Machine.

---

## 4. Реальная структура GM-096

Линейная схема из четырёх Machine была бы ошибочной.

Корректнее представить её как условную Chain:

```text
                 CHANGE / CHANGE NEED
                         │
                         ▼
                ┌─────────────────┐
                │      PPCR       │
                │ change control  │
                └────────┬────────┘
                         │
                         ▼
                 DECISION GATE
                    /        \
                   /          \
          PTR required?      no PTR
                │               │
                ▼               │
              PTR               │
                │               │
                └───────┬───────┘
                        ▼
                EVALUATION /
                VERIFICATION
                        │
                        ▼
                 IMPLEMENTED /
                 CONTROLLED STATE
                        │
              ┌─────────┼─────────┐
              │         │         │
              ▼         ▼         ▼
           NORMAL     BANKING   BYPASS
            FLOW       STATE      STATE
              │         │         │
              └─────────┼─────────┘
                        ▼
                 VERIFICATION /
                    REVIEW
                        │
                        ▼
                  ACCEPT / CLOSE
```

**Важно:** это CMOC-архитектурная реконструкция. GM QSB не утверждает именно
эту единую диаграмму.

---

## 5. Почему это Chain, а не Machine

### Machine имеет собственную границу

| Machine | Собственный вопрос |
|---|---|
| PPCR | Как провести изменение управляемо? |
| PTR | Нужно ли и как провести производственное испытание? |
| Banking | Как удержать материал в управляемом extended-storage состоянии? |
| Bypass | Как управлять временно изменённым процессом и вернуться в normal state? |

Каждая Machine может быть вызвана отдельно в другом контексте.

### Chain имеет другую границу

Chain отвечает на вопрос:

> **Как связать несколько управляемых переходов так, чтобы изменение не
> потеряло управляемость на пути от необходимости изменения до принятого
> или восстановленного состояния?**

Следовательно:

`Machine = bounded construction`

`Chain = bounded sequence / conditional composition of constructions`

---

## 6. Четыре роли в Chain

### PPCR — ENTRY / GOVERNANCE

PPCR является управляющей точкой входа.
Он не выполняет PTR, Banking или Bypass вместо них.

### PTR — EVIDENCE-GENERATING BRANCH

PTR появляется только при соответствующем решении.
Его выход — evidence / evaluation input для следующего решения.

### Banking — MATERIAL-STATE BRANCH

Banking не является обязательным этапом каждого изменения.
Он активируется, когда material переводится в специальное состояние
extended storage.

### Bypass — PROCESS-STATE BRANCH

Bypass также не является обязательным этапом.
Он активируется, когда normal process временно недоступен или выполнение
выходит за пределы approved process.

---

## 7. Ключевое различие Banking и Bypass

Это особенно важно для CMOC.

```text
Banking
   ↓
объект изменения состояния = MATERIAL

Bypass
   ↓
объект изменения состояния = PROCESS
```

Banking отвечает за сохранение управляемости материального объекта вне
обычного потока.

Bypass отвечает за сохранение управляемости производственного процесса вне
обычного состояния.

Поэтому они не являются двумя вариантами одной Machine.

---

## 8. PTR — не «следующая стадия» всегда

Ещё одна важная коррекция.

Нельзя записывать:

`PPCR → PTR`

как обязательную последовательность.

Правильнее:

```text
PPCR
  ↓
Decision Gate
  ├── PTR required → PTR → Evaluation
  └── PTR not required
```

Таким образом, **Decision Gate является механизмом ветвления Chain**, а не
самостоятельной Machine.

---

## 9. Banking и Bypass — состояния, а не просто действия

В обоих случаях появляется важный CMOC-признак:

```text
NORMAL STATE
     ↓
CONTROLLED SPECIAL STATE
     ↓
MONITOR / VERIFY
     ↓
RETURN / RELEASE
     ↓
NORMAL / ACCEPTED STATE
```

Это позволяет рассматривать Chain не только как последовательность действий,
но и как **управляемый граф переходов состояний**.

---

## 10. Invariant Machine vs Chain

Не следует преждевременно создавать новую Machine вида:

`MC-CAND-096-05 Change Management Machine`

Пока нет основания считать, что вся Chain имеет собственную независимую
bounded identity, отличную от составляющих её Machines.

На текущем уровне доказательств правильнее:

```text
PPCR      = Machine
PTR       = Machine
Banking   = Machine
Bypass    = Machine

Decision Gate
Verification
Authorization
Traceability
Controlled Transition
          = Mechanisms / Patterns

Managing Change
          = Chain / Assembly
```

---

## 11. Что здесь действительно инвариантно

После удаления GM-специфических названий остаётся конструкция:

```text
1. Change / abnormal transition identified
2. Object and scope identified
3. Responsibility assigned
4. Decision made
5. Authorization obtained
6. Transition executed under defined controls
7. Evidence generated / state monitored
8. Verification performed
9. Object accepted, released or returned
10. Record retained
```

Это уже кандидат на **CMOC Pattern уровня управляемого перехода**.

Рабочее имя:

`Managed Transition`

Статус:

`PATTERN CANDIDATE / NON-CANON`

Важно: это пока не новая Machine.

---

## 12. Boundary test для Managed Transition

### Не является Machine

Потому что не задаёт одну конкретную воспроизводимую реализацию.

### Не является просто Mechanism

Потому что объединяет несколько механизмов в устойчивую логику перехода:

`identify → decide → authorize → transition → verify → accept/return → record`

### Может быть Pattern

Поскольку та же логика потенциально может проявляться в:

- process change;
- equipment change;
- organizational change;
- material state transition;
- temporary process deviation;
- controlled implementation;
- release / return-to-normal scenarios.

Однако переносимость за пределы производственного change context пока не
доказана. Поэтому `NON-CANON`.

---

## 13. CMOC architectural stack

GM-096 позволяет впервые достаточно чётко показать пятиуровневую конструкцию:

```text
PATTERN
Managed Transition
       │
       ▼
MECHANISMS
Decision / Authorization / Verification / Traceability
       │
       ▼
MACHINES
PPCR / PTR / Banking / Bypass
       │
       ▼
CHAIN
Managing Change Chain
       │
       ▼
ASSEMBLY / SYSTEM
конкретная организационная реализация
```

При этом `Managed Transition` — не надстройка, которая управляет Machine.
Это общий способ организации перехода, который может быть реализован разными
Machines и Chains.

---

## 14. Catalog decision

**Не изменять основной MACHINE-CATALOG этим patch.**

Причины:

1. Chain-уровень уже концептуально присутствует в каталоге как направление.
2. Новая Chain ID пока не нужна: сначала требуется проверить, является ли
   `Managing Change Chain` устойчивой самостоятельной Chain, а не только
   реконструкцией одного источника.
3. `Managed Transition` пока только Pattern Candidate.
4. Четыре Machine уже имеют паспорта и multi-source confirmation.

Следовательно, patch фиксирует архитектурную гипотезу, но не меняет каталог.

---

## 15. REG-001 / Canon

`REG-001: unchanged`

`Canon: unchanged`

`MACHINE-CATALOG: unchanged`

No new Machine ID.

No canonization.

---

## 16. Следующий cross-check

Проверить `Managed Transition` не по GM, а по другим источникам:

```text
CHANGE CONTROL
ECN / ECR
MANAGEMENT OF CHANGE
TEMPORARY DEVIATION
CONTINGENCY / ALTERNATE PROCESS
RELEASE / RETURN TO NORMAL
```

Цель — выяснить, является ли

`identify → decide → authorize → controlled transition → verify → accept/return → record`

действительно устойчивым CMOC Pattern.

Отдельно проверить, не распадается ли он на уже существующие Patterns:

- Assessment against Criterion;
- Response to Abnormality;
- Measurement-to-Action;
- Controlled Deviation;
- Decision Gate.

Только после этого решать, нужен ли отдельный Pattern `Managed Transition`.

---

## 17. Итоговый verdict

Четыре GM-096 кандидата не схлопываются в одну Machine.

Они образуют **условную Chain**, в которой:

`PPCR` — governing entry,
`PTR` — conditional evidence branch,
`Banking` — material-state branch,
`Bypass` — process-state branch.

Общий инвариант пока разумнее зафиксировать как:

`Managed Transition — PATTERN CANDIDATE / NON-CANON`.

**Это важный результат CMOC:** мы получили не пятую машинку, а проверяемую
гипотезу о новом уровне архитектуры — `Pattern → Machines → Chain`.
