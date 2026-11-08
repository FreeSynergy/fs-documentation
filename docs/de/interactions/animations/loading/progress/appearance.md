# Progress - Aussehen

## Grundlayout

Eine Leiste, deren gefüllter Bereich mit dem Fortschritt von links nach rechts wächst (bei einem Ring im Uhrzeigersinn).

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│0 %          25 %          50 %          100 %        │
│                                                      │
│[--------]   [###------]   [######---]   [########]   │
│                                                      │
│unbestimmt: [~~>~~~~]   [~~~>~~~]   Segment wandert   │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Balken** | die klassische horizontale Füllung mit Prozentangabe |
| **Ring** | kreisförmiger Fortschritt, z. B. in runden Icons |
| **Segmente** | diskrete Schritte (1/5, 2/5 …) für Assistenten |
| **Unbestimmt** | ein wandernder Abschnitt, wenn die Zielgröße unbekannt ist |
| **Kompakt** | eine dünne Leiste am Seitenrand (z. B. Lesefortschritt) |

## Dauer

- Typisch: 200–500 ms pro Wertänderung, Schleife 1000–1500 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Skeleton](../skeleton/description.md)
- [Typing](../typing/description.md)
