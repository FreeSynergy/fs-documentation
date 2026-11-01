# Geodaten

Orte, Koordinaten und Postadressen. Löst unsere Kritik an der „Westeuropäisierung" der Adressfelder (`mappings.md`): JSContact-`Address`-Komponenten + ISO 19160.

## Standards in dieser Domäne

| Standard | Beleg | Rolle bei FreeSynergy |
|----------|-------|-----------------------|
| **GeoJSON, RFC 7946** | ✅ | kanonisches Modell für Geometrien (Features in `map-view`) |
| **`geo:`-URI, RFC 5870** | ✅ | Koordinaten in JSContact `Address.coordinates` |
| **JSContact `Address`** (RFC 9553 §2.5.1) | ✅ | Postadressen mit Komponententypen (`locality`, `region`, `postcode`, …) |
| **ISO 19160 Addressing** (Teil 1:2015, Teil 4:2023) | ✅ URL geprüft, Inhalt ungelesen | konzeptioneller Rahmen für internationale Postadressen |

## Offene Punkte

- ISO 19160-Inhalt lesen und entscheiden, ob wir nur die JSContact-Komponenten nutzen oder die 19160-Elementnamen mitführen
- Kachel-/Tile-Formate (PBF/MVT) sind Karten-Technik, kein Datenstandard — außerhalb dieser Domäne

## Siehe auch

- [standards.md → Orte, Dateien](../standards.md)
- [kontakt/jscontact](../kontakt/jscontact/beschreibung.md) (Adressen gehören zur Card)
