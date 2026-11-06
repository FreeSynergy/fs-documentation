# Mail View (Mailansicht)

| Feld | Wert |
|------|------|
| **Kategorie** | `data` |
| **Erbt von** | `base` |
| **Varianten** | `full`, `compact`, `source` |
| **Zustände** | `unread`, `read`, `encrypted`, `signed`, `signature-invalid` |
| **Gesten** | keine — Gesten kommen vom Frontend, nicht von der Komponente (ADR 0037) |
| **Animationen** | `fade-in` |
| **Verwandt** | `description-list`, `html-view`, `message-bubble`, `file-upload`, `encryption-state` |
| **Status** | Skizze |

## Beschreibung

Eine Mailansicht zeigt eine E-Mail: Kopf (Von, An, Cc, Betreff, Datum), Text als Klartext oder HTML, Anhänge sowie den Signatur- und Verschlüsselungsstatus.

## Verwendungszweck

- Lesebereich eines Mailprogramms
- Suchtreffer und Vorschauen (kompakt)
- Mail innerhalb einer Ticket- oder Kontaktansicht (ADR 0037)

## Varianten

| Variante | Beschreibung |
|---|---|
| **full** | Kopf, Text und Anhänge |
| **compact** | Kopfzeile und Auszug (Listenvorschau, Suchtreffer) |
| **source** | Original-MIME ⚠️ |

## Features

- Kopffelder über [description-list](../description-list/)
- Text als Klartext oder bereinigtes HTML über [html-view](../../../workbenches/special/html-view/)
- Anhangsliste mit Vorschau
- Status für Signatur und Verschlüsselung
- Keine externen Inhalte standardmäßig geladen (Messenger-Anforderung)

## Datenbindung

Bindet JMAP-`Email` plus das Original-MIME (`message/rfc822`). Darstellungsregister (ADR 0023): `Message → mail`. Der HTML-Text ist der `text/html`-Teil und wird an [html-view](../../../workbenches/special/html-view/) übergeben.

## Abgrenzung

- **Nicht verwechseln mit** [message-bubble](../message-bubble/): Chatzeile gegenüber einer Mail mit Kopf.
- **Nicht verwechseln mit** [html-view](../../../workbenches/special/html-view/): Diese rendert nur den fremden HTML-Text; die Mailansicht ist der Rahmen darum.
- **Nicht verwechseln mit** [description-list](../description-list/): Der Kopf wird daraus aufgebaut; die Mailansicht ergänzt Text und Anhänge.

## Best Practices

- Die echte Absenderadresse zeigen, nicht nur den Anzeigenamen.
- Unverschlüsselte und unsignierte Mails sichtbar kennzeichnen.
- „Externe Inhalte laden“ nur als bewusste Aktion pro Mail anbieten.

## Hinweis zu Blinc

Kein Blinc-Gegenstück (`description-list` ist auch nicht vorhanden). In unserer Schicht gebaut. Der HTML-Text hängt vom Blinc-Plan `html_view()` ab, Backlog **a782b47**; bis dahin wird die Textfassung verwendet.

## Offene Punkte

- ⚠️ Variante `source`: In der ersten Version nötig?
- ⚠️ Eingebettete Bilder mit `cid:`-Teilen: erlaubt, Remote-URLs blockiert; wie wird die Ausnahme angezeigt?

## Siehe auch

- [data – Übersicht](../index.md)
- [Description List](../description-list/)
- [HTML View](../../../workbenches/special/html-view/)
- [Message Bubble](../message-bubble/)
- [Messenger-Anforderungen](../../../../programs/apps/messenger/requirements.md)
- [Basiskomponente](../../../primitives/basics/base.md)
