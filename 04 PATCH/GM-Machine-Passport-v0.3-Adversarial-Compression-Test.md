# GM Machine Passport v0.3 — Adversarial Compression Test

**Notice:** 0162+170926  
**Status:** PASS / NON-CANON  

## 1. Purpose

Проверить, не стала ли компактная схема Passport v0.3 слишком широкой: может ли обычный объект получить вид Machine только потому, что ему можно приписать имя, вход, действие и результат.

Adversarial candidates:

- Checklist;
- Record;
- Meeting;
- Monitoring;
- Static Visual Control.

## 2. Classification rule

Само наличие полей Passport не делает объект Machine.

Перед заполнением Passport требуется доказать:

```text
identity-bearing relation/mode
+ own execution boundary
+ local capability
+ closure condition
```

Если этого нет, Passport не должен «создавать» Machine из объекта.

## 3. Checklist

### Attempted Passport

```text
name: Checklist
trigger: audit/inspection
inputs: criteria
execution: check items
outputs: completed checklist
closure: checklist completed
```

На поверхности всё похоже на Machine.

### Boundary test

Identity-bearing relation отсутствует: checklist — это прежде всего структурированный носитель критериев/пунктов проверки.

Execution boundary принадлежит использующему его assessment/audit process, а не самому документу.

Local capability документа — представить/зафиксировать критерии и результаты, но не выполнить самостоятельную bounded transformation.

**Result: FAIL AS MACHINE.**

Classification: **ARTIFACT / SUPPORTING OBJECT**.

## 4. Record

### Attempted Passport

```text
name: Record
trigger: event
inputs: data
execution: capture/store
outputs: record
closure: stored
```

### Boundary test

Record фиксирует evidence/result. Его existence не означает собственной Machine execution boundary.

`capture/store` может быть механизмом конкретной Machine, но generic Record не имеет собственной invariant execution relation.

**Result: FAIL AS MACHINE.**

Classification: **ARTIFACT / EVIDENCE CARRIER**.

## 5. Meeting

### Attempted Passport

```text
name: Meeting
trigger: scheduled event
inputs: participants/information
execution: discussion
outputs: decisions/actions
closure: meeting ended
```

### Boundary test

Generic Meeting does not have one invariant execution relation. It can host Audit review, Problem Solving, Decision Gate, Knowledge Transfer and other Machines.

The fact that a meeting has a beginning, participants, actions and an end is insufficient.

**Result: FAIL AS GENERIC MACHINE.**

Classification: **ASSEMBLY / HOSTING CONTEXT**.

Qualification: a specifically bounded meeting-based realization could instantiate a Machine if its own invariant relation, capability and closure are independently demonstrated. The generic object “Meeting” remains non-Machine.

## 6. Monitoring

### Attempted Passport

```text
name: Monitoring
trigger: continuous/scheduled
inputs: process state
execution: observe/measure
outputs: status/data
closure: observation cycle
```

### Boundary test

Generic Monitoring normally supplies observation/status to another bounded execution. It does not inherently include a Machine-level local response relation.

The previous Machine tests already distinguished Monitoring from:

- Gemba Walk;
- Expected-vs-Actual Control Verification;
- Andon.

Monitoring can be an internal mechanism of a Machine or Assembly.

A concrete bounded monitoring realization with its own closure and local capability may separately qualify, but the generic class “Monitoring” must not be promoted automatically.

**Result: FAIL AS GENERIC MACHINE.**

Classification: **MECHANISM / SUPPORTING EXECUTION**.

## 7. Static Visual Control

### Attempted Passport

```text
name: Static Visual Control
trigger: existence/update need
inputs: state information
execution: display information
outputs: visible information
closure: information displayed
```

### Boundary test

A static sign, label, board or posted standard is primarily an Artifact. It can represent a Machine realization, but the static object itself does not necessarily execute a bounded relation.

This is consistent with the earlier Visual Control boundary test: a concrete bounded visual-status execution may qualify, while a static visual artifact does not.

**Result: FAIL AS STATIC OBJECT.**

Classification: **ARTIFACT**, unless a concrete executable visual-control realization independently demonstrates Machine boundary.

## 8. Adversarial matrix

| Candidate | Passport-looking fields possible? | Machine boundary? | Result |
|---|---:|---:|---|
| Checklist | Yes | No | FAIL — Artifact |
| Record | Yes | No | FAIL — Evidence carrier |
| Meeting | Yes | No, generic | FAIL — Assembly/hosting context |
| Monitoring | Yes | No, generic | FAIL — Mechanism |
| Static Visual Control | Yes | No, static object | FAIL — Artifact |

## 9. Compression safety test

The reduced Passport therefore does **not** act as a classifier by field count.

The sequence is:

```text
OBJECT
  ↓
BOUNDARY PROOF
  ↓
Machine candidate?
  ├─ NO → Artifact / Mechanism / Context / Assembly / other class
  └─ YES → Passport
```

This preserves the distinction established by the earlier Machine Passport Boundary Test.

## 10. Important qualification

A generic object can contain or host a Machine realization.

Therefore:

```text
Checklist ≠ Machine
but
Checklist-based verification Machine → possible

Meeting ≠ Machine
but
Meeting-hosted bounded Machine → possible

Monitoring ≠ generic Machine
but
bounded monitoring realization → possible

Static Visual Control ≠ Machine
but
executable visual-control realization → possible
```

The Passport describes the **bounded Machine realization**, not the generic noun from which that realization is named.

## 11. Architectural consequence

The adversarial test strengthens the hierarchy:

```text
PATTERN
  ↓
MACHINE
  ↓
DOMAIN MACHINE
  ↓
ASSEMBLY
  ↓
CAPABILITY
```

And separately:

```text
OBJECT → boundary proof → Passport
```

Passport is therefore not the mechanism that determines Machine status. Machine boundary proof precedes Passport instantiation.

## 12. Conclusion

**Adversarial Compression Test — PASS.**

The compact v0.3 schema remains safe against the tested false-positive classes.

Confirmed:

- field presence does not establish Machine identity;
- bounded execution remains a prerequisite;
- generic artifacts remain artifacts;
- generic records remain evidence carriers;
- generic meetings remain hosting contexts/Assemblies;
- generic monitoring remains a mechanism/supporting execution;
- static visual control remains an artifact unless an executable realization is separately demonstrated;
- a concrete realization can still qualify when its own invariant execution relation, local capability and closure are demonstrated.

**Working status:** Machine Passport v0.3 CANDIDATE / NON-CANON.

**No Catalog / Canon / REG-001 changes.**

**Next methodological question:** freeze the v0.3 schema as a working Passport specification and test it on one complete real GM Machine passport, preferably Reverse PFMEA or PTR, including provenance and validation.