# Monica - Structure and UI/UX

## Page structure

```
┌───────────────────────────────────────────────────────────────────┐
│ Monica  [Dashboard][Contacts][Activities][Tasks][Gifts][Settings] │
├──────────────────────────┬────────────────────────────────────────┤
│ Contact list (left)      │ Contact page                           │
│ 🔍 Search…                │ ┌──────────────────────────────────┐   │
│ ○ Andrea Berg ★          │ │ [Photo] Andrea Berg   ⋯          │   │
│ ○ Ben Klein              │ │ Partner · Berlin · 41            │   │
│ ○ Beta GmbH              │ │ ────────────────────────────────  │  │
│ + Contact                │ │ Tabs: About | Activities |       │   │
│                          │ │ Tasks | Relationships | Gifts    │   │
│                          │ │ ────────────────────────────────  │  │
│                          │ │ Timeline: 03.11 Hike (⛰)       │     │
│                          │ │           12.10 Call (10 min)  │     │
│                          │ └──────────────────────────────────┘   │
└──────────────────────────┴────────────────────────────────────────┘
```

- Contact page = tabs with a timeline; the "Add activity" form is always present
- The dashboard shows birthdays, outstanding tasks, "people important to you"

## UI/UX

- Calm card look, accent colour blue; light/dark theme (newer versions)
- Masks follow the Laravel standard forms, editable inline, many "+" buttons

## Interactions

- **Quick capture**: activities straight from the dashboard ("What did you do?")
- **Drag & drop**: ❌ not present
- **Animations**: subtle fade transitions of the tabs; timeline entries fade in

## Responsive design

| Width | Behaviour |
|-------|-----------|
| Desktop | Two columns + tabs |
| Tablet/mobile | Single column, navigation as a dropdown |

## Accessibility

- HTML forms/tables, keyboard tabbing is fine, labels are present
- Timeline as a list with dates — screen-reader friendly
- The colour accent is additionally marked in text (star, type names)

## Performance

- Instances with more than 50k activities stay fast (paginated timeline); schedule cron runs for the reminders
