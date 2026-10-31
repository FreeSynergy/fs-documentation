# Search Field (Suchfeld mit Filter) - Attribute

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `value` | string | - | Wert (Suchbegriff) |
| `onChange` | function | - | Event bei Änderung |

## Verhaltens-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `variant` | enum | `simple` | Stil: `simple`, `filter`, `auto-complete` |
| `disabled` | boolean | `false` | Deaktiviert? |
| `placeholder` | string | `null` | Placeholder-Text |
| `showClear` | boolean | `true` | Clear-Button anzeigen? |

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
| `role` | string | ARIA-Rolle: `search` |

## Event-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onBlur` | function | Wird beim Verlassen ausgeführt |
| `onFocus` | function | Wird beim Fokus ausgeführt |
| `onSubmit` | function | Wird bei Submit ausgeführt |

## Auto-Complete-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showSuggestions` | boolean | `false` | Vorschläge anzeigen? |
| `suggestions` | array[] | - | Array von Vorschlägen |

## Filter-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showFilters` | boolean | `false` | Filter anzeigen? |
| `filters` | array[] | - | Array von Filtern |
| `onFilterChange` | function | Wird bei Filteränderung ausgeführt |

## Display-Attribute

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `showIcon` | boolean | `true` | Icon anzeigen? |
| `icon` | string | `search` | Icon-Name |
