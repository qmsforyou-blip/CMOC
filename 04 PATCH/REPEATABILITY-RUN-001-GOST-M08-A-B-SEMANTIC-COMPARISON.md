# REPEATABILITY-RUN-001-GOST-M08-A-B-SEMANTIC-COMPARISON

Дата: 18-09-2026

## Исправление предыдущей сверки

При повторной проверке исходного M08 Run A обнаружено, что ранее в сверке были неверно указаны 8 объектов Run A как `001–008`.

Фактический Run A содержит `NEEDS_EVIDENCE` у:

`001, 002, 003, 005, 006, 007, 008, 009`

Run B содержит `NEEDS_EVIDENCE` у:

`002, 009, 012, 019`

## Фактический результат

Общее `NEEDS_EVIDENCE`:

`002, 009` → 2 объекта.

Только Run A:

`001, 003, 005, 006, 007, 008` → 6 объектов.

Только Run B:

`012, 019` → 2 объекта.

Общее `PROVISIONAL`:

30 объектов.

Итого:

- **MATCH: 32/40**
- **VARIANT: 8/40**
- **DIVERGENCE: 0/40**

`MATCH` здесь означает совпадение решения epistemic status.
`VARIANT` означает различие решения `PROVISIONAL ↔ NEEDS_EVIDENCE`.
Объектные границы и идентичность 40 объектов не расходятся.

## 8 реальных вариантов

| Object | Run A | Run B | Направление |
|---|---|---|---|
| 001 Руководство по управлению претензиями | NEEDS_EVIDENCE | PROVISIONAL | A → B |
| 003 Область применимости процесса жалоб | NEEDS_EVIDENCE | PROVISIONAL | A → B |
| 005 Функции процесса работы с жалобами | NEEDS_EVIDENCE | PROVISIONAL | A → B |
| 006 Интеграция процесса в СМК | NEEDS_EVIDENCE | PROVISIONAL | A → B |
| 007 Жизненный цикл процесса жалоб | NEEDS_EVIDENCE | PROVISIONAL | A → B |
| 008 Условия эффективности процесса | NEEDS_EVIDENCE | PROVISIONAL | A → B |
| 012 Цель, политика и процесс | PROVISIONAL | NEEDS_EVIDENCE | B → A |
| 019 Представитель руководства | PROVISIONAL | NEEDS_EVIDENCE | B → A |

## Relations

M07 после нормализации endpoint identity:

**25/25 MATCH, 0 VARIANT, 0 DIVERGENCE.**

## Вывод

M08 выявляет 8, а не 10 нестабильных решений.

Нестабильность относится исключительно к критерию присвоения `PROVISIONAL / NEEDS_EVIDENCE`. Это не расхождение объектного множества, не потеря трассируемости и не расхождение Relations.

Следующая операция — анализ восьми вариантов и формализация воспроизводимого M08 DECISION RULE.

Run A и Run B не переписываются.
