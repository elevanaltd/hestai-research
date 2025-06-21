# 04 - Workshop System Implementation Plan

**Date:** 2025-06-09
**Author:** LOGOS (Synthesis Architect)
**Purpose:** To outline a high-level, phased implementation plan for the Workshop System, using `/Users/shaunbuswell/dev/hestai-system` as the foundational repository for core configurations and scripts.

---

## Core Principle

Start with the absolute minimal viable system that enforces the core constraints, then iteratively add capabilities. Each step should be testable and provide demonstrable value.

---

## Phase 0: Foundation & Role Definition (Prerequisites)

*Focus: Establish stable, well-defined constitutional and structural rules for system components. Much of this may be in place but requires review and refinement for Workshop alignment.*

1.  **Finalize Core Principles & Laws (HestAI Base):**
    *   **Action:** Ensure `/hestai-system/config/foundation/hestai-laws.octave` and `/hestai-system/config/foundation/hestai-principles.octave` are stable and reflect any Workshop-specific considerations.
    *   **Status:** Mostly complete; review needed.

2.  **Define Universal SHAFT Structure Rule:**
    *   **Action:** Create a clear, documented OCTAVE-based rule/template (`SHAFT_STRUCTURE_RULE.octave`) for all Role SHAFT (identity) documents. This rule defines mandatory sections (e.g., `CORE_IDENTITY`, `OPERATIONAL_BOUNDARIES`, `TRIADIC_RELATIONSHIPS`, `ROLE_VERIFICATION_PROTOCOL`), syntax, and semantic expectations.
    *   **Needed:** `/hestai-system/config/foundation/SHAFT_STRUCTURE_RULE.octave`.

3.  **Refine HERMES SHAFT:**
    *   **Action:** Update `/hestai-system/config/role-anchors/HERMES_SHAFT.octave` to perfectly adhere to the new `SHAFT_STRUCTURE_RULE.octave`. HERMES will serve as the exemplar.
    *   **Needed:** Updated HERMES SHAFT.

4.  **Align All Other Core Role SHAFTs (PATHOS, ETHOS, LOGOS):**
    *   **Action:** Using the refined HERMES SHAFT and the `SHAFT_STRUCTURE_RULE.octave`, update or create the SHAFT documents for PATHOS, ETHOS, and LOGOS.
    *   **Needed:** Updated/Created PATHOS, ETHOS, LOGOS SHAFTs in `/hestai-system/config/role-anchors/`.

5.  **Define Basic Skill & Pattern Structure Rules:**
    *   **Action:** Similar to SHAFTs, define basic structural rules (e.g., `SKILL_STRUCTURE_RULE.octave`, `PATTERN_STRUCTURE_RULE.octave`) for `SKILL.octave` and `PATTERN.json/octave` files, outlining essential metadata and content sections.
    *   **Needed:** `/hestai-system/config/foundation/SKILL_STRUCTURE_RULE.octave`, `/hestai-system/config/foundation/PATTERN_STRUCTURE_RULE.octave`.

---

## Phase 1: Minimal Viable Workshop - Core Activation & Guarding (Weeks 1-2)

*Focus: Implement the most basic operational scripts for role activation and configuration validation. Establish the initial `./workshop` CLI entry point.*

6.  **Role Activation Scripts (`activate_role.sh <ROLE_NAME>`):**
    *   **Action:** Develop simple shell scripts (one per core role: HERMES, PATHOS, ETHOS, LOGOS).
    *   **Functionality:** Each script should `echo` a role activation message, `cat` the respective Role SHAFT (and perhaps core skills) to display identity and constraints in the Warp terminal.
    *   **Location:** `/hestai-system/scripts/activation/`.

7.  **Basic Config Guardian Script (`config_guardian_validate.sh <FILE_PATH>`):**
    *   **Action:** Create a script that performs rudimentary structural checks on a *single* staged config file (e.g., validates OCTAVE syntax, checks for a `META::` block).
    *   **Location:** `/hestai-system/scripts/validators/`.

8.  **Initial Workshop CLI Script (`./workshop`):**
    *   **Action:** Create the main `./workshop` shell script (potentially in `daedalus-project/scripts/` or a new dedicated `workshop-cli` project that references `hestai-system`).
    *   **Initial Commands:** Implement `./workshop status` (shows current active role, if any) and `./workshop chat [ROLE_NAME]` (which, for now, simply calls `activate_role.sh <ROLE_NAME>` in the current or a new Warp tab).

9.  **Warp Startup Integration (Manual Practice):**
    *   **Action:** Manually establish the practice of opening Warp with multiple tabs, each running an `activate_role.sh` for a different core role to simulate the daily startup environment.

---

## Phase 2: "Produce" Mode & Living Guardrails - MVP (Weeks 3-4)

*Focus: Develop the first version of the `./workshop produce` command, integrating basic automated governance checks (drift monitoring, reanchoring, config staging/validation).*

10. **`./workshop produce` Script - Version 1 (Intelligent Conductor MVP):**
    *   **Action:** Enhance the `./workshop` script or create a dedicated `produce.sh` sub-script.
    *   **Functionality:** Takes a simple task list file (e.g., a basic `ATOMIC-TASKS.md` or phase file) as input. For each task:
        *   Determines the appropriate Role (initially hardcoded or via a simple lookup table based on task keywords).
        *   Calls the relevant `activate_role.sh <ROLE_NAME>` in a designated Warp tab.
        *   Passes the task instruction to Warp's AI (as a natural language prompt to the activated role).
        *   Logs basic completion: `[ROLE][TASK] completed.`

11. **Lightweight Drift Monitor Script (`monitor_drift_basic.sh <OUTPUT_TEXT> <ROLE_KEYWORDS_FILE>`):**
    *   **Action:** Create a script that checks given text against a file of role-specific keywords/anti-keywords to detect basic language drift.
    *   **Integration:** Integrate this into the `./workshop produce` flow to run after significant AI output for a task.
    *   **Location:** `/hestai-system/scripts/watchers/`.

12. **Reanchor Script (`reanchor.sh <ROLE_NAME>`):**
    *   **Action:** Create a script that simply re-runs `activate_role.sh <ROLE_NAME>` to refresh the role context.
    *   **Integration:** The `./workshop produce` script should offer to run this if `monitor_drift_basic.sh` detects potential drift.
    *   **Location:** `/hestai-system/scripts/activation/`.

13. **Config Guardian Staging & Auto-validation in `produce` Flow:**
    *   **Action:** Enhance `./workshop produce`.
    *   **Functionality:** If a task output appears to be a configuration file (e.g., by file extension or content cues like `META::`):
        1.  Save it to a temporary `/hestai-system/config_staging/` directory.
        2.  Automatically call `config_guardian_validate.sh` on the staged file.
        3.  Log success/failure of validation. Halt or warn on failure.

---

## Phase 3: Enhancements & Learning (Ongoing)

*Focus: Iteratively improve the system by adding more sophisticated learning mechanisms, deeper skill integration, advanced validation, and comprehensive documentation.*

14. **Pattern & Learning Log System:**
    *   **Action:** Define directory structure (e.g., `/hestai-system/review/learning_logs/[ROLE]/[DATE].md`) and conventions for learning logs.
    *   **Integration:** Enhance `./workshop produce` to append significant successes, failures, or observed patterns to these logs.

15. **Skill System Integration:**
    *   **Action:** Refine `activate_role.sh` to also load/list skills defined as associated with the role in its SHAFT.
    *   **Enhancement:** Allow tasks in `./workshop produce` plans to specify particular skills to be active/prioritized for that task.

16. **Advanced `CONFIG_GUARDIAN` Capabilities:**
    *   **Action:** Iteratively improve `config_guardian_validate.sh` and potentially introduce new validator scripts for more sophisticated checks (e.g., cross-file dependency validation, pattern duplication detection, AI-assisted semantic validation if feasible).

17. **User Interface / Experience Refinements in Warp:**
    *   **Action:** Continuously explore Warp features (e.g., custom themes, block rendering, workflows) to provide better visual feedback on active roles, monitor status, task progress, etc.

18. **Documentation & Guides:**
    *   **Action:** Incrementally develop comprehensive documentation in `/hestai-system/docs/` and user guides in `/hestai-system/guides/` covering Workshop system usage, configuration management, pattern evolution, and troubleshooting.

---

## Order of Need (Summary)

*   **Immediate (Foundation):**
    *   Stable HestAI Laws & Principles.
    *   SHAFT Structure Rule.
    *   Refined HERMES SHAFT (as exemplar).
*   **Very Soon (Core Roles & Basic CLI):**
    *   Aligned PATHOS, ETHOS, LOGOS SHAFTs.
    *   Basic Skill & Pattern Structure Rules.
    *   Role Activation Scripts (`activate_role.sh`).
    *   Basic Config Guardian Validator (`config_guardian_validate.sh`).
    *   Initial `./workshop` CLI (with `status`, `chat` placeholders).
*   **Medium Term (Produce MVP & Initial Guardrails):**
    *   `./workshop produce` script (V1 - basic task execution).
    *   Lightweight Drift Monitor (`monitor_drift_basic.sh`).
    *   Reanchor Script (`reanchor.sh`).
    *   Integration of Config Staging & Auto-validation into `produce` flow.
*   **Longer Term (Evolution & Sophistication):**
    *   Pattern & Learning Log System.
    *   Full Skill System Integration.
    *   Advanced Config Guardian features.
    *   Warp UI/UX Refinements.
    *   Comprehensive Documentation and Guides.

---

This plan provides a structured approach to building the Workshop System, ensuring that foundational governance and operational clarity are established before more complex features are introduced. The `/Users/shaunbuswell/dev/hestai-system` directory will serve as the central repository for all core definitions, rules, and automation scripts that underpin the Workshop's functionality.

