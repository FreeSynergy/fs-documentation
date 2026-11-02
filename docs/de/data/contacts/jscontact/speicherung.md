# JSContact – Speicherung

Entsprechend Beschluss 4 in [standards.md](../../standards.md) ist das **belegte Standardmodell die Quelle der Wahrheit**: Kontakte werden feldgenau als JSContact-Objekt (RFC 9553) gespeichert — nicht in einer eigenen Zwischentabelle, aus der das Modell nur projiziert wird. Alle anderen Formate (vCard, jCard, protobuf, JSON-LD/AS2) sind abgeleitete Projektionen.

## Grundregeln

| Punkt | Regel | Beleg/Beschluss |
|-------|-------|-----------------|
| Kanonische Form | eine Card = ein JSContact-Objekt, JSON-feldgenau | Beschluss 1, 4 |
| `uid` | bleibt über alle Projektionen und Exporte identisch | RFC 9553 §2.3 |
| Interne ID | ULID (opaque, sortierbar) | Beschluss 3 |
| Externer Handle | absoluter IRI `https://<instanz>/kontakt/<ulid>` | Beschluss 3 (AS2 Core §4.1) |
| Teilweise Änderung | JSON Patch (RFC 6902) bzw. `PatchObject` aus RFC 9553; Pfade wie `emails/work/value` | [api.md](../../api.md) |
| Eigene Felder | nur über `extensions` (z. B. `lifecycle`) — niemals durch umbenannte oder zweckentfremdete Standardfelder | Beschluss 5 |

## Speicherungsform

- Die Card wird als Ganzes persistiert (JSON-Spalte bzw. Dokument), damit die Standardstruktur ohne Feldzerrissung erhalten bleibt
- Indizierbare Extraktionen (`uid`, Name-Komponenten, Organisationsname, `directories`) dürfen als abgeleitete Spalten/Indexes vorhanden sein — sie sind Projektionen, keine Quelle
- Revisionen: Der Standard definiert kein Revisionsmodell; FreeSynergy führt Änderungen als Versionierungsebene außerhalb der Card (Änderungsprotokoll pro `uid`), Export bleibt eine einzelne valide Card

## Austauschpfade (abgeleitete Projektionen)

| Richtung | Format | Mechanismus |
|----------|--------|-------------|
| Export/Import Datei | vCard 4.0 (RFC 6350) | Brücke über RFC 9554, verlustlos für die belegten Eigenschaften |
| Export/Import JSON-vCard | jCard (RFC 7095) | Konvertierung vCard ↔ JSON |
| Sync mit Clients | CardDAV (RFC 6352) | Karte ↔ vCard-Resource pro Kontaktordner (`directories`) |
| Envelope nach außen | AS2/ActivityPub (`Create`/`Update`/`Delete`) | Card als Domänen-Payload im Objekt; `to`/`cc` steuern Offenlegung, nicht Zugriff (Beschluss 2) |
| intern | protobuf/gRPC | aus dem Standardmodell generiert (Beschluss 4) |

## Offene Punkte (Standards-konform zu klären, nicht zu erfinden)

- `lifecycle` als `extensions`-Eintrag: JSON-Schema/Mechanismus der Erweiterung noch belegen (⚠️, siehe [kontakt/index.md](../index.md))
- Revisions-/Löschzustände (`status`) im Zusammenspiel mit CardDAV-Sync festlegen
- `media`-Objekte: Data-URI inline oder Auslagerung in Objektspeicherung mit URL — beides RFC-9553-konform, Entscheidung dokumentieren

## Siehe auch

- [beschreibung.md](beschreibung.md) – was JSContact ist
- [kontakt/index.md](../index.md) – Domäne Kontakte
- [standards.md](../../standards.md) – Beschlüsse 1–5
- [mappings.md](../../mappings.md) – Mapping auf Alt-Felder und Zielsysteme
- [api.md](../../api.md) – Patch- und Fehlerformat
