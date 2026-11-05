# Notion - Functions

## Overview

Notion uses a **block-based visual editor** built on modern web standards. The
editor is extremely user-friendly and allows a high degree of flexibility when
designing content.

## Available editors

### 1. Visual editor (WYSIWYG)

#### Functions:
- **Formatting**: headings (H1-H6), bold, italic, underline, strikethrough
- **Lists**: numbered lists, bullet lists, task lists (checkboxes)
- **Tables**: create/edit tables (add/remove columns and rows)
- **Media**: insert images and files (drag & drop)
- **Links**: add external and internal links
- **Alignment**: text alignment (left, centre, right, justified)
- **Notes/boxes**: info, warning and success notices (callouts)
- **Code blocks**: syntax highlighting for many programming languages
- **Math formulas**: LaTeX support (`$...$` or `$$...$$`)
- **Diagrams**: Mermaid diagrams (with an extension)
- **Embeds**: YouTube, Twitter, GitHub, Google Maps, etc.
- **Databases**: database blocks with tables, kanban boards, calendars
- **Preview links**: inserting a URL automatically creates a card

#### What the editor does NOT do:
- no direct HTML editing
- no Markdown syntax in the editor (it is converted automatically)
- no complex table formulas
- no vertical text alignment
- no text wrapping with a manual line break between all sentences

---

## Block-based architecture

Notion uses a **block editor** in which every text line, list, table and so on
is its own "block".

### Typical blocks:
1. **Text block**: normal text with formatting
2. **Heading**: H1-H6 with automatic outlining
3. **To-do list**: `-[ ] Task` for tasks
4. **Bullet list**: `* item` for lists
5. **Numbered list**: `1. item` for numbered lists
6. **Quote**: `> text` for quotes
7. **Callout**: highlighted notice (info, warning, etc.)
8. **Code block**: ``` for code with syntax highlighting
9. **Table**: table block for data
10. **Image**: image block with options (size, alignment)
11. **Embed**: embed block for external content
12. **Database**: database block (table, kanban, calendar)
13. **Toggle**: expandable block
14. **Bookmark**: link card
15. **PDF/file**: file embed

### Navigation in the block editor:
- `Enter`: create a new line/block
- `Tab`: indent (lists, block level)
- `Shift+Tab`: outdent (lists, block level)
- `Escape`: leave the block focus
- `Cmd/Ctrl+Enter`: tick the checkbox
- `Cmd/Ctrl+M`: open the menu

---

## Code block support

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

## Table features

Notion tables are particularly flexible:

### Functions:
- **Columns/rows**: add and delete
- **Formatting**: text, numbers, checkboxes, date fields, selects, multi-selects
- **Formulas**: `prop("Column")` for calculations
- **Relations**: links to other databases
- **Rollup**: aggregations (SUM, COUNT, AVERAGE, etc.)
- **Filtering**: filter columns (in the database)
- **Sorting**: sort columns
- **Views**: edit views (table, kanban, calendar, list)

### Database types:
- **Table**: classic table view
- **Calendar**: data in a calendar view
- **List**: list view with preview images
- **Kanban**: cards in columns
- **Gallery**: image gallery

---

## Callout blocks (notes)

### Function:
Highlighted notes with an icon and text.

### Syntax:
`/callout` → choose the type (info, warning, success, question, etc.)

### Example:
> ℹ️ **Information**: this is an info box

---

## Databases

### Functions:
- **Column types**:
  - text & description
  - number (formulas possible)
  - select (a single choice)
  - multi-select (several choices)
  - date (date with time)
  - checkbox (true/false)
  - people (link members)
  - files & media (link files)
  - URL, email, phone
  - relation (to other databases)
  - formula (calculations)
  - rollup (aggregations)

- **Views**:
  - table view
  - kanban view
  - calendar view
  - list view
  - gallery view

---

## Formulas

### Syntax:
`prop("Column name")` for a column reference

### Examples:
```
prop("Price") * prop("Quantity")
dateBetween(prop("End"), prop("Start"), "days")
concat(prop("FirstName"), " ", prop("LastName"))
```

### Functions:
- `concat()`: join text
- `dateBetween()`: difference between dates
- `format()`: formatting
- `if()`: condition
- `dateAdd()`: add to a date
- `prop()`: fetch a column value

---

## Embed support

Notion supports embeds from many services:

- **Video**: YouTube, Vimeo, Loom, Streamable
- **Audio**: Spotify, SoundCloud
- **Code**: GitHub Gist, CodePen, JSFiddle, Replit
- **Design**: Figma, Sketch, Adobe XD
- **Social**: Twitter, LinkedIn, Instagram, TikTok
- **Documents**: Google Docs, Notion, Slides
- **Maps**: Google Maps, OpenStreetMap
- **Others**: PDF, web pages (via bookmark)

---

## Template system

### Functions:
- **Template selection**: choose a template when creating
- **Custom templates**: create your own templates
- **Template category**: organised by type
- **Sharing templates**: share templates with the team

### Example templates:
- meeting minutes
- project planning
- product release notes
- team onboarding
- bug report
- content calendar
- personal database
- budget planning

---

## Shortcuts

See [shortcuts.md](shortcuts.md) for a complete list of all keyboard shortcuts.

---

## Comparison with other editors

| Function | Notion | Tango.io | Confluence | XWiki |
|----------|--------|----------|------------|-------|
| Block-based | ✅ yes | ✅ yes | ❌ no | ❌ no |
| Code highlighting | ✅ yes (40+ languages) | ✅ yes (20+ languages) | ❌ no | ✅ yes |
| Databases | ✅ yes | ❌ no | ❌ no | ✅ yes |
| Templates | ✅ yes | ✅ yes | ✅ yes | ✅ yes |
| Formulas | ✅ yes | ❌ no | ❌ no | ✅ yes |
| Embeds | ✅ yes (100+ services) | ✅ yes (100+ services) | ✅ yes | ✅ yes |
| Markdown | ❌ no | ❌ no | ❌ no | ✅ yes |
| Visual feedback | ✅ yes | ✅ yes | ✅ yes | ✅ yes |

---

## Recommendation

- **For team collaboration**: Notion (excellent databases and block structure)
- **For quick writing**: block-based navigation
- **For technical documentation**: code block with syntax highlighting
- **For data-based projects**: databases with relations and formulas
- **For visual organisation**: embeds, images and flexible layouts
