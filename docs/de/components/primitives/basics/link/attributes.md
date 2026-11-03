# Link (Verweis) - Attribute

Nur **eigene** Attribute. Alles andere kommt aus der Basisklasse, siehe
[base](../../basics/base/).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `href` | string | - | Zieladresse (Pflicht) |
| `external` | boolean | `false` | neues Tab-Fenster, setzt `rel="noopener"` |
| `download` | boolean \| string | `false` | Download statt Navigation, optional Dateiname |

## Darstellung

| Attribut | Typ | Default | Beschreibung |
|----------|-----|---------|--------------|
| `variant` | enum | `standard` | `standard`, `muted`, `icon`, `unterstrichen` |
| `underline` | enum | `hover` | `hover`, `always`, `never` |
| `icon` | string | `null` | Icon-Name |
| `iconPosition` | enum | `right` | `left`, `right` |

## Events

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `onNavigate` | function | vor dem Sprung; kann ihn abbrechen |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|----------|-----|--------------|
| `role` | string | `link` |
| `aria-current` | string | `page`/`location`, wenn das Ziel das aktuelle ist |
| `aria-label` | string | ergänzend bei Icon-Zusatz („öffnet neues Fenster“) |

## Geerbt von

`id`, `label`, `visible`, `enabled`/`disabled`, `size`, `theme`, `state`,
`tabIndex`, `onFocus`, `onBlur`, `gesture`, `aria-*` →
[Basiskomponente](../base/)
