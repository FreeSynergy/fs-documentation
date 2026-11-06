# Encryption State (Verschlüsselungsstatus)

| Feld | Wert |
|------|------|
| **Kategorie** | `feedback` |
| **Erbt von** | `base` |
| **Varianten** | `icon`, `icon-text`, `warning` |
| **Zustände** | `encrypted`, `unencrypted`, `unknown`, `focused` |
| **Gesten** | keine — Gesten kommen vom Frontend, nicht von der Komponente (ADR 0037) |
| **Animationen** | `pop-in` (Zustandsänderung) |
| **Verwandt** | `badge`, `link`, `message-status`, `key-verification`, `tooltip` |
| **Status** | Skizze |

## Beschreibung

Ein Verschlüsselungsstatus zeigt, wie eine Nachricht oder Unterhaltung geschützt ist (MLS, OpenPGP, Megolm, nur Transport, keine). Unverschlüsselt wird sichtbar markiert. Er ist **klickbar** und führt zum Leitfaden, der den Zustand erklärt.

## Verwendungszweck

- Verschlüsselung jeder Nachricht und Unterhaltung anzeigen (Messenger-Anforderung `message.encryption`)
- Unverschlüsselte eingehende Nachrichten deutlich markieren
- Zum Leitfaden zur Verschlüsselung führen (ADR 0018, ADR 0031)

## Varianten

| Variante | Beschreibung |
|---|---|
| **icon** | nur das Schloss-Symbol |
| **icon-text** | Symbol und Art der Verschlüsselung |
| **warning** | unverschlüsselt, deutlich hervorgehoben |

## Features

- Fünf Arten: `mls`, `openpgp`, `megolm`, `transport-only`, `none`
- Klick oder Enter öffnet den Leitfaden in der Bibliothek
- Optionale Übergabe an [key-verification](../../../widgets/overlays/key-verification/) für ungeprüfte Schlüssel

## Datenbindung

Bindet das Verschlüsselungsfeld `freesynergy.net:encryption` (`mls`, `openpgp`, `megolm`, `transport-only`, `none`). Darstellungsregister (ADR 0023): `Encryption → encryption-state | text`. Grenzfall, entschieden am 2026-11-05: **Primitive, kein Badge**, weil sie bedienbar ist.

## Abgrenzung

- **Nicht verwechseln mit** [badge](../badge/): Ein Badge ist nur Anzeige (keine Interaktion); diese Komponente ist ein Bedienelement, das zum Leitfaden verlinkt.
- **Nicht verwechseln mit** [message-status](../message-status/): Dieser zeigt den Zustellfortschritt.
- **Nicht verwechseln mit** [key-verification](../../../widgets/overlays/key-verification/): Diese ist der Dialog zur Bestätigung des Vertrauens.

## Best Practices

- Die Art im Tooltip in Worten nennen, nicht nur per Symbol.
- `none` muss auffälliger sein als `mls`, nie umgekehrt.
- Keine Sicherheit vortäuschen, die nicht da ist: `transport-only` ist nicht Ende-zu-Ende.

## Hinweis zu Blinc

Teilweise in Blinc vorhanden (`cn::badge` plus ein Link), aber die Datenbindung macht es zu unserer Schicht. Backlog-ID: keine ⚠️. Ein allgemeiner klickbarer Marker könnte später upstream beigetragen werden ⚠️.

## Offene Punkte

- ⚠️ Genaues Leitfaden-Ziel pro Art (IDs der Leitfaden-Seiten)
- ⚠️ Anzeigeregeln pro Nachricht oder pro Unterhaltung

## Siehe auch

- [feedback – Übersicht](../index.md)
- [Badge](../badge/)
- [Message Status](../message-status/)
- [Link](../../basics/link/)
- [Key Verification](../../../widgets/overlays/key-verification/)
- [Messenger-Anforderungen](../../../../programs/apps/messenger/requirements.md)
- [Basiskomponente](../../basics/base.md)
