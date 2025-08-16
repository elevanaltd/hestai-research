===DUPLICATE_DETECTION_PATTERN===

META:
  NAME::"Research Duplicate Detection Protocol"
  TYPE::"CURATION_PATTERN"
  VERSION::"1.0"
  PURPOSE::"Systematic detection of content duplicates during research curation"
  USAGE::"Apply when processing new research documents or conducting corpus audits"

DETECTION_METHODS:

  CONTENT_FINGERPRINTING:
    key_phrases::{{
      method: "Search for unique findings, quotes, empirical data, dates"
      commands: [
        "grep -r 'unique_finding_phrase' /research/",
        "find . -name '*.md' -exec grep -l 'specific_quote' {} \\;"
      ]
    }}
    
    structural_patterns::{{
      method: "Compare document structure, methodology, conclusions"
      indicators: ["Same section headers", "Identical methodology", "Same data tables"]
    }}

  FILENAME_ANALYSIS:
    pattern_matching::{{
      similar_names: "role-loading-* vs *-role-loading vs loading-role-*"
      date_variants: "2025-07-24 vs 2025-07-24T* vs july-24-2025"
      version_indicators: "v1, v2, -updated, -final, -revised"
    }}

  CROSS_REFERENCE_ANALYSIS:
    citation_overlap::{{
      method: "Documents citing identical sources with same page numbers"
      threshold: "80%+ citation overlap indicates potential duplicate"
    }}
    
    evidence_reuse::{{
      method: "Same empirical data, same performance metrics, same test results"
      red_flags: ["Identical statistical findings", "Same experimental setup", "Same participant quotes"]
    }}

LEGITIMATE_DUPLICATION_EXCEPTIONS:

  ARCHIVAL_PRESERVATION:
    system_evolution::{{
      pattern: "Documents in both complete-timeline/ and era-specific directories"
      validation: "Check README.md for explicit archival policy"
      action: "No action - intentional historical preservation"
    }}
    
    version_archives::{{
      pattern: "Active documents with _archive/ versions"
      validation: "Newer versions should reference archived predecessors"
      action: "Verify archive directory structure is intentional"
    }}

  LEGITIMATE_REPUBLICATION:
    cross_category::{{
      pattern: "Same content in different research categories"
      validation: "Different research purposes (empirical vs theoretical vs implementation)"
      action: "Verify categorization rationale in document headers"
    }}

RESOLUTION_PROTOCOL:

  WHEN_DUPLICATES_FOUND:
    assessment::{{
      step_1: "Compare creation dates and authorship"
      step_2: "Assess content evolution (is one clearly more complete?)"
      step_3: "Check cross-references (which is cited by other research?)"
      step_4: "Verify intentionality via README or documentation"
    }}
    
    resolution_decision::{{
      consolidate: "Merge content, preserve best elements, redirect citations"
      archive: "Move older version to _archive/ with reference pointer"
      separate: "Keep both if serving different research purposes"
      delete: "Remove if truly redundant and uncited"
    }}

  DOCUMENTATION_REQUIREMENTS:
    changes_log::{{
      record: "Document all duplicate resolution actions"
      location: "00-meta/inbox/PROCESSING_LOG.md"
      format: "Date, Action, Files involved, Rationale"
    }}
    
    index_updates::{{
      master_index: "Update document counts and cross-references"
      category_indices: "Update relevant category README files"
      citation_repair: "Fix broken cross-references after consolidation"
    }}

AUTOMATION_OPPORTUNITIES:

  BATCH_DETECTION:
    file_hashing::{{
      command: "find . -name '*.md' -exec md5sum {} \\; | sort | uniq -d -w32"
      purpose: "Identify byte-for-byte identical files"
    }}
    
    content_similarity::{{
      approach: "Compare first/last paragraphs and key findings sections"
      threshold: "90%+ similarity warrants manual review"
    }}

  MONITORING_INTEGRATION:
    new_document_check::{{
      trigger: "Every time document moves from inbox to research categories"
      automated: "Run filename and key phrase searches"
      manual_review: "Flag potential matches for curator review"
    }}

SUCCESS_CRITERIA:
  - Zero unintentional content duplication
  - Preserved archival structures remain intact
  - All duplicate resolution actions documented
  - Master index maintains accurate document counts
  - Research integrity maintained through proper consolidation

VALIDATION_KEY::"CONSOLIDATION"

===END_PATTERN===