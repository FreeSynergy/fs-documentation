# Wiki.js - Structure & UI/UX

## Overview

Wiki.js has a clear, user-friendly structure with a sidebar-based navigation and
a central content area.

## Window structure

### Main areas

```
┌─────────────────────────────────────────────────────────────────┐
│  Header (navigation, search, user menu)                         │
├────────────┬────────────────────────────────────────────────────┤
│            │                                                     │
│  Sidebar   │     Content area                                    │
│  (links)   │     (main content)                                  │
│            │                                                     │
│ - Home     │  ┌─────────────────────────────────────────────┐   │
│ - Pages    │  │  page/content                               │   │
│ - Media    │  │                                             │   │
│ - Users    │  │  [editor or view]                           │   │
│ - Groups   │  │                                             │   │
│ - Settings │  │                                             │   │
│ - ...      │  └─────────────────────────────────────────────┘   │
│            │                                                     │
└────────────┴────────────────────────────────────────────────────┘
```

### Sidebar (left)

The sidebar is placed flush left and holds the main navigation:

| Element | Size | Function |
|---------|------|----------|
| Logo | ~40px | Wiki.js logo |
| Navigation items | variable | menu entries |
| User profile | ~40px | profile, settings, sign out |

### Content area (middle)

The content area takes up the largest part of the screen:

- **Header**: page title, menu (edit, share, etc.)
- **Breadcrumbs**: the navigation path
- **Main content**: page/content (editor or view)
- **Sidebar (right)**: optional meta information (versions, author, etc.)

### Layout variants

1. **Standard layout**: sidebar left + content + sidebar right
2. **Compact layout**: sidebar left + content (without the right sidebar)
3. **Full-screen editor**: only the editor, without navigation bars

## UI/UX

### Design principles

- **Minimalism**: reduced UI elements
- **Clarity**: a clear hierarchy and structure
- **Immediacy**: fast feedback on interactions
- **Consistency**: a uniform design across all areas

### Colour scheme

- **Light theme**: the classic light colour scheme
- **Dark theme**: a dark colour scheme for use at night
- **Custom**: adjustable colours (theme system)

### Typography

- **Headings**: a clear hierarchy (H1-H6)
- **Text**: readable font sizes (14-16px)
- **Code**: a monospace typeface
- **Lists**: clear bullets

### Interactions

- **Hover effects**: visual feedback on hover
- **Click feedback**: direct feedback on clicks
- **Drag & drop**: for media uploads
- **Auto-save**: automatic saving in the editor

### Responsive design

- **Desktop**: full functions with the sidebar
- **Tablet**: a reduced sidebar, optimised views
- **Mobile**: hamburger menu, optimised editor functions

## Editor structure

### WYSIWYG editor

```
┌─────────────────────────────────────────────────────────────────┐
│  Formatting bar (menu)                                          │
├─────────────────────────────────────────────────────────────────┤
│  Content area (full width)                                      │
│                                                                 │
│  [text, tables, images, etc.]                                   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Status bar (words, characters, preview button)                 │
└─────────────────────────────────────────────────────────────────┘
```

### Markdown editor

```
┌─────────────────────┬───────────────────────────────────────────────┐
│  Editor (left)      │  Preview (right)                              │
│                     │                                               │
│  [Markdown syntax]  │  [parsed HTML]                                │
│                     │                                               │
└─────────────────────┴───────────────────────────────────────────────┘
```

## Accessibility

- **Keyboard navigation**: complete control from the keyboard
- **Screen-reader support**: ARIA attributes
- **Contrast**: high contrast for better readability
- **Zoom**: a scalable UI without losing function

## Performance

- **Fast loading**: lazy loading for images
- **Caching**: client-side caching
- **Pagination**: for large lists
- **Debounce**: for search functions
