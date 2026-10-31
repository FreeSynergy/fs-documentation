# Progress - Aussehen

## Grundlayout

Eine Schiene, deren gefüllter Bereich mit dem Fortschritt von links nach rechts (beim Ring im Uhrzeigersinn) mitwächst.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│0 %          25 %          50 %          100 %        │
│                                                      │
│[--------]   [###------]   [######---]   [########]   │
│                                                      │
│unbestimmt:  [~~>~~~~]   [~~~>~~~]   Segment pendelt  │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Balken** | klassische horizontale Füllung mit Prozentwert |
| **Ring** | kreisförmiger Fortschritt, z. B. in runden Icons |
| **Segmente** | diskrete Schritte (1/5, 2/5 …) für Assistenten |
| **Unbestimmt** | wanderndes Segment, wenn die Zielgröße unbekannt ist |
| **Kompakt** | dünner Balken am Seitenrand (z. B. Lesefortschritt) |

## Dauer

- Typisch: 200–500 ms pro Wertänderung, Loop 1000–1500 ms

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Skeleton](../skeleton/description.md)
- [Typing](../typing/description.md)
