# Stepper - Aussehen

## Grundlayout

Ein Stepper ist eine visuelle Fortschrittsanzeige für Schritte.

## Layout

```
┌─────────────────────────────────────────┐
│  ●  ─────  ●  ─────  ○  ─────  ○       │
│ Schritt 1  Schritt 2  Schritt 3         │
└─────────────────────────────────────────┘
```

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Horizontal** | Horizontal (häufiger) |
| **Vertical** | Vertikal |
| **Dots** | Punkte-Stepper |
| **Lines** | Linien-Stepper |

## States

| State | Beschreibung |
|-------|--------------|
| **Active** | Aktueller Schritt |
| **Completed** | Abgeschlossener Schritt |
| **Pending** | Ausstehender Schritt |
| **Error** | Schritt mit Fehler |

## Größe-Varianten

| Größe | Schriftgröße | Verwendung |
|-------|-------------|------------|
| Small | 10px | Inline |
| Medium | 12px | Standard |
| Large | 14px | Featured |

## Farb-Varianten

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Active** | Primärfarbe | Aktueller Schritt |
| **Completed** | Grün | Abgeschlossener Schritt |
| **Pending** | Grau | Ausstehender Schritt |
| **Error** | Rot | Fehler |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `color` | Farbe ändert sich |
| `scale` | Vergrößerung |

## Animationen

| Effekt | Beschreibung |
|--------|--------------|
| `Fade In` | Einfade-Effekt |
| `Scale` | Skalierung |
