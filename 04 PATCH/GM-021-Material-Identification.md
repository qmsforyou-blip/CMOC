# GM-021 — Material Identification

**Извещение на изменение:** 0132+280826  
**SOURCE:** GM Quality System Basics rev. March 2009  
**Section:** 2.2 — Material Identification  
**Status:** CANDIDATE / SINGLE-SOURCE

---

## SOURCE

GM states that identification of nonconforming or suspect material is paramount. Organizations shall establish a method to prevent product that does not conform to specified requirements from unintended use or installation by:

- consistent identification and visual management, including examples such as tagging, dedicated scrap bins and paint dots;
- release using a defined process and authority.

The following page provides examples of tag/status conventions: SUSPECT / DO NOT USE, OK FOR USE, SCRAP, and requirements associated with rework/reinspect/suspect material. Tag content in the shown section is left to local discretion; for scrap bins painted red, a tag is not required. The source also states that a tag should show the last operation to assure proper reintroduction. 

---

## LOCATION

Source pp. 56–57, 2.2 — Material Identification.

---

## TERMS

- nonconforming material
- suspect material
- identification
- visual management
- tag
- dedicated scrap bin
- paint dot
- DO NOT USE
- OK FOR USE
- SCRAP
- rework / reinspect
- last operation
- release
- defined process
- authority

---

## DISTINCTIONS

### DIS-GM-021-01

**Nonconforming/suspect material ≠ unidentified material.**

GM treats identification as a control requirement because the material must be prevented from unintended use or installation.

### DIS-GM-021-02

**Identification ≠ disposition.**

A visual/tagging method identifies the status of material; release is performed through a defined process and authority. The two operations must not be collapsed.

### DIS-GM-021-03

**Visual management ≠ a particular color or tag format.**

GM gives examples (tagging, dedicated scrap bins, paint dot), while the tag content shown in the section is at local discretion.

### DIS-GM-021-04

**Status identification ≠ physical location alone.**

The source combines identification with visual management and, elsewhere in the section, segregation. Identification must make status recognizable.

### DIS-GM-021-05

**Last operation is information required for controlled reintroduction.**

GM states that the tag should show the last operation to assure proper reintroduction.

---

## GM-FORMULATIONS

- “IDENTIFICATION OF NONCONFORMING OR SUSPECT MATERIAL IS PARAMOUNT.”
- Organizations shall establish a method to prevent unintended use or installation.
- Use consistent identification and visual management.
- Examples include tagging, dedicated scrap bins and paint dots.
- Release using a defined process and authority.
- Tag content in the indicated section is at local discretion.
- A tag should show the last operation to assure proper reintroduction.

---

## EXTRACTION

The source describes a status-identification control:

```text
MATERIAL
   ↓
NONCONFORMING / SUSPECT
   ↓
CONSISTENT IDENTIFICATION
   +
VISUAL MANAGEMENT
   ↓
RECOGNIZABLE STATUS
   ↓
PREVENT UNINTENDED USE / INSTALLATION
```

And a separate release path:

```text
IDENTIFIED MATERIAL
      ↓
DEFINED RELEASE PROCESS
      ↓
AUTHORIZED RELEASE
      ↓
OK FOR USE
```

For reintroduction, the source specifically links the tag to the last operation.

---

## REL

```text
Nonconforming / Suspect Material
        ↓
Consistent Identification
        ↓
Visual Management
        ↓
Recognizable Status
        ↓
Prevention of Unintended Use / Installation
```

Separate relation:

```text
Material Status
      ↓
Defined Release Process
      ↓
Authority
      ↓
Release
```

---

## MECHANISM

### CANDIDATE — Material Status Identification Mechanism

**Input:** material whose conformity status is nonconforming or suspect.

**Transformation:** apply a consistent identification / visual-management convention that makes its status recognizable.

**Output:** visibly identified material/status.

**Organizational effect:** reduces the possibility of unintended use or installation.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## CAPABILITY

**NONE**

No separate capability is extracted from this fragment.

---

## CORE CANDIDATE

> **Material Status Identification — a reproducible organizational mechanism for making the conformity status of nonconforming or suspect material visibly recognizable so that unintended use or installation can be prevented.**

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## MACHINE

### CANDIDATE MACHINE — Visual Status Identification

```text
NONCONFORMING / SUSPECT MATERIAL
             ↓
       [ IDENTIFY ]
             ↓
     VISIBLE STATUS
             ↓
    UNINTENDED USE BLOCKED
```

The engineering test is satisfied at candidate level:

- **Input:** material with a nonconforming/suspect status;
- **Transformation:** consistent visual identification;
- **Output:** recognizable status;
- **Effect:** prevention of unintended use/installation.

The particular implementation may be a tag, dedicated scrap bin or paint dot; the machine is the control function, not any one physical artifact.

**STATUS: CANDIDATE / SINGLE-SOURCE**

---

## CHAIN

### SOURCE-SUPPORTED

```text
Nonconforming / Suspect Material
        ↓
Identification / Visual Management
        ↓
Recognizable Status
        ↓
Prevent Unintended Use / Installation
```

A separate release chain is supported:

```text
Identified Material
      ↓
Defined Release Process
      ↓
Authority
      ↓
Release
```

Do not merge the two chains into one without additional SOURCE evidence.

---

## STATUS

**CANDIDATE / SINGLE-SOURCE**

No CANON status assigned.

---

## CMOC INTERPRETATION

The important engineering distinction is:

> **Identification is an intervention in the behavior of the material flow, not merely a label attached to a product.**

The relevant transformation is:

```text
UNKNOWN / AMBIGUOUS STATUS
          ↓
CONSISTENT IDENTIFICATION
          ↓
RECOGNIZABLE STATUS
          ↓
CONTROLLED USE
```

The source supports the prevention effect directly. The stronger CMOC formulation above is an interpretation, not a GM claim.

A second important distinction is that **identification does not authorize release**. GM explicitly requires release through a defined process and authority.

---

## INTER-SOURCE NOTE

Potentially relevant for later comparison with ISO/DIS 9001:2025 regarding identification/status/control of nonconforming outputs. No cross-source confirmation is asserted in this PATCH.
