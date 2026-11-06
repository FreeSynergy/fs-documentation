# Reaction Bar (Reaktionsleiste)

| Feld | Wert |
|------|------|
| **Kategorie** | `data` |
| **Erbt von** | `base` |
| **Varianten** | `inline`, `compact` |
| **Zustände** | `own-active`, `empty` |
| **Gesten** | keine — Gesten kommen vom Frontend, nicht von der Komponente (ADR 0037) |
| **Animationen** | `pop-in` (Zähleränderung) |
| **Verwandt** | `badge`, `emoji-picker`, `message-bubble`, `tooltip` |
| **Status** | Skizze |

## Beschreibung

Eine Reaktionsleiste zeigt Reaktionen auf eine Nachricht als Emoji mit Anzahl und erlaubt, die eigene Reaktion umzuschalten.

## Verwendungszweck

- Reaktionen unter einer Chatnachricht
- Schnelle Reaktion über einen [emoji-picker](../../fields/emoji-picker/) (Variante `reaction`)
- Zusammenfassung, wer reagiert hat (Tooltip)

## Varianten

| Variante | Beschreibung |
|---|---|
| **inline** | Reihe von Emoji-Chips unter einer Nachricht |
| **compact** | ein Zusammenfassungs-Chip mit der Gesamtzahl |

## Features

- Emoji plus Anzahl pro Chip
- Eigene Reaktion hervorgehoben; ein Klick schaltet um
- „+“-Chip öffnet den Emoji-Picker
- Tooltip listet auf, wer reagiert hat

## Datenbindung

Bindet aggregierte Reaktionen: ActivityStreams `Like` / `EmojiReact` mit `Undo`, MIMI-Reaktion, Matrix `m.annotation`. Darstellungsregister (ADR 0023): `Reaction → reaction-bar | text`. ⚠️ Nicht in unseren Frontend-Dateien; bekannt aus den Produkten (Messenger-Anforderung `message.react`).

## Abgrenzung

- **Nicht verwechseln mit** [badge](../../../primitives/feedback/badge/): Ein Badge ist nicht bedienbar.
- **Nicht verwechseln mit** [emoji-picker](../../fields/emoji-picker/): Dieser wählt ein Emoji aus; die Leiste zeigt bestehende Reaktionen an und schaltet sie um.

## Best Practices

- Chips begrenzen und den Rest in einem Überlauf-Chip gruppieren.
- Jeder Chip braucht einen Textnamen für Screenreader.
- Nicht zeigen, wer reagiert hat, wenn die Unterhaltung das verbirgt.

## Hinweis zu Blinc

Teilweise in Blinc vorhanden (`badge`, `toggle_group`). In unserer Schicht gebaut wegen des Reaktionsdatenmodells. Backlog-ID: keine ⚠️.

## Offene Punkte

- ⚠️ Eigene Emojis (Bilder): unterstützt?

## Siehe auch

- [data – Übersicht](../index.md)
- [Message Bubble](../message-bubble/)
- [Emoji Picker](../../fields/emoji-picker/)
- [Badge](../../../primitives/feedback/badge/)
- [Messenger-Anforderungen](../../../../programs/apps/messenger/requirements.md)
- [Basiskomponente](../../../primitives/basics/base.md)
