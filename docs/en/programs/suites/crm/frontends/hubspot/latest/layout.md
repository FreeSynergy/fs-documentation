# HubSpot - Structure and UI/UX

## Page structure

```
┌───────────────────────────────────────────────────────────────────┐
│ [CRM|Marketing|Sales|Service|⚙]   🔍 Search            [🔔][👤]    │
├───────────────────────────────────────────────────────────────────┤
│ Contacts  [Filter ▾][+ Create contact][Import]                    │
│ ☐ Andrea Berg   Company: Beta   Lifecycle: Customer  🕐 2 d       │
│ ☐ Ben Klein     …                                                │
├───────────────────────────────────────────────────────────────────┤
│ Contact page: Andrea Berg   [Email][Call][Task][+]                │
│ Left: properties · Right: timeline | Email | Engagements          │
└───────────────────────────────────────────────────────────────────┘
```

- Uniform card masks; the hub switcher at the top switches work areas

## UI/UX

- Friendly orange/white design, high consistency between hubs
- Lists with saved views; kanban deals with drag

## Interactions

- **Drag & drop**: deal cards in the pipeline, forms in the page editor
- **Embedded panels**: email preview, calendar, call player inline
- Partly live updates (engagement history)

## Responsive design

- Web app well responsive; **HubSpot mobile app** (iOS/Android) as a full client, incl. offline notes

## Accessibility

- HubSpot publishes VPAT/WCAG reports; standard masks are screen-reader friendly
- Keyboard: `Cmd/Ctrl+K` quick find (in many views), otherwise Tab navigation

## Performance

- Client-side, SPA-like; large portals (> 1M contacts) come with segment performance notes
