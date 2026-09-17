# GM-096 — PTR Passport / Cross-Check

> Извещение на изменение: **0132+170926**
>
> Файл: `04 PATCH/GM-096-PTR-Passport-CrossCheck.md`
>
> Статус: **WORKING / PASSPORT / CROSS-CHECK / NON-CANON**

---

## 1. Объект

**MC-CAND-096-02 — Production Trial Run (PTR)**

Source: `GM Quality System Basics rev March 2009 — Managing Change`

Source location: pp. 333–335.

Passport:

`03_MACHINE-CATALOG/MACHINES/MC-CAND-096-02 Production Trial Run.md.md`

---

## 2. Задача проверки

Проверить, сохраняет ли PTR самостоятельную Machine identity после перевода
исходного описания GM в CMOC-структуру.

Критический вопрос:

> PTR — самостоятельная специализированная Machine или только механизм
> PPCR / Change Control?

---

## 3. Source construction

GM-096 задаёт для PTR отдельную конструкцию:

- written PTR procedure / flowchart;
- PTR Request;
- PTR Core Team decision / approval;
- определение customer/internal PTR requirement;
- внутреннее рассмотрение / approval;
- Communication Form, документирующий каждый шаг;
- customer evaluation, когда применимо.

Источник отдельно ограничивает PTR: он не является substitute или extension
of product validation.

Следовательно, источник описывает не единичную операцию «испытать», а
управляемую последовательность с trigger, ролями, решениями, артефактами,
trial и документированным результатом.

---

## 4. Machine identity test

| Признак | Результат | Основание |
|---|---|---|
| Собственный trigger | YES | решение о необходимости PTR |
| Собственный input | YES | change description, PTR request, requirements |
| Собственный набор действий | YES | request → decision → requirement decision → trial → evaluation |
| Собственные роли | YES | Change Leader, PTR Core Team, approvers, customer contacts |
| Собственные артефакты | YES | PTR procedure, Request, Communication Form, records |
| Собственный mechanism | YES | controlled trial with decision/approval and documented evidence |
| Собственная capability | YES | проверка change в производственных условиях |
| Собственный output | YES | trial result / evaluation input |
| Воспроизводимость | YES | отдельная written procedure / flowchart |
| Независимость от PPCR | NO | PTR вызывается change-control architecture и является её частью |

---

## 5. Cross-check: Machine vs Mechanism

### Почему PTR больше, чем механизм

Отдельные элементы PTR можно разложить на механизмы:

- Decision Gate;
- controlled trial;
- evaluation;
- documented communication.

Но их совокупность образует bounded construction с собственной процедурой,
ролями, артефактами и результатом.

Сведение PTR только к `Controlled Trial` теряет управленческую часть
конструкции: решение о необходимости trial, approvals, определение
требований и фиксацию результата.

### Почему PTR не следует поглощать PPCR

PPCR управляет изменением в целом. PTR отвечает на более узкий вопрос:

> что делать, когда для принятия изменения требуется испытание
> в производственных условиях?

PTR имеет собственную последовательность и собственный output.
Поэтому он может быть отдельной специализированной Machine внутри PPCR/Change
Control Chain.

---

## 6. Boundary test

### Inside PTR

- PTR request;
- решение PTR Core Team;
- approval;
- определение customer/internal requirement;
- controlled production trial;
- документирование шагов и результата;
- evaluation, когда применимо.

### Outside PTR

- регистрация и общее управление изменением — PPCR;
- product validation;
- Banking;
- Bypass;
- общая Audit / verification architecture.

Граница функционально различима.

---

## 7. Distinction from existing CMOC architecture

### PPCR

PPCR управляет полным изменением производственного процесса. PTR является
специализированным ответвлением, когда trial required.

**Result:** specialization, not duplicate.

### Audit / Assessment against Criterion

PTR включает evaluation / verification, но его назначение — организовать
производственный trial изменения. Он не сводится к проверке состояния
относительно критерия.

**Result:** no duplicate.

### Product Validation

Источник прямо отделяет PTR от product validation.

**Result:** not a validation Machine.

### Decision Gate

Decision / approval является частью PTR, но не исчерпывает его.

**Result:** Decision Gate remains Mechanism / Pattern.

---

## 8. Specialized Machine test

PTR имеет смысл сохранять как **specialized Machine**, потому что его
специализация определяется не только контекстом применения, но и отдельной
bounded construction:

```text
PTR REQUIRED
     ↓
PTR REQUEST
     ↓
TEAM DECISION / APPROVAL
     ↓
REQUIREMENT DECISION
     ↓
PRODUCTION TRIAL
     ↓
DOCUMENTED RESULT
     ↓
EVALUATION
```

Это не просто один шаг PPCR, а воспроизводимый подцикл.

При этом независимость от общей Change Control Chain отсутствует:
PTR вызывается из неё и возвращает evidence обратно в неё.

---

## 9. Passport verdict

### Identity

PTR имеет **достаточно выраженную самостоятельную специализированную Machine
identity** для сохранения как candidate passport.

### Status

**SPECIALIZED-CANDIDATE / NON-CANON**

### Evidence level

**SINGLE-SOURCE**.

### Multi-source requirement

Нужен независимый источник с аналогичной конструкцией controlled production
trial для проверки устойчивости функциональной границы.

---

## 10. What changes in CMOC

### REG-001

**NO CHANGE.** Нового противоречия не выявлено.

### Canon

**NO CHANGE.** Evidence threshold не достигнут.

### MACHINE-CATALOG

**NO NEW INDEX ENTRY IN THIS PATCH.** Кандидат уже зарегистрирован в индексе
GM-096. Этот PATCH фиксирует паспортирование и cross-check.

### Passport

Создан:

`MC-CAND-096-02 Production Trial Run.md.md`

---

## 11. Next evidence

1. Найти независимые источники controlled production trial / manufacturing
   trial и проверить функциональную эквивалентность.
2. Сравнить границы PTR с общими Trial / Validation constructions.
3. Не расширять PTR до универсальной Validation Machine.
4. После этого вернуться к Banking Process.

---

## VERDICT

```text
PTR
→ самостоятельная bounded construction
→ SPECIALIZED MACHINE CANDIDATE
→ SINGLE-SOURCE
→ NON-CANON

Не просто Mechanism.
Не duplicate PPCR.
Не Product Validation.
Не Audit.

Функционально:
PPCR → [PTR when required] → evidence → change decision
```
