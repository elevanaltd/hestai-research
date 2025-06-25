# Claude Code Configuration Guide

Yes, Claude Code provides a comprehensive configuration system that allows you to tailor its behavior to your preferences and workflow. You can manage settings globally or per project using the `claude config` command or by editing configuration files directly.

⸻

## 🛠️ Configuration Options

Here are the key settings you can adjust:

### General Settings
- **theme**: Sets the UI theme.
  Options: `dark`, `light`, `dark-daltonized`, `light-daltonized`.
- **verbose**: Controls the verbosity of Claude's output.
  Options: `true`, `false`.
- **autoUpdaterStatus**: Enables or disables the auto-updater.
  Options: `enabled`, `disabled`.
- **preferredNotifChannel**: Determines how notifications are delivered.
  Options: `iterm2`, `iterm2_with_bell`, `terminal_bell`, `notifications_disabled`.

### Model and Prompt Settings
- **model**: Specifies the Claude model to use.
  Examples: `claude-3-7-sonnet-20250219`, `claude-3-5-sonnet`.
- **thinking**: Toggles the display of model thinking steps.
  Options: `true`, `false`.
- **maxHistorySize**: Sets the maximum number of conversation history entries.
  Value: Integer.
- **maxTokens**: Defines the maximum number of tokens per completion.
  Value: Integer.
- **temperature**: Adjusts the randomness of the model's output.
  Value: Float between 0 and 1.

### Permissions and Tools
- **toolPermissions**: Manages permissions for specific tools.
  Format:
  ```json
  {
    "toolPermissions": {
      "Bash": "allow",
      "Edit": "prompt",
      "Replace": "deny"
    }
  }
  ```

- **allowedTools**: Lists tools that are always allowed.
  Example: `["Bash (npm run lint)", "Edit"]`.
- **deny**: Lists tools that are always denied.
  Example: `["Bash (curl:*)"]`.

### Environment Variables
- **env**: Sets environment variables for Claude sessions.
  Example:
  ```json
  {
    "env": {
      "CLAUDE_CODE_ENABLE_TELEMETRY": "1",
      "OTEL_METRICS_EXPORTER": "otlp"
    }
  }
  ```

### Cleanup and History
- **cleanupPeriodDays**: Determines how long to retain chat transcripts locally.
  Default: 30 days.

### MCP Servers
- **mcpServers**: Configures Model Context Protocol (MCP) servers.
  Example:
  ```json
  {
    "mcpServers": {
      "filesystem": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-filesystem"]
      }
    }
  }
  ```

⸻

## 🗂️ Configuration Files

Claude Code uses a hierarchical configuration system:
- **Global Settings**: `~/.claude/settings.json` – Applies to all projects.
- **Project Settings**: `<project>/.claude/settings.json` – Shared across team members.
- **Local Project Settings**: `<project>/.claude/settings.local.json` – Personal preferences, not checked into version control.

Settings are applied in the following order of precedence:
1. Enterprise policies (if applicable).
2. Command-line arguments.
3. Local project settings.
4. Shared project settings.
5. User settings.

⸻

## 🔧 Managing Configurations

You can manage configurations using the `claude config` command:
- List all settings:
  ```bash
  claude config list
  ```

- Get a specific setting:
  ```bash
  claude config get <key>
  ```

- Set a setting:
  ```bash
  claude config set <key> <value>
  ```

- Set a global setting:
  ```bash
  claude config set --global <key> <value>
  ```

- Add to a list setting:
  ```bash
  claude config add <key> <value>
  ```

- Remove from a list setting:
  ```bash
  claude config remove <key> <value>
  ```

⸻

For more detailed information, refer to the official Claude Code settings documentation.

If you need assistance with specific configurations or setting up your environment, feel free to ask!