# Jira - Struktur und UI/UX

## Seitenstruktur (Board)

```
┌─────────────────────────────────────────────────────────────────────┐
│ Jira   Suche…            Projekte Filter Dashboards ⚙   👤          │
├──────────┬──────────────────────────────────────────────────────────┤
│ WEB-Nav  │ Kanban-Board                                             │
│ Boards   │ ┌───────┬──────────┬───────────┬───────────┐             │
│ Backlog  │ │To Do  │In Progress│In Review │ Done      │             │
│ Reports  │ │WEB-14 │ WEB-12   │ WEB-13   │ WEB-9     │             │
│ …        │ │🐞 Bug │ 👤Anna   │          │           │             │
│          │ │SP 3   │          │          │           │             │
│          │ └───────┴──────────┴───────────┴───────────┘             │
│          │ Filter: assignee = currentUser()  [♻]                   │
└──────────┴──────────────────────────────────────────────────────────┘
```

- Issue-Detail als Full-Page oder Side-Panel; Felder links, Historie/Kommentare rechts

## UI/UX

- Atlassian-Design (Blau/Grau, Compass), hohe Dichte; Board-Filter oben
- Drag & Drop zwischen Spalten und im Backlog (Ranking)

## Interaktionen

- **Schnellerfassung** (`c`), Inline-Bearbeitung vieler Felder, Issue-Links per Typ
- Live-Boardaktualisierung für eingeloggte Teams (Commit-Autosync)

## Responsive Design

- Web responsiv mit Abstrichen; **Jira Mobile App** (iOS/Android) für Boards/Issues

## Accessibility

- Atlassian Accessibility (WCAG-Bemühungen dokumentiert); Kurzbefehle ersetzen Mäuseingaben (siehe [shortcuts.md](shortcuts.md))

## Performance

- Boards > 1k Issues: Spalten-/Query-Filter Pflicht; JQL mit `ORDER BY Rank` ist der Standardweg
