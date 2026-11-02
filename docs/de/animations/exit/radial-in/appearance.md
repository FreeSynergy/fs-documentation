# Radial In - Aussehen

## Grundlayout

Der Ankerkern bleibt als Sammelpunkt stehen. Jeder Punkt verlässt seine Ringposition
und wandert auf seinem Winkelstrahl zurück zur Ankermitte, wobei er schrumpft und
ausbleicht. Ringe lösen sich von außen nach innen auf.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────────────────┐
│   0 ms           50 ms            110 ms           160 ms    │
│                                                              │
│  ◆ ○ ◆         ◆   ●   ◆       ◆  ◆ ●          nur Kern ●   │
│  alle Ringe   Ring 2 fast     nur Ring 1      s = 0, α = 0   │
│  stehen       weg, α → 0      auf halben      Kern blendet   │
│                               Radius, s → 0   zuletzt aus    │
└──────────────────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | alle Punkte zugleich, kurze lineare Sogbewegung (160 ms) |
| **Ringe nacheinander** | äußerster Ring zuerst, `ringStep` nach innen durchgereicht |
| **Nur Zweig** | verlässt der Zeiger einen Punkt, wandert nur dessen Unterpunkt-Ring zurück |
| **Fächer** | an Ecke oder Kante: Punkte treten in die Ecke zurück |
| **Sog** | Punkte beschleunigen zum Anker (`ease-in`), wirkt „eingezogen“ |

## Dauer

- Typisch: 120–200 ms
- Standardwert: 160 ms
- Punkte untereinander: 8–15 ms Versatz (`staggerStep`)
- Ringe untereinander: 40–60 ms Versatz (`ringStep`), Reihenfolge `outside-in`

## Siehe auch

- [Animationen Übersicht](../../index.md)
- [Radial Out](../../entrance/radial-out/description.md)
- [Radial Menu](../../../components/navigation/radial-menu/description.md)
