# Nachrichten – Standards

> Belege stehen zentral in [standards.md](../standards.md) — **nichts aus dem Web nachladen.**

## Kernstandard

| Standard | Beleg | Rolle |
|----------|-------|-------|
| **Activity Streams 2.0 Vocabulary (W3C)** | ✅ | kanonisches Payload: `Note`, `Article`; Mehrsprachigkeit `contentMap`/`nameMap`; Audience `to`/`cc`/`bto`/`bcc` (Core, ✅) |
| **ActivityPub** (Envelope) | ✅ (Core-Regeln belegt; Signatur-Mechanismen ❌ siehe Korrekturliste) | `Create`/`Update`/`Delete` auf `Note`/`Article` (Beschluss 2) |

## Referenzen und Interop

| Standard | Beleg | Rolle |
|----------|-------|-------|
| **JMAP, RFC 8620/8621** | ✅ | Referenz für sauberes Adressieren/Patchen/Synchronisieren von JSON-Ressourcen |
| **Mail-Adressformat, RFC 5322 §3.4.1** | ✅ | Absender-/Empfängeradressen in Projektionen |
| **W3C Web Annotation Model** | ✅ | Kommentare/Tags an Textteilen (`TextQuoteSelector`, `body`/`target`) — entlastet die Message-Domäne |
| **XMPP (RFC 6120/6121)** | ⚠️ ungeprüft | Interop mit Chat-Alt-Systemen, vor Verwendung belegen |
| **MLS, RFC 9420** | ⚠️ in dieser Runde nicht abgerufen | Kandidat Ende-zu-Ende-Verschlüsselung von Gruppen |

## AS2-Felder, die wir belegen (✅ Core/Vocabulary gelesen)

`@context`, `type`, `id` (absoluter IRI), `actor`, `object`, `target`, `inReplyTo`, `name`, `nameMap`, `content`, `contentMap`, `summary`, `to`, `cc`, `bto`, `bcc`, `published`, `updated`, `url`, `Tag` (als Link-Erweiterung: `Hashtag` ist **nicht** im AS2-Kern, ❌ belegt — Mastodon-Erweiterung).

## Offene Standard-Punkte

- **Threading:** AS2 definiert `inReplyTo`, aber keinen Thread-Abschluss → eigene Regel (in [technical.md](technical.md))
- **Editier-Historie, Lesequittungen:** kein Standard → eigene Festlegung
- Signatur-Mechanismen für ActivityPub-Objekte: ❌ alte Referenz war 404 — neu recherchieren, bevor Signatur spezifiziert wird
