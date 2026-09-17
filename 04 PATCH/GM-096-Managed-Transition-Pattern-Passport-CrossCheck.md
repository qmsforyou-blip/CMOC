# GM-096 — Managed Transition — Pattern Passport CrossCheck

**Дата:** 17-09-2026  
**Извещение на изменение:** `0140+170926`  
**Статус:** `CROSS-CHECK COMPLETE / NON-CANON`

## 1. Цель

Проверить, обладает ли рабочая конструкция **Managed Transition** достаточной
самостоятельностью, чтобы быть зафиксированной как Pattern Passport, не
превращая её в Machine и не утверждая название как универсальный отраслевой
термин.

---

## 2. Рабочее различение

Managed Transition — это не просто:

- изменение;
- переход состояния;
- контроль исполнения;
- Change Management как дисциплина.

Рабочая конструкция фиксирует повторяющуюся последовательность:

```text
STATE A
   ↓
IDENTIFY
   ↓
ASSESS
   ↓
AUTHORIZE
   ↓
CONTROLLED TRANSITION
   ↓
VERIFY
   ↓
ACCEPT / RETURN
   ↓
RECORD / CLOSE
```

Ключевое различение:

> управляется не только новое состояние и не только изменение,
> а сам переход между состояниями.

---

## 3. Cross-check по источникам

### GM QSB — Managing Change

GM-096 задаёт несколько специализированных реализаций одной общей логики:

- Plant Process Change Control — регистрация и согласование изменения;
- Production Trial Run — контролируемое испытание изменения;
- Banking — управление специальным состоянием материала;
- Bypass — управление специальным состоянием процесса;
- Verification / Review — подтверждение результата;
- Return / Close — возврат или завершение.

GM не называет эту совокупность `Managed Transition`; это **CMOC-интерпретация**
архитектурного инварианта.

### Independent Management of Change sources

Независимые источники по Management of Change воспроизводят ту же структурную
логику: идентификация изменения, оценка, authorization, controlled
implementation, verification, formal close-out либо return для временного
изменения.

Особенно важна повторяемость временного перехода:

```text
NORMAL STATE
    ↓
TEMPORARY CHANGE
    ↓
VERIFY
    ↓
RETURN / PERMANENT ADOPTION
    ↓
CLOSE
```

Это поддерживает существование общей конструкции, не зависящей от конкретной
отраслевой реализации.

---

## 4. Проверка самостоятельности Pattern

### Criterion 1 — повторяемая структура

**Да.**

Одинаковая последовательность обнаруживается в разных доменах управления
изменениями и в разных специальных реализациях GM.

### Criterion 2 — независимость от конкретной Machine

**Да.**

PPCR, PTR, Banking и Bypass решают разные специализированные задачи, но могут
быть описаны через общую transition grammar.

### Criterion 3 — отличие от Mechanism

**Да.**

Approval, Verification, Decision Gate, Controlled Deviation и другие элементы
являются отдельными механизмами / паттернами. Managed Transition связывает их
в устойчивую последовательность перехода.

### Criterion 4 — воспроизводимость

**Да, на уровне Pattern.**

Воспроизводится не конкретная форма документа или роли, а структурная
последовательность операций, критериев и состояний.

### Criterion 5 — собственная граница

**Да.**

Паттерн применим только там, где имеется различимый переход из State A в
State B и требуется управлять самим переходом. Он не является общим описанием
любого процесса управления.

### Criterion 6 — отличие от State Transition

**Да.**

State Transition может описывать сам переход между состояниями.
Managed Transition добавляет организационную конструкцию управления:
оценку, полномочие, проверку и принятие / возврат.

### Criterion 7 — отличие от Change Management

**Да, но граница требует дальнейшей проверки.**

Change Management является более широкой дисциплиной / областью практик.
Managed Transition выделяет структурный инвариант внутри неё.

---

## 5. Классификация

| Поле | Решение |
|---|---|
| Kind | `PATTERN` |
| ID | `MP-CAND-096-01` |
| Name | `Managed Transition` |
| Russian name | `Управляемый переход` |
| Status | `STRONG PATTERN CANDIDATE / NON-CANON` |
| Evidence | `MULTI-SOURCE CONFIRMED` |
| Scope | межотраслевая организационная / процессная логика перехода |
| Machine | нет |
| Mechanism | нет |
| Universal Change Management Machine | нет |

---

## 6. Specialized implementations observed

```text
                 MANAGED TRANSITION
                         │
        ┌────────────────┼────────────────┐
        │                │                │
       PPCR             PTR           Temporary Change
        │                │                │
        │                │                └── MOC implementations
        │                │
     Banking          Bypass
        │                │
        └──────── specialized states ──────┘
```

Эта схема не утверждает, что все перечисленные конструкции являются
формальными специализациями с одинаковой онтологической природой. Она показывает
рабочую архитектурную гипотезу: они используют общий transition pattern.

---

## 7. Важное ограничение названия

`Managed Transition` используется здесь как **рабочее CMOC-наименование**.

Cross-check подтверждает распространённость самой идеи managed transition,
но не подтверждает, что существует единый универсальный стандарт,
предписывающий именно это название для данного Pattern.

Поэтому:

- термин не канонизировать;
- не переносить автоматически в LAU;
- не объявлять отраслевым стандартным термином;
- использовать как рабочее имя до дальнейшей номенклатурной проверки.

---

## 8. Что изменилось в CMOC

Создан Pattern Passport:

`03_MACHINE-CATALOG/PATTERNS/MP-CAND-096-01 Managed Transition.md.md`

Commit:

`7f6e59c13356fe9d7849412ec69c5b66cb828639`

При этом:

- `REG-001` — **без изменения**;
- `Canon` — **без изменения**;
- `MACHINE-CATALOG` — **без изменения**;
- существующие Machine Passports — **без изменения**;
- новые Machine не создаются.

---

## 9. Следующий cross-check

Не канонизация.

Следующая проверка должна испытать Pattern на независимых конструкциях,
которые не являются Management of Change:

1. deployment / release transition;
2. organizational transition;
3. migration / cut-over;
4. temporary operating state;
5. return-to-normal / rollback.

Цель — проверить **границу применимости** Pattern, а не увеличить число
источников ради количества.

---

## VERDICT

**Managed Transition имеет достаточную самостоятельность для Pattern Passport.**

Статус:

> **STRONG PATTERN CANDIDATE / MULTI-SOURCE CONFIRMED / NON-CANON**

Главное: мы зафиксировали не ещё одну "машинку", а **инвариантную грамматику
управляемого перехода**, на которой могут строиться разные специализированные
организационные конструкции.
