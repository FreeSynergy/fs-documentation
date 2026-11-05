# Wiki.js - Features

## Overview

Wiki.js offers two editor modes: a visual WYSIWYG editor and a Markdown editor.
The editor is extremely user-friendly and modularly extensible.

## Available editors

### 1. Visual editor (WYSIWYG)

#### Functions:
- **Formatting**: headings, bold, italic, underline, strikethrough
- **Lists**: numbered lists, bullet lists, task lists
- **Text marking**: quotes, code blocks, highlighting
- **Tables**: create and edit tables (add/remove columns/rows)
- **Media**: insert images, add links, emojis
- **Alignment**: text alignment (left, centre, right, justified)
- **Notices/boxes**: info, warning and success notices
- **Code blocks**: syntax highlighting for various programming languages
- **Math formulas**: LaTeX support (optional)
- **Diagrams**: Mermaid diagrams (optional)
- **Embeds**: videos (YouTube, Vimeo), iframes

#### What the editor does NOT do:
- no direct HTML editing in the visual mode
- no complex macros (only through extensions)
- no vertical text alignment
- no text wrapping with a manual line break between every sentence

---

### 2. Markdown editor

#### Functions:
- **Complete Markdown support**: the common Markdown syntax
- **GitHub-flavoured Markdown**: tables, task lists, strikes
- **Front matter**: metadata for pages (title, description, etc.)
- **Live preview**: a real-time preview of the result
- **Snippets**: templates for frequently used blocks
- **Extensible syntax**: through plugins (e.g. Mermaid, LaTeX)

#### Markdown-supported formatting:
```markdown
# Heading 1
## Heading 2
### Heading 3

**bold**, *italic*, `code`

- bullet
- item 2
- item 3

1. numbered
2. list

> quote

| Table | Column 1 | Column 2 |
|-------|----------|----------|
| Row 1 | Data A   | Data B   |
```

#### What the editor does NOT do:
- no WYSIWYG while editing (you have to know the Markdown syntax)
- no visual table editing
- no direct formatting of text colours (only via inline HTML or extensions)

---

## Editor comparison

| Function | WYSIWYG | Markdown |
|----------|---------|----------|
| Visual editing | ✅ yes | ❌ no |
| Markdown syntax | ❌ no | ✅ yes |
| Live preview | ✅ yes | ✅ yes |
| Tables | ✅ visual | ✅ syntax |
| Code blocks | ✅ with syntax highlighting | ✅ with syntax highlighting |
| Images | ✅ drag & drop | ✅ Markdown syntax |
| Links | ✅ link button | ✅ Markdown syntax |
| Table editor | ✅ visual | ✅ text-based |
| No learning curve | ✅ yes | ❌ Markdown has to be learned |
| Advanced formatting | ❌ limited | ✅ very flexible |

---

## Extensible functions (through plugins)

Wiki.js is extremely extensible. The following functions can be added through
plugins:

- **Mermaid**: diagrams (flowcharts, sequence diagrams, etc.)
- **LaTeX**: mathematical formulas
- **Syntax highlighting**: support for 200+ programming languages
- **Embeds**: YouTube, Vimeo, Spotify, Twitter, etc.
- **Emoji**: extended emoji support
- **Kroki**: diagrams from text (PlantUML, Mermaid, etc.)
- **MathJax**: mathematical formulas
- **VideoJS**: extended video support

---

## Shortcuts

see [shortcuts.md](shortcuts.md) for a complete list of all keyboard shortcuts.

---

## Recommendation

- **For beginners**: the WYSIWYG editor (intuitive, no syntax needed)
- **For advanced users**: the Markdown editor (more control, faster working)
- **For developers**: Markdown with code blocks and syntax highlighting
