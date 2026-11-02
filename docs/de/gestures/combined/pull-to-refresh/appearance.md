# Pull to Refresh - Aussehen

## Grundlayout

Die Liste hängt an der oberen Kante; ein Indikator wächst aus dem Rand hervor.

```
┌─────────────────────────────────────────┐
│            ◌  (Indikator, wächst)       │
│  ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄          │
│  │ Eintrag 1                            │
│  │ Eintrag 2        ↑ Liste folgt dem   │
│  │ Eintrag 3          Finger (Gummiband)│
└─────────────────────────────────────────┘
```

## Zustands-Feedback

| Zustand | Aussehen |
|---------|----------|
| Pulling | Indikator halbtransparent, skaliert mit Distanz |
| Armed | Indikator voll, Pfeil dreht, Haptic Tick |
| Refreshing | Indikator rotiert unter der Liste |
| Done | Indikator schrumpft, Liste federt zurück |

## Indikator-Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Spinner** | Klassischer Kreispunkt (Material) |
| **Arrow** | Pfeil → Spinner (iOS-ähnlich) |
| **Custom** | Logo/Animation der App |

## Dauer

- Zonen bis Threshold: folgt dem Finger
- Ein-/Ausblenden: 200–300ms
- Ladezeit: unbegrenzt bis Antwort

## Unterschied zu Drag

- Pull to Refresh: Bewegung an fixierter Kante, löst Laden aus, federt zurück
- Drag: Bewegung eines Elements, Ziel ist eine neue Position
