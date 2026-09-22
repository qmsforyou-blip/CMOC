# ARCHITECTURE CHAIN REVIEW — R1 → C2

**Date:** 22-09-2026  
**Status:** REVIEWED / ARCHITECTURE CANDIDATE  
**Scope:** R1, R2–R10, C1, C2  
**Purpose:** проверить целостность границ от QUERY/RECONCILIATION до CMOC WRITE.

## 1. Итоговая цепочка

```
SOURCE
  ↓
DISCOVERY
  ↓
DISCOVERY_RESULT
  ↓
RECONCILIATION / QUERY
  ↓
NO_MATCH / NEEDS_REVIEW
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
CMOC_WRITTEN
```

При этом R1–R10 не образуют одну машину принятия решения: это последовательность отдельных доказательных и decision boundaries.

## 2. Что установлено

### R1 — QUERY / RECONCILIATION

```
MATCH      → EXISTING_EQUIVALENT
NO_MATCH   → NEEDS_REVIEW
CANDIDATE  → NEEDS_REVIEW
AMBIGUOUS  → NEEDS_REVIEW
```

Ключевая инварианта:

```
NO_MATCH ≠ NEW
CANDIDATE ≠ EXISTING_EQUIVALENT
AMBIGUOUS ≠ EXISTING_EQUIVALENT
```

### R2 / R2.1 / R2.2 / R2.3

Сформирована отдельная область NEW DECISION.

NO_MATCH является необходимым, но недостаточным условием.

NEW требует:
- source-bound candidate;
- достаточного query scope;
- завершённых разрешённых query modes;
- отсутствия ambiguity;
- отсутствия unresolved candidate;
- стабильной границы объекта;
- разрешённого target object type;
- полной traceability;
- отсутствия скрытого semantic enrichment.

Evidence gate отделён от самого NEW decision.

### R3 / R10

NEW DECISION отделён от QUERY, RECONCILIATION и CANONIZATION.

Различие документов:
- R3 фиксирует контракт границы NEW DECISION;
- R10 уточняет исполняемое decision rule и versioning.

Это не должно превращаться в две последовательные semantic decisions.

Правильная трактовка:

```
R2/R2.3 → eligibility/evidence gate
R3/R10  → NEW DECISION
```

Результат:

```
NEW_APPROVED
или
NEW_REJECTED
```

NEW_APPROVED не создаёт object_id и не пишет CMOC.

### R4–R8

Semantic novelty разложена на отдельные доказательные слои:

```
R4  semantic NEW criteria
R5  semantic distinction model
R6  relevant comparison set
R7  semantic comparison
R8  semantic distinction assembly
```

Ключевая инварианта:

```
different wording ≠ semantic distinction
different source ≠ semantic distinction
LLM assertion ≠ evidence
DISTINCT ≠ NEW_APPROVED
```

Comparison dimensions:

```
Entity
Property
Relation
Mechanism
Capability
```

Dimension-level evidence сохраняется, а не сворачивается в opaque score.

### R9

R9 собирает evidence package для NEW DECISION.

Он не принимает решение.

```
SEMANTIC_DISTINCTION
        ↓
NEW_DECISION_INPUT
```

### C1 — CANONIZATION

C1 принимает только:

```
NEW_APPROVED
```

и выдаёт:

```
CANONICALIZATION_READY
```

C1 не переоценивает novelty.

Approved-candidate integrity hash защищает границу между NEW DECISION и CANONIZATION.

### C2 — CMOC WRITE

C2 принимает только:

```
CANONICALIZATION_READY
```

и выполняет persistence boundary.

Проверено:
- entry gate;
- provenance;
- traceability;
- canonical identity;
- integrity;
- unauthorized mutation;
- unsupported relations;
- idempotent repeat;
- same-ID/different-representation conflict;
- post-write verification.

C2 не выполняет:
- semantic comparison;
- NEW decision;
- relation creation;
- existing-object mutation;
- OBJECT INDEX rebuild.

## 3. Главный архитектурный результат

Смысловое решение и физическая запись разведены:

```
EVIDENCE
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
```

Следовательно:

> Запись в CMOC не является скрытым местом принятия решения о новизне.

## 4. Что НЕ следует делать дальше

Не следует сейчас объединять R1–C2 в один runtime.

Также не следует:
- переносить semantic comparison в C1;
- переносить NEW decision в C1;
- переносить semantic comparison или NEW decision в C2;
- заставлять C2 создавать relations;
- заставлять C2 перестраивать OBJECT INDEX;
- превращать количество DISTINCT в novelty score.

## 5. Оставшаяся архитектурная граница

После C2 остаётся отдельный вопрос:

> Как детерминированно отразить уже записанный CMOC object в OBJECT INDEX?

Это не semantic decision.

OBJECT INDEX уже имеет отдельный deterministic build.

Поэтому следующий естественный boundary:

```
CMOC WRITE
   ↓
INDEX REFRESH / REBUILD
   ↓
OBJECT INDEX
```

Этот boundary не должен повторно решать NEW, semantic equivalence или canonization.

## 6. Предлагаемый следующий этап

Следующий этап целесообразно оформить как отдельный **C3 — CMOC → OBJECT INDEX synchronization boundary**.

Минимальная задача C3:
- принять подтверждённый CMOC write;
- запустить/зафиксировать deterministic index build;
- проверить появление canonical representation в OBJECT INDEX;
- проверить воспроизводимость;
- не принимать semantic decisions;
- не изменять canonical CMOC representation;
- не создавать relations;
- сохранить traceability CMOC object → index representation.

До начала C3 следует считать цепочку R1–C2 архитектурно собранной, но ещё не productionized.

## 7. Boundary map

| Boundary | Вопрос | Запись |
|---|---|---|
| R1 | Что найдено в CMOC? | нет |
| R2–R9 | Достаточно ли evidence для NEW decision? | нет |
| R10 | NEW или REJECT? | нет |
| C1 | Как approved candidate канонически представить? | нет |
| C2 | Как сохранить canonical representation? | да |
| C3 | Как отразить сохранённый объект в OBJECT INDEX? | derived index |

## 8. Current status

R1–R10, C1 и C2 рассматриваются как отдельные архитектурные boundaries.

C2 test gate: PASS.

C2 evidence: ACCEPTED.

Production semantic novelty engine: не установлен.

Production canonization engine: не установлен.

Production CMOC persistence engine: не установлен.

Следующий архитектурный объект для разработки: **C3 — OBJECT INDEX synchronization boundary**.
