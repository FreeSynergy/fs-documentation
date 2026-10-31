# Shake - Aussehen

## Grundlayout

Das Element bleibt an seiner Position im Layout und pendet in kleinen Schritten um diese Mitte.

## Visueller Verlauf

```
┌──────────────────────────────────────────────────┐
│  Rütteln um die Ruhelage, Amplitude klingt ab    │
│                                                  │
│  -8 px → [LOGIN]                                 │
│      +6 px → [LOGIN]                             │
│    -4 px → [LOGIN]                               │
│        +2 px → [LOGIN]                           │
│  0 px  → [LOGIN]   Ruhelage nach 400 ms          │
└──────────────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **Standard** | horizontal, 8 px, 3 Zyklen mit Abklingen |
| **Vertikal** | `achse: y` - nickt bei abgelehnter Bestätigung |
| **Rotierend** | `achse: rotate` - leichtes Verdrehen um wenige Grad |
| **Hart** | `waveform: linear`, `decay: false` - mechanischer Eindruck |
| **Dezent** | 3 px Amplitude, 2 Zyklen für subtile Hinweise |

## Dauer

- Typisch: 400 ms (Bereich 300–500 ms)

## Siehe auch

- [Animationen Übersicht](../index.md)
- [Wiggle](../wiggle/description.md)
- [Ripple](../ripple/description.md)
