# Projekte – Beschreibung

**Was diese Domäne ist:** Boards, Listen, Meilensteine, Projektrollen und **Beziehungen zwischen Aufgaben** (blockiert, dupliziert, referenziert). Das ist unsere Domäne mit der **größten regulären Lücke**: ❌ es gibt keinen offenen RFC/W3C/ISO-**Datenstandard** dafür (Recherche abgeschlossen 2026-11-02, Belege in [standards.md → Nachrecherche](../standards.md)).

**Was sie abdeckt:**

- `Projekt` als Hülle (Beziehung zu Team und beteiligten Kontakten)
- `Board` → `Liste` → Position/Reihenfolge
- `Relation` zwischen Aufgaben: `blocks`, `duplicates`, `references` (eigene Enum-Festlegung, zur Diskussion)
- `Milestone` (als JSCalendar-`Event` realisiert)
- Rollen im Projekt (Owner, Mitwirkender, Beobachter)

**Was sie NICHT abdeckt:** Die Aufgaben-**Daten** selbst. Ein Task ist ein unveränderliches JSCalendar-`Task`-Objekt aus [events/](../events/index.md). Diese Domäne ergänzt nur die Struktur darum herum.

**Abgrenzung:**

| Thema | Wo es liegt |
|-------|-------------|
| Task-Inhalt (Titel, Fälligkeit, Fortschritt) | [events/](../events/index.md) (JSCalendar, ✅) |
| Personen und Organisationen | [people/](../people/index.md) |
| Termine/Meilensteine im Kalender | [events/](../events/index.md) |
| Prozessführung (Phasen, Verantwortung) | ISO 21502 ist **Prozess-Leitfaden, kein Datenformat** (✅ belegt 2026-11-02) |

**Standard-Status:** eigene Spec = **Spec-Kandidat Nr. 3** (nach Block/Dokument und WoT). Import/Export-Gegenstellen: MSPDI (`mspdi_pj12.xsd`, ✅ Existenz, De-facto-Format).
