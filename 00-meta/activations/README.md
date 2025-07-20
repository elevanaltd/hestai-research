# Research Activations Directory

This directory contains skills and patterns specifically designed for research work within the HestAI research repository.

## Structure

### `/skills/`
Specialized skills for research roles:
- `RESEARCH_CURATOR_SKILL_HERMES.oct.md` - Primary research curation skill with navigation, extraction, and curation capabilities

### `/patterns/`
Reusable patterns for consistent research practices:
- `CITATION_FORMAT_PATTERN.md` - Standard citation format: "[Finding] (category/document:line)"
- `EVIDENCE_CHAIN_PATTERN.md` - Tracking claim validation from hypothesis to production
- `CROSS_REFERENCE_PATTERN.md` - Validating references between documents
- `PREVENTION_CHECKLIST_PATTERN.md` - Active prevention rules to follow
- `RESEARCH_PATTERNS_MAP.oct.md` - OCTAVE map showing pattern relationships and dependencies
- `LLM_COMPRESSED_ORGANIZATION_PATTERN.md` - Document compression strategy using parallel directory structure
- `SIGNATURE_STANDARD_PATTERN.md` - Attribution format for LLM role work: ROLE(MODEL)

### Loading Protocols
**Primary Activation**: Use `/Volumes/HestAI/hestai-orchestrator/assembly/protocols/gold/research-curator-gold.md` for role loading via the new HestAI orchestrator.

**Alternative Direct Loading**: Load via `hestai-research/CLAUDE.md` instructions which reference the orchestrator.

**Archived Legacy Templates** (available in `/00-meta/archive/activations/`):
- `HERMES_LOADING_TEMPLATE.md` - Generic HERMES loading (superseded)
- `HERMES_RESEARCH_CURATOR_SEQUENCE.md` - Old research-specific loading (superseded)

### Active Prevention Files
- `/prevention-checklist.yaml` - **START HERE** - Read before any work

## Usage

### Loading Research Skills
**Current Method**: Use the HestAI orchestrator's `execute_role` tool:
```bash
cd /Volumes/HestAI/hestai-orchestrator
./run-server.sh
# Then use execute_role(role_id="research-curator", prompt="...", files=[...])
```

**Legacy Method** (archived):
```bash
load HERMES_SHANK on BUILD_ARM with RESEARCH_CURATOR
```

The RESEARCH_CURATOR skill provides:
- `research_search` - Find documents by keyword/pattern across all 13 research categories
- `cross_reference` - Validate citations between documents and check bidirectional links
- `evidence_chain` - Track claim lineage from hypothesis to production with confidence scoring
- `insight_extraction` - Pull key findings with proper citation format
- `research_collection` - Add new findings to appropriate categories using research-lock protocol
- `pattern_recognition` - Identify recurring themes across research areas

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