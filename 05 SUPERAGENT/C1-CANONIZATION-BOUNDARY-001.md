# C1-CANONIZATION-BOUNDARY-001

## Статус
CONTRACT CANDIDATE — v0.1

## Назначение

Зафиксировать изолированную границу:

NEW_APPROVED
→ CANONIZATION
→ CANONICALIZATION_READY

C1 не принимает новое semantic решение и не выполняет CMOC WRITE.

## 1. Entry

C1 принимает только approved candidate со статусом:

`NEW_APPROVED`

Обязательны:

- candidate representation;
- provenance;
- traceability;
- approved candidate integrity hash.

`NEW_REJECTED` и иные состояния не допускаются.

## 2. Integrity

C1 проверяет, что полученная candidate representation соответствует сохранённому approved candidate integrity hash.

Mismatch → REJECT.

Integrity check не является semantic comparison и не устанавливает NEW/EQUIVALENT.

## 3. Output

Успешный C1 выдаёт:

`CANONICALIZATION_READY`

и создаёт canonical object identity только внутри границы C1.

Минимально:

```yaml
status: CANONICALIZATION_READY
object_id:
object_type:
canonical_name:
canonical_representation:
provenance:
traceability:
new_evidence_ref:
approved_candidate_hash:
```

## 4. Boundary

C1:

- не выполняет NEW Decision;
- не выполняет semantic comparison;
- не изменяет existing CMOC object;
- не создаёт relations;
- не выполняет CMOC WRITE;
- не изменяет OBJECT INDEX.

После C1:

```text
CANONICALIZATION_READY
→ C2 CMOC WRITE
```

## 5. Negative controls

Должны быть отклонены:

- NEW_REJECTED;
- missing provenance;
- missing traceability;
- missing approved candidate hash;
- changed candidate after approval;
- hidden semantic enrichment;
- existing-object mutation request;
- unsupported relation creation.

## 6. Idempotency boundary

Повторная канонизация одного и того же approved candidate должна воспроизводить тот же canonical object identity.

Различное содержимое при том же approved candidate identity не должно молча перезаписывать результат.

## 7. Scope

Контракт не определяет:

- semantic novelty algorithm;
- NEW Decision;
- LLM prompt;
- relation discovery;
- CMOC persistence;
- OBJECT INDEX synchronization;
- conflict resolution.

## Статус

CONTRACT CANDIDATE — v0.1.
