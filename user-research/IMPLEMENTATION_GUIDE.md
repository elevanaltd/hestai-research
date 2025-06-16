# GitHub Integration Implementation Guide

This guide provides step-by-step instructions for working with the Thymos Framework GitHub repository.

## Current Setup

The Thymos Framework is connected to GitHub with the following configuration:

- **Repository URL**: https://github.com/elevanaltd/thymos-framework.git
- **Working Directory**: `/Users/shaunbuswell/dev/thymos/thymos-mvp/`
- **Current Branch**: octave-adoption (with other branches including main)

## Workflow Guide

### Initial Setup (Already Complete)

The repository has been set up with:
- Git initialization
- Remote connection to GitHub
- Git LFS configuration
- Essential files pushed to GitHub

### Daily Workflow

#### 1. Making Changes

Work directly in the thymos-mvp directory as normal:

```bash
# Navigate to working directory
cd /Users/shaunbuswell/dev/thymos/thymos-mvp

# Edit files using your preferred editor
# Example: Edit a core protocol file
nano core/P2-apollo-effective.md
```

#### 2. Checking Status

Regularly check which files have been modified:

```bash
# Check modified files
git status

# See specific changes in a file
git diff core/P2-apollo-effective.md
```

#### 3. Committing Changes

Save your changes to the repository:

```bash
# Stage specific files
git add core/P2-apollo-effective.md

# Or stage all changes
git add .

# Commit with a descriptive message
git commit -m "Update Apollo protocol with clearer pattern recognition examples"
```

#### 4. Syncing with GitHub

Push your changes to GitHub to share and back them up:

```bash
# Push changes to GitHub
git push origin main

# Get latest changes from GitHub (if collaborating)
git pull origin main
```

### Working with Git LFS

Large files are automatically handled by Git LFS based on the patterns in `.gitattributes`:

```bash
# Check which files are tracked by LFS
git lfs ls-files

# All standard git commands work normally
git add large-file.pdf
git commit -m "Add documentation PDF"
git push
```

### Project Development Workflow

When working on any project in the Thymos framework:

1. **Project Organization**:
   - Work within the appropriate project directory in `/projects/open/`
   - Follow the standard project structure for consistency
   - Use project-specific README.md files to document purpose and progress

2. **Development Process**:
   - Make incremental, logical changes
   - Test functionality before committing
   - Document changes thoroughly

3. **Git Workflow**:
   - Commit related changes together
   - Use descriptive commit messages that clearly explain the purpose
   - Follow the conventional commits format when possible

## Branching Strategy

For larger features or collaborative work:

```bash
# Create a feature branch
git checkout -b feature/new-capability

# Work on changes
# ...

# Commit changes
git add .
git commit -m "Implement new capability"

# Push to GitHub
git push -u origin feature/new-capability

# When ready, merge to main
git checkout main
git merge feature/new-capability
git push origin main
```

## Handling Large Files

Git LFS is configured to track several file types:

- PDFs and other documents
- Images and media files
- Large markdown files (>50KB)

When you add a file matching these patterns, it will automatically use LFS.

## Troubleshooting

### Push Issues

If you have trouble pushing:

```bash
# Make sure you have the latest changes
git pull --rebase origin main

# Then try pushing again
git push origin main
```

### LFS Issues

If LFS files aren't being tracked correctly:

```bash
# Check LFS status
git lfs status

# Ensure LFS is installed
git lfs install

# Fix tracking if needed
git lfs track "*.pdf"
git add .gitattributes
git commit -m "Update LFS tracking"
```

### Connection Issues

If you can't connect to GitHub:

```bash
# Verify remote connection
git remote -v

# Update connection if needed
git remote set-url origin https://github.com/elevanaltd/thymos-framework.git
```

## Best Practices

1. **Commit Frequently**: Make small, logical commits rather than large changes
2. **Descriptive Messages**: Write clear commit messages explaining why changes were made
3. **Pull Before Push**: Always get latest changes before pushing your own
4. **Respect Boundaries**: Follow the boundary management framework for file organization
5. **Document Changes**: Update documentation when making significant changes
6. **Link Styles**: 
   - For markdown files, use relative paths without a leading slash: `core/THE_HEART_OF_THYMOS.md` 
   - For scripts, use self-referential paths with `${THYMOS_ROOT}` variable
7. **Path Management**: Follow guidelines in `scripts/system/docs/PATH_MANAGEMENT.md`

---

**Guide Version**: 1.2  
**Last Updated**: April 17, 2025  
**Maintained By**: Hecate (Boundary Management)