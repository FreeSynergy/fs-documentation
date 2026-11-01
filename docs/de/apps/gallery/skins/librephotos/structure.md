# LibrePhotos - Struktur und UI/UX

## Oberfläche

```
┌──────────────────────────────────────────────────────────────────────┐
│ Suche 🔍 (semantisch)            Filter ⚙   Upload ⬆    Avatar       │
├───────────┬──────────────────────────────────────────────────────────┤
│ Navigation│  Zeitleiste gruppiert nach Datum                         │
│ Suche     │  12. Juni 2026  ┌──┐┌──┐┌──┐┌──┐                         │
│ Orte      │                 └──┘└──┘└──┘└──┘                         │
│ Alben     │  11. Juni 2026  ┌──┐┌──┐                                 │
│ Menschen  │                 └──┘└──┘                                 │
│ Gelöscht  ├──────────────────────────────────────────────────────────┤
│           │  Viewer / Seitenleiste: EXIF, Personen, ähnliche Bilder  │
└───────────┴──────────────────────────────────────────────────────────┘
```

- Suche-Overlay kombiniert Text, Datumsbereich, Personen und Orte
- Viewer mit Linksnavigation, EXIF rechts, „ähnliche“ darunter

## UI/UX

- Material-artige Oberfläche, Hell/Dunkel, feste Sidebar (einklappbar)
- Grouping-Regler für Zeitleiste (Tag/Monat/Jahr)

## Interaktionen

- **Shift+Klick** für Bereichsauswahl, Werkzeugleiste erscheint oben
- **Gesicht anklicken** → Personenseite mit Zeitleiste der Person
- **Teilen-Dialog** mit Benutzer- oder Linkfreigabe
- **Animationen**: Skeleton-Kacheln, sanftes Nachladen beim Scrollen

## Responsive Design

| Breite | Verhalten |
|--------|-----------|
| Desktop | Sidebar + 4–6 Spalten Raster |
| Tablet | Sidebar als Drawer, 3–4 Spalten |
| Mobil | Tab-Leiste unten, 2–3 Spalten, Swipe-Viewer |

## Accessibility

- Tastatur im Viewer (`Esc`, Pfeile), Fokus-Ringe in Kacheln
- Alternativtexte aus Objekterkennung nachrüstbar
- Symbole mit Beschriftung in der Navigationsleiste

## Performance

- Scan-Pipeline asynchron (Celery), Suche über Datenbank + Vektoren
- Miniaturstufen auf Platte; große Bibliotheken benötigen ausreichend CPU für den Erstdurchlauf
