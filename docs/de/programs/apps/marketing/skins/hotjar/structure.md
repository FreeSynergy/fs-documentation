# Hotjar - Struktur und UI/UX

## Layout

```
Site-Auswahl ▾   Zeitraum ▾
├ Heatmaps:     Seiten-Overlay (rot=heiß) über DOM-Screenshot,
│               device-Umschalter (Desktop/Mobil), Klick-Liste
├ Recordings:   Tabellenliste (Thumbnail, Seitenzahl, Dauer,
│               Rage-Click-Badge) → Player (Timeline, Mauspfad,
│               DOM-Rekonstruktion, Maskierte Felder „•••“)
├ Surveys:      Frage-Editor links, Vorschau-Telefon rechts
└ Ziel-Funnel:  Stufenbalken mit Abbruchquoten
```

## UI/UX

- visuell-ledigich: Overlays/Thumbnails statt Zahlenkolonnen
- Geführte Anlage („Welche Seite? Welcher Zeitraum?“)

## Interaktionen

- Heatmap-Ebenen umschalten (Klick/Move/Scroll)
- Replay-Player: Play/Pause, Geschwindigkeit, Mausspur ein/aus

## Responsive Design

- Web-Dashboard responsiv; Aufnahmen je Device-Typ getrennt

## Accessibility

- Standard-Web; Videos/Overlays nicht barrierefrei ersetzbar (Berichte als Textexport)

## Performance

- Aufnahme-Sampling begrenzt Datenvolumen; Player lädt DOM-Schnipsel nach
