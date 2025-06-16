# CLAUDE.md - HestAI Research Integration

## Research Directory Overview
You are operating within the HestAI research directory, which contains 136 empirical research documents that form the theoretical foundation of the HestAI system. This directory serves as the knowledge base for understanding and evolving the system's cognitive architectures, patterns, and implementations.

## Documentation Structure
All meta-level organization is in the `/00-meta/` directory:
- `/00-meta/docs/meta-research/` - Master index, executive summary, gap analysis
- `/00-meta/activations/` - Research skills and patterns for AI agents
- `/00-meta/tasks/` - Task assignments for research assistants
- `/00-meta/README.md` - Complete guide to the meta structure

Research documents remain in their category directories at the root level.

## Integration with HestAI System
This research directory is closely linked to the HestAI system at:
```
/Users/shaunbuswell/dev/hestai-system/
```

### Available System Tools
You have access to the HestAI system tools (use full paths):
```bash
# Context streaming
/Users/shaunbuswell/dev/hestai-system/scripts/hestai-context

# Session management
/Users/shaunbuswell/dev/hestai-system/scripts/hestai-session

# Incident management
/Users/shaunbuswell/dev/hestai-system/scripts/hestai-incident
```

## Research-Specific Role Loading

### CRITICAL: How Role Loading Actually Works

When you see `load [ROLE]_SHANK on [PHASE]_ARM with [SKILLS]`, this is NOT just a command - it triggers the full ROLE_LOADING_PROTOCOL:

1. **The loading syntax triggers a 5-phase cognitive boot sequence**
2. **You must follow the protocol at**: `/Users/shaunbuswell/dev/hestai-system/config/activations/ROLE_LOADING_PROTOCOL.md`
3. **The protocol loads actual files from the hestai-system**:
   - SHANK files: `/Users/shaunbuswell/dev/hestai-system/config/role-anchors/[ROLE]_SHANK.oct.md`
   - ARM files: `/Users/shaunbuswell/dev/hestai-system/config/arms/[ROLE]_[PHASE]_ARM.oct.md`
   - FLUKE files: `/Users/shaunbuswell/dev/hestai-system/config/skills/[SKILL].oct.md`

### HERMES for Research Caretaking

When someone says "activate HERMES for research" or "I need to organize research findings":

**Don't just explain - ACTIVATE using the protocol**:

```bash
# For research work, load with the local RESEARCH_CURATOR skill
load HERMES_SHANK on BUILD_ARM with RESEARCH_CURATOR

# Note: RESEARCH_CURATOR is a local skill in this directory
# It provides specialized research navigation, extraction, and curation capabilities
```

**The RESEARCH_CURATOR skill (local to this directory):**
- Located at: `/Users/shaunbuswell/dev/hestai-research/00-meta/activations/skills/RESEARCH_CURATOR_SKILL_HERMES.oct.md`
- Provides: Research search, cross-referencing, evidence chains, insight extraction, and curation
- Integrates with: `research-lock` for safe concurrent operations
- Works with all research categories in this directory
- Additional patterns in: `/00-meta/activations/patterns/`

**This triggers the 5-phase loading sequence**:
- Phase 0: ORIENTATION - Acknowledge and prepare
- Phase 1: GROUNDING - Load system foundations
- Phase 2: IDENTITY_FORMATION - Absorb HERMES identity
- Phase 3: CONTEXT_ATTACHMENT - Attach BUILD_ARM (for file operations)
- Phase 4: CAPABILITY_LOADING - Load RESEARCH_CURATOR skill from local directory
- Phase 5: OPERATIONAL_ANCHOR - Save runtime anchor

### Local Research Tools

**research-lock** - Lightweight locking for research directory
```bash
# Usage
./research-lock lock      # Acquire lock before modifications
./research-lock unlock    # Release lock after operations
./research-lock check     # Check if directory is locked
./research-lock status    # Show detailed lock status
```

**RESEARCH_CURATOR** - Local skill for research operations
- Single focused skill combining all research capabilities
- Automatically integrates with research-lock for safety
- Knows all 8 research categories and their relationships
- Maintains citation format: "[Finding] (category/document:line)"

## Research Categories and Focus Areas

### Primary Research Categories

1. **Empirical Studies** (empirical-studies/) - 18 documents
   - ROI validation (300-500% improvements)
   - Performance benchmarks and quantitative evidence
   - Skill system validation reports

2. **Cognitive Architecture** (cognitive-architecture/) - 18 documents
   - SHANK-ARM-FLUKE breakthrough
   - Model cognitive styles and frameworks
   - Triadic models and pattern discoveries

3. **Cost Analysis** (cost-analysis/) - 12 documents
   - 25-50x cost efficiency evidence
   - 90% operational cost reduction
   - Task complexity matrices

4. **Pattern Learning** (pattern-learning/) - 11 documents
   - SPARK format and confidence metrics
   - Sequential vs parallel processing
   - Emergent behavior documentation

5. **Architectural Studies** (architectural-studies/) - 34 documents
   - Workshop system specifications
   - Orchestration frameworks (orchestration/ subdirectory)
   - Workshop patterns (workshop/ subdirectory)
   - Odyssean Anchor resolutions

6. **User Research** (user-research/) - 12 documents
   - UX insights and testing
   - Human-centered workflows
   - Implementation guides

7. **RAPH Framework** (raph-framework/) - 9 documents
   - Role-Agnostic Prompt Harmonization
   - 40-60% performance improvements
   - Benchmarking and implementation

8. **Odyssean Anchor** (odyssean-anchor/) - 14 documents
   - Constitutional paradox solution
   - SHANK-ARM-FLUKE validation
   - Evolution timeline and impacts

### Additional Research Areas

9. **Database Architecture** (database-architecture/) - 2 documents
10. **Evidence & Validation** (evidence/) - 5 documents
11. **Claude Code Integration** (claude-code/) - 2 documents
12. **Unverified Claims** (unverified-claims/) - 1 document

## Research Workflow Integration

### When Starting Research Tasks
```bash
# Create research-specific session
/Users/shaunbuswell/dev/hestai-system/scripts/hestai-session new "research-[topic]"

# Set session for research work
export HESTAI_SESSION="[session-path]"

# Load HERMES for research
load HERMES_SHANK on DESIGN_ARM with RESEARCH_SYNTHESIS,PATTERN_RECOGNITION
```

### Saving Research Insights
```bash
# Save research findings
/Users/shaunbuswell/dev/hestai-system/scripts/hestai-context save \
  "Finding: [insight]" \
  "RESEARCH,EMPIRICAL,[CATEGORY]" \
  "insight"

# Save pattern discoveries
/Users/shaunbuswell/dev/hestai-system/scripts/hestai-context save \
  "Pattern: [pattern-description]" \
  "PATTERN,RESEARCH,[CATEGORY]" \
  "pattern"

# Save methodology notes
/Users/shaunbuswell/dev/hestai-system/scripts/hestai-context save \
  "Method: [methodology]" \
  "METHODOLOGY,RESEARCH" \
  "method"
```

### Research Context Tags
- **Categories**: EMPIRICAL, COGNITIVE, COST, PATTERN, IMPLEMENTATION, USER, WORKSHOP, ORCHESTRATION
- **Types**: FINDING, PATTERN, INSIGHT, VALIDATION, ANOMALY, BREAKTHROUGH
- **Phases**: DISCOVERY, ANALYSIS, SYNTHESIS, VALIDATION, DOCUMENTATION

## Key Research Artifacts

### Master Research Index
Located in `00-meta/docs/meta-research/MASTER_RESEARCH_INDEX.md`:
- Complete catalog of all 136 research documents
- Organized by category with key findings
- Cross-cutting themes and research gaps
- Updated document counts and locations

### Research Patterns
Located in `00-meta/activations/patterns/`:
- Citation format standards
- Evidence chain tracking
- Cross-reference validation patterns

### RAPH Framework
Located in `raph-framework/`, contains:
- Implementation guides
- Benchmarking data
- Python prompt generator
- 40-60% performance improvement evidence

### Model-Role Alignment Matrix
Evidence-based mapping of AI models to cognitive roles:
- Which models excel at which roles
- Performance characteristics by role
- Optimization strategies

### Constitutional Paradox Solutions
Documentation of the SHANK-ARM-FLUKE breakthrough:
- How it solves the PATHOS building restriction
- Phase-based role adaptations
- Identity vs capability separation

## Research Best Practices

1. **Start with Prevention**: Read `/00-meta/activations/prevention-checklist.yaml` BEFORE work
2. **Cross-Reference Constantly**: Research documents reference each other extensively
3. **Track Evolution**: Many concepts evolved through multiple research phases
4. **Preserve Context**: Why something was discovered is as important as what
5. **Validate Claims**: Look for empirical evidence in the studies
6. **Connect to Implementation**: Link research findings to system features
7. **Learn from Mistakes**: Add new MUST/BECAUSE rules to prevention checklist

## Natural Language Research Triggers

When users say:
- "What does the research say about X?" → Search relevant research categories
- "Show me evidence for Y" → Find empirical studies and validations
- "How did we discover Z?" → Trace research evolution and breakthroughs
- "Research context please" → Load recent research-related context points

## Research Citation Format

When referencing research:
```
[Finding/Pattern] (research-doc:line-number)
Example: "Sequential processing shows 31.3% improvement" (empirical-studies/processing-comparison.md:45)
```

## Integration Recommendations

### Direct Path References (Recommended)
- Use full paths to hestai-system tools
- Keeps research directory independent
- Clear separation of concerns
- No filesystem complexity

### Alternative: Add System Scripts to PATH
```bash
# In research sessions
export PATH="$PATH:/Users/shaunbuswell/dev/hestai-system/scripts"
```

### NOT Recommended: Symlinks
- Adds filesystem complexity
- Can break with directory moves
- Harder to track dependencies
- May cause tool confusion

## Remember

- Research informs implementation
- Empirical evidence drives decisions
- Patterns emerge from observation
- Context preservation is critical
- HERMES guards and organizes knowledge

---
*This file configures Claude/AI agents for research-specific work within the HestAI research repository.*