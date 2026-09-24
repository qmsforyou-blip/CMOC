# RULE-GOVERNANCE-001

## Статус
CONTRACT CANDIDATE — v0.1

## Назначение

Зафиксировать минимальную границу управления RULE, используемыми для автоматического принятия DECISION.

## Главный принцип

RULE не получает право принимать DECISION только потому, что оно существует в Registry.

Право возникает через явно зафиксированное approval и разрешённый статус.

Цепочка:

RULE
→ REVIEW / APPROVAL
→ APPROVED
→ ACTIVE
→ DECISION

## 1. RULE REVIEW

До approval должно быть установлено, что RULE:

- имеет уникальный rule_id;
- имеет конкретную версию;
- имеет определённую область применимости;
- имеет однозначные входы;
- имеет проверяемые условия;
- имеет детерминированный результат;
- не выполняет скрытое сопоставление;
- не нарушает границы Reconciliation и Admission.

## 2. APPROVAL

APPROVAL — это утверждение права использовать конкретную версию RULE для принятия Decision в определённой области.

Approval должен сохранять:

- rule_id;
- version;
- approved_by;
- approved_at;
- scope;
- basis;
- traceability.

APPROVAL не является самим Decision и не является CMOC Admission.

## 3. ACTIVE

APPROVED означает, что версия RULE прошла утверждение.

ACTIVE означает, что версия RULE разрешена runtime к фактическому применению.

Не предполагается, что APPROVED автоматически означает ACTIVE.

Переход APPROVED → ACTIVE должен быть явно управляемым.

## 4. SUSPENDED / RETIRED

SUSPENDED означает временный запрет применения RULE.

RETIRED означает, что версия больше не должна использоваться для новых Decision.

Старые Decision, принятые при действовавшей версии RULE, не переписываются.

## 5. Кто утверждает RULE

На уровне CONTRACT CANDIDATE не вводится отдельный обязательный объект authority.

Минимально достаточно, чтобы approval имел идентифицированного approved_by.

Конкретная организационная роль, имеющая право утверждать RULE, остаётся открытым вопросом.

## 6. MACHINE / LLM

MACHINE / LLM может:

- предложить RULE;
- провести техническую проверку формальных свойств;
- сформировать evidence для review.

Но сама MACHINE / LLM не получает authority утверждать RULE только в силу способности его сформировать.

До approval RULE не может использоваться как APPROVED RULE для автоматического Decision.

## 7. Изменение RULE

Изменение условий, результата, scope или другого элемента, влияющего на семантику применения, создаёт новую версию RULE.

Новая версия проходит отдельный approval.

Старая версия сохраняется для traceability уже принятых Decision.

## 8. Runtime boundary

RULE-GOVERNANCE не:

- выполняет Reconciliation;
- изменяет RECONCILIATION_RESULT;
- принимает Decision за runtime;
- выполняет Admission;
- пишет объект в CMOC.

Его результат — разрешение или запрет использования конкретной версии RULE.

## 9. Минимальная цепочка

RULE DRAFT
→ REVIEW
→ APPROVED
→ ACTIVE
→ RULE EXECUTION
→ DECISION
→ ADMISSION

При этом REVIEW здесь является процессом рассмотрения RULE, а не отдельным REVIEW_RECORD кандидата из Reconciliation.

## 10. Открытые вопросы

1. Кто является authority для approval?
2. Нужна ли двухступенчатая схема approval?
3. Какие классы RULE требуют обязательного human approval?
4. Можно ли автоматически активировать уже approved новую версию?
5. Нужен ли отдельный audit trail для lifecycle RULE?
6. Какие проверки обязательны до approval?

До ответа на эти вопросы RULE Governance остаётся контрактом, а не реализованным workflow.
