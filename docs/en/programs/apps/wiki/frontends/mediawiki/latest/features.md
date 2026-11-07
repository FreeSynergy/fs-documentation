# MediaWiki - Features

## Overview

MediaWiki offers two main editors: the classic **source editor** with wiki syntax and the **Visual Editor (VisualEditor)**. Availability depends on the server configuration.

## Available Editors

### 1. Visual Editor (VisualEditor)

#### Features:
- **WYSIWYG**: What you see is what you edit
- **Formatting**: Headings (H1-H6), bold, italic, underline
- **Lists**: Numbered lists, bulleted lists
- **Tables**: Create/edit tables (columns/rows)
- **Media**: Insert images and files
- **Links**: Add external and internal links
- **Templates**: Insert templates (visually)
- **Sources**: Citations and references
- **Code blocks**: Syntax highlighting (optional)
- **Math formulas**: LaTeX support (optional)
- **Diagrams**: With extensions (e.g. Graphviz)

#### What the editor CANNOT do:
- No direct wiki syntax editing in visual mode
- No direct view of complex template parameters
- No direct editing of wikitext structures
- Limited support for advanced features

---

### 2. Source Editor (WikiText)

#### Features:
- **Full wiki syntax**: MediaWiki syntax (wikitext)
- **Full control**: Control every character
- **Templates**: `{{Template}}` syntax
- **Links**: `[[Page name]]` internal links
- **Images**: `[[File:Image.jpg|Thumb|Description]]`
- **Categories**: `[[Category:Name]]`
- **Formatting**: `'bold'`, `''italic''`, `===Heading===`
- **Lists**: `* Bulleted`, `# Numbered`
- **Tables**: `{| ... |}` syntax
- **HTML**: Limited HTML support

#### Wiki syntax examples:
```wikitext
== Heading ==
'''Bold text''' and ''italic text''

* Bulleted list
* Item 2

1. Numbered
2. List

[[Internal page]]
[[Internal page|Displayed text]]

[[File:Image.jpg|mini|Right|Description]]

{{Template|Parameter=Value}}
```

#### What the editor CANNOT do:
- No visual feedback (you only see the code)
- Wiki syntax has to be learned
- No drag and drop for images
- No live preview (except with special extensions)

---

### 3. Edit Source (Alternative Mode)

#### Features:
- **Code editor**: For developers
- **Syntax highlighting**: Colored markup
- **Autocompletion**: Optional
- **Line numbers**: Optional

#### What the editor CANNOT do:
- No WYSIWYG
- No live preview (without an extension)

---

## Editor Comparison

| Feature | Visual Editor | Source Editor |
|---------|---------------|---------------|
| Visual editing | ✅ Yes | ❌ No |
| Wiki syntax | ❌ (invisible) | ✅ Directly visible |
| Templates | ✅ Visual (limited) | ✅ Complete |
| Tables | ✅ Visual | ✅ Syntax (complex) |
| Insert images | ✅ Drag & drop | ✅ Syntax |
| Live preview | ✅ Yes | ❌ No (optional) |
| Learning curve | ✅ Low | ❌ Medium-high |
| Advanced features | ❌ Limited | ✅ Full control |

---

## Recommendation

- **For beginners**: Visual Editor (intuitive, no syntax required)
- **For advanced users**: Source Editor (more control, fast)
- **For template users**: Source Editor (complete template support)

---

## Shortcuts

See [shortcuts.md](shortcuts.md) for a complete list of keyboard shortcuts.

---

## MediaWiki Variant "Source Editor" (Web UI)

Many MediaWiki installations also offer an improved source editor with:

- **Syntax highlighting**: Colored syntax markup
- **Line numbers**: For better orientation
- **Autocompletion**: For common syntax
- **Diff view**: Changes in context

---

## Editor Extensions

### VisualEditor extensions:
- **Citoid**: Automatic citation
- **Math**: LaTeX formulas
- **Graph**: Diagrams
- **Kartographer**: Maps
- **Score**: Music notation
- **Linter**: Error detection

### Source editor extensions:
- **CodeEditor**: Improved source editor
- **WikiEditor**: Extended toolbar
- **SyntaxHighlight**: Code highlighting
