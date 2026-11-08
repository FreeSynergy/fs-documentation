# Cross Slide - Aussehen

## Grundlayout

Beide Elemente liegen auf derselben Fläche, die seitlich begrenzt und abgeschnitten ist. Sie bewegen sich mit gleicher Geschwindigkeit in entgegengesetzte Richtungen, ohne Änderung von Größe oder Deckkraft.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│  0 ms             140 ms              280 ms         │
│                                                      │
│  ┌─────┐          ┌─────┐             ┌─────┐       │
│  │ Tab1│ Tab2     │Tab1 │Tab2    Tab1 │ Tab2│       │
│  └─────┘          └─────┘             └─────┘       │
│   T1 bei 0        jeweils 50 % des Weges  T2 bei 0  │
│                                                      │
│  richtung: left – Inhalt gleitet nach links hinaus   │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | `richtung: left`, volle Breite, gleichzeitige Bewegung |
| **Rückwärts** | `richtung: right` – klar lesbar als "zurück" |
| **Vertikal** | `richtung: up` für Stapel, Benachrichtigungen, Monatslisten |
| **Versetzt** | `anteilUeberlappung: 0.3` – das `altesElement` geht zuerst, dann kommt das neue |

## Dauer

- Typisch: 200–350 ms
- Standardwert: 280 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Cross Fade](../cross-fade/description.md)
- [Slide In](../../entrance/slide-in/description.md)
- [Slide Out](../../exit/slide-out/description.md)
