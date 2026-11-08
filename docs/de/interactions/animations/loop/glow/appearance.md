# Glow - Aussehen

## Grundlayout

Das Element steht still. Um seine Kontur liegt ein weicher, farbiger Schein, der langsam anschwillt und wieder abnimmt.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────┐
│Bild 1         Bild 2          Bild 3         Bild 4  │
│                                                      │
│[■]            ~[■]~          ~~[■]~~        ~[■]~    │
│aus            schwach         hell           schwach  │
│                                                      │
│Intensität: 0 → 50 → 100 → 50 % (endlose Schleife)    │
└──────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Konstant** | der Schein steht auf fester Intensität (Auswahl) |
| **Pulsierend** | der Schein atmet in der Schleife (Live-Status, Anwesenheit) |
| **Kontur** | der Schein folgt genau der Form des Elements (SVG/Eckenradius) |
| **Rechteckig** | der Schein als unscharfes Rechteck, günstiger zu rendern |
| **Ein/Aus** | der Schein baut sich bei Aktivierung weich auf und ab |

## Dauer

- Typisch: 1000–2000 ms pro Zyklus, Ein-/Ausblenden 200–400 ms

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Skeleton](../../loading/skeleton/description.md)
- [Typing](../../loading/typing/description.md)
