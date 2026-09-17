# GM-096 — PPCR Passport / Cross-Check

> Извещение на изменение: **0131+170926**
>
> Файл: `04 PATCH/GM-096-PPCR-Passport-CrossCheck.md`
>
> Статус: **WORKING / PASSPORT / CROSS-CHECK / NON-CANON**

---

## 1. Объект

**MC-CAND-096-01 — Plant Process Change Control (PPCR)**

Source: `GM Quality System Basics rev March 2009 — Managing Change`

Source location: pp. 327–331, 344.

Passport:

`03_MACHINE-CATALOG/MACHINES/MC-CAND-096-01 Plant Process Change Control.md.md`

---

## 2. Задача проверки

Проверить, сохраняет ли PPCR самостоятельную Machine identity после
перевода исходного описания GM в универсальную CMOC-структуру:

`trigger → input → actions → roles/artifacts → mechanism → capability → output`.

Критический вопрос:

> PPCR — самостоятельная воспроизводимая Machine или только механизм
> более общей Change Control Architecture?

---

## 3. Source construction

GM-096 задаёт для Plant Process Change:

- отдельную процедуру Plant Process Changes;
- охват planned и emergency changes;
- документирование через Plant Process Change form;
- контроль формы через Document Control;
- ведение записи изменений, влияющих на final product;
- информирование затронутых сторон и возможность их input;
- согласование и управляемое прохождение изменения.

Следовательно, исходное описание содержит не только отдельный термин,
но устойчивую последовательность действий, роли и артефакты.

---

## 4. Machine identity test

| Признак | Результат | Основание |
|---|---|---|
| Собственный trigger | YES | необходимость planned / emergency process change |
| Собственный input | YES | описание и сведения о требуемом изменении |
| Собственный набор действий | YES | registration → review → approval → implementation → record |
| Собственные роли | YES | responsible person, stakeholders, approvers, Document Control |
| Собственные артефакты | YES | procedure, Plant Process Change form, records |
| Собственный mechanism | YES | управляемое прохождение изменения через review/approval |
| Собственная capability | YES | способность проводить change без потери управляемости и traceability |
| Собственный output | YES | controlled change + controlled record |
| Воспроизводимость | YES | процедура задаётся как системный порядок, а не разовое решение |
| Полная независимость от общей архитектуры | NO | PPCR является частью более широкой Change Control Chain |

---

## 5. Cross-check: Machine vs Mechanism

### Почему это больше, чем Mechanism

Отдельные элементы PPCR действительно являются механизмами:

- change registration;
- stakeholder notification / input;
- approval;
- controlled implementation;
- record keeping.

Но их совокупность образует bounded construction с собственным trigger,
ролями, артефактами, последовательностью и выходом.

Поэтому сведение PPCR только к `Controlled Change Implementation` или
`Decision Gate` теряет существенную часть конструкции.

### Почему это не следует считать отдельной универсальной Change Control Machine

GM-096 показывает PPCR в конкретном контексте **plant process changes**.
Кроме того, PPCR является управляющим входом в другие специализированные
конструкции GM-096: PTR, Banking и Bypass.

Следовательно, CMOC не должен расширять название до универсальной
`Change Control Machine` без multi-source evidence.

---

## 6. Cross-check: Machine vs Chain

На уровне GM-096 наблюдается архитектура:

```text
CHANGE / CHANGE NEED
        ↓
PLANT PROCESS CHANGE CONTROL
        ↓
TRIAL REQUIRED?
   ┌────┴─────┐
   │          │
  NO         YES
   │          ↓
   │         PTR
   │          ↓
   └────→ IMPLEMENTED STATE
                 ↓
       NORMAL / EXCEPTION STATE
             ↓       ↓
          BANKING   BYPASS
             \       /
              VERIFICATION
                   ↓
              REVIEW / APPROVAL
```

Это **CMOC interpretation**, а не буквальная схема GM QSB.

PPCR в этой Chain выполняет отдельную функцию: **инициализация и управление
самим изменением**.

---

## 7. Boundary test

### Inside PPCR

- регистрация изменения;
- идентификация затронутых сторон;
- review / input;
- approval;
- controlled implementation;
- record / status.

### Outside PPCR

- собственно production trial — PTR;
- длительное хранение и защита материала — Banking;
- временное отклонение от approved process — Bypass;
- product validation как самостоятельная деятельность.

Граница достаточно различима.

---

## 8. Distinction from existing CMOC architecture

### `MC-009-15 Audit`

Audit отвечает на другую базовую функцию: проверку состояния относительно
критериев. PPCR организует изменение состояния.

**Result:** no duplicate.

### `MC-009-10 Andon / MP-002 Response to Abnormality`

Andon / Response to Abnormality запускает реакцию на ненормальность. PPCR
управляет изменением процесса как объектом управления.

**Result:** no duplicate.

### `MP-003 Problem Solving`

Problem Solving предназначен для разрешения проблемы. PPCR предназначен для
управления изменением процесса, независимо от того, возникло ли оно из-за
проблемы.

**Result:** no duplicate.

### `Decision Gate`

Approval является частью PPCR, но не исчерпывает PPCR.

**Result:** Decision Gate remains Mechanism / Pattern.

### `Controlled Change Implementation`

Implementation является одной фазой PPCR.

**Result:** no duplicate; implementation remains Mechanism / Pattern.

---

## 9. Passport verdict

### Identity

PPCR имеет **достаточно выраженную самостоятельную Machine identity** для
сохранения как candidate passport.

### Status

**STRONG-CANDIDATE / NON-CANON**

### Evidence level

**SINGLE-SOURCE**.

### Multi-source requirement

Необходимо подтвердить, что аналогичная bounded construction встречается
в других независимых источниках и сохраняет ту же функциональную границу.

---

## 10. What changes in CMOC

### REG-001

**NO CHANGE.** Противоречия существующим различениям не обнаружено.

### Canon

**NO CHANGE.** Threshold для CANON не достигнут.

### MACHINE-CATALOG

**NO NEW INDEX ENTRY IN THIS PATCH.**

`MC-CAND-096-01` уже присутствует в текущем индексе кандидатов; данный PATCH
фиксирует именно паспортирование и cross-check, а не повторное добавление
кандидата.

### Passport

Создан отдельный паспорт:

`MC-CAND-096-01 Plant Process Change Control.md.md`

---

## 11. Next evidence

Следующая проверка для PPCR:

1. найти независимый источник с сопоставимой construction;
2. проверить сохранение границ `trigger / actions / output`;
3. проверить, не является ли PPCR частным случаем более общего Machine,
   уже существующего в CMOC;
4. только после этого рассматривать `MULTI-SOURCE CONFIRMED`.

Для GM-096 далее логично проверить **PTR**, поскольку PTR является
специализированной Machine внутри той же Change Control Chain.

---

## VERDICT

```text
PPCR
→ самостоятельная bounded construction
→ MACHINE CANDIDATE
→ STRONG CANDIDATE
→ SINGLE-SOURCE
→ NON-CANON

Не Mechanism.
Не Pattern.
Не duplicate Audit / Andon / Problem Solving.
Не универсальная Change Control Machine.
```
