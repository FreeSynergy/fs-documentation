# Wiki.js - Features

## Overview

Wiki.js offers two editor modes: a visual WYSIWYG editor and a Markdown editor. The editor is extremely user-friendly and modularly extensible.

## Available Editors

### 1. Visual Editor (WYSIWYG)

#### Features:
- **Formatting**: Headings, bold, italic, underline, strikethrough
- **Lists**: Numbered lists, bulleted lists, task lists
- **Text markup**: Quotes, code blocks, highlighting
- **Tables**: Create and edit tables (add/delete columns/rows)
- **Media**: Insert images, add links, emojis
- **Alignment**: Text alignment (left, center, right, justified)
- **Callouts/boxes**: Info, warning, success callouts
- **Code blocks**: Syntax highlighting for various programming languages
- **Math formulas**: LaTeX support (optional)
- **Diagrams**: Mermaid diagrams (optional)
- **Embedding**: Videos (YouTube, Vimeo), iframes

#### What the editor CANNOT do:
- No direct HTML editing in visual mode
- No complex macros (only via extensions)
- No vertical text alignment
- No manual line breaks between all sentences

---

### 2. Markdown Editor

#### Features:
- **Full Markdown support**: Common Markdown syntax
- **GitHub-Flavored Markdown**: Tables, task lists, strikethrough
- **Front matter**: Metadata for pages (title, description, etc.)
- **Live preview**: Real-time preview of the result
- **Snippets**: Templates for common blocks
- **Extensible syntax**: Via plugins (e.g. Mermaid, LaTeX)

#### Supported Markdown formatting:
```markdown
# Heading 1
## Heading 2
### Heading 3

**bold**, *italic*, `code`

- Bulleted list
- Item 2
- Item 3

1. Numbered
2. List

> Quote

| Table | Column 1 | Column 2 |
|---------|----------|----------|
| Row 1 | Data A  | Data B  |
```

#### What the editor CANNOT do:
- No WYSIWYG while editing (you must know Markdown syntax)
- No visual table editing
- No direct formatting of text colors (only via inline HTML or extensions)

---

## Editor Comparison

| Feature | WYSIWYG | Markdown |
|---------|---------|----------|
| Visual editing | ✅ Yes | ❌ No |
| Markdown syntax | ❌ No | ✅ Yes |
| Live preview | ✅ Yes | ✅ Yes |
| Tables | ✅ Visual | ✅ Syntax |
| Code blocks | ✅ With syntax highlighting | ✅ With syntax highlighting |
| Images | ✅ Drag & drop | ✅ Markdown syntax |
| Links | ✅ Link button | ✅ Markdown syntax |
| Table editor | ✅ Visual | ✅ Text-based |
| No learning curve | ✅ Yes | ❌ Markdown must be learned |
| Advanced formatting | ❌ Limited | ✅ Very flexible |

---

## Extensible Features (via Plugins)

Wiki.js is highly extensible. The following features can be added via plugins:

- **Mermaid**: Diagrams (flowcharts, sequence diagrams, etc.)
- **LaTeX**: Mathematical formulas
- **Syntax highlighting**: Support for 200+ programming languages
- **Embeds**: YouTube, Vimeo, Spotify, Twitter, etc.
- **Emoji**: Extended emoji support
- **Kroki**: Diagrams from text (PlantUML, Mermaid, etc.)
- **MathJax**: Mathematical formulas
- **VideoJS**: Extended video support

---

## Shortcuts

See [shortcuts.md](shortcuts.md) for a complete list of keyboard shortcuts.

---

## Recommendation

- **For beginners**: WYSIWYG editor (intuitive, no syntax required)
- **For advanced users**: Markdown editor (more control, faster work)
- **For developers**: Markdown with code blocks and syntax highlighting
