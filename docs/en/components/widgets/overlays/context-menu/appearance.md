# Context Menu (Rechtsklick-Menü) - Aussehen

## Grundlayout
Ein Context Menu wird durch Rechtsklick oder lange Touch-Aktion geöffnet.

```
┌─────────────────────────────────────────┐
│ 📋 Bearbeiten                           │
│ 📄 Kopieren                             │
│ 🗑️ Löschen                              │
│ ─────────────────────                   │
│ 🔄 Aktualisieren                        │
│ ℹ️ Eigenschaften                         │
└─────────────────────────────────────────┘
```

## Varianten

| Variante | Auslöser | Aussehen |
|----------|----------|----------|
| **Standard** | Rechtsklick (Desktop) | Menü am Zeiger |
| **Long Press** | lange Touch-Aktion | Menü über dem Objekt, Full-Width auf schmaler Fläche |
| **Overflow Menu** | Klick auf drei Punkte | Menü unter der Schaltfläche |

## Größen

| Größe | Breite | Schriftgröße | Verwendung |
|-------|--------|-------------|------------|
| Small | 150px | 12px | Wenige Optionen |
| Medium | 200px | 14px | Standard |
| Large | 250px | 16px | Viele Optionen |

## Farben und Zustände

| Status | Farbe | Beschreibung |
|--------|-------|--------------|
| **Active** | Primärfarbe | Aktiver Menüpunkt |
| **Hover** | Heller | Hover-Zustand |
| **Disabled** | Grau | Deaktivierte Optionen |
| **Danger** | Rot | Gefährliche Aktionen |

## Hover- und Fokus-Effekte

| Effekt | Beschreibung |
|--------|--------------|
| `background` | Hintergrund ändert sich |
| `color` | Farbe ändert sich |
| `border-radius` | Ecken abgerundet |

## Reaktiv

Das Menü klappt von der Auslösungsstelle weg und wechselt die Seite, wenn zum Bildschirmrand
zu wenig Platz ist (`pop-in` von der jeweiligen Ecke). Ist es höher als der freie Raum,
scrollt es selbst; der Auslösepunkt bleibt sichtbar.

```css
.context-menu { position: fixed; min-width: 150px; max-height: 70vh; overflow: auto;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2); animation: pop-in 120ms; }
.context-menu--flip-x { transform-origin: right top; }  /* kein Platz rechts */
.context-menu--flip-y { transform-origin: left bottom; } /* kein Platz unten */
```

## Icons

| Icon | Bedeutung |
|------|-----------|
| 📋 | Bearbeiten |
| 📄 | Kopieren |
| 🗑️ | Löschen |
| 🔄 | Aktualisieren |
| ℹ️ | Informationen |

## Separator

```
┌─────────────────────────────────────────┐
│ Aktionen                                │
│ ─────────────────────                   │
│ Weitere Aktionen                        │
└─────────────────────────────────────────┘
```
