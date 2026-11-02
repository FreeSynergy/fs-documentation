# Flick - Aussehen

## Grundlayout

Der Finger wischt schnell und hebt ab; der Inhalt rollt mit abnehmender
Geschwindigkeit weiter.

```
┌─────────────────────────────────────────┐
│  ┌───────────────────────────┐          │
│  │ ░░░ Inhalt                │  ←───┐   │
│  │ ░░░░░                     │      │ Finger hebt ab
│  │ ░░░░░░░        ·····►     │   (Velocity)
│  └───────────────────────────┘  Nachlauf, decelariert
└─────────────────────────────────────────┘
```

## Phasen

| Phase | Beschreibung |
|-------|--------------|
| **Beschleunigen** | Inhalt folgt dem Finger, Geschwindigkeit steigt |
| **Loslassen** | Velocity wird gemessen, Over-Scroll möglich |
| **Nachlaufen** | Inhalt decelariert, ggf. Einrasten am Element |

## Feedback-Optionen

| Option | Beschreibung |
|--------|--------------|
| **Momentum** | Auslaufen mit abnehmender Geschwindigkeit |
| **Snap** | Am nächsten Listenelement einrasten |
| **Rubber Band** | Über die Grenze hinaus federn (siehe rubber-band-Animation) |
| **Haptic** | Vibration beim Einrasten / an der Grenze |

## Geschwindigkeit

| Intensität | Velocity | Verwendung |
|------------|----------|------------|
| Leicht | 1000–2000 px/s | Weiterblättern um wenige Einträge |
| Mittel | 2000–4000 px/s | Typisches Throw-Scrolling |
| Stark | > 4000 px/s | Schnell nach unten „springen“ |

## Unterschied zu Swipe

- Swipe: Distanz entscheidet, Bewegung endet mit dem Finger
- Flick: Geschwindigkeit entscheidet, Bewegung lebt weiter
