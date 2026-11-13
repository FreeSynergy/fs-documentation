# Notion - Features

> **Status 2026-11-13:** This page is an earlier draft; parts are unverified (for example Mermaid, HTML-free claims, "Markdown not supported in the editor" — the official help says Markdown shortcuts convert while typing [S11][S30]). The verified feature list is in the [2026-11-07 snapshot](../2026-11-07/features.md). The user workflows built from official pages are in [workflows.md](workflows.md); states, dialogs, tests and gaps are in [states.md](states.md), [dialogs.md](dialogs.md), [acceptance.md](acceptance.md), [gaps.md](gaps.md).

## Overview

Notion uses a **block-based visual editor** built on modern web standards. The editor is extremely user-friendly and offers great flexibility in designing content.

## Available Editors

### 1. Visual Editor (WYSIWYG)

#### Features:
- **Formatting**: Headings (H1-H6), bold, italic, underline, strikethrough
- **Lists**: Numbered lists, bulleted lists, to-do lists (checkboxes)
- **Tables**: Create/edit tables (add/delete columns/rows)
- **Media**: Insert images and files (drag & drop)
- **Links**: Add external and internal links
- **Alignment**: Text alignment (left, center, right, justified)
- **Callouts/boxes**: Info, warning, success callouts
- **Code blocks**: Syntax highlighting for many programming languages
- **Math formulas**: LaTeX support (`$...$` or `$$...$$`)
- **Diagrams**: Mermaid diagrams (with extension)
- **Embeds**: YouTube, Twitter, GitHub, Google Maps, etc.
- **Databases**: Database blocks with tables, Kanban boards, calendars
- **Preview links**: Pasting a URL automatically creates a bookmark card

#### What the editor CANNOT do:
- No direct HTML editing
- No Markdown syntax in the editor (converted automatically)
- No complex table formulas
- No vertical text alignment
- No manual line breaks between all sentences

---

## Block-Based Architecture

Notion uses a **block editor**, where every line of text, list, table, etc. is its own "block".

### Typical blocks:
1. **Text block**: Normal text with formatting
2. **Heading**: H1-H6 with automatic outline
3. **To-do list**: `-[ ] Task` for tasks
4. **Bulleted list**: `* Item` for lists
5. **Numbered list**: `1. Item` for numbered lists
6. **Quote**: `> Text` for quotes
7. **Callout**: Highlighted note (info, warning, etc.)
8. **Code block**: ``` for code with syntax highlighting
9. **Table**: Table block for data
10. **Image**: Image block with options (size, alignment)
11. **Embed**: Embed block for external content
12. **Database**: Database block (table, Kanban, calendar)
13. **Toggle**: Collapsible block
14. **Bookmark**: Link card
15. **PDF/File**: File embed

### Navigation in the block editor:
- `Enter`: Create new line/block
- `Tab`: Indent (lists, block level)
- `Shift+Tab`: Outdent (lists, block level)
- `Escape`: Leave focused block
- `Cmd/Ctrl+Enter`: Tick checkbox
- `Cmd/Ctrl+M`: Open menu

---

## Code Block Support

Notion supports syntax highlighting for many languages:

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

```go
// Go
package main

import "fmt"

func main() {
    fmt.Println("Hello World")
}
```

Supported languages:
- JavaScript, TypeScript, JSX, TSX
- Python, Java, C#, C++, C, Go, Rust
- HTML, CSS, SCSS, LESS
- SQL, JSON, YAML, YAML, TOML
- Bash, PowerShell, PHP, Ruby, Swift
- Kotlin, Scala, Dart, Lua, R
- MATLAB, Fortran, COBOL, VHDL
- Markdown, ReStructuredText
- Assembly, Verilog, SystemVerilog

---

## Table Features

Notion tables are particularly flexible:

### Features:
- **Columns/rows**: Add and delete
- **Formatting**: Text, numbers, checkboxes, date fields, selects, multi-selects
- **Formulas**: `prop("Column")` for calculations
- **Relations**: Links to other databases
- **Rollup**: Aggregations (SUM, COUNT, AVERAGE, etc.)
- **Filtering**: Filter columns (in the database)
- **Sorting**: Sort columns
- **Views**: Edit views (table, Kanban, calendar, list)

### Database types:
- **Table**: Classic table view
- **Calendar**: Data in calendar view
- **List**: List view with preview images
- **Kanban**: Cards in columns
- **Gallery**: Image gallery

---

## Callout Blocks (Notes)

### Function:
Highlighted notes with an icon and text.

### Syntax:
`/callout` → select type (Info, Warning, Success, Question, etc.)

### Example:
> ℹ️ **Information**: This is an info box

---

## Databases

### Features:
- **Column types**:
  - Text & Description
  - Number (formulas possible)
  - Select (single choice)
  - Multi-select (multiple choices)
  - Date (date with time)
  - Checkbox (true/false)
  - People (link members)
  - Files & Media (link files)
  - URL, Email, Phone
  - Relation (to other databases)
  - Formula (calculations)
  - Rollup (aggregations)

- **Views**:
  - Table view
  - Kanban view
  - Calendar view
  - List view
  - Gallery view

---

## Formulas

### Syntax:
`prop("Column name")` for column references

### Examples:
```
prop("Price") * prop("Quantity")
dateBetween(prop("End"), prop("Start"), "days")
concat(prop("First name"), " ", prop("Last name"))
```

### Functions:
- `concat()`: Join text
- `dateBetween()`: Difference between dates
- `format()`: Format
- `if()`: Condition
- `dateAdd()`: Add to date
- `prop()`: Get column value

---

## Embed Support

Notion supports embeds from many services:

- **Video**: YouTube, Vimeo, Loom, Streamable
- **Audio**: Spotify, SoundCloud
- **Code**: GitHub Gist, CodePen, JSFiddle, Replit
- **Design**: Figma, Sketch, Adobe XD
- **Social**: Twitter, LinkedIn, Instagram, TikTok
- **Documents**: Google Docs, Notion, Slides
- **Maps**: Google Maps, OpenStreetMap
- **Other**: PDF, web pages (via bookmark)

---

## Template System

### Features:
- **Template selection**: Choose templates when creating
- **Custom templates**: Create your own templates
- **Template categories**: Organization by type
- **Template sharing**: Share templates with the team

### Example templates:
- Meeting notes
- Project planning
- Product release notes
- Team onboarding
- Bug report
- Content calendar
- Personal database
- Budget planning

---

## Shortcuts

See [shortcuts.md](shortcuts.md) for a complete list of keyboard shortcuts.

---

## Comparison with Other Editors

| Feature | Notion | Tango.io | Confluence | XWiki |
|---------|--------|----------|------------|-------|
| Block-based | ✅ Yes | ✅ Yes | ❌ No | ❌ No |
| Code highlighting | ✅ Yes (40+ languages) | ✅ Yes (20+ languages) | ❌ No | ✅ Yes |
| Databases | ✅ Yes | ❌ No | ❌ No | ✅ Yes |
| Templates | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |
| Formulas | ✅ Yes | ❌ No | ❌ No | ✅ Yes |
| Embeds | ✅ Yes (100+ services) | ✅ Yes (100+ services) | ✅ Yes | ✅ Yes |
| Markdown | ❌ No | ❌ No | ❌ No | ✅ Yes |
| Visual feedback | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Yes |

---

## Recommendation

- **For team collaboration**: Notion (excellent databases and block structure)
- **For fast writing**: Block-based navigation
- **For technical documentation**: Code block with syntax highlighting
- **For data-driven projects**: Databases with relations and formulas
- **For visual organization**: Embeds, images, and flexible layouts
