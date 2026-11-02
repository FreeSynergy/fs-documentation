# Shake - Aussehen

## Grundlayout

Ein Shake ist ein schnelles Hin- und Herbewegen des Geräts oder Elements.

## Visuelles Feedback

```
┌─────────────────────────────────────────┐
│                                         │
│        ┌───┐                            │
│   ←──  │ □ │  ──→  ←──  ──→            │
│        └───┘                            │
│      Bewegung um die Ausgangsposition   │
└─────────────────────────────────────────┘
```

## Feedback-Optionen

| Option | Beschreibung |
|--------|--------------|
| **Wiggle** | Element kippt leicht hin und her |
| **Translate** | Element verschiebt sich horizontal |
| **Haptic** | Vibration auf Mobilgeräten |
| **Error Color** | Randeinfärbung rot bei ungültiger Eingabe |
| **None** | Kein Feedback, nur Callback |

## Amplitude

| Intensität | Verschiebung | Verwendung |
|------------|--------------|------------|
| Leicht | 2–4px | Bestätigung |
| Mittel | 5–10px | Standard-Feedback |
| Stark | 10–20px | Fehler, Warnung |

## Dauer

- Typisch: 300–1000ms
- Feedback-Animation: 300–500ms

## Unterschied zu Swipe

- Swipe: eine Bewegung in eine Richtung
- Shake: mehrere Bewegungen hin und zurück
