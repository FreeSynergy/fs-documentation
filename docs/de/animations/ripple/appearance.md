# Ripple - Aussehen

## Grundlayout

Eine halbtransparente Kreisfläche startet am Berührungspunkt, wächst und verblasst innerhalb des Elements.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────┐
│  0 ms        150 ms      300 ms      450 ms      │
│    ●          ( ● )     (   ●   ) (     ●     )  │
│  R = 0       R = 40 %    R = 85 %    α = 0       │
│  Start am Berührungspunkt, blendet zum Ende      │
│  aus und wird an der Kontur beschnitten          │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Ab Touchpunkt** | `wellenUrsprung: click` - Standard auf Touchgeräten |
| **Zentriert** | `wellenUrsprung: center` - Einheitlich bei Tastaturbedienung |
| **Ausgefärbt** | `farbe` stark gesättigt - deutliche Bestätigung |
| **Überlaufend** | `containInElement: false` - Welle ragt über die Kontur |
| **Mehrfach** | `maxWellen` > 1 - schnelle Tiposerie |

## Dauer

- Typisch: 450 ms pro Welle (Bereich 350–600 ms)

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Highlight](../highlight/description.md)
- [Shake](../shake/description.md)
