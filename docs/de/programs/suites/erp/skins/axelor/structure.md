# Axelor - Struktur und UI/UX

## UI-Layout

```
┌──────────────────────────────────────────────────────────────────┐
│ Axelor  Menüs ▾  Suche……                        🔔 🌐 👤         │
├──────────────────────────────────────────────────────────────────┤
│ Grid „Sale Orders“: Spalten sortierbar, ☑ Massenaktionen         │
│ Form „SO-2026-0012“: Status-Timeline (draft→confirmed→invoiced)  │
│   Feldgruppen · Panels (Linien, Calculi) · BPM-Aufgabenliste     │
│ Dashboards: KPI-Karten + Charts aus Builder-Konfiguration        │
└──────────────────────────────────────────────────────────────────┘
```

- Master-View (Grid) + Detail-Form mit „workflow bar“; Kanban/Calendar als alternative Views

## UI/UX

- technisch-nüchtern; Builder-Begriffe (Model/Action/View) tauchen in der UI auf
- BPM-Aufgaben als „Wartend auf…“-Banner

## Interaktionen

- Reiter-Forms, One2many-Editierung, Mass-update-Aktionen
- Workflow-Buttons (draft/confirm…) je BPM-Zustand sichtbar

## Responsive Design

- Web responsive; Mobile für Zustimmung/Aufgaben brauchbar

## Accessibility

- Standard-Web; Grid-Tastaturnavigation elementar

## Performance

- große Grids serverseitig paginiert; BPM-Instanzen sauber halten (Archive)
