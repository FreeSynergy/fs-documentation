# Link – Attribute

Nur **eigene** Attribute. Alles Weitere kommt von der Basisklasse, siehe
[base](../base.md).

## Hauptattribute

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `href` | string | - | Zieladresse (Pflicht) |
| `external` | boolean | `false` | neues Tab-Fenster, setzt `rel="noopener"` |
| `download` | boolean \| string | `false` | Download statt Navigation, optional mit Dateiname |

## Darstellung

| Attribut | Typ | Standard | Beschreibung |
|-----------|------|---------|-------------|
| `variant` | enum | `standard` | `standard`, `muted`, `icon`, `unterstrichen` |
| `underline` | enum | `hover` | `hover`, `always`, `never` |
| `icon` | string | `null` | Icon-Name |
| `iconPosition` | enum | `right` | `left`, `right` |

## Ereignisse

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `onNavigate` | function | vor dem Sprung; kann ihn abbrechen |

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|-----------|------|-------------|
| `role` | string | `link` |
| `aria-current` | string | `page`/`location`, wenn das Ziel das aktuelle ist |
| `aria-label` | string | zusätzlicher Text bei einem Icon („öffnet ein neues Fenster“) |

## Geerbt von

`id`, `label`, `visible`, `enabled`/`disabled`, `size`, `theme`, `state`,
`tabIndex`, `onFocus`, `onBlur`, `gesture`, `aria-*` →
[Basiskomponente](../base.md)
