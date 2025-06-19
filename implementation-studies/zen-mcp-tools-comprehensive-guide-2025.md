# Zen-MCP Tools Comprehensive Guide

**Document Type:** Implementation Study  
**Date:** June 19, 2025  
**Version:** zen-mcp v5.2.1  
**Focus:** AI orchestration tools and multi-model collaboration  
**Status:** Reference complete  

## Overview

The zen-mcp server provides 13 specialized AI orchestration tools that enable multi-model collaboration, deep analysis, and intelligent development workflows. Each tool can leverage different AI models based on task requirements, with sophisticated thinking depth controls and context preservation features.

## Available Models

### Gemini Models
- **flash** / **gemini-2.5-flash**: Ultra-fast analysis with 1M context window
- **pro** / **gemini-2.5-pro**: Deep reasoning with thinking mode support, 1M context

### OpenAI Models
- **o3**: Strong reasoning, 200K context
- **o3-mini**: Fast O3 variant, balanced performance
- **o3-pro**: Professional-grade reasoning (EXTREMELY EXPENSIVE - use sparingly)
- **o4-mini**: Latest reasoning model, optimized for shorter contexts
- **o4-mini-high**: Enhanced O4 mini for complex tasks
- **gpt-4.1-2025-04-14** / **gpt4.1**: Latest GPT-4.1 variant
- **mini**: General purpose mini model

## Tool Catalog

### 1. thinkdeep
**Purpose**: Extended thinking & reasoning for complex problems  
**When to use**: Architecture decisions, complex bugs, performance challenges, security analysis  
**Key features**:
- Deep exploration of alternatives and edge cases
- Challenge assumptions and validate approaches
- Thinking modes: minimal (0.5%), low (8%), medium (33%), high (67%), max (100%)
- Web search integration for current best practices
- Continuation support for multi-turn analysis

**Parameters**:
- `prompt` (required): Detailed problem description with context
- `model` (required): Model selection based on complexity
- `thinking_mode`: Depth of analysis (defaults to 'high')
- `focus_areas`: Specific aspects to focus on
- `files`: Absolute paths to relevant files
- `images`: Visual references for analysis
- `use_websearch`: Enable web search (default: true)
- `continuation_id`: Thread continuation token

### 2. codereview
**Purpose**: Comprehensive code analysis for bugs, security, and quality  
**When to use**: Code reviews, security audits, quality checks, verify code behavior  
**Key features**:
- Severity classification: Critical→High→Medium→Low
- Support for individual files and entire directories
- Focused review types: full, security, performance, quick
- Pattern detection and best practice validation

**Parameters**:
- `files` (required): Code files/directories to review
- `prompt` (required): Review objectives and context
- `model` (required): Model selection
- `review_type`: Type of review (default: 'full')
- `severity_filter`: Minimum severity to report (default: 'all')
- `focus_on`: Specific areas of concern
- `standards`: Coding standards to enforce
- `thinking_mode`: Analysis depth

### 3. debug
**Purpose**: Systematic debugging with root cause analysis  
**When to use**: Complex bugs, race conditions, memory leaks, integration issues  
**Key features**:
- Step-by-step investigation methodology
- Hypothesis formation and validation
- File and method tracking
- Confidence assessment with backtracking
- Evidence collection and pattern analysis

**Parameters**:
- `step` (required): Current investigation step description
- `step_number` (required): Current step in sequence
- `total_steps` (required): Estimated total steps
- `next_step_required` (required): Whether more steps needed
- `findings` (required): Discoveries in current step
- `model` (required): Model selection
- `hypothesis`: Current working theory
- `confidence`: Confidence level (low/medium/high)
- `files_checked`: All examined files
- `relevant_files`: Files directly related to issue
- `relevant_methods`: Key methods involved
- `backtrack_from_step`: Step to revise from

### 4. analyze
**Purpose**: General-purpose file and code analysis  
**When to use**: Codebase exploration, dependency analysis, pattern detection  
**Key features**:
- Multiple analysis types: architecture, performance, security, quality, general
- Support for files and directories
- Flexible output formats: summary, detailed, actionable

**Parameters**:
- `files` (required): Files/directories to analyze
- `prompt` (required): What to analyze or look for
- `model` (required): Model selection
- `analysis_type`: Type of analysis to perform
- `output_format`: How to format output (default: 'detailed')
- `thinking_mode`: Analysis depth
- `use_websearch`: Enable documentation lookup

### 5. chat
**Purpose**: General collaborative thinking and brainstorming  
**When to use**: Bouncing ideas, getting second opinions, exploring alternatives  
**Key features**:
- Flexible conversational AI assistance
- Context-aware responses
- Image support for visual discussions
- Temperature control for creativity

**Parameters**:
- `prompt` (required): Question or idea with full context
- `model` (required): Model selection
- `files`: Optional context files
- `images`: Visual context (diagrams, UI, etc.)
- `temperature`: Response creativity (0-1, default: 0.5)
- `thinking_mode`: Thinking depth
- `use_websearch`: Enable web search
- `continuation_id`: Thread continuation

### 6. consensus
**Purpose**: Multi-model consensus gathering on decisions  
**When to use**: Validation, feasibility assessment, getting diverse perspectives  
**Key features**:
- Advanced stance steering (for/against/neutral)
- Custom instructions per model
- Structured debate capabilities
- RAPH-compatible role specialization

**Parameters**:
- `prompt` (required): What to get consensus on
- `models` (required): List of model configurations
  - Each model can have: `model`, `stance`, `stance_prompt`
- `focus_areas`: Specific aspects to evaluate
- `files`: Context files
- `images`: Visual references
- `thinking_mode`: Analysis depth
- `temperature`: Consistency control (default: 0.2)
- `use_websearch`: Enable research

### 7. listmodels
**Purpose**: Display all available AI models and capabilities  
**When to use**: Understanding available models, checking configurations  
**Key features**:
- Shows configured providers
- Lists model aliases and capabilities
- Displays context windows

**Parameters**: None required

### 8. planner
**Purpose**: Interactive sequential planning for complex tasks  
**When to use**: Project planning, system design, migration strategies  
**Key features**:
- Step-by-step plan building
- Revision and branching capabilities
- Dynamic step count adjustment
- Full context awareness

**Parameters**:
- `step` (required): Current planning step content
- `step_number` (required): Current step number
- `total_steps` (required): Estimated total steps
- `next_step_required` (required): Whether more steps needed
- `is_step_revision`: If revising previous step
- `revises_step_number`: Which step being revised
- `is_branch_point`: If creating alternative branch
- `branch_from_step`: Origin step for branch
- `branch_id`: Branch identifier
- `more_steps_needed`: If exceeding initial estimate

### 9. precommit
**Purpose**: Pre-commit validation for git changes  
**When to use**: Before any git commit, reviewing changes, validating implementations  
**Key features**:
- Catches bugs and incomplete implementations
- Ensures changes match requirements
- Searches git repositories recursively
- Compares staged/unstaged changes or branches

**Parameters**:
- `path` (required): Starting directory to search
- `model` (required): Model selection
- `prompt`: Original request description
- `compare_to`: Git ref to compare against
- `include_staged`: Include staged changes (default: true)
- `include_unstaged`: Include unstaged changes (default: true)
- `review_type`: Type of review (default: 'full')
- `severity_filter`: Minimum severity (default: 'all')
- `focus_on`: Specific aspects to check
- `files`: Additional context files
- `images`: Expected UI changes
- `thinking_mode`: Review depth

### 10. testgen
**Purpose**: Comprehensive test generation with edge cases  
**When to use**: Creating test suites, improving coverage, TDD  
**Key features**:
- Analyzes code paths for comprehensive coverage
- Identifies realistic failure modes
- Framework-specific test generation
- Pattern following from examples

**Parameters**:
- `files` (required): Code to generate tests for
- `prompt` (required): Testing objectives and scope
- `model` (required): Model selection
- `test_examples`: Existing tests for style reference
- `thinking_mode`: Test generation depth

### 11. refactor
**Purpose**: Intelligent code refactoring suggestions  
**When to use**: Code improvement, modernization, organization  
**Key features**:
- Four refactor types: codesmells, decompose, modernize, organization
- Line-number specific guidance
- Style guide compliance
- Actionable refactoring steps

**Parameters**:
- `files` (required): Code to analyze for refactoring
- `prompt` (required): Refactoring goals and context
- `refactor_type` (required): Type of refactoring
- `model` (required): Model selection
- `focus_areas`: Specific improvement areas
- `style_guide_examples`: Target style examples
- `thinking_mode`: Analysis depth

### 12. tracer
**Purpose**: Analysis prompt generator for code tracing  
**When to use**: Understanding execution flow, dependency mapping  
**Key features**:
- Two modes: precision (methods/functions), dependencies (classes/modules)
- Generates structured analysis prompts
- Execution flow and call chain tracing

**Parameters**:
- `prompt` (required): What to trace and why
- `trace_mode` (required): 'precision' or 'dependencies'
- `images`: Architecture diagrams or flow charts

### 13. version
**Purpose**: Show zen-mcp server configuration  
**When to use**: Debugging, checking capabilities  
**Key features**:
- Server version and configuration
- Available tools and models
- Provider status

**Parameters**: None required

## Model Selection Guidelines

### Quick Tasks & Simple Analysis
- Use `flash` or `gemini-2.5-flash`
- Lowest cost, fastest response
- Good for: Simple queries, rapid iterations

### Standard Development Tasks
- Use `o3-mini` or `o4-mini`
- Balanced performance and cost
- Good for: Code generation, standard analysis

### Complex Problems & Deep Analysis
- Use `pro`, `gemini-2.5-pro`, or `o3`
- Higher cost but superior reasoning
- Good for: Architecture, complex debugging

### Critical & Universe-Scale Problems
- Use `o3-pro` (EXTREMELY EXPENSIVE)
- Only when explicitly requested or absolutely necessary
- Good for: Mission-critical decisions, exceptionally complex analysis

## Thinking Mode Optimization

- **minimal** (0.5%): Very quick checks
- **low** (8%): Small code snippets, simple tasks
- **medium** (33%): Standard files/modules
- **high** (67%): Complex systems, default for most tools
- **max** (100%): Critical analysis, large codebases

## Cost Optimization Patterns

### 1. RAPH Pattern (via consensus)
- Stage 1: Fast model for exploration ($0.0002)
- Stage 2: Deep model for validation ($0.003-0.005)
- 85-90% cost reduction vs always using expensive models

### 2. Thinking Mode Selection
- Match thinking depth to task complexity
- Avoid 'max' unless truly needed
- Use 'minimal' or 'low' for quick validations

### 3. Model Cascading
- Start with cheaper models
- Escalate only when needed
- Use consensus for automatic cascading

## Integration with HESTAI

All tools support:
- OCTAVE format inputs (no parsing needed)
- Role-based orchestration patterns
- Continuation IDs for multi-turn workflows
- File path references for context
- Image inputs for visual analysis

The tools are designed to work together, enabling complex workflows through tool composition and context preservation.

## Research Significance

This comprehensive tool catalog demonstrates:

1. **Multi-Model Orchestration**: Sophisticated model selection based on task complexity and cost considerations
2. **Cost Optimization**: RAPH patterns showing 85-90% cost reduction through intelligent model cascading
3. **Thinking Depth Control**: Granular control over reasoning intensity (0.5% to 100%)
4. **Tool Composition**: Designed for complex workflows through continuation and context preservation
5. **HESTAI Integration**: Full support for OCTAVE format and role-based orchestration patterns

## Empirical Evidence

The tool specifications provide evidence for:
- **Cost efficiency patterns**: RAPH cascading reduces costs by 85-90% (implementation-studies/zen-mcp-tools-comprehensive-guide-2025.md:292)
- **Model performance tiers**: Clear hierarchy from flash→mini→o3→o3-pro for different complexity levels
- **Thinking mode effectiveness**: Granular control from 0.5% to 100% thinking depth
- **Integration capabilities**: Native OCTAVE and continuation support

---

## Cross-References

**Related Studies:**
- RAPH framework implementation: (raph-framework/)
- Cost optimization analysis: (cost-analysis/)
- Multi-model orchestration: (architectural-studies/orchestration/)
- MCP protocol patterns: (implementation-studies/llm-training-priorities-hestai-platform-2025.md)

**Implementation Impact:**
- Production-ready tool specifications
- Cost optimization validation
- Multi-model collaboration patterns
- HESTAI system integration guidelines