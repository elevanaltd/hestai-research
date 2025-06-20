# Contributing to Research Inbox

## For HestAI Roles

When working in role (HERMES, PATHOS, ETHOS, LOGOS), drop insights here:

```bash
# Quick format
echo "**Date:** $(date '+%Y-%m-%d %H:%M')
**Role/Context:** PATHOS BUILD phase
**Observation:** [what you noticed]
**Impact:** [why it matters]" > /Users/shaunbuswell/dev/hestai-research/00-meta/inbox/active/$(date +%Y-%m-%d)-brief-description.md
```

## For Automated Scripts

```python
# Python example
from datetime import datetime
import os

def log_insight(title, observation, impact, category="Tool Behavior"):
    date_str = datetime.now().strftime("%Y-%m-%d")
    time_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    content = f"""# Insight: {title}

**Date:** {time_str}
**Contributor:** Automated Script
**Context:** Automated testing
**Category:** {category}

## Observation
{observation}

## Potential Impact
{impact}

---
**Research Status:** 🔴 Unprocessed
"""
    
    filename = f"{date_str}-{title.lower().replace(' ', '-')}.md"
    filepath = f"/Users/shaunbuswell/dev/hestai-research/00-meta/inbox/active/{filename}"
    
    with open(filepath, 'w') as f:
        f.write(content)
```

## For Integration with Tools

When zen-mcp tools discover patterns:

```javascript
// After interesting tool response
const insight = {
    tool: 'mcp__zen__debug',
    pattern: 'Unexpected success with minimal thinking mode',
    context: 'Complex bug resolved with mode=low',
    timestamp: new Date().toISOString()
};

// Log to inbox
fs.writeFileSync(
    `/Users/shaunbuswell/dev/hestai-research/00-meta/inbox/active/${date}-tool-pattern.json`,
    JSON.stringify(insight, null, 2)
);
```

## Naming Convention

```
YYYY-MM-DD-brief-kebab-case-description.md
```

Examples:
- `2025-06-20-codereview-bias-discovery.md`
- `2025-06-21-pathos-creativity-burst.md`
- `2025-06-22-consensus-tool-timeout.md`

## Batch Processing

For HERMES or research synthesis:

```bash
# Review all unprocessed insights
ls /Users/shaunbuswell/dev/hestai-research/00-meta/inbox/active/

# Move processed insights
mv /Users/shaunbuswell/dev/hestai-research/00-meta/inbox/active/2025-06-20-*.md \
   /Users/shaunbuswell/dev/hestai-research/00-meta/inbox/processed/
```

---

*The inbox is write-friendly and synthesis-ready. Drop insights freely!*