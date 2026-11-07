# Tango.io - Structure & UI/UX

## Overview

Tango.io has a clear, user-friendly structure with sidebar-based navigation and a central content area.

## Window Structure

### Main Areas

```
┌─────────────────────────────────────────────────────────────────┐
│  Header (Workspace, Search, User menu)                          │
├────────────┬────────────────────────────────────────────────────┤
│            │                                                    │
│  Sidebar   │     Content area                                   │
│  (Left)    │     (Main content)                                 │
│            │                                                    │
│ - Home     │  ┌─────────────────────────────────────────────┐  │
│ - Pages    │  │  Page/Content                               │  │
│ - Files    │  │                                             │  │
│ - Templates│  │  [Editor or view]                           │  │
│ - Members  │  │                                             │  │
│ - Dashboard│  │                                             │  │
│ - Settings │  └─────────────────────────────────────────────┘  │
│            │                                                    │
└────────────┴────────────────────────────────────────────────────┘
```

### Sidebar (Left)

The sidebar is placed on the left and contains the main navigation:

| Element | Size | Function |
|---------|------|----------|
| Logo | ~40px | Tango.io logo |
| Navigation items | variable | Menu items |
| Workspace selector | ~40px | Switch workspace |

### Content Area (Center)

The content area takes up most of the screen:

- **Header**: Page title, menu (Edit, Share, etc.)
- **Breadcrumbs**: Navigation path
- **Main content**: Page/content (editor or view)
- **Sidebar (Right)**: Optional meta information (versions, author, etc.)

### Layout Variants

1. **Standard layout**: Left sidebar + content + right sidebar
2. **Compact layout**: Left sidebar + content (without right sidebar)
3. **Full-screen editor**: Editor only, without navigation bars

## UI/UX

### Design Principles

- **Minimalism**: Reduced UI elements
- **Clarity**: Clear hierarchy and structure
- **Immediacy**: Fast feedback on interactions
- **Consistency**: Uniform design across all areas

### Color Scheme

- **Light theme**: Classic light color scheme
- **Dark theme**: Dark color scheme for night use
- **Custom**: Customizable colors (theme system)

### Typography

- **Headings**: Clear hierarchy (H1-H6)
- **Text**: Readable font sizes (14-16px)
- **Code**: Monospace font
- **Lists**: Clear bullet points

### Interactions

- **Hover effects**: Visual feedback on hover
- **Click feedback**: Direct feedback on clicks
- **Drag & drop**: For media uploads
- **Auto-save**: Automatic saving in the editor

### Responsive Design

- **Desktop**: Full features with sidebar
- **Tablet**: Reduced sidebar, optimized views
- **Mobile**: Hamburger menu, optimized editor features

## Editor Structure

### Block-Based Editor

```
┌─────────────────────────────────────────────────────────────────┐
│  Block menu (menu for each block)                               │
├─────────────────────────────────────────────────────────────────┤
│  Content area (full screen)                                     │
│                                                                 │
│  [Text, tables, images, etc.]                                   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Status bar (words, characters, preview button)                 │
└─────────────────────────────────────────────────────────────────┘
```

## Accessibility

- **Keyboard navigation**: Full control via keyboard
- **Screen reader support**: ARIA attributes
- **Contrast**: High contrast for better readability
- **Zoom**: Scalable UI without loss of function

## Performance

- **Fast loading**: Lazy loading for images
- **Caching**: Client-side caching
- **Pagination**: For large lists
- **Debounce**: For search functions
