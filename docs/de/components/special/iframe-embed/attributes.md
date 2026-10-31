# iFrame Embed - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `src` | string | - | Quell-URL |
| `title` | string | - | Titel |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `responsive` | boolean | `true` | Responsives Layout? |
| `allowFullscreen` | boolean | `true` | Vollbild erlauben? |
| `sandbox` | string | - | Sandbox-Attribute |

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
| `role` | string | ARIA-Rolle: `iframe` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onLoad` | function | Wird beim Laden ausgeführt |
| `onError` | function | Wird bei Fehler ausgeführt |

## Communication-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `postMessage` | boolean | `false` | Nachrichten austauschen? |
| `origin` | string | - | Erlaubte Origin |

## Display-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showBorder` | boolean | `true` | Rand anzeigen? |
| `borderColor` | string | `#ccc` | Rand-Farbe |
