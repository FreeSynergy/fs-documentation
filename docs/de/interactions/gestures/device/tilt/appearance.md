# Tilt - Aussehen

## Grundlayout

Das Gerät wird geneigt; Inhalt bewegt sich mit oder ein Indikator wandert
Ruhelage → Ziel.

```
┌───────────────────────────────┐
│      ╱ Gerät kippt            │
│    ╱                          │
│  ●─────┐  Level-Indikator    │
│        └──●───────┐           │
│   Inhalt wandert mit ═►       │
└───────────────────────────────┘
```

## Feedback-Optionen

| Option | Beschreibung |
|--------|--------------|
| **Parallax** | Ebenen verschieben sich unterschiedlich schnell |
| **Level Indicator** | Wasserwaage/Kreuz zeigt Neigung |
| **Clamp Bounce** | Am Maximalwinkel leichtes Überfedern |
| **None** | Kein sichtbares Signal, nur Steuerwert |

## Empfindlichkeit

| Modus | Deadzone | Verwendung |
|-------|----------|------------|
| Fein | 1–2° | Fotograster, Panorama |
| Standard | 3–5° | Steuerung, Parallax |
| Träge | 6–10° | Grobe Auswahlen |

## Dauer

- kontinuierliche Messung, Reaktion < 100ms
- Ruhelage-Erkennung: 500ms ohne Änderung

## Unterschied zu Shake

- Tilt: Zustand („wie schräg?“), langsam, ein Zielwert
- Shake: Ereignis („wie oft geschüttelt?“), schnell, binär
