# Button – Attribute

Nur **eigene** Attribute. Alles Weitere kommt von der Basisklasse, siehe
[base](../../basics/base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `variant` | enum | `secondary` | hier mit festem Wertebereich: `primary`, `secondary`, `outline`, `ghost`, `danger`, `link` |
| `type` | enum | `button` | Formularrolle: `button`, `submit`, `reset` |
| `loading` | boolean | `false` | Ladezustand, verhindert wiederholtes Auslösen |

## Verhalten

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `fullWidth` | boolean | `false` | volle Breite des übergeordneten Kastens |
| `preventDoubleClick` | boolean | `true` | ein zweites Auslösen innerhalb von 300 ms ignorieren |
| `group` | string | `null` | Gruppen-ID, wenn der Button zu einer `button-group` gehört |

## Ereignisse

Es werden nur die geerbten Ereignisse genutzt: `onClick`, `onFocus`, `onBlur`.

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `aria-label` | string | erforderlich, wenn `iconOnly = true` |
| `aria-busy` | boolean | gesetzt, solange `loading = true` |
| `role` | string | `button` |

## Icon

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `icon` | string | `null` | Icon-Name (siehe [icon](../../media/icon/)) |
| `iconPosition` | enum | `left` | `left`, `right`, `none` |
| `iconOnly` | boolean | `false` | quadratischer Button ohne Text; benötigt `aria-label` |

## Geerbt von

`id`, `label`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`,
`tabIndex`, `onClick`, `onFocus`, `onBlur`, `animation`, `gesture`, `aria-*` →
[Basiskomponente](../../basics/base.md)
