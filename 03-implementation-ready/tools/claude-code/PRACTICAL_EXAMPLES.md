# Claude Code Practical Examples & Patterns

This document provides concrete examples demonstrating Claude Code's capabilities and limitations through real-world scenarios.

## Basic File Operations

### Example 1: Creating a Project Structure
```bash
# What Claude Code CAN do:
User: "Create a React project structure with TypeScript"

Claude Code executes:
mkdir -p src/{components,hooks,utils,types}
touch src/App.tsx src/index.tsx
echo '{"compilerOptions": {...}}' > tsconfig.json

# What Claude Code CANNOT do:
User: "Keep track of which files we created for later"
# ❌ No persistent memory - must read filesystem
```

### Example 2: Refactoring Across Files
```bash
# CAN: Rename a function across multiple files
User: "Rename getUserData to fetchUserProfile everywhere"

Claude Code:
1. grep -r "getUserData" src/
2. Read each file
3. MultiEdit each file with replacements
4. Verify with grep again

# CANNOT: Maintain refactoring state
User: "Undo that last rename"
# ❌ No undo history - would need git
```

## Command Execution Patterns

### Example 3: Development Server Management
```bash
# CAN: Start servers and check status
User: "Start the dev server and check if it's running"

Claude Code:
npm run dev &  # Starts in background
sleep 3
curl http://localhost:3000 || echo "Server not responding"
ps aux | grep node

# CANNOT: Interact with running server
User: "Press Ctrl+C in the dev server"
# ❌ No interactive control
```

### Example 4: Database Operations
```bash
# CAN: Run database commands
User: "Create a new PostgreSQL database"

Claude Code:
psql -U postgres -c "CREATE DATABASE myapp;"
psql -U postgres -d myapp -f schema.sql

# CANNOT: Interactive psql session
User: "Open psql and explore the tables"
# ❌ No interactive CLI - must use -c flag
```

## Complex Workflows

### Example 5: Full Feature Implementation
```bash
# CAN: Implement complete features
User: "Add user authentication to the Express app"

Claude Code:
1. Reads existing app structure
2. Creates auth middleware
3. Implements JWT logic
4. Adds routes
5. Creates tests
6. Updates documentation

# Actual execution:
- Read package.json
- npm install jsonwebtoken bcrypt
- Create src/middleware/auth.js
- Create src/routes/auth.js
- Create tests/auth.test.js
- Update README.md

# CANNOT: Test the auth flow interactively
# Must write automated tests instead
```

### Example 6: Git Workflow
```bash
# CAN: Full git workflow
User: "Create a feature branch and PR for the auth changes"

Claude Code:
git checkout -b feature/user-auth
git add -A
git commit -m "Add user authentication

- Implement JWT-based auth
- Add login/register endpoints
- Include middleware for protected routes"
git push -u origin feature/user-auth
gh pr create --title "Add user authentication" --body "..."

# CANNOT: Resolve merge conflicts interactively
# Must detect and report conflicts for manual resolution
```

## Search and Analysis

### Example 7: Codebase Analysis
```bash
# CAN: Analyze patterns and dependencies
User: "Find all API endpoints in the codebase"

Claude Code:
grep -r "router\.(get|post|put|delete)" src/
grep -r "@GetMapping\|@PostMapping" src/  # For Spring
find . -name "*.py" -exec grep -l "app.route" {} \;

# Then reads relevant files and creates summary

# CANNOT: Keep running analysis updated
# Each request starts fresh analysis
```

### Example 8: Dependency Management
```bash
# CAN: Analyze and update dependencies
User: "Check for outdated npm packages"

Claude Code:
npm outdated
npm audit
cat package.json
# Reads and suggests updates

# CANNOT: Automatically decide which updates are safe
# Requires human judgment for breaking changes
```

## REPL-Like Interactions

### Example 9: Python Development
```bash
# ATTEMPTING REPL (What users often try):
User: "x = 42"
User: "print(x * 2)"
# ❌ FAILS - No persistent interpreter

# CORRECT PATTERN:
User: "Create a Python script that sets x=42 and prints x*2"

Claude Code:
cat > calc.py << 'EOF'
x = 42
print(x * 2)
EOF
python calc.py  # Output: 84
```

### Example 10: Incremental Development
```bash
# SIMULATING REPL with files:
User: "Let's build a data processor step by step"

# Step 1
echo "data = [1, 2, 3, 4, 5]" > processor.py
python processor.py

# Step 2  
echo "data = [1, 2, 3, 4, 5]
filtered = [x for x in data if x > 2]" > processor.py
python processor.py

# Each step rebuilds the entire script
```

## Integration Examples

### Example 11: CI/CD Setup
```bash
# CAN: Create complete CI/CD pipelines
User: "Set up GitHub Actions for testing and deployment"

Claude Code creates:
.github/workflows/ci.yml
.github/workflows/deploy.yml
Scripts for deployment
Environment configuration

# CANNOT: Access GitHub secrets or trigger workflows
# Must be configured in GitHub UI
```

### Example 12: Docker Development
```bash
# CAN: Docker configuration and commands
User: "Containerize this Node.js application"

Claude Code:
- Creates Dockerfile
- Creates docker-compose.yml
- Runs: docker build -t myapp .
- Runs: docker-compose up -d
- Checks: docker ps

# CANNOT: Debug inside running containers interactively
# Must use docker exec with specific commands
```

## Advanced Patterns

### Example 13: Code Generation with Context
```bash
# CAN: Generate contextually aware code
User: "Create a REST API client based on our backend routes"

Claude Code:
1. Analyzes backend route files
2. Extracts endpoint patterns
3. Generates TypeScript client with:
   - Proper types
   - Error handling
   - Authentication
   - Request/response interfaces

# CANNOT: Validate against live API
# Generates based on static analysis only
```

### Example 14: Performance Optimization
```bash
# CAN: Analyze and optimize code
User: "Optimize the database queries in our app"

Claude Code:
- Finds all database queries
- Identifies N+1 problems
- Suggests indexes
- Implements query builders
- Adds query logging

# CANNOT: Run real performance benchmarks
# Provides static analysis only
```

## Error Handling Examples

### Example 15: Debugging Scenarios
```bash
# CAN: Investigate errors
User: "Debug why the server crashes on startup"

Claude Code:
- Reads error logs
- Checks package.json
- Verifies dependencies
- Looks for syntax errors
- Suggests fixes

# CANNOT: Attach debugger or step through code
# Must rely on logs and static analysis
```

## MCP Extension Examples

### Example 16: GitHub Integration
```bash
# WITH GitHub MCP:
User: "Review PR #123 and suggest improvements"

Claude Code:
gh pr view 123
gh pr diff 123
# Analyzes changes
# Provides feedback
gh pr comment 123 --body "Suggestions: ..."

# WITHOUT MCP: Would need manual API calls
```

## Best Practice Patterns

### Pattern 1: Project Initialization
```bash
# Optimal approach for new projects:
1. Create structure
2. Initialize git
3. Set up base configs
4. Create CLAUDE.md with project context
5. Implement core features
6. Add tests incrementally
```

### Pattern 2: Debugging Workflow
```bash
# Effective debugging pattern:
1. Read error message
2. Locate relevant files
3. Search for error patterns
4. Read specific problem areas
5. Implement fix
6. Verify with tests
```

### Pattern 3: Refactoring Strategy
```bash
# Safe refactoring approach:
1. Search for all occurrences
2. Create backup branch
3. Make changes incrementally  
4. Run tests after each change
5. Commit working states
```

## Common Pitfalls and Solutions

### Pitfall 1: Assuming Memory
```bash
# ❌ Wrong:
"Remember that API key I mentioned?"

# ✓ Correct:
"Read the API key from .env file"
```

### Pitfall 2: Interactive Commands
```bash
# ❌ Wrong:
"Run npm init and answer the prompts"

# ✓ Correct:
"Create package.json with these settings: ..."
```

### Pitfall 3: Large File Operations
```bash
# ❌ Wrong:
"Read all log files and find errors"

# ✓ Correct:
"Use grep to find errors in log files, then read specific matches"
```

---
*These examples demonstrate real-world usage patterns and help set proper expectations for Claude Code capabilities.*