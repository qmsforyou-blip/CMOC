# PATCH-ISO-034 — ISO-034: 8.6 Release of products and services

**Извещение на изменение:** 0103+270826

## SOURCE
ISO/DIS 9001:2025(E), 8.6 Release of products and services.

Организация должна реализовать planned arrangements на appropriate stages для verification того, что requirements for products and services выполнены. Release to the customer не должен происходить до satisfactory completion planned arrangements, кроме случая approval relevant authority и, если применимо, customer. Documented information должна быть evidence release и включать: (a) evidence of conformity with acceptance criteria; (b) traceability to person(s) authorizing release.

## TERMS
- release
- planned arrangements
- appropriate stages
- verify
- acceptance criteria
- conformity
- authorization
- documented information
- traceability

## DISTINCTIONS
1. Production completion ≠ release.
2. Verification ≠ release.
3. Conformity with acceptance criteria ≠ authorization of release.
4. Release ≠ delivery to customer.
5. Planned arrangements ≠ evidence of their completion.
6. Evidence of conformity ≠ traceability to authorizing person.
7. Authorization ≠ conformity evidence.
8. Release is a controlled transition, not merely a status description.

## GM
- Сначала заверши запланированные проверки, затем разрешай release.
- Не смешивай conformity evidence и authorization.
- Release должен иметь traceability к person(s) authorizing it.
- Финальный результат не должен переходить клиенту до выполнения planned arrangements, кроме явно предусмотренного approval.

## REL
- Planned arrangements → verification → requirements met → release.
- Acceptance criteria → evidence of conformity → release.
- Release → authorization → traceability.
- Release → customer delivery only after satisfactory completion of planned arrangements.
- Documented information → evidence of release.

## MECHANISM
### M-039 — Controlled release

Output
→ planned verification at appropriate stage(s)
→ conformity with acceptance criteria
→ authorization
→ release
→ customer

Evidence branch:

release
→ documented information
→ conformity evidence + authorizer traceability

**STATUS: CANDIDATE / SINGLE-SOURCE**

## CAPABILITY
### CAP-034 — Release control capability

Способность организации не передавать product/service customer до выполнения установленных verification arrangements, подтверждения conformity with acceptance criteria и наличия необходимой authorization/traceability.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## CORE CANDIDATES
### CORE-CANDIDATE-086 — Release is a distinct control boundary

Conformity of an output не равна его release. Между ними существует authorization/control boundary.

**STRONG CANDIDATE / SINGLE-SOURCE**

### CORE-CANDIDATE-087 — Release requires both conformity evidence and authorization traceability

Release evidence имеет как минимум две функции: показать conformity и установить, кто authorized release.

**STRONG CANDIDATE / SINGLE-SOURCE**

## MACHINE
**NONE**

Механизм controlled release присутствует, но конкретная воспроизводимая организационная реализация Machine Источником не задана.

## CHAIN
### CHAIN-CANDIDATE-043
Planned arrangements → verification → acceptance criteria → conformity → authorization → release.

### CHAIN-CANDIDATE-044
Conformity evidence + authorizer traceability → documented information → release evidence.

**STATUS: CANDIDATE / SINGLE-SOURCE**

## ROLE
**NONE**

## PHYSICAL REALIZATION
**NONE**

## DOCUMENT / DOCUMENTED INFORMATION / RECORD
8.6 прямо требует documented information как evidence on release. Она должна содержать evidence of conformity with acceptance criteria и traceability to authorizing person(s).

Это сильное подтверждение ранее добытого различения:

Documented information ≠ автоматически Record.

Но здесь documented information имеет явно evidentiary функцию.

## CMOC INTERPRETATION

8.6 даёт очень чистую управленческую границу:

OUTPUT
→ CONFORMITY
→ AUTHORIZATION
→ RELEASE
→ CUSTOMER

То есть даже подтверждённый conforming output ещё не обязательно может быть передан customer. Нужен отдельный акт release.

Для CMOC это потенциально важная конструкция:

**CONFORMITY ≠ RELEASE**

и:

**RELEASE = CONFORMITY EVIDENCE + AUTHORIZATION**

Последняя формула — именно CMOC interpretation, а не буквальное определение ISO.

### CROSS-CLAUSE

ISO-029: process control → conformity.
ISO-033: output/state of control → conformity.
ISO-034: conformity → authorization → release.

Предварительная цепь:

Requirement
→ Process
→ Controlled realization
→ Output state
→ Conformity
→ Release
→ Customer

**MULTI-CONFIRMATION CANDIDATE; not CORE / not CANON.**

## STATUS SUMMARY
- DIS: NEW / STRONG CANDIDATES
- REL: NEW
- M: M-039 NEW
- CAP: CAP-034 NEW
- CORE: 2 STRONG CANDIDATES
- MACHINE: NONE
- CHAIN: 2 CANDIDATES
- ROLE: NONE
- PHYSICAL REALIZATION: NONE
- Overall: CANDIDATE / SINGLE-SOURCE

## SCOPE CONTROL
CORE, MACHINE-CATALOG, ROLE-CATALOG, CHAIN-CATALOG не изменялись.