# Zammad - Struktur und UI/UX

## Ticketmaske

```
┌──────────────────────────────────────────────────────────────────────┐
│ Symboleiste │ Filter/Links        │ Ticket #1231 „Drucker offline“ ⋮ │
│ ▦ 🎫 👥 📚 ⚙│ Gespeicherte Filter ├──────────┬───────────────────────┤
│             │ Offene Tickets      │ Artikel  │ Attribute             │
│             │ Überfällige         │ ┌──────┐ │ Status: open          │
│             │ Geteilte            │ │Kunde │ │ Eigentümer: Anna      │
│             │                     │ │"Neu… │ │ Gruppe: Support       │
│             │                     │ └──────┘ │ Priority: hoch        │
│             │                     │ Antwort- │ Tags: drucker, hw     │
│             │                     │ editor   │ Kunde: Beta GmbH      │
│             │                     │ [📎 😃 ✉→]│ Org: Beta GmbH        │
└───────────────────────────────────┴──────────┴───────────────────────┘
```

- Mitte: Chronologie aus Kundenartikeln und Notizen, Antworteditor unten
- Rechts: Attribute und Historie, links: Filternavigation

## UI/UX

- Zammad-„Kachel“-Design, Hell/Dunkel-Themes, Akzentfarben adminwählbar
- Volltextsuche (⌕) öffnet Overlay mit Live-Treffern
- Drag & Drop: Anhänge in den Editor, Filter links per Klick

## Interaktionen

- **Massenauswahl**: Checkboxen links → „Bearbeitungsmaske“ mit State/Owner/Tags-Aktionen
- **Textbaustein-Picker**: `#` im Editor öffnet die Bausteinliste
- **Zahlen-Overlay**: SLU-Ticker oben rechts zeigt anstehende Fristen
- **Animationen**: Artikel blenden ein; Live-Aktualisierungen per WebSocket ohne Reload

## Responsive Design

| Breite | Verhalten |
|--------|-----------|
| Desktop | Drei-Spalten |
| Tablet | Attribute als aufklappbares Panel |
| Mobil | einspaltig, Navigation als Drawer |

## Accessibility

- Tastatur-Palette (`Ctrl+Shift+K`) für Navigation/Aktionen
- Editor mit Standard-Tastatur-/Screenreader-Support; Live-Regionen für neue Artikel
- Farbstatus zusätzlich mit Text (open/…, closed)

## Performance

- Elasticsearch hält Suche < 1 s bei > 1 Mio. Artikeln; WebSocket-Kanal hält Masken aktuell
