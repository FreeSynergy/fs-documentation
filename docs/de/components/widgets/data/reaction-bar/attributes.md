# Reaction Bar (Reaktionsleiste) - Attribute

Nur **eigene** Attribute. Alles Weitere stammt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `reactions` | array[] | - | Liste von `{emoji, count, own}` |
| `messageId` | string | - | Nachricht, zu der die Reaktionen gehören |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `inline` | `inline`, `compact` |
| `maxVisible` | number | `8` | Chips vor dem Überlauf-Chip |
| `canReact` | boolean | `true` | Schreibberechtigung |

## Events

| Event | Typ | Beschreibung |
|---|---|---|
| `onToggle` | function | eigene Reaktion (Emoji) umgeschaltet |
| `onAdd` | function | „+“ aktiviert, Auswahl öffnen |

Gesten (Swipe, Long-Press, Drag) sind **keine** Attribute dieser Komponente: Sie werden vom Frontend ergänzt (ADR 0037).

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|---|---|---|
| `role` | string | `group` |
| `aria-pressed` | boolean | an jedem Chip: eigene Reaktion aktiv |

## Geerbt von

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
