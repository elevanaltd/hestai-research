# Cross-Reference Pattern

## Purpose
Ensure accuracy and completeness of references between research documents, maintaining bidirectional awareness and preventing broken citations.

## Cross-Reference Types

### 1. Direct Citations
When Document A cites specific content from Document B:
```
Document A: "RAPH shows 40-60% improvement (raph-framework/benchmarking/raph-benchmarking-evidence.md:45)"
Document B should acknowledge this citation or related finding
```

### 2. Concept Evolution
Track how concepts develop across documents:
```
Initial: "shaft concept" (cognitive-architecture/discoveries/pattern-recognition.md:23)
Refined: "SHAFT architecture" (architectural-studies/04-shaft-skills-architecture.md:12)
Final: "SHANK-ARM-FLUKE" (odyssean-anchor/core-resolution/18-shaunos-odyssean-anchor-resolution.md:45)
```

### 3. Validation References
Link hypotheses to their validations:
```
Hypothesis: (pattern-learning/initial-observations.md:15)
Validation: (empirical-studies/pattern-validation.md:78)
Implementation: (architectural-studies/pattern-implementation.md:34)
```

## Verification Process

### Step 1: Extract References
```python
# Pattern to find citations
citation_pattern = r'\(([^/]+/[^:]+):(\d+)\)'
```

### Step 2: Verify Target Exists
- Check file exists
- Verify line number is valid
- Confirm content matches citation

### Step 3: Check Bidirectionality
For significant citations, verify reverse reference:
- If A cites B's major finding, B should acknowledge A's use
- Exception: Minor utility references don't need bidirectional links

### Step 4: Track Evolution
Create chains showing concept development:
```yaml
concept: "Role Loading"
evolution:
  - stage: "Discovery"
    doc: (cognitive-architecture/initial-insights.md:34)
  - stage: "Formalization" 
    doc: (cognitive-architecture/llm-role-loading-technical-reality.md:78)
  - stage: "Implementation"
    doc: (architectural-studies/17-shaft-fluke-architecture-pattern.md:123)
```

## Common Issues to Flag

1. **Broken References**
   - File doesn't exist
   - Line number out of range
   - Content mismatch

2. **Orphaned Concepts**
   - Mentioned but never defined
   - Defined but never used

3. **Circular References**
   - A→B→C→A without progression
   - Self-referential loops

4. **Version Conflicts**
   - Outdated understanding cited as current
   - Superseded findings still referenced

## Output Format

```markdown
## Cross-Reference Validation Report

### Valid References: X/Y (Z%)

### Issues Found:

#### Broken References
- Source: (category/doc:line)
  Target: (category/doc:line) 
  Issue: [File not found|Line invalid|Content mismatch]

#### Missing Bidirectional Links
- Primary: (category/doc:line) cites Target: (category/doc:line)
  Issue: Target doesn't acknowledge primary's use

#### Concept Evolution Gaps
- Concept: "Example"
  Gap: No validation between hypothesis and implementation
```

## Usage Notes

- Focus on significant conceptual references
- Utility references (e.g., "see also") don't need full validation
- Prioritize broken references that impact understanding
- Track temporal evolution - older docs may have outdated refs

---
*Cross-referencing ensures research integrity and navigability*