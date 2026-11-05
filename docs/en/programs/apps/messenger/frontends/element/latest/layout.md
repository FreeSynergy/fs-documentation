# Element - Structure & UI/UX

## Overview

Element has a modern, clear UI with activity bar, navigation area, content area, and status bar, optimized for chat communication.

## Window Structure

### Main Areas

```
┌─────────────────────────────────────────────────────────────────┐
│  Title bar (Menu, Title, Window controls)                       │
├───────┬──────────────────┬──────────────────┬───────────────────┤
│       │                  │                  │                   │
│  Act. │   Navigation     │   Content        │   Sidebar         │
│  Bar  │   (Left)         │   (Center)       │   (Right)         │
│ (Ext.)│  - Rooms         │  - Chat          │  - Room desc.     │
│       │  - Invitations   │  - Messages      │  - Members        │
│       │  - Search        │                  │  - Settings       │
│       │                  │                  │                   │
└───────┴──────────────────┴──────────────────┴───────────────────┘
```

### Activity Bar (Left)

The activity bar contains the main navigation:

| Element | Function |
|---------|----------|
| Rooms | Room overview |
| Invitations | Manage invitations |
| Search | Quick search |
| Profile | Own profile |
| Settings | Settings |

### Navigation (Left sidebar)

Next to the activity bar (in the current view):

| Element | Function |
|---------|----------|
| Rooms | Room overview (pinned rooms at top) |
| Invitations | Open invitations |
| Search | Search field |
| Profile | Own profile |
| Settings | Settings |

### Content Area (Center)

The content area takes up the largest part of the screen:

- **Room overview**: List of rooms
- **Chat window**: Chat messages
- **Message list**: Messages in chronological order
- **Input field**: Enter messages

### Sidebar (Right)

Optionally right: Display of details depending on the selected room

- **Room description**: Description and topic
- **Members**: Member list
- **Settings**: Room settings
- **Random functions**: Random functions

## UI/UX

### Design Principles

- **Modern**: Modern design with flat UI
- **Functional**: Function over form
- **Consistent**: Consistent design across all areas
- **Customizable**: Theme support

### Color Scheme

- **Light Theme**: Light color scheme (default)
- **Dark Theme**: Dark color scheme
- **Custom**: Customizable colors via theme system
- **Context-based colors**: Colors for message status

### Typography

- **Headings**: Clear hierarchy
- **Text**: Readable font sizes (12-14pt)
- **Lists**: Clear bullet points
- **Monospace**: For code blocks

### Interactions

- **Hover effects**: Visual feedback on hover
- **Click feedback**: Direct feedback on clicks
- **Drag & Drop**: For file transfer
- **Auto-save**: Automatic saving of drafts
- **Live preview**: Live preview when entering messages

### Responsive Design

- **Desktop**: Full features with sidebar
- **Tablet**: Limited (desktop app)
- **Mobile**: Separate mobile apps (iOS, Android)

## Editor Structure

### Chat Editor

```
┌─────────────────────────────────────────────────────────────────┐
│  Message list                                                   │
├─────────────────────────────────────────────────────────────────┤
│  [Messages]                                                     │
│                                                                 │
├─────────────────────────────────────────────────────────────────┤
│  Input field                                                    │
├─────────────────────────────────────────────────────────────────┤
│  [Enter message]                                                │
└─────────────────────────────────────────────────────────────────┘
```

### Room Description

```
┌─────────────────────────────────────────────────────────────────┐
│  Room name                                                      │
├─────────────────────────────────────────────────────────────────┤
│  Description                                                    │
│  [Room description]                                             │
├─────────────────────────────────────────────────────────────────┤
│  Topic                                                          │
│  [Room topic]                                                   │
├─────────────────────────────────────────────────────────────────┤
│  Members                                                        │
│  [Members list]                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## Accessibility

- **Keyboard navigation**: Complete control via keyboard
- **Screen reader support**: ARIA attributes
- **Contrast**: High contrast for better readability
- **Zoom**: Scalable UI (100-400%)
- **Accessibility**: WCAG compliance

## Performance

- **Fast loading**: Fast opening of messages
- **Caching**: Client-side caching
- **Pagination**: For large lists
- **Debounce**: For search functions
- **Lazy loading**: For large rooms
