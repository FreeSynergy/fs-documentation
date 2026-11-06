# Message Status (Nachrichtenstatus)

| Feld | Wert |
|------|------|
| **Kategorie** | `feedback` |
| **Erbt von** | `base` |
| **Varianten** | `icon`, `icon-text` |
| **Zustände** | `sending`, `sent`, `delivered`, `read`, `failed` |
| **Gesten** | keine — Gesten kommen vom Frontend, nicht von der Komponente (ADR 0037) |
| **Animationen** | `pop-in` (Zustandsänderung) |
| **Verwandt** | `badge`, `encryption-state`, `progress`, `tooltip`, `message-bubble` |
| **Status** | Skizze |

## Beschreibung

Ein Nachrichtenstatus zeigt, wie weit eine gesendete Nachricht gekommen ist: wird gesendet, gesendet, zugestellt, gelesen oder fehlgeschlagen. Es ist ein kleines Anzeigeelement und nicht bedienbar.

## Verwendungszweck

- Zustand einer gesendeten Nachricht in einer Blase oder Listenzeile
- Zustellungs- und Lesebestätigungen (Lesebestätigungen liegen in der Entscheidung der Person)
- Fehlermarker mit dem Grund als Tooltip, z. B. kein verschlüsselter Weg

## Varianten

| Variante | Beschreibung |
|---|---|
| **icon** | nur das Zustandssymbol, für Blasen und Listenzeilen |
| **icon-text** | Symbol mit einem kurzen Wort, für Details und Tabellen |

## Features

- Fünf Zustände, jeder ohne Farbe unterscheidbar (Symbolform und Tooltiptext)
- Tooltip mit der Uhrzeit der Zustandsänderung (siehe [tooltip](../../../widgets/overlays/tooltip/))
- Bei eingehenden Nachrichten ausgeblendet

## Datenbindung

Bindet den **Nachrichtenzustand**: MIMI-message-status-Entwurf `-02`, ActivityStreams `Read`, Matrix `m.receipt`, Mail DSN/MDN. Im Darstellungsregister (ADR 0023): `MessageState → message-status | text`. Der Zustand wird **lokal** in `fs-store` gespeichert (ADR 0037), damit Vorschauen ohne Matrix- oder Mailserver funktionieren. ⚠️ Offen, ob `sending` ein gespeicherter Zustand oder nur ein UI-Zustand ist.

## Abgrenzung

- **Nicht verwechseln mit** [badge](../badge/): Ein Badge ist ein frei gestalteter Marker, diese Komponente hat eine feste Zustandsmenge, die an das Nachrichtenmodell gebunden ist.
- **Nicht verwechseln mit** [progress](../progress/): Es gibt keine Prozentangabe, nur diskrete Zustände.
- **Nicht verwechseln mit** [encryption-state](../encryption-state/): Dieser zeigt, *wie* eine Nachricht geschützt ist, und ist bedienbar.

## Best Practices

- Nie allein auf Farbe verlassen; die Symbolform unterscheidet sich pro Zustand.
- `failed` dauerhaft anzeigen, die übrigen Zustände können nach einer Weile ausgeblendet werden.
- Einen erneuten Versuch über das Host-Programm anbieten (Blasenmenü), nicht innerhalb dieser Komponente.

## Hinweis zu Blinc

Nicht in Blinc vorhanden (`cn::badge` kommt am nächsten, ohne direktes Gegenstück). In unserer Schicht gebaut, weil sie den Nachrichtenzustand bindet. Backlog-ID: keine ⚠️ (die Zerlegung hat dafür kein Blinc-Issue).

## Offene Punkte

- ⚠️ Gruppenchats: aggregierter Zustand (zugestellt an 3 von 5) oder pro Empfänger?
- ⚠️ Mail: Ist ein DSN-`delivered` dasselbe wie `delivered` im Chat?

## Siehe auch

- [feedback – Übersicht](../index.md)
- [Badge](../badge/)
- [Encryption State](../encryption-state/)
- [Message Bubble](../../../widgets/data/message-bubble/)
- [Messenger-Anforderungen](../../../../programs/apps/messenger/requirements.md)
- [Basiskomponente](../../basics/base.md)
