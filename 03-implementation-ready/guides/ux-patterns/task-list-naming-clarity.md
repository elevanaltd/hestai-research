# OBSERVATION: Task List Naming Confusion

**Date**: 2025-02-06
**Type**: Naming clarity issue

## PROBLEM

Everything is called "Constitutional TODO":
- CONSTITUTIONAL-TODO-RULEBOOK.md (the laws)
- CONSTITUTIONAL-TODO.md (project task lists)
- "Constitutional TODO compliance" (confusing)

This muddies the distinction between:
- The CONSTITUTION (governance/laws)
- The TASK LISTS (things following the laws)

## BETTER NAMING

**Governance Layer** (keep "Constitutional"):
- CONSTITUTIONAL-RULEBOOK.md
- CONSTITUTIONAL-LAWS/
- Constitutional compliance

**Implementation Layer** (new names):
- ATOMIC-TASKS.md
- PRIME-TASKS.md
- PROJECT-TASKS.md
- VERIFIED-TASKS.md

## BENEFITS

- Clear separation of governance vs implementation
- "ATOMIC" emphasizes small, testable units
- "PRIME" could reference the PRIME command
- Less intimidating than "Constitutional"
- Easier to understand hierarchy

## EXAMPLE

Instead of:
"Create a Constitutional TODO following the Constitutional TODO Rulebook"

Better:
"Create ATOMIC TASKS following the Constitutional Rulebook"

Or:
"Create a PRIME TASK LIST per Constitutional Law"