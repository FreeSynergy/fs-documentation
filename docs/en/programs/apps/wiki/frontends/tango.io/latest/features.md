# Tango.io - Features

## Overview

Tango.io uses a modern, visual editor built on web standards. The editor is strongly modeled on Notion, but with Tango.io-specific features.

## Available Editors

### 1. Visual Editor (WYSIWYG)

#### Features:
- **Formatting**: Headings (H1-H6), bold, italic, underline, strikethrough
- **Lists**: Numbered lists, bulleted lists, to-do lists (checkboxes)
- **Tables**: Create/edit tables (add/delete columns/rows)
- **Media**: Insert images, add links, emojis
- **Alignment**: Text alignment (left, center, right)
- **Callouts/boxes**: Info, warning, success callouts
- **Code blocks**: Syntax highlighting for several programming languages
- **Embeds**: YouTube, Vimeo, Spotify, Figma, Notion, Confluence, etc.
- **Page links**: Links to other Tango.io pages
- **User mentions**: @mention for collaboration
- **Timestamps**: Automatic dates

#### What the editor CANNOT do:
- No direct HTML editing
- No Markdown syntax in the editor (converted automatically)
- No complex table formulas
- No vertical text alignment
- No manual line breaks between all sentences

---

## Editor Features in Detail

### Block-Based Editing

Tango.io uses a **block editor**, where every line of text or component is its own "block".

#### Typical blocks:
1. **Text block**: Normal text with formatting
2. **Heading**: H1-H6 with automatic outline
3. **To-do list**: `-[ ] Task` for tasks
4. **Bulleted list**: `* Item` for lists
5. **Numbered list**: `1. Item` for numbered lists
6. **Quote**: `>` for quotes
7. **Code block**: ``` for code with syntax highlighting
8. **Table**: Table block for data
9. **Image**: Image block with options
10. **Embed**: Embed block for external content
11. **Page link**: Link to other pages
12. **File**: File upload

#### Block navigation:
- `Enter`: Create new line/block
- `Tab`: Indent (lists)
- `Shift+Tab`: Outdent (lists)
- `Escape`: Leave block
- `Cmd/Ctrl+Enter`: Run block (e.g. tick checkbox)

---

### Code Block Support

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
- Markdown (for code blocks themselves)

---

### Table Features

#### Features:
- **Columns/rows**: Add and delete
- **Formatting**: Text, numbers, checkboxes
- **Filtering**: Filter columns (per workspace)
- **Sorting**: Sort columns
- **Resize**: Adjust column width

#### Example:
| Name | Status | Priority |
|------|--------|----------|
| Task 1 | ✅ Done | High |
| Task 2 | ⏳ In progress | Medium |
| Task 3 | ❌ Open | Low |

---

### Embed Support

Tango.io supports embeds from many services:

- **Video**: YouTube, Vimeo
- **Audio**: Spotify, SoundCloud
- **Design**: Figma, Sketch, Adobe XD
- **Code**: GitHub Gist, CodePen, JSFiddle
- **Documents**: Google Docs, Notion, Slides
- **Maps**: Google Maps, OpenStreetMap
- **Social media**: Twitter, LinkedIn, Instagram (posts)

---

### Template System

#### Features:
- **Template selection**: Choose templates when creating
- **Custom templates**: Create your own templates
- **Template categories**: Organization by type
- **Template sharing**: Share templates with the team

#### Example templates:
- Meeting notes
- Project planning
- Product release notes
- Team onboarding
- Bug report
- Content calendar

---

## Shortcuts

See [shortcuts.md](shortcuts.md) for a complete list of keyboard shortcuts.

---

## Comparison with Other Editors

| Feature | Tango.io | Notion | Confluence |
|---------|----------|--------|------------|
| Block-based | ✅ Yes | ✅ Yes | ❌ No |
| Code highlighting | ✅ Yes (20+ languages) | ✅ Yes | ❌ No |
| Embeds | ✅ Yes (100+ services) | ✅ Yes | ✅ Limited |
| Tables | ✅ With filter/sort | ✅ With filter/sort | ✅ Basic |
| Templates | ✅ Yes | ✅ Yes | ✅ Yes |
| Markdown | ❌ No | ✅ Yes | ❌ No |
| Visual feedback | ✅ Yes | ✅ Yes | ✅ Yes |

---

## Recommendation

- **For team collaboration**: Tango.io editor (excellent embeds and block structure)
- **For fast writing**: Block-based navigation
- **For technical documentation**: Code block with syntax highlighting
- **For visual organization**: Embeds and images
