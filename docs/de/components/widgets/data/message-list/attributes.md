# Message List (Nachrichtenliste) - Attribute

Nur **eigene** Attribute. Alles Weitere stammt von der Basisklasse, siehe
[base](../../../primitives/basics/base.md).

## Hauptattribute

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `messages` | array[] | - | Nachrichten des Kontexts (oder eine Datenquelle mit Paging) |
| `context` | string | - | Unterhaltungs-ID |

## Verhalten

| Attribut | Typ | Default | Beschreibung |
|---|---|---|---|
| `variant` | enum | `chat` | `chat`, `thread`, `mail` |
| `anchor` | enum | `bottom` | `bottom`, `top` |
| `showSeparators` | boolean | `true` | Trenner für Tage und ungelesene Nachrichten |
| `showTyping` | boolean | `true` | Schreibanzeige ⚠️ |

## Events

| Event | Typ | Beschreibung |
|---|---|---|
| `onLoadOlder` | function | oben erreicht, mehr Verlauf nötig |
| `onVisible` | function | Nachricht ist sichtbar geworden (für Lesebestätigungen) |
| `onSelect` | function | Nachricht ausgewählt (Mehrfachauswahl) |

Gesten (Swipe, Long-Press, Drag) sind **keine** Attribute dieser Komponente: Sie werden vom Frontend ergänzt (ADR 0037).

## Barrierefreiheit

| Attribut | Typ | Beschreibung |
|---|---|---|
| `role` | string | `log` (neue Einträge werden höflich angesagt) ⚠️ oder `feed` |
| `aria-label` | string | Name der Unterhaltung |

## Geerbt von

`id`, `visible`, `enabled`/`disabled`, `size`, `theme`, `rounded`, `state`, `tabIndex`,
`onFocus`, `onBlur`, `animation`, `aria-*` → [Basiskomponente](../../../primitives/basics/base.md)
