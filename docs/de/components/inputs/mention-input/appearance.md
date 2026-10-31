# Mention Input - Aussehen

## Grundlayout

Ein Mention Input ist ein Textfeld mit Benutzer-/Kontakt-Erwähnung.

## Layout

```
┌─────────────────────────────────────────┐
│ @John Doe @Jane Smith                   │
└─────────────────────────────────────────┘
```

## Größe-Varianten

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 200px | Inline |
| Medium | 300px | Standard |
| Large | 400px | Featured |
| Full | 100% | Volle Breite |

## Farb-Varianten

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Default** | Hell | Standard |
| **Mention** | Primärfarbe | Erwähnte Benutzer |
| **Active** | Dunkel | Aktiver Zustand |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `border` | Rand leuchtet auf |
| `shadow` | Schatten stärker |

## Auto-Complete

```
┌─────────────────────────────────────────┐
│ @                                       │
├─────────────────────────────────────────┤
│  John Doe                               │
│  Jane Smith                             │
│  Bob Müller                             │
│  +                                      │
└─────────────────────────────────────────┘
```

## Selected Users

```
┌─────────────────────────────────────────┐
│ @John Doe @Jane Smith (2 ausgewählt)    │
└─────────────────────────────────────────┘
```
