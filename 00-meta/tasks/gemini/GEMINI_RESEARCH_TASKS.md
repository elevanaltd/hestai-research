# Gemini Flash Research Assistant Tasks

## Task 1: Implementation Readiness Audit (Start Here)

### Objective
Create a comprehensive audit of research findings that are ready for implementation in the hestai-system.

### Specific Instructions

1. **Search for Implementation Markers**
   ```
   Search for these patterns across all research documents:
   - "ready for implementation"
   - "validated and tested"
   - "production ready"
   - "MVP complete"
   - "empirically validated"
   ```

2. **Create Implementation Matrix**
   For each finding, document:
   - Finding: [Brief description]
   - Source: [category/document:line]
   - Evidence Level: [Empirical|Theoretical|Prototype]
   - Implementation Status: [Not Started|In Progress|Complete]
   - Blockers: [Technical|Resource|Priority|None]
   - Priority: [High|Medium|Low]

3. **Focus Categories** (in order):
   - architectural-studies/workshop/ (Workshop system ready?)
   - raph-framework/implementation/ (RAPH ready?)
   - empirical-studies/ (What's been validated?)
   - pattern-learning/ (Which patterns are stable?)

4. **Output Format**
   Create a new file: `implementation-readiness-audit-2025-01.md` with:
   ```markdown
   # Implementation Readiness Audit
   Generated: [Date]
   
   ## Summary Statistics
   - Total Findings: X
   - Ready for Implementation: Y
   - Blocked: Z
   
   ## High Priority Items
   [Items with empirical validation + no blockers]
   
   ## Implementation Matrix
   [Detailed findings table]
   
   ## Recommendations
   [Top 5 items to implement first]
   ```

### Success Criteria
- Find at least 20 implementation-ready findings
- Identify clear blockers for non-implemented items
- Provide actionable priority list

## Task 2: Cost Model Validation (After Task 1)

### Objective
Verify all cost efficiency claims and build a model selection guide.

### Specific Instructions

1. **Extract All Cost Claims**
   Search for:
   - Percentage improvements (e.g., "90% reduction")
   - Cost multipliers (e.g., "25-50x")
   - ROI figures (e.g., "300-500% ROI")
   - Dollar amounts or token costs

2. **Verify Each Claim**
   For each cost claim:
   - Original Claim: [Quote]
   - Source: [category/document:line]
   - Supporting Data: [Link to benchmark/study]
   - Confidence: [High|Medium|Low]
   - Caveats: [When it doesn't apply]

3. **Build Decision Tree**
   Create logic for model selection:
   ```
   IF task_complexity = "simple" AND volume = "high"
     THEN use Gemini Flash (25-50x savings)
   ELIF ...
   ```

## Task 3: Research-to-Reality Bridge (After Task 2)

Map all research findings to actual hestai-system implementations.

## Getting Started

### Prerequisites
1. Load HERMES for research work:
   ```
   load HERMES_SHANK on BUILD_ARM with RESEARCH_CURATOR
   ```
   Identity acknowledgment: "I am Gemini Flash operating as HERMES for research curation"
   
2. Read `/00-meta/activations/prevention-checklist.yaml` BEFORE starting
3. Review patterns in `/00-meta/activations/patterns/`:
   - CITATION_FORMAT_PATTERN.md
   - EVIDENCE_CHAIN_PATTERN.md
   - CROSS_REFERENCE_PATTERN.md

### Task Execution
1. Confirm HERMES activation: "As Gemini Flash operating as HERMES, I'm ready for research work"
2. Begin with Task 1
3. Use RESEARCH_CURATOR capabilities for all research operations
4. Create output files in: `/00-meta/tasks/gemini/outputs/`
5. Report progress after completing each major section
6. Maintain awareness: You are Gemini Flash performing HERMES protocols, not becoming HERMES

### Quality Standards
- Follow citation format: `(category/document:line)`
- Use evidence chain pattern for validation levels
- Distinguish empirical evidence from theoretical proposals
- Note temporal context (findings may have evolved)
- Use `./research-lock lock` before creating files
- Use `./research-lock unlock` after file operations

Good luck! Start with Task 1 and report your initial findings.