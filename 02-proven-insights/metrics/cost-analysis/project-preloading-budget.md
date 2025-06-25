# Project Preloading Budget

## Token Budget Allocation

### Total Budget: 30,000 tokens

| Category | Budget | Purpose |
|----------|--------|---------|
| **Role Anchor** | 7,000 tokens | Core role identity and behavioral specifications |
| **Skills** | 7,000 tokens | Essential skill definitions for the task |
| **Patterns** | 5,000 tokens | Relevant patterns for the work type |
| **Principles** | 3,000 tokens | Core principles and guidelines |
| **Atomic Tasks** | 5,000 tokens | Task list and current work context |
| **Misc** | 3,000 tokens | Additional context, reminders, and utilities |

## Current Loading Analysis

### Problem Statement
Currently loading 150k+ tokens before work can begin. This is:
- Inefficient for token usage
- Slow to initialize
- Often includes unnecessary context
- Creates cognitive overload

### Optimization Goals
1. **Reduce total preload to 30k tokens maximum**
2. **Load only essential context for the specific task**
3. **Implement lazy loading for additional context**
4. **Create task-specific preload profiles**

## Analysis Categories

### 1. Role Anchor (7,000 tokens)
- Core identity
- Essential behaviors
- Primary directives
- Role boundaries

### 2. Skills (7,000 tokens)
- Only skills relevant to current task
- Prioritize by:
  - Direct relevance
  - Frequency of use
  - Task dependencies

### 3. Patterns (5,000 tokens)
- Task-specific patterns only
- Universal patterns if essential
- Exclude role-specific patterns unless actively needed

### 4. Principles (3,000 tokens)
- Constitutional laws (if applicable)
- Project-specific principles
- Quality standards

### 5. Atomic Tasks (5,000 tokens)
- Current task context
- Active task details
- Immediate dependencies
- Progress markers

### 6. Miscellaneous (3,000 tokens)
- Session notes (last relevant entries)
- Current working state
- Critical reminders
- Active warnings/issues

## Next Steps
1. Audit current preloading sequence
2. Categorize each loaded item
3. Assess token count per item
4. Determine if item fits budget category
5. Identify items for:
   - Removal (not essential)
   - Streamlining (reduce size)
   - Lazy loading (load on demand)
   - Retention (critical context)