# Human-Centered Naming Workflow Proposal

## Core Workflow Design

**1. Immediate Name Assignment Using TEMP_**
- **Rationale**: Using the TEMP_ prefix as an immediate, provisional label creates instant visibility for unfinalized concepts during any discussion, plan, or protocol drafting.
- **Benefit**: Acts as a clear flag for yourself and collaborators: "Needs renaming, or discussion still open."

**2. Need for a Naming-Suite or Tracker**

### Key Functions
1. **Track All Provisional Names**
   - Automatically or manually logs every TEMP_ name that appears in docs, code, or communications.
   - Centralizes the "naming debt" for ongoing visibility.

2. **Naming Workflow** 
   - Lets you or a team initiate a "naming sub-project" for any TEMP_ name—useful for concepts requiring deeper consideration, stakeholder input, or creative/brand review.
   - Captures discussion history, rationale, and alternatives considered.

3. **Status Update & Version Control**
   - When a name is finalized, update the entry and propagate changes to relevant artifacts (manually or via scripts).

## Implementation Format: JSON is Appropriate

### Why JSON Works
- **Structure**: Easily represents a list of objects, each with attributes (current temp name, proposed/final name, status, history, links, etc.).
- **Integrability**: Readable by humans and machines; compatible with scripts, bots, or manual edits.
- **Flexibility**: Supports status fields (e.g., TEMP, REVIEW, NAMED) and extensible for metadata (author, date, discussion link).

### Sample Schema

```json
[
  {
    "temp_name": "TEMP_PROTOCOL_A",
    "final_name": null,
    "status": "TEMP",
    "created": "2025-05-26",
    "last_updated": "2025-05-26",
    "discussion_link": null,
    "rationale": null
  },
  {
    "temp_name": "TEMP_PROCESS_X",
    "final_name": "MERGE_CONFLICTS",
    "status": "NAMED",
    "created": "2025-05-20",
    "last_updated": "2025-05-25",
    "discussion_link": "https://...",
    "rationale": "Direct, matches system pattern"
  }
]
```

- Add fields as needed: history, alternatives, participants, etc.

## Optional Extensions

- **Automated Extraction**: Scripts to scan codebases/docs for TEMP_ and auto-add new entries.
- **Web/GUI Interface**: Lightweight front-end for browsing, editing, and updating the naming tracker.
- **Alerts/Reminders**: Notify when TEMP_ items age past a threshold without review.

## Summary

- **JSON is a strong, future-proof format** for this use case.
- **The naming-suite/tracker provides both a practical tool and a lightweight governance model** for naming discipline.
- **This aligns with authentic, transparent naming**—no friction between idea emergence and naming responsibility.

## Implementation Options

1. **Static JSON file** - Simple, immediate implementation
2. **Automated extraction** - Scripts to detect and track TEMP_ usage
3. **Minimal UI** - Lightweight interface for naming workflow management

---

**Next step**: Decide if you want to prototype as a static JSON file, automate extraction, or build a minimal UI. Sample scripts, templates, or starter documentation can be drafted on request.