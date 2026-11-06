# Key Verification (Schlüsselprüfung) - Aussehen

## Grundlayout

```
┌──────────────────────────────────────┐
│ Verify Anna's key                    │
│ 4F2A 91BC 77D0 1E5A                  │
│ 0B3C 9A44 D1E8 62F0     ▒▒▒▒ QR     │
│ [ They match ]  [ They differ ]      │
└──────────────────────────────────────┘
```

## Varianten

| Variante | Aussehen |
|---|---|
| **fingerprint** | Monospace-Gruppen zu je vier Zeichen |
| **qr** | quadratischer QR-Code, Beschriftung darunter |
| **device-list** | Zeilen mit Zustandssymbol |

## Größen

| Größe | Höhe | Verwendung |
|---|---|---|
| `medium` | 360 px | Dialog |
| `large` | 480 px | mit Geräteliste |

## Farben und Zustände

| Zustand | Aussehen |
|---|---|
| `unverified` | Warnton |
| `verified` | Erfolgston |
| `mismatch` | Fehlerton |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|---|---|
| `background` | Button-Hover wie bei [button](../../../primitives/actions/button/) |

## Reaktiv

- Auf schmalen Bildschirmen wird der Dialog zu einem Vollbild-Blatt.
- Fingerprint-Gruppen brechen in zwei Zeilen um.
