# HTML View (HTML-Ansicht) - Attribute

Nur **eigene** Attribute. Alles Weitere stammt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `html` | string | - | fremder HTML-Quelltext |
| `baseParts` | array | - | `cid:`-Teile, die angezeigt werden dürfen |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `sanitised` | `sanitised`, `remote-allowed` |
| `allowRemote` | boolean | `false` | externe Inhalte laden |

## Events

| Event | Typ | Beschreibung |
|---|---|---|
| `onLinkClick` | function | Link aktiviert; der Host entscheidet |
| `onAllowRemote` | function | externe Inhalte erlaubt |

Gesten (Swipe, Long-Press, Drag) sind **keine** Attribute dieser Komponente: Sie werden vom Frontend ergänzt (ADR 0037).

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|---|---|---|
| `role` | string | `document` |
| `aria-label` | string | „Nachrichteninhalt“ |

## Geerbt von

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
