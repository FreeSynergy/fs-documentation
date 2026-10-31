# File Upload - Aussehen

## Grundlayout

Ein File Upload ist ein Element für Dateiauswahl und Upload.

## Layout-Varianten

### File Picker
```
┌─────────────────────────────────────────┐
│ [📁 Datei auswählen]                    │
└─────────────────────────────────────────┘
```

### Drag & Drop
```
┌─────────────────────────────────────────┐
│                                         │
│   Ziehen Sie Ihre Datei hierher         │
│                                         │
└─────────────────────────────────────────┘
```

### Image Preview
```
┌─────────────────────────────────────────┐
│  🖼️                                    │
│                                         │
│  [Dateiname.jpg]     [✕]                │
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
| **Primary** | Primärfarbe | Primär |
| **Active** | Dunkel | Aktiver Zustand |
| **Disabled** | Grau | Deaktiviert |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `border` | Rand leuchtet auf |
| `shadow` | Schatten stärker |
| `background` | Hintergrund ändert sich |

## Progress-Indicator

```
┌─────────────────────────────────────────┐
│ Datei.jpg                               │
│ ▓▓▓▓▓▓▓▓▓▓░░░░░░  75%                  │
└─────────────────────────────────────────┘
```
