# Immich - Struktur und UI/UX

## Zeitleiste

```
┌──────────────────────────────────────────────────────────────────────┐
│ Navigation  │ Suche (🔍 semantisch)     │ Upload ⬆  │ Avatar         │
│ Fotos       ├───────────────────────────┴────────────────────────────┤
│ Alben       │ 2026  ▾   [Jahr][Monat][Alle]                          │
│ Durchsuchen │ ┌──┐┌──┐┌──┐┌──┐┌──┐┌──┐   virtuelles Raster           │
│ Favoriten   │ └──┘└──┘└──┘└──┘└──┘└──┘   (Lazy-Load, Dateigruppen)   │
│ Geteilt     │ Auswahl-Werkzeugleiste erscheint oben                  │
│ Mülleimer   │ ▣ Auswahl  ♥  ⤓  🗑  ⑂ Share                              │
└─────────────┴────────────────────────────────────────────────────────┘
```

- Viewer: Vollbild mit linker Miniaturleiste, EXIF-Panel rechts, Video mit Timeline
- Auswahlmodus: Klick + `Shift` für Bereich, Werkzeugleiste mit Massenaktionen

## UI/UX

- Dunkles und helles Theme, Akzentfarbe, Touch-Wischgesten im Viewer
- Virtuelles Raster hält große Bibliotheken (100k+ Aufnahmen) flüssig
- Upload-Overlay mit Fortschritt und Duplicate-Warnung

## Interaktionen

- **Drag & Drop**: Dateien direkt in die Zeitleiste ziehen
- **Persona-Suche**: Klick auf Gesicht öffnet Personen-Seite mit deren Zeitleiste
- **Album-Teilen**: Dialog mit Benutzerauswahl oder Link (Passwort/Ablauf optional)
- **Animationen**: Fade-in der Miniaturen, Skeleton-Plätze beim Laden

## Responsive Design

| Breite | Verhalten |
|--------|-----------|
| Desktop | Navigationsleiste + mehrspaltiges Raster |
| Tablet | Navigationsleiste einklappbar, Raster 3–4 Spalten |
| Mobil | untere Tab-Leiste, Raster 2–3 Spalten, Swipe-Viewer |

## Accessibility

- Tastatursteuerung im Viewer (Pfeile, `Esc`), Fokus-Ringe im Raster
- Alternativtexte aus ML-Beschlagwortung nachrüstbar, Screenreader-Labels in Dialogen
- Farbige Zustände zusätzlich beschriftet (Favorit = Symbol + Text)

## Performance

- Derivate (Thumbnail/Preview/Webp) serverseitig, Client lädt maßrichtige Variante
- Jobs laufen asynchron; Suche über PostgreSQL-Volltext + pgvector/CLIP-Embeddings
