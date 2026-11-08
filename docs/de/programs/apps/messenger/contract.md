# Messenger — Vertrag (Entwurf 0.2)

Die Schnittstelle zwischen `fs-messenger` und jedem Frontend (ADR 0021). **Entwurf**; kompiliert mit `capnpc-embedded` 0.2.0 (capnp 1.4.0) + `capnpc` 0.23 (2026-11-05) — ohne C++-Toolchain (ADR 0040).
Die Schemadatei liegt im Schnittstellen-Repository: [`schema/messenger.capnp`](https://github.com/FreeSynergy/fs-interfaces/blob/main/schema/messenger.capnp) in `fs-interfaces` (ADR 0045); das Programm, dem sie gehört, ist `fs-messenger`.

## Warum Cap'n Proto zu unserer Idee von Fähigkeiten passt

Cap'n-Proto-RPC ist **fähigkeitsbasiert**: Ein Frontend bekommt Verweise auf Schnittstellen
(`Conversations`, `Compose`, `Rules`, …) und kann nur das tun, was diese Verweise erlauben. Das ist die technische Form von
„das Programm bietet Fähigkeiten an; ein Frontend nutzt sie oder nicht“ (ADR 0021/0037).
Das ganz einfache Frontend fragt nur `conversations` und `compose` ab; das volle auch
`search` und `rules`.

## Aufbau

| Schnittstelle | Fähigkeiten (Anforderungen) |
|-----------|-----------------------------|
| `Messenger` (Wurzel) | `capabilities()` listet Fähigkeiten-IDs + Vertragsversion; gibt die anderen weiter |
| `Accounts` | `account.add`, `account.remove`, `account.edit` |
| `Conversations` / `Conversation` | `conversation.list`, `conversation.open`, `conversation.pin`, `conversation.move`, `message.delete`, `message.flag`, `message.react`, `message.forward`, `message.edit`; `nextUnread` für Frontend Nr. 1 |
| `Compose` / `Draft` | `message.send` (inkl. Planung), `draft.save`, `attachment.add`, `encryptionPlan` = einen verschlüsselten Weg finden (ADR 0018) |
| `Search` | `message.search` |
| `Rules` | Regeln als Sieve (optionale Fähigkeit) |
| `subscribe` + `Listener` | Live-Aktualisierungen: angelegt, geändert, gelöscht, Zustellstatus (lokal gespeichert, ADR 0037) |

Die Datenstrukturen folgen dem Speichermodell: `Envelope` (AS2-Felder, ADR 0020), `Encryption` (ADR 0018),
`DeliveryState`, `original` als Blob (ADR 0030), sensible Kategorien (ADR 0029), UUIDv7 (ADR 0027).

## KI-Agenten im Vertrag (Entwurf 0.2, `fs-interfaces` v0.16.0)

Ein `ToolCall` ist das, was eine KI tun will oder getan hat. Er hat eine `revision`, die die Engine bei jeder Änderung erhöht, damit ein verspätetes Ereignis
nie einen neueren Stand überschreiben kann. `askedOf` nennt die Person, deren Entscheidung zählt. Eine `ToolCallDecision` trägt den `signer`, der
genau diese Person sein muss, und verweist auf einen Digest der Argumente. So deckt die Entscheidung genau das ab, was die Person gesehen hat. Nicht gesetzte Werte bedeuten nie etwas Gutes: Ein nicht gesetztes `Encryption` ist `unknown`, ein nicht gesetztes `kind` ist `unknown`. Eine Freigabe wird einer KI nie angeboten (ADR 0054).

## Offen

- gemeinsame `common.capnp` (Uuid, Timestamp, Cursor, Problem, Blob) für alle Programme
- Erzeugung von JSON / CLI / MCP aus dem Schema
- Kontakte und Kalender werden über die Verträge ihrer eigenen Programme genutzt, nicht hier doppelt geführt
