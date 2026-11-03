# Context Menu (Rechtsklick-Menü) - Appearance

## Base layout
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

## Variants

| Variant | Auslöser | Appearance |
| ---------- | ---------- | ---------- |
| **Standard** | Rechtsklick (Desktop) | Menü am Zeiger |
| **Long Press** | lange Touch-Aktion | Menü über dem Objekt, Full-Width auf schmaler Fläche |
| **Overflow Menu** | Klick auf drei Punkte | Menü unter der Schaltfläche |

## Sizes

| Size | Width | Font size | Use |
| ------- | -------- | ------------- | ------------ |
| Small | 150px | 12px | Wenige Optionen |
| Medium | 200px | 14px | Standard |
| Large | 250px | 16px | Viele Optionen |

## Colours and states

| State | Colour | Description |
| -------- | ------- | -------------- |
| **Active** | Primärfarbe | Aktiver Menüpunkt |
| **Hover** | Heller | hover state |
| **Disabled** | Grau | Deaktivierte Optionen |
| **Danger** | Rot | Gefährliche Aktionen |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `background` | Hintergrund ändert sich |
| `color` | the colour changes |
| `border-radius` | Ecken abgerundet |

## Responsive

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
| ------ | ----------- |
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
