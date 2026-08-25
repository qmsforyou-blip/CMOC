# PATCH-ISO-004

**Извещение на изменение:** 0073+250826

**SOURCE:** ISO/DIS 9001:2025 (6th Ed. DIS)
**LOCATION:** Introduction, 0.3.2 Plan-Do-Check-Act cycle
**STATUS:** CANDIDATE / SINGLE-SOURCE
**CONFIRMATION:** 1 source

## TERMS

- Plan
- Do
- Check
- Act
- PDCA cycle
- objectives
- resources
- risks
- opportunities
- processes
- results
- monitoring
- measurement
- requirements
- planned activities
- performance

## DISTINCTIONS

### DIS-001
**PDCA ≠ only continual improvement**

The source states that the PDCA cycle can be applied to all processes and to the quality management system as a whole.

**STATUS:** CANDIDATE

### DIS-002
**PLAN ≠ merely planning activities**

Plan includes establishing objectives, resources, and addressing risks and opportunities.

**STATUS:** CANDIDATE

### DIS-003
**CHECK ≠ merely measurement**

Check includes monitoring, measurement where applicable, comparison against policy, objectives, requirements and planned activities, and reporting results.

**STATUS:** CANDIDATE

### DIS-004
**ACT ≠ merely correction**

Act is defined as taking actions to improve performance, as necessary.

**STATUS:** CANDIDATE

## GM

> Управленческий цикл замыкается через планирование требуемого состояния, реализацию, проверку фактического состояния и последующее воздействие на результат.

> Планируй требуемое состояние и условия его достижения → реализуй → проверь результат относительно заданного основания → воздействуй на performance.

## REL

### REL-001
```text
PLAN
  ↓
DO
  ↓
CHECK
  ↓
ACT
  ↺
PLAN
```

**STATUS:** CANDIDATE

### REL-002
```text
OBJECTIVES + RESOURCES + RISKS / OPPORTUNITIES
                    ↓
              PLANNED STATE
```

**STATUS:** CANDIDATE

### REL-003
```text
PROCESS / RESULT
      ↓
MONITOR / MEASURE
      ↓
COMPARE AGAINST
      ↓
REPORT RESULTS
```

**STATUS:** CANDIDATE

### REL-004
```text
CHECK RESULT
     ↓
    ACT
     ↓
IMPROVED PERFORMANCE
```

**STATUS:** CANDIDATE

## MECHANISM

### M-004 — PDCA as a management mechanism

**SOURCE CLAIM:** The PDCA cycle can be applied to all processes and to the quality management system as a whole; its phases are Plan, Do, Check and Act.

**CMOC extraction:**

```text
DEFINE INTENDED STATE
        ↓
REALIZE
        ↓
OBSERVE / MEASURE
        ↓
COMPARE
        ↓
ACT
        ↓
CHANGE PERFORMANCE
        ↺
```

**CLASS:** M
**STATUS:** CANDIDATE
**CONFIRMATION:** 1 source

## CAPABILITY

### CAP-CANDIDATE — closed management cycle

Potential capability inferred from the described PDCA structure: a process/QMS can pass through planning, realization, checking and action as a closed management cycle.

**IMPORTANT:** CMOC interpretation; not a direct ISO term or claim.

**STATUS:** CANDIDATE

## CORE CANDIDATE

### CORE-CANDIDATE — closed management cycle

```text
INTENDED STATE
      ↓
ACTION
      ↓
OBSERVED RESULT
      ↓
EVALUATION
      ↓
ACTION ON PERFORMANCE
      ↺
```

Rationale: the source applies PDCA to individual processes and to the QMS as a whole, making the cycle potentially reusable at different system levels.

**STATUS:** CANDIDATE / 1 source

## MACHINE

**NONE**

Reason: the source specifies a general management mechanism and cycle, but does not yet show a concrete reproducible organizational/physical realization satisfying the CMOC Machine test.

## CHAIN

### CHAIN-CANDIDATE-002

```text
PLAN → DO → CHECK → ACT → PLAN
```

**CLASS:** CHAIN
**STATUS:** CANDIDATE / SINGLE-SOURCE

**Not MACHINE-CHAIN.** The source does not establish each PDCA phase as a separate Machine.

## CROSS-SOURCE / INTERNAL CMOC INTERPRETATION

The fragment extends the distinction established in ISO-002:

```text
PRINCIPLE
    ≠
MECHANISM
    ≠
CHAIN
    ≠
MACHINE
```

Preliminary composition with ISO-003:

```text
PROCESS APPROACH
      ↓
SYSTEMATIC MANAGEMENT OF PROCESSES + INTERACTIONS
      ↓
PDCA CYCLE
      ↓
MANAGED PERFORMANCE
```

This is a CMOC interpretation and is not canonized.

## NOT CONFIRMED

- PDCA as Machine
- separate P/D/C/A Machines
- physical realizations
- roles
- Machine-chain
- role-chain

## CANONIZATION

**NONE.**

All extracted structures remain **CANDIDATE / SINGLE-SOURCE** until confirmed by independent sources or otherwise promoted under CMOC rules.
