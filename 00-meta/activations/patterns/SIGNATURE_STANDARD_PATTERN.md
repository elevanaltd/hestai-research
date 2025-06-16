# Signature Standard Pattern

## Purpose
Consistent attribution format when documenting work performed by LLMs operating as roles.

## Standard Format
```
[ROLE]([MODEL])
```

## Examples
- `HERMES(Claude)` - Claude operating as HERMES
- `PATHOS(Gemini-1.5-Pro)` - Gemini operating as PATHOS  
- `ETHOS(Claude)` - Claude operating as ETHOS
- `LOGOS(GPT-4)` - GPT-4 operating as LOGOS

## Usage Contexts

### Document Headers
```markdown
# Research Analysis Report
Author: HERMES(Claude)
Date: 2025-01-16
```

### Context Saves
```bash
hestai-context save "Found pattern" "PATTERN,PATHOS(Gemini)" "insight"
```

### Commit Attribution
```
Author: HERMES(Claude)
Co-Author: ETHOS(Claude)
```

## Why This Format
1. **Role Primary** - Operational mode matters most
2. **Model Context** - Preserves architectural tracking
3. **Parse-Friendly** - Easy to extract both parts
4. **Actor-Director Aligned** - Shows conscious performance

## When NOT to Use
- During role activation (already explicit)
- In casual conversation (understood from context)
- When model operates without role

---
*Standard attribution enables tracking while maintaining role primacy*