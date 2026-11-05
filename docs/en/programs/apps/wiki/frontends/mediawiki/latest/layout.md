# MediaWiki - Structure & UI/UX

## Overview

MediaWiki has a classic layout structure with sidebar navigation and a central
content area. The layout depends heavily on user rights.

## Window structure

### Main areas

```
┌─────────────────────────────────────────────────────────────────┐
│  Header (navigation, search, user menu)                         │
├─────────────┬───────────────────────────────────────────────────┤
│             │                                                   │
│  Sidebar    │   Main content                                    │
│  (left)     │   (main content)                                  │
│             │                                                   │
│ - Actions   │  ┌─────────────────────────────────────────┐     │
│ - Tools     │  │  page/content                           │     │
│ - Special   │  │                                         │     │
│             │  │  [editor or view]                       │     │
│             │  │                                         │     │
│             │  └─────────────────────────────────────────┘     │
└─────────────┴───────────────────────────────────────────────────┘
```

### Sidebar (left)

The sidebar is placed flush left and holds the main navigation:

| Element | Size | Function |
|---------|------|----------|
| Logo | ~40px | MediaWiki logo |
| Navigation | variable | actions, tools |
| Search | ~30px | search field |
| Languages | variable | interwiki links |

### Content area (middle)

The content area takes up the largest part of the screen:

- **Header**: page title, actions menu (edit, share, etc.)
- **Breadcrumbs**: the navigation path (optional)
- **Main content**: page/content (editor or view)
- **Footer**: footer information (page author, licence, etc.)

## UI/UX

### Design principles

- **Minimalism**: reduced UI elements
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

### Source-code editor

```
┌─────────────────────┬───────────────────────────────────────────────┐
│  Editor (left)      │  Diff/preview (right)                         │
│                     │                                               │
│  [WikiText]         │  [parsed HTML]                                │
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
