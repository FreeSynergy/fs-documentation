# Tango.io - Structure & UI/UX

## Overview

Tango.io has a clear, user-friendly structure with a sidebar-based navigation
and a central content area.

## Window structure

### Main areas

```
┌─────────────────────────────────────────────────────────────────┐
│  Header (workspace, search, user menu)                          │
├────────────┬────────────────────────────────────────────────────┤
│            │                                                     │
│  Sidebar   │     Content area                                    │
│  (left)    │     (main content)                                  │
│            │                                                     │
│ - Home     │  ┌─────────────────────────────────────────────┐   │
│ - Pages    │  │  page/content                               │   │
│ - Files    │  │                                             │   │
│ - Templates│  │  [editor or view]                           │   │
│ - Members  │  │                                             │   │
│ - Dashboard│  │                                             │   │
│ - Settings │  └─────────────────────────────────────────────┘   │
│            │                                                     │
└────────────┴────────────────────────────────────────────────────┘
```

### Sidebar (left)

The sidebar is placed flush left and holds the main navigation:

| Element | Size | Function |
|---------|------|----------|
| Logo | ~40px | Tango.io logo |
| Navigation items | variable | menu entries |
| Workspace selection | ~40px | switch workspace |

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
- **Clarity**: clear hierarchy and structure
- **Immediacy**: fast feedback on interactions
- **Consistency**: a uniform design across all areas

### Colour scheme

- **Light theme**: classic light colour scheme
- **Dark theme**: dark colour scheme for night use
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

### Block-based editor

```
┌─────────────────────────────────────────────────────────────────┐
│  Block menu (a menu for every block)                            │
├─────────────────────────────────────────────────────────────────┤
│  Content area (full screen)                                     │
│                                                                 │
│  [text, tables, images, etc.]                                   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Status bar (words, characters, preview button)                 │
└─────────────────────────────────────────────────────────────────┘
```

## Accessibility

- **Keyboard navigation**: complete control by keyboard
- **Screen reader support**: ARIA attributes
- **Contrast**: high contrast for better readability
- **Zoom**: scalable UI without loss of function

## Performance

- **Fast loading**: lazy loading for images
- **Caching**: client-side caching
- **Pagination**: for large lists
- **Debounce**: for search functions
