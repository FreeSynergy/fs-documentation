# Mail View (Mailansicht) - Attribute

Nur **eigene** Attribute. Alles Weitere stammt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `mail` | object | - | JMAP-`Email`-Objekt mit Textteilen |
| `source` | blob | - | Original-MIME, optional |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `full` | `full`, `compact`, `source` |
| `allowRemote` | boolean | `false` | externe Inhalte für diese Mail laden |
| `showHeaders` | enum | `basic` | `basic`, `all` |

## Events

| Event | Typ | Beschreibung |
|---|---|---|
| `onOpenAttachment` | function | Anhang geöffnet oder gespeichert |
| `onAddressClick` | function | Adresse ausgewählt (antworten, Kontakt hinzufügen) |
| `onAllowRemote` | function | externe Inhalte von der Person erlaubt |

Gesten (Swipe, Long-Press, Drag) sind **keine** Attribute dieser Komponente: Sie werden vom Frontend ergänzt (ADR 0037).

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|---|---|---|
| `role` | string | `article` |
| `aria-label` | string | „Mail von Anna: Betreff“ |

## Geerbt von

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
