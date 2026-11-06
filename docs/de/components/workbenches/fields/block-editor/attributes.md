# Block Editor (Blockeditor) - Attribute

Nur **eigene** Attribute. Alles Weitere stammt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `value` | object | - | Blockdokument |
| `onChange` | function | - | Änderungsereignis |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `edit` | `edit`, `read`, `template` |
| `blockTypes` | array | all | erlaubte Blocktypen |
| `showLayers` | boolean | `true` | Markierungen anzeigen |

## Events

| Event | Typ | Beschreibung |
|---|---|---|
| `onBlockAdd` | function | Block eingefügt |
| `onBlockMove` | function | Block verschoben |
| `onLinkFollow` | function | interner Link aufgerufen |

Gesten (Swipe, Long-Press, Drag) sind **keine** Attribute dieser Komponente: Sie werden vom Frontend ergänzt (ADR 0037).

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|---|---|---|
| `role` | string | `textbox` (mehrzeilig) mit `group` je Block |
| `aria-label` | string | Name des Dokuments |

## Geerbt von

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
