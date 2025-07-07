# RepoPrompt Comprehensive Research Documentation

## Research Metadata
- **Date**: 2025-07-06
- **Researcher**: HERMES (Claude operating as System Steward)
- **Sources**: Web research, GitHub repository, official documentation
- **Purpose**: Complete understanding of RepoPrompt system for HestAI research

## Executive Summary

RepoPrompt exists in two distinct forms:
1. **RepoPrompt macOS Application**: A commercial native app for AI-assisted coding workflows
2. **RepoPrompt Python Library**: An open-source library for converting repositories to LLM-suitable prompts

## 1. RepoPrompt macOS Application

### Overview
A macOS native application designed to "remove all the friction involved in iterating on your code with the most powerful AI models." This is a commercial product focused on AI-assisted development workflows.

### Key Features

#### File Selection and Context Management
- Advanced file/folder selection for AI prompts
- Token usage insights and counting
- File tree generation for comprehensive context
- Workspace management and organization

#### Workflow Optimization
- **PLAN Mode**: Encourages planning code changes before implementation
- **ACT Mode**: Scans files and assigns specific commits rather than full file rewrites
- Structured approach: Plan → Implement → Review

#### Multi-Model Support
- Support for OpenAI and Anthropic models
- Local model connections for privacy
- Smart model delegation based on task complexity
- Parallel model processing capabilities

#### Advanced Capabilities
- Granular code change review and acceptance
- Delegate coding tasks to specific models based on commit complexity and file length
- Regex-based search functionality
- Clipboard integration for prompt editing

### Pricing Structure
- Free tier available
- Pro mode with advanced model delegation features
- Specific pricing details not publicly documented

### User Experience Insights
- "Demands a bit more effort up front, but the payoff is substantial"
- Provides structured, controlled AI-assisted coding
- Best suited for complex project development and large codebases

### Platform Availability
- **macOS Only**: Currently exclusive to macOS platform
- No cross-platform versions documented

## 2. RepoPrompt Python Library

### Overview
Open-source Python library for converting entire code repositories into text prompts suitable for Large Language Models (LLMs).

### Technical Specifications
- **Repository**: https://github.com/mhallsmoore/repoprompt
- **License**: MIT License
- **Python Requirements**: Python 3.9+
- **Installation**: `pip install git+https://github.com/mhallsmoore/repoprompt.git@main`

### Core Features

#### Repository Processing
- Complete repository concatenation into standardized text format
- File tree structure generation
- Individual file contents with clear delimiters
- Repository path inclusion in output

#### Filtering Capabilities
- Include/exclude files based on regex patterns
- `.gitignore` pattern recognition and processing
- Optional hidden file inclusion
- Flexible file selection mechanisms

#### Usage Methods

**Command Line Interface**:
```bash
python -m repoprompt /path/to/repository
```

**Python API**:
```python
from pathlib import Path
from repoprompt import RepoPrompt

rp = RepoPrompt()
prompt = rp(
    root_path=Path('/path/to/repo'),
    include_hidden=False,
    include_pattern=r'\.py$'
)
```

#### Development Setup
- Development dependencies: `pip install repoprompt[dev]`
- Testing: `pytest`

### Output Format
- Repository path identification
- Complete file tree structure
- Individual file contents with clear delimiters
- Standardized formatting for LLM consumption

## 3. Ecosystem and Alternatives

### Similar Tools Identified
- **Repomix**: Similar repository packaging tool with broader feature set
- **16x Prompt**: Alternative service positioning itself as RepoPrompt alternative
- **Open-RepoPrompt**: Open-source implementations by various developers

### Market Positioning
- RepoPrompt focuses on workflow optimization and model delegation
- Emphasis on structured AI-assisted development
- Premium positioning with advanced features

## 4. Technical Analysis

### Strengths
- Native macOS integration for optimal user experience
- Sophisticated workflow management (PLAN/ACT modes)
- Advanced model delegation capabilities
- Token management and cost optimization
- Granular control over file selection and context

### Limitations
- Platform exclusivity (macOS only)
- Limited public documentation
- Commercial model may limit adoption
- JavaScript-heavy web presence limiting accessibility

### Comparison Points for HestAI Research
- **Workflow Structure**: PLAN → ACT → Review mirrors HestAI's DESIGN → BUILD phases
- **Model Delegation**: Advanced capability for task-specific model selection
- **Context Management**: Sophisticated file selection and token management
- **Integration Approach**: Native app vs. CLI/API library trade-offs

## 5. Implementation Insights

### Recommended Usage Patterns (from review analysis)
- **Planning Stage**: Use advanced models (Gemini 2.5 pro-EXP, Claude 3.7 Thinking MAX)
- **Implementation**: Use smaller, faster, cheaper models
- **Review**: Granular acceptance of individual changes

### Workflow Philosophy
- Structured approach over ad-hoc prompting
- Context control over comprehensive inclusion
- Quality over speed in AI-assisted development

## 6. Research Questions and Gaps

### Unanswered Questions
1. Detailed pricing structure for Pro features
2. Specific model delegation algorithms
3. Performance benchmarks vs. alternatives
4. Integration with existing development tools
5. Scalability for large enterprise codebases

### Documentation Limitations
- Official website requires JavaScript, limiting accessibility
- Limited public documentation of advanced features
- Pricing information not transparently available

## 7. Strategic Implications for HestAI

### Alignment with HestAI Principles
- **Constraint Catalysis**: Tool provides boundaries that enhance AI interaction
- **Thoughtful Action**: PLAN → ACT workflow mirrors DESIGN → BUILD phases
- **Empirical Development**: Focus on real workflow optimization over theoretical features

### Potential Integration Points
- Workflow patterns could inform HestAI agent orchestration
- Model delegation strategies applicable to PATHOS/ETHOS/LOGOS role assignment
- Context management approaches for large codebase analysis

### Differentiation Opportunities
- Cross-platform availability (HestAI's potential advantage)
- Open-source approach vs. commercial model
- Integration with broader AI agent orchestration systems

## 8. References and Sources

### Primary Sources
- GitHub Repository: https://github.com/mhallsmoore/repoprompt
- Official Website: https://repoprompt.com/ (limited access due to JavaScript requirement)
- Review Analysis: https://masonjames.com/repo-prompt-review-granular-control-and-workflow-excellence/

### Search Results and Additional Context
- Future Tools listing (with some inaccuracies noted)
- Alternative tool comparisons
- Community discussions and implementations

### Research Methodology
- Web search across multiple sources
- GitHub repository analysis
- Review and blog post analysis
- Ecosystem mapping through search results

---

*Research completed with HERMES stewardship: Perfect fidelity preservation of all discovered information about RepoPrompt systems and ecosystem.*