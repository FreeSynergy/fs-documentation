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
| JSContact | [jscontact/](jscontact/beschreibung.md) |

## Offene Punkte

- `lifecycle` (lead/prospect/customer/churned) existiert in keinem der Standards (❌ belegt) → als JSContact-Erweiterung über `extensions` (⚠️ Mechanismus noch belegen)
- Mapping unserer Alt-Felder (`firstName`/`lastName`, `street`/`city`): siehe [mappings.md → Contact](../mappings.md)

## Siehe auch

- [standards.md](../standards.md) (Belegtabrik, Beschlüsse)
- [mappings.md](../mappings.md) (Feld für Feld)
- [felder.md](../felder.md)
