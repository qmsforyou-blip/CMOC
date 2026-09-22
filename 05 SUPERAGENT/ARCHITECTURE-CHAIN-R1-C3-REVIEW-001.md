# ARCHITECTURE CHAIN REVIEW — R1 → C3

**Date:** 22-09-2026  
**Status:** REVIEWED / ARCHITECTURE CANDIDATE  
**Scope:** R1, R2–R10, C1, C2, C3  
**Purpose:** проверить целостность цепочки от QUERY/RECONCILIATION до детерминированного OBJECT INDEX.

## 1. Итоговая цепочка

```
SOURCE
  ↓
DISCOVERY
  ↓
DISCOVERY_RESULT
  ↓
QUERY / RECONCILIATION
  ↓
NEW DECISION EVIDENCE
  ↓
SEMANTIC COMPARISON
  ↓
SEMANTIC DISTINCTION
  ↓
NEW DECISION
  ↓
NEW_APPROVED
  ↓
CANONIZATION
  ↓
CANONICALIZATION_READY
  ↓
CMOC WRITE
  ↓
CMOC_WRITE_ACCEPTED
  ↓
C3 INDEX SYNCHRONIZATION
  ↓
OBJECT INDEX
  ↓
QUERY
```

R1–R10, C1, C2 и C3 остаются отдельными boundaries. Они не должны сворачиваться в одну непрозрачную semantic machine.

## 2. Boundary map

| Boundary | Основной вопрос | Результат | Изменение CMOC |
|---|---|---|---|
| R1 | Что найдено в CMOC? | EXISTING_EQUIVALENT / NEEDS_REVIEW | нет |
| R2–R9 | Достаточно ли evidence? | eligibility / evidence package | нет |
| R10 | Является ли кандидат NEW? | NEW_APPROVED / NEW_REJECTED | нет |
| C1 | Как approved candidate представить канонически? | CANONICALIZATION_READY | нет |
| C2 | Как сохранить canonical representation? | CMOC_WRITE_ACCEPTED / rejected | да |
| C3 | Как детерминированно отразить сохранённый объект в индексе? | INDEX_SYNCHRONIZED / related status | только derived index |

## 3. R1–R10

### R1

Зафиксирована граница:

```
MATCH      → EXISTING_EQUIVALENT
NO_MATCH   → NEEDS_REVIEW
CANDIDATE  → NEEDS_REVIEW
AMBIGUOUS  → NEEDS_REVIEW
```

Ключевые инварианты:

```
NO_MATCH ≠ NEW
CANDIDATE ≠ EXISTING_EQUIVALENT
AMBIGUOUS ≠ EXISTING_EQUIVALENT
```

### R2–R3 / R9–R10

NEW DECISION отделён от поиска, reconciliation и canonization.

R2–R9 формируют доказательную основу и eligibility.

R10 принимает отдельное решение:

```
NEW_APPROVED
или
NEW_REJECTED
```

NEW_APPROVED не создаёт object_id и не пишет CMOC.

### R4–R8

Semantic novelty разложена по измерениям:

```
Entity
Property
Relation
Mechanism
Capability
```

Сохраняется dimension-level evidence.

Не допускается:

```
different wording = semantic distinction
different source = semantic distinction
LLM assertion = evidence
DISTINCT = NEW_APPROVED
```

## 4. C1 — CANONIZATION

C1 принимает только NEW_APPROVED.

Результат:

```
CANONICALIZATION_READY
```

Approved-candidate integrity hash защищает границу между NEW DECISION и CANONIZATION.

C1 не должен:
- повторно решать NEW;
- выполнять semantic comparison;
- менять semantic boundary без отдельного upstream решения;
- создавать unsupported relations;
- писать CMOC.

Следовательно:

```
NEW_APPROVED ≠ CANONICAL_OBJECT
```

Object identity, создаваемая на C1, является частью canonical representation, а не новой evidence of novelty.

## 5. C2 — CMOC WRITE

C2 принимает только CANONICALIZATION_READY.

C2 отвечает за persistence boundary.

Проверенные свойства:
- entry gate;
- provenance;
- traceability;
- canonical identity;
- integrity;
- unauthorized mutation protection;
- unsupported relations protection;
- idempotent repeat;
- same-ID/different-representation conflict;
- post-write verification.

C2 не выполняет semantic comparison, NEW decision, relation creation или OBJECT INDEX rebuild.

Главная инварианта:

> CMOC WRITE сохраняет уже принятое и канонически подготовленное представление; он не решает, что это представление означает.

## 6. C3 — OBJECT INDEX SYNCHRONIZATION

C3 принимает только подтверждённый:

```
CMOC_WRITE_ACCEPTED
```

и переводит persisted CMOC representation в deterministic OBJECT INDEX representation.

Тест C3: **PASS**, 16/16 branches, failures = 0.

Проверены:
- valid synchronization;
- invalid entry rejection;
- missing object identity;
- missing traceability;
- missing index object;
- already synchronized;
- synchronization conflict;
- orphan index object;
- deterministic rebuild;
- object identity mismatch;
- no semantic comparison;
- no NEW decision;
- no canonization;
- no CMOC mutation;
- no relation creation;
- derivation-only behavior.

## 7. Главный результат после C3

Теперь архитектурно разведены четыре разных действия:

```
DECIDE
  ↓
CANONIZE
  ↓
PERSIST
  ↓
INDEX
```

Их нельзя считать одной операцией.

В частности:

- NEW DECISION отвечает за решение о NEW;
- C1 отвечает за canonical representation;
- C2 отвечает за persistence;
- C3 отвечает за derived index synchronization.

## 8. Трассировка

Архитектурная цепочка теперь может быть представлена как:

```
SOURCE
  ↓
DISCOVERY
  ↓
DISCOVERY_RESULT
  ↓
RECONCILIATION
  ↓
NEW DECISION EVIDENCE
  ↓
NEW DECISION
  ↓
NEW_APPROVED
  ↓
CANONIZATION
  ↓
CANONICALIZATION_READY
  ↓
CMOC WRITE
  ↓
CMOC_WRITE_ACCEPTED
  ↓
OBJECT INDEX
```

C3 не создаёт новый semantic meaning, а сохраняет связь persisted object → derived index representation.

## 9. Что теперь считается установленным

На уровне synthetic / isolated architecture boundaries установлено:

1. Query/Reconciliation не превращает NO_MATCH в NEW.
2. NEW DECISION отделён от semantic evidence.
3. Semantic comparison не скрыт внутри canonization.
4. Canonization не скрыта внутри CMOC WRITE.
5. CMOC WRITE не скрывает semantic decision.
6. OBJECT INDEX не является второй semantic authority.
7. OBJECT INDEX может быть детерминированно получен из persisted CMOC state.
8. Синхронизационный конфликт не превращается автоматически в semantic resolution.
9. Повторная индексация должна быть воспроизводимой.
10. CMOC остаётся canonical persisted representation.

## 10. Что пока НЕ установлено

Эта цепочка пока не является production runtime.

Не установлены:
- production semantic novelty engine;
- production canonization engine;
- production CMOC persistence engine;
- production CMOC → OBJECT INDEX synchronization service;
- production end-to-end orchestration;
- production recovery/transaction semantics;
- production concurrency semantics.

Это не дефекты текущих boundaries. Это отдельный следующий слой реализации.

## 11. Что не следует делать следующим шагом

Не следует немедленно объединять R1–C3 в один runtime.

Не следует:
- переносить semantic decisions в C1/C2/C3;
- делать OBJECT INDEX semantic authority;
- использовать index conflict как основание для автоматического semantic merge;
- создавать relations на C3;
- добавлять LLM как скрытый resolver;
- превращать synthetic tests в утверждение о production readiness.

## 12. Следующая архитектурная граница

После C3 следующий вопрос уже не:

> «Как ещё глубже решить semantic novelty?»

и не:

> «Как ещё один раз записать объект?»

Следующий отдельный вопрос:

> **Как безопасно и воспроизводимо связать всю цепочку SOURCE → DISCOVERY → DECISION → CANONIZATION → CMOC → OBJECT INDEX в единый end-to-end traceable run?**

Это потенциально отдельная integration/orchestration boundary.

На текущем основании не следует заранее называть её C4 как установленный стандарт: сначала должен быть сформулирован её контракт и проверена необходимость.

## 13. Архитектурный вывод

R1 → C3 образуют последовательность границ ответственности:

```
R1
QUERY / RECONCILIATION
        ↓
R2–R9
EVIDENCE
        ↓
R10
NEW DECISION
        ↓
C1
CANONIZATION
        ↓
C2
CMOC WRITE
        ↓
C3
OBJECT INDEX SYNCHRONIZATION
```

Ключевая архитектурная инварианта:

> **Каждый следующий слой работает с уже установленным результатом предыдущего слоя и не присваивает себе его semantic decision responsibility.**

Следовательно, после C3 прежде всего требуется **end-to-end integration boundary review**, а не ещё один semantic layer.

**Current status:** R1–C3 architecturally reviewed; C3 evidence ACCEPTED; productionization remains a separate stage.
