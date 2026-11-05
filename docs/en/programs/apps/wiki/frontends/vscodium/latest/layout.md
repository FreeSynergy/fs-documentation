# VSCodium - Structure & UI/UX

## Overview

VSCodium has a modular layout structure with an activity bar, sidebar, editor
area and status bar.

## Window structure

### Main areas

```
┌─────────────────────────────────────────────────────────────────┐
│  Title bar (menu, window controls)                              │
├───────┬─────────────────────────────────────────────────────────┤
│       │                                                         │
│  Act. │  Sidebar (file tree, search, Git, debug, extensions)    │
│  Bar  │                                                         │
│ (left │  ┌───────────────────────┬─────────────────────────────┐│
│  )    │  │  Explorer           │  Search window               ││
│       │  │  - projects         │  - search field              ││
│       │  │  - file tree        │  - filter                    ││
│       │  └───────────────────────┴─────────────────────────────┘│
│       │                                                         │
│       │   Editor area (middle)                                  │
│       │  ┌─────────────────────────────────────────────────────┐│
│       │  │  File name 1    File name 2    File name 3          ││
│       │  ├─────────────────────────────────────────────────────┤│
│       │  │                                                     ││
│       │  │  Code editor                                        ││
│       │  │                                                     ││
│       │  │  [code with syntax highlighting]                    ││
│       │  │                                                     ││
│       │  └─────────────────────────────────────────────────────┘│
│       │                                                         │
│       │   Status bar (bottom)                                   │
│       │  ┌─────────────────────────────────────────────────────┐│
│       │  │  Line:Column  |  Syntax  |  Git  | Encoding  |  🐛  ││
│       │  └─────────────────────────────────────────────────────┘│
└───────┴─────────────────────────────────────────────────────────┘
```

### Activity bar (left)

The activity bar is placed flush left and holds the main navigation:

| Element | Size | Function |
|---------|------|----------|
| Explorer | ~50px | file tree |
| Search | ~50px | file search |
| Source control | ~50px | Git |
| Debugging | ~50px | debugging |
| Extensions | ~50px | plugins |

### Editor area (middle)

The editor area takes up the largest part of the screen:

- **Tab bar**: the open files
- **Editor**: code editor with syntax highlighting
- **Sidebar (right)**: optional (symbol definitions, search results)

### Status bar (bottom)

The status bar shows the important information:

| Element | Function |
|---------|----------|
| Line:Column | the cursor position |
| Syntax | the current syntax |
| Git | the Git status |
| Encoding | the file encoding |
| Linter | the linter status |

## UI/UX

### Design principles

- **Minimalism**: reduced UI elements
- **Clarity**: clear hierarchy and structure
- **Flexibility**: customisable layouts
- **Consistency**: a uniform design across all areas

### Colour scheme

- **Light theme**: classic light colour scheme
- **Dark theme**: dark colour scheme for night use
- **Custom**: adjustable colours (theme system)

### Typography

- **Code**: monospace font
- **UI**: sans-serif font
- **Lists**: clear bullet points

### Interactions

- **Hover effects**: visual feedback on hover
- **Click feedback**: direct feedback on clicks
- **Drag & drop**: for file operations
- **Auto-save**: automatic saving (optional)

### Responsive design

- **Desktop**: full functions with the sidebar
- **Tablet**: reduced sidebar, optimised views
- **Mobile**: limited (desktop app)

## Editor structure

### Code editor

```
┌─────────────────────────────────────────────────────────────────┐
│  Tab bar (open files)                                           │
├─────────────────────────────────────────────────────────────────┤
│  Content area (full screen)                                     │
│                                                                 │
│  [code with syntax highlighting]                                │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Status bar (line, column, syntax, Git, etc.)                   │
└─────────────────────────────────────────────────────────────────┘
```

## Accessibility

- **Keyboard navigation**: complete control by keyboard
- **Screen reader support**: ARIA attributes
- **Contrast**: high contrast for better readability
- **Zoom**: scalable UI without loss of function

## Performance

- **Fast loading**: files open quickly
- **Caching**: client-side caching
- **Pagination**: for large lists
- **Debounce**: for search functions
