# Radial In - Erscheinungsbild

## Grundaufbau

Der Ankerkern bleibt als Sammelpunkt stehen. Jeder Punkt verlässt seine Ringposition und wandert
entlang seines Winkelstrahls zurück zur Ankermitte, dabei schrumpft und verblasst er. Die Ringe
lösen sich von außen nach innen auf.

## Visueller Ablauf

```
┌──────────────────────────────────────────────────────────────┐
│   0 ms           50 ms            110 ms           160 ms    │
│                                                              │
│  ◆ ○ ◆         ◆   ●   ◆       ◆  ◆ ●          nur Kern ●    │
│  alle Ringe    Ring 2 fast      nur Ring 1      s = 0, α = 0  │
│  stehen        weg, α → 0       halber Radius,  Kern verblasst│
│                                 s → 0           zuletzt       │
└──────────────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Standard** | alle Punkte gleichzeitig, eine kurze lineare Zugbewegung (160 ms) |
| **Ringe nacheinander** | zuerst der äußerste Ring, `ringStep` wirkt nach innen |
| **Nur Zweig** | verlässt der Zeiger einen Punkt, wandert nur dessen Unterring zurück |
| **Fächer** | an einer Ecke oder Kante: Die Punkte wandern zurück in die Ecke |
| **Ziehen** | Punkte beschleunigen zum Anker (`ease-in`), wirkt „eingesogen“ |

## Dauer

- Typisch: 120–200 ms
- Standardwert: 160 ms
- Punkte untereinander: 8–15 ms Versatz (`staggerStep`)
- Ringe untereinander: 40–60 ms Versatz (`ringStep`), Reihenfolge `outside-in`

## Siehe auch

- [Übersicht Animationen](../../index.md)
- [Radial Out](../../entrance/radial-out/description.md)
- [Radial Menu](../../../../components/widgets/navigation/radial-menu/description.md)
