# Message Composer (Nachrichtenverfasser) - Attribute

Nur **eigene** Attribute. Alles Weitere stammt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `draft` | object | - | Entwurf mit Empfängern, Betreff, Text, Anhängen |
| `onSend` | function | - | Senden angefordert |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `chat` | `chat`, `mail`, `reply` |
| `editor` | enum | `simple` | `simple` (Standard), `extended` ⚠️ |
| `encryptionRequired` | boolean | `true` | Nachrichten werden nur verschlüsselt gesendet (ADR 0018) |

## Events

| Event | Typ | Beschreibung |
|---|---|---|
| `onChange` | function | Entwurf geändert (automatisches Speichern) |
| `onSend` | function | Senden angefordert |
| `onAttach` | function | Anhang hinzugefügt |
| `onMention` | function | Erwähnung eingefügt |

Gesten (Swipe, Long-Press, Drag) sind **keine** Attribute dieser Komponente: Sie werden vom Frontend ergänzt (ADR 0037).

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|---|---|---|
| `role` | string | `form` |
| `aria-label` | string | „Nachricht schreiben“ |

## Geerbt von

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
