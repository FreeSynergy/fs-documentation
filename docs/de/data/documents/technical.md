# Dokumente – technische Erklärung

Entscheidungen: ADR 0020/0030 (Original + Envelope + Protokoll), ADR 0023 (Code- und Block-Editor), ADR 0031.

## Speicherung (ADR 0034)

| Baustein | Original | Envelope | Inhalt |
|----------|----------|----------|--------|
| Textdatei | Bytes, wie geschrieben/importiert | `Document` (`mediaType`); Markdown: `Article` + `source` | gerendertes HTML abgeleitet, nie als Wahrheit gespeichert |
| Seite (Block-Dokument) | — (hier geboren) | `Article`, `mediaType` = Blockformat | Blockbaum-JSON, stabile Block-IDs |
| Passage | — | benannte Markierung (ADR 0033) auf einer Spanne, oder ein Block mit Namen | wird referenziert, wo immer sie wiederverwendet wird |
| Sammlung | — | `Collection` / `OrderedCollection` | Item-IRIs, Referenzen auf andere Sammlungen, `locked`-Zustand |
| Regal | — | Instanzgrenze | eigenes `fs-store`, eigene Rechte |
| Markierung (Erklärung, Variable, …) | — | Web Annotation, eine `freesynergy.net`-Motivation | Anker (Punkt/Spanne/Bildbereich) + Name + Typ + Wert |

- IDs UUIDv7 (ADR 0027); sensible Markierung greift (ADR 0029).
- **Leiser stellen:** eine Spannen-Markierung mit Ersetzungswert stellt das Original für ihre
  Leserschaft leiser; `Undo`/`Delete` der Markierung bringt es zurück. Das Original wird nie geändert.

## Protokoll-Abbildung (AS2)

| Aktion | Activity |
|--------|----------|
| Seite / Sammlung anlegen | `Create` |
| bearbeiten | `Update` (Block-Diff im Payload) |
| Seite/Sammlung zu einer Sammlung hinzufügen | `Add` (target = Sammlung) / `Remove` |
| Sammlung sperren / entsperren | `Update` (Zustand) |
| markieren (einfügen, benennen, ersetzen) | `Create` auf der Markierung |
| Markierung entfernen / zurückholen | `Undo` / `Delete` auf der Markierung |

## Hilfe in jedem Werkzeug (ADR 0031)

- Jedes Werkzeug deklariert einen **Hilfe-Schlüssel**; die Bibliothek löst ihn in einen Eintrag auf (eigene Spec, Lücke 4).
- Geöffnet in einem Fenster/Werkbank (Code- oder Block-Editor, Lesemodus), nicht in der Wiki-App.

## Crates

| Bedarf | Crate | Lizenz |
|--------|-------|--------|
| Markdown parsen/rendern | `pulldown-cmark` 0.13 (Quellpositionen über `into_offset_iter`); `markdown-rs` inaktiv seit 2025-04 | MIT |
| Text-Puffer | `ropey` | MIT OR Apache-2.0 |
| Syntax-Highlighting | `syntect` 5.3 mit `default-features = false, features = ["default-fancy"]` (pures Rust; die Voreinstellung zieht Oniguruma = C) + `two-face`-Grammatiken | MIT |
| Struktur (Folden, Gliederung) für eigene Formate | `logos` + `rowan`, oder `lelwel` | MIT/Apache |
| ~~tree-sitter~~ | ausgeschlossen: Grammatiken sind C, auch mit `tree-sitter-c2rust` (Nutzer 2026-11-05, `temp/research/blinc-health-and-parsers.md`) | |
| Formatierung | dprint (MIT), Biome (MIT OR Apache-2.0, crates.io veraltet) | |
| Export | EPUB 3.3 / GFM-Schreiber — Crates noch zu wählen | |
| Geschichte | `gix` 0.90 (Kandidat) | MIT OR Apache-2.0 |

`comrak` ist BSD-2-Clause — permissiv, aber außerhalb unserer Lizenzregel; nicht benutzt.
