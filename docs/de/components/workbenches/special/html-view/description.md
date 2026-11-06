# HTML View (HTML-Ansicht)

| Feld | Wert |
|------|------|
| **Kategorie** | `special` |
| **Erbt von** | `base` |
| **Varianten** | `sanitised`, `remote-allowed` |
| **Zustände** | `loading`, `blocked-remote`, `ready` |
| **Gesten** | keine — Gesten kommen vom Frontend, nicht von der Komponente (ADR 0037) |
| **Animationen** | `fade-in` |
| **Verwandt** | `embed`, `mail-view`, `link`, `image` |
| **Status** | Skizze |

## Beschreibung

Eine HTML-Ansicht zeigt fremdes HTML (zum Beispiel einen Mailtext) in bereinigter Form, ohne etwas Externes zu laden.

## Verwendungszweck

- HTML-Text einer Mail
- Umfangreiche fremde Inhalte in Nachrichten
- Sichere Anzeige ohne Skripte, Tracking-Pixel oder externe Stile

## Varianten

| Variante | Beschreibung |
|---|---|
| **sanitised** | Standard: bereinigtes HTML, kein externes Laden |
| **remote-allowed** | externe Inhalte für diese Ansicht erlaubt |

## Features

- Der Sanitizer entfernt Skripte, Formulare, Frames und Ereignis-Handler
- Keine externen Bilder, Schriften oder Stile; `cid:`-Teile sind erlaubt
- Links sind markiert und laufen über den Host
- Hinweisleiste „Remote content blocked“ mit einer Auswahl pro Ansicht

## Datenbindung

Bindet den `text/html`-Teil einer MIME-Nachricht. Darstellungsregister (ADR 0023): `Html → html-view`. Einordnung am 2026-11-05 entschieden: **Workbench**, weil der Inhalt erst zur Laufzeit bekannt ist, wie bei [embed](../embed/).

## Abgrenzung

- **Nicht verwechseln mit** [embed](../embed/): Embed bindet fremde Programme oder Seiten ein; html-view rendert inaktives HTML als Inhalt. ⚠️ Könnte eine Variante von `embed` werden.
- **Nicht verwechseln mit** [mail-view](../../../widgets/data/mail-view/): Die Mailansicht ist der Rahmen; diese Komponente rendert nur den Text.

## Best Practices

- Standardmäßig blockierte externe Inhalte belassen.
- Niemals Skripte ausführen, unabhängig von der Variante.
- Auf den Textteil zurückfallen, wenn HTML nicht bereinigt werden kann.

## Hinweis zu Blinc

Upstream in Blinc: Backlog **a782b47** (phasenweiser Plan für `html_view()`; `embed` hat kein Gegenstück). Bis dahin wird der Textteil verwendet. Die Bereinigungsregeln sind unsere Schicht.

## Offene Punkte

- ⚠️ Regelsatz des Sanitizers (Allow-Liste)
- ⚠️ Darstellung von Mailfarben im Dunkelmodus

## Siehe auch

- [special – Übersicht](../index.md)
- [Embed](../embed/)
- [Mail View](../../../widgets/data/mail-view/)
- [Messenger-Anforderungen](../../../../programs/apps/messenger/requirements.md)
- [Basiskomponente](../../../primitives/basics/base.md)
