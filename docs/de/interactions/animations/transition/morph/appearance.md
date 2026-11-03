# Morph - Aussehen

## Grundlayout

Ein Element behält Position und Fläche; seine Kontur wandert ohne Sprung von einer Form zur nächsten.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│eckig         abgerundet    fast rund     Endform     │
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
| **Flächen-Morph** | kleines Element wächst zur Panel-Form (FAB) |
| **Farb-Morph** | Füllung wechselt weich mit der Form |
| **Pfad-Morph** | freie SVG-Pfade mit Stützpunkt-Zuordnung |

## Dauer

- Typisch: 300–600 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Cross Fade](../cross-fade/description.md)
- [Elastic](../../feedback/elastic/description.md)
