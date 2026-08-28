# GM-023 — Containment

**Извещение на изменение:** 0134+280826  
**SOURCE:** GM Quality System Basics rev. March 2009  
**Section:** 2.4 — Containment; 2.4.1 — Containment Worksheet  
**Status:** CANDIDATE / SINGLE-SOURCE

---

## SOURCE

GM requires Leadership to develop, organize and maintain a system for control of nonconforming product. The containment system includes a documented containment procedure to prevent identified defects from flowing to the next customer, supported by a Containment Worksheet, Quality Alert, Instructions, Operator training records, and a clear understanding of the standard and deviation supported by a visual.

For product containment issues, containers are identified by status: Red = Nonconforming product; Yellow = Suspect product; Green = after breakpoint conforming product. When sorting, nonconforming product shall not be placed into standard work-in-process or finished-goods containers.

The Containment Worksheet provides a systematic approach to containing all suspect product. It identifies potential quantity and all areas to be checked, reconciles expected suspect quantities with actual quantities, documents the defect condition and standard, records sort method and identification method, tracks results, and can trigger customer notification if an escape is possible.

---

## LOCATION

Source pp. 59–62, **2.4 — Containment** and **2.4.1 — Containment Worksheet**.

---

## TERMS

- containment procedure
- identified defect
- next customer
- Containment Worksheet
- Quality Alert
- Instructions
- Operator training records
- standard
- deviation
- visual
- Red / Nonconforming
- Yellow / Suspect
- Green / after breakpoint conforming
- sorting
- standard WIP / finished-goods containers
- potential quantity
- areas to be checked
- expected quantity
- actual quantity
- sort method
- identification method
- results
- customer notification
- escape

---

## DISTINCTIONS

### DIS-GM-023-01
**Fast Response Containment ≠ Nonconforming Product Containment.**

The same term appears in both sections, but GM-010 concerns containing the problem during problem solving, while GM-023 concerns control of suspect/nonconforming product so identified defects do not flow to the next customer.

### DIS-GM-023-02
**Identification ≠ Containment.**

GM-021 makes product status recognizable. GM-023 uses identification as one component of a broader containment system that controls the product flow.

### DIS-GM-023-03
**Segregation ≠ Containment.**

GM-022 physically separates product. GM-023 describes the broader containment system: defined procedure, status containers, sorting, scope, quantity reconciliation, documentation, result tracking, and possible customer notification.

### DIS-GM-023-04
**Suspect quantity ≠ actual affected quantity.**

The worksheet requires reconciliation of expected suspect material against actual material found.

### DIS-GM-023-05
**Sorting ≠ containment system.**

Sorting is one operation within the containment system. GM additionally requires scope definition, criteria, identification, tracking and reaction to possible escape.

### DIS-GM-023-06
**Conforming after breakpoint ≠ ordinary conforming product.**

GM gives Green a specific meaning: after-breakpoint conforming product. This is a controlled status within containment, not simply the generic state of conforming product.

---

## GM-FORMULATIONS

- “Leadership shall develop, organize and maintain a system for control of nonconforming product.”
- “A documented containment procedure to prevent identified defects from flowing to the next customer.”
- “A Containment worksheet shall be used and completed to provide a systematic approach to containing all suspect product.”
- “Identify a potential quantity and all areas to be checked for nonconforming product.”
- “Reconcile expected quantities of suspect material vs. actual.”
- “Track and document results of the containment activity.”
- “Trigger a customer notification if an escape is possible.”

---

## EXTRACTION

```text
IDENTIFIED DEFECT / SUSPECT PRODUCT
                ↓
        CONTAINMENT SYSTEM
                ↓
   ┌────────────┼──────────────┐
   ↓            ↓              ↓
DEFINE SCOPE   SORT        IDENTIFY STATUS
   ↓            ↓              ↓
POTENTIAL QTY   PASS/FAIL      GOOD / BAD
   ↓            ↓              ↓
AREAS TO CHECK  RESULTS        CONTROLLED CONTAINERS
   └────────────┼──────────────┘
                ↓
       RECONCILE EXPECTED
          VS ACTUAL
                ↓
      TRACK / DOCUMENT RESULTS
                ↓
       ESCAPE POSSIBLE?
          ↓           ↓
         NO          YES
                      ↓
             CUSTOMER NOTIFICATION
```

---

## REL

```text
Identified Defect
      ↓
Containment Procedure
      ↓
Define Potential Scope
      ↓
Check Areas / Quantities
      ↓
Sort Against Standard
      ↓
Identify Good / Bad
      ↓
Segregate into Controlled Containers
      ↓
Reconcile Expected vs Actual
      ↓
Track / Document Results
      ↓
If Escape Possible → Customer Notification
```

This relation combines the operations explicitly described across pp. 59–62; it does not imply that GM prescribes every operation as one uninterrupted real-time sequence.

---

## MECHANISM

### CANDIDATE — Product Containment Control Mechanism

**Input:** identified defect / suspect product.

**Transformation:** define containment scope, inspect relevant locations and quantities, sort against a stated standard, identify conforming/nonconforming output, place product into controlled containers, reconcile expected and actual quantities, and track results.

**Output:** controlled and accounted-for product population with documented containment status.

**Organizational effect:** prevents identified defects from flowing to the next customer and provides a basis for reaction when an escape is possible.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## CAPABILITY

**NONE**

---

## CORE CANDIDATE

> **Product Containment Control — a reproducible control mechanism that defines the scope of suspect product, checks and sorts the affected population against an explicit standard, identifies the resulting statuses, reconciles expected and actual quantities, and tracks the containment result to prevent defective product from flowing to the next customer.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## MACHINE

### CANDIDATE MACHINE — Containment Control

```text
INPUT
Identified defect / suspect product
        ↓
SCOPE
Potential quantity + areas to check
        ↓
SORT
Against defined standard
        ↓
IDENTIFY
Conforming / Nonconforming
        ↓
CONTROL
Status containers / segregation
        ↓
RECONCILE
Expected vs Actual
        ↓
TRACK / DOCUMENT
Results
        ↓
OUTPUT
Contained, accounted-for product population
        ↓
EFFECT
Defect prevented from flowing to next customer
```

The machine test is satisfied at candidate level. The **Containment Worksheet** is treated as a concrete implementation/supporting device of this machine, not automatically as the machine itself.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## CHAIN

### SOURCE-SUPPORTED CANDIDATE

```text
Defect / Suspect Product
→ Scope
→ Check Areas
→ Sort
→ Identify Good/Bad
→ Control Containers
→ Reconcile Quantities
→ Track Results
→ Customer Notification if Escape Possible
```

The source supports the individual operations and their containment purpose. The exact operational timing of every transition is not asserted beyond what the source states.

---

## STATUS

**CANDIDATE / SINGLE-SOURCE**

No CANON status assigned.

---

## CMOC INTERPRETATION

This wagonette resolves the question raised in GM-020–022: **Containment is broader than identification or segregation.**

```text
GM-021  IDENTIFY
        → make status recognizable

GM-022  SEGREGATE
        → remove product from normal flow

GM-023  CONTAIN
        → control the suspect population,
          its scope, sorting, status,
          quantity and result
```

The most important CMOC-level distinction is:

> **Containment is not merely holding defective product; it is establishing a controlled boundary around the potentially affected product population and accounting for what happens inside that boundary.**

The Containment Worksheet is especially significant because GM explicitly makes it systematic: scope, quantity, locations, criteria, identification, results and possible customer reaction are brought into one operational record.

This is a CMOC interpretation, not a GM claim about CMOC.

---

## INTER-SOURCE NOTE

Potentially relevant for later comparison with ISO/DIS 9001:2025 treatment of nonconforming outputs and controlled disposition. No cross-source confirmation is asserted in this PATCH.
