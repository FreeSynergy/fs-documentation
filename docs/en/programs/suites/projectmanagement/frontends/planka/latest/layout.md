# Planka - Structure and UI/UX

## Page structure

```
┌──────────────────────────────────────────────────────────────────┐
│ Planka   [Project name ▾]       🔍 Search    👤 User    ⚙ Admin  │
├──────────────┬───────────────────────────────────────────────────┤
│ Project      │  Board view (columns)                             │
│ sidebar      │  ┌──────────┬──────────┬──────────┐               │
│ 🏠 Boards    │  │ To Do    │ In Perf. │ Done     │               │
│ 📋 Projects  │  │ ┌──────┐ │ ┌──────┐ │ ┌──────┐ │               │
│ 🏷 Labels    │  │ │Task A│ │ │Task C│ │ │Task E│ │               │
│ 👥 Members   │  │ └──────┘ │ └──────┘ │ └──────┘ │               │
│ 📅 Calendar  │  │ ┌──────┐ │          │          │               │
│ ⚙ Settings   │  │ │Task B│ │          │          │               │
│              │  │ └──────┘ │          │          │               │
│ + Project    │  └──────────┴──────────┴──────────┘               │
└──────────────┴───────────────────────────────────────────────────┘
```

- Task cards show title, labels (coloured), due date, assignee avatars, comment/subtask counters
- Task detail as a modal: description, checklist (subtasks), activity feed, labels, members, due date, location

## UI/UX

- Flat, light Trello look; labels colour-coded; dark mode as a theme
- Columns scroll horizontally, cards with drag-&-drop boundaries
- Responsive layout: sidebar collapsible, single-column on mobile devices

## Interactions

- **Drag & drop**: cards between columns/order; order persistent
- **Inline editing**: title directly on the card
- **Animations**: cards glide when reordering (subtle), modals fade in — corresponds to the documentation building blocks "drag", "cross-fade"
- **Right click on a card**: context menu (edit, copy, delete)

## Responsive design

| Width | Behaviour |
|-------|-----------|
| Desktop | sidebar + board |
| Tablet | collapsible sidebar |
| Mobile | board scrollable column-wise, bottom navigation |

## Accessibility

- DOM-based UI, keyboard navigation via Tab; drag & drop has no keyboard alternative (❌)
- Labels not only coloured but with text
- Screen readers: basic structure ok, modal focus management present
