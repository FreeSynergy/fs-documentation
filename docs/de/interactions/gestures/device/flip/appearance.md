# Flip - Aussehen

## Grundlayout

Das Gerät dreht sich um eine horizontale Achse; die UI zeigt den neuen Modus
als Icon-Zustand, nicht als Animation auf dem Gerät selbst.

```
┌───────────────────────────────┐
│   📱 (Display oben)            │
│      │  Umdrehen 180°         │
│      ▼                        │
│   📵 (Display unten)          │
│   Toast: „Nicht stören“       │
└───────────────────────────────┘
```

## Feedback-Optionen

| Option | Beschreibung |
|--------|--------------|
| **Toast** | Kurze Statusmeldung („Nicht stören aktiv“) |
| **Haptic** | Vibration beim Erkennen der Umkehr |
| **Status Icon** | Modus-Icon in Statusleiste bleibt sichtbar |
| **None** | lautlos, nur Zustandswechsel |

## Zustände

| Zustand | Anzeige |
|---------|---------|
| Normal | kein Icon |
| Umgedreht | Glocke durchgestrichen / Mond-Icon |
| Zurückgedreht | Icon verschwindet (bei `autoRevert`) |

## Dauer

- Erkennung: nach `holdTime` (typisch 1s)
- Toast-Sichtbarkeit: 2–3s

## Unterschied zu Shake

- Flip: 180°-Drehung, stabiler neuer Zustand, meist „Stumm“
- Shake: Hin- und Her, einmaliges Ereignis, meist „Undo“
