# Panel - Erscheinungsbild

## Grundlayout
Ein Panel ist ein großer Container mit Kopfzeile, Inhalt und Fußzeile.

```
┌─────────────────────────────────────────┐
│ Kopfzeile / Titel                       │
├─────────────────────────────────────────┤
│                                         │
│   Inhalt                                │
│   ...                                   │
│                                         │
├─────────────────────────────────────────┤
│ Fußzeile / Aktionen                     │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Beschreibung |
|----------|--------------|
| **standard** | Standard mit Kopfzeile |
| **einklappbar** | die Kopfzeile klappt den Inhalt ein und aus |
| **verschiebbar** | kann verschoben werden |
| **filter** | mit Filteroptionen |

## Größen

| Größe | Höhe | Verwendung |
|-------|------|------------|
| small | 200px | kleinere Panels |
| medium | 300px | Standard |
| large | 400px | große Panels |
| full | 100% | volle Breite |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **default** | hell | Standard |
| **primary** | Primärfarbe | primär |
| **secondary** | Sekundärfarbe | sekundär |

## Hover- und Fokuseffekte

| Effekt | Beschreibung |
|--------|--------------|
| `shadow` | der Schatten wird stärker |
| `border` | der Rahmen leuchtet auf |

## Responsiv

Panels folgen dem verfügbaren Platz: nebeneinander, untereinander oder als
Overlay. Auf einer schmalen Fläche wird ein Seiten-Panel zu einer [Drawer](../../overlays/drawer/).
Der Inhalt bleibt dabei unverändert.

```css
.panel-grid { display: grid; grid-template-columns: 2fr 1fr; gap: 16px; }
.panel-body { overflow: auto; }              /* der Inhalt scrollt, Kopf- und Fußzeile bleiben */

@media (max-width: 900px) {
  .panel-grid { grid-template-columns: 1fr; } /* Panels stapeln sich untereinander */
}
```
