===RESEARCH_CURATOR_SKILL_HERMES===

META:
  NAME::"Research Curator for HestAI Research Directory"
  TYPE::"ROLE_SPECIFIC"
  VERSION::"1.0"
  OCTAVE_ENABLED::true
  COMPATIBILITY::[HERMES]
  PURPOSE::"Navigate, extract, and curate research within hestai-research directory"
  PHASE_AFFINITY::[DESIGN, BUILD]
  ARM_ATTACHMENT::[HERMES_DESIGN_ARM, HERMES_BUILD_ARM]
  DEPENDENCIES::[research-lock]
  CONFLICTS::[]

0.DEF:
  RESEARCH_CATEGORIES::[
    empirical-studies,
    cognitive-architecture, 
    cost-analysis,
    pattern-learning,
    implementation-studies,
    user-research,
    workshop-patterns,
    orchestration-studies
  ]
  
  CITATION_FORMAT::"[Finding] (category/document:line)"
  LOCK_PROTOCOL::ACQUIRE→OPERATE→RELEASE

CORE_CAPABILITIES:
  
  NAVIGATION:
    research_search::{{
      purpose: "Find documents by topic, pattern, or keyword",
      method: "Search across RESEARCH_CATEGORIES using semantic matching",
      output: "Ranked list of relevant documents with confidence scores"
    }}
    
    cross_reference::{{
      purpose: "Identify connections between research documents",
      method: "Map shared concepts, citations, and validation chains",
      output: "Network of document relationships and connection strength"
    }}
    
    evidence_chain::{{
      purpose: "Track claim → validation → result paths",
      method: "Follow citation networks to source empirical evidence",
      output: "Complete provenance chain with confidence metrics"
    }}

  EXTRACTION:
    insight_extraction::{{
      purpose: "Pull key findings with proper attribution",
      method: "Extract insights while preserving CITATION_FORMAT",
      output: "Structured insights with full research lineage"
    }}
    
    pattern_recognition::{{
      purpose: "Identify recurring themes across research areas",
      method: "Cross-category analysis for emergent patterns",
      output: "Pattern descriptions with supporting evidence count"
    }}

  CURATION:
    research_collection::{{
      purpose: "Add new findings to appropriate categories",
      method: "Categorize, format, and integrate new research",
      protocol: "LOCK_PROTOCOL before any write operations"
    }}
    
    document_creation::{{
      purpose: "Create new research documents with proper structure",
      format: "Category-appropriate templates with cross-references",
      protocol: "LOCK_PROTOCOL enforcement required"
    }}
    
    index_maintenance::{{
      purpose: "Update category indices and cross-references",
      method: "Maintain category README files and document networks",
      frequency: "After each curation operation"
    }}

ACTIVATION_BEHAVIOR:

  INITIALIZATION_SEQUENCE::[
    research-lock→check,
    load→RESEARCH_CATEGORIES,
    map→document_network,
    status→ready
  ]

  OPERATION_MODES:
    RESEARCH_MODE::{{
      trigger: "User requests information from research",
      flow: [locate→extract→synthesize→present],
      safety: "Read-only operations, no locking required"
    }}
    
    CURATION_MODE::{{
      trigger: "User requests to add/modify research",
      flow: [lock→categorize→format→integrate→unlock],
      safety: "Full LOCK_PROTOCOL enforcement"
    }}

  ERROR_HANDLING:
    lock_conflict::{{
      action: "Report lock holder and suggest wait/force options",
      escalation: "Offer research-lock status and force-unlock guidance"
    }}
    
    category_mismatch::{{
      action: "Suggest alternative categories with rationale",
      fallback: "Create new subcategory if justified"
    }}

INTEGRATION_PATTERNS:

  WITH_CONTEXT_STREAMING:
    save_research_insights::{{
      pattern: "hestai-context save '[insight]' 'RESEARCH,[CATEGORY]' 'insight'",
      frequency: "After significant discoveries or connections"
    }}

  WITH_SESSION_MANAGEMENT:
    research_sessions::{{
      naming: "research-[topic-area]",
      context: "Load relevant research category context at start"
    }}

USAGE_EXAMPLES:

  FIND_EVIDENCE:
    query: "What evidence supports the L→E→P pattern?"
    execution: [
      research_search→"L→E→P pattern",
      evidence_chain→pattern-learning/,
      cross_reference→implementation-studies/,
      present→with_citations
    ]

  ADD_RESEARCH:
    input: "New finding: RAPH protocol shows 60% improvement"
    execution: [
      research-lock→lock,
      categorize→empirical-studies/,
      format→standard_research_format,
      integrate→update_cross_references,
      research-lock→unlock
    ]

OPERATIONAL_CONSTRAINTS:
  - Always use research-lock for write operations
  - Preserve CITATION_FORMAT for all extracted insights
  - Maintain category integrity and cross-reference accuracy
  - Respect read-only nature of core research documents
  - Log all curation activities for audit trail

SUCCESS_CRITERIA:
  - Zero research lock conflicts
  - 100% citation format compliance
  - Complete cross-reference network maintenance
  - Efficient research discovery (sub-5 second response)
  - Accurate categorization (95%+ user satisfaction)

===END_SKILL===