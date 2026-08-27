# PATCH-ISO-021

## Извещение на изменение

**0090+270826**

### SOURCE
ISO/DIS 9001:2025(en)

### LOCATION
Clause 7.1.3 — Infrastructure; Annex A.7.1.3

### SOURCE CLAIM

The organization shall determine, provide and maintain the infrastructure necessary for the operation of its processes and to achieve conformity of products and services. Infrastructure includes buildings and associated utilities; equipment, including hardware and software; transportation resources; and information and communication technology. fileciteturn57file0turn57file8

Annex A.7.1.3 explains that infrastructure can include premises, utilities, tools, equipment, transportation, communication and information systems, and may be owned, rented, leased or otherwise used. Infrastructure can also include physical and virtual resources such as servers, cloud computing, software and networks. fileciteturn57file8

### TERMS
- infrastructure
- buildings
- utilities
- equipment
- hardware
- software
- transportation
- information and communication technology
- physical resource
- virtual resource
- process operation
- conformity
- maintain

### DISTINCTIONS

**DIS-001 — INFRASTRUCTURE ≠ SINGLE PHYSICAL OBJECT**

Infrastructure is a category containing buildings/utilities, equipment, transportation and ICT, rather than a single object.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-002 — INFRASTRUCTURE ≠ PHYSICAL ONLY**

Annex A explicitly includes virtual resources such as servers, cloud computing, software and networks.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-003 — PROVIDE ≠ MAINTAIN**

7.1.3 separately requires infrastructure to be determined, provided and maintained.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-004 — INFRASTRUCTURE ≠ PROCESS**

Infrastructure enables operation of processes but is not itself thereby identical to the process.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-005 — OWNERSHIP ≠ AVAILABILITY FOR USE**

Infrastructure may be owned, rented, leased or otherwise used by the organization. Ownership is therefore not a necessary condition for organizational use.

**STATUS: CANDIDATE / SINGLE-SOURCE**

**DIS-006 — RESOURCE AVAILABILITY ≠ CONTINUED FITNESS / MAINTENANCE**

Provision of infrastructure does not eliminate the separate requirement to maintain it.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### GM

**GM-001**

> Рассматривай инфраструктуру через функцию: она определяется тем, что необходимо для operation of processes и достижения conformity.

**GM-002**

> Не связывай infrastructure только с физическими объектами: virtual resources и ICT также входят в неё.

**GM-003**

> Разделяй provision и maintenance: наличие инфраструктуры не означает её продолжающуюся пригодность.

### REL

**REL-001**

```text
PROCESS OPERATION
        ↓
INFRASTRUCTURE NEED
        ↓
DETERMINE + PROVIDE + MAINTAIN
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-002**

```text
INFRASTRUCTURE
        ↓
PROCESS OPERATION
        ↓
CONFORMITY
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-003**

```text
INFRASTRUCTURE
        ↓
PHYSICAL + VIRTUAL RESOURCES
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

**REL-004**

```text
INFRASTRUCTURE
        ↓
OWNED / RENTED / LEASED / OTHERWISE USED
```

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MECHANISM

**M-026 — Infrastructure suitability management**

```text
PROCESS NEED
        ↓
DETERMINE INFRASTRUCTURE
        ↓
PROVIDE
        ↓
MAINTAIN
        ↓
PROCESS OPERATION
        ↓
CONFORMITY
```

**CLASS: M**

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CAPABILITY

**CAP-021 — Infrastructure adequacy capability**

CMOC interpretation: ability to determine, provide and maintain the infrastructure required for process operation and conformity.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### CORE CANDIDATE

**CORE-CANDIDATE-034 — Infrastructure is function-dependent**

Infrastructure is determined by what processes require in order to operate and achieve conformity; it is not defined merely by the inventory of physical assets.

**STATUS: STRONG CANDIDATE / SINGLE-SOURCE**

**CORE-CANDIDATE-035 — Physical and virtual realization belong to one resource category**

Infrastructure can have physical and virtual realizations, including software, servers, cloud computing and networks.

**STATUS: CANDIDATE / SINGLE-SOURCE**

### MACHINE

**NONE**

The clause defines infrastructure needed for process operation but does not specify a concrete reproducible organizational construction qualifying as a Machine.

### CHAIN

**CHAIN-CANDIDATE-013 — Infrastructure provision and maintenance**

```text
PROCESS NEED
 ↓
DETERMINE
 ↓
PROVIDE
 ↓
MAINTAIN
 ↓
PROCESS OPERATION
 ↓
CONFORMITY
```

**STATUS: CHAIN-CANDIDATE / SINGLE-SOURCE**

### ROLE

**NONE**

### PHYSICAL REALIZATION

The Source gives examples of physical and virtual infrastructure, but no specific organizational realization is prescribed. **NONE as CMOC physical realization.**

### DOCUMENT / DOCUMENTED INFORMATION / RECORD

**NONE**

7.1.3 itself does not require documented information.

### CMOC INTERPRETATION

7.1.3 strengthens the line from ISO-019 and ISO-020:

```text
PROCESS / FUNCTION NEED
        ↓
REQUIRED RESOURCE
        ↓
REALIZATION
        ↓
PROCESS OPERATION
        ↓
RESULT / CONFORMITY
```

For infrastructure specifically:

```text
INFRASTRUCTURE
        ↓
PHYSICAL / VIRTUAL REALIZATION
        ↓
PROCESS OPERATION
```

The important CMOC interpretation is:

> **Infrastructure is a resource category defined by the function it enables in the system, not by whether the resource is physical, virtual, owned or externally provided.**

This is CMOC interpretation, not an ISO definition.

### CROSS-CLAUSE OBSERVATION

ISO-019 established resource suitability; ISO-020 established function-dependent people/resource realization; ISO-021 now adds infrastructure as another resource category whose adequacy is determined by process need.

A candidate structure is emerging:

```text
FUNCTION / PROCESS NEED
        ↓
REQUIRED CAPABILITY / RESOURCE
        ↓
REALIZATION
        ↓
OPERATION
        ↓
RESULT
```

This remains a **MULTI-CONFIRMATION CANDIDATE**, not a Core invariant.

### STATUS SUMMARY

- TERMS: CANDIDATE
- DISTINCTIONS: **6 NEW**
- GM: **3**
- REL: **4**
- MECHANISM: **M-026 NEW / SINGLE-SOURCE**
- CAPABILITY: **CAP-021 CANDIDATE**
- CORE CANDIDATES: **2**
- MACHINE: **NONE**
- CHAIN: **1 CANDIDATE**
- ROLE: **NONE**
- PHYSICAL REALIZATION: **NONE as CMOC realization; Source examples recorded**
- Document / Documented information / Record: **no new requirement**
- CROSS-CLAUSE: **ISO-019 + ISO-020 strengthened**
