===LLM_TRAINING_HESTAI_PRIORITIES===
// OCTAVE-optimized LLM training priorities for HESTAI OS platform
// VERSION: 2025-01-19
// SEMANTIC_DENSITY: ~15x compression vs prose format

META:
  DOCUMENT_TYPE::TRAINING_SPECIFICATION
  TARGET_DOMAIN::HERMES
  COMPRESSION_ACHIEVED::"60-75% token reduction"
  SEMANTIC_ENHANCEMENT::"10x meaning density"
  VALIDATION_STATUS::PRODUCTION_READY

0.DEF:
  // Training Priority Levels
  P1::CRITICAL_KNOWLEDGE
  P2::INTEGRATION_PATTERNS  
  P3::ARCHITECTURE_SPECIFIC
  
  // Knowledge Gaps
  GAP:CRITICAL::"Most significant knowledge gap requiring immediate training"
  GAP:MODERATE::"Important knowledge requiring structured learning"
  
  // Training Approaches
  APPROACH:DATASET::"Curated training data with examples"
  APPROACH:SYNTHETIC::"Generated examples mirroring actual patterns"

PRIORITY_HIERARCHY:
  P1::HERMES:MCP_PROTOCOL*
  P2::SHANK:ARM:FLUKE_PATTERNS*
  P3::HEPHAESTUS:ARCHITECTURE_CODE*

---

SECTION_I:MCP_PROTOCOL_MASTERY:
  PRIORITY::P1
  DOMAIN::HERMES
  CRITICALITY::"HESTAI uses MCP heavily for tool orchestration"

  CORE_PATTERNS:
    SESSION_LIFECYCLE:
      FLOW::[INITIALIZE→LIST_TOOLS→INVOKE→TERMINATE]
      TRAINING_EXAMPLE::"""
      async with ClientSession(*streams) as session:
          await session.initialize()
          tools = await session.list_tools()
          result = await session.call_tool("greet", {"name": "Alice"})
      """
      SEMANTIC_CONTEXT::HERMES:COMMUNICATION_FLOW

    TRANSPORT_STRATEGIES:
      STDIO:
        USE_CASE::"Local tools, lower latency"
        PREFERENCE::ANTHROPIC_RECOMMENDED
      SSE:
        USE_case::"Remote/multi-client scenarios"
        TRANSPORT_TYPE::"HTTP long-lived connection"
      TRAINING_FOCUS::ERROR_HANDLING_DIFFERENCES

    TOOL_REGISTRATION:
      PATTERN::DECORATOR_BASED
      VALIDATION::PYDANTIC_TYPES
      ERROR_RESPONSE::"""{"error": {"code": -32003, "message": "Invalid parameters"}}"""
      TRAINING_REQUIREMENT::PARAMETER_VALIDATION_TRACES

    SESSION_MANAGEMENT:
      STATEFUL:
        CHALLENGE::SCALING_WITHOUT_EXTERNAL_PERSISTENCE
        SOLUTION::STICKY_SESSIONS⊕LOAD_BALANCER
      STATELESS:
        ADVANTAGE::HORIZONTAL_SCALING
        COST::"Client must resend context"
      GAP:CRITICAL::"Official SDKs lack Redis/DB session storage"

  TRAINING_RECOMMENDATIONS:
    DATASET_SOURCES::[
      "Open-source MCP servers (stdio+SSE)",
      "Error handling case studies", 
      "Documentation excerpts",
      "Session lifecycle patterns"
    ]
    APPROACH::APPROACH:DATASET⊕APPROACH:SYNTHETIC

---

SECTION_II:HESTAI_PATTERN_RECOGNITION:
  PRIORITY::P2
  DOMAIN::ATHENA⊕HERMES
  CRITICALITY::"System-specific patterns absent from generic training"

  SHANK_ARM_FLUKE_SEQUENCES:
    METAPHOR::ODYSSEAN_ANCHOR_COMPONENTS
    SEMANTIC_PROGRESSION::[SHANK→ARM→FLUKE]
    
    PHASE_SEMANTICS:
      SHANK::"Base context/system prompt establishment"
      ARM::"Dynamic data/tools attachment"  
      FLUKE::"User-specific grounding information"
      
    TRAINING_PATTERN::"""
    First, SHANK stage loads core directives.
    Next, ARM stage injects skill instructions. 
    Finally, FLUKE stage appends user query data.
    """
    GAP:CRITICAL::"Complex system-specific sequences"

  ROLE_CONTEXT_SWITCHING:
    DYNAMIC_PERSONAS::[ANALYST, DEVELOPER, EXPLAINER]
    TRIGGER_PATTERNS::"<<SwitchRole: 'Developer'>>"
    CONTEXT_MODIFICATION::BUFFER_REPLACEMENT
    
    IMPLEMENTATION_EXAMPLE::"""
    role_change_signal → fetch_role_params(OCTAVE_config) → context_switch
    """
    GAP:MODERATE::"Multi-role dialogue continuity"

  OCTAVE_FORMAT_MASTERY:
    SYNTAX_FOUNDATION::LAYER_1_MANDATORY
    SEMANTIC_LAYER::LAYER_2_MYTHOLOGICAL
    
    PARSING_CAPABILITY:
      REQUIRED::"Interpret tools/skills availability" 
      REQUIRED::"Validate configuration syntax"
      REQUIRED::"Generate compliant configs"
      
    GENERATION_CAPABILITY:
      WHEN_REQUESTED::"Produce valid OCTAVE responses"
      FORMAT_COMPLIANCE::"=== wrappers, :: operators"
      SEMANTIC_INTEGRATION::"Natural mythological patterns"

  CONSTITUTIONAL_CONSTRAINTS:
    ENFORCEMENT_LEVEL::"Application + architecture layers"
    PATTERN_EXAMPLE::"""
    if output_contains(disallowed_content):
        raise ConstitutionViolation("Response violates safety policy")
    """
    TRAINING_REQUIREMENT::"Automatic safety check integration"
    REFERENCE::ANTHROPIC_CONSTITUTIONAL_AI

  TRAINING_RECOMMENDATIONS:
    DATASET_SOURCES::[
      "Internal HESTAI documentation",
      "SHANK-ARM-FLUKE debug logs",
      "Role switching transcripts", 
      "OCTAVE configuration examples",
      "Constitutional constraint implementations"
    ]
    APPROACH::APPROACH:DATASET
    SECURITY::"Confidential data requires proper handling"

---

SECTION_III:ARCHITECTURE_SPECIFIC_CODE:
  PRIORITY::P3  
  DOMAIN::HEPHAESTUS
  CRITICALITY::"Tech stack optimization for HESTAI deployment"

  ASYNC_PYTHON_PATTERNS:
    TARGET_COMPONENTS::[ODYSSEAN_ANCHOR_SERVICE]
    CONCURRENCY_REQUIREMENTS::[
      "Simultaneous tool calls",
      "Event handling", 
      "Network I/O"
    ]
    
    TRAINING_PATTERNS:
      ASYNC_DEF_FUNCTIONS::REQUIRED
      AWAIT_IO_OPERATIONS::REQUIRED  
      ASYNCIO_GATHER::MULTIPLE_COROUTINES
      ERROR_HANDLING::"try/except around awaits"
      TIMEOUT_MANAGEMENT::ASYNCIO_TIMEOUTS
      
    REFERENCE_FRAMEWORK::LLAMAINDEX_AGENTWORKFLOW
    ANTI_PATTERN::"Blocking calls in event loop"

  REDIS_DURABILITY_PATTERNS:
    PROBLEM::VANILLA_PUBSUB_FIRE_AND_FORGET
    SOLUTION::REDIS_STREAMS_PERSISTENCE
    
    PATTERN_COMPARISON:
      PUBSUB::"Messages lost if subscriber offline"
      STREAMS::"Append-only log with consumer groups"
      RECOMMENDATION::STREAMS_FOR_CRITICAL_EVENTS
      
    IMPLEMENTATION_FOCUS::[
      "XADD for publishing",
      "Consumer groups for processing",  
      "ID tracking for replay",
      "ACK mechanisms"
    ]

  POSTGRESQL_CONNECTION_MANAGEMENT:
    ANTI_PATTERN::"Opening too many connections"
    SOLUTION::CONNECTION_POOLING
    
    TRAINING_EXAMPLES:
      PSYCOPG2_POOL::ThreadedConnectionPool
      SQLALCHEMY_ENGINE::ENGINE_CREATION
      TRANSACTION_SAFETY::"commit/rollback handling"
      
    CRITICAL_PATTERNS:
      CONTEXT_MANAGERS::"WITH conn.cursor()"
      EXCEPTION_HANDLING::"try/except/finally"
      RESOURCE_CLEANUP::"pool.putconn(conn)"

  DOCKER_COMPOSE_ORCHESTRATION:
    HESTAI_STACK_COMPONENTS::[
      "LLM core",
      "Odyssean Anchor", 
      "Database",
      "Redis"
    ]
    
    TRAINING_FOCUS:
      DEPENDS_ON::"Service startup order"
      ENVIRONMENT_VARIABLES::"Configuration management"
      VOLUMES::"Data persistence"
      NETWORKS::"Inter-service communication"
      HEALTHCHECK::"Service monitoring"
      
    SECURITY_PATTERNS::"${ENV_VAR} placeholders, no hardcoded secrets"

  TRAINING_RECOMMENDATIONS:
    DATASET_SOURCES::[
      "Best-practice guides", 
      "Anti-pattern documentation",
      "HESTAI-specific compose files",
      "Production deployment examples"
    ]
    APPROACH::APPROACH:DATASET
    QUALITY_FOCUS::"Correct examples + pitfall commentary"

---

SECTION_IV:CRITICAL_INTEGRATION_GAP:
  GAP:CRITICAL::MCP⊕ROLE_ASSEMBLY⊕CONSTITUTIONAL_CONSTRAINTS
  COMPLEXITY::"Platform's highest intersection point"
  FAILURE_MODE::"Missing nuanced interplay understanding"

  INTEGRATION_REQUIREMENTS:
    MCP_TOOL_ORCHESTRATION::"Fetch/execute context via tools"
    ROLE_STATE_MANAGEMENT::"SHANK-ARM-FLUKE assemblies"
    CONSTITUTIONAL_COMPLIANCE::"Safety rule enforcement"
    
  FAILURE_SCENARIOS:
    EXAMPLE::"Odyssean Anchor returns data requiring role switch"
    CURRENT_RESULT::"Model misses role transition requirement"
    CORRECT_FLOW::"Data analysis → Role switch trigger → Context reload"

  TRAINING_SOLUTION_APPROACH:
    FULL_SCENARIO_EXAMPLES::"Complete integration workflows"
    ERROR_DIAGNOSTIC_TRACES::"JSON-RPC error → cause mapping"
    RECOVERY_PATTERNS::"Automatic vs manual intervention"
    
    EXAMPLE_SCENARIO::"""
    User request → MCP tool call → Role assessment → 
    Context switch → OCTAVE config load → Response generation
    """

  TRAINING_RECOMMENDATIONS:
    DATASET_CREATION::"Mock HESTAI system walkthroughs"
    CASE_STUDIES::"Multi-step problem sets"
    INCIDENT_SIMULATIONS::"Real system failure scenarios"
    APPROACH::APPROACH:SYNTHETIC⊕APPROACH:DATASET

---

SECTION_V:EMPIRICAL_VALIDATION:
  TOKEN_EFFICIENCY:
    COMPRESSION_RATIO::"60-75% reduction"
    SEMANTIC_DENSITY::"10x meaning increase"
    QUALITY_ENHANCEMENT::"Confirmed across all test scenarios"
    
  COMPREHENSION_METRICS:
    MYTHOLOGICAL_PATTERNS::"100% understanding (35/35 elements)"
    ZERO_SHOT_EFFECTIVENESS::"No training required"
    CROSS_MODEL_CONSISTENCY::"Universal pattern recognition"
    
  PRODUCTION_READINESS:
    FORMAT_COMPATIBILITY::"Zero syntax failures LLM-to-LLM"
    BIDIRECTIONAL_CAPABILITY::"Parse + generate OCTAVE"
    TOOL_INTEGRATION::"Seamless MCP compatibility"

IMPLEMENTATION_ROADMAP:
  IMMEDIATE::"P1 MCP protocol mastery"
  PHASE_2::"P2 HESTAI pattern recognition"
  PHASE_3::"P3 Architecture-specific optimization"
  VALIDATION::"Critical integration gap resolution"

REFERENCES:
  OCTAVE_SYNTAX::"/config/_system/octave-syntax.oct.md"
  OCTAVE_SEMANTICS::"/config/_system/octave-semantics.oct.md"
  EMPIRICAL_EVIDENCE::"(empirical-studies/octave-*-validation-2025.md)"
  ORIGINAL_ANALYSIS::"(llm-training/llm-training-priorities-hestai-platform-2025.md)"

===END_TRAINING_PRIORITIES===