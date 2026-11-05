# GNOME Contacts - Structure and UI/UX

## Window structure

```
┌────────────────────────────────────────────────────────┐
│ ⌕ Search…           GNOME Contacts            ⋮        │  (HeaderBar)
├───────────────────────────┬────────────────────────────┤
│ Contact cards (list)      │ Contact card (detail)      │
│ ┌──────────┐ ┌──────────┐ │ ┌────────────────────────┐ │
│ │[F] Andrea│ │[F] Ben   │ │ │ [Photo] Andrea Berg    │ │
│ │ Andrea   │ │ Ben      │ │ │ 📧 a@… ✎ ☎ +49… ✎      │ │
│ └──────────┘ └──────────┘ │ │ ✚ Field · Source: Pers.│ │
│ …                         │ │ [Edit]                 │ │
│                           │ └────────────────────────┘ │
└───────────────────────────┴────────────────────────────┘
```

- Grid of contact cards; the detail on the right as an overlaying panel (the "Edit" toggle)
- The HeaderBar contains search, "New Contact", menu ⋮

## UI/UX

- libadwaita design: round cards, clear typography, light/dark following the system
- Very few visible controls — mode switch "view ⇄ edit"

## Interactions

- **Quick editing**: in edit mode all fields are inline; `Tab` jumps onward
- **Add field**: "+" menu with category submenus (phone types, address types)
- **Link cards**: select two contacts → "Merge"
- **Animations**: card transitions (libadwaita standard fades)

## Responsive design

| Width | Behaviour |
|-------|-----------|
| Desktop | Grid + detail next to it |
| Mobile (GNOME Mobile/Phone) | Single column, detail as push navigation |

## Accessibility

- GTK4/ATK: full keyboard navigation, screen-reader labels, focus visibility
- Keyboard shortcuts see [shortcuts.md](shortcuts.md)

## Performance

- EDS cache: thousands of contacts run smoothly; LDAP sources with a slow server slow the search down
