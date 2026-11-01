# File Upload - Aussehen

## Grundlayout

Ein File Upload ist ein Element für Dateiauswahl und Upload.

## Varianten

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

## Größen

| Größe | Breite | Verwendung |
|-------|--------|------------|
| Small | 200px | Inline |
| Medium | 300px | Standard |
| Large | 400px | Featured |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Default** | Hell | Standard |
| **Primary** | Primärfarbe | Primär |
| **Active** | Dunkel | Aktiver Zustand |
| **Disabled** | Grau | Deaktiviert |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `border` | Rand leuchtet auf |
| `shadow` | Schatten stärker |
| `background` | Hintergrund ändert sich |

## Reaktiv

- Die Drop-Zone wächst mit dem Inhalt: ohne Datei füllt sie die volle Breite,
  mit Dateiliste wird sie zur Liste unter dem Auslöser.
- Auf schmalen Bildschirmen stapeln sich Vorschau und Dateiname untereinander,
  der Entfernen-Knopf bleibt rechts oben erreichbar.
- Unter `small` Bildschirmbreite wird die Drop-Zone auf `Full` gestellt und der
  Auslöser als Vollbreiter Button gesetzt.

## Progress-Indicator

```
┌─────────────────────────────────────────┐
│ Datei.jpg                               │
│ ▓▓▓▓▓▓▓▓▓▓░░░░░░  75%                  │
└─────────────────────────────────────────┘
```
