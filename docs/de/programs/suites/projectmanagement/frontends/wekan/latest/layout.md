# Wekan - Struktur und UI/UX

## Seitenstruktur

```
┌───────────────────────────────────────────────────────────────────┐
│ Organisation ▾   Board „Sprinttafel“          Mitglieder  ⋮  ☰   │
├───────────────────────────────────────────────────────────────────┤
│ Swimlane „Q4“                                                    │
│  ┌─ To Do ──┬─ Doing ──┬─ Done ─┐                                │
│  │ Karte A🏷│ Karte C  │        │                                │
│  └──────────┴──────────┴────────┘                                │
│ Swimlane „Backlog“                                               │
│  ┌─ To Do ─────────────┐                                         │
│  │ Karte B 📅11.11 👤  │                                         │
│  └─────────────────────┘                                         │
├───────────────────────────────────────────────────────────────────┤
│ Karte „B“: Beschreibung · Checkliste · Labels · Custom Fields     │
└───────────────────────────────────────────────────────────────────┘
```

- Swimlane-Überschriften als Querstreifen; Karten-Modal zentriert, Aktivitäten rechts

## UI/UX

- funktional, dichter als Trello; Swimlanen horizontal scrollbar
- Farbaccent pro Swimlane/Label

## Interaktionen

- **Drag & Drop** Karten zwischen Listen/Swimlanen; Checkbox-Massenaktion eingeschränkt
- Echtzeit: Meteor-Sync, Karten bewegen sich live für alle
- Quick-Cards-Editor (Titel + Enter)

## Responsive Design

- Desktop-optimiert; Mobil bedingtes Scrolling (kein eigenes Layout-Konzept)

## Accessibility

- Tastaturtabellen für Formulare; Drag ohne Tastaturalternative (Kartenmenü „Verschieben“ als Ersatz)

## Performance

- sehr große Boards (>2k Karten) bremsen; Swimlanen-/Listenarchiv empfohlen
