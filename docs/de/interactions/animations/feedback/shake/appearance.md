# Shake - Erscheinungsbild

## Grundaufbau

Das Element bleibt an seiner Position im Layout und schwingt in kleinen Schritten um diese Mitte.

## Visueller Ablauf

```
┌──────────────────────────────────────────────────┐
│  wackelt um die Ruheposition, die Amplitude      │
│  klingt ab                                       │
│                                                  │
│  -8 px → [ANMELDEN]                              │
│      +6 px → [ANMELDEN]                          │
│    -4 px → [ANMELDEN]                            │
│        +2 px → [ANMELDEN]                        │
│  0 px  → [ANMELDEN]   nach 400 ms in Ruhe        │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|---------|-------------|
| **Standard** | waagerecht, 8 px, 3 Zyklen mit Abklingen |
| **Vertikal** | `achse: y` – nickt bei einer abgelehnten Bestätigung |
| **Drehend** | `achse: rotate` – eine leichte Drehung um wenige Grad |
| **Hart** | `waveform: linear`, `decay: false` – ein mechanischer Eindruck |
| **Dezent** | 3 px Amplitude, 2 Zyklen für zurückhaltende Hinweise |

## Dauer

- Typisch: 400 ms (Bereich 300–500 ms)

## Siehe auch

- [Übersicht Animationen](../../index.md)
- [Wiggle](../wiggle/description.md)
- [Ripple](../ripple/description.md)
