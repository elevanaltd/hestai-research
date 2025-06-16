===RESEARCH_PATTERNS_MAP===
// Relationships between research patterns
// Individual patterns remain in .md for accessibility

0.DEF:
  PATTERN::"Reusable research methodology"
  DEPENDENCY::"Pattern that must be understood first"
  ENABLES::"Pattern that becomes possible after"

PATTERN_RELATIONSHIPS:
  CITATION_FORMAT:
    PURPOSE::"Consistent references across corpus"
    DEPENDENCY::[]  // Foundation pattern
    ENABLES::[CROSS_REFERENCE, EVIDENCE_CHAIN]
    RELATIONSHIP::"Citations are atoms; cross-refs are molecules"
    
  CROSS_REFERENCE:
    PURPOSE::"Validate reference integrity"
    DEPENDENCY::[CITATION_FORMAT]
    ENABLES::[EVIDENCE_CHAIN]
    RELATIONSHIP::"Can't validate refs without consistent format"
    
  EVIDENCE_CHAIN:
    PURPOSE::"Track claim evolution"
    DEPENDENCY::[CITATION_FORMAT, CROSS_REFERENCE]
    ENABLES::[RESEARCH_SYNTHESIS]
    RELATIONSHIP::"Chains require valid cross-references"
    
  PREVENTION_CHECKLIST:
    PURPOSE::"Active mistake prevention"
    DEPENDENCY::[]  // Standalone
    ENABLES::[CONTINUOUS_IMPROVEMENT]
    RELATIONSHIP::"Transforms lessons into rules"

USAGE_FLOWS:
  BASIC_RESEARCH::[
    CITATION_FORMAT→CROSS_REFERENCE
  ]
  
  VALIDATION_WORK::[
    CITATION_FORMAT→CROSS_REFERENCE→EVIDENCE_CHAIN
  ]
  
  QUALITY_CONTROL::[
    PREVENTION_CHECKLIST→ALL_PATTERNS
  ]

PATTERN_SYNERGIES:
  CITATION+CROSS_REF::"Ensures navigable research"
  CROSS_REF+EVIDENCE::"Validates claim lineage"
  ALL+PREVENTION::"Reduces repeated mistakes"

===END_RESEARCH_PATTERNS_MAP===