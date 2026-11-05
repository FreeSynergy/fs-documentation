# Kontaktdaten – Technische Erklärung

## Speicherperspektive (ADR 0019, 0020)

- **Objekt = Envelope + Inhalt + Protokoll.**
  - *Envelope* (AS2 **`Profile`**, ✅): `id`, `type: Profile`, `describes` (die Schauspieler-IRI oder DID der Person, falls bekannt), `attributedTo` (wer diese Karte geschrieben hat), `to`/`cc`/`bto`/`audience` (wer sie sehen darf), `published`, `updated`.
  - *Inhalt*: das **JSContact-`Card`-JSON** (RFC 9553) — das Standardmodell ist die Quelle der Wahrheit.
  - *Protokoll*: AS2-Aktivitäten `Create`/`Update`/`Delete` pro Karte, von `fs-store` dieselbe Transaktion geschrieben.
- Spalten, die für Indizes **herausgezogen** werden: `id`, `uid` (JSContact), `kind` (✅ `individual`/`group`/`org`/`location`/`device`/`application`), `describes`, `name_sort` (aus `name.components`), E-Mails/Telefonnummern (normalisiert, für Hub-Zuordnung), `created_at`, `updated_at`.
- **IDs:** UUIDv7 (RFC 9562, ADR 0027); extern `https://<instanz>/contacts/<id>`.
- **Sensible Felder** (z. B. sexuelle Orientierung) sind markiert; markierte Daten werden nie automatisch verknüpft, verlassen das Gerät nur mit ausdrücklicher Freigabe und werden verschlüsselt gespeichert (ADR 0029).

## Schlüssel und Verknüpfungen

- `contact.id` ← Referenz von überall: `events`-Teilnehmer verweisen auf `email`/`sendTo`, das `login`-Konto verweist auf die **Selbst-Card** (Beschluss-Kandidat 6), `profile`-Projektionen lesen die Card.
- `cryptoKeys` in der Card ist das Andockfeld für Schlüssel aus [identity/](../identity/index.md) (vCard `KEY` ↔ JSContact `cryptoKeys`, ✅ Brücke RFC 9554).

## Fluss

1. **Erstellen:** `Create` (AS2-Envelope, Beschluss 2) mit JSContact-Payload → Validierung gegen RFC 9553 → Store.
2. **Ändern:** JSON-Patch (RFC 6902) oder das **JSContact-eigene Patch-Objekt** (`PatchObject`, RFC 9553, ✅) → `Update` nach außen.
3. **Sync:** Clients nutzen `sync_token` (Muster wie RFC 6578); CardDAV-RFCs (RFC 6352, ✅) für Interop mit externen Adressbüchern.
4. **Export/Import:** jCard (RFC 7095) / vCard (RFC 6350) **verlustlos** über RFC 9554.

## Projektionen

| Ziel | Projektion |
|------|------------|
| [profile/](../profile/index.md) | Teilmenge der Felder, publikumsgesteuert (Verlustfreiheit wird dort bewusst aufgehoben) |
| [events/](../events/index.md) | `Participant`-Objekt aus Card-Anteilen (`name`, `email`, `language`) |
| CRM-Frontends | `lifecycle` als Anbieter-Eigenschaft `<domain>:lifecycle` (✅ Mechanismus, RFC 9553 §1.8.1) |
| intern Cap'n Proto (ADR 0021) | aus dem kanonischen JSON generiert (Beschluss 4) |

## Dieselbe Person in mehreren Programmen (ADR 0019)

- Kein Standard definiert Zusammenführen (❌ geprüft 2026-11-05). Unsere Regel: **verknüpfen statt zusammenführen.**
- Der Hub findet Kandidaten (gleiche normalisierte E-Mail/Telefonnummer, gleiches `describes`/DID) und schlägt sie vor; ein Mensch bestätigt.
- Eine bestätigte Verknüpfung wird als AS2-**`Relationship`** zwischen den beiden Karten gespeichert (Relation `owl:sameAs`, ADR 0029); bei Karten mit sensiblen Feldern wird nie automatisch vorgeschlagen. Beide Karten bleiben bestehen, Ansichten dürfen sie kombiniert zeigen. Rückgängig = `Undo` auf der Relationship.
- `relatedTo` wird dafür **nicht** benutzt — seine Werte beschreiben Beziehungen zwischen *verschiedenen* Personen (✅).

## Löschen

- Löschen ist ein `Delete` im Protokoll; Beglaubigungen aus [identity/](../identity/index.md) auf die gelöschte Karte bleiben als gebrochene Referenzen sichtbar (bewusst: Vertrauen verschwindet nicht still).
