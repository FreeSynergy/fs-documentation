# Widget Embed - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `widgetId` | string | - | Widget-ID |
| `config` | object | - | Konfiguration |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsive` | boolean | `true` | Responsives Layout? |
| `interactive` | boolean | `true` | Interaktiv? |
| `disabled` | boolean | `false` | Deaktiviert? |

## Styling-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `size` | enum | `medium` | Größe: `small`, `medium`, `large` |
| `rounded` | boolean | `true` | Abgerundete Ecken? |
| `theme` | enum | `default` | Theme: `default`, `dark` |

## Accessibility (Barrierefreiheit)

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Beschreibender Text |
| `role` | string | ARIA-Rolle: `region` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onLoad` | function | Wird beim Laden ausgeführt |
| `onError` | function | Wird bei Fehler ausgeführt |

## Communication-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `postMessage` | boolean | `false` | Nachrichten austauschen? |

## Display-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showBorder` | boolean | `true` | Rand anzeigen? |
