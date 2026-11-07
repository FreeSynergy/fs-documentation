# OPNsense - Structure & UI/UX

## Overview

After sign-in, OPNsense shows the dashboard; above it lies the horizontal menu bar. Each page is a "Page" made of a form panel or grid table, with an apply bar added on firewall pages. Overlays (edit dialogues, status messages) appear centred or as a toast at the top right. The state "unsaved/unapplied changes" is always visible.

## Window structure

### Firewall rule page (example)

```
┌──────────────────────────────────────────────────────────────────────┐
│ 🏠 | Interfaces | Firewall | VPN | Services | System      [Admin ▾]  │
├──────────┬───────────────────────────────────────────────────────────┤
│ Firewall │ Firewall: Rules: LAN     [+ Add] [⚙ Columns] [Apply]     │
│ ▸ Rules  │ ┌───────────────────────────────────────────────────────┐ │
│ ▸ NAT    │ │ ⋮ # │Proto│Source     │Dest      │Port │Desc │[⋮]    │ │
│ ▸ Aliases│ │   1 │ TCP │ lan_net   │ wan      │ 443 │ https│ ⋮    │ │
│ ▸ Settin.│ │   2 │ ANY │ alias_geo │ lan_srv  │ *   │ lab  │ ⋮    │ │
│          │ ├───────────────────────────────────────────────────────┤ │
│          │ │ search [_________]   rows 25  « 1 2 3 »               │ │
│          │ └───────────────────────────────────────────────────────┘ │
└──────────┴───────────────────────────────────────────────────────────┘
```

### Edit dialogue (rule/alias)

```
┌──────────────────────────────────────────┐
│  Edit: Firewall Rule             [X]     │
├──────────────────────────────────────────┤
│  (General) (Advanced) (Description)      │ ← section accordion
│  Action [Pass ▾]  Protocol [TCP ▾]       │
│  Source [network|alias]  [________]      │
├──────────────────────────────────────────┤
│           [Cancel]        [Save]         │
└──────────────────────────────────────────┘
```

### Apply state

```
┌────────────────────────────────────────────────────────┐
│ ⚠ Changes have been made that require apply.  [Apply]  │
└────────────────────────────────────────────────────────┘
```

## Areas

| Area | Position | Content |
|---------|----------|--------|
| Top menu | Top | Dashboard, Interfaces, Firewall, VPN, Services, System |
| Submenu/left | Below menu | Sub-items of the selected top menu (extensible via plugins) |
| Page header | Top of content | Title, add buttons, column menu, apply button (firewall) |
| Grid | Centre of content | Tables with search, pagination, `⋮` row menus |
| Form panels | Content | Accordions ("General", "Advanced") with Save/Revert |
| Toasts | Top right | Success/error/action results |
| User menu | Top right | Sign out, theme, session info |

## UI/UX

### Design principles

- **Save ≠ Apply**: editing and activating are deliberately separated (rule set integrity)
- **Grids for volume**: rules/aliases/logs as searchable tables, never as a wall of lists
- **Accordion forms**: rarely used options hidden under "Advanced"
- **Consistent controller patterns**: same dialogue structure across almost all pages (MVC framework)

### Colour scheme and themes

- Light/dark via theme selection (user menu, version-dependent); system and plugin pages partly follow their own themes
- Status: green = active/allowed, red = blocked/error, orange = warning/pending apply
- Minimal decoration – information density before colour

### Interactions

- **Rule order**: drag and drop on arrow handles, order = processing sequence
- **Grid search**: live against the server (`searchPhrase`), pagination server-side
- **Copy/move**: duplicate rules/aliases via `⋮` menus
- **Toasts and progress**: longer actions (apply, feeds) show status messages
- **Autocomplete**: interface/alias selection lists in rule dialogues
- **Type-ahead selects**: selection fields filter while typing (large alias/certificate lists)
- **Login page**: form with optional 2FA prompt; errors appear inline

### Responsive design

- **Desktop**: full layout; submenu permanently on the left
- **Narrow windows**: menu collapses into a hamburger, grids scroll horizontally
- **Mobile**: core pages usable, dense rule grids remain a compromise (version-dependent)
- **No offline mode**: without UI access, the console/CLI remains

### Accessibility

- **Keyboard**: forms/dialogues via `Tab`/`Enter`, accordion headers focusable; grid row menus reachable via `Tab`
- **Screen reader**: dialogues with heading/ARIA; grid headers linked, but dynamic parts are mediocre depending on version
- **Focus indicator**: visible; dialogues trap focus
- **Language**: UI in many languages (German translation almost complete, version-dependent)

### Performance

- **Server-side grids**: large rule sets stay fast; every search is an API-like request
- **Dashboard polling**: widgets load at intervals; too many widgets lengthen loading time
- **Apply phases**: loading pf rules can take noticeable time with huge alias feeds – the toast shows progress
- **Recommendation**: maintain feed aliases with "wide"/duplicate clean-up, filter log grids by time

## See also

- [menu.md](menus.md) - Menu paths and roles
- [features.md](features.md) - Feature areas
- [shortcuts.md](shortcuts.md) - Keyboard operation
- [api.md](api.md) - MVC API behind every page
