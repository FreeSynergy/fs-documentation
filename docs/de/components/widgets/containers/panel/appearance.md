# Panel - Aussehen

## Grundlayout
Ein Panel ist ein großer Container mit Header, Inhalt und Footer.

```
┌─────────────────────────────────────────┐
│ Header / Titel                          │
├─────────────────────────────────────────┤
│                                         │
│   Inhalt                                │
│   ...                                   │
│                                         │
├─────────────────────────────────────────┤
│ Footer / Aktionen                       │
└─────────────────────────────────────────┘
```

## Varianten

| Variant | Beschreibung |
|---------|--------------|
| **Default** | Standard mit Header |
| **Collapsible** | Header klappt Inhalt ein/aus |
| **Draggable** | Verschiebbar |
| **Filter** | Mit Filter-Optionen |

## Größen

| Größe | Höhe | Verwendung |
|-------|------|------------|
| Small | 200px | Kleinere Panels |
| Medium | 300px | Standard |
| Large | 400px | Große Panels |
| Full | 100% | Volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Default** | Hell | Standard |
| **Primary** | Primärfarbe | Primär |
| **Secondary** | Sekundärfarbe | Sekundär |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `shadow` | Schatten stärker |
| `border` | Rand leuchtet auf |

## Reaktiv

Panels richten sich nach dem verfügbaren Platz: nebeneinander, untereinander oder als
Overlay. Ein Seitenpanel wird auf schmaler Fläche zum [drawer](../../overlays/drawer/),
sein Inhalt bleibt dabei unverändert.

```css
.panel-grid { display: grid; grid-template-columns: 2fr 1fr; gap: 16px; }
.panel-body { overflow: auto; }              /* Inhalt scrollt, Header/Footer bleiben */

@media (max-width: 900px) {
  .panel-grid { grid-template-columns: 1fr; } /* Panels stapeln untereinander */
}
```
