# XWiki - Functions

## Overview

XWiki offers several editors depending on the configuration and the
extensions. The standard editor is the "WYSIWYG editor" (web content editor),
but XWiki also supports Markdown and the XWiki syntax.

## Available editors

### 1. WYSIWYG editor (web content editor)

#### Functions:
- **Visual editing**: like Word or Google Docs
- **Formatting**: headings (H1-H6), bold, italic, underline, strikethrough
- **Lists**: numbered lists, bullet lists, task lists
- **Tables**: create/edit tables (add/remove columns and rows)
- **Media**: insert images, add links
- **Alignment**: text alignment, indents
- **Notes**: boxes for information, warnings, etc.
- **Code blocks**: syntax highlighting (optional)
- **Macros**: visual macro insertion (e.g. tables, diagrams, info boxes)
- **Rich content**: videos, iframes, diagrams

#### What the editor does NOT do:
- no direct HTML writing (only through a macro)
- no Markdown syntax in WYSIWYG mode
- no complex versioning directly in the editor
- macros have to be inserted through the menu (not directly in the text)

---

### 2. XWiki syntax editor

#### Functions:
- **XWiki macro syntax**: complete XWiki macro support
- **Direct writing**: no WYSIWYG, but full control
- **Versioning**: the complete history
- **Macros**: `{{macro}}` syntax for complex elements
- **Macros**:
  ```xwiki
  {{toc/}}
  {{message box="info"}}
  This is an info message
  {{/message}}
  {{velocity}}
  #set($x = 1)
  {{/velocity}}
  ```

#### What the editor does NOT do:
- no visual feedback (you only see the code)
- the XWiki syntax has to be learned
- no drag & drop for images

---

### 3. Markdown editor (optional)

#### Functions:
- **GitHub-flavoured Markdown**: standard Markdown
- **Live preview**: real-time preview
- **Lists, tables, code**: everything Markdown provides
- **Integration**: XWiki macros can be embedded

#### What the editor does NOT do:
- no XWiki-specific macros (except through inline HTML)
- fewer functions than WYSIWYG

---

## Comparing the editors

| Function | WYSIWYG | XWiki syntax | Markdown |
|----------|---------|--------------|----------|
| Visual editing | ✅ yes | ❌ no | ❌ no |
| XWiki macros | ✅ via menu | ✅ directly | ❌ limited |
| HTML | ❌ only via macro | ✅ yes | ✅ inline HTML |
| Markdown | ❌ no | ✅ (XWiki extension) | ✅ yes |
| Tables | ✅ visual | ✅ syntax | ✅ syntax |
| Live preview | ✅ yes | ❌ no | ✅ yes (optional) |
| Learning curve | ✅ low | ❌ high | ✅ medium |

---

## Recommendation

- **For editors**: the WYSIWYG editor (intuitive, visual)
- **For developers**: the XWiki syntax editor (full control, macros)
- **For frontend developers**: Markdown (if the XWiki configuration allows it)

---

## Shortcuts

See [shortcuts.md](shortcuts.md) for a complete list of all keyboard shortcuts.

---

## XWiki macros (examples)

### Information box
```xwiki
{{message box="info"}}
This is some information
{{/message}}
```

### Table
```xwiki
{{table}}
|| Head 1 || Head 2 ||
|| Cell 1 | Cell 2 ||
{{/table}}
```

### Velocity (scripting)
```xwiki
{{velocity}}
#set($list = ["A", "B", "C"])
#foreach($item in $list)
$item
#end
{{/velocity}}
```

### Diagram (with the chart extension)
```xwiki
{{chart type="pie"}}
{"data": [1, 2, 3], "labels": ["A", "B", "C"]}
{{/chart}}
```
