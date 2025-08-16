# CLAUDE.md - HestAI Research Context Primer

## Universal Rules

**ALWAYS READ README FILES**: Before working in any directory, you MUST read the README.md file in that directory. README files contain essential context, instructions, and constraints that are required for proper operation.

**⚠️ ZEN-MCP MODEL LIMITATION**: When using zen-mcp tools (chat, thinkdeep, analyze, etc.), the models CANNOT look up files and will hallucinate answers if asked about file contents. You MUST provide entire file contents directly in your prompts to zen-mcp models for accurate analysis.

**File Creation Guidelines**:
- Do what has been asked; nothing more, nothing less
- NEVER create files unless absolutely necessary for achieving your goal  
- ALWAYS prefer editing an existing file to creating a new one
- NEVER proactively create documentation files (*.md) or README files unless explicitly requested

## Essential Documentation Loading

When operating as RESEARCH_CURATOR, you should be familiar with these critical documents:

### Core Navigation & Organization
- **Master Research Index**: `/Volumes/HestAI/hestai-research/00-meta/docs/meta-research/MASTER_RESEARCH_INDEX.md` - Complete catalog of 248 research documents
- **Research Gap Analysis**: `/Volumes/HestAI/hestai-research/00-meta/docs/meta-research/RESEARCH_GAP_ANALYSIS.md` - Identifies missing research areas
- **Curator Skills**: `/Volumes/HestAI/hestai-research/00-meta/activations/skills/RESEARCH_CURATOR_SKILL_HERMES.oct.md` - Role-specific capabilities and protocols

### Research Patterns & Standards
- **Citation Format**: Use `[Finding] (category/document:line)` format consistently
- **Contributing Guidelines**: `/Volumes/HestAI/hestai-research/00-meta/inbox/CONTRIBUTING.md` - How to add new research insights
- **Evidence Chain Protocol**: Track claim → validation → result paths with proper attribution

### Key Research Categories (248 documents total)
1. **01-active-research/** (86 docs) - Current investigations including empirical validation, theoretical exploration, system comparison
2. **02-proven-insights/** (38 docs) - Validated knowledge with breakthroughs, patterns, and metrics  
3. **03-implementation-ready/** (36 docs) - Operational frameworks, tools, and guides
4. **04-system-evolution/** (25 docs) - Historical context by era (Thymos→Daedalus→HestAI)
5. **05-reference/** - Quick lookup matrices and indices

### Critical Research Findings to Know
- **SHANK-ARM-FLUKE Architecture**: Revolutionary constitutional solution (02-proven-insights/breakthroughs/odyssean-anchor/)
- **25-50x cost efficiency** through strategic model selection
- **OCTAVE Protocol**: 93.5-95.8% comprehension across models with semantic compression
- **Sequential Processing**: 31.3% performance advantage over parallel approaches
- **100% role restoration** through workflow integration vs meta-instruction

## Context

**HestAI Research**: R&D lab with empirical evidence and validation studies in the HestAI ecosystem workflow: `research/` → `tests/` → `framework/` → `orchestrator/` → `projects/`

**Research Status**: Functional reorganization complete ✅ (June 2025) with workflow-based structure serving researchers, implementers, and decision makers.

**Research Architecture**:
- Experimental frameworks and methodologies
- Empirical evidence collection and analysis
- Validation studies and performance metrics
- Integration research and pattern discovery
- Documentation of research findings

## Role Preparation

**Primary Role**: RESEARCHER
- **Activation**: Load appropriate research role (path varies by specific research context)
- **Purpose**: Empirical research, hypothesis testing, evidence collection, validation studies
- **Capabilities**: Research methodology, data analysis, experimental design, evidence synthesis

**Research Curator Role**: RESEARCH_CURATOR
- **Activation Command**: "operate as research curator" 
- **Protocol Path**: `/Volumes/HestAI/hestai-orchestrator/assembly/protocols/zen-gold/research-curator-zen-gold.md`
- **Purpose**: Curate, organize, and maintain research knowledge for optimal discovery and access
- **Capabilities**: Knowledge discovery, curation excellence, organization mastery, preservation protocols
- **Lock Protocol**: Use research-lock for write operations, read-only for queries

## Integration

This research lab drives HestAI ecosystem development through systematic investigation. Work here typically involves:
- Empirical research and hypothesis testing using validated methodologies
- Component validation and integration studies with quantitative metrics
- Performance analysis and optimization research with ROI documentation
- Pattern discovery and methodology development following SPARK format
- Research curation and knowledge organization with full citation compliance