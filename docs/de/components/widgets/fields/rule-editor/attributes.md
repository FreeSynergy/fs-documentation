# Rule Editor (Regeleditor) - Attribute

Nur **eigene** Attribute. Alles Weitere stammt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `rules` | array[] | - | Liste der Regeln (Bedingungsmenge, Aktionen, aktiviert) |
| `sieve` | string | - | Sieve-Quelltext; Alternative zu `rules` |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `list` | `list`, `simple` |
| `vocabulary` | object | mail | verfügbare Bedingungen und Aktionen |
| `allowExpert` | boolean | `false` | rohes Sieve anzeigen |

## Events

| Event | Typ | Beschreibung |
|---|---|---|
| `onChange` | function | Regelmenge geändert |
| `onTest` | function | Testlauf angefordert |
| `onSave` | function | gültige Regelmenge bestätigt |

Gesten (Swipe, Long-Press, Drag) sind **keine** Attribute dieser Komponente: Sie werden vom Frontend ergänzt (ADR 0037).

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|---|---|---|
| `role` | string | `group` je Regel, `list` für die Menge |
| `aria-label` | string | „Regel 2: wenn Absender news@ enthält“ |

## Geerbt von

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
