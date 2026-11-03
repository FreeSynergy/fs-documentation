# Damselfly - Struktur und UI/UX

## Oberfläche

```
┌──────────────────────────────────────────────────────────────────────┐
│ 🔍 Suche (Text, "ähnlich wie…")   Filter ▾   Upload ⬆   Avatar/ Admin │
├──────────────┬───────────────────────────────────────────────────────┤
│ Ordnerbaum   │ Kachelraster (virtualisiert, Datum gruppiert)         │
│ ▸ 2026       │ ┌────┐┌────┐┌────┐┌────┐                              │
│ ▸ Urlaube    │ └────┘└────┘└────┘└────┘                              │
│ Label /      │ Auswahl: Checkboxen + Aktionsleiste                    │
│ Personen     ├───────────────────────────────────────────────────────┤
│              │ Detail-Drawer rechts: Vorschau, EXIF, Label, Personen │
└──────────────┴───────────────────────────────────────────────────────┘
```

- Viewer im Vollbild mit „ähnliche Bilder“-Streifen darunter
- Filterkapseln zeigen aktive Kriterien an und sind einzeln entfernbar

## UI/UX

- Helle, dichte Oberfläche mit Fokus auf Trefferlisten
- Statuszeile zeigt Index-Fortschritt (wartende Aufgaben)

## Interaktionen

- **Ähnlichkeitssuche**: „More like this“ öffnet neue Ergebnisliste
- **Person anklicken** → Personenansicht mit allen Treffern
- **Drag & Drop** auf Ordner = Upload in diesen Ordner
- **Animationen**: Skeleton-Kacheln, sanftes Nachladen

## Responsive Design

| Breite | Verhalten |
|--------|-----------|
| Desktop | Ordnerbaum + Raster + Detail-Drawer |
| Tablet | Ordnerbaum einklappbar, Drawer als Overlay |
| Mobil | Navigation als Drawer, 2 Spalten Raster |

## Accessibility

- Tastatur im Viewer und in Dialogen, Fokus-Sichtbarkeit in Kacheln
- Alt-Texte aus Labels, Beschriftungen statt reiner Symbole
- Screenreader: Statusmeldungen beim Indexieren

## Performance

- pgvector für Ähnlichkeitssuche, Watcher für inkrementelle Indexierung
- Vorschaustufen auf Anfrage generiert und gecacht
