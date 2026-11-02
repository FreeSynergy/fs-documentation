# Force Press - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `onForcePress` | function | - | Wird beim Force Press ausgeführt |
| `onPeek` | function | - | Vorschau-Stufe erreicht |
| `onPop` | function | - | Öffnen-Stufe erreicht |
| `onPressureChange` | function | - | Druckwert ändert sich |

## Druck-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `peekThreshold` | number | `0.5` | Ab diesem Druckwert (0–1) beginnt Peek |
| `popThreshold` | number | `0.75` | Ab diesem Druckwert öffnet die Geste |
| `fallbackLongPress` | boolean | `true` | Long Press als Ersatz ohne Drucksensor? |
| `fallbackDelay` | number | `500` | Delay des Long-Press-Fallbacks in ms |

## Vorschau-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `peekContent` | node \| url | - | Inhalt der Vorschau-Karte |
| `peekSize` | string | `small` \| `large` | Größe der Vorschau |
| `peekDimming` | boolean | `true` | Hintergrund hinter der Vorschau abdunkeln? |
| `quickActionItems` | array | `[]` | Kontext-Aktionen an der Vorschau |

## Feedback-Attribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `hapticFeedback` | boolean | `true` | Vibration beim Stufenwechsel? |
| `pressAnimation` | boolean | `true` | Element sinkt beim Drücken ein? |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `alternativeAction` | function | - | Long Press / Menüpunkt als gleichwertiger Weg |
| `requiresPressureHardware` | boolean | readonly | `true` wenn Hardware nötig |
| `aria-label` | string | - | Beschreibender Text |
