# Toolbar (Symbolleiste) - Appearance

## Base layout

Eine Toolbar ist eine Reihe von Buttons/Icons für häufige Aktionen.

## Variants

| Variant | Appearance |
| ---------- | ---------- |
| **standard** | einzeilige Leiste mit Symbolen |
| **kontext** | Leiste tauscht ihre Knöpfe, wenn sich die Auswahl ändert |
| **ribbon** | zwei oder drei Zeilen mit Gruppenüberschriften |

### Horizontal (Standard)
```
┌─────────────────────────────────────────────────────┐
│ [📄] [✏️] [✂️] [✔️] [❌] [🔍] [⚙️]                  │
└─────────────────────────────────────────────────────┘
```
### Floating (Schwebend)
```
                    ┌─────────────────────────────┐
                    │ [📄] [✏️] [✂️] [✔️]        │
                    └─────────────────────────────┘
```
### Sidebar (Links/Rechts)
```
┌─────┬─────────────────────────────────────────────┐
│     │ [📄] [✏️] [✂️] [✔️] [❌] [🔍] [⚙️]         │
│     │                                             │
│     │                                             │
└─────┴─────────────────────────────────────────────┘
```

## Sizes

| Size | Icon size | Button-Größe | Use |
| ------- | ------------ | -------------- | ------------ |
| Small | 16px | 32px | Inline |
| Medium | 24px | 48px | Standard |
| Large | 32px | 64px | Featured |

## Colours and states

| State | Colour | Description |
| -------- | ------- | -------------- |
| **Primary** | Primärfarbe | Hauptaktion |
| **Secondary** | Sekundärfarbe | Sekundäre Aktion |
| **Danger** | Rot | Gefährliche Aktion |
| **Disabled** | Grau | Deaktivierte Aktion |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `color` | the colour changes |
| `background` | Hintergrund ändert sich |
| `scale` | Leichte Vergrößerung |
| `shadow` | Schatten erscheint |

## Responsive

- Die Leiste ist vollbreit und bleibt beim Scrollen oben stehen (`geklebt`); der Inhalt der
  Gruppe rechts rutscht zuerst weg.
- Passt die Reihe nicht mehr, wandern die übrigen Knöpfe hinter ein ``+``-Aufklappfeld,
  das die Gruppen beibehält.
- Auf Touch-Geräten sind die Knöpfe mindestens 44 px groß; auf großen Bildschirmen kann
  `Symbol und Text` gezeigt werden, auf kleinen nur das Symbol.

## Beschriftung der Knöpfe

| Form | Description |
| ------ | -------------- |
| **nur Symbol** | Standard, mit Tooltip |
| **nur Text** | wenn kein eindeutiges Symbol existiert |
| **Symbol und Text** | neue oder mehrdeutige Aktionen |

## Separator

```
┌─────────────────────────────────────────────────────┐
│ [📄] [✏️] [✂️] ───── [✔️] [❌] [🔍] [⚙️]            │
└─────────────────────────────────────────────────────┘
```
