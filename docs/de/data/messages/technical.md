# Nachrichten – technische Erklärung

Entscheidungen: ADR 0018 (ein Messenger, nur verschlüsselt, Konnektoren), ADR 0019/0020 (`fs-store`,
Envelope + Inhalt + Protokoll), ADR 0027 (UUIDv7). Belege: [standards.md](standards.md).

## Prinzip: Original + Envelope

Jede Nachricht wird **wie empfangen** gespeichert (das Original, ggf. signiert) **plus** ein
normalisierter Envelope:

| Teil | Chat (MIMI) | E-Mail | Matrix |
|------|-------------|--------|--------|
| Original | MIMI-Inhalt (CBOR) | rohes MIME (RFC 5322) | Event-JSON |
| Envelope `type` | `Note` | `Note` (`name` = Betreff) | `Note` |
| `mediaType` des Payloads | MIMI-Inhaltstyp nach Entwurf -10 | `message/rfc822` | Matrix-Event |
| `context` (Unterhaltung) | MIMI-Raum / Thema | JMAP `threadId` | Raum / `m.thread`-Wurzel |
| `inReplyTo` | MIMI-Antwort-ID | `In-Reply-To`-Header | `m.in_reply_to` |
| herausgezogene Indexfelder | Absender, Rumpftext | JMAP-`Email`-Felder (from, to, subject, sentAt, textBody, attachments) | Absender, Rumpftext |

Signaturen bleiben verifizierbar, weil das Original nie umgeschrieben wird.

## Speicherung (ADR 0020)

- `id` = UUIDv7 (unserer). **Alias-Tabelle** `message_alias(id, scheme, external_id)` für `Message-ID`, Matrix `event_id`, MIMI-ID — Lücke, siehe Standards.
- Herausgezogene Spalten: `id`, `context`, `in_reply_to`, `attributed_to`, `published`, `updated`, `encryption`, `kind` (`mail`/`chat`/`comment`), Volltextfelder.
- **Verschlüsselungszustand** je Nachricht, Anbieter-Eigenschaft `freesynergy.net:encryption` (ADR 0028): `mls` · `openpgp` · `megolm` · `transport-only` · `none`. Ausgehendes `transport-only`/`none` wird abgelehnt oder nachgefragt (ADR 0018); eingehendes wird **markiert**, mit Link zum Bibliotheksführer fürs Verschlüsseln von Mail (ADR 0031).
- Inhalt wird im Ruhezustand verschlüsselt gespeichert (ADR 0024); sensible Markierung greift (ADR 0029).
- **Zustellungs-Kopien:** `to`/`cc`/`bto`/`bcc` entscheiden, **wo Kopien landen** (Beschluss 2). Intern: Tabelle `message_delivery` (`message_id`, `recipient_id`, `audience` ∈ `to|cc|bto|bcc`). Die eigentliche Autorisierung läuft getrennt über Ressourcen-Rechte — die Audience-Felder ersetzen sie nicht.

## Protokoll-Abbildung (AS2-Aktivitäten)

| Aktion | Activity | MIMI | Matrix | E-Mail |
|--------|----------|------|--------|--------|
| senden | `Create` | Nachricht | `m.room.message` | SMTP/JMAP-Auftrag |
| bearbeiten | `Update` (ID der **ersten** Fassung bleibt) | Edit (ersetzt) | `m.replace` | — (Lücke) |
| löschen | `Delete` + Tombstone | leerer Rumpf, ID der ersten Fassung | Redaction | in Papierkorb / endgültig löschen |
| reagieren | `Like` / `EmojiReact`, rückgängig über `Undo` | Reaktion | `m.annotation` | — (Lücke) |
| lesen | `Read` | message-status | `m.receipt` | RFC 9007 MDN |
| zugestellt | Lücke | message-status | — | DSN |

## Threading

- `context` = Unterhaltung (Raum, Mail-Thread, Kommentar-Thread); `inReplyTo` = direkter Elternbeitrag.
- Anzeige flach (Chat) oder als Baum (Kommentare, Mail) — aus denselben Feldern gerendert.

## Projektionen

| Ziel | Projektion |
|------|------------|
| Frontends | Cap'n Proto (ADR 0021) — Frontends sehen nie Protokolle |
| Mail-Versand | MIME + OpenPGP v6 + RFC 9788 Header Protection + Autocrypt |
| Matrix | `matrix-sdk`-Konnektor |
| MIMI | `mimi-content` + OpenMLS |
| Suche | Volltext über die herausgezogenen Felder |

## Offene technische Punkte

- Anzeige der Editier-Historie (alle Fassungen aus dem Protokoll, oder nur die letzte?)
