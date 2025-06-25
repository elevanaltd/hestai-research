#!/usr/bin/env python3
"""
raph_prompt_generator.py - RAPH Sequential Processing Prompt Generator

This script generates structured prompts for sequential RAPH processing
(READ-ABSORB-PERCEIVE-HARMONIZE) for use with any LLM (Claude, GPT, etc.)

It creates prompts that:
- Align with the symbolic fidelity of RAPH framework
- Produce compressible, referenceable outputs
- Embed clear cognitive role focus into each stage
- Respect token budget by design
- Support OCTAVE format for machine-to-machine efficiency

Usage:
  python3 raph_prompt_generator.py generate READ document_name
  python3 raph_prompt_generator.py generate ABSORB document_name --read-output=path/to/read_output.txt
  python3 raph_prompt_generator.py generate PERCEIVE document_name --read-output=path --absorb-output=path
  python3 raph_prompt_generator.py generate HARMONIZE document_name --read-output=path --absorb-output=path --perceive-output=path
"""

import os
import sys
import argparse
from pathlib import Path

# Configuration
OCTAVE_FORMAT = True  # Set to True to use OCTAVE formatting
COMPRESSION_MODE = True  # Set to True to enforce compression directives

def generate_raph_prompt(doc_name, stage="READ", read_output=None, absorb_output=None, perceive_output=None, octave_format=OCTAVE_FORMAT, compression=COMPRESSION_MODE):
    """Generate a structured prompt for the specified RAPH stage."""
    
    octave_primer = """
# OCTAVE Format Reference
────────────────────────────────────────────────────────
MODULE  (ver X.X.X • WT:1.00 • TS:YYYY-MM-DDThh:mm:ssZ)
────────────────────────────────────────────────────────

0.DEF
PTN:NAME="Pattern definition"  PTN:NEXT="Another pattern"
SYM:→progression  SYM:φdivine  SYM:✓verification  SYM:≠not_equal

1.SECTION  purpose→outcome
ELEMENT="value"  NEXT="another value"  #comments
ARRAY=[item1,item2,item3]  #ordered list
MATRIX=[x→y,a→b]  #mapping

2.REL
element1→element2→outcome  #relationship chain
source(context)→destination(context)→effect(quality)

3.PHI
1."Philosophical principle one."
2."Philosophical principle two."

4.VAL✓
section1✓ section2✓ section3✓

FORMAT REQUIREMENTS:
- Section names are numbered with a period (1.SECTION)
- Patterns use PTN: prefix and quotes around values
- Relationships use arrows (→) to show progression
- Comments use # and appear at the end of lines
- Every pattern and relationship must be defined
"""

    # Common prefix for all stages
    common_prefix = f"""# RAPH {stage} — Document: {doc_name}
"""

    if octave_format:
        common_prefix += f"""# OCTAVE MODE ENABLED
{octave_primer if stage == "READ" else "# Using OCTAVE format for structured output"}
"""

    if stage == "READ":
        prompt = f"""{common_prefix}
## Task
Extract foundational insights from {doc_name} that will empower the ABSORB phase. Focus on **supporting relationship identification**, not summary or structure.

## Focus
- Identify hidden structures not revealed by formatting
- Extract key non-obvious terminology with functional meaning
- Note elements likely to connect across sections/domains
- Highlight implicit frameworks or logics
- Avoid repeating obvious section names or lists

## Output Format
{f"- Use OCTAVE format with PTN:, REL:, and PHI: sections" if octave_format else "- Use brief bullet notes (aim for 30% of original doc length)"}
- Include section headers or markers where relevant
- No narrative. Use compressed, symbolic, referenceable notation.

## Style
- Precise. Compressed. Token-aware.
- Only include what helps understand **relationships** in ABSORB.
{f"- Target maximum 300 tokens output." if compression else ""}

[Your output starts below]

---
"""
    
    elif stage == "ABSORB":
        if not read_output:
            raise ValueError("ABSORB stage requires prior READ output.")

        prompt = f"""{common_prefix}
## Prior Context
The following is the READ output this analysis must build upon:

<<<READ_OUTPUT>>>
{read_output}
<<<END>>>

## Task
Create a relationship-focused analysis of {doc_name} using the prior READ output. Focus exclusively on identifying **connections** between elements.

## Output Requirements
{f'''
0.DEF
PTN: Define key patterns you'll reference
REL: Create relationship chains
DOM: Map domain connections
INT: Note harmonic intervals
''' if octave_format else '''
- REL: chains (e.g. REL:A(triggers)→B(expands)→C(constrains))
- DOM: domain mappings (e.g. DOM:SECTION_A→SECTION_B(causal))
- PTN: recurring patterns (define as needed)
- INT: harmonic relations (use musical interval metaphor)
'''}
- DO NOT restate the document content

## Format
{f"Use strict OCTAVE format with numbered sections" if octave_format else "Use clear relationship notation with symbolic compression"}

## Compression Policy
- Maximize token efficiency.
- All statements should use symbolic notation.
- Only include connections that emerge **from prior READ output**.
{f"- Target maximum 300 tokens output." if compression else ""}

[Your output starts below]

---
"""

    elif stage == "PERCEIVE":
        if not read_output or not absorb_output:
            raise ValueError("PERCEIVE stage requires both READ and ABSORB outputs.")

        prompt = f"""{common_prefix}
## Prior Context
The following are the READ and ABSORB outputs this analysis must build upon:

<<<READ_OUTPUT>>>
{read_output}
<<<END>>>

<<<ABSORB_OUTPUT>>>
{absorb_output}
<<<END>>>

## Task
Identify broader patterns and meta-frameworks in {doc_name} based on the READ facts and ABSORB relationships.

## Output Requirements
{f'''
0.DEF
PTN: Define meta-patterns
FRAME: Identify conceptual frameworks
META: Note cross-domain principles
ALIGN: Map to established systems
''' if octave_format else '''
- META: meta-patterns across relationships
- FRAME: broader conceptual frameworks
- ALIGN: connections to established models
- IMPL: implementation implications
'''}
- Focus on emergent properties from relationships
- Do NOT introduce concepts absent from READ/ABSORB

## Format
{f"Use strict OCTAVE format with numbered sections" if octave_format else "Use clear meta-pattern notation with framework references"}

## Compression Policy
- Focus on higher-order patterns only
- Reference READ/ABSORB symbolic notation for efficiency
- Each pattern should connect multiple relationships
{f"- Target maximum 400 tokens output." if compression else ""}

[Your output starts below]

---
"""

    elif stage == "HARMONIZE":
        if not read_output or not absorb_output or not perceive_output:
            raise ValueError("HARMONIZE stage requires READ, ABSORB, and PERCEIVE outputs.")

        prompt = f"""{common_prefix}
## Prior Context
The following are the READ, ABSORB, and PERCEIVE outputs this analysis must build upon:

<<<READ_OUTPUT>>>
{read_output}
<<<END>>>

<<<ABSORB_OUTPUT>>>
{absorb_output}
<<<END>>>

<<<PERCEIVE_OUTPUT>>>
{perceive_output}
<<<END>>>

## Task
Create cross-domain insights by integrating patterns across fields of knowledge, building on all previous RAPH stages.

## Output Requirements
{f'''
0.DEF
HARM: Define harmonic integrations
TRANS: Identify transformative principles
NOVEL: Create novel insights
APP: Suggest application domains
''' if octave_format else '''
- HARM: harmonic integrations across domains
- TRANS: transformative principles
- NOVEL: novel insights from integration
- APP: application domains for insights
'''}
- Each insight must connect multiple patterns
- Focus on emergent understanding impossible at earlier stages
- Create bridges between distinct knowledge domains

## Format
{f"Use strict OCTAVE format with numbered sections" if octave_format else "Use clear integration notation with cross-domain references"}

## Compression Policy
- Focus on highest-order integrations only
- Reference patterns by their symbolic names from PERCEIVE
- Each integration should connect multiple domains
{f"- Target maximum 600 tokens output." if compression else ""}

[Your output starts below]

---
"""
    else:
        raise ValueError(f"Invalid stage: {stage}. Use 'READ', 'ABSORB', 'PERCEIVE', or 'HARMONIZE'.")

    return prompt

def load_output_file(file_path):
    """Load output from a file if it exists."""
    path = Path(file_path)
    if not path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    try:
        with open(path, 'r') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        sys.exit(1)

def write_prompt_to_file(prompt, output_path):
    """Write the generated prompt to a file."""
    try:
        with open(output_path, 'w') as f:
            f.write(prompt)
        print(f"Prompt written to: {output_path}")
    except Exception as e:
        print(f"Error writing to file {output_path}: {e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description='Generate RAPH prompts for sequential processing.')
    subparsers = parser.add_subparsers(dest='command', help='Command to run')
    
    # Generate command
    gen_parser = subparsers.add_parser('generate', help='Generate a prompt for a RAPH stage')
    gen_parser.add_argument('stage', choices=['READ', 'ABSORB', 'PERCEIVE', 'HARMONIZE'], 
                            help='The RAPH stage to generate a prompt for')
    gen_parser.add_argument('document', help='Name or path of the document being processed')
    gen_parser.add_argument('--read-output', help='Path to READ stage output (required for ABSORB+)')
    gen_parser.add_argument('--absorb-output', help='Path to ABSORB stage output (required for PERCEIVE+)')
    gen_parser.add_argument('--perceive-output', help='Path to PERCEIVE stage output (required for HARMONIZE)')
    gen_parser.add_argument('--no-octave', action='store_true', help='Disable OCTAVE formatting')
    gen_parser.add_argument('--no-compression', action='store_true', help='Disable compression directives')
    gen_parser.add_argument('--output', '-o', help='Output file path (defaults to stage_prompt.txt)')
    
    # Process command
    process_parser = subparsers.add_parser('process', help='Execute a full RAPH processing chain')
    process_parser.add_argument('document', help='Path to the document to process')
    process_parser.add_argument('--model', default='claude-3-sonnet-20240229', 
                               help='Model to use (if API available)')
    process_parser.add_argument('--api-key', help='API key for the LLM service')
    process_parser.add_argument('--output-dir', help='Directory for output files')
    
    args = parser.parse_args()
    
    if args.command == 'generate':
        read_output = None
        absorb_output = None
        perceive_output = None
        
        # Load previous stage outputs if needed
        if args.stage in ['ABSORB', 'PERCEIVE', 'HARMONIZE'] and args.read_output:
            read_output = load_output_file(args.read_output)
            
        if args.stage in ['PERCEIVE', 'HARMONIZE'] and args.absorb_output:
            absorb_output = load_output_file(args.absorb_output)
            
        if args.stage == 'HARMONIZE' and args.perceive_output:
            perceive_output = load_output_file(args.perceive_output)
        
        # Generate the prompt
        prompt = generate_raph_prompt(
            args.document, 
            args.stage,
            read_output,
            absorb_output,
            perceive_output,
            not args.no_octave,
            not args.no_compression
        )
        
        # Determine output destination
        if args.output:
            output_path = args.output
        else:
            output_path = f"{args.stage.lower()}_prompt.txt"
        
        # Output the prompt
        if output_path == '-':
            print(prompt)
        else:
            write_prompt_to_file(prompt, output_path)
    
    elif args.command == 'process':
        print("Full process chain not implemented yet. Please use 'generate' for each stage separately.")
        # Future implementation would handle the full chain with API calls if available
    
    else:
        parser.print_help()

if __name__ == "__main__":
    main()