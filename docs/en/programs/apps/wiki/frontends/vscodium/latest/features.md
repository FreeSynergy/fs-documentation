# VSCodium - Functions

## Overview

VSCodium is a full-featured source-code editor with extensive functions for
developers. The editor is extremely customisable and extendable through
extensions.

## Available editors

### 1. Code editor (standard)

#### Functions:
- **Syntax highlighting**: supports 100+ programming languages
- **Autocompletion**: IntelliSense (completion, parameter hints)
- **Code formatting**: automatic formatting (Prettier, ESLint, etc.)
- **Refactoring**: rename, extract method, etc.
- **Code navigation**: jump to definition, show references
- **Debugging**: built-in debugger (Chrome, Node.js, Python, etc.)
- **Git integration**: automatic detection, commit, push, pull
- **Multi-cursor**: several cursors at the same time
- **Fast editing**: snippets, tab completion
- **Preview**: live preview for Markdown, HTML, etc.

#### What the editor does NOT do:
- no WYSIWYG for HTML/CSS (only syntax highlighting)
- no visual layout editor for web pages
- no direct database administration (only through extensions)

---

## Syntax highlighting

VSCodium supports syntax highlighting for many languages:

### Supported languages (by default):
- JavaScript, TypeScript, JSX, TSX
- Python, Java, C#, C++, C, Go, Rust
- HTML, CSS, SCSS, LESS, SASS
- SQL, JSON, YAML, TOML, XML
- Bash, PowerShell, PHP, Ruby, Swift
- Kotlin, Scala, Dart, Lua, R
- Markdown, ReStructuredText
- Assembly, VHDL, Verilog
- and many more (100+ languages)

### Example:
```javascript
// JavaScript
function hello() {
  console.log("Hello World");
}
```

```python
// Python
def hello():
    print("Hello World")
```

```sql
// SQL
SELECT * FROM users WHERE active = true;
```

---

## IntelliSense (autocompletion)

### Functions:
- **Variable completion**: automatic completion
- **Function completion**: show parameter hints
- **Import suggestions**: automatic import suggestions
- **Type checking**: show type information
- **Snippet completion**: template completion

### Example:
Type `fun` → suggestion for `function`

---

## Snippets (code templates)

### Functions:
- **Predefined snippets**: for many languages
- **Custom snippets**: create your own templates
- **Tab completion**: run them with the tab key

### Example snippets:
- `fori`: `for (let i = 0; i < array.length; i++) { ... }`
- `forEach`: `array.forEach(item => { ... })`
- `if`: `if (condition) { ... }`
- `console`: `console.log()`
- `imp`: `import ... from ...`

---

## Git integration

### Functions:
- **Automatic detection**: detect the Git repository automatically
- **Status display**: mark file changes
- **Diff view**: show the changes in context
- **Commit**: commit the changes
- **Push/pull**: synchronise with the remote repository
- **Branches**: create/switch branches
- **Conflicts**: resolve conflicts visually

### Git commands:
- `Cmd/Ctrl+Shift+G`: open the Git panel
- `Cmd/Ctrl+Shift+J`: open the search window
- `Cmd/Ctrl+Shift+E`: open the explorer

---

## Debugging

### Functions:
- **Breakpoints**: set breakpoints on lines
- **Stack trace**: show the call stack
- **Variables**: show variable values
- **Watch expressions**: watch expressions
- **Stepping**: step into, over, out
- **Configuration**: `launch.json` for the debugging configuration

### Debugging support:
- Node.js
- Python
- C#
- C++
- Go
- PHP
- Ruby
- Java
- and many more (via extensions)

---

## Terminal

### Functions:
- **Built-in terminal**: bash, zsh, PowerShell, etc.
- **Several terminals**: split the terminal
- **Commands**: run any command
- **History**: command history
- **Filter**: filter commands

### Terminal commands:
- `` Cmd/Ctrl+`` ``: open/close the terminal
- `` Cmd/Ctrl+Shift+`` ``: new terminal

---

## Extensions (plugins)

### Functions:
- **Syntax highlighting**: for further languages
- **Linting**: code quality (ESLint, Pylint, etc.)
- **Debugging**: for further languages
- **Themes**: change the colour scheme
- **Snippets**: for specific frameworks
- **Git**: extended Git functions
- **Docker**: Docker integration
- **Database**: database administration
- **API**: API test client (REST, GraphQL)

### Popular extensions:
- **Prettier**: code formatting
- **ESLint**: JavaScript linting
- **Python**: Python support
- **GitLens**: extended Git information
- **Markdown Preview**: Markdown preview
- **Docker**: Docker integration
- **PostgreSQL**: PostgreSQL administration
- **REST Client**: testing APIs

---

## Customisation

### Settings:
- **User settings**: global settings
- **Workspace settings**: project-specific settings
- **Settings editor**: visual settings editor
- **settings.json**: JSON-based settings

### Example settings:
```json
{
  "editor.fontSize": 14,
  "editor.tabSize": 2,
  "editor.formatOnSave": true,
  "files.autoSave": "onFocusChange",
  "editor.defaultFormatter": "esbenp.prettier-vscode"
}
```

---

## Shortcuts

See [shortcuts.md](shortcuts.md) for a complete list of all keyboard shortcuts.

---

## Comparison with other editors

| Function | VSCodium | Notion | Tango.io | Confluence |
|----------|----------|--------|----------|------------|
| Source-code editor | ✅ yes | ❌ no | ❌ no | ❌ no |
| Syntax highlighting | ✅ yes (100+ languages) | ✅ yes (40+ languages) | ✅ yes (20+ languages) | ✅ yes (with an extension) |
| IntelliSense | ✅ yes | ❌ no | ❌ no | ❌ no |
| Git integration | ✅ yes | ❌ no | ❌ no | ❌ no |
| Debugging | ✅ yes | ❌ no | ❌ no | ❌ no |
| Extensions | ✅ yes | ❌ no | ❌ no | ✅ yes |
| Snippets | ✅ yes | ✅ yes | ❌ no | ❌ no |
| Terminal | ✅ yes | ❌ no | ❌ no | ❌ no |

---

## Recommendation

- **For developers**: VSCodium (a mature development environment)
- **For quick writing**: IntelliSense and snippets
- **For technical documentation**: code block with syntax highlighting
- **For Git users**: the integrated Git support
- **For debugging**: the built-in debugger with several languages

---

## VSCodium vs. VS Code

VSCodium is identical to VS Code, but:
- **open source**: completely free software
- **no telemetry**: no data sent to Microsoft
- **no MS EULA**: a different licence
- **the same extensions**: VS Code extensions are compatible
