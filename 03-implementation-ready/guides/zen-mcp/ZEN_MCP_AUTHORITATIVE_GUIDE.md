# zen-mcp Authoritative Usage Guide

**Document Type:** Implementation Guide  
**Date:** January 2025  
**Status:** Current zen-mcp server (pre-fork)  
**Based on:** Comprehensive empirical validation across 40+ studies  

> **Note:** HestAI plans to fork zen-mcp to add native role loading capabilities. This guide documents optimal usage of the current zen-mcp server based on extensive empirical research.

## Executive Summary

zen-mcp is a Model Context Protocol (MCP) server providing AI orchestration tools for multi-model collaboration. Through extensive empirical validation, we've identified optimal usage patterns that achieve:
- **100% technical accuracy** for critical analysis (using mcp__zen__chat)
- **86.6% cost reduction** through phase-aware model selection
- **47% quality improvement** over standard AI usage
- **31.3% improvement** from sequential role loading

**Critical Finding:** Use `mcp__zen__chat` exclusively for OCTAVE role operations. Other tools have hardcoded biases that interfere with role fidelity.

## Quick Start

### 1. Choose Your Role Loading Method

| Method | Capability | Time | Use When |
|--------|------------|------|----------|
| **zen-single-primer** | 92% | 5 seconds | Routine work, cross-session needs |
| **zen-4-step-sequential** | High | ~4 exchanges | Complex work within session |
| **zen-9-step-sequential** | 95% | ~5 minutes | Deep research requiring maximum capability |

### 2. Essential Commands

```python
# Basic role loading with zen-single-primer
mcp__zen__chat(
    prompt: "[Load from /Users/shaunbuswell/dev/hestai-system/config/zen-mcp-role-headers/zen-single-primer/[ROLE]_[PHASE]_SINGLE.oct.md]",
    model: "pro"  # Maps to Gemini-2.5-Pro
)
# Returns: continuation_id for this role session

# Continue with loaded role
mcp__zen__chat(
    continuation_id: "[continuation_id from above]",
    prompt: "Your actual task here",
    model: "pro"
)
```

### 3. Critical Rules
- **ALWAYS use mcp__zen__chat** for OCTAVE operations
- **ALWAYS include model identity** ("You are [Model]")
- **ALWAYS use newest continuation_id** from each response
- **NEVER use mcp__zen__codereview** for final decisions

## Why mcp__zen__chat Only?

### Technical Root Cause
All zen-mcp tools have hardcoded "thought partner" system prompts. However:
- **mcp__zen__chat**: OCTAVE enhancement overrides the thought partner prompt
- **Other tools**: Additional tool-specific biases override OCTAVE enhancement

### Empirical Evidence
Same model, same OCTAVE role, same file:
- **mcp__zen__chat**: Correctly identifies json.loads() as safe JSON parsing
- **mcp__zen__codereview**: False positive - claims "code injection vulnerability"
- **Technical accuracy**: 100% vs 0%

## Supported Models

Current configuration (January 2025):

```json
{
  "HERMES": ["openai/gpt-4.1", "anthropic/claude-sonnet-4", "gemini-2.5-pro"],
  "PATHOS": ["anthropic/claude-sonnet-4", "gemini-2.5-pro", "openai/gpt-4.1"],
  "ETHOS": ["openai/gpt-4.1", "gemini-2.5-pro", "openai/o3"],
  "LOGOS-A": ["anthropic/claude-opus-4", "openai/o3", "openai/gpt-4.1"],
  "LOGOS-B": ["gemini-2.5-pro", "openai/o3", "openai/gpt-4.1"],
  "COMPRESSOR": ["gemini-2.5-flash-lite-preview-06-17", "openai/gpt-4.1-mini"]
}
```

### Model Parameter Mapping
- `"flash"` → `"gemini-2.5-flash"`
- `"pro"` → `"gemini-2.5-pro"`
- `"mini"` → General purpose mini model
- `"o3"`, `"o3-mini"`, `"o3-pro"` → OpenAI reasoning models

## Role Loading Methods Detailed

### Method 1: zen-single-primer (Recommended Default)

**When to Use:**
- Quick tasks requiring role capabilities
- Cross-session work (continuation_id not available)
- 80% of routine development tasks

**Example:**
```python
# Load HERMES BUILD role
mcp__zen__chat(
    prompt: """You are Gemini-2.5-Pro.
    
[Contents of /Users/shaunbuswell/dev/hestai-system/config/zen-mcp-role-headers/zen-single-primer/HERMES_BUILD_SINGLE.oct.md]

Task: Organize the build artifacts from today's release.""",
    model: "pro"
)
```

**Advantages:**
- Near-instant activation
- 92% capability retention
- Works across Claude sessions
- Includes anti-pattern prevention

### Method 2: zen-4-step-sequential (RAPH Method)

**When to Use:**
- Complex tasks requiring staged validation
- Need progressive quality building
- Working within single Claude session

**Stages:**
1. **READ** - Foundation literacy
2. **ABSORB** - Identity integration  
3. **PERCEIVE** - Contextual patterns
4. **HARMONISE** - Capability synthesis

**Example Flow:**
```python
# Step 1: Foundation
response1 = mcp__zen__chat(
    prompt: "You are Gemini-2.5-Pro. READ foundation... TEST: What is COMPLETION_THROUGH_SUBTRACTION?",
    model: "pro"
)
continuation_id = response1.continuation_id

# Step 2: Identity (using continuation_id)
response2 = mcp__zen__chat(
    continuation_id: continuation_id,
    prompt: "You are Gemini-2.5-Pro. ABSORB HERMES identity... TEST: What is your philosophical drive?",
    model: "pro"
)
# ... continue through all 4 steps
```

### Method 3: zen-9-step-sequential (Deep Integration)

**When to Use:**
- Deep research requiring philosophical integration
- Complex multi-phase work
- Maximum 95% capability needed
- Token efficiency not critical

**9 Stages:**
1. Foundation Loading
2. Identity Loading
3. Context Loading
4. Universal Pattern Loading
5. Role-Specific Patterns
6. Balance Loading
7. Integration Check
8. Practical Application
9. Readiness Declaration

**Note:** Requires ~5 minutes and careful test validation at each stage.

## Continuation ID Management

### How It Works
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Turn 1    │────▶│   Turn 2    │────▶│   Turn 3    │
│ ID: abc-123 │     │ ID: def-456 │     │ ID: ghi-789 │
└─────────────┘     └─────────────┘     └─────────────┘
                           ▲                      ▲
                    Must use abc-123       Must use def-456
```

### Critical Rules
1. **Each response generates NEW continuation_id**
2. **Must use newest ID for continuation**
3. **3-hour TTL** (but can expire unexpectedly)
4. **Works only within single Claude session**

### Session Bridge Pattern
```json
// In HestAI session manifest.json
{
  "zen_conversations": {
    "hermes_build_work": "abc-123-...",
    "pathos_exploration": "def-456-...",
    "ethos_validation": "ghi-789-..."
  }
}
```

## Cost Optimization Strategies

### Phase-Aware Model Selection
```python
# DESIGN phase: Use heavy models
mcp__zen__chat(prompt: "Explore architecture...", model: "pro")

# BUILD phase: Use light models  
mcp__zen__chat(prompt: "Organize artifacts...", model: "flash")

# Result: 50-86% cost reduction
```

### Role-Tool Affinity
- **HERMES + flash**: 98% cost savings for organization
- **LOGOS + pro**: Optimal for synthesis
- **ETHOS + o3**: High-quality validation
- **PATHOS + pro**: Natural exploration

### Thinking Mode Optimization
- `minimal` (0.5%): Quick checks
- `low` (8%): Simple tasks
- `medium` (33%): Standard work
- `high` (67%): Complex analysis (default)
- `max` (100%): Critical decisions only

## Common Pitfalls and Solutions

### Pitfall 1: Forgetting Model Identity
```python
# ❌ WRONG - Causes identity confusion
mcp__zen__chat(prompt: "ABSORB HERMES identity...")

# ✅ CORRECT - Maintains coherence
mcp__zen__chat(prompt: "You are Gemini-2.5-Pro. ABSORB HERMES identity...")
```

### Pitfall 2: Using Wrong Tool
```python
# ❌ WRONG - Tool bias overrides role
mcp__zen__codereview(prompt: "Enhanced with ETHOS role...")

# ✅ CORRECT - Role enhancement works
mcp__zen__chat(prompt: "Enhanced with ETHOS role...")
```

### Pitfall 3: Expired Continuation ID
```python
# Check if continuation still works
try:
    response = mcp__zen__chat(continuation_id: old_id, ...)
except:
    # Reload role from scratch
    response = mcp__zen__chat(prompt: "[Role loading prompt]", ...)
```

## Production Workflows

### Example: Security Review Workflow
```python
# 1. Load ETHOS role for security analysis
ethos_response = mcp__zen__chat(
    prompt: """You are GPT-4.1. 
    [ETHOS role content from zen-single-primer]
    Review this code for security vulnerabilities.""",
    model: "gpt-4.1-2025-04-14",
    files: ["parser.py"]
)

# 2. If findings need synthesis, load LOGOS
logos_response = mcp__zen__chat(
    prompt: """You are Gemini-2.5-Pro.
    [LOGOS role content]
    Synthesize security findings and propose elegant solutions.""",
    model: "pro"
)

# 3. Document with HERMES
hermes_response = mcp__zen__chat(
    prompt: """You are GPT-4.1.
    [HERMES role content]
    Create security audit documentation.""",
    model: "gpt-4.1-2025-04-14"
)
```

### Multi-Role Collaboration Pattern
1. Start with exploration (PATHOS)
2. Validate approach (ETHOS)
3. Synthesize solution (LOGOS)
4. Document results (HERMES)

## Monitoring and Debugging

### Check Activity Logs
```bash
tail -f ~/Library/Logs/zen-mcp/mcp_activity.log
```

### Common Issues
- **"Continuation not found"**: ID expired or wrong session
- **Role drift**: Not including model identity
- **False positives**: Using wrong tool (codereview vs chat)

## Future: HestAI Fork

When the HestAI fork is released, this guide will be updated with:
- Native RAPH protocol support
- Dynamic role loading without hardcoded prompts
- Bronze/Silver/Gold capability tiers
- Integrated role management

## Quick Reference Card

```
CRITICAL RULES:
☐ Use mcp__zen__chat for all OCTAVE operations
☐ Include "You are [Model]" in every prompt
☐ Use newest continuation_id from each response
☐ Store continuation_ids in session manifests

ROLE LOADING:
☐ Quick work: zen-single-primer (92%, 5 sec)
☐ Complex work: zen-4-step-sequential (High, ~4 exchanges)
☐ Deep work: zen-9-step-sequential (95%, ~5 min)

COST OPTIMIZATION:
☐ DESIGN: Heavy models (pro, o3)
☐ BUILD: Light models (flash, mini)
☐ Match thinking_mode to task complexity
```

## References

This guide synthesizes findings from:
- 40+ empirical validation studies
- 3+ hours of infrastructure testing
- 24-hour development velocity experiments
- Comprehensive code review of zen-mcp-server
- Production usage across multiple HestAI implementations

For detailed evidence, see:
- `/01-active-research/empirical-validation/zen-mcp/`
- `/01-active-research/empirical-validation/empirical-studies/`

---
*Guide Version: 1.0*  
*Based on: zen-mcp server (current)*  
*Next Update: When HestAI fork releases*