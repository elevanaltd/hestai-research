# RepoPrompt macOS App Research Documentation

## Research Metadata
- **Date**: 2025-07-06 (Corrected)
- **Researcher**: HERMES (Claude operating as System Steward)
- **Sources**: Web research, reviews, official documentation attempts
- **Purpose**: Complete understanding of RepoPrompt macOS application for HestAI research

## Executive Summary

RepoPrompt is a commercial macOS native application designed to "remove all the friction involved in iterating on your code with the most powerful AI models." This is a standalone commercial product focused on AI-assisted development workflows.

## Key Features

### File Selection and Context Management
- Advanced file/folder selection for AI prompts
- Token usage insights and counting
- File tree generation for comprehensive context
- Workspace management and organization

### Workflow Optimization
- **PLAN Mode**: Encourages planning code changes before implementation
- **ACT Mode**: Scans files and assigns specific commits rather than full file rewrites
- Structured approach: Plan → Implement → Review

### Multi-Model Support
- Support for OpenAI and Anthropic models
- Local model connections for privacy
- Smart model delegation based on task complexity
- Parallel model processing capabilities

### Advanced Capabilities
- Granular code change review and acceptance
- Delegate coding tasks to specific models based on commit complexity and file length
- Regex-based search functionality
- Clipboard integration for prompt editing

## Pricing Structure
- Free tier available
- Pro mode with advanced model delegation features
- Specific pricing details not publicly documented

## User Experience Insights
From review analysis:
- "Demands a bit more effort up front, but the payoff is substantial"
- Provides structured, controlled AI-assisted coding
- Best suited for complex project development and large codebases

## Platform Availability
- **macOS Only**: Currently exclusive to macOS platform
- No cross-platform versions documented

## Workflow Details

### PLAN Mode
- Uses advanced models for planning phase
- Recommended models: Gemini 2.5 pro-EXP or Claude 3.7 Thinking MAX
- Focus on thoughtful code architecture and feature planning
- Generates comprehensive plans before implementation

### ACT Mode
- Uses smaller, faster, cheaper models for implementation
- Analyzes files to assign specific commits
- Avoids full file rewrites in favor of targeted changes
- Enables granular review of proposed changes

### Model Delegation Strategy
- Automatically selects appropriate models based on:
  - Task complexity
  - File length
  - Commit scope
  - Cost optimization goals
- Parallel processing of different tasks with different models

## Technical Analysis

### Architecture Inference
Based on functionality, likely components include:

#### User Interface
- Native macOS UI (likely SwiftUI or Cocoa)
- File browser with advanced selection
- Real-time token counting display
- Model selection and delegation interface

#### Core Engine
- File parsing and analysis
- Token counting algorithms
- Context optimization logic
- Workspace state management

#### AI Integration
- Multi-model API management
- Cost tracking and optimization
- Request routing based on task analysis
- Response aggregation and presentation

## Strategic Value Propositions

### For Individual Developers
- Reduced friction in AI-assisted coding
- Cost optimization through intelligent model selection
- Structured workflow prevents ad-hoc, inefficient prompting
- Native macOS experience

### For Complex Projects
- Handles large codebases effectively
- Maintains context across sessions via workspaces
- Enables systematic approach to AI-assisted development
- Granular control over AI-generated changes

## Limitations and Considerations

### Platform Exclusivity
- macOS only limits market reach
- No Windows or Linux support
- Requires macOS ecosystem buy-in

### Documentation Accessibility
- Website requires JavaScript, limiting analysis
- Limited public technical documentation
- Pricing transparency issues

### Commercial Model
- Freemium may limit advanced features
- Vendor lock-in considerations
- Unclear data handling and privacy policies

## Competitive Positioning

### Unique Differentiators
- Native macOS integration
- Sophisticated PLAN/ACT workflow
- Advanced model delegation
- Granular change management

### Market Position
- Premium tool for serious AI-assisted development
- Focused on workflow optimization over simple conversion
- Targets developers willing to invest in structured approach

## Research Gaps

### Information Not Available
1. Detailed pricing for Pro features
2. Specific model delegation algorithms
3. Performance benchmarks
4. Data privacy and security details
5. Integration with development tools
6. Roadmap and future features

### Technical Details Needed
- API limits and rate limiting
- Workspace file format and portability
- Offline capabilities
- Custom model support details
- Enterprise features

## References and Sources

### Primary Sources
- Official Website: https://repoprompt.com/ (JavaScript-dependent)
- Review: https://masonjames.com/repo-prompt-review-granular-control-and-workflow-excellence/

### Search Results
- Future Tools listing (contains some inaccuracies)
- Various mentions in AI tool comparisons
- Community discussions about alternatives

### Research Limitations
- Limited official documentation access
- Reliance on third-party reviews
- No technical documentation available
- No direct product trial conducted

---

*Research updated with HERMES stewardship: Focused exclusively on RepoPrompt macOS application with previous Python library conflation removed.*