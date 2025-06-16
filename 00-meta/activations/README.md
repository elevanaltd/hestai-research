# Research Activations Directory

This directory contains skills and patterns specifically designed for research work within the HestAI research repository.

## Structure

### `/skills/`
Specialized skills for research roles:
- `RESEARCH_CURATOR_SKILL_HERMES.oct.md` - Primary research curation skill

### `/patterns/`
Reusable patterns for consistent research practices:
- `CITATION_FORMAT_PATTERN.md` - Standard citation format
- `EVIDENCE_CHAIN_PATTERN.md` - Tracking claim validation
- `CROSS_REFERENCE_PATTERN.md` - Validating references between documents
- `PREVENTION_CHECKLIST_PATTERN.md` - Active prevention rules to follow
- More patterns can be added as needed

### Active Prevention Files
- `/prevention-checklist.yaml` - **START HERE** - Read before any work

## Usage

### Loading Research Skills
When activating HERMES for research work:
```bash
load HERMES_SHANK on BUILD_ARM with RESEARCH_CURATOR
```

The RESEARCH_CURATOR skill provides:
- `research_search` - Find documents by keyword/pattern
- `cross_reference` - Validate citations between documents
- `evidence_chain` - Track claim lineage
- `extract_insights` - Pull key findings with citations
- `curate_findings` - Organize discoveries by theme

### Applying Patterns
Patterns ensure consistency across all research work:

1. **Citations**: Follow CITATION_FORMAT_PATTERN.md
   - Example: "Finding" (category/document:line)

2. **Evidence**: Use EVIDENCE_CHAIN_PATTERN.md
   - Track from hypothesis → production
   - Include confidence scores

## Creating New Patterns
When you identify a repeated research practice:
1. Document it as a pattern in `/patterns/`
2. Include purpose, format, examples
3. Reference in task assignments

---
*Patterns evolve through use - suggest improvements when you find better approaches*