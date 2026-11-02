# Projekte – Standards

> Belege stehen zentral in [standards.md](../standards.md) — **nichts aus dem Web nachladen.** Recherche abgeschlossen 2026-11-02.

## Ergebnis der Standardsuche (2026-11-02)

| Kandidat | Beleg | Einordnung |
|----------|-------|------------|
| **RFC / W3C / ISO-Datenformat für Boards & Tasks** | ❌ nichts gefunden | **keine offene Daten-Spec** → eigene Spec, Spec-Kandidat Nr. 3 |
| **ISO 21502:2020 „Project, programme and portfolio management — Guidance on project management“** (ISO/TC 258) | ✅ Existenz belegt | **Prozess-Leitfaden, kein Datenformat**; nützlich als Rollen-/Vokabularreferenz |
| **MSPDI — Microsoft Office Project 2007 XML Data Interchange Schema (`mspdi_pj12.xsd`)** | ✅ Existenz belegt | De-facto-XML-Import/Export (Tasks, Kalender; Dauern in Zehntelsekunden); kein offener Standard |
| **W6C XML Schema** | ⚠️ weiterhin unbelegt | nicht verwenden bis belegt |

## Wiederverwendete Bausteine (✅)

| Baustein | Beleg | Nutzung |
|----------|-------|---------|
| **JSCalendar `Task`** (RFC 8984) | ✅ | kanonisches Task-Objekt — siehe [events/standards.md](../events/standards.md) für die Feldliste |
| **JSCalendar `Event`** (RFC 8984) | ✅ | Meilensteine |
| **ActivityStreams 2** (W3C) | ✅ | Envelope für `task.moved` etc. (Beschluss 2) |

## Weitere Kandidaten (⚠️ ungeprüft, bewusst nicht nachgeladen)

| Kandidat | Status |
|----------|--------|
| W3C Organization Ontology (`vocab-org`) | ✅ URL geprüft, **Inhalt ungelesen** — Baustein für Rollen/Hierarchie |
| schema.org `Project` | ⚠️ Existenz nicht verifiziert |

## Eigene Festlegung (zur Diskussion — Spec-Kandidat Nr. 3)

Kleine, offene Kernmodelle: `Project`, `Board`, `List`, `task_link`, `Relation` mit Enum `kind ∈ {blocks, duplicates, references, parent}` (Enum-Regel: lowercase, Singular). **Erweitern statt erfinden (Beschluss 5):** Task-Felder werden nicht dupliziert; Projekte-Felder leben nur in den Struktur-Modellen.
