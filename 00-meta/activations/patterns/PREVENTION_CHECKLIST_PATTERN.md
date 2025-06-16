# Prevention Checklist Pattern

## Purpose
Active prevention rules learned from experience. Read this BEFORE starting work.

## Format
```yaml
MUST: "Specific action to take"
BECAUSE: "What happens if you don't (one sentence)"
```

## Prevention Checklist

### Task Planning
```yaml
MUST: "Break compound tasks into numbered items (1. Create X, 2. Move Y, 3. Update Z)"
BECAUSE: "You'll forget subtasks hidden inside broad todos"
```

### File Operations
```yaml
MUST: "Always Read before Edit, never Write to existing files"
BECAUSE: "You'll overwrite content and lose user data"
```

### Creating New Structures
```yaml
MUST: "Ask 'where should this go?' before creating new categories"
BECAUSE: "You'll clutter directories with misplaced files"
```

### Pattern Recognition
```yaml
MUST: "After 3 similar operations, stop and create a template"
BECAUSE: "You'll waste time on repetitive work that could be automated"
```

### System Alignment
```yaml
MUST: "Check for existing patterns/conventions before inventing names"
BECAUSE: "You'll create confusing inconsistencies (OOPS vs RCFP)"
```

## How Models Should Use This

1. **START HERE** - Read prevention checklist before beginning any task
2. **REFERENCE DURING WORK** - Check against list when uncertain
3. **ADD NEW RULES** - When you learn something, add a MUST/BECAUSE pair

## Collection File
Active rules in: `00-meta/activations/prevention-checklist.yaml`
Archive of sources in: `00-meta/activations/mini-rcfp-log.yaml`

## Key Difference
- Mini RCFP Log: Historical record of what went wrong
- Prevention Checklist: Active rules to follow right now

---
*Prevention is cheaper than correction*