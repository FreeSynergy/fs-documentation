# Confluence - Functions

## Overview

Confluence offers two main editors: the **Visual Editor** and the **source-code
editor (Wiki Markup)**. Since Confluence Cloud the visual editor is the default.

## Available editors

### 1. Visual Editor

#### Functions:
- **Formatting**: headings (H1-H6), bold, italic, underline, strikethrough
- **Lists**: numbered lists, bullet lists, task lists
- **Tables**: create/edit tables (add/remove columns and rows)
- **Media**: insert images and files (drag & drop)
- **Links**: add external and internal links
- **Alignment**: text alignment (left, centre, right)
- **Notes/boxes**: info, warning and success notices (callouts)
- **Code blocks**: syntax highlighting (with an extension)
- **Databases**: Confluence Data Center (tables, kanban)
- **Embeds**: YouTube, Jira issues, Confluence pages, etc.
- **Macros**: visual macro insertion
- **Templates**: insert templates

#### What the editor does NOT do:
- no direct HTML editing in visual mode
- no Markdown syntax in the visual editor
- no complex wiki macro syntax in visual mode
- code highlighting only with an extension

---

### 2. Source-code editor (Wiki Markup)

#### Functions:
- **Complete Wiki Markup syntax**: the Confluence syntax
- **Complete control**: control every character
- **Macros**: `{macro}` syntax for complex elements
- **HTML**: HTML support (with restrictions)
- **Links**: `[]` for internal links
- **Images**: `!image.jpg!` for images
- **Formatting**: `*bold*`, `_italic_`, `h1. Heading`
- **Tables**: `{table}` syntax
- **Macro examples**:
  ```confluence
  {toc}
  {note}
  This is a note
  {note}
  {code:javascript}
  console.log("Hello");
  {code}
  ```

#### What the editor does NOT do:
- no visual feedback (you only see the code)
- the Confluence syntax has to be learned
- no drag & drop for images

---

## Comparing the editors

| Function | Visual Editor | Source-code editor |
|----------|---------------|--------------------|
| Visual editing | ✅ yes | ❌ no |
| Wiki macro syntax | ❌ (invisible) | ✅ directly visible |
| Macros | ✅ visual (limited) | ✅ complete |
| HTML | ❌ only via macro | ✅ yes (limited) |
| Tables | ✅ visual | ✅ syntax (complex) |
| Insert images | ✅ drag & drop | ✅ syntax |
| Live preview | ✅ yes | ❌ no |
| Learning curve | ✅ low | ❌ medium-high |
| Advanced functions | ❌ limited | ✅ full control |

---

## Confluence macros (examples)

### Information box
```confluence
{note:title=Information}
This is some information
{note}
```

### Warning box
```confluence
{warning:title=Warning}
This is a warning
{warning}
```

### Code block (with an extension)
```confluence
{code:javascript}
function hello() {
  console.log("Hello World");
}
{code}
```

### Table
```confluence
{table}
| Head 1 | Head 2 |
| Cell 1 | Cell 2 |
{table}
```

### Embed content
```confluence
{embed:http://example.com}
```

### Embed a Jira issue
```confluence
{jira:PROJECT-123}
```

---

## Code block support

Confluence supports syntax highlighting for many languages (with an extension
or in newer versions):

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

Supported languages (varies with the configuration):
- JavaScript, TypeScript
- Python, Java, C#, C++, Go, Rust
- HTML, CSS, SCSS
- SQL, JSON, YAML, XML
- Bash, PowerShell
- Ruby, PHP, Swift, Kotlin
- Markdown, ReStructuredText
- and many more

---

## Confluence database block (Confluence Data Center)

### Functions:
- **Table view**: classic tables
- **Kanban view**: cards in columns
- **Calendar view**: data in a calendar
- **Filtering**: filter columns
- **Sorting**: sort columns

---

## Embed support

Confluence supports embeds from many services:

- **Video**: YouTube, Vimeo
- **Documents**: Google Docs, Office 365
- **Code**: GitHub Gist, Bitbucket
- **Social**: Twitter
- **Data**: Confluence pages (internal link)
- **Maps**: Google Maps
- **Others**: Jira issues, Confluence blog posts

---

## Shortcuts

See [shortcuts.md](shortcuts.md) for a complete list of all keyboard shortcuts.

---

## Comparison with other editors

| Function | Confluence | Notion | Tango.io | XWiki |
|----------|------------|--------|----------|-------|
| Visual editor | ✅ yes | ✅ yes | ✅ yes | ✅ yes |
| Wiki macro syntax | ✅ yes | ❌ no | ❌ no | ✅ yes |
| Code highlighting | ✅ yes (with an extension) | ✅ yes (40+ languages) | ✅ yes (20+ languages) | ✅ yes |
| Databases | ✅ yes (Data Center) | ✅ yes | ❌ no | ✅ yes |
| Templates | ✅ yes | ✅ yes | ✅ yes | ✅ yes |
| Embeds | ✅ yes | ✅ yes | ✅ yes | ✅ yes |
| Markdown | ❌ no | ✅ yes | ❌ no | ✅ yes |
| Live preview | ✅ yes | ✅ yes | ✅ yes | ❌ no |

---

## Recommendation

- **For enterprise environments**: Confluence (Jira integration, security)
- **For team collaboration**: Confluence (excellent integrations)
- **For technical documentation**: code block with syntax highlighting
- **For projects with Jira**: Confluence (native integration)
- **For beginners**: the visual editor (intuitive)
