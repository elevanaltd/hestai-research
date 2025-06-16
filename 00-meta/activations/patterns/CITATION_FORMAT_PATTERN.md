# Citation Format Pattern

## Purpose
Standardize citations across all research documents for consistency and traceability.

## Format
```
[Finding/Claim] (category/document:line)
```

## Examples
- "Sequential processing shows 31.3% improvement" (empirical-studies/processing-comparison.md:45)
- "SHANK-ARM-FLUKE solves constitutional paradox" (odyssean-anchor/core-resolution/18-shaunos-odyssean-anchor-resolution.md:127)

## Rules
1. Always include line numbers when available
2. Use relative paths from research root
3. Omit .md extension in citations
4. For multi-line findings, cite the starting line

## Special Cases
- Cross-category references: Use full path
- External references: Use [Source: External - URL]
- Uncertain line numbers: Use :~estimated-line