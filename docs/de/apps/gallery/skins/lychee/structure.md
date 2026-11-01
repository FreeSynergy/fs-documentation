# Lychee - Struktur und UI/UX

## Oberfläche

```
┌──────────────────────────────────────────────────────────────────────┐
│ ☰ Alben  🔍 Suche   ⬆ Neu            Favoriten  Teilen  Avatar       │
├──────────────────────────────────────────────────────────────────────┤
│ Album-Kacheln (Cover + Titel + Anzahl)                               │
│ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐                          │
│ └────────┘ └────────┘ └────────┘ └────────┘                          │
│ Album-Ansicht: Raster der Aufnahmen, Kopfzeile mit Album-Aktionen ⋮  │
│ Lightbox: großes Bild | links/rechts Navigation | EXIF-Overlay (i)   │
└──────────────────────────────────────────────────────────────────────┘
```

- Verschachtelte Alben als eigene Ebene, Back-Button oben links
- Auswahlmodus mit Checkboxen und Sammelaktionen

## UI/UX

- Reduzierte, dunkle Standardoberfläche, Fokus auf Bildflächen
- Kontextmenü pro Album/Aufnahme über ⋮ bzw. Rechtsklick

## Interaktionen

- **Drag & Drop**: Dateien direkt ins Album, Fortschrittsstreifen
- **Rechtsklick**: Album-/Foto-Aktionen
- **Teilen-Dialog**: Link mit Parameterleiste (Passwort, Ablauf, Rechte)
- **Animationen**: Blending beim Öffnen, sanftes Lazy-Load

## Responsive Design

| Breite | Verhalten |
|--------|-----------|
| Desktop | Kacheln 4–6 Spalten, Lightbox mit Seitenleisten |
| Tablet | 3 Spalten, Bedienung über ⋮ |
| Mobil | 2 Spalten, Lightbox randlos, Wischgesten |

## Accessibility

- Tastaturnavigation in Lightbox (`←`/`→`, `Esc`, `i`)
- Alt-Texte aus Titeln/Beschreibungen, Fokus-Ringe in Kacheln
- Aktionen zusätzlich mit Text in Menüs

## Performance

- Mehrere Vorschaugrößen, Client wählt passende Stufe
- Alben werden paginiert geladen; große Alben bleiben flüssig
