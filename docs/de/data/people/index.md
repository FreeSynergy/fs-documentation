# Kontaktdaten

Personen, Firmen und ihre Erreichbarkeiten. Diese Domäne ist vollständig standardisiert: wir übernehmen **JSContact** als kanonisches Speicher- und Austauschmodell (Beschluss 1).

## Standards in dieser Domäne

| Standard | Beleg | Rolle bei FreeSynergy |
|----------|-------|-----------------------|
| **JSContact, RFC 9553** | ✅ | **kanonisches Modell** (Speicher + API-Payload) |
| **vCard Extensions for JSContact, RFC 9554** | ✅ | verlustlose Brücke JSContact ↔ vCard |
| **vCard 4.0, RFC 6350** | ✅ | Datei-Austausch (Import/Export) |
| **jCard, RFC 7095** | ✅ | JSON-Form von vCard |
| **CardDAV, RFC 6352** | ✅ | Zugriff und Sync auf Kontaktordner |

## Standard-Verzeichnisse

| Standard | Verzeichnis |
|----------|-------------|
| JSContact | [jscontact/](jscontact/description.md) |

## Offene Punkte

- Envelope: AS2 `Profile` mit `describes` (ADR 0020) — siehe [technical.md](technical.md)
- `lifecycle` existiert in keinem der Standards (❌) → Anbieter-Eigenschaft `freesynergy.net:lifecycle` (✅ RFC 9553 §1.8.1, ADR 0028)
- Dieselbe Person in mehreren Programmen: Verknüpfung über `Relationship`, kein Merge (ADR 0019) — Relation `owl:sameAs`; sensible Daten sind markiert und werden nie automatisch verknüpft (ADR 0029)
- Mapping unserer Alt-Felder (`firstName`/`lastName`, `street`/`city`): siehe [mappings.md → Contact](../mappings.md)

## Siehe auch

- [standards.md](../standards.md) (Belegtabelle, Beschlüsse)
- [mappings.md](../mappings.md) (Feld für Feld)
- [fields.md](../fields.md)
