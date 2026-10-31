# Tree View (Baumansicht) - Aussehen

## Grundlayout

Ein Tree View ist eine hierarchische Verzeichnisstruktur mit Ein-/Ausklappen.

## Layout

```
┌─────────────────────────────────────────┐
│ ▶ Ordner 1                              │
│   └─ Datei 1                            │
│   └─ Datei 2                            │
├─────────────────────────────────────────┤
│ ▶ Ordner 2                              │
│   └─ Datei 3                            │
│   └─ Datei 4                            │
└─────────────────────────────────────────┘
```

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Simple** | Nur Text |
| **With Icons** | Mit Icons |
| **With Checkboxes** | Mit Checkboxen |
| **Draggable** | Verschiebbar |

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
| **Hover** | Heller | Hover-Zustand |
| **Active** | Primärfarbe | Aktiver Zustand |
| **Disabled** | Grau | Deaktiviert |
| **Selected** | Dunkel | Ausgewählter Knoten |

## Hover-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `background` | Hintergrund ändert sich |
| `border` | Rand leuchtet auf |

## Expand/Collapse

```
├─ [+] Ordner 1                          │
│  └─ [+] Datei 1                        │
│     └─ [+] Datei 2                     │
│        └─ [+] Datei 3                  │
│        └─ [✓] Datei 4                  │
│        └─ [✓] Datei 5                  │
└─────────────────────────────────────────┘
```
