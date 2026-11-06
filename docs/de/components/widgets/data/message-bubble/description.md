# Message Bubble (Nachrichtenblase)

| Feld | Wert |
|------|------|
| **Kategorie** | `data` |
| **Erbt von** | `base` |
| **Varianten** | `incoming`, `own`, `compact` |
| **Zustände** | `own`, `incoming`, `selected`, `edited`, `deleted`, `failed` |
| **Gesten** | keine — Gesten kommen vom Frontend, nicht von der Komponente (ADR 0037) |
| **Animationen** | `slide-in`, `pop-in` (Reaktion) |
| **Verwandt** | `message-list`, `message-status`, `encryption-state`, `reaction-bar`, `link-preview`, `avatar` |
| **Status** | Skizze |

## Beschreibung

Eine Nachrichtenblase zeigt eine Chatnachricht mit Absender, Inhalt, Antwortbezug, Reaktionen, Zustellstatus und Verschlüsselung.

## Verwendungszweck

- Eine Nachricht innerhalb einer [message-list](../message-list/)
- Suchtreffer und Vorschauen (kompakt)
- Zitierte oder weitergeleitete Nachricht

## Varianten

| Variante | Beschreibung |
|---|---|
| **incoming** | links, mit Absendername und Avatar |
| **own** | rechts, mit Zustellstatus |
| **compact** | eine Zeile, für Suchergebnisse und Vorschauen |

## Features

- Absender, Uhrzeit und Bearbeitungsmarkierung
- Antwortbezug mit Sprung zum Original
- Anhänge und [link-preview](../link-preview/)
- [reaction-bar](../reaction-bar/) unter dem Inhalt
- [message-status](../../../primitives/feedback/message-status/) und [encryption-state](../../../primitives/feedback/encryption-state/)
- Platzhalter für gelöschte Nachrichten

## Datenbindung

Bindet eine Nachricht: ActivityStreams `Note` plus MIMI-Inhalt bzw. Matrix-Ereignis. Darstellungsregister (ADR 0023): `Message → bubble`. Dieselben Daten zeigt [mail-view](../mail-view/) (`mail`), Listenzeilen (`list-entry`) und als einfacher `text`.

## Abgrenzung

- **Nicht verwechseln mit** [mail-view](../mail-view/): Eine Mail hat Kopffelder, Text und Anhänge; eine Blase ist eine Chatzeile.
- **Nicht verwechseln mit** [card](../../containers/card/): Eine Card ist generisch; die Blase bindet das Nachrichtenmodell.
- **Nicht verwechseln mit** [message-list](../message-list/): Diese ordnet viele Blasen an.

## Best Practices

- Der Absender ist ohne Hover sichtbar.
- Aufeinanderfolgende Nachrichten desselben Absenders gruppieren; den Avatar nur einmal zeigen.
- Aktionen (antworten, reagieren, bearbeiten) bietet der Host an, z. B. als Hover-Leiste oder per Wischgeste aus dem Frontend (ADR 0037).

## Hinweis zu Blinc

Kein Blinc-Gegenstück. In unserer Schicht gebaut auf `cn::card`-ähnlichen Primitiven. Backlog-ID: keine ⚠️.

## Offene Punkte

- ⚠️ Darstellung von Rich Text (schreibgeschützter Modus des rich-text-editor, geplante Änderung)
- ⚠️ Thread-Anzeige innerhalb der Blase

## Siehe auch

- [data – Übersicht](../index.md)
- [Message List](../message-list/)
- [Reaction Bar](../reaction-bar/)
- [Link Preview](../link-preview/)
- [Mail View](../mail-view/)
- [Messenger-Anforderungen](../../../../programs/apps/messenger/requirements.md)
- [Basiskomponente](../../../primitives/basics/base.md)
