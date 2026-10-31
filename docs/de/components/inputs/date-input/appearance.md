# Date Input - Aussehen

## Grundlayout

Ein Date Input ist ein Datumsauswahl-Feld mit Kalender.

## Layout

```
┌─────────────────────────────────────────┐
│Datum                                    │
├─────────────────────────────────────────┤
│  📅 2024-01-15                          │
│                                         │
└─────────────────────────────────────────┘
```

## Größe-Varianten

| Größe | Höhe | Verwendung |
|-------|------|------------|
| Small | 32px | Inline |
| Medium | 48px | Standard |
| Large | 64px | Featured |

## Farb-Varianten

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Default** | Hell | Standard |
| **Primary** | Primärfarbe | Primär |
| **Active** | Dunkel | Aktiver Zustand |
| **Disabled** | Grau | Deaktiviert |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `border` | Rand leuchtet auf |
| `shadow` | Schatten stärker |

## Kalender-Overlay

```
┌─────────────────────────────────────────┐
│        Januar 2024                      │
│ Mo Di Mi Do Fr Sa So                    │
│          1  2  3  4  5  6  7            │
│  8  9 10 11 12 13 14 [15] 16 17         │
│ 18 19 20 21 22 23 24 25 26 27 28 29 30  │
│ 31                                       │
└─────────────────────────────────────────┘
```

## Range-Selection

```
┌─────────────────────────────────────────┐
│ Von - Bis                               │
├─────────────────────────────────────────┤
│  [01.01.2024] ━━━━━━━━━━━ [15.01.2024] │
└─────────────────────────────────────────┘
```
