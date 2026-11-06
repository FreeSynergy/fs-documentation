# Link Preview (Linkvorschau) - Attribute

Nur **eigene** Attribute. Alles Weitere stammt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `url` | string | - | Linkziel |
| `title` | string | - | vom Absender mitgelieferter Titel |
| `description` | string | - | kurzer Text |
| `image` | blob | - | angehängtes Bild, nie extern |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `card` | `card`, `compact` |
| `confirmOpen` | boolean | `true` | vor dem Öffnen externer Ziele nachfragen |

## Events

| Event | Typ | Beschreibung |
|---|---|---|
| `onOpen` | function | aktiviert; das Host-Programm entscheidet, wie geöffnet wird |

Gesten (Swipe, Long-Press, Drag) sind **keine** Attribute dieser Komponente: Sie werden vom Frontend ergänzt (ADR 0037).

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|---|---|---|
| `role` | string | `link` |
| `aria-label` | string | „Link: Titel, example.org“ |

## Geerbt von

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
