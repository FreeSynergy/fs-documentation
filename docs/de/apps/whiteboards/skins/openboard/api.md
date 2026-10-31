# OpenBoard - API Dokumentation

## Übersicht

OpenBoard hat **keine API**. Der Austauschweg ist das Dateiformat: `.obz`-Archive (ZIP) mit SVG-Seiten und Metadaten — damit sind Konverter/Automationen außerhalb des Programms möglich.

**API-Arten im Überblick**

| Art | Verwendung | Status |
|-----|------------|--------|
| `.obz`-Dateiformat | Export/Import, Konvertierung | offiziell (Struktur stabil, schwach dokumentiert) |
| PDF-Export | Präsentation/Archiv | offiziell |
| REST/WebSocket | — | ❌ |
| Webhooks | — | ❌ |

## `.obz`-Aufbau (praktisch)

```
dokument.obz (ZIP)
├── document.svg / metadata    (Seitenreferenzen, Titel, Ersteller)
├── page-1.svg …               (Vektorelemente je Seite)
└── media/                     (eingebettete Bilder/PDFs)
```

Werkzeuge: unzip → SVG verarbeiten (Inkscape, `rsvg-convert`, eigene Parser) → repacken.

## Beispiel: PDF-Kette

```bash
unzip retro.obz -d retro/
rsvg-convert -f pdf -o seite-1.pdf retro/page-1.svg
```

## Skin-Hinweis

Ein „OpenBoard-Skin“ in FreeSynergy baut die Tafel-UI (Seite/Element) nach und tauscht `.obz`/SVG — Modell: [Whiteboard-Elemente](../../../../data/modelle.md) seitenbasiert statt Canvas-Records.
