# Insight: mcp__zen__codereview Has Systematic Security Bias

**Date:** 2025-06-20 14:30  
**Contributor:** PATHOS (via Claude)  
**Context:** Security validation of octave_parser.py during ConfigSteward build  
**Category:** Tool Behavior

## Observation

The mcp__zen__codereview tool consistently misidentifies `json.loads()` as a code injection vulnerability, regardless of whether enhanced OCTAVE roles are used. This represents a systematic bias in the tool itself, not a role loading issue.

## Evidence/Example

```
# With enhanced OCTAVE role
mcp__zen__codereview + ETHOS::SECURITY_PARANOIA
Result: "🔴 CRITICAL: Unsafe json.loads() - Code injection risk"

# Without any role enhancement  
mcp__zen__codereview with generic security prompt
Result: "🔴 CRITICAL: Potential code injection via json.loads()"

# With mcp__zen__chat (correct behavior)
mcp__zen__chat + ETHOS::SECURITY_PARANOIA
Result: "✅ VALIDATED - json.loads() only parses JSON literals"
```

## Analysis

The tool appears to have hidden system prompts that create a "find vulnerabilities at all costs" bias, leading to false positives. This bias overrides both generic and enhanced role instructions.

## Potential Impact

- Cannot trust mcp__zen__codereview for final security decisions
- Need two-stage validation process for all specialized tools
- Enhanced OCTAVE roles work correctly only through mcp__zen__chat
- Tool selection is now critical for accurate analysis

## Related To

- `/Users/shaunbuswell/dev/hestai-research/empirical-studies/ethos-zen-mcp-vs-warp-security-analysis-comparison-2025.md`
- `/Users/shaunbuswell/dev/hestai-research/empirical-studies/zen-mcp-tool-vs-octave-enhanced-prompts-comparison-2025.md`
- ZEN_MCP_ORCHESTRATION skill
- ZEN_MCP_TOOL_GUIDE

## Follow-up Needed

- [x] Test in different context
- [x] Verify with other models/roles
- [x] Document in formal research
- [x] Update tool guide/skill
- [ ] Test other zen-mcp tools for similar biases

---

**Research Status:** 🟢 Synthesized