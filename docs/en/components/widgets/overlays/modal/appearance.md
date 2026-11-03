# Modal (Modaler Dialog) - Appearance

## Base layout
Ein Modal ist ein Overlay-Fenster mit Fokus auf Inhalt.

```
┌─────────────────────────────────────────┐
│ [✕] Titel                               │
├─────────────────────────────────────────┤
│                                         │
│   Inhalt                                │
│   ...                                   │
│                                         │
├─────────────────────────────────────────┤
│  [Abbrechen]       [Speichern]         │
└─────────────────────────────────────────┘
```

## Variants

| Variant | Size | Description |
| --------- | ------- | -------------- |
| **Small** | 300px | Formulare, Bestätigungen |
| **Medium** | 500px | Bearbeitungsdialoge |
| **Large** | 700px | Komplette Ansichten |
| **Fullscreen** | 100% | Komplette Ansicht |

## Sizes

| Size | Width | Height | Use |
| ------- | -------- | ------ | ------------ |
| Small | 300px | automatisch | Bestätigung, kurzer Text |
| Medium | 500px | automatisch | Standard |
| Large | 700px | automatisch | Formulare, Listen |
| Fullscreen | 100% | 100% | komplexe Ansicht |

Obergrenze sind 85 % der Viewport-Höhe; der Inhalt scrollt, Kopf- und Fußzeile bleiben stehen.

## Colours and states

| State | Colour | Description |
| -------- | ------- | -------------- |
| **Overlay** | Dunkel | Hintergrund abdunkeln |
| **Header** | Hell | Titelzeile |
| **Content** | Hell | Inhalt |
| **Footer** | Hell | Aktionen |

## Hover and focus effects

| Effect | Description |
| -------- | -------------- |
| `shadow` | stronger shadow |
| `border` | the border lights up |

## Responsive

Das Overlay legt sich über die Seite, sperrt den Hintergrund-Scroll und hält den Fokus im
Dialog (Escape schließt, Tab kreist innerhalb). Auf schmaler Fläche wird das Modal automatisch
zur Vollfläche, auf hohem Inhalt scrollt nur der Body.

```css
.modal        { position: fixed; inset: 0; display: grid; place-items: center; }
.modal-panel  { width: min(500px, 92vw); max-height: 85vh;
                display: grid; grid-template-rows: auto 1fr auto; }
.modal-body   { overflow: auto; }              /* nur der Inhalt scrollt */
body.modal-open { overflow: hidden; }          /* Hintergrund ist gesperrt */

@media (max-width: 600px) {
  .modal-panel { width: 100%; height: 100%; max-height: none; border-radius: 0; }
}
```

## Close-Button

```
┌─────────────────────────────────────────┐
│ [✕] Titel                               │
├─────────────────────────────────────────┤
│                                         │
│   Inhalt                                │
│                                         │
└─────────────────────────────────────────┘
```
