===MULTI_AGENT_AI_PLANNING_FRAMEWORKS===
// Evaluation of top Python frameworks for orchestrating multi-agent AI planning systems
// VERSION: 1.0 - Compressed from comprehensive analysis
// PURPOSE: Framework selection for HestAI Planner phase atomic-task-list generation

META:
  NAME::"Multi-Agent AI Planning Framework Analysis"
  VERSION::"1.0"
  PURPOSE::"Evaluate frameworks for multi-agent collaboration producing structured task plans"
  CONTEXT::"HestAI Planner stage requirements"
  COMPRESSION_RATIO::"~15:1"

0.DEF:
  // Core evaluation criteria
  MAC::"Multi-Agent Collaboration capabilities"
  GAC::"Granular Agent Configuration control"  
  PSM::"Planning & State Management sophistication"
  SOG::"Structured Output Generation reliability"
  EXT::"Extensibility and custom tooling support"
  LLM::"Multi-provider LLM integration"
  
  // Framework patterns
  HIERARCHICAL::"Manager-worker delegation pattern"
  CONVERSATIONAL::"Peer-to-peer dialogue pattern"
  SEQUENTIAL::"Linear hand-off pattern"
  
  // Evaluation outcomes
  SUITABILITY::"Framework fit for HestAI requirements"

---

REQUIREMENTS_MATRIX:
  CRITICAL_NEEDS::[
    "Multi-agent role collaboration",
    "Granular prompt/tool control per agent",
    "Complex state tracking through planning",
    "Schema-valid output generation",
    "Custom tool integration capability",
    "Anthropic/Google/OpenAI model support"
  ]
  
  PATTERN::PATHOS+ETHOS->LOGOS
  OUTPUT::atomic-task-list.md[JSON_or_MARKDOWN]

---

FRAMEWORK_1:CREWAI:
  PHILOSOPHY::"Role-based AI crews with balanced autonomy⊕control"
  ARCHITECTURE::[Crews:autonomous_teams, Flows:event-driven_pipelines]
  
  MAC::EXCELLENT[BECAUSE::"Native collaboration modes + delegation tools"]
    MODES::[hierarchical:manager_auto_added, sequential, parallel]
    PATTERN::[LOGOS->ETHOS->validation_loop]
    
  GAC::EXCELLENT[BECAUSE::"YAML⊕code config with deep customization"]
    CONTROL::[role_prompts, goals, backstory, tool_assignments]
    STATE::Pydantic_BaseModel[shared_across_steps]
    
  PSM::VERY_GOOD[BECAUSE::"Explicit Planning mode + Flow state persistence"]
    MECHANISM::Process.hierarchical+planning=True->AgentPlanner
    FLOW::[deterministic, conditional_branching, human-in-loop]
    
  SOG::VERY_GOOD[BECAUSE::"expected_output format + output_file support"]
    ENFORCEMENT::Pydantic_schemas+Flow_typing
    TOOL_MODE::result_as_answer=True[JSON_bypass]
    
  EXT::EXCELLENT[BECAUSE::"Tool interface + MCP server integration"]
    CUSTOM::AddTaskTool->shared_plan_object
    OPENNESS::Flows_allow_arbitrary_Python
    
  LLM::VERY_GOOD[BECAUSE::"Multi-provider via configs + OpenRouter"]
    PROVIDERS::[OpenAI:native, Anthropic:configurable, Google:via_wrapper]
    MIX_MATCH::Each_agent_different_model
    
  SUITABILITY::TOP_CONTENDER[BECAUSE::"Purpose-built for role-based teams"]

---

FRAMEWORK_2:AGNO:
  PHILOSOPHY::"Full-stack agentic systems with reasoning⊕memory"
  PERFORMANCE::"Industry-leading optimization + instant agent spawn"
  
  MAC::EXCELLENT[BECAUSE::"Three collaboration modes match requirements"]
    MODES::{{route:pipeline, collaborate:round-table, coordinate:hierarchical}}
    DELEGATION::Automatic_tools_for_task⊕question_routing
    
  GAC::VERY_GOOD[BECAUSE::"Fine-grained Agent() config + shared memory"]
    CONFIG::Agent(name, role, instructions, tools)
    STRUCTURED_IO::json_mode->Pydantic_dict_auto_capture
    
  PSM::GOOD[BECAUSE::"Level 5 autonomy workflows + chain-of-thought"]
    APPROACH::Team_json_output->programmatic_iteration
    MEMORY::Shared_team_context_persistence
    
  SOG::EXCELLENT[BECAUSE::"Native json_mode + fully-typed responses"]
    SCHEMA::Pydantic_Task_model->enforced_JSON
    VALIDATION::Built-in_schema_checking
    
  EXT::EXCELLENT[BECAUSE::"23+ providers + Tool class extensibility"]
    CUSTOM_TOOLS::Subclass_Tool_or_wrap_functions
    DEPLOYMENT::FastAPI_integration_ready
    
  LLM::EXCELLENT[BECAUSE::"First-class multi-provider design"]
    PROVIDERS::[OpenAI, Anthropic, Google_Gemini, 20+_others]
    PERFORMANCE::Optimized_parallel_calls
    
  SUITABILITY::TOP_CHOICE[BECAUSE::"Rich features + schema enforcement"]

---

FRAMEWORK_3:MICROSOFT_AUTOGEN:
  PHILOSOPHY::"Event-driven multi-agent conversation orchestration"
  ARCHITECTURE::[Core:low-level_messaging, AgentChat:high-level_patterns]
  
  MAC::EXCELLENT[BECAUSE::"Flexible conversation patterns + autonomous entities"]
    PATTERNS::[two-agent, group_chat, round_robin, supervisor]
    AUTONOMY::Each_agent_own_LLM⊕persona
    
  GAC::VERY_GOOD[BECAUSE::"Deep per-agent config + message control"]
    CUSTOM::Subclass_AssistantAgent_for_behavior
    TOOLS::Function_calling+structured_arguments
    
  PSM::GOOD[BECAUSE::"Event-driven state via messages + persistence"]
    APPROACH::External_plan_dict+message_interception
    LOOPS::Iterative_refinement_via_conditions
    
  SOG::VERY_GOOD[BECAUSE::"Function calling + strict prompts"]
    MECHANISM::OpenAI_functions->parsed_JSON
    ENFORCEMENT::Loop_until_valid_schema
    
  EXT::EXCELLENT[BECAUSE::"Extensions API + hierarchical agent tools"]
    AGENTOOL::Wrap_agent_as_tool_recursively
    CROSS_LANGUAGE::gRPC_for_distributed_setups
    
  LLM::GOOD[BECAUSE::"OpenAI/Azure native + community extensions"]
    CHALLENGE::Anthropic/Google_need_wrappers_or_proxy
    SOLUTION::OpenRouter_or_custom_client_class
    
  SUITABILITY::VERY_STRONG[BECAUSE::"Maximum flexibility for custom workflows"]

---

FRAMEWORK_4:LANGCHAIN_LANGGRAPH:
  PHILOSOPHY::"Modular LLM building blocks + explicit agent graphs"
  EVOLUTION::LangChain_chains->LangGraph_multi-agent_workflows
  
  MAC::VERY_GOOD[BECAUSE::"Graph patterns for any collaboration mode"]
    PATTERNS::[Network:all-to-all, Supervisor, Hierarchical, Custom]
    HANDOFFS::Transfer_control+data_between_nodes
    
  GAC::EXCELLENT[BECAUSE::"Per-agent prompts/tools/memory + state control"]
    STATE::Custom_schemas_per_workflow_section
    TOOLS::Scoped_assignment_per_agent_role
    
  PSM::EXCELLENT[BECAUSE::"Explicit graph state + Command objects"]
    COMMANDS::Agent_returns_next_agent+state_updates
    DURABILITY::Persist_progress+time_travel_debug
    
  SOG::EXCELLENT[BECAUSE::"OutputParser + schema at every level"]
    SEPARATION::Content_generation _VERSUS_ formatting
    PYDANTIC::AtomicTaskList_model_enforcement
    
  EXT::EXCELLENT[BECAUSE::"Most extensible via modular design"]
    ECOSYSTEM::Huge_tool_library+custom_interfaces
    CONTROL::Insert_Python_anywhere_in_graph
    
  LLM::EXCELLENT[BECAUSE::"Connectors for every major provider"]
    UNIFIED::Each_agent_different_model_seamlessly
    UPDATES::Community_keeps_providers_current
    
  SUITABILITY::HIGHLY_SUITABLE[BECAUSE::"Ultimate control via explicit graphs"]
  TRADEOFF::More_coding_required_for_setup

---

FRAMEWORK_5:METAGPT:
  PHILOSOPHY::"Simulated software company with fixed AI roles"
  PATTERN::CEO->PM->Architect->Engineers->QA[SISYPHEAN]
  
  MAC::GOOD[BECAUSE::"Multi-agent but fixed pipeline"]
    LIMITATION::Scripted_sequence_not_dynamic
    FIT::Works_if_matching_their_workflow
    
  GAC::FAIR[BECAUSE::"Pre-defined roles with prompt editing"]
    CONSTRAINT::Can't_add_arbitrary_agents
    DATA::Text_based_not_structured_objects
    
  PSM::FAIR[BECAUSE::"Hardcoded planning for software dev"]
    LINEAR::No_feedback_loops_or_iterations
    STATE::Text_artifacts_not_formal_objects
    
  SOG::GOOD[BECAUSE::"Produces structured markdown docs"]
    CHALLENGE::Schema_via_prompts_only
    OUTPUT::Requirements_lists+design_docs
    
  EXT::POOR[BECAUSE::"Not designed as generic framework"]
    TOOLS::Minimal_integration_points
    MODELS::GPT-4_focused_not_pluggable
    
  LLM::FAIR[BECAUSE::"Built for OpenAI GPT-4 only"]
    EFFORT::Manual_modification_for_others
    
  SUITABILITY::MODERATE[BECAUSE::"Too rigid for HestAI needs"]
  VERDICT::Reference_not_solution

---

SYNTHESIS:FRAMEWORK_SELECTION:
  TOP_TIER::[CrewAI, Agno][HARMONIA]
  SECOND_TIER::[LangChain/Graph, AutoGen][REQUIRES::more_development]
  REFERENCE::[MetaGPT][PATTERN::inspiration_only]
  
  WINNER::CrewAI[EDGE::"Built-in planning + hierarchical coordination"]
  RUNNER_UP::Agno[STRENGTH::"Schema enforcement + 23+ providers"]
  
  RATIONALE::[
    "Both handle complex multi-agent orchestration",
    "Both enforce structured outputs reliably",
    "Both integrate required LLM providers",
    "CrewAI slightly leads on planning abstractions",
    "Agno excels at reasoning chains + performance"
  ]
  
  DEPLOYMENT::Either_framework->Docker->atomic-task-list.md

---

IMPLEMENTATION_GUIDANCE:
  CREWAI_APPROACH:
    SETUP::YAML_project_scaffold
    AGENTS::[LOGOS:planner, ETHOS:validator, OUTPUT:formatter]
    FLOW::hierarchical_with_manager
    SUCCESS::"Transparent multi-model planning"
    
  AGNO_APPROACH:
    SETUP::Team(mode="coordinate")
    AGENTS::json_mode_for_structured_plans
    TOOLS::AddToPlanTool+ValidatePlanTool
    SUCCESS::"High-performance validated outputs"

===END_FRAMEWORK_ANALYSIS===