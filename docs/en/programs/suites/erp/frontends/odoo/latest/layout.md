# Odoo - Structure and UI/UX

## Menu tree and views

```
┌──────────────────────────────────────────────────────────────────┐
│ ▦ Apps ▾   Verkäufe            🔍 /c-Befehle…        ⚙ 👤        │
├──────────────────────────────────────────────────────────────────┤
│ Ansichten: ▦ Kanban | ☰ Liste | 🗓 Kalender | ⛓ Gantt            │
│ Kanban „Angebote“:  S/2026/0042          S/2026/0043             │
│   Kunde X 12.400 €  [Phase: Quotation→Sent]                      │
│ Liste: ☑ | Referenz | Kunde | Datum | Gesamt                     │
│ Form: Kopf (Status-Chips) · Reiter · Notiz · Chatter rechts    │
└──────────────────────────────────────────────────────────────────┘
```

- The **chatter** (history + comments + logging) is the signature UI element on every form
- Stage bar (kanban status) at the top of forms

## UI/UX

- Unified framework (OWL): form/list/kanban operate identically everywhere
- Breadcrumbs + favourites; dashboards as pivot/graph tiles

## Interactions

- Inline editing in lists; One2many lists as editable rows; "compute" fields live
- Drag in kanban/Gantt views; bulk actions via the ☑ actions menu

## Responsive design

- Web responsive down to tablet; **Odoo app** (iOS/Android) for CRM/warehouse/POS

## Accessibility

- Standard web components; the `c` palette replaces menu searches; colour status always with text

## Performance

- Design compute fields sparingly (trigger channels); large lists via "Load more"; worker tuning under RPC load
