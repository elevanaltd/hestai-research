# OA Repository Enhancement Analysis: Applying HestAI Research Findings

**Document Type:** System Comparison & Enhancement Analysis
**Date Created:** 2025-11-19
**Repository Analyzed:** https://github.com/elevanaltd/oa (Odyssean Anchor)
**Status:** Enhancement Recommendations
**Confidence Level:** 0.95 (Based on validated research findings)

---

## Executive Summary

The **OA repository** (Odyssean Anchor) implements a constitutional agent architecture for Claude Code using the SHANK-ARM-FLUKE framework. This analysis evaluates the current implementation against validated empirical findings from the HestAI research repository and provides specific, actionable enhancement recommendations.

**Key Finding:** The OA repository has implemented the foundational SHANK-ARM-FLUKE architecture and UserPromptSubmit hook, but is **missing critical behavioral monitoring and dynamic task injection capabilities** that research shows achieve 100% role restoration success.

**High-Impact Opportunities:**
1. **Dynamic Task Injection System** — Not yet implemented; research shows 100% restoration success
2. **Quality Drift Detection** — Limited monitoring; research provides 15x efficiency patterns
3. **PreToolUse/PostToolUse Hooks** — Marked as planned; research validates approach
4. **Context Stream Management** — Not present; research shows 15x faster re-orientation
5. **Compaction Prediction & Handling** — Not implemented; research provides proven strategies

---

## Table of Contents

1. [Current OA Implementation Analysis](#current-implementation)
2. [Research Findings Applicability Matrix](#applicability-matrix)
3. [Enhancement Recommendations by Priority](#enhancements)
4. [Technical Implementation Roadmap](#roadmap)
5. [Auto-Injection & Review Aspects](#auto-injection)
6. [Triggers & Detection Mechanisms](#triggers)
7. [Integration Architecture](#integration)
8. [Validation & Testing Strategy](#validation)
9. [Implementation Code Examples](#code-examples)
10. [Risk Assessment & Mitigation](#risks)

---

## <a name="current-implementation"></a>1. Current OA Implementation Analysis

### 1.1 What's Currently Implemented ✅

**SHANK-ARM-FLUKE Architecture (Core Foundation)**
- ✅ Agent constitution files (`.claude/agents/*.oct.md`)
- ✅ SHANK identity definitions (MUST_ALWAYS, MUST_NEVER constraints)
- ✅ ARM phase context (CONCEPTUAL D0-D3, ACTUAL B0-B5)
- ✅ FLUKE skill definitions with base confidence scores
- ✅ Cognition types (LOGOS, ETHOS, PATHOS)

**UserPromptSubmit Hook (Constitutional Enforcement)**
- ✅ Agent constitution loading
- ✅ Phase detection from PROJECT-CONTEXT.md
- ✅ Skill confidence calculation (base + SHANK + ARM modulation)
- ✅ Constitutional reminder injection
- ✅ Session state management (1-hour timeout)
- ✅ Reminder suppression (once per agent activation)

**Technical Infrastructure**
- ✅ TypeScript implementation
- ✅ Path traversal protection
- ✅ File validation
- ✅ Error handling (graceful degradation)
- ✅ Logging and monitoring infrastructure

**Directory Structure**
- ✅ 61 agent definitions
- ✅ Organized library (foundation, cognitions, contexts, capabilities)
- ✅ Hook system with testing
- ✅ Documentation and guides

### 1.2 What's Marked as Planned (Not Yet Implemented) 📋

**PreToolUse Hook**
- 📋 JIT skill loading before tool execution
- 📋 Preventive skill injection
- 📋 Real-time capability modulation

**PostToolUse Hook**
- 📋 Outcome tracking and reinforcement
- 📋 Evidence collection for validation
- 📋 Learning from execution history

**Advanced Capabilities**
- 📋 Skill co-evolution mechanisms
- 📋 Dynamic affinity graph updates
- 📋 Self-learning from execution

### 1.3 What's Missing (Critical Gaps) ❌

**Dynamic Task Injection System**
- ❌ **No monitoring for quality degradation**
- ❌ **No dynamic recovery task injection**
- ❌ **No atomic task list management**
- ❌ **No forward-chaining pattern**

**Behavioral Monitoring**
- ❌ **No context stream tracking**
- ❌ **No quality drift detection**
- ❌ **No behavioral fingerprinting**
- ❌ **No continuous monitoring system**

**Context Compaction Handling**
- ❌ **No compaction prediction**
- ❌ **No pre-compaction preparation**
- ❌ **No post-compaction recovery**
- ❌ **No token usage monitoring**

**Integration with Workflow**
- ❌ **No integration with Claude Code task management**
- ❌ **No workflow-based verification enforcement**
- ❌ **No external orchestrator component**

**Validation & Learning**
- ❌ **No post-recovery quality verification**
- ❌ **No outcome-based learning**
- ❌ **No continuous improvement loop**

### 1.4 Architecture Comparison

| Component | OA Current Implementation | Research-Validated Pattern | Gap Analysis |
|-----------|---------------------------|----------------------------|--------------|
| **SHANK** | ✅ Constitutional files with MUST_ALWAYS/NEVER | ✅ Same approach | ✅ **Aligned** |
| **ARM** | ✅ Phase detection (CONCEPTUAL/ACTUAL) | ✅ Same approach | ✅ **Aligned** |
| **FLUKE** | ✅ Skill definitions + confidence scoring | ✅ Same approach | ✅ **Aligned** |
| **Constitutional Reminder** | ✅ Injected via UserPromptSubmit hook | ✅ Same approach | ✅ **Aligned** |
| **Quality Monitoring** | ❌ Not implemented | ✅ Context stream + RAPH analysis | ❌ **Missing** |
| **Drift Detection** | ❌ Not implemented | ✅ Behavioral fingerprinting | ❌ **Missing** |
| **Dynamic Injection** | ❌ Not implemented | ✅ Atomic task forward-chaining | ❌ **Missing** |
| **Compaction Handling** | ❌ Not implemented | ✅ Prediction + recovery | ❌ **Missing** |
| **Recovery Mechanism** | ❌ Not implemented | ✅ 100% validated workflow integration | ❌ **Missing** |
| **Verification Loop** | ❌ Not implemented | ✅ Post-recovery quality check | ❌ **Missing** |

---

## <a name="applicability-matrix"></a>2. Research Findings Applicability Matrix

### 2.1 Directly Applicable (Immediate Implementation) 🟢

| Research Finding | Applicability | Implementation Complexity | Impact |
|------------------|---------------|---------------------------|--------|
| **Dynamic Task Injection** | 100% | High | **CRITICAL** — 100% restoration |
| **Forward Chaining Pattern** | 100% | Medium | **HIGH** — Enables injection |
| **Context Stream Tracking** | 100% | Medium | **HIGH** — 15x efficiency |
| **Hook Limitations Understanding** | 100% | Low | **HIGH** — Prevents wasted effort |
| **Session State Management** | ✅ Already implemented | N/A | N/A |
| **SHANK-ARM-FLUKE Architecture** | ✅ Already implemented | N/A | N/A |

### 2.2 Applicable with Modification (Adaptation Required) 🟡

| Research Finding | Applicability | Modification Needed | Impact |
|------------------|---------------|---------------------|--------|
| **RAPH Sequential Processing** | 80% | Adapt for real-time monitoring | **MEDIUM** — Quality analysis |
| **Compaction Prediction** | 90% | May need Claude Code-specific metrics | **HIGH** — Proactive recovery |
| **Behavioral Fingerprinting** | 85% | Define OA-specific patterns | **HIGH** — Drift detection |
| **Multi-Agent Orchestration** | 70% | OA focuses on single-agent initially | **MEDIUM** — Future expansion |

### 2.3 Research Context (Informative, Not Directly Applicable) 🔵

| Research Finding | Relevance | Usage |
|------------------|-----------|-------|
| **Model Selection (25-50x cost)** | Informative | Context for why monitoring matters |
| **OCTAVE Protocol** | Informative | Possible future skill injection format |
| **Skill Loading Impact (70% overhead)** | ✅ Validates OA's approach | Confirms importance of phase-aware loading |

---

## <a name="enhancements"></a>3. Enhancement Recommendations by Priority

### Priority 1: Critical Enhancements (Implement First) 🔴

#### **Enhancement 1.1: External Orchestrator with Dynamic Task Injection**

**Research Evidence:**
- 100% role restoration success rate (validated 2025-06-21)
- Workflow integration superior to meta-instruction
- Forward chaining prevents desynchronization

**Current Gap:**
OA currently injects constitutional reminders but has no mechanism to:
- Monitor ongoing agent behavior
- Detect quality degradation
- Inject recovery tasks dynamically
- Maintain atomic task lists

**Recommended Implementation:**

```typescript
// New file: .claude/hooks/lib/external-orchestrator.ts

interface AtomicTask {
  id: string;           // e.g., "1", "1.5", "2"
  task: string;         // Description
  steps: string[];      // Step 1, 2, 3...
  next: string;         // Next task ID
  status: 'pending' | 'in_progress' | 'completed';
}

class ExternalOrchestrator {
  private atomicTasks: AtomicTask[] = [];
  private contextStream: ContextPoint[] = [];

  /**
   * Monitor agent output and detect degradation
   */
  monitorContinuously(): void {
    // Hook into PostToolUse to capture agent outputs
    // Analyze for quality drift, role adherence
    // Trigger injection when degradation detected
  }

  /**
   * Inject recovery task into workflow
   */
  injectRecoveryTask(currentTaskId: string): void {
    const recoveryTaskId = `${currentTaskId}.5`;

    const recoveryTask: AtomicTask = {
      id: recoveryTaskId,
      task: 'POST COMPACTION PROTOCOL',
      steps: [
        `Verify task ${currentTaskId} complete`,
        `Add task ${this.getNextTask(recoveryTaskId)} to TODO`,
        'Execute full ROLE_LOADING_PROTOCOL from .claude/agents/{active-agent}.oct.md'
      ],
      next: this.getNextTask(recoveryTaskId),
      status: 'pending'
    };

    this.atomicTasks.splice(
      this.findTaskIndex(currentTaskId) + 1,
      0,
      recoveryTask
    );

    // Update agent's TODO list (external file)
    this.updateAgentTodo();
  }

  /**
   * Forward chaining: Step 2 always adds NEXT task
   */
  private formatTaskSteps(taskId: string, task: AtomicTask): string[] {
    return [
      'STEP 1: Ensure all previous steps are marked off as complete',
      `STEP 2: Add "Check atomic list for task ${task.next}" to your todo list`,
      `STEP 3: ${task.task}`
    ];
  }
}
```

**Integration Points:**
- Create `.claude/hooks/lib/external-orchestrator.ts`
- Hook into PostToolUse (when implemented)
- Maintain `.claude/.oa-atomic-tasks.json`
- Update `.claude/.oa-agent-todo.md` dynamically

**Success Criteria:**
- Agent automatically executes recovery tasks when injected
- 100% role restoration after degradation
- No voluntary compliance required (workflow enforcement)

---

#### **Enhancement 1.2: Context Stream & Quality Monitoring**

**Research Evidence:**
- 15x faster re-orientation (2 min vs 30+ min)
- ~5KB vs 50+ pages of history
- 100% context with zero clarifying questions

**Current Gap:**
OA has session state (last agent, timestamp) but no:
- Sequential behavioral tracking
- Quality trend analysis
- Pattern-based drift detection

**Recommended Implementation:**

```typescript
// New file: .claude/hooks/lib/context-stream.ts

interface ContextPoint {
  id: number;
  type: 'discovery' | 'analysis' | 'synthesis' | 'drift-detection' | 'quality-drop';
  timestamp: string;
  participants: string[];  // e.g., ['HUMAN', 'implementation-lead']
  tags: string[];          // e.g., ['pattern-detection', 'quality-metrics']
  narrative: string;       // Brief description
  metrics: {
    quality_score?: number;
    role_adherence?: number;
    capability_utilization?: number;
  };
}

class ContextStreamManager {
  private stream: ContextPoint[] = [];
  private persistencePath = '.claude/.oa-context-stream.json';

  /**
   * Add context point from agent output
   */
  addContextPoint(output: string, agent: string): ContextPoint {
    const point: ContextPoint = {
      id: this.stream.length + 1,
      type: this.classifyOutput(output),
      timestamp: new Date().toISOString(),
      participants: ['HUMAN', agent],
      tags: this.extractTags(output),
      narrative: this.summarize(output),
      metrics: this.assessQuality(output, agent)
    };

    this.stream.push(point);
    this.persist();
    return point;
  }

  /**
   * Detect degradation trend
   */
  detectDegradation(windowSize: number = 5): boolean {
    if (this.stream.length < windowSize) return false;

    const recentPoints = this.stream.slice(-windowSize);
    const avgQuality = this.average(recentPoints.map(p => p.metrics.quality_score || 1.0));
    const avgAdherence = this.average(recentPoints.map(p => p.metrics.role_adherence || 1.0));

    // Degradation thresholds from research
    const qualityDrop = avgQuality < 0.7;
    const adherenceDrop = avgAdherence < 0.7;

    return qualityDrop || adherenceDrop;
  }

  /**
   * Classify output type
   */
  private classifyOutput(output: string): ContextPoint['type'] {
    // Pattern matching for output classification
    if (output.includes('Error:') || output.includes('failed')) return 'quality-drop';
    if (output.includes('pattern') || output.includes('recognize')) return 'discovery';
    // ... more classification logic
    return 'analysis';
  }

  /**
   * Assess quality metrics using RAPH-inspired analysis
   */
  private assessQuality(output: string, agent: string): ContextPoint['metrics'] {
    // Load agent constitutional patterns
    const constitution = this.loadAgentConstitution(agent);

    // Check for role-specific patterns
    const roleAdherence = this.checkRolePatterns(output, constitution);

    // Assess code quality if present
    const qualityScore = this.assessCodeQuality(output);

    // Check capability utilization
    const capabilityUtilization = this.checkCapabilities(output, constitution);

    return {
      quality_score: qualityScore,
      role_adherence: roleAdherence,
      capability_utilization: capabilityUtilization
    };
  }
}
```

**Integration Points:**
- Create `.claude/hooks/lib/context-stream.ts`
- Update PostToolUse hook to log context points
- Persist to `.claude/.oa-context-stream.json`
- Provide `/context-stream` command for viewing

**Success Criteria:**
- Continuous quality tracking throughout session
- Automated drift detection
- Rapid re-orientation on new session (read stream vs full history)

---

#### **Enhancement 1.3: Compaction Prediction & Pre-Recovery**

**Research Evidence:**
- Context compaction triggers quality loss
- Prediction at 90% enables proactive recovery
- Manual compaction superior to auto-compaction

**Current Gap:**
No monitoring of context usage or compaction prediction

**Recommended Implementation:**

```typescript
// Add to: .claude/hooks/lib/context-monitor.ts

class ContextCompactionMonitor {
  private readonly CONTEXT_LIMIT = 200000; // Claude Code limit
  private readonly WARNING_THRESHOLD = 0.85; // 85%
  private readonly CRITICAL_THRESHOLD = 0.90; // 90%

  private tokenCount = 0;

  /**
   * Track token usage (approximate)
   */
  updateTokenCount(newContent: string): void {
    // Approximate: 1 token ≈ 4 characters
    const estimatedTokens = Math.ceil(newContent.length / 4);
    this.tokenCount += estimatedTokens;
  }

  /**
   * Get current usage percentage
   */
  getUsagePercentage(): number {
    return (this.tokenCount / this.CONTEXT_LIMIT);
  }

  /**
   * Check if compaction is imminent
   */
  shouldTriggerPreCompaction(): boolean {
    return this.getUsagePercentage() >= this.WARNING_THRESHOLD;
  }

  /**
   * Check if critical (must compact now)
   */
  isCritical(): boolean {
    return this.getUsagePercentage() >= this.CRITICAL_THRESHOLD;
  }

  /**
   * Trigger pre-compaction workflow
   */
  async triggerPreCompactionWorkflow(orchestrator: ExternalOrchestrator): Promise<void> {
    console.error('⚠️  Context at 85% — triggering pre-compaction workflow');

    // Inject pre-compaction summary task
    orchestrator.injectTask({
      id: 'pre-compact-1',
      task: 'PREPARE FOR CONTEXT COMPACTION',
      steps: [
        'Verify all recent work is complete',
        'Write comprehensive summary to .claude/.oa-session-summary.md',
        'Include: active agent, current phase, completed tasks, next tasks',
        'Save all critical context that must survive compaction'
      ],
      next: 'compact-1'
    });

    // Inject manual compaction instruction
    orchestrator.injectTask({
      id: 'compact-1',
      task: 'MANUAL CONTEXT COMPACTION',
      steps: [
        'Review summary in .claude/.oa-session-summary.md',
        'Run: /compact with custom instructions to preserve key details',
        'Verify compaction summary includes all critical context'
      ],
      next: 'post-compact-1'
    });

    // Inject post-compaction recovery
    orchestrator.injectTask({
      id: 'post-compact-1',
      task: 'POST COMPACTION RECOVERY',
      steps: [
        'Load .claude/.oa-session-summary.md',
        'Execute full ROLE_LOADING_PROTOCOL',
        'Verify role identity and phase context restored',
        'Continue with next planned task'
      ],
      next: 'resume-work'
    });
  }
}
```

**Integration Points:**
- Create `.claude/hooks/lib/context-monitor.ts`
- Hook into every tool use to track tokens
- Trigger pre-compaction workflow at 85%
- Force workflow at 90%

**Success Criteria:**
- Compaction never happens unexpectedly
- Pre-compaction summaries preserve critical context
- Post-compaction recovery achieves 100% role restoration

---

### Priority 2: High-Value Enhancements (Implement Soon) 🟡

#### **Enhancement 2.1: PreToolUse Hook for JIT Skill Injection**

**Research Evidence:**
- Phase-appropriate skill loading eliminates 70% overhead
- Missing skills create systematic inefficiencies
- Skills fundamentally change approach, not just knowledge

**Current Status:** Marked as planned in OA roadmap

**Recommended Implementation:**

```typescript
// New file: .claude/hooks/pre_tool_use/skill-injector.ts

interface SkillInjectionDecision {
  skill: string;
  confidence: number;
  rationale: string;
  inject: boolean;
}

async function preToolUseOrchestrate(): Promise<void> {
  const input = await readStdin();
  const { tool, args, agent, phase } = parseInput(input);

  // Determine which skills are needed for this tool use
  const requiredSkills = determineRequiredSkills(tool, args);

  // Calculate confidence scores
  const injectionDecisions: SkillInjectionDecision[] = [];

  for (const skill of requiredSkills) {
    const baseScore = getBaseConfidence(skill, tool);
    const shankModulation = getShankModulation(skill, agent);
    const armModulation = getArmModulation(skill, phase);

    const finalConfidence = Math.min(1.0, baseScore + shankModulation + armModulation);

    injectionDecisions.push({
      skill,
      confidence: finalConfidence,
      rationale: `Base: ${baseScore}, SHANK: ${shankModulation}, ARM: ${armModulation}`,
      inject: finalConfidence >= 0.70
    });
  }

  // Inject skills above threshold
  const skillsToInject = injectionDecisions.filter(d => d.inject);

  if (skillsToInject.length > 0) {
    const skillContent = await loadSkills(skillsToInject.map(d => d.skill));

    // Output as context injection (PreToolUse can modify context)
    console.log(formatSkillInjection(skillContent, skillsToInject));
  }

  // Allow tool execution
  process.exit(0);
}

/**
 * Determine which skills are needed based on tool and args
 */
function determineRequiredSkills(tool: string, args: any): string[] {
  const skillMap: Record<string, string[]> = {
    'Write': ['build-execution', 'TDD-discipline'],
    'Edit': ['build-execution', 'verification-protocols'],
    'Bash': ['security-awareness', 'error-handling'],
    'Read': ['code-comprehension', 'pattern-recognition'],
    // ... more mappings
  };

  return skillMap[tool] || [];
}
```

**Integration Points:**
- Create `.claude/hooks/pre_tool_use/run-hook.sh`
- Create `.claude/hooks/pre_tool_use/skill-injector.ts`
- Update `.claude/settings.json` with PreToolUse hook
- Maintain skill-tool affinity matrix

**Success Criteria:**
- Skills injected JIT before relevant tool use
- Confidence scores reflect SHANK + ARM modulation
- Measurable reduction in inappropriate tool use

---

#### **Enhancement 2.2: PostToolUse Hook for Outcome Learning**

**Research Evidence:**
- Continuous learning improves detection accuracy
- Behavioral fingerprints evolve with agent use
- Outcome tracking enables validation

**Current Status:** Marked as planned in OA roadmap

**Recommended Implementation:**

```typescript
// New file: .claude/hooks/post_tool_use/outcome-tracker.ts

interface ToolOutcome {
  tool: string;
  args: any;
  agent: string;
  phase: string;
  success: boolean;
  skillsActive: string[];
  quality: number;
  adherence: number;
  timestamp: string;
}

async function postToolUseOrchestrate(): Promise<void> {
  const input = await readStdin();
  const { tool, args, result, agent, phase } = parseInput(input);

  // Assess outcome quality
  const outcome: ToolOutcome = {
    tool,
    args,
    agent,
    phase,
    success: assessSuccess(result),
    skillsActive: getActiveSkills(), // From PreToolUse
    quality: assessQuality(result),
    adherence: assessRoleAdherence(result, agent),
    timestamp: new Date().toISOString()
  };

  // Log to context stream
  contextStreamManager.addContextPoint(
    JSON.stringify(outcome),
    agent
  );

  // Update behavioral fingerprint
  behavioralFingerprint.updateFromOutcome(outcome);

  // Check if this indicates degradation
  if (outcome.quality < 0.6 || outcome.adherence < 0.6) {
    console.error('⚠️  Quality degradation detected in tool outcome');
    externalOrchestrator.considerRecoveryInjection();
  }

  // Allow continuation
  process.exit(0);
}

/**
 * Update behavioral fingerprint based on outcomes
 */
class BehavioralFingerprint {
  private outcomes: ToolOutcome[] = [];

  updateFromOutcome(outcome: ToolOutcome): void {
    this.outcomes.push(outcome);

    // Calculate rolling averages
    const recent = this.outcomes.slice(-20);
    const avgQuality = this.average(recent.map(o => o.quality));
    const avgAdherence = this.average(recent.map(o => o.adherence));

    // Update baseline expectations
    this.updateBaselines({
      expectedQuality: avgQuality,
      expectedAdherence: avgAdherence,
      toolUsagePatterns: this.analyzeToolPatterns(recent)
    });
  }

  private analyzeToolPatterns(outcomes: ToolOutcome[]): any {
    // Identify patterns in tool usage
    // e.g., "Edit" followed by "Bash" for testing
    // Returns pattern insights
  }
}
```

**Integration Points:**
- Create `.claude/hooks/post_tool_use/run-hook.sh`
- Create `.claude/hooks/post_tool_use/outcome-tracker.ts`
- Update `.claude/settings.json` with PostToolUse hook
- Persist outcomes to `.claude/.oa-outcomes.json`

**Success Criteria:**
- Every tool use tracked and assessed
- Behavioral fingerprint updates continuously
- Degradation detected proactively (before severe)

---

### Priority 3: Future Enhancements (Plan for Later) 🔵

#### **Enhancement 3.1: Multi-Agent Task Delegation**

**Research Context:**
- Research validates orchestration patterns
- OA currently focuses on single-agent
- Future expansion to multi-agent scenarios

**Recommended Approach:**
- Defer until single-agent monitoring is robust
- Design orchestrator to manage multiple agents
- Each agent maintains own SHANK-ARM-FLUKE identity
- Cross-agent constitutional coherence validation

---

#### **Enhancement 3.2: Self-Learning Skill Affinities**

**Research Context:**
- Static affinities work but suboptimal
- Learning from outcomes improves accuracy
- Affinity graphs can evolve

**Recommended Approach:**
- Start with static affinities (current OA approach)
- Track skill-tool success correlations
- Gradually adjust affinities based on evidence
- Requires significant data collection period

---

## <a name="roadmap"></a>4. Technical Implementation Roadmap

### Phase 1: Foundation (Weeks 1-2)

**Week 1: External Orchestrator Setup**
- [ ] Create `external-orchestrator.ts` with atomic task management
- [ ] Implement forward-chaining task pattern
- [ ] Create `.claude/.oa-atomic-tasks.json` persistence
- [ ] Create `.claude/.oa-agent-todo.md` dynamic TODO
- [ ] Test atomic task injection workflow

**Week 2: Context Stream & Monitoring**
- [ ] Create `context-stream.ts` with ContextPoint tracking
- [ ] Implement quality assessment metrics
- [ ] Create `.claude/.oa-context-stream.json` persistence
- [ ] Implement degradation detection algorithms
- [ ] Test monitoring accuracy

### Phase 2: Integration (Weeks 3-4)

**Week 3: Hook Integration**
- [ ] Integrate orchestrator with UserPromptSubmit hook
- [ ] Implement compaction monitoring
- [ ] Create pre/post compaction workflows
- [ ] Test end-to-end injection on degradation

**Week 4: PreToolUse & PostToolUse Hooks**
- [ ] Implement PreToolUse skill injection
- [ ] Implement PostToolUse outcome tracking
- [ ] Create behavioral fingerprint system
- [ ] Test JIT skill loading

### Phase 3: Validation (Weeks 5-6)

**Week 5: Empirical Testing**
- [ ] Run isolation protocol tests (from research)
- [ ] Measure role restoration success rate
- [ ] Validate against research benchmarks (100% target)
- [ ] Document any deviations or issues

**Week 6: Refinement**
- [ ] Tune detection thresholds based on testing
- [ ] Optimize performance (latency, overhead)
- [ ] Improve error handling
- [ ] Update documentation

### Phase 4: Production Hardening (Weeks 7-8)

**Week 7: Robustness**
- [ ] Add comprehensive error handling
- [ ] Implement fallback mechanisms
- [ ] Add logging and observability
- [ ] Performance optimization

**Week 8: Documentation & Release**
- [ ] Complete implementation documentation
- [ ] Create usage guides and examples
- [ ] Update README with new capabilities
- [ ] Tag release v2.0.0

---

## <a name="auto-injection"></a>5. Auto-Injection & Review Aspects

### 5.1 Auto-Injection Architecture

**Research-Validated Pattern:**

```
Trigger → Detection → Decision → Injection → Execution → Verification
```

**Implementation in OA:**

```typescript
class AutoInjectionSystem {
  /**
   * TRIGGER: What causes injection to be considered?
   */
  private triggers = {
    // Quality-based triggers
    qualityDrop: (metrics: QualityMetrics) => metrics.quality < 0.7,
    roleDrift: (metrics: QualityMetrics) => metrics.roleAdherence < 0.7,

    // Context-based triggers
    compactionImminent: () => contextMonitor.getUsagePercentage() > 0.85,
    compactionOccurred: () => detectCompactionEvent(),

    // Pattern-based triggers
    errorSpike: () => errorRate() > 0.3, // 30% error rate
    genericResponses: () => detectGenericPattern(),

    // Time-based triggers
    sessionDuration: () => sessionDuration() > 4 * 60 * 60 * 1000, // 4 hours
  };

  /**
   * DETECTION: Continuous monitoring
   */
  monitorContinuously(): void {
    setInterval(() => {
      const metrics = this.collectMetrics();

      for (const [triggerName, triggerFn] of Object.entries(this.triggers)) {
        if (triggerFn(metrics)) {
          this.handleTrigger(triggerName, metrics);
        }
      }
    }, 30000); // Check every 30 seconds
  }

  /**
   * DECISION: Should we inject?
   */
  private handleTrigger(trigger: string, metrics: any): void {
    const decision = this.makeInjectionDecision(trigger, metrics);

    if (decision.shouldInject) {
      this.executeInjection(decision);
    }
  }

  /**
   * INJECTION: Insert recovery task
   */
  private executeInjection(decision: InjectionDecision): void {
    const recoveryTask = this.createRecoveryTask(decision);
    this.orchestrator.injectTask(recoveryTask);

    // Log for verification
    this.log('INJECTION', {
      trigger: decision.trigger,
      taskId: recoveryTask.id,
      timestamp: new Date().toISOString()
    });
  }

  /**
   * VERIFICATION: Did it work?
   */
  private verifyRecovery(taskId: string): boolean {
    // Wait for task completion
    const postRecoveryMetrics = this.collectMetrics();

    const qualityRestored = postRecoveryMetrics.quality > 0.8;
    const roleRestored = postRecoveryMetrics.roleAdherence > 0.8;

    return qualityRestored && roleRestored;
  }
}
```

### 5.2 Review Aspects Implementation

**Automated Review Checkpoints:**

```typescript
interface ReviewCheckpoint {
  type: 'constitutional' | 'quality' | 'phase' | 'capability';
  frequency: 'per-tool' | 'per-task' | 'periodic' | 'on-trigger';
  validator: (context: any) => ReviewResult;
}

class AutoReviewSystem {
  private checkpoints: ReviewCheckpoint[] = [
    {
      type: 'constitutional',
      frequency: 'per-tool',
      validator: (ctx) => this.validateConstitutional(ctx)
    },
    {
      type: 'quality',
      frequency: 'per-task',
      validator: (ctx) => this.validateQuality(ctx)
    },
    {
      type: 'phase',
      frequency: 'on-trigger', // Phase transitions
      validator: (ctx) => this.validatePhaseAppropriate(ctx)
    },
    {
      type: 'capability',
      frequency: 'periodic', // Every 10 minutes
      validator: (ctx) => this.validateCapabilities(ctx)
    }
  ];

  /**
   * Constitutional review: MUST_ALWAYS / MUST_NEVER
   */
  private validateConstitutional(context: any): ReviewResult {
    const agent = context.activeAgent;
    const constitution = loadAgentConstitution(agent);

    // Check MUST_ALWAYS requirements
    const mustAlwaysViolations = this.checkMustAlways(
      context.output,
      constitution.MUST_ALWAYS
    );

    // Check MUST_NEVER prohibitions
    const mustNeverViolations = this.checkMustNever(
      context.output,
      constitution.MUST_NEVER
    );

    if (mustAlwaysViolations.length > 0 || mustNeverViolations.length > 0) {
      return {
        passed: false,
        violations: [...mustAlwaysViolations, ...mustNeverViolations],
        action: 'INJECT_CONSTITUTIONAL_REMINDER'
      };
    }

    return { passed: true };
  }

  /**
   * Quality review: Code quality, analysis depth
   */
  private validateQuality(context: any): ReviewResult {
    const qualityScore = assessCodeQuality(context.output);
    const depthScore = assessAnalysisDepth(context.output);

    if (qualityScore < 0.7 || depthScore < 0.7) {
      return {
        passed: false,
        metrics: { quality: qualityScore, depth: depthScore },
        action: 'INJECT_QUALITY_RECOVERY'
      };
    }

    return { passed: true };
  }

  /**
   * Phase-appropriate review: ARM validation
   */
  private validatePhaseAppropriate(context: any): ReviewResult {
    const currentPhase = detectPhase();
    const expectedBehaviors = getPhaseExpectations(currentPhase);

    const adherence = checkPhaseAdherence(
      context.output,
      expectedBehaviors
    );

    if (adherence < 0.7) {
      return {
        passed: false,
        issue: 'PHASE_INAPPROPRIATE_BEHAVIOR',
        action: 'INJECT_PHASE_REMINDER'
      };
    }

    return { passed: true };
  }
}
```

---

## <a name="triggers"></a>6. Triggers & Detection Mechanisms

### 6.1 Comprehensive Trigger Catalog

**Quality-Based Triggers:**

| Trigger Name | Detection Method | Threshold | Action |
|--------------|------------------|-----------|--------|
| **Quality Drop** | RAPH analysis of code quality | < 0.7 | Inject quality recovery |
| **Error Spike** | Track error rate in outputs | > 30% | Inject debugging recovery |
| **Incomplete Work** | Check for TODO accumulation | > 5 unresolved | Inject completion task |
| **Generic Responses** | Pattern matching for generic phrases | > 3 in sequence | Inject role reminder |

**Context-Based Triggers:**

| Trigger Name | Detection Method | Threshold | Action |
|--------------|------------------|-----------|--------|
| **Compaction Warning** | Token usage monitoring | > 85% | Inject pre-compaction workflow |
| **Compaction Critical** | Token usage monitoring | > 90% | Force compaction workflow |
| **Session Long** | Time tracking | > 4 hours | Inject role refresh |
| **Context Loss** | Detect compaction event | Compaction detected | Inject post-compaction recovery |

**Constitutional Triggers:**

| Trigger Name | Detection Method | Threshold | Action |
|--------------|------------------|-----------|--------|
| **MUST_NEVER Violation** | Pattern matching against prohibitions | Any violation | Block + inject reminder |
| **MUST_ALWAYS Omission** | Check for required behaviors | Missing requirement | Inject constitutional reminder |
| **Boundary Violation** | ARM phase check | Wrong phase behavior | Inject phase correction |

**Pattern-Based Triggers:**

| Trigger Name | Detection Method | Threshold | Action |
|--------------|------------------|-----------|--------|
| **Role Drift** | Behavioral fingerprint comparison | < 0.7 similarity | Inject role restoration |
| **Capability Misuse** | FLUKE utilization check | Wrong capability active | Inject skill correction |
| **Repetitive Errors** | Same error > N times | > 3 occurrences | Inject debugging task |

### 6.2 Trigger Implementation

```typescript
// .claude/hooks/lib/trigger-system.ts

interface Trigger {
  name: string;
  check: () => Promise<boolean>;
  severity: 'low' | 'medium' | 'high' | 'critical';
  action: () => Promise<void>;
  cooldown: number; // Milliseconds before can trigger again
  lastTriggered?: number;
}

class TriggerSystem {
  private triggers: Trigger[] = [
    {
      name: 'quality-drop',
      check: async () => {
        const recent = contextStream.getRecent(5);
        const avgQuality = average(recent.map(p => p.metrics.quality_score));
        return avgQuality < 0.7;
      },
      severity: 'high',
      action: async () => {
        await orchestrator.injectRecoveryTask('QUALITY_RESTORATION');
      },
      cooldown: 5 * 60 * 1000 // 5 minutes
    },
    {
      name: 'compaction-imminent',
      check: async () => {
        return contextMonitor.getUsagePercentage() > 0.85;
      },
      severity: 'critical',
      action: async () => {
        await orchestrator.triggerPreCompactionWorkflow();
      },
      cooldown: 30 * 60 * 1000 // 30 minutes (only warn once per session)
    },
    {
      name: 'constitutional-violation',
      check: async () => {
        const lastOutput = getLastAgentOutput();
        const violations = await reviewSystem.validateConstitutional(lastOutput);
        return !violations.passed;
      },
      severity: 'critical',
      action: async () => {
        await hookSystem.blockOperations();
        await orchestrator.injectConstitutionalReminder();
      },
      cooldown: 0 // Immediate, every time
    }
    // ... more triggers
  ];

  /**
   * Continuous trigger monitoring
   */
  async monitorTriggers(): Promise<void> {
    for (const trigger of this.triggers) {
      // Check cooldown
      if (trigger.lastTriggered &&
          Date.now() - trigger.lastTriggered < trigger.cooldown) {
        continue;
      }

      // Check condition
      if (await trigger.check()) {
        console.error(`🔔 Trigger activated: ${trigger.name} [${trigger.severity}]`);

        // Execute action
        await trigger.action();

        // Update last triggered
        trigger.lastTriggered = Date.now();
      }
    }
  }
}
```

---

## <a name="integration"></a>7. Integration Architecture

### 7.1 Complete System Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                      CLAUDE CODE                             │
│                    (Agent Executor)                          │
└────────────┬─────────────────────────────────────────────────┘
             │
             ↓
┌──────────────────────────────────────────────────────────────┐
│                    HOOK SYSTEM                               │
├──────────────────────────────────────────────────────────────┤
│  UserPromptSubmit   │  PreToolUse   │  PostToolUse          │
│  ✅ Implemented     │  📋 Planned   │  📋 Planned           │
│                     │               │                        │
│  • Agent loading    │  • JIT skills │  • Outcome tracking   │
│  • Phase detection  │  • Confidence │  • Quality assessment │
│  • Reminder inject  │  • Context    │  • Fingerprint update │
└────────────┬────────────┬────────────┬────────────────────────┘
             │            │            │
             ↓            ↓            ↓
┌──────────────────────────────────────────────────────────────┐
│              EXTERNAL ORCHESTRATOR (New)                     │
├──────────────────────────────────────────────────────────────┤
│  ┌────────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │ Context Stream │  │ Trigger Sys  │  │ Atomic Tasks    │  │
│  │                │  │              │  │                 │  │
│  │ • Track points │  │ • Monitor    │  │ • Maintain list │  │
│  │ • Assess       │  │ • Detect     │  │ • Inject tasks  │  │
│  │ • Detect drift │  │ • Trigger    │  │ • Forward chain │  │
│  └────────────────┘  └──────────────┘  └─────────────────┘  │
│                                                              │
│  ┌────────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │ Context Monitor│  │ Review System│  │ Behavioral FP   │  │
│  │                │  │              │  │                 │  │
│  │ • Token track  │  │ • Validate   │  │ • Learn         │  │
│  │ • Predict      │  │ • Checkpoints│  │ • Update        │  │
│  │ • Pre-compact  │  │ • Block      │  │ • Compare       │  │
│  └────────────────┘  └──────────────┘  └─────────────────┘  │
└──────────────────────┬───────────────────────────────────────┘
                       │
                       ↓
┌──────────────────────────────────────────────────────────────┐
│                  PERSISTENCE LAYER                           │
├──────────────────────────────────────────────────────────────┤
│  • .oa-atomic-tasks.json      (Task list)                    │
│  • .oa-context-stream.json    (Context points)               │
│  • .oa-session-state.json     (Current state)                │
│  • .oa-behavioral-fp.json     (Fingerprint)                  │
│  • .oa-outcomes.json          (Tool outcomes)                │
│  • .oa-agent-todo.md          (Dynamic TODO)                 │
│  • .oa-session-summary.md     (Pre-compaction summary)       │
└──────────────────────────────────────────────────────────────┘
```

### 7.2 Data Flow

**Normal Workflow:**
```
User Prompt
  → UserPromptSubmit Hook (constitutional check)
  → Claude Code (processes prompt)
  → PreToolUse Hook (JIT skill injection)
  → Tool Execution
  → PostToolUse Hook (outcome tracking)
  → Context Stream Update
  → Trigger System Check
  → [If no trigger] Continue
```

**Recovery Workflow:**
```
Trigger Detected (e.g., quality drop)
  → External Orchestrator Decision
  → Atomic Task List Update (inject recovery task)
  → Agent TODO Update
  → [Hook unblocks if blocked]
  → Agent Reads TODO
  → Agent Executes Recovery Task
  → Role Loading Protocol
  → Quality Verification
  → Resume Normal Workflow
```

---

## <a name="validation"></a>8. Validation & Testing Strategy

### 8.1 Validation Against Research Benchmarks

**Target Metrics (from research):**

| Metric | Research Benchmark | OA Target | Validation Method |
|--------|-------------------|-----------|-------------------|
| **Role Restoration Success** | 100% | 100% | Isolation protocol testing |
| **Quality Improvement** | 31.3% (RAPH) | N/A (different context) | Comparative analysis |
| **Context Stream Efficiency** | 15x faster | 10x+ faster | Re-orientation time trials |
| **Compaction Prediction** | 90% accuracy | 85%+ accuracy | Prediction vs actual events |
| **Constitutional Adherence** | 100% blocking | 100% blocking | Violation testing |

### 8.2 Testing Protocol

**Phase 1: Unit Testing**
```typescript
describe('ExternalOrchestrator', () => {
  it('should inject recovery task with forward chaining', () => {
    const orchestrator = new ExternalOrchestrator();
    orchestrator.addTask({ id: '1', task: 'Setup', next: '2' });
    orchestrator.addTask({ id: '2', task: 'Implement', next: '3' });

    orchestrator.injectRecoveryTask('1');

    const tasks = orchestrator.getTasks();
    expect(tasks[1].id).toBe('1.5');
    expect(tasks[1].next).toBe('2');
  });
});
```

**Phase 2: Integration Testing**
```typescript
describe('Trigger System Integration', () => {
  it('should detect quality drop and inject recovery', async () => {
    // Simulate degraded output
    contextStream.addContextPoint({
      quality_score: 0.5,
      role_adherence: 0.6
    });

    // Run trigger check
    await triggerSystem.monitorTriggers();

    // Verify injection
    const tasks = orchestrator.getTasks();
    expect(tasks.some(t => t.task.includes('RECOVERY'))).toBe(true);
  });
});
```

**Phase 3: Empirical Validation**
```bash
# Run isolation protocol (from research)
1. Set up clean workspace
2. Activate agent with known constitution
3. Simulate degradation (long session, compaction)
4. Verify automatic recovery injection
5. Measure restoration success rate
6. Target: 100% restoration (research benchmark)
```

---

## <a name="code-examples"></a>9. Implementation Code Examples

### 9.1 Complete Hook Integration

**File: `.claude/hooks/user_prompt_submit/constitutional-orchestrator.ts`**

```typescript
// Extend current implementation with orchestrator integration

import { ExternalOrchestrator } from '../lib/external-orchestrator';
import { ContextStreamManager } from '../lib/context-stream';
import { TriggerSystem } from '../lib/trigger-system';

// Existing orchestrate function
async function orchestrate(): Promise<void> {
  // ... existing code for constitutional loading ...

  // NEW: Initialize monitoring systems
  const orchestrator = ExternalOrchestrator.getInstance();
  const contextStream = ContextStreamManager.getInstance();
  const triggerSystem = TriggerSystem.getInstance();

  // NEW: Log context point
  contextStream.addContextPoint(userPrompt, agentName);

  // NEW: Check triggers
  await triggerSystem.monitorTriggers();

  // ... existing code for constitutional injection ...
}
```

**File: `.claude/hooks/post_tool_use/outcome-tracker.ts`** (New)

```typescript
import { ContextStreamManager } from '../lib/context-stream';
import { ExternalOrchestrator } from '../lib/external-orchestrator';

async function orchestrate(): Promise<void> {
  const input = await readStdin();
  const { tool, args, result } = JSON.parse(input);

  // Track outcome
  const contextStream = ContextStreamManager.getInstance();
  const outcome = assessOutcome(tool, args, result);

  contextStream.addContextPoint(
    `Tool: ${tool}, Success: ${outcome.success}, Quality: ${outcome.quality}`,
    getActiveAgent()
  );

  // Check for degradation
  if (contextStream.detectDegradation()) {
    console.error('⚠️  Degradation detected in tool outcome');

    const orchestrator = ExternalOrchestrator.getInstance();
    await orchestrator.considerRecoveryInjection();
  }

  process.exit(0);
}

orchestrate().catch(console.error);
```

### 9.2 Configuration Files

**File: `.claude/settings.json`** (Updated)

```json
{
  "hooks": {
    "SessionStart": {
      "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/session_start/setup-dependencies.sh"
    },
    "UserPromptSubmit": {
      "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/user_prompt_submit/run-hook.sh"
    },
    "PreToolUse": {
      "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/pre_tool_use/run-hook.sh"
    },
    "PostToolUse": {
      "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/post_tool_use/run-hook.sh"
    }
  }
}
```

**File: `.claude/.oa-config.json`** (New)

```json
{
  "monitoring": {
    "enableContinuous": true,
    "checkIntervalMs": 30000,
    "contextStreamMaxPoints": 100
  },
  "triggers": {
    "qualityDropThreshold": 0.7,
    "roleAdherenceThreshold": 0.7,
    "compactionWarningPercent": 85,
    "compactionCriticalPercent": 90
  },
  "injection": {
    "enableAutoRecovery": true,
    "requireVerification": true,
    "maxInjectionsPerSession": 5
  },
  "learning": {
    "enableBehavioralFingerprint": true,
    "outcomeHistorySize": 100,
    "updateFrequency": "continuous"
  }
}
```

---

## <a name="risks"></a>10. Risk Assessment & Mitigation

### 10.1 Implementation Risks

| Risk | Severity | Probability | Mitigation |
|------|----------|-------------|------------|
| **Performance overhead** | Medium | High | Optimize monitoring frequency, async processing |
| **False positive injections** | Medium | Medium | Tune thresholds empirically, add cooldowns |
| **Hook execution failures** | High | Low | Graceful degradation, comprehensive error handling |
| **Agent confusion from injections** | Low | Low | Clear task formatting, natural language |
| **Persistence layer failures** | Medium | Low | Fallback to in-memory, regular backups |
| **Token counting inaccuracy** | Low | Medium | Use conservative estimates, trigger early |

### 10.2 Mitigation Strategies

**Performance Optimization:**
```typescript
// Use debouncing for expensive checks
const debouncedQualityCheck = debounce(
  () => contextStream.assessQuality(),
  5000 // Only check every 5 seconds max
);

// Async monitoring to avoid blocking
async function monitorAsync(): Promise<void> {
  setImmediate(async () => {
    await triggerSystem.monitorTriggers();
    monitorAsync(); // Continue loop
  });
}
```

**False Positive Prevention:**
```typescript
// Require multiple confirmations for non-critical triggers
class TriggerSystem {
  private confirmations = new Map<string, number>();

  async checkTrigger(trigger: Trigger): Promise<boolean> {
    if (await trigger.check()) {
      const count = (this.confirmations.get(trigger.name) || 0) + 1;
      this.confirmations.set(trigger.name, count);

      // Require 3 consecutive confirmations for non-critical
      const threshold = trigger.severity === 'critical' ? 1 : 3;
      return count >= threshold;
    } else {
      this.confirmations.set(trigger.name, 0);
      return false;
    }
  }
}
```

---

## 11. Conclusion

### Summary of Recommendations

The OA repository has built a **solid foundation** with the SHANK-ARM-FLUKE architecture and UserPromptSubmit hook. To achieve the **100% role restoration success** demonstrated in research, the following critical enhancements are needed:

**Priority 1 (Critical):**
1. ✅ **External Orchestrator** — Dynamic task injection system
2. ✅ **Context Stream** — 15x efficiency behavioral tracking
3. ✅ **Compaction Handling** — Prediction and recovery workflows

**Priority 2 (High-Value):**
4. ✅ **PreToolUse Hook** — JIT skill injection
5. ✅ **PostToolUse Hook** — Outcome learning and verification

**Priority 3 (Future):**
6. ✅ **Multi-Agent Orchestration** — Scale beyond single-agent
7. ✅ **Self-Learning Affinities** — Dynamic skill evolution

### Expected Outcomes

With these enhancements implemented, OA will achieve:

- **100% role restoration** after context compaction (vs current: unhandled)
- **Proactive degradation prevention** (vs current: reactive constitutional reminders)
- **15x faster re-orientation** on session restart (vs current: full context reload)
- **Validated production-ready monitoring** (vs current: proof-of-concept)
- **Continuous learning and improvement** (vs current: static configuration)

### Next Steps

1. **Review this analysis** with OA maintainers
2. **Prioritize enhancements** based on resources and timeline
3. **Begin Phase 1 implementation** (External Orchestrator + Context Stream)
4. **Validate against research benchmarks** throughout development
5. **Document learnings** and contribute back to HestAI research

---

**Document Maintenance:**
- **Created:** 2025-11-19
- **Repository Analyzed:** https://github.com/elevanaltd/oa
- **Research Base:** HestAI Research Repository (248 documents)
- **Confidence Level:** 0.95 (High confidence in applicability)
- **Recommended Review Frequency:** Quarterly as OA evolves

**Related Documents:**
- `odyssean-anchor-monitoring-injection-system-consolidated-2025.md` — Complete research consolidation
- All source documents in Section 9.1 of consolidated findings
