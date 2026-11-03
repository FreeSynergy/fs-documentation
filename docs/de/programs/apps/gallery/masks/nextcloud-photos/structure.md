# Nextcloud Photos - Struktur und UI/UX

## Oberfläche

```
┌──────────────────────────────────────────────────────────────────────┐
│ ☰ Apps   [Fotos]         🔍 Suche            Avatar ▾                 │
├──────────────────────────────────────────────────────────────────────┤
│ Unter-Leiste: Neueste | Alben | Ordner | Geteilt | Favoriten         │
│ Chronologie-Grid (spaltenfüllend, virtualisiert)                     │
│ ┌────┐┌────┐┌────┐┌────┐     Datumstrenner „Juni 2026“               │
│ └────┘└────┘└────┘└────┘                                             │
│ Viewer: großes Bild | Links/Rechts-Pfeile | Aktionen ⋮ (Teilen, …)   │
└──────────────────────────────────────────────────────────────────────┘
```

- Viewer teilt sich die Maske mit der Files-App (Vorschau-Overlay)
- Albenseite zeigt Cover-Kacheln, Bearbeiten nur für Besitzer

## UI/UX

- Nextcloud-Designsprache (Kopfzeile, blaue Akzentfarbe), Hell/Dunkel
- Actions-Menü ⋮ pro Bild/Album statt sichtbarer Buttons

## Interaktionen

- **Drag & Drop** von Dateien in die Chronologie (= Upload in Zielordner)
- **Teilen-Dialog** mit Link, Passwort, Ablauf, Upload-Erlaubnis
- **Mehrfachauswahl** über `Ctrl`/`Shift` + Klick im Files-View
- **Animationen**: Blending der Vorschaubilder, Spinner für Preview-Generierung

## Responsive Design

| Breite | Verhalten |
|--------|-----------|
| Desktop | App-Leiste + Unter-Leiste, Grid 5–8 Spalten |
| Tablet | App-Leiste als Iconleiste, 3–5 Spalten |
| Mobil | App-Wechsel über ☰, Grid 2–3 Spalten, Swipe im Viewer |

## Accessibility

- Tastaturnavigation im Viewer (`←`/`→`, `Esc`), Fokus-Ringe in Kacheln
- Alternativtexte aus Dateinamen/Metadaten, Menüpunkte mit Text
- Screenreader-Meldungen beim Nachladen der Chronologie

## Performance

- Vorschaubilder serverseitig generiert und gecacht (Redis/Files-Preview-Cache)
- Chronologie paginiert in Blöcken; große Ordner benötigen Preview-Scan im Hintergrund
