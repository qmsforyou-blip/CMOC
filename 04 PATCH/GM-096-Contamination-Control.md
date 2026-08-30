# GM-096 — Contamination Control

**Source:** GM Quality Systems Basics rev March 2009, Global Purchasing and Supply Chain, pp. 272–293.

## Scope

The source presents Contamination Control as a structured control system for protecting product appearance and/or function from contamination. It covers manufacturing operations, assembly, shipping/receiving and in-plant operations.

## 1. Purpose

The stated purpose is to improve part cleanliness over time through measurement, control, and process/handling improvements; establish a standardized, systematic and structured approach to monitoring and controlling contamination sources; and apply a disciplined approach when responding to issues.

## 2. Contamination control architecture

The source identifies four distinct contamination areas:

- Sediment;
- Extra Parts;
- Dirt in Paint;
- Retained Material in Castings.

Suppliers shall have procedures and work instructions for Contamination Control where appropriate. Such work instructions may require process monitoring, SPC/data collection, routine maintenance, and preventive or predictive maintenance.

The source explicitly requires contamination failure modes to be included in PFMEA and Control Plans under Process Controls.

## 3. Sediment control

The source requires an acceptable initial level of part/process cleanliness, appropriate processes and controls, specified-frequency cleanliness measurement, recording/plotting of measurements, control limits that trigger reaction plans, and corrective action to prevent nonconforming products.

Monitoring of the process is to be included in Layered Process Audits, with nonconformances considered for Fast Response.

Sediment reduction controls include:

- parts washers;
- de-burring operations;
- metal working fluid controls;
- fluid/air probe flush station controls;
- dunnage and part storage systems;
- work-station cleanliness.

Each manufacturing site shall define procedures for the method and frequency of checks required to ensure proper functionality of equipment and processes designed to remove/prevent sediment contamination.

### Parts washers

Local procedures define and maintain washer systems and their effectiveness. Minimum controls include daily verification of nozzle functionality, daily verification of washer-fluid concentration and temperature where applicable, contamination/dirt requirements, and a documented preventive-maintenance program.

### De-burring

Local procedures define and maintain deburring systems. Minimum controls include daily verification of functionality, daily verification of process parameters/settings, and a documented preventive-maintenance program.

### Metal working fluids

Local procedures define the method and frequency of checks needed to ensure fluid quality and cleanliness. Controls include fluid properties such as concentration, bacteria and tramp oil; cleanliness/particulate suspended in the fluid; and a documented preventive-maintenance program covering filtration, pumps, separators and similar equipment.

### Fluid/air probe flush stations

Local procedures define the method and frequency of checks required to ensure functionality. Controls include unobstructed probes/flush nozzles, required flow rate/pressure/direction, and preventive maintenance as required.

### Work-station cleanliness

Local procedures define and maintain cleanliness of areas that physically touch the part, such as nests, hangars and storage surfaces. Minimum controls include daily verification against an established cleanliness standard and standardized work defining cleaning methods, equipment and frequency. The source gives tape-lift testing as an example of cleanliness monitoring.

### Dunnage and parts storage

Procedures define methods to verify materials and processes involved in storage and transport so as to minimize/eliminate sediment on components. Controls include a dunnage cleaning process with frequency and method, monitoring storage areas for cleanliness, protection of finished goods during transport/storage, storage-environment controls such as temperature, humidity, dirt, dust and pests, and limitation of cardboard use.

### Purchased parts and materials

Local procedures determine which purchased components require sediment monitoring and/or cleaning before use. Requirements include defined in-house cleaning requirements where applicable, method and frequency of checks, and established acceptable limits.

## 4. Extra Parts

Extra Parts are defined as parts or materials that fall into or stick to products but are not intended to be part of the finished product.

The manufacturing site shall use process controls to eliminate or reduce Extra Parts. Examples include controlled rollovers/dump stations, prescribed assembly/rework locations, magnetic-wrench functionality, masks where parts may fall into assemblies, use of the same tools in rework as in the primary operation, Layered Process Audit verification of storage, and monitoring findings with data management/corrective action.

## 5. Clean Rooms

Where clean rooms are required, the source identifies practices including limited access, defined protective clothing, positive pressure, air locks, sticky mats, atmospheric air-quality monitoring, ESD controls, and control of chemicals detrimental to the process.

## 6. Dirt in Paint

Dirt is defined as an undesired foreign inclusion in the paint film caused by disturbances in the paint process or operation. Dirt contamination is presented as a major group of paint defects. Sources should be minimized and dirt control must be continuous and ongoing.

The source distinguishes key issues in the People and Process areas.

People controls include dirt-awareness training, self-inspection/clean-up, treating the paint shop as a clean area, communicating expectations, approved attire, personal-product restrictions, no food/drink/smoking, and restrictions on fibrous materials and paper/cardboard sources.

Process controls include prevention of paint spatter/chips/overspray, hair/clothing/towels/cardboard, conveyor lubricants, rust and minerals from condensation; communicating expectations; adherence to preventive-maintenance schedules; process monitoring; and auditing to requirements.

## 7. CMOC architectural extraction

The strongest CMOC-level distinction exposed by this section is:

> **Control begins where the system can hold a state that does not have to be directly visible.**

In the source, contamination control is not reduced to visual inspection or cleanliness activity. The control architecture is built through:

`Requirement / cleanliness standard → observable or measurable condition → measurement / verification → record → control limit / status → reaction plan → corrective action → process-control update`

The source also demonstrates a second layer:

`Control measure → verification of control functionality → preventive maintenance → evidence of effectiveness`

Thus the system controls both **the state of the product/process** and **the capability of the means used to control that state**.

## 8. CMOC significance

This extraction is retained as an architectural principle rather than as a new “machine”. The source provides a concrete GM example of how an organization can make an otherwise poorly visible condition governable through defined criteria, measurement/verification, records, limits, reactions and maintenance of the control means.

**Status:** source extraction / architectural confirmation. No new REG-001 distinction is added by this patch.