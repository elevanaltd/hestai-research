#!/bin/bash
# Generate comprehensive file index for HestAI research

OUTPUT_FILE="FILE_INDEX.md"
TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")

# Function to count files in directory
count_files() {
    local dir=$1
    find "$dir" -name "*.md" -not -name "index.md" -not -name "README.md" 2>/dev/null | wc -l | tr -d ' '
}

# Generate the index
cat > "$OUTPUT_FILE" << EOF
# HestAI Research File Index
Generated: $TIMESTAMP

## Summary Statistics
EOF

# Count total research documents
TOTAL=$(find . -name "*.md" -not -path "./docs/*" -not -path "./node_modules/*" -not -name "README.md" -not -name "index.md" -not -name "CLAUDE.md" -not -name "*.oct.md" | wc -l | tr -d ' ')
echo "Total Research Documents: $TOTAL" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Generate category counts
echo "## Category Breakdown" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

for dir in empirical-studies cognitive-architecture cost-analysis pattern-learning architectural-studies user-research raph-framework odyssean-anchor database-architecture evidence unverified-claims claude-code; do
    if [ -d "$dir" ]; then
        count=$(count_files "$dir")
        echo "- **$dir/**: $count documents" >> "$OUTPUT_FILE"
    fi
done

echo "" >> "$OUTPUT_FILE"
echo "## Detailed File List" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Generate detailed file list by category
for dir in empirical-studies cognitive-architecture cost-analysis pattern-learning architectural-studies user-research raph-framework odyssean-anchor database-architecture evidence unverified-claims claude-code; do
    if [ -d "$dir" ]; then
        echo "### $dir/" >> "$OUTPUT_FILE"
        find "$dir" -name "*.md" -not -name "index.md" -not -name "README.md" | sort | while read -r file; do
            # Get file size and last modified date
            size=$(wc -c < "$file" | awk '{print int($1/1024) "KB"}')
            modified=$(date -r "$file" +"%Y-%m-%d" 2>/dev/null || echo "Unknown")
            echo "- \`$file\` ($size, modified: $modified)" >> "$OUTPUT_FILE"
        done
        echo "" >> "$OUTPUT_FILE"
    fi
done

# Add git status if available
if command -v git &> /dev/null && git rev-parse --git-dir > /dev/null 2>&1; then
    echo "## Git Information" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    echo "### Recently Modified Files (Last 10)" >> "$OUTPUT_FILE"
    git log --name-status --oneline -10 | grep "^[MAD]" | cut -f2 | grep "\.md$" | sort -u | head -10 | while read -r file; do
        echo "- \`$file\`" >> "$OUTPUT_FILE"
    done
    echo "" >> "$OUTPUT_FILE"
fi

echo "File index generated at: $OUTPUT_FILE"