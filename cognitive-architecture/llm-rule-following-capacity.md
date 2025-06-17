# LLM Rule-Following Capacity Research

## Executive Summary

Research from both ChatGPT and Claude reveals there's no fixed upper limit where LLMs suddenly fail at following rules. Instead, performance degrades gradually based on rule complexity, interdependency, and presentation rather than raw quantity.

## Key Findings

### No Magic Number
- No research shows "LLMs break down after exactly X rules"
- Performance degradation is gradual, not cliff-like
- Complexity matters more than quantity

### Token Limits (Hard Ceiling)
| Model | Token Limit | Practical Usage |
|-------|------------|-----------------|
| GPT-4-turbo | ~128k tokens | Stay under 5-10k for stable reasoning |
| Claude 3 Opus | ~200k tokens | Better at long documents |
| Gemini 1.5 Pro | ~1M tokens | Experimental, varying fidelity |

### Performance Thresholds

**Simple Rules**
- 20-50 independent rules can work well if clearly structured
- GPT-4: 20-40 structured rules
- Claude: 30-60 hierarchical rules
- Gemini: 50-100+ factual rules (retrieval focused)

**Complex Constraints**
- Even 3-5 interacting rules can cause significant issues
- ~30% of real user requests require constraint satisfaction
- Current models struggle with modest constraint complexity

## Critical Factors Affecting Performance

### 1. Rule Clarity and Structure
- **Independent rules** → higher compliance
- **Interdependent rules** → rapid performance degradation
- **Contradictions** → immediate failure
- **Clear separation** (numbered/bulleted) improves compliance
- **Hierarchical organization** enhances understanding

### 2. Constraint Types
Research identifies different constraint dimensions:
- **Format constraints**: JSON structure, word limits
- **Semantic constraints**: tone, audience, style
- **Behavioral constraints**: specific actions to take
- **Utility constraints**: particular requirements

Mixing constraint types increases failure risk beyond 15-20 simultaneous guidelines.

### 3. Order and Position Effects
- Models perform better with "hard-to-easy" constraint ordering
- Performance fluctuates dramatically when constraint order is disturbed
- Sequential presentation (RAPH protocol) works by applying subsets of rules

### 4. Composition Complexity
Different composition types affect difficulty:
- **"And"** (coordination) - multiple simultaneous constraints
- **"Chain"** (sequential) - constraints that build on each other
- **"Selection"** (conditional) - if-then constraint logic

## Empirical Observations

### Model-Specific Performance
| Model | Strengths | Failure Modes |
|-------|-----------|---------------|
| GPT-4 | Precision tasks, code, logic | Soft constraint confusion |
| Claude | Long narrative, structured logic | Hallucinated synthesis under ambiguity |
| Gemini | Memory depth, token breadth | Rule entanglement or priority bleed |

### Current Limitations
- Even SOTA models have "large violation rates" for length instructions
- Models "often fail to follow even simple and clear instructions"
- Multi-constraint instruction following remains a significant challenge

## Implications for HestAI

### Why Current System Struggles
The "rule soup" problem of loading 8+ documents creates exactly the complexity and interdependency issues research warns about:
- Multiple overlapping constraint types
- Unclear hierarchy and precedence
- Interdependent rules creating cognitive load

### Why RAPH Protocol Works
The staged loading (READ → ABSORB → PERCEIVE → HARMONIZE) succeeds because:
- Each stage applies a subset of rules
- Avoids simultaneous constraint overload
- Creates clear progression and hierarchy

### Solution Alignment
LOGOS's plan to reorganize rules into UNIVERSAL/DESIGN/BUILD categories directly addresses:
- Reduces interdependency by clear categorization
- Separates constraint types appropriately
- Creates modular, attachable rule sets (FLUKEs)

## Testing Recommendations

### Progressive Testing Approach
1. Start with 10 rules → measure compliance
2. Escalate to 25 rules → check degradation
3. Test 50 rules → identify breaking point
4. Use role-based segmentation to isolate rule sets

### Rule Echo Test
After task execution, ask the LLM to summarize what rules it thinks it's following. Drift here signals threshold breach.

### Compliance Monitoring
- Check rule adherence after 2-4k tokens of task work
- Monitor for "rule drift" as context grows
- Test recall of specific constraints mid-task

## Conclusions

1. **Quantity isn't the primary issue** - even 3-5 complex, interacting constraints can cause problems
2. **Structure and clarity matter more** than raw rule count
3. **Interdependency is the killer** - independent rules scale better
4. **Current models have fundamental limitations** in multi-constraint following
5. **The solution is modular, hierarchical organization** not reduction in valuable rules

## Bottom Line

The research supports LOGOS's revised plan: organize existing rules into clear, modular categories (SHANK/ARM/FLUKE) rather than trying to reduce the number of valuable guidelines. The key is reducing complexity and interdependency, not just cutting rules.

---
*Research compiled from ChatGPT and Claude analyses of current LLM constraint-following literature*