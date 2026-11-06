# Messenger — Vertrag (Entwurf 0.1)

Die Schnittstelle zwischen `fs-messenger` und jedem Frontend (ADR 0021). **Entwurf**; kompiliert mit `capnpc-embedded` 0.2.0 (capnp 1.4.0) + `capnpc` 0.23 (2026-11-05) — ohne C++-Toolchain (ADR 0040).
Die Schema-Datei liegt im Schnittstellen-Repository: [`schema/messenger.capnp`](https://github.com/FreeSynergy/fs-interfaces/blob/main/schema/messenger.capnp) in `fs-interfaces` (ADR 0045); Besitzer ist `fs-messenger`.

## Warum Cap'n Proto zu unserer Idee von Fähigkeiten passt

Cap'n-Proto-RPC ist **capability-basiert**: Ein Frontend erhält Referenzen auf Schnittstellen
(`Conversations`, `Compose`, `Rules`, …) und kann nur das tun, was diese Referenzen erlauben. Das ist die technische Form von „das Programm bietet Fähigkeiten an; ein Frontend nutzt sie oder nicht“ (ADR 0021/0037).
Das sehr einfache Frontend fordert nur `conversations` und `compose` an; das vollständige zusätzlich `search` und `rules`.

## Aufbau

| Schnittstelle | Fähigkeiten (Anforderungen) |
|-----------|-----------------------------|
| `Messenger` (Wurzel) | `capabilities()` listet Fähigkeiten-Kennungen + Vertragsversion; reicht die anderen weiter |
| `Accounts` | `account.add`, `account.remove`, `account.edit` |
| `Conversations` / `Conversation` | `conversation.list`, `conversation.open`, `conversation.pin`, `conversation.move`, `message.delete`, `message.flag`, `message.react`, `message.forward`, `message.edit`; `nextUnread` für Frontend Nr. 1 |
| `Compose` / `Draft` | `message.send` (inkl. Terminierung), `draft.save`, `attachment.add`, `encryptionPlan` = einen verschlüsselten Weg finden (ADR 0018) |
| `Search` | `message.search` |
| `Rules` | Regeln als Sieve (optionale Fähigkeit) |
| `subscribe` + `Listener` | Live-Updates: erstellt, aktualisiert, gelöscht, Zustellstatus (lokal gespeichert, ADR 0037) |

Datenstrukturen folgen dem Speichermodell: `Envelope` (AS2-Felder, ADR 0020), `Encryption` (ADR 0018),
`DeliveryState`, `original` als Blob (ADR 0030), sensible Kategorien (ADR 0029), UUIDv7 (ADR 0027).

## Offen

- gemeinsame `common.capnp` (Uuid, Timestamp, Cursor, Problem, Blob) für alle Programme
- Erzeugung von JSON / CLI / MCP aus dem Schema
- Kontakte und Kalender werden über die Verträge ihrer eigenen Programme genutzt, nicht hier dupliziert
