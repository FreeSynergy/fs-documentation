# Trello - Struktur und UI/UX

## Seitenstruktur

```
┌──────────────────────────────────────────────────────────────────┐
│ ← Workspace      Board „Redaktion“         Mitglieder ☹☹☹  ☰ ⋮  │
├──────────┬───────────┬───────────┬───────────────────────────────┤
│ Ideen    │ In Arbeit │ Review    │ Fertig                        │
│ ┌──────┐ │ ┌──────┐  │ ┌──────┐  │ ┌──────┐                      │
│ │✎ Titel│ ││✎ Titel│  ││✎ Titel│  ││✓ Titel│                      │
│ │🏷🔴 📅│ ││🏷🟡 👤│  ││📅 über│  │└──────┘                       │
│ └──────┘ │ └──────┘  │ └──────┘  │                               │
│ [+ Karte]│           │           │                               │
└──────────┴───────────┴───────────┴───────────────────────────────┘
```

- Listen horizontal scrollbar; Karte als Overlay (Modal) mit Aktivitäten rechts

## UI/UX

- verspieltes Grunddesign (Hintergrundbilder, Kartenfarben) — absichtliche Leichtigkeit
- Karten-Vorschau zeigt Labels/Fälligkeit/Checklisten-Fortschritt

## Interaktionen

- **Drag & Drop** (Karte↔Liste, Liste↔Position), Long-Press auf Mobil
- Karten per `C` anlegen (siehe [shortcuts.md](shortcuts.md)), Checklisten einklappbar
- Live: Karten bewegen sich für alle Teilnehmenden fast zeitgleich

## Responsive Design

- Web responsiv; Mobile-App volle Funktion (Brett-Optik); Table-/Timeline-Ansichten desktoplastig

## Accessibility

- Tastatursteuerung gut abgedeckt (Shortcuts-Overlay `?`); Drag-Alternative: Karten-Menü „Verschieben“
- Labels immer mit Text, Farben zusätzlich codiert

## Performance

- Sehr große Boards (>500 Karten) bremsen Drag-Flüssigkeit; Listen archivieren hilft
