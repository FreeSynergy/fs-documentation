# Taiga - Struktur und UI/UX

## Seitenstruktur

```
┌─────────────────────────────────────────────────────────────────┐
│ Projekt „API-Umbau“   Backlog Kanban Issues Sprints Epics Wiki  │
├─────────────────────────────────────────────────────────────────┤
│ Backlog (Scrum)                                                  │
│ US#12 Login-Session  | Points: 3 | Sprint #4 👤Anna             │
│ US#13 Token-Refresh  | Points: 5 | —        👤Ben  [drag]       │
│ ── Sprint #4 ────────────────────────────────── (8/13 Punkte)   │
│ US#11 Logout-Ecke    | Points: 2 | ✔                            │
└─────────────────────────────────────────────────────────────────┘
Detail-Panel rechts (US#12): Beschreibung, Anhang, History,
Subtasks, Reviewer-Kommentare
```

- Kopfzeile = Modulreiter; Tafeln mit Spalten; Drag-Interaction überall zentral

## UI/UX

- Taiga-typisch: Weiß/Grün-Akzente, Karten mit Punkt- und Status-Badges
- Filterchips über Tafeln; Bulk-Edit über Checkboxen

## Interaktionen

- **Drag & Drop**: Stories zwischen Sprints/Spalten, Subtask-Reihenfolge
- Inline-Picker für Status/Points; Quick-Add-Zeile am Listenende
- Live-Aktualisierungen über WebSocket-Kanal (Events-Service)

## Responsive Design

- Web gut responsiv; Tafeln auf Mobil scrollbar; keine natives App-Feeling

## Accessibility

- Standard-Web-Zugänglichkeit; Drag-Alternativen: Sprint-/Status-Auswahl im Panel
- Farbstatus zusätzlich beschriftet

## Performance

- Backlogs > 1.000 Stories: Filter nutzen; Events-Service hält Last niedrig
