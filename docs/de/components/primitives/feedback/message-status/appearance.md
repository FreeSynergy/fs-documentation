# Message Status (Nachrichtenstatus) - Aussehen

## Grundlayout

```
 sending   sent    delivered   read     failed
   ◷        ✓        ✓✓        ✓✓ (in colour)   ⚠
```

## Varianten

| Variante | Aussehen |
|---|---|
| **icon** | 16 px großes Symbol; `read` nutzt die Akzentfarbe, `failed` die Fehlerfarbe |
| **icon-text** | Symbol, gefolgt von einem 12 px großen Wort |

## Größen

| Größe | Höhe | Verwendung |
|---|---|---|
| `small` | 12 px | in der Ecke einer Blase |
| `medium` | 16 px | Listenzeilen (Standard) |
| `large` | 20 px | Detailpanel |

## Farben und Zustände

| Zustand | Aussehen |
|---|---|
| `sending` | neutral, Uhr-Symbol |
| `sent` | neutral, ein Haken |
| `delivered` | neutral, zwei Haken |
| `read` | Akzentfarbe, zwei Haken |
| `failed` | Fehlerfarbe, Warnsymbol |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|---|---|
| `tooltip` | Zustandswort und Uhrzeit, siehe [tooltip](../../../widgets/overlays/tooltip/) |
| – | keine eigene Hover-Änderung |

## Reaktiv

- Auf schmalen Bildschirmen wird nur die Variante `icon` verwendet.
- Das Symbol bricht nie um; es bleibt am Ende des Zeitstempels.
