# GM-022 — Segregation

**Извещение на изменение:** 0133+280826  
**SOURCE:** GM Quality System Basics rev. March 2009  
**Section:** 2.3 — Segregation  
**Status:** CANDIDATE / SINGLE-SOURCE

---

## SOURCE

GM requires all nonconforming and suspect product to be segregated to prevent unintended use or installation through containment. At the end of each shift, nonconforming product should be counted, documented, and removed from the process/manufacturing area to an off-line designated containment area or scrap containers.

Segregation areas shall be foot-printed or otherwise identified. Examples include scrap bins, rework tables, containment areas, and nonconforming material hold areas.

A method to inventory nonconforming material is required, including Date, P/N, Defect, and MRB disposition.

---

## LOCATION

Source p. 58, **2.3 — Segregation**, Control of Nonconforming Product.

---

## TERMS

- nonconforming product
- suspect product
- segregation
- unintended use or installation
- counted
- documented
- off-line designated containment area
- scrap containers
- segregation area
- foot-printed / identified
- inventory
- Date
- P/N
- Defect
- MRB disposition

---

## DISTINCTIONS

### DIS-GM-022-01
**Identification ≠ Segregation.**

GM-021 makes status recognizable. GM-022 adds physical/locational separation of the material from the normal process flow.

### DIS-GM-022-02
**Segregation ≠ mere relocation.**

The purpose of segregation is explicitly to prevent unintended use or installation. Location therefore functions as a control condition, not merely storage.

### DIS-GM-022-03
**Segregation ≠ inventory.**

Physical separation and inventory/documentation are distinct requirements. GM requires both.

### DIS-GM-022-04
**Segregation area ≠ arbitrary space.**

The area must be foot-printed or otherwise identified; examples are defined containment locations.

### DIS-GM-022-05
**Count/document ≠ disposition.**

Inventory information includes MRB disposition, but this does not mean that counting or documenting itself constitutes disposition.

---

## GM-FORMULATIONS

- “All nonconforming and suspect product shall be segregated to prevent unintended use or installation through containment.”
- “At the end of each shift, non-conforming product should be counted, documented, and should be removed from the process/manufacturing area to an off line designated containment area or into scrap containers.”
- “Segregation areas shall be foot printed or otherwise identified.”
- “A method to inventory non-conforming material is required (Including Date, P/N, Defect, MRB disposition).”

---

## EXTRACTION

```text
NONCONFORMING / SUSPECT PRODUCT
              ↓
       SEGREGATION
              ↓
┌──────────────────────────────────┐
│ designated / identified area     │
│ or scrap container               │
└──────────────────────────────────┘
              ↓
   NORMAL FLOW IS BYPASSED
              ↓
UNINTENDED USE / INSTALLATION PREVENTED
```

Parallel control record:

```text
SEGREGATED MATERIAL
        ↓
COUNT
        ↓
DOCUMENT / INVENTORY
        ↓
Date + P/N + Defect + MRB disposition
```

---

## REL

```text
Nonconforming / Suspect Product
        ↓
Identification (GM-021)
        ↓
Segregation (GM-022)
        ↓
Controlled location / physical separation
        ↓
Prevention of unintended use or installation
```

A separate supporting relation is:

```text
Segregated Material
        ↓
Count
        ↓
Document / Inventory
        ↓
Traceable status information
```

---

## MECHANISM

### CANDIDATE — Physical Segregation Mechanism

**Input:** nonconforming or suspect product.

**Transformation:** remove the material from normal process/manufacturing flow and place it in an identified/defined segregation location or scrap container.

**Output:** material physically separated from normal product flow.

**Organizational effect:** reduces/prevents unintended use or installation.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## CAPABILITY

**NONE**

---

## CORE CANDIDATE

> **Physical Segregation — a reproducible control mechanism that removes nonconforming or suspect material from normal product flow and places it in an identified location or container to prevent unintended use or installation.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## MACHINE

### CANDIDATE MACHINE — Physical Segregation

```text
INPUT
Nonconforming / Suspect Product
        ↓
OPERATION
Remove from normal flow
        ↓
Place in identified segregation area
or scrap container
        ↓
OUTPUT
Physically separated material
        ↓
EFFECT
Unintended use / installation prevented
```

The source provides the input, physical transformation, controlled output condition, and intended organizational effect. The concrete forms (scrap bin, rework table, containment area, hold area) are implementations, not the machine itself.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## CHAIN

### SOURCE-SUPPORTED

```text
Nonconforming / Suspect Product
        ↓
Segregate
        ↓
Identified / designated location
        ↓
Count + Document / Inventory
        ↓
Controlled material status
```

Do not infer from this fragment that segregation itself determines final disposition.

---

## STATUS

**CANDIDATE / SINGLE-SOURCE**

No CANON status assigned.

---

## CMOC INTERPRETATION

GM-021 and GM-022 expose two different control transformations:

```text
GM-021
MATERIAL STATUS
    ↓
BECOMES RECOGNIZABLE

GM-022
MATERIAL
    ↓
BECOMES PHYSICALLY SEPARATED
```

The important engineering point is that **visual recognition alone is not equivalent to physical control of the flow**. GM adds a spatial/physical barrier to unintended use or installation.

At the same time, the source couples segregation with counting, documentation and inventory. This creates a traceable population of segregated material, but the source fragment does not yet establish that inventory is itself a machine or that it determines disposition.

This interpretation is CMOC analysis, not a GM claim about CMOC.

---

## INTER-SOURCE NOTE

Potentially relevant for later comparison with ISO/DIS 9001:2025 concepts concerning nonconforming outputs and control, but no cross-source confirmation is asserted here.
