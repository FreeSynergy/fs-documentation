# Geodaten – Beschreibung

**Was diese Domäne ist:** Orte als **Geometrien und Features** (Karten, Punkte, Wege) sowie das **Komponentenmodell von Postadressen**. Kanonisches Modell: **GeoJSON** (RFC 7946, ✅) für Geometrien; **JSContact-`Address`** (RFC 9553 §2.5.1, ✅) für Postadressen; konzeptioneller Rahmen **ISO 19160** (✅ URL geprüft, Inhalt ungelesen).

**Was sie abdeckt:**

- Features für Karten-Ansichten (`map-view`): Punkt, Linie, Polygon als GeoJSON
- Koordinaten-Angabe über `geo:`-URI (RFC 5870, ✅)
- Internationale Postadressen **ohne Westeuropäisierung**: Adressen bestehen aus benannten Komponenten (`locality`, `region`, `postcode`, `country`, …), nicht aus festen Feldern wie „Straße + Hausnummer“
- Verknüpfung von Features mit anderen Domänen (Termin-`locations`, Karten-Marker auf Contacts)

**Abgrenzung zu anderen Domänen:**

| Thema | Wo es liegt | Warum |
|-------|-------------|-------|
| Postadresse **einer Person/Organisation** | [people/](../people/index.md) (JSContact `Address`) | Die Adresse ist Teil der Card; diese Domäne liefert nur das Adress-**Modell** |
| Ort **an einem Termin** | [events/](../events/index.md) (JSCalendar `locations`) | Der Termin referenziert einen Ort, besitzt ihn aber nicht |
| Kachel-/Tile-Formate (PBF/MVT) | außerhalb (Karten-Technik) | Darstellungsformat, kein Datenstandard |

**Warum das eine eigene Domäne ist:** Das Adress-Komponentenmodell und die Geometrien werden domänenübergreifend gebraucht (contacts, events, projects, marketplace). Ein Feld „addresse“ pro Modul zu kopieren verstößt gegen Regel Nr. 1 (ein Feld, ein Owner).
