# XWiki - Structure & UI/UX

## Overview

XWiki has a classic three-column layout structure with sidebar navigation and a
central content area.

## Window structure

### Main areas

```
┌─────────────────────────────────────────────────────────────────┐
│  Header (search, navigation, user menu)                         │
├─────────────┬──────────────────────┬────────────────────────────┤
│             │                      │                            │
│  Sidebar    │   Main content       │  Right sidebar             │
│  (left)     │   (main content)     │  (meta information)        │
│             │                      │                            │
│ - Actions   │  ┌────────────────┐  │  - Page info               │
│ - Search    │  │  page/content  │  │  - Versions                │
│ - Tools     │  │                │  │  - Author                  │
│ - Pages     │  │  [editor or    │  │  - Permissions             │
│ - Spaces    │  │   view]        │  │  - Tags                    │
│ - ...       │  │                │  │  - Web links               │
│             │  └────────────────┘  │                            │
└─────────────┴──────────────────────┴────────────────────────────┘
```

### Sidebar (left)

The sidebar is placed flush left and holds the main navigation:

| Element | Size | Function |
|---------|------|----------|
| Logo | ~50px | XWiki logo |
| Actions | variable | edit, print, etc. |
| Search | ~30px | search field |
| Tools | variable | further tools |
| Pages | variable | page navigation |
| Spaces | variable | space selection |

### Content area (middle)

The content area takes up the largest part of the screen:

- **Header**: page title, actions menu (edit, share, etc.)
- **Breadcrumbs**: the navigation path
- **Main content**: page/content (editor or view)
- **Footer**: footer information

### Right sidebar

Optional right sidebar with meta information:

| Element | Function |
|---------|----------|
| Page info | meta information |
| Versions | version history |
| Tags | tag information |
| Web links | links |

## UI/UX

### Design principles

- **Classic**: traditional wiki design
- **Clarity**: clear hierarchy and structure
- **Function**: function over form
- **Consistency**: a uniform design across all areas

### Colour scheme

- **Light theme**: classic light colour scheme
- **Custom**: adjustable colours (theme system)

### Typography

- **Headings**: clear hierarchy (H1-H6)
- **Text**: readable font sizes (14-16px)
- **Code**: monospace font
- **Lists**: clear bullet points

### Interactions

- **Hover effects**: visual feedback on hover
- **Click feedback**: direct feedback on clicks
- **Drag & drop**: for media uploads
- **Auto-save**: automatic saving in the editor

### Responsive design

- **Desktop**: full functions with the sidebar
- **Tablet**: reduced sidebar, optimised views
- **Mobile**: hamburger menu, optimised editor functions

## Editor structure

### WYSIWYG editor

```
┌─────────────────────────────────────────────────────────────────┐
│  Formatting bar (menu)                                          │
├─────────────────────────────────────────────────────────────────┤
│  Content area (full screen)                                     │
│                                                                 │
│  [text, tables, images, etc.]                                   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Status bar (words, characters, preview button)                 │
└─────────────────────────────────────────────────────────────────┘
```

### XWiki syntax editor

```
┌─────────────────────┬───────────────────────────────────────────────┐
│  Editor (left)      │  Preview (right)                              │
│                     │                                               │
│  [XWiki syntax]     │  [parsed HTML]                                │
│                     │                                               │
└─────────────────────┴───────────────────────────────────────────────┘
```

### Markdown editor

```
┌─────────────────────┬───────────────────────────────────────────────┐
│  Editor (left)      │  Preview (right)                              │
│                     │                                               │
│  [Markdown]         │  [parsed HTML]                                │
│                     │                                               │
└─────────────────────┴───────────────────────────────────────────────┘
```

## Accessibility

- **Keyboard navigation**: complete control by keyboard
- **Screen reader support**: ARIA attributes
- **Contrast**: high contrast for better readability
- **Zoom**: scalable UI without loss of function

## Performance

- **Fast loading**: server-side caching
- **Client-side caching**: browser-side caching
- **Pagination**: for large lists
- **Debounce**: for search functions
