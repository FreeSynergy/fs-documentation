# Projekte

Boards, Listen, Aufgaben-Beziehungen, Meilensteine, Rollen im Projekt. Das ist die Domäne mit der **größten regulären Lücke**: ❌ kein etablierter Standard gefunden (Kandidaten W6C XML Schema, MSPDI, PMI WBS sind ⚠️ unbelegt — siehe [standards.md](../standards.md)).

## Bestand

| Stück | Beleg | Rolle bei FreeSynergy |
|-------|-------|-----------------------|
| ❌ Projekt-/Board-Struktur | ❌/⚠️ | **unser Spec-Kandidat Nr. 3** (nach Block/Dokument und WoT) |
| **ISO 21502:2020** (ISO/TC 258) | ✅ Existenz belegt 2026-11-02 | Prozess-Leitfaden Projektmanagement, **kein Datenformat** — Rollen-/Vokabularreferenz |
| **MSPDI (`mspdi_pj12.xsd`)** | ✅ Existenz belegt 2026-11-02 | De-facto-XML-Import/Export (MS Project); kein offener Standard |
| **JSCalendar `Task`** | ✅ | Aufgaben als kanonisches Task-Objekt (Wiederverwendung aus [events/](../events/index.md)) |
| **W3C Organization Ontology** (`vocab-org`) | ✅ URL geprüft, Inhalt ungelesen | Rollen/Hierarchie-Baustein für Projektmitgliedschaften |
| **schema.org `Project`** | ⚠️ Existenz nicht verifiziert | vor Verwendung belegen |

## Vorläufige Strukturidee (eigene Festlegung, zur Diskussion)

`Projekt` (Beziehung zu `Team`/`Contact`) → `Board` → `Liste` → `Task` (JSCalendar) mit Relationen (blockiert, dupliziert) und `Milestone` (JSCalendar-`Event`). Beziehungstypen als Enums nach unserer Enum-Regel.

## Offene Punkte

- Standardsuche abgeschlossen (2026-11-02): keine offene RFC/W3C-Daten-Spec gefunden; Details in [standards.md → Nachrecherche](../standards.md) — nicht erneut recherchieren
- Reihenfolge der Spec-Arbeit: Block/Dokument zuerst, weil Tasks oft Blöcke referenzieren
- Webhook-/Automatisierungs-Ereignisse (`task.moved`) sind Envelope-Thema, nicht Domänenmodell

## Siehe auch

- [standards.md → Was wir erfinden müssen](../standards.md)
- [events/](../events/index.md) (Task-Standard), [modell-Übersicht](../models.md)
