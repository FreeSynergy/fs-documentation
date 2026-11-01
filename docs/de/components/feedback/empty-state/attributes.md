# Empty State (Leerer Zustand) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `title` | string | - | ein Satz, warum die Fläche leer ist |
| `description` | string | `null` | Zusatz in einem zweiten Satz |
| `icon` | string | `null` | Icon-Name (siehe [icon](../../media/icon/)) |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `variant` | enum | `leer` | `leer`, `kein-treffer`, `fehler` |
| `actionLabel` | string | `null` | Text der Hauptaktion |
| `actionHref` | string | `null` | Ziel der Hauptaktion, falls Verweis |
| `hint` | string | `null` | Kurztext für Kürzel oder Hilfe |
| `query` | string | `null` | Suchbegriff, in `kein-treffer` angezeigt |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onAction` | function | Hauptaktion ausgelöst |
| `onReset` | function | Filter zurückgesetzt |

## Barrierefreiheit

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `role` | string | `status` | - |
| `aria-live` | enum | `polite` | damit Wechsel gemeldet werden |
| `icon` | string | - | rein dekorativ, kein `aria-label` nötig |

## Geerbt von

`id`, `visible`, `enabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base/)
