# Button (Schaltfläche) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `variant` | enum | `secondary` | hier mit festem Wertebereich: `primary`, `secondary`, `outline`, `ghost`, `danger`, `link` |
| `type` | enum | `button` | Formularrolle: `button`, `submit`, `reset` |
| `loading` | boolean | `false` | Ladezustand, blockiert Mehrfachauslösung |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `fullWidth` | boolean | `false` | volle Breite der Elternbox |
| `preventDoubleClick` | boolean | `true` | zweite Auslösung innerhalb 300 ms ignorieren |
| `group` | string | `null` | Gruppen-id, wenn der Button zu einem `button-group` gehört |

## Events

Es werden nur die geerbten Events genutzt: `onClick`, `onFocus`, `onBlur`.

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `aria-label` | string | Pflicht bei `iconOnly = true` |
| `aria-busy` | boolean | gesetzt, solange `loading = true` |
| `role` | string | `button` |

## Icon

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `icon` | string | `null` | Icon-Name (siehe [icon](../../media/icon/)) |
| `iconPosition` | enum | `left` | `left`, `right`, `none` |
| `iconOnly` | boolean | `false` | quadratischer Button ohne Text; verlangt `aria-label` |

## Geerbt von

`id`, `label`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base/)
