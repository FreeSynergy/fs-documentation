# Message Bubble (Nachrichtenblase) - Attribute

Nur **eigene** Attribute. Alles Weitere stammt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `message` | object | - | Nachrichtenobjekt (Note + Erweiterungen) |
| `sender` | object | aus der Nachricht | Akteur, angezeigt als Name und Avatar |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `incoming` | `incoming`, `own`, `compact` |
| `showSender` | boolean | `true` | Name und Avatar anzeigen |
| `selectable` | boolean | `false` | Auswahlmodus (Mehrfachauswahl) |

## Events

| Event | Typ | Beschreibung |
|---|---|---|
| `onReply` | function | Antwort angefordert |
| `onReact` | function | Reaktion umgeschaltet (aus [reaction-bar](../reaction-bar/)) |
| `onOpenAttachment` | function | Anhang geöffnet |
| `onJumpTo` | function | Sprung zur beantworteten Nachricht |

Gesten (Swipe, Long-Press, Drag) sind **keine** Attribute dieser Komponente: Sie werden vom Frontend ergänzt (ADR 0037).

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|---|---|---|
| `role` | string | `article` |
| `aria-label` | string | „Anna, 10:42, zugestellt: Nachrichtentext …“ |

## Geerbt von

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
