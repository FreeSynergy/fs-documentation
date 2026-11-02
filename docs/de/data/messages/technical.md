# Nachrichten – Technische Erklärung

## Speicherperspektive

- **Eine Tabelle `message`**: kanonischer Payload = AS2-Objekt-JSON (`Note`/`Article`) (Beschluss 4). Herausgezogene Spalten: `id` (ULID), `type`, `thread_id`, `in_reply_to` (ULID oder IRI), `actor_id`, `created_at`, `updated_at`, `deleted` (Tombstone-Markierung).
- **Zustellungs-Kopien:** `to`/`cc`/`bto`/`bcc` entscheiden, **wo Kopien landen** (Beschluss 2). Intern: Tabelle `message_delivery` (`message_id`, `recipient_id`, `audience` ∈ `to|cc|bto|bcc`). Die eigentliche Autorisierung läuft getrennt über Ressourcen-Rechte — die Audience-Felder ersetzen sie nicht.

## Thread-Regel (eigene Festlegung — in AS2 nicht vollständig definiert)

AS2 kennt `inReplyTo`, aber keinen vollständigen Thread-Mechanismus (offener Punkt in [index.md](index.md)). Vorschlag:

- `thread_id` = ULID des **Wurzel-Beitrags** (eine Spalte, indiziert)
- `in_reply_to` = direkter Eltern-Beitrag (baUM-Struktur)
- Anzeige: flach (Chat) oder gefädelt (Kommentare) — beides aus denselben Spalten gerendert

## Fluss

1. Senden: `Create` (Envelope) mit `Note`; Server prüft Rechte, legt Zustellungs-Kopien an.
2. Ändern: `Update` — Editier-Fenster und Kennzeichnung (`updated` ≠ `created`) sind Produktregel, kein Standard.
3. Löschen: `Delete` + Tombstone (Inhalt weg, Metadaten bleiben — Reichweite noch zu entscheiden).
4. Empfänger-Sync: JMAP-Muster (RFC 8620/8621, ✅) als Referenz für effizientes Abholen/Patchen von JSON-Ressourcen.

## Projektionen

| Ziel | Projektion |
|------|------------|
| Mail-Versand | RFC 5322 (✅ §3.4.1 Adressformat) — SMTP-Transport ist eigenes Thema (kein Datenmodell) |
| JMAP-Endpunkt | `Note` → JMAP-Email-Struktur, Feldmapping offen |
| Suche/Indizes | `content`/`contentMap` Volltext; `name` als Betreff |
| Verschlüsselung | MLS (RFC 9420, ⚠️ in dieser Runde nicht abgerufen) als Kandidat für Gruppen-E2EE |

## Offene technische Punkte

- Editier-Historie: keine AS2-Regel — eigene Festlegung nötig (Revisionen wie im Wiki oder nicht?).
- Zustellungsquittung (gelesen/gesendet): kein Datenstandard; MLS-Deckquittungen ⚠️.
