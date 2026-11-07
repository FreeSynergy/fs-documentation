# Tryton - Structure and UI/UX

## Desktop client

```
┌──────────────────────────────────────────────────────────────────┐
│ Menü der Module ▾   „Sales“: Quotations ☐                         │
├──────────────┬───────────────────────────────────────────────────┤
│ Seitenbaum   │ Liste S/2026… | Party | Amount | State ▣           │
│ Account ▸    │ Form: State-Chips (draft/confirmed) · Felder      │
│ Sale ▸       │   Lines-Table · Related (Invoice/Move)             │
│ Stock ▸      │ Statusleiste: Speichern/Löschen/Persistieren      │
└──────────────┴───────────────────────────────────────────────────┘
```

- Tree on the left, list → double-click → form; buttons at the top; "Related" links between documents

## UI/UX

- Desktop-native consistency (GTK), shortcuts menu in every mask, quick start (`Ctrl+S` save)
- Forms with tabs; lists with column settings

## Interactions

- Selections (Many2One) with popup search + create; "Expand" buttons for related records
- Offline: desktop writes a server queue when connected

## Responsive design

not applicable (desktop/web UI separate)

## Accessibility

- GTK-based accessibility (screen reader fundamentals); consistency beats eye candy

## Performance

- Lists paginated server-side; partition large instances (periods)
