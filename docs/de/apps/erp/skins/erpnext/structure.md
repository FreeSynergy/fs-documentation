# ERPNext - Struktur und UI/UX

## Desk-Layout

```
┌──────────────────────────────────────────────────────────────────┐
│ ≡  🔍 Go to… (Ctrl+G)                         🔔 👤 Workspace ▾  │
├───────────┬──────────────────────────────────────────────────────┤
│ Workspaces│ Liste „Sales Orders“: Filter · ☑ Bulk-Actions        │
│ Selling   │  SO-2026-0042 | Kunde X | 12.400 € | ●Submitted     │
│ Stock     │  SO-2026-0043 | Kunde Y |  3.100 € | ○Draft         │
│ …         │ Form: Status-Kreispfad ●→○→○  Links (Delivery…)     │
│           │       Felder · Tags · Chatter (Comments/Timeline)    │
└───────────┴──────────────────────────────────────────────────────┘
```

- Status-Kreispfad zeigt Dokumentfluss (Draft→Submitted→Invoiced…); verlinkte Dokumente als Chips

## UI/UX

- Frappe-Desk-Look (Weiß/Grau, Blau-Akzente); Listen mit Listen-/Card-Ansicht
- Rechts-Drawer für Berichte/Charts aus Workspaces

## Interaktionen

- **Ctrl+G-Palette** als Haupteinstieg; Tags, Assign to Me, Bookmark an Formularen
- Value-Setter (Bulk-Änderung), Report-Builder per Klick

## Responsive Design

- Desktop-optimiert; Mobil über Browser brauchbar, keine natives App-Feeling

## Accessibility

- Standard-Web; Palette reduziert Suchklicks; Status immer beschriftet

## Performance

- Reports auf großen Tischen: Index/Query-Optimizer; Scheduler nicht mit Endbenutzern teilen (Worker trennen)
