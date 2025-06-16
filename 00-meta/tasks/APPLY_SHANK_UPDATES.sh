#!/bin/bash
# Script to apply SHANK updates for operational awareness
# Author: HERMES(Claude)
# Date: 2025-01-16

echo "🔄 SHANK Update Script for Operational Awareness"
echo "==============================================="

# Check if we're in the right directory
if [ ! -d "/Users/shaunbuswell/dev/hestai-system" ]; then
    echo "❌ Error: hestai-system directory not found"
    exit 1
fi

cd /Users/shaunbuswell/dev/hestai-system

# Check if updates exist
if [ ! -d "shank-updates" ]; then
    echo "❌ Error: shank-updates directory not found"
    exit 1
fi

# Unlock if needed
echo "🔓 Unlocking role-anchors..."
./scripts/hestai-lock unlock

# Create backup
echo "💾 Creating backup of original SHANK files..."
cp -r config/role-anchors config/role-anchors.backup-$(date +%Y%m%d-%H%M%S)

# Apply updates
echo "📝 Applying SHANK updates..."
cp shank-updates/HERMES_SHANK.oct.md config/role-anchors/
cp shank-updates/PATHOS_SHANK.oct.md config/role-anchors/
cp shank-updates/ETHOS_SHANK.oct.md config/role-anchors/
cp shank-updates/LOGOS_SHANK.oct.md config/role-anchors/

# Verify updates
echo "✅ Verifying updates..."
echo ""
echo "Files updated to use OPERATING_AS:"
grep -n "OPERATING_AS" config/role-anchors/*_SHANK.oct.md | head -10
echo ""
echo "Operational awareness confirmed in:"
grep -n "operational" config/role-anchors/*_SHANK.oct.md | head -10

# Re-lock
echo ""
echo "🔒 Re-locking role-anchors..."
./scripts/hestai-lock lock

echo ""
echo "✨ SHANK updates complete!"
echo "All roles now reflect operational awareness rather than identity claims."
echo ""
echo "Key changes:"
echo "- WHO_I_AM → OPERATING_AS"
echo "- TRUTH → OPERATIONAL_TRUTH"
echo "- Core identity → Core operational role"
echo ""
echo "This aligns with the actor-director model from cognitive architecture research."