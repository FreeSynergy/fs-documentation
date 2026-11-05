# Dokumente – Standards

> Beleg: `temp/research/documents-standards.md` (2026-11-05). Politik: jüngster gangbarer Standard (ADR 0026).

## Envelope (ActivityStreams 2.0, ✅)

| Begriff | Definition (kurz) | Verwendung |
|---------|-------------------|------------|
| `Article` | "any kind of multi-paragraph written work" | Seite, Block-Dokument |
| `Document` | a document of any kind | Textdatei |
| `Page` | "a Web Page" | für Wiki-Seiten **nicht** benutzt |
| `Collection` / `OrderedCollection` | ungeordnete / geordnete Menge von Einträgen | Bibliothek, Regal / Buch, Kapitel |
| `attachment` | angehängte Objekte | Screenshots, Bilder |
| `content` + `mediaType`; ActivityPub `source` | gerenderter Inhalt; Originalquelle (z. B. Markdown) | Original + Rendering (ADR 0030) |
| FEP-b2b8 Langtext-Entwurf | Entwurf, schließt Buchlänge aus | beobachten |
| FEP-bad1 Versionsgeschichte von Objekten | Entwurf | nah an unserem Aktivitätsprotokoll |

## Text und Blöcke

| Standard | Beleg | Rolle |
|----------|-------|-------|
| CommonMark 0.31.2 (2024-01-28), GFM 0.29-gfm | ✅ | Markdown-Dialekt; Markdown selbst ist nicht standardisiert (RFC 7763/7764 Informational: Media-Type `text/markdown; variant=…`) |
| Block-Dokumentbaum | ❌ **kein offener Standard** (geprüft: ProseMirror, Portable Text, Editor.js, Lexical, BlockSuite, Notion, Block Protocol — alles Projekt-/Anbieterformate) | **eigene Spec**, neutraler Name für die Einreichung bei IETF/W3C (Arbeitstitel offen): stabile Block-IDs, typisierte Blöcke (jeder ein Datentyp mit Repräsentation, ADR 0023), benannte Passagen (ADR 0034), verlustfreier Export nach GFM; Ideen aus Portable Text/ProseMirror und aus den analysierten Wiki-Frontends (ADR 0013) |

## Struktur-Vokabular (nur Export/Import, ADR 0034)

| Standard | Beleg | Rolle |
|----------|-------|-------|
| schema.org `Book`, `Chapter`, `Collection`, `hasPart`/`isPartOf` (= Dublin Core) | ✅ | Abbildung, wenn Sammlungen als Bücher exportiert werden |
| EPUB 3.3 (W3C Rec 2023-05-25); EPUB 3.4 CR (Entwurf 2026-11-02) | ✅ | Exportformat |
| Publication Manifest (W3C Rec 2020-11-10) | ✅ | Manifest für Exporte |
| DITA 1.3 (OASIS) | ✅ (Status 2.0 ⚠️) | Referenz für topicbasierte Hilfe; nicht übernommen |
| IDs kontextbezogener Hilfe | ❌ kein Standard | eigene Spec: Hilfe-Schlüssel |

## Annotationen — eigene Erklärung daneben, Original leiser gestellt

| Standard | Beleg | Rolle |
|----------|-------|-------|
| W3C Web Annotation Data Model / Vocabulary / Protocol (Rec 2017-02-23) | ✅ | verankert eigene Erklärungen, Kommentare und Tags an Text- und Screenshot-Bereichen (`TextQuoteSelector`, `TextPositionSelector`, `SvgSelector`, …) |
| 13 Motivationen (`assessing`, `bookmarking`, `classifying`, `commenting`, `describing`, `editing`, `highlighting`, `identifying`, `linking`, `moderating`, `questioning`, `replying`, `tagging`) | ✅ | `editing` *fordert* eine Änderung nur an; **nichts bedeutet "Original leiser stellen"** |
| eigene Motivationen über `skos:broader` erlaubt | ✅ | **eine** Markierungsmotivation unter `freesynergy.net` (ADR 0028, 0033); Punkt-Anker = einfügen, Spannen-Anker = benennen/ersetzen; Name + Typ (aus dem Repräsentationsregister, ADR 0023) + Wert im Body |
| EPUB Annotations 1.0 (W3C WD 2026-10-15) | ✅ | Profil von Web Annotation für Bücher — verfolgen |

## Versionierung und Zusammenarbeit

| Punkt | Beleg | Anmerkung |
|-------|-------|-----------|
| CRDT-Standard | ❌ keiner | Automerge (`automerge` 0.12, MIT) / `yrs` 0.28 (MIT) nur, falls gemeinsames Live-Editieren nötig wird |
| gitoxide (`gix` 0.90, MIT OR Apache-2.0, pures Rust, 0.x) | ✅ | Kandidat für Dateigeschichte (Gespräch läuft) |

## Lücken → Kandidaten für eigene Spezifikationen

1. **Block-Dokumentformat** (Hauptlücke; neutraler Name für die Einreichung)
2. **Markierung**: Vokabular (ADR 0033) + wie "leiser gestellt" angezeigt wird
3. Collection-Profil auf AS2-Sammlungen (Referenzen zwischen Sammlungen, Sperren)
4. Hilfe-Schlüssel (Werkzeug → Bibliothekseintrag)
