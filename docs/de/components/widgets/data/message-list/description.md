# Message List (Nachrichtenliste)

| Feld | Wert |
|------|------|
| **Kategorie** | `data` |
| **Erbt von** | `base` |
| **Varianten** | `chat`, `thread`, `mail` |
| **Zustände** | `loading-older`, `anchored-bottom`, `scrolled-up`, `leer` |
| **Gesten** | keine — Gesten kommen vom Frontend, nicht von der Komponente (ADR 0037) |
| **Animationen** | `slide-in` (neue Nachricht), `fade-in` |
| **Verwandt** | `timeline`, `list-view`, `message-bubble`, `mail-view`, `separator` |
| **Status** | Skizze |

## Beschreibung

Eine Nachrichtenliste zeigt die Nachrichten einer Unterhaltung in zeitlicher Reihenfolge, unten verankert. Ältere Nachrichten werden auf Anforderung geladen; Trenner markieren Tage und ungelesene Nachrichten.

## Verwendungszweck

- Chatansicht einer Unterhaltung
- Bereich eines Antwortstrangs (Seitenspalte)
- Kompaktes Nachrichtenfenster, eingebettet in andere Programme (ADR 0037)

## Varianten

| Variante | Beschreibung |
|---|---|
| **chat** | flach, chronologisch, unten verankert |
| **thread** | Antwortstrang in einem Seitenbereich |
| **mail** | eine Zeile pro Mail, aufklappbar ⚠️ |

## Features

- Unten verankert: Neue Nachrichten halten das Ende im Blick
- Lädt ältere Nachrichten beim Scrollen nach oben (virtualisierte Zeilen)
- Trenner für Tage und ein Trenner „ungelesen ab hier“
- Schreibanzeige („schreibt …“) als letztes Element
- Sprung zur nächsten ungelesenen Nachricht

## Datenbindung

Bindet eine Folge von Nachrichten innerhalb eines `context`: eine Reihe von ActivityStreams-`Note`-Objekten, die Raum-Zeitleiste von Matrix oder eine MIMI-Unterhaltung. Darstellungsregister (ADR 0023): `Message → bubble | mail | list-entry | text`; die Liste wählt die Darstellung pro Eintrag (Standard `bubble`, bei Mail-Unterhaltungen `mail`). Zeilen sind [message-bubble](../message-bubble/) oder (kompakt) [mail-view](../mail-view/).

## Abgrenzung

- **Nicht verwechseln mit** [timeline](../timeline/): Eine Timeline ordnet Ereignisse auf einer Zeitachse an. ⚠️ Offen, ob `message-list` eine Variante von `timeline` wird.
- **Nicht verwechseln mit** [list-view](../list-view/): Eine List-View ist eine allgemeine Liste ohne umgekehrtes Scrollen oder Verankerung.
- **Nicht verwechseln mit** [message-bubble](../message-bubble/): Diese ist eine einzelne Nachricht.

## Best Practices

- Die Position beibehalten, wenn ältere Nachrichten nachgeladen werden.
- Die Grenze zu ungelesenen Nachrichten markieren; nicht ans Ende springen, wenn die Person nach oben gescrollt hat.
- Zeilen müssen virtualisiert sein; Unterhaltungen haben Tausende Einträge.

## Hinweis zu Blinc

Teilweise in Blinc vorhanden: `virtual_list` existiert, aber umgekehrtes Scrollen und Verankerung unten fehlen. In unserer Schicht darauf aufgebaut; eine Option für umgekehrtes Scrollen könnte upstream vorgeschlagen werden ⚠️. Backlog-ID: keine ⚠️.

## Offene Punkte

- ⚠️ Variante von `timeline` oder eigene Komponente
- ⚠️ Schreibanzeige: Teil dieser Komponente (Zerlegung) oder separat

## Siehe auch

- [data – Übersicht](../index.md)
- [Message Bubble](../message-bubble/)
- [Mail View](../mail-view/)
- [Timeline](../timeline/)
- [List View](../list-view/)
- [Messenger-Anforderungen](../../../../programs/apps/messenger/requirements.md)
- [Basiskomponente](../../../primitives/basics/base.md)
