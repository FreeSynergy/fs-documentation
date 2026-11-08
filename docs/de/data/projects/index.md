# Projekte

Boards, Listen, Aufgaben-Beziehungen, Meilensteine, Rollen im Projekt. Das ist die Domäne mit der **größten regulären Lücke**: ❌ kein etablierter Standard gefunden (die Kandidaten W6C XML Schema, MSPDI, PMI WBS sind ⚠️ nicht belegt — siehe [standards.md](../standards.md)).

## Bestand

| Baustein | Beleg | Rolle in FreeSynergy |
|-------|----------|---------------------|
| ❌ Projekt-/Board-Struktur | ❌/⚠️ | **unser Spezifikationskandidat Nr. 3** (nach Block/Dokument und WoT) |
| **ISO 21502:2020** (ISO/TC 258) | ✅ Existenz belegt 2026-11-02 | Prozessleitfaden für Projektmanagement, **kein Datenformat** — Referenz für Rollen und Vokabular |
| **MSPDI (`mspdi_pj12.xsd`)** | ✅ Existenz belegt 2026-11-02 | de-facto XML-Import/-Export (MS Project); kein offener Standard |
| **JSCalendar `Task`** | ✅ | Aufgaben als kanonisches Aufgabenobjekt (übernommen aus [events/](../events/index.md)) |
| **W3C Organization Ontology** (`vocab-org`) | ✅ URL geprüft, Inhalt nicht gelesen | Baustein für Rollen und Hierarchie in Projektmitgliedschaften |
| **schema.org `Project`** | ⚠️ Existenz nicht geprüft | vor der Nutzung belegen |

## Vorläufige Strukturidee (unsere eigene Entscheidung, zur Diskussion offen)

`project` (Beziehung zu `Team`/`Contact`) → `board` → `list` → `task` (JSCalendar) mit Beziehungen (blockiert, Duplikat) und `milestone` (JSCalendar `Event`). Beziehungsarten als Enums nach unserer Enum-Regel.

## Offene Punkte

- Standardsuche abgeschlossen (2026-11-02): keine offene RFC-/W3C-Datenspezifikation gefunden; Details in [standards.md → Folgerecherche](../standards.md) — nicht erneut recherchieren
- Reihenfolge der Spezifikationsarbeit: zuerst Block/Dokument, weil Aufgaben oft auf Blöcke verweisen
- Webhook-/Automatisierungsereignisse (`task.moved`) sind ein Umschlag-Thema, kein Fachmodell

## Siehe auch

- [standards.md → Was wir erfinden müssen](../standards.md)
- [events/](../events/index.md) (Aufgaben-Standard), [Modell-Übersicht](../models.md)
