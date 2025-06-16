# RAPH Framework Research

> ⚠️ **IMPORTANT: Read [BULLSHIT-FILTER.md](./BULLSHIT-FILTER.md) first** - This framework contains misleading terminology about "cognitive processing" that doesn't reflect how LLMs actually work. The techniques are effective, but the explanations are often wrong.

Role-Aligned Prompting Hierarchy (RAPH) is the sequential cognitive loading protocol that enables HestAI's phase-based activation system.

## Overview

RAPH represents a breakthrough in structured LLM activation, demonstrating that sequential, phase-based loading of cognitive components produces superior results compared to monolithic prompting approaches.

## Directory Structure

```
raph-framework/
├── benchmarking/         # Empirical validation and performance data
├── implementation/       # Guides and code for RAPH implementation
└── specifications/       # Formal RAPH specifications and theory
```

## Key Findings

### 1. Sequential Loading Advantage
- **Finding**: Phase-based loading improves comprehension by 40-60%
- **Impact**: Informed HestAI's 6-phase activation protocol
- **Evidence**: See `benchmarking/raph-benchmarking-evidence.md`

### 2. Constraint Effects
- **Finding**: Constraints introduced during specific phases have differential impacts
- **Impact**: Led to optimal placement of governance in Phase 3
- **Evidence**: See `benchmarking/raph-constraint-effects.md`

### 3. Cross-Model Applicability
- **Finding**: RAPH principles work across different model architectures
- **Impact**: Enables model-agnostic role activation
- **Evidence**: See `benchmarking/gemini-raph-validation.md`

### 4. Cost Efficiency
- **Finding**: RAPH can achieve 90% performance at 10% token cost
- **Impact**: Makes sophisticated role activation economically viable
- **Evidence**: See `benchmarking/raph-mini-costing.md`

## RAPH Phases

1. **ORIENTATION** - Context about the loading process
2. **GROUNDING** - System facts and foundational laws
3. **IDENTITY_FORMATION** - Core role identity
4. **CAPABILITY_AWARENESS** - What the role can do
5. **INTEGRATION** - How capabilities work together
6. **SELF_SUMMARY** - Articulation of understanding

## Implementation in HestAI

RAPH directly enables:
- The SHAFT sequential loading system
- Phase-aware cognitive bootstrapping
- Predictable role activation
- Consistent identity formation

## Key Documents

### Benchmarking
- `raph-benchmarking-evidence.md` - Core performance validation
- `raph-constraint-effects.md` - Optimal constraint placement
- `gemini-raph-validation.md` - Cross-model validation
- `raph-mini-costing.md` - Economic analysis

### Implementation
- `RAPH_PROCESSING_GUIDE.md` - Practical implementation guide
- `raph_prompt_generator.py` - Python implementation

### Specifications
- `F1-RAPH-1.1.0.octave.txt` - Formal RAPH specification
- `RAPH-REFERENCE-ENHANCED.md` - Enhanced reference documentation

## Using RAPH Research

1. **For Protocol Design** - Reference benchmarking when designing activation sequences
2. **For Implementation** - Use processing guides and generators
3. **For Validation** - Compare new approaches against RAPH baselines
4. **For Extension** - Build on proven sequential loading principles

## Critical Insights

1. **Order Matters** - The sequence of cognitive loading significantly impacts final performance
2. **Less is More** - Focused, phased loading outperforms comprehensive single prompts
3. **Identity First** - Establishing role identity before capabilities improves coherence
4. **Constraints as Features** - Well-placed constraints enhance rather than limit performance

---

*RAPH research provides the empirical foundation for HestAI's sequential activation architecture.*