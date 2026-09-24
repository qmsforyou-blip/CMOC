# DECISION-AUTHORITY-001

## Статус
CONTRACT CANDIDATE — v0.1

## Назначение

Определить, кто или что может формировать окончательный DECISION после RECONCILIATION_RESULT.

## Главный вывод

Детерминированное правило может быть субъектом DECISION только в пределах заранее утверждённого правила принятия решения.

Сам факт существования алгоритма или совпадения не даёт машине права принимать любой Decision.

## 1. HUMAN

HUMAN может принять DECISION при наличии:

- конкретного match_id;
- исходного RECONCILIATION_RESULT;
- basis;
- traceability;
- идентифицированного decided_by.

HUMAN является допустимым субъектом для всех кандидатных решений:

- ADMIT_EXISTING;
- ADMIT_NEW;
- REJECT;
- DEFER.

## 2. RULE

RULE может самостоятельно формировать DECISION только если:

1. правило заранее определено и идентифицировано;
2. его область применимости известна;
3. условия правила проверяемы из доступных входов;
4. результат правила детерминирован;
5. правило не выполняет скрытое новое сопоставление;
6. в Decision сохраняется идентификатор правила как decided_by / decision_basis.

### Важное ограничение

RULE не получает право создавать ADMIT_NEW только потому, что Reconciliation вернул NO_MATCH или NEEDS_REVIEW.

Для ADMIT_NEW требуется отдельное утверждённое правило, которое содержит достаточное основание признать кандидата новым объектом.

## 3. MACHINE

MACHINE/LLM в текущем MVP не является самостоятельным субъектом окончательного DECISION.

Она может формировать:

- recommendation;
- evidence summary;
- proposed basis;
- candidate decision.

Но окончательный Decision должен быть принят HUMAN либо заранее утверждённым RULE.

## 4. Особый случай ADMIT_EXISTING

Если Reconciliation уже установил EXISTING_EQUIVALENT и существует заранее утверждённое детерминированное правило, допускающее автоматическое принятие такого результата, RULE может сформировать ADMIT_EXISTING без отдельного человеческого решения.

Это допустимо только при явном policy/rule contract.

Без такого правила EXISTING_EQUIVALENT остаётся результатом Reconciliation и не превращается автоматически в Decision.

## 5. Authority chain

Допустимые варианты:

RECONCILIATION_RESULT
→ HUMAN
→ DECISION

RECONCILIATION_RESULT
→ APPROVED RULE
→ DECISION

RECONCILIATION_RESULT
→ MACHINE RECOMMENDATION
→ HUMAN
→ DECISION

Недопустимый для текущего MVP вариант:

RECONCILIATION_RESULT
→ MACHINE/LLM
→ DECISION

без HUMAN или заранее утверждённого RULE.

## 6. Traceability

Каждый DECISION должен позволять установить:

- кто или какое правило его приняло;
- на каком RECONCILIATION_RESULT он основан;
- какой basis использован;
- какие дополнительные evidence были использованы;
- когда решение принято.

## 7. Boundary

DECISION authority не выполняет физический CMOC admission.

Даже автоматически сформированный RULE Decision не означает:

DECISION → CMOC WRITE

Без отдельного ADMISSION шага.

## 8. Открытые вопросы

1. Где хранится реестр утверждённых RULE?
2. Кто утверждает RULE?
3. Может ли RULE быть изменено без пересмотра его authority?
4. Нужен ли отдельный policy ID в Decision?
5. Какие решения разрешается автоматизировать первыми?

До ответа на эти вопросы автоматизация конкретных Decision не считается разрешённой по умолчанию.
