# uMap - Struktur und UI/UX

## Layout

```
┌──────────────────────────────────────────────────────────────────┐
│ uMap  Karte „Treffpunkte Nordring“    ⚙ (nur Bearbeiter)  👁/✎   │
├──────────┬───────────────────────────────────────────────────────┤
│ Ebenen   │        (OSM-Kacheln mit Markern/Clustern)             │
│ ▸Routes  │               ⬤  ⬤⬤                                   │
│ ▸Orte(12)│        Popup: Titel + Text + Bild, „Bearbeiten“      │
│ Filter…  │                                                       │
└──────────┴───────────────────────────────────────────────────────┘
Zoom +/− · Attributierung OSM
```

- Ebenenliste links (neuere uMap-Versionen: Blattleiste rechts unten), Popup-Dialog zentriert
- Bearbeiten-Modus färbt Werkzeuge ein; Lesemodus blendet sie aus

## UI/UX

- bewusst einfach: Symbole statt GIS-Terminologie („Marker“ statt „Feature“)
- Popup-Felder frei konfigurierbar (Eingabeformular je Ebene)

## Interaktionen

- **Klick auf Karte** = neues Element im aktiven Modus; Drag verschiebt
- Remote-Ebenen schreibgeschützt (Symbol), Import zeigt Vorschau

## Responsive Design

- Web responsiv; Mobil-Bearbeitung möglich, Komfort auf Desktop

## Accessibility

- Standard-Web (Leaflet); Popup-Inhalte HTML-barrierearm gestaltbar

## Performance

- tausende Marker → Clustering aktivieren; Remote-GeoJSON cachen
