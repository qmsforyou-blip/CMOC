# GM-015 — Step 4: Implement Corrective Action

**Извещение на изменение:** `0126+280826`

**SOURCE:** GM Quality System Basics Overview Supplier Audit.pdf  
**SECTION:** FAST RESPONSE → 1.3 Problem Solving → Step 4 — Implement Corrective Action  
**STATUS:** CANDIDATE / SINGLE-SOURCE

---

## SOURCE

GM Step 4 задаёт четыре операции:

1. Brainstorm possible solutions and select the most effective, efficient and cost effective solution.
2. Determine if a trial run is needed to confirm and test the proposed solution, verify that it is effective and has no other adverse effects.
3. Determine the steps and actions needed to implement and timing.
4. Identify the breakpoint of implementing to all key stakeholders.

Immediately following Step 4, GM defines Step 5 as verification of effectiveness and Step 6 as institutionalization.

## LOCATION

p. 42 of the source presentation; Step 4 — Implement Corrective Action.

## TERMS

- corrective action
- possible solutions
- effective
- efficient
- cost effective
- trial run
- verify effective
- adverse effects
- implementation steps
- timing
- breakpoint
- key stakeholders

## DISTINCTIONS

### DIS-GM-015-01 — Solution selection ≠ implementation

GM first requires generation and selection of a solution, then separately determines the steps and timing for implementation.

### DIS-GM-015-02 — Proposed solution ≠ verified solution

A trial run may be required to test the proposed solution for effectiveness and adverse effects. Verification is therefore not assumed merely because a solution has been selected.

### DIS-GM-015-03 — Implementation ≠ institutionalization

Step 4 implements the corrective action. Step 6 separately institutionalizes the solution throughout the organization.

### DIS-GM-015-04 — Implementation ≠ verification of effectiveness

Step 5 is explicitly dedicated to verification of effectiveness. Step 4 therefore does not establish effectiveness by itself.

### DIS-GM-015-05 — Implementation scope has a breakpoint

GM requires identifying the breakpoint at which implementation extends to all key stakeholders. This introduces an explicit transition point in the implementation scope.

## GM-FORMULATIONS

- “Brainstorm possible solutions and select the most effective, efficient and cost effective solution.”
- “Determine if a trial run is needed to confirm and test the proposed solution to verify it is effective and has no other adverse effects.”
- “Determine the steps and actions needed to implement and timing.”
- “Identify the breakpoint of implementing to all key stake holders.”

## REL

```text
Possible Solutions
      ↓
Selection
      ↓
Proposed Solution
      ↓
[if needed] Trial Run
      ↓
Effectiveness / adverse-effects check
      ↓
Implementation Steps + Timing
      ↓
Breakpoint
      ↓
Implementation to Key Stakeholders
```

The SOURCE does not state that a trial run is mandatory in every case; it explicitly says to determine whether one is needed.

## MECHANISM

### CANDIDATE — Corrective Action Implementation Mechanism

**Input:** selected solution addressing the established root cause.

**Transformation:** evaluate need for trial run → define implementation steps and timing → identify breakpoint → extend implementation to key stakeholders.

**Output:** corrective action implemented with defined scope and timing.

**Organizational effect:** the selected solution is converted from a proposed response into an implemented change.

**STATUS:** CANDIDATE / SINGLE-SOURCE

## CAPABILITY

NONE

The source does not directly establish a capability from this fragment.

## CORE CANDIDATE

> **Corrective Action Implementation — a structured operation for converting a selected solution into an implemented change through optional trial verification, defined implementation steps, timing, and a defined breakpoint for extension to key stakeholders.**

**STATUS:** CANDIDATE / SINGLE-SOURCE

## MACHINE

### CANDIDATE MACHINE — Corrective Action Implementation

```text
SELECTED SOLUTION
        ↓
[ IMPLEMENTATION MACHINE ]
        │
        ├── determine trial need
        ├── test proposed solution if needed
        ├── determine steps
        ├── determine timing
        └── identify breakpoint
        ↓
IMPLEMENTED CORRECTIVE ACTION
        ↓
KEY STAKEHOLDERS INCLUDED
```

The machine candidate is deliberately limited to Step 4. Effectiveness verification belongs to Step 5; organization-wide institutionalization belongs to Step 6.

## CHAIN

### SOURCE-SUPPORTED

```text
Solution Selection
→ Trial Run if Needed
→ Implementation Planning
→ Timing
→ Breakpoint
→ Implementation to Key Stakeholders
```

The broader chain continues in the SOURCE into:

```text
Step 4 Implement
→ Step 5 Verify Effectiveness
→ Step 6 Institutionalize
```

## STATUS

**CANDIDATE / SINGLE-SOURCE**

### CONFIRM / UPDATE

**UPDATE GM-014:** the system-root-cause analysis does not terminate the problem-solving chain. GM explicitly places implementation of corrective action after root-cause analysis.

**UPDATE GM-013:** finding root cause and selecting/implementing a corrective action are separate operations.

## CMOC INTERPRETATION

GM gives us a clean transition from **cause knowledge** to **system change**:

```text
ROOT CAUSE
    ↓
SELECT SOLUTION
    ↓
TEST IF NEEDED
    ↓
PLAN IMPLEMENTATION
    ↓
DEFINE BREAKPOINT
    ↓
IMPLEMENT CHANGE
```

The particularly valuable distinction for CMOC is:

> **A corrective action is not complete merely because a solution has been selected.**

There is a separate engineering operation that turns the selected solution into an implemented change, with explicit attention to testing, adverse effects, timing and implementation boundary.

No CANON is claimed from this single source.
