# Naming Workflow Examples: The System in Action

## Example 1: Simple Case - Internal Process

### Initial Discussion
**You**: "We need a way to check if all our documentation is consistent before publishing."
**PATHOS**: "That sounds like TEMP_DOC_CHECK - scan through files, flag inconsistencies, generate report."

### Auto-Logging
```json
{
  "temp_name": "TEMP_DOC_CHECK",
  "status": "TEMP",
  "created": "2025-05-26",
  "context": "documentation workflow",
  "usage_count": 1
}
```

### Your Review (Next Day)
You see the tracker, notice TEMP_DOC_CHECK. Think: "This is just internal tooling, TEMP_ is fine for now."

**Result**: Stays TEMP_DOC_CHECK. No naming project needed. Used in scripts and internal docs as-is.

---

## Example 2: Complex Case - Important Concept

### Initial Discussion
**You**: "We keep talking about this pattern where we start permissive and gradually add constraints based on what we learn."
**PATHOS**: "Right, like TEMP_TIGHTENING_APPROACH - begin loose, observe problems, add specific rules."

### Auto-Logging
```json
{
  "temp_name": "TEMP_TIGHTENING_APPROACH",
  "status": "TEMP", 
  "created": "2025-05-26",
  "context": "system design pattern",
  "usage_count": 1
}
```

### Your Review (After Using It 3 Times)
**You**: "This TEMP_TIGHTENING_APPROACH is actually central to how we work. Let's name it properly."

### Sub-Project Creation
```
naming-suite/active-naming/TEMP_TIGHTENING_APPROACH/
├── context.md
├── candidates.md  
└── decision.md
```

**context.md**:
- Used in: workflow design, constraint protocols, learning systems
- Why it matters: Core pattern we reference constantly
- Current usage: 8 references across 3 documents

**candidates.md**:
- LOOSE_TO_TIGHT (functional, clear)
- GRADUAL_CONSTRAINT (academic-sounding)
- PERMISSION_FIRST (focuses on starting point)
- LEARN_THEN_LIMIT (action-oriented)

### Collaborative Discussion
**You**: "I like PERMISSION_FIRST - captures that we start by allowing things."
**PATHOS**: "LEARN_THEN_LIMIT emphasizes the learning trigger for adding constraints."
**ETHOS**: "PERMISSION_FIRST passes the authenticity test - immediately clear function."

### Final Decision
**decision.md**: Chose PERMISSION_FIRST - clear function, no academic inflation, works in conversation.

### Propagation
1. Update tracker: "TEMP_TIGHTENING_APPROACH" → "PERMISSION_FIRST"
2. Find-replace in documents
3. Archive the naming project folder

---

## Example 3: Dead End Case

### Initial Discussion
**LOGOS**: "We could create TEMP_META_OPTIMIZER for analyzing how our other tools perform."

### Auto-Logging
```json
{
  "temp_name": "TEMP_META_OPTIMIZER",
  "status": "TEMP",
  "created": "2025-05-26", 
  "context": "tool analysis concept",
  "usage_count": 1
}
```

### Natural Death
Concept never gets used again. After 30 days, you review:

**Your decision**: "This was theoretical nonsense. Delete it."

**Result**: Remove from tracker, no naming project needed.

---

## The Pattern in Action

**Immediate naming**: Everything gets TEMP_ instantly, no thinking required
**Attention filtering**: You decide what deserves proper naming based on actual usage
**Quality investment**: Important concepts get collaborative naming attention
**Natural selection**: Unused concepts die quietly, important ones get proper names

The system separates **naming velocity** (fast TEMP_ assignment) from **naming quality** (deliberate sub-projects for concepts that matter).

## Workflow Benefits Demonstrated

1. **No bottlenecks**: Ideas can be captured and used immediately
2. **Quality where it counts**: Important concepts get proper attention
3. **Natural filtering**: Usage patterns reveal what matters
4. **Collaborative refinement**: Multiple perspectives improve final names
5. **Clean resolution**: Each case reaches appropriate conclusion

## Key Success Metrics

- **TEMP_ concepts that stay TEMP_**: Internal tools, temporary processes
- **TEMP_ concepts that get named**: Core patterns, public interfaces, repeated concepts
- **TEMP_ concepts that die**: Theoretical ideas that don't prove useful

---

**Demonstration**: The workflow feels natural, reduces friction, and allocates naming effort where it provides real value.