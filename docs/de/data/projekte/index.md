# Projekte

Boards, Listen, Aufgaben-Beziehungen, Meilensteine, Rollen im Projekt. Das ist die Domäne mit der **größten regulären Lücke**: ❌ kein etablierter Standard gefunden (Kandidaten W6C XML Schema, MSPDI, PMI WBS sind ⚠️ unbelegt — siehe [standards.md](../standards.md)).

## Bestand

| Stück | Beleg | Rolle bei FreeSynergy |
|-------|-------|-----------------------|
| ❌ Projekt-/Board-Struktur | ❌/⚠️ | **unser Spec-Kandidat Nr. 3** (nach Block/Dokument und WoT) |
| **JSCalendar `Task`** | ✅ | Aufgaben als kanonisches Task-Objekt (Wiederverwendung aus [events/](../events/index.md)) |
| **W3C Organization Ontology** (`vocab-org`) | ✅ URL geprüft, Inhalt ungelesen | Rollen/Hierarchie-Baustein für Projektmitgliedschaften |
| **schema.org `Project`** | ⚠️ Existenz nicht verifiziert | vor Verwendung belegen |

## Vorläufige Strukturidee (eigene Festlegung, zur Diskussion)

`Projekt` (Beziehung zu `Team`/`Contact`) → `Board` → `Liste` → `Task` (JSCalendar) mit Relationen (blockiert, dupliziert) und `Milestone` (JSCalendar-`Event`). Beziehungstypen als Enums nach unserer Enum-Regel.

## Offene Punkte

- Reihenfolge der Spec-Arbeit: Block/Dokument zuerst, weil Tasks oft Blöcke referenzieren
- Webhook-/Automatisierungs-Ereignisse (`task.moved`) sind Envelope-Thema, nicht Domänenmodell

## Siehe auch

- [standards.md → Was wir erfinden müssen](../standards.md)
- [events/](../events/index.md) (Task-Standard), [modell-Übersicht](../modelle.md)
