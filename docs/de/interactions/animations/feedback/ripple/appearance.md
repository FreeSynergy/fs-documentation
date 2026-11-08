# Ripple - Erscheinungsbild

## Grundaufbau

Ein halbtransparenter Kreis beginnt am Berührungspunkt, wächst und verblasst innerhalb des
Elements.

## Visueller Ablauf

```
┌──────────────────────────────────────────────────┐
│  0 ms        150 ms      300 ms      450 ms      │
│    ●          ( ● )     (   ●   ) (     ●     )  │
│  R = 0       R = 40 %    R = 85 %    α = 0       │
│  beginnt am Berührungspunkt, verblasst am Ende   │
│  und wird an der Kontur abgeschnitten            │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Vom Berührungspunkt** | `wellenUrsprung: click` – der Standard auf Touchgeräten |
| **Zentriert** | `wellenUrsprung: center` – einheitlich bei Tastaturbedienung |
| **Farbig** | `farbe` stark gesättigt – eine deutliche Bestätigung |
| **Überlaufend** | `containInElement: false` – die Welle reicht über die Kontur hinaus |
| **Mehrere** | `maxWellen` > 1 – eine schnelle Folge von Tippern |

## Dauer

- Typisch: 450 ms pro Welle (Bereich 350–600 ms)

## Siehe auch

- [Übersicht Animationen](../../index.md)
- [Highlight](../highlight/description.md)
- [Shake](../shake/description.md)
