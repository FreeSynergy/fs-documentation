# MediaWiki - Structure & UI/UX

## Overview

MediaWiki has a classic layout structure with sidebar navigation and a central content area. The layout depends heavily on user permissions.

## Window Structure

### Main Areas

```
┌─────────────────────────────────────────────────────────────────┐
│  Header (Navigation, Search, User menu)                         │
├─────────────┬───────────────────────────────────────────────────┤
│             │                                                   │
│  Sidebar    │   Main Content                                    │
│  (Links)    │   (Main content)                                  │
│             │                                                   │
│ - Actions   │  ┌─────────────────────────────────────────┐     │
│ - Tools     │  │  Page/Content                           │     │
│ - Special   │  │                                         │     │
│             │  │  [Editor or view]                       │     │
│             │  │                                         │     │
│             │  └─────────────────────────────────────────┘     │
└─────────────┴───────────────────────────────────────────────────┘
```

### Sidebar (Links)

The sidebar is placed on the left and contains the main navigation:

| Element | Size | Function |
|---------|------|----------|
| Logo | ~40px | MediaWiki logo |
| Navigation | variable | Actions, tools |
| Search | ~30px | Search field |
| Languages | variable | Interwiki links |

### Content Area (Center)

The content area takes up most of the screen:

- **Header**: Page title, actions menu (Edit, Share, etc.)
- **Breadcrumbs**: Navigation path (optional)
- **Main content**: Page/content (editor or view)
- **Footer**: Footer information (page author, license, etc.)

## UI/UX

### Design Principles

- **Minimalism**: Reduced UI elements
- **Clarity**: Clear hierarchy and structure
- **Function**: Function over form
- **Consistency**: Uniform design across all areas

### Color Scheme

- **Light theme**: Classic light color scheme
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

### Visual Editor

```
┌─────────────────────────────────────────────────────────────────┐
│  Formatting toolbar (menu)                                      │
├─────────────────────────────────────────────────────────────────┤
│  Content area (full screen)                                     │
│                                                                 │
│  [Text, tables, images, etc.]                                   │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Status bar (words, characters, preview button)                 │
└─────────────────────────────────────────────────────────────────┘
```

### Source Editor

```
┌─────────────────────┬───────────────────────────────────────────────┐
│  Editor (Left)      │  Diff/Preview (Right)                         │
│                     │                                               │
│  [WikiText]         │  [Parsed HTML]                                │
│                     │                                               │
└─────────────────────┴───────────────────────────────────────────────┘
```

## Accessibility

- **Keyboard navigation**: Full control via keyboard
- **Screen reader support**: ARIA attributes
- **Contrast**: High contrast for better readability
- **Zoom**: Scalable UI without loss of function

## Performance

- **Fast loading**: Server-side caching
- **Client-side caching**: Browser-side caching
- **Pagination**: For large lists
- **Debounce**: For search functions
