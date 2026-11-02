# Kontaktdaten – Technische Erklärung

## Speicherperspektive

- **Eine Tabelle `contact`**, eine Zeile pro `Card`. Der kanonische Payload ist das **JSContact-JSON selbst** (Beschluss 4: das Standardmodell ist die Quelle der Wahrheit, nicht eine erfundene Tabellenform).
- Spalten, die aus der Card **herausgezogen** werden (für Indizes/Filter): `id` (ULID), `uid` (JSContact-`uid`, für Austausch-Stabilität), `kind` (Rolle: `individual`/`organization`/`group`/`device` — ⚠️ exakte Enum-Werte aus RFC 9553 noch Feld für Feld belegen), `name_sort` (aus `name.components` abgeleitet), `created_at`, `updated_at`, `sync_token`.
- **IDs:** intern ULID, extern `https://<instanz>/contacts/<ulid>` (Beschluss 3).

## Schlüssel und Verknüpfungen

- `contact.id` ← Referenz von überall: `events`-Teilnehmer verweisen auf `email`/`sendTo`, `login`-Konto verweist auf die **Selbst-Card** (Beschluss-Kandidat 6), `profile`-Projektionen lesen die Card.
- `cryptoKeys` in der Card ist das Andockfeld für Schlüssel aus [identity/](../identity/index.md) (vCard `KEY` ↔ JSContact `cryptoKeys`, ✅ Brücke RFC 9554).

## Fluss

1. **Erstellen:** `Create` (AS2-Envelope, Beschluss 2) mit JSContact-Payload → Validierung gegen RFC 9553 → Store.
2. **Ändern:** JSON-Patch (RFC 6902) bzw. das **JSContact-eigene Patch-Objekt** (`PatchObject`, RFC 9553, ✅) → `Update` nach außen.
3. **Sync:** Clients nutzen `sync_token` (Muster wie RFC 6578); CardDAV-RFCS (RFC 6352, ✅) für Interop mit externen Adressbüchern.
4. **Export/Import:** jCard (RFC 7095) / vCard (RFC 6350) **verlustlos** über RFC 9554.

## Projektionen

| Ziel | Projektion |
|------|------------|
| [profile/](../profile/index.md) | Teilmenge der Felder, publikumsgesteuert (Verlustfreiheit wird dort bewusst aufgehoben) |
| [events/](../events/index.md) | `Participant`-Objekt aus Card-Anteilen (`name`, `email`, `language`) |
| CRM-Skins | `lifecycle` u. a. als `extensions`-Eintrag (⚠️) |
| gRPC/protobuf intern | generiert aus dem kanonischen JSON (Beschluss 4) |

## Zusammenführen und Löschen

- Zwei Karten für dieselbe Person: `merge` erzeugt eine Karte, die alte `uid` bleibt als Alias erhalten (eigene Festlegung, zur Diskussion — kein Standard belegt).
- Löschen ist ein `Delete` im Envelope; [identity/](../identity/index.md)-Beglaubigungen auf die gelöschte Karte bleiben als gebrochene Referenzen sichtbar (bewusst: Vertrauen verschwindet nicht still).
