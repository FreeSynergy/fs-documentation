# Confluence - Structure & UI/UX

## Overview

Confluence has a classic three-column layout structure with sidebar navigation
and a central content area.

## Window structure

### Main areas

```
┌─────────────────────────────────────────────────────────────────┐
│  Header (navigation, search, user menu)                         │
├─────────────┬──────────────────────┬────────────────────────────┤
│             │                      │                            │
│  Sidebar    │   Main content       │  Right sidebar             │
│  (left)     │   (main content)     │  (meta information)        │
│             │                      │                            │
│ - Pages     │  ┌────────────────┐  │  - Page info               │
│ - Spaces    │  │  page/content  │  │  - Versions                │
│ - Dashboard │  │                │  │  - Author                  │
│ - Templates │  │  [editor or    │  │  - Permissions             │
│ - ...       │  │   view]        │  │  - Tags                    │
│             │  └────────────────┘  │                            │
└─────────────┴──────────────────────┴────────────────────────────┘
```

### Sidebar (left)

The sidebar is placed flush left and holds the main navigation:

| Element | Size | Function |
|---------|------|----------|
| Logo | ~50px | Confluence logo |
| Pages | variable | page navigation |
| Spaces | variable | space selection |
| Dashboard | ~30px | dashboard access |
| Templates | variable | template access |

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

### Visual editor

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

### Wiki Markup editor

```
┌─────────────────────┬───────────────────────────────────────────────┐
│  Editor (left)      │  Preview (right)                              │
│                     │                                               │
│  [Wiki Markup]      │  [parsed HTML]                                │
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
