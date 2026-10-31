# Planka - Struktur und UI/UX

## Seitenstruktur

```
┌──────────────────────────────────────────────────────────────────┐
│ Planka   [Projektname ▾]        🔍 Suche    👤 Benutzer   ⚙ Admin │
├──────────────┬───────────────────────────────────────────────────┤
│ Projekt-     │  Board-Ansicht (Spalten)                          │
│ seitenleiste │  ┌──────────┬──────────┬──────────┐               │
│ 🏠 Board     │  │ To Do    │ In Perf. │ Done     │               │
│ 📋 Projekte  │  │ ┌──────┐ │ ┌──────┐ │ ┌──────┐ │               │
│ 🏷 Labels    │  │ │Task A│ │ │Task C│ │ │Task E│ │               │
│ 👥 Mitglieder│  │ └──────┘ │ └──────┘ │ └──────┘ │               │
│ 📅 Kalender  │  │ ┌──────┐ │          │          │               │
│ ⚙ Einstellungen│ │ │Task B│ │          │          │               │
│              │  │ └──────┘ │          │          │               │
│ + Projekt    │  └──────────┴──────────┴──────────┘               │
└──────────────┴───────────────────────────────────────────────────┘
```

- Aufgabenkarten zeigen Titel, Labels (farbig), Fälligkeit, Bearbeiter-Avatare, Kommentare-/Unteraufgaben-Zähler
- Task-Detail als Modal: Beschreibung, Checkliste (Unteraufgaben), Activity-Feed, Labels, Mitglieder, Fälligkeit, Ablageort

## UI/UX

- Flache, helle Trello-Optik; Labels farbcodiert; Dark-Mode als Theme
- Spalten horizontal scrollbar, Karten mit Drag-&-Drop-Grenzen
- Responsives Layout: Seitenleiste einklappbar, auf Mobilgerains einspaltig

## Interaktionen

- **Drag & Drop**: Karten zwischen Spalten/Reihenfolge; Reihenfolge persistent
- **Inline-Bearbeitung**: Titel direkt auf der Karte
- **Animationen**: Karten gleiten beim Umsortieren (dezent), Modale blenden ein — entspricht den Doku-Bausteinen „Drag", „Cross-fade"
- **Rechtsklick auf Karte**: Kontextmenü (Bearbeiten, Kopieren, Löschen)

## Responsive Design

| Breite | Verhalten |
|--------|-----------|
| Desktop | Seitenleiste + Board |
| Tablet | einklappbare Seitenleiste |
| Mobil | Board spaltenweise scrollbar, Bottom-Navigation |

## Accessibility

- DOM-basierte Oberfläche, Tastatur-Navigation über Tab; Drag&Drop hat keine Tastatur-Alternative (❌)
- Labels nicht nur farbig, sondern mit Text
- Screenreader: Grundstruktur ok, Modal-Fokusverwaltung vorhanden
