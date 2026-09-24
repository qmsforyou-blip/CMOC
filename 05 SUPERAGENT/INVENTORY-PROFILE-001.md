# INVENTORY-PROFILE-001 — Реальный профиль адресуемости CMOC

**ID:** INVENTORY-PROFILE-001  
**Date:** 24-09-2026  
**Status:** DESIGN / ARCHITECTURE CANDIDATE — v0.1  
**Basis:** STD-0001 Universal CMOC Object + current CMOC-INVENTORY-001 + build_cmoc_object_index.py

## 1. Purpose

Fix the currently evidenced structural rules that the future production INVENTORY-BUILDER must use.

This profile does not invent a new CMOC object model. It records rules already evidenced by the current repository inventory and OBJECT INDEX builder.

## 2. Primary object rule

STD-0001 requires:

- every CMOC object has a unique identifier;
- every object has a passport;
- passport is at the beginning of the file;
- minimum passport fields are id, type, status, title, source, created, tags;
- objects without an identifier do not exist in CMOC.

Therefore a future production Inventory Builder must not treat an arbitrary Markdown file as a CMOC object merely because it contains an identifier-like string.

## 3. Existing structural object classes

The current build_cmoc_object_index.py explicitly maps these Inventory classes to object types:

- TERM_FILE → TERM
- DISTINCTION_FILE → DISTINCTION
- GM_FORMULATION_FILE → GM_FORMULATION
- MACHINE → MACHINE
- CHAIN → CHAIN
- PATTERN → PATTERN
- LAW → LAW
- OBSERVATION → OBSERVATION
- ORGANIZATIONAL_CONSTRUCTION → ORGANIZATIONAL_CONSTRUCTION

This mapping is existing implementation evidence, not a new semantic classification proposal.

## 4. Existing addressability mechanisms

The current OBJECT INDEX builder uses two structural mechanisms:

### A. OBJECT_FILE

For Inventory-classified object files it:

1. reads the file;
2. reads YAML frontmatter;
3. attempts explicit object identity from fields:
   - id
   - machine_id
   - chain_id
   - pattern_id
   - law_id
   - observation_id
   - construction_id
4. otherwise checks permitted identifier patterns in filename/stem;
5. rejects unresolved object_id.

### B. REGISTRY_RECORD

The current builder additionally derives addressable records from fixed CMOC Core registries:

- LAB-000 → TERM
- LAB-002 → DISTINCTION
- LAB-004 → INVARIANT
- LAB-005 → ORGANIZATIONAL_CONSTRUCTION

These are structural registry records, not object files.

## 5. Existing identifier patterns

The current builder explicitly recognizes:

- T-\d{4}
- DIS-\d+
- LAB-\d+
- MC-[A-Z0-9-]+
- CHAIN-[A-Z0-9-]+
- MP-[A-Z0-9-]+
- LAW-\d+
- OBS-\d+
- OC-\d+

These patterns must be treated as existing repository evidence.

They must not be expanded by the future Builder without an explicit architectural decision.

## 6. Explicit exclusions

The current builder excludes the following Inventory-classified paths from OBJECT_FILE indexing:

- 000 База/01 Термины/01 База Термины.base
- 000 База/02 Различения/02 база различения.base
- 000 База/02 Различения/Без названия.md
- 000 База/03 GM-формулировки/03 GM формулировки.base
- 03_MACHINE-CATALOG/MACHINES/MACHINE-CANDIDATES.md
- 07 К/LAW/Реестр LAW.md.md

This exclusion list is existing implementation evidence.

It should not be silently generalized to other files.

## 7. Consequence for INVENTORY-BUILDER

The production Builder should therefore not start from:

all .md files = CMOC objects

It should start from:

configured structural scope → existing classification rules → addressability check → inventory record

The Builder must distinguish:

- addressable object representation;
- addressable registry record;
- repository/infrastructure file;
- unresolved structural representation;
- duplicate/conflicting addressable representation.

## 8. Provenance

The current Inventory and OBJECT INDEX already preserve:

- repository;
- branch/state;
- source commit;
- inventory snapshot;
- file path or registry container;
- structural representation kind.

The future Builder must preserve equivalent provenance.

## 9. Important unresolved point

The current repository contains a mixture of:

- STD-0001 passport-governed object files;
- registry-derived addressable records;
- machine/runtime infrastructure;
- standards;
- patches;
- repository support files.

Therefore the production Builder must use the existing structural classification boundary rather than attempting to infer CMOC objecthood from Markdown syntax alone.

## 10. Acceptance consequence

Before production implementation, the acceptance test must be extended from a synthetic fixture with an explicit object marker to fixtures representing the two real mechanisms already evidenced:

1. OBJECT_FILE with STD-0001-style YAML passport;
2. REGISTRY_RECORD from an explicit CMOC Core registry.

The test must also include at least one current explicit exclusion.

## 11. Status

DESIGN / ARCHITECTURE CANDIDATE — v0.1.

This profile is the bridge from the synthetic INVENTORY-BUILDER-001 acceptance test to the real CMOC repository structure. It does not yet authorize production implementation.
