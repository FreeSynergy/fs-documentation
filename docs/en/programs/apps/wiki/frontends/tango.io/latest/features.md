# Tango.io - Functions

## Overview

Tango.io uses a modern visual editor built on web standards. The editor is
closely modelled on Notion, but with Tango.io-specific functions.

## Available editors

### 1. Visual editor (WYSIWYG)

#### Functions:
- **Formatting**: headings (H1-H6), bold, italic, underline, strikethrough
- **Lists**: numbered lists, bullet lists, task lists (checkboxes)
- **Tables**: create/edit tables (add/remove columns and rows)
- **Media**: insert images, add links, emojis
- **Alignment**: text alignment (left, centre, right)
- **Notes/boxes**: info, warning and success notices
- **Code blocks**: syntax highlighting for several programming languages
- **Embeds**: YouTube, Vimeo, Spotify, Figma, Notion, Confluence, etc.
- **Page links**: links to other Tango.io pages
- **User mentions**: @mention for collaboration
- **Timestamps**: automatic dates

#### What the editor does NOT do:
- no direct HTML editing
- no Markdown syntax in the editor (it is converted automatically)
- no complex table formulas
- no vertical text alignment
- no text wrapping with a manual line break between all sentences

---

## Editor features in detail

### Block-based editing

Tango.io uses a **block editor** in which every text line or component is its
own "block".

#### Typical blocks:
1. **Text block**: normal text with formatting
2. **Heading**: H1-H6 with automatic outlining
3. **To-do list**: `-[ ] Task` for tasks
4. **Bullet list**: `* item` for lists
5. **Numbered list**: `1. item` for numbered lists
6. **Quote**: `>` for quotes
7. **Code block**: ``` for code with syntax highlighting
8. **Table**: table block for data
9. **Image**: image block with options
10. **Embed**: embed block for external content
11. **Page link**: a link to another page
12. **File**: file upload

#### Block navigation:
- `Enter`: create a new line/block
- `Tab`: indent (lists)
- `Shift+Tab`: outdent (lists)
- `Escape`: leave the block
- `Cmd/Ctrl+Enter`: run the block (e.g. tick the checkbox)

---

### Code block support

Tango.io supports syntax highlighting for many languages:

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

Supported languages:
- JavaScript, TypeScript
- Python, Java, C#, C++, Go, Rust
- HTML, CSS, SCSS
- SQL, JSON, YAML, XML
- Bash, PowerShell
- Ruby, PHP, Swift, Kotlin
- Markdown (for the code blocks themselves)

---

### Table features

#### Functions:
- **Columns/rows**: add and delete
- **Formatting**: text, numbers, checkboxes
- **Filtering**: filter columns (per workspace)
- **Sorting**: sort columns
- **Resize**: adjust the column width

#### Example:
| Name | Status | Priority |
|------|--------|----------|
| Task 1 | ✅ Done | High |
| Task 2 | ⏳ In progress | Medium |
| Task 3 | ❌ Open | Low |

---

### Embed support

Tango.io supports embeds from many services:

- **Video**: YouTube, Vimeo
- **Audio**: Spotify, SoundCloud
- **Design**: Figma, Sketch, Adobe XD
- **Code**: GitHub Gist, CodePen, JSFiddle
- **Documents**: Google Docs, Notion, Slides
- **Maps**: Google Maps, OpenStreetMap
- **Social media**: Twitter, LinkedIn, Instagram (posts)

---

### Template system

#### Functions:
- **Template selection**: choose a template when creating
- **Custom templates**: create your own templates
- **Template category**: organised by type
- **Sharing templates**: share templates with the team

#### Example templates:
- meeting minutes
- project planning
- product release notes
- team onboarding
- bug report
- content calendar

---

## Shortcuts

See [shortcuts.md](shortcuts.md) for a complete list of all keyboard shortcuts.

---

## Comparison with other editors

| Function | Tango.io | Notion | Confluence |
|----------|----------|--------|------------|
| Block-based | ✅ yes | ✅ yes | ❌ no |
| Code highlighting | ✅ yes (20+ languages) | ✅ yes | ❌ no |
| Embeds | ✅ yes (100+ services) | ✅ yes | ✅ limited |
| Tables | ✅ with filter/sort | ✅ with filter/sort | ✅ basic |
| Templates | ✅ yes | ✅ yes | ✅ yes |
| Markdown | ❌ no | ✅ yes | ❌ no |
| Visual feedback | ✅ yes | ✅ yes | ✅ yes |

---

## Recommendation

- **For team collaboration**: the Tango.io editor (excellent embeds and block structure)
- **For quick writing**: block-based navigation
- **For technical documentation**: code block with syntax highlighting
- **For visual organisation**: embeds and images
