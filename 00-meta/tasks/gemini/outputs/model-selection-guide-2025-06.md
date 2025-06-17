# Model Selection Guide
Generated: 2025-06-16

## Verified Cost Claims

| Claim | Source | Confidence | Caveats |
|---|---|---|---|
| Token efficiency: 20-30% reduction possible (Cognitive Genome) | cognitive-architecture/discoveries/cognitive-genome-architecture-insight.md:145 | Medium | Still requires implementation and testing. |
| Token reductions of 54.2-67.8% compared to JSON (OCTAVE) | empirical-studies/octave-validation-summary.md:38 | High | Requires proper implementation of OCTAVE protocol. |
| Non-thinking mode: $0.15/$0.60 per 1M tokens (Gemini Flash) | evidence/cost-analysis/gemini-cost-validation.md:11 | High | N/A |
| Thinking mode: $3.50 per 1M tokens (Gemini) | evidence/cost-analysis/gemini-cost-validation.md:12 | High | N/A |
| Estimated: $15-30 per 1M tokens (Opus, Sonnet, GPT-4.1) | cost-analysis/task-complexity-matrix.md:35 | Low | Requires further cost validation. |
| 90% cost reduction vs traditional models (Gemini Flash) | evidence/cost-analysis/gemini-cost-validation.md:16 | High | With equal/better quality |
| 25-50x ROI improvement with equal/better quality (Gemini Flash) | evidence/cost-analysis/gemini-cost-validation.md:17 | High | N/A |
| RAPH sequences: $0.05-0.17 per sequence | evidence/cost-analysis/gemini-cost-validation.md:18 | High | N/A |

## Model Selection Decision Tree

1. **For initial task processing and general tasks:**
   - Use Gemini Flash in non-thinking mode ($0.60/1M tokens) for 90% cost reduction.

2. **For tasks requiring structured LLM-to-LLM communication:**
   - Implement OCTAVE protocol for 54.2-67.8% token reduction compared to JSON.

3. **For complex analysis, multi-step tasks, or when higher quality is desired:**
    -  Implement the RAPH framework with Claude Sonnet, Opus, Gemini Pro (cost between $0.05-0.17 per sequence - but can vary up to 7x).

4. **When you need to understand the deeper context and relationships of an implementation:**
    - Use Gemini Pro, it will be the ideal solution for more HERMES assessment tasks

5.  **If maximum innovation/breakthrough insights are required (regardless of cost):**
    - Use Claude Opus.

6. **If maximum reasoning power is required and cost is not the primary concern:**
    - Use Gemini in thinking mode ($3.50 per 1M tokens).

7.  If you need to operate under strict limitations and maintain 95-100% understanding you can use OCTAVE.

This decision tree prioritizes cost-effectiveness while leveraging the strengths of each approach. We will need more test data to further refine specific cases, model type and task complexity.

