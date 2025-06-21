# Workshop System Specification

**Version:** 1.0
**Date:** 2025-06-09
**Status:** Approved for implementation

---

## Purpose
To establish a unified, practical system—the Workshop—that enables structured clarity-building and efficient execution for AI-augmented collaborative work. Designed to address both exploratory, collaborative design and automated task production, the Workshop operates with strict role governance, configuration guardianship, and empirical, stepwise expansion.

---

## System Overview

The Workshop is a role-activated, script-driven collaborative environment integrating Warp Terminal, constitutional anchoring, and continuous system evolution. It consists of two primary modes:

1. **Collaborative Design Mode:**
   - Structured, multi-role dialogue for clarity-building and creative problem-solving when requirements are unknown or evolving.
   - Produces refined requirements, solution patterns, and rationale artifacts for reuse.

2. **Production Mode:**
   - Automated execution of well-understood tasks based on previously established patterns or clear requirements.
   - Actions coordinated via shell scripts and configuration-driven workflows.

Evolution, validation, and system integrity are maintained by configuration guardianship, real-time monitoring, and progressive learning logs.

---

## Architectural Principles

1. **Do Not Rebuild Proven Infrastructure:**
   - Warp Terminal is the orchestration/activation surface; do not replicate its capabilities.
2. **Strict Role Boundaries:**
   - PATHOS, ETHOS, LOGOS, HERMES roles are anchored in separate config files; council authorship only.
   - No self-authoring of role/identity/config documents; HERMES preserves only.
3. **Odyssean Anchor for Reliability:**
   - Identity, skills, and patterns loaded on session start.
   - /reanchor and live monitoring mandatory; session logs fuel learnings/pattern promotion.
4. **Centralized Config Guardian:**
   - All config changes routed via a single validation process (CONFIG_CURATOR or equivalent).
   - Request-based or git-based change flow with full audit/logging and drift detection.
5. **Empirical/Iterative Expansion:**
   - Start minimal (single role activation, config guardian, monitor); expand after validation.
   - All added complexity must demonstrate utility and preserve operational clarity.

---

## File/Directory Structure (Reference)

- `/hestai-system/config/` — Anchors (roles), skills, patterns, rules, protocols in strict subfolders
- `/hestai-system/scripts/` — Shell scripts for role activation, config validation, monitoring, reanchoring
- `/hestai-system/docs/` — Principle documents, system rationale, explanation/guides
- `/hestai-system/guides/` — Operational guides, review checklists
- `/hestai-system/review/` — Session logs and pattern learning artifacts

---

## Operational Flow

1. **Daily Startup**
    - `warp` opens workspace
    - Each tab: runs role activation script (PATHOS, ETHOS, LOGOS, HERMES)
    - Context loads—anchor, skills, patterns—displayed and constrained
    - No config changes occur except by guarded request
2. **Collaborative Mode**
    - Run `./workshop chat`
    - Engages roles in structured dialogue; context, constraints, and purpose tracked
    - Emerging requirements and solution patterns are saved as artifacts
3. **Production Mode**
    - Run `./workshop produce [pattern|task]`
    - Loads requirements, applies solution pattern, executes automated flow
    - All outputs logged; failures analyzed in post-session review
4. **Config Change Workflow**
    - All /config/ change requests submitted via protocol
    - Validator/enforcer script audits, logs, and applies approved edits
    - Changes reflected in next session startup; all changes auditable
5. **Learning/Evolution**
    - Monitors track boundary drift, pattern successes/failures
    - Session logs and learning patterns reviewed weekly
    - Only proven, valuable patterns are promoted; bloat avoided

---

## Role Governance Summary

- **PATHOS:** Pattern discovery, visioning, ideation—never implements or enforces
- **ETHOS:** Constraint enforcement, validation—never implements, only verifies
- **LOGOS:** Solution synthesis, architectural planning/execution—never pure ideation
- **HERMES:** Steward/config guardian—preserves only, never authors
- **Triadic council (PATHOS/ETHOS/LOGOS)** authors/updates all roles/configs
- All role/config changes must follow explicit declaration, handoff, and validation protocols

---

## Constraints

- No self-editing or cross-boundary mutation by roles
- Empirical then expand: stepwise progression enforced
- Every session anchored; all config edits validated and auditable
- Always allow emergency/manual override with logging
- Only add complexity after measured and validated benefit

---

## Initial Implementation Plan

1. Author clean anchor/config files for all roles (OCTAVE or YAML)
2. Implement shell scripts for role activation and context display (single tab/test)
3. Build/enable config guardian/validator
4. Set up session monitor, /reanchor capability, and pattern log/archive directory
5. Implement `./workshop chat` and `./workshop produce` scripts (minimal viable)
6. Document operational cycle, review protocol, and pattern promotion plan

---

## Success Criteria

- Role activation and separation validated in daily use
- All config changes pass guardian protocol, with logs
- Patterns and system logic evolve only through empirical validation
- No bloat: only effective, used patterns or scripts are promoted
- Users can reliably navigate from unclear need (chat) to clear outcome (produce) within the Workshop

---

## Appendix: Command/Script Reference

- `./workshop chat` — Structured role dialogue, clarity-building
- `./workshop produce <task|pattern>` — Pattern-driven, automated workflow execution
- `./workshop status` — Display workspace and config state
- `./workshop review` — Collaborative artifact review
- `./workshop forge` — Config curation (HERMES/guardian only)

