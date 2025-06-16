# Claude Code Commands Reference

## CLI Commands

| Command | Description | Example |
|---------|-------------|---------|
| `claude` | Start interactive REPL | `$ claude` |
| `claude "query"` | Start REPL with initial prompt | `$ claude "explain this project"` |
| `claude -p "query"` | Run one-off query, then exit | `$ claude -p "explain this function"` |
| `cat file \| claude -p "query"` | Process piped content | `$ cat logs.txt \| claude -p "explain"` |
| `claude config` | Configure settings | `$ claude config set --global theme dark` |
| `claude update` | Update to latest version | `$ claude update` |
| `claude mcp` | Configure Model Context Protocol servers | (Refer to MCP tutorials) |

## CLI Flags

- **`--print`**: Print response without interactive mode
- **`--verbose`**: Enable verbose logging
- **`--dangerously-skip-permissions`**: Skip permission prompts

## Slash Commands (within session)

| Command | Purpose |
|---------|---------|
| `/bug` | Report bugs to Anthropic |
| `/clear` | Clear conversation history |
| `/compact` | Compact conversation to save context space |
| `/config` | View/modify configuration |
| `/cost` | Show token usage statistics |
| `/doctor` | Check Claude Code installation health |
| `/help` | Get usage help |
| `/init` | Initialize project with CLAUDE.md guide |
| `/login` | Switch Anthropic accounts |
| `/logout` | Sign out from Anthropic account |
| `/pr_comments` | View pull request comments |
| `/review` | Request code review |
| `/terminal-setup` | Install Shift+Enter key binding |

## Key Tips

- Use `/config` to manage global and project-level settings
- Slash commands help control Claude's behavior within a session
- CLI commands provide flexible interaction methods
- The pipe operator (`|`) can be used to pass file contents directly to Claude
- Use `--print` flag for scripting and automation workflows

## Common Usage Patterns

### Quick One-Off Questions
```bash
claude -p "What does this function do?" < function.js
```

### Start Session with Context
```bash
claude "I need help refactoring the authentication module"
```

### Pipe Log Analysis
```bash
tail -n 100 app.log | claude -p "Find any errors or warnings"
```

### Update Configuration
```bash
claude config set --global model claude-3-5-sonnet
claude config set temperature 0.7
```

### Check Token Usage
Within a Claude session:
```
/cost
```

### Initialize Project Documentation
Within a Claude session:
```
/init
```

---
*Source: https://ib.bsb.br/claude-code/*