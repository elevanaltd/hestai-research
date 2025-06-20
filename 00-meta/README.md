# 00-meta: Research Organization Hub

This directory contains all meta-level organization for the HestAI research repository.

## Structure

### `/docs/`
High-level documentation and indices:
- `meta-research/` - Master index, executive summary, gap analysis
- `README.md` - Documentation structure guide

### `/activations/`
Research-specific skills and patterns for AI agents:
- `skills/` - Specialized skills like RESEARCH_CURATOR
- `patterns/` - Reusable patterns for research work
- Used when activating roles for research tasks

### `/tasks/`
Task assignments and tracking:
- `gemini/` - Tasks for Gemini Flash assistants
- `completed/` - Archive of completed tasks
- Future task categories can be added as needed

### `/inbox/` 
Research insight collection point:
- `active/` - New insights and observations
- `processed/` - Insights synthesized into research
- `archive/` - Historical processed insights
- Drop observations here for research synthesis

## Usage

### For HERMES Research Work
```bash
load HERMES_SHANK on BUILD_ARM with RESEARCH_CURATOR
# Skill loaded from: 00-meta/activations/skills/RESEARCH_CURATOR_SKILL_HERMES.oct.md
```

### For Task Assignment
1. Create task files in appropriate subfolder
2. Reference patterns from `/activations/patterns/`
3. Move to `completed/` when done

### For Documentation
- Master index: `docs/meta-research/MASTER_RESEARCH_INDEX.md`
- Gap analysis: `docs/meta-research/RESEARCH_GAP_ANALYSIS.md`
- Executive summary: `docs/meta-research/EXECUTIVE_SUMMARY.md`

## Naming Convention
The `00-` prefix ensures this meta directory appears first in listings, making it easy to find organizational materials.

---
*Last updated: June 2025*