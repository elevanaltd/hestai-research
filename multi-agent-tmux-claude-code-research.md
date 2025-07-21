# Multi-Agent AI Coding with tmux, Claude Code, and Git Worktrees

## Abstract

This research document analyzes a methodology for orchestrating multiple AI coding agents using tmux (terminal multiplexer), Claude Code, and git worktrees to enable parallel, asynchronous task execution while preventing code conflicts and maintaining project integrity.

## Background

AI coding assistants like Claude Code, Aider, and Open Code have become prevalent tools for software development. However, scaling these tools to work on multiple tasks simultaneously presents challenges:

1. **Code Conflicts**: Multiple AI agents working on the same project can overwrite each other's changes
2. **Task Management**: Manual assignment and navigation through multiple AI instances is tedious
3. **State Isolation**: Need for proper isolation between different development streams

## Core Components

### 1. Task Claiming System

A structured approach to task management that enables multiple AI agents to work simultaneously without conflicts.

**Key Elements:**
- **Task File**: Central markdown file containing all tasks to be accomplished
- **Branch Management**: Each task assigned to a specific branch
- **Status Tracking**: Real-time status updates (claimed, in-progress, intervention required)
- **Session Tracking**: Records tmux session names for each task

**Task Structure:**
```
- Branch Name: feature-name
- Status: pending/claimed/in-progress/intervention-required
- Tmux Session: session-name
- Description: Task details
```

### 2. Git Worktrees

Git worktrees provide physical copies of the repository that can be worked on simultaneously without branch switching.

**Benefits:**
- **Parallel Development**: Multiple development streams without conflicts
- **State Isolation**: Each worktree maintains independent file states
- **Git Integration**: Maintains full git functionality and merge capabilities
- **No Branch Switching**: Direct work on features without disrupting main workspace

**Implementation:**
```bash
git worktree add -b <feature-name> <work-directory>/<feature-name>
```

### 3. Terminal Multiplexer (tmux)

Tmux enables creation and management of multiple terminal sessions running in the background.

**Capabilities:**
- **Session Management**: Create, detach, and reattach to terminal sessions
- **Background Execution**: Long-running processes continue when detached
- **Multiple Sessions**: Handle numerous concurrent AI agent instances
- **Interactive Access**: Attach to any session for monitoring or intervention

**Basic Commands:**
```bash
# Create new session
tmux new-session -s <session-name>

# Detach from session
Ctrl+b, then d

# Attach to existing session
tmux attach -t <session-name>
```

## Agent-Spawn Workflow

### Orchestrator Implementation

The workflow is implemented as a Claude Code command that acts as an agent spawner and orchestrator.

**Workflow Steps:**
1. **Task Analysis**: Read tasks file and identify suitable task groupings
2. **Agent Assignment**: Assign independent tasks to separate agents, dependent tasks to same agent
3. **Worktree Creation**: Create git worktree for each agent
4. **Session Management**: Launch tmux session with Claude Code instance
5. **Status Updates**: Update task file with claimed status and session information

### Agent Configuration

Each spawned agent is configured with:
- Specific prompt for assigned tasks
- Limited tool access (edit, write, bash, replace)
- Dedicated worktree environment
- Isolated tmux session

## Technical Architecture

### Workflow Orchestration
```
Tasks File → Task Analysis → Agent Assignment → Worktree Creation → Session Launch → Status Updates
```

### Session Management
```
Main Terminal → tmux Session Creation → Claude Code Launch → Background Execution → Status Monitoring
```

### Integration Points
```
Git Repository → Worktrees → tmux Sessions → AI Agents → Task Completion → Merge Back
```

## Implementation Details

### Task File Format
- Markdown structure for human readability
- Clear status indicators for automation
- Session tracking for monitoring
- Dependency indication for proper grouping

### Automation Features
- Automatic worktree creation
- Session naming conventions
- Status update mechanisms
- Progress monitoring capabilities

### Monitoring and Control
- Session attachment for real-time monitoring
- Status querying through main orchestrator
- Intervention handling for blocked tasks
- Progress reporting and updates

## Benefits and Advantages

1. **Scalability**: Handle multiple tasks simultaneously
2. **Isolation**: Prevent code conflicts between agents
3. **Automation**: Reduce manual task assignment overhead
4. **Flexibility**: Support various AI coding tools
5. **Monitoring**: Real-time visibility into agent progress
6. **Recovery**: Easy intervention and recovery mechanisms

## Limitations and Considerations

1. **Resource Usage**: Multiple AI instances consume significant system resources
2. **Complexity**: Requires understanding of tmux, git worktrees, and orchestration
3. **Dependency Management**: Careful task dependency analysis required
4. **Merge Conflicts**: Post-completion merge may require manual resolution
5. **Tool Compatibility**: Specific to compatible AI coding assistants

## Future Research Directions

1. **Enhanced Orchestration**: More sophisticated task dependency analysis
2. **Resource Optimization**: Dynamic agent scaling based on system resources
3. **Conflict Resolution**: Automated merge conflict resolution strategies
4. **Cross-Tool Compatibility**: Support for heterogeneous AI agent types
5. **Performance Metrics**: Quantitative analysis of parallel vs. sequential development

## Conclusion

The combination of tmux, git worktrees, and Claude Code provides a robust foundation for multi-agent AI coding workflows. This approach successfully addresses the core challenges of parallel AI development while maintaining code integrity and enabling scalable task execution.

The methodology demonstrates significant potential for accelerating software development through intelligent orchestration of AI coding assistants, though careful consideration of resource management and task dependencies remains crucial for successful implementation.

---

*Research compiled from YouTube transcript analysis focusing on practical multi-agent AI coding methodologies.*