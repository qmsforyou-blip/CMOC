# PATCH-ISO-014

## Извещение на изменение

**0083+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 5.2 — Quality policy; 5.2.1 Establishing the quality policy; 5.2.2 Communicating the quality policy

### SOURCE CLAIM

Top management shall establish, implement and maintain a quality policy that is appropriate to the purpose and context of the organization, supports its strategic direction, provides a framework for setting quality objectives, includes a commitment to satisfy applicable requirements, and includes a commitment to continual improvement of the QMS. The quality policy shall be available as documented information, be communicated, understood and applied within the organization, and be available to relevant interested parties, as appropriate. fileciteturn46file13

The Source distinguishes a policy from objectives: the policy provides a framework for setting quality objectives, while the objectives are established at relevant functions, levels and processes and are consistent with the quality policy. fileciteturn46file13

### TERMS
- quality policy
- purpose
- context
- strategic direction
- quality objectives
- framework
- applicable requirements
- continual improvement
- documented information
- communicated
- understood
- applied
- relevant interested parties

### DISTINCTIONS

**DIS-001 — QUALITY POLICY ≠ QUALITY OBJECTIVE**

The policy provides a framework for setting objectives; objectives are separately established at relevant functions, levels and processes and are consistent with the policy. fileciteturn46file13

**STATUS: CANDIDATE / 1 source**

**DIS-002 — POLICY ≠ DECLARATION**

The Source requires the policy to be established, implemented and maintained; communicated, understood and applied. It therefore has an operational status beyond merely being a statement. fileciteturn46file13

**STATUS: CANDIDATE / 1 source**

**DIS-003 — AVAILABLE AS DOCUMENTED INFORMATION ≠ COMMUNICATED / UNDERSTOOD / APPLIED**

The Source specifies these as distinct requirements for the policy. Availability as documented information does not by itself establish communication, understanding or application.

**STATUS: CANDIDATE / 1 source**

### GM

**GM-001**

> Рассматривай quality policy как управленческий объект: она должна быть не только сформулирована и зафиксирована, но также внедрена, сообщена, понята и применена.

**GM-002**

> Используй policy как framework для формирования quality objectives, сохраняя различие между политикой и целями.

### REL

**REL-001**

```text
ORGANIZATIONAL PURPOSE + CONTEXT
        ↓
QUALITY POLICY
```

**STATUS: CANDIDATE / 1 source**

**REL-002**

```text
STRATEGIC DIRECTION
        ↓
QUALITY POLICY
        ↓
QUALITY OBJECTIVES
```

**STATUS: CANDIDATE / 1 source**

**REL-003**

```text
QUALITY POLICY
        ↓
FRAMEWORK
        ↓
QUALITY OBJECTIVES
```

**STATUS: CANDIDATE / 1 source**

**REL-004**

```text
QUALITY POLICY
        ↓
COMMUNICATE
        ↓
UNDERSTAND
        ↓
APPLY
```

**STATUS: CANDIDATE / 1 source**

**REL-005**

```text
QUALITY POLICY
        ↓
DOCUMENTED INFORMATION
```

**STATUS: CANDIDATE / 1 source**

### MECHANISM

**M-016 — Policy operationalization**

The Source establishes a management mechanism in which policy is:

```text
ESTABLISH
   ↓
IMPLEMENT
   ↓
MAINTAIN
   ↓
COMMUNICATE
   ↓
UNDERSTAND
   ↓
APPLY
```

and functions as a framework for quality objectives while supporting applicable requirements and continual improvement.

**CLASS: M**

**STATUS: CANDIDATE / SINGLE-SOURCE**

No Machine is created: the Source specifies required states/actions for the policy but no concrete reusable organizational implementation.

### CAPABILITY

**CAP-011 — Ability to operationalize a quality policy**

CMOC interpretation: ability to establish a policy aligned with purpose, context and strategic direction and ensure that it becomes available, communicated, understood and applied, while providing a framework for objectives.

**STATUS: CANDIDATE / 1 source**

### CORE CANDIDATE

**CORE-CANDIDATE-017 — Policy as an operational management object**

A policy is not merely a declaration: its managed state includes establishment, implementation, maintenance, communication, understanding and application.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-018 — Policy → objectives framework**

The policy provides a framework within which quality objectives are set; therefore policy and objective are distinct but structurally related management objects.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MACHINE

**NONE**

### CHAIN

**CHAIN-CANDIDATE-005 — Policy operationalization**

```text
ESTABLISH → IMPLEMENT → MAINTAIN → COMMUNICATE → UNDERSTAND → APPLY
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

Do not promote to confirmed Chain until the Source or subsequent clauses provide sufficient evidence that this is an execution sequence rather than a set of requirements.

### ROLE

**NONE NEW**

Top management remains the role identified in ISO-013.

### PHYSICAL REALIZATION

**NONE**

### DOCUMENT / DOCUMENTED INFORMATION / RECORD — SPECIAL OBSERVATION

This clause gives a useful new confirmation for the Document/Documented information line: the quality policy shall be **available as documented information**, while separately it shall be communicated, understood and applied. Therefore the existence/availability of documented information is not equivalent to organizational understanding or application.

The Source's terminology guidance also preserves the distinction between documentation formerly described as being maintained and records formerly described as being retained as evidence. fileciteturn46file18

```text
DOCUMENTED INFORMATION
        ≠
COMMUNICATION
        ≠
UNDERSTANDING
        ≠
APPLICATION
```

The broader:

```text
DOCUMENT ≠ DOCUMENTED INFORMATION ≠ RECORD
```

remains a cross-clause candidate and is not canonized here.

### CMOC INTERPRETATION

ISO-014 adds an important transformation to the architecture:

```text
PURPOSE + CONTEXT + STRATEGIC DIRECTION
                ↓
         QUALITY POLICY
                ↓
       FRAMEWORK FOR OBJECTIVES
                ↓
         QUALITY OBJECTIVES
```

But the policy also has an operational dimension:

```text
POLICY
  ↓
ESTABLISH
  ↓
IMPLEMENT
  ↓
MAINTAIN
  ↓
COMMUNICATE
  ↓
UNDERSTAND
  ↓
APPLY
```

The key CMOC interpretation is therefore:

> **A management statement becomes an operational management object only when its required state includes implementation and use, not merely existence as text.**

This is CMOC interpretation, not an ISO definition.

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **3 CANDIDATES**
- GM: **2**
- REL: **5 CANDIDATES**
- MECHANISM: **M-016 NEW / SINGLE-SOURCE**
- CAPABILITY: **CAP-011 CANDIDATE**
- CORE CANDIDATES: **2**
- MACHINE: **NONE**
- CHAIN: **1 CHAIN-CANDIDATE**
- ROLE: NONE NEW
- PHYSICAL REALIZATION: NONE
- DOCUMENT / DOCUMENTED INFORMATION / RECORD: **cross-clause confirmation**
- CONFIRMATION: **1 source — ISO/DIS 9001:2025**
