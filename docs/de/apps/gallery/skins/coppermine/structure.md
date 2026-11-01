# Coppermine - Struktur und UI/UX

## Publikumsbereich (Standard-Theme)

```
┌──────────────────────────────────────────────────────────────────────┐
│ Galerie-Titel  Menü: Startseiten | Alben | Suche | Login             │
├───────────────┬──────────────────────────────────────────────────────┤
│ Seitenblock   │ Kategorie-/Albenübersicht mit Miniaturen             │
│ (Blöcke)      │ ┌────┐┌────┐┌────┐┌────┐                             │
│ letzte Uploads│ └────┘└────┘└────┘└────┘                             │
│ Bestseller    │ Albenkopf: Titel, Beschreibung, Bildzähler, Sort.    │
└───────────────┴──────────────────────────────────────────────────────┘
   Bildseite: Bild mittig | Dateinfo | Bewertung | Kommentare | Navigation
```

- Admin-Oberfläche „cuPCP“ ist ein separates Maskensystem mit Tab-Reitern
- Seitenränder bestehen aus Blöcken, die pro Theme placiert werden

## UI/UX

- Standard-Theme zweispaltig, ältere Themes mit fester Breite
- Aktionen als Textlinks unter Bild/Miniatur („rotate“, „edit“, „move“)

## Interaktionen

- **Batch-Verwaltung**: Checkboxen pro Miniatur → Aktionsleiste
- **Upload-Meister**: mehrstufiger Dialog (Album, Dateien, Beschreibung, Schlagwörter)
- **Bewertung**: Sterne direkt auf der Bildseite, Kommentarfeld darunter
- **Animationen**: kaum vorhanden, Lightbox-Plugins liefern Übergänge

## Responsive Design

| Breite | Verhalten |
|--------|-----------|
| Desktop | zweispaltig mit Blöcken |
| Tablet | Blöcke unterhalb der Galerie (je Theme) |
| Mobil | einspaltig nur mit responsivem Theme; Standard-Theme scrollt horizontal (⚠) |

## Accessibility

- Begrenzt: Bildalternativen aus Dateititeln, Skip-Links fehlen im Standard-Theme
- Formulare beschriftet, aber Tastaturführung in Batch-Masken schwach
- Nachrustbar über eigene Themes (empfohlener Weg in Skin-Projekten)

## Performance

- Vorschaugrößen werden beim Upload erzeugt; Neubauen per Wartungsfunktion
- Kein eingebauter Seiten-Cache; Caching über Webserver/Proxy erforderlich
