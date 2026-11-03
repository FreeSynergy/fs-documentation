# Odoo - Struktur und UI/UX

## Menübaum und Ansichten

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

- **Chatter** (Verlauf + Kommentare + Logging) ist das UI-Signaturelement an jeder Maske
- Phasen-Balken (Kanban-Status) oben in Formularen

## UI/UX

- Einheits-Framework (OWL): Form/List/Kanban überall identisch bedienbar
- Breadcrumbs + Favoriten; Dashboards als Pivot-/Graph-Kacheln

## Interaktionen

- Inline-Edit in Listen; One2many-Listen als Editierzeilen; „Compute“-Felder live
- Drag in Kanban-/Gantt-Ansichten; Bulk-Aktionen über ☑-Aktionenmenü

## Responsive Design

- Web responsive bis Tablet; **Odoo-App** (iOS/Android) für CRM/Lager/POS

## Accessibility

- Standard-Web-Komponenten; Palette `c` ersetzt Menüsuchen; Farbstatus immer mit Text

## Performance

- Compute-Felder sparsam designen (trigger-Kanäle); große Listen via „Load more“; Worker-Tuning bei RPC-Last
