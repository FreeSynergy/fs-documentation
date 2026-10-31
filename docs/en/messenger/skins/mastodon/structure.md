# Mastodon - Structure & UI/UX

## Overview

Mastodon has a modern, clear UI with activity bar, navigation area, content area, and status bar, optimized for microblogging.

## Window Structure

### Main Areas

```
┌─────────────────────────────────────────────────────────────────┐
│  Title bar (Menu, Title, Window controls)                       │
├───────┬──────────────────┬──────────────────┬───────────────────┤
│       │                  │                  │                   │
│  Act. │   Navigation     │   Content        │   Sidebar         │
│  Bar  │   (Left)         │   (Center)       │   (Right)         │
│ (Int.)│  - Timeline      │  - Toots         │  - Users          │
│       │  - Toots         │  - Timeline      │  - Notifications  │
│       │  - Profile       │                  │  - Profile        │
│       │                  │                  │                   │
└───────┴──────────────────┴──────────────────┴───────────────────┘
```

### Activity Bar (Left)

The activity bar contains the main navigation (integrated into the navigation bar):

| Element | Function |
|---------|----------|
| Timeline | Timeline overview |
| Toots | Toot input field |
| Profile | Own profile |
| Notifications | Notifications |
| Direct Messages | Direct messages |

### Navigation (Left)

Left in the navigation bar:

| Element | Function |
|---------|----------|
| Home | Home timeline |
| Local | Local timeline |
| Federated | Federated timeline |
| Hashtags | Hashtag timeline |
| Profile | Own profile |
| Notifications | Notifications |
| Direct Messages | Direct messages |

### Content Area (Center)

The content area takes up the largest part of the screen:

- **Timeline overview**: Timeline selection (Home, Local, Federated)
- **Toot list**: Toots in chronological order
- **Toot input field**: Enter toots

### Sidebar (Right)

Optionally right: Display of details depending on the selected element

- **User profiles**: Profile information
- **Notifications**: List of notifications
- **Profile**: Own profile
- **Search**: Search in timeline

## UI/UX

### Design Principles

- **Minimal**: Minimalist design with focus on content
- **Clear**: Clear hierarchy and navigation
- **Functional**: Function over form
- **Consistent**: Consistent design across all areas

### Color Scheme

- **Light Theme**: Light color scheme (default)
- **Dark Theme**: Dark color scheme
- **Custom**: Customizable colors via theme system
- **Context-based colors**: Colors for toot status

### Typography

- **Headings**: Clear hierarchy
- **Text**: Readable font sizes (14-16pt)
- **Lists**: Clear bullet points
- **Monospace**: For code blocks

### Interactions

- **Hover effects**: Visual feedback on hover
- **Click feedback**: Direct feedback on clicks
- **Drag & Drop**: For media uploads
- **Auto-save**: Automatic saving of drafts
- **Live preview**: Live preview when entering toots

### Responsive Design

- **Desktop**: Full features with sidebar
- **Tablet**: Limited (desktop app)
- **Mobile**: Separate mobile apps (iOS, Android)

## Editor Structure

### Toot Editor

```
┌─────────────────────────────────────────────────────────────────┐
│  New toot                                                       │
├─────────────────────────────────────────────────────────────────┤
│  [Toot input field]                                             │
├─────────────────────────────────────────────────────────────────┤
│  Media                                                          │
├─────────────────────────────────────────────────────────────────┤
│  [Select images/videos]                                         │
├─────────────────────────────────────────────────────────────────┤
│  Sensitive                                                                      │
├─────────────────────────────────────────────────────────────────┤
│  [Sensitive checkbox]                                           │
├─────────────────────────────────────────────────────────────────┤
│  Visibility                                                     │
├─────────────────────────────────────────────────────────────────┤
│  [Public/Unlisted/Private/Direct]                               │
├─────────────────────────────────────────────────────────────────┤
│  [Send toot]                                                    │
└─────────────────────────────────────────────────────────────────┘
```

### Timeline View

```
┌─────────────────────────────────────────────────────────────────┐
│  Timeline header                                                │
├─────────────────────────────────────────────────────────────────┤
│  Home  Local  Federated  Hashtags                              │
├─────────────────────────────────────────────────────────────────┤
│  Toot list                                                      │
├─────────────────────────────────────────────────────────────────┤
│  [Toot]                                                         │
│  [Toot]                                                         │
│  [Toot]                                                         │
└─────────────────────────────────────────────────────────────────┘
```

## Accessibility

- **Keyboard navigation**: Complete control via keyboard
- **Screen reader support**: ARIA attributes
- **Contrast**: High contrast for better readability
- **Zoom**: Scalable UI (100-400%)
- **Accessibility**: WCAG compliance

## Performance

- **Fast loading**: Fast opening of toots
- **Caching**: Client-side caching
- **Pagination**: For large lists
- **Debounce**: For search functions
- **Lazy loading**: For large timelines
