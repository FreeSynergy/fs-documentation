# Morph - Aussehen

## Grundlayout

Ein Element behält seine Position und Fläche. Seine Kontur wandert ohne Sprung von einer Form zur nächsten.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│eckig         abgerundet    fast rund    Endform      │
│                                                      │
│+--------+  .--------.  ( -------- )  ( ........ )    │
│                                                      │
│Eckenradien und Pfade werden durchgehend interpoliert │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Icon-Morph** | zwei Icons werden zu einem durchgehenden Pfad |
| **Radius-Morph** | Rechteck ↔ Kreis über den Eckenradius |
| **Flächen-Morph** | ein kleines Element wächst zur Panel-Form (FAB) |
| **Farb-Morph** | die Füllung wechselt weich zusammen mit der Form |
| **Pfad-Morph** | freie SVG-Pfade mit einer Zuordnung von Stützpunkten |

## Dauer

- Typisch: 300–600 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Cross Fade](../cross-fade/description.md)
- [Elastic](../../feedback/elastic/description.md)
