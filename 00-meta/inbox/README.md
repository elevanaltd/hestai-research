# Research Inbox

**Purpose:** Collection point for insights, observations, and discoveries from active development work that can be synthesized into formal research documents.

## How to Use This Inbox

### For Contributors (Roles/Models/Developers)

1. **Drop insights here** when you discover something noteworthy during work
2. **Use the template** (INSIGHT_TEMPLATE.md) for consistency
3. **Name files descriptively**: `YYYY-MM-DD-brief-description.md`
4. **Don't worry about perfection** - raw observations are valuable

### For Research Synthesis (HERMES/Research Team)

1. **Review inbox regularly** for patterns and insights
2. **Synthesize related observations** into formal research
3. **Move processed items** to `/processed/` subdirectory
4. **Update MASTER_RESEARCH_INDEX** with new findings

## Insight Categories

- **Tool Behavior**: Unexpected tool responses, biases, capabilities
- **Role Performance**: How roles perform in practice vs theory
- **Pattern Discovery**: Emergent patterns in development
- **Integration Issues**: Cross-system interaction insights
- **Performance Metrics**: Timing, token usage, quality observations
- **Failure Modes**: What breaks and why
- **Success Patterns**: What works exceptionally well

## Directory Structure

```
inbox/
├── README.md (this file)
├── INSIGHT_TEMPLATE.md
├── active/           # New insights go here
├── processed/        # Synthesized insights moved here
└── archive/          # Old processed insights
```

## Quick Drop Format

If you don't have time for the full template:

```markdown
**Date:** YYYY-MM-DD
**Role/Context:** [Who observed this]
**Observation:** [What you noticed]
**Impact:** [Why it matters]
```

## Research Pipeline

```
Observation → Inbox → Review → Synthesis → Research Doc → MASTER_INDEX
```

---

*This inbox helps capture ephemeral insights that might otherwise be lost in the flow of development work.*