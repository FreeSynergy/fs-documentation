# Logseq

> Kategorie: [wiki](../../index.md) · Typ: Gliederungswerkzeug / Wissensgraph, datenschutzorientiert · Anbieter: Logseq (Open-Source-Projekt) · Lizenz: AGPL-3.0

## Was es ist
Logseq ist ein quelloffenes Gliederungswerkzeug, in dem jeder Punkt ein Block ist, auf den von anderen Stellen verwiesen werden kann; eine Datenbankversion ersetzt die Version mit Markdown-Dateien.

## Bemerkenswerte Ideen
Warum dieses Programm hier dokumentiert ist (ADR 0013). Nur Funktionsanalyse, in eigenen Worten.

- Blockverweise und Einbettungen: einen einzelnen Block an anderen Stellen referenzieren oder live einbetten; referenzierte Blöcke zeigen, wo sie verwendet werden (verlinkte und unverlinkte Verweise).
- DB-Version: Seiten und Blöcke sind als Knoten mit Schlagwörtern und typisierten Eigenschaften vereint; Schlagwörter erweitern andere Schlagwörter und erben deren Eigenschaften — nahe an Tanas Idee.
- Abfragen (einfach und erweitert), angezeigt als Tabelle, Liste oder Galerie.

## Dokumentierte Versionen
| Version | Dokumentiert am | Status |
|---------|-----------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ teilweise verifiziert, Lücken als „Offen“ markiert |

## Dokumentierte Versionen

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Pflichtdateien vorhanden |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| Datei | Inhalt |
|------|----------|
| [description.md](latest/description.md) | Ausführliche Beschreibung, Abgrenzung, für wen geeignet |
| [features.md](latest/features.md) | Was das Programm kann — und was nicht |
| [layout.md](latest/layout.md) | Fensterstruktur, Bereiche, Panels |
| [menus.md](latest/menus.md) | Menüstruktur, Kontextmenüs, Menüs nach Rolle |
| [shortcuts.md](latest/shortcuts.md) | Tastaturkürzel |
| [api.md](latest/api.md) | APIs und Protokolle, Authentifizierung, Ratenlimits |

⚠️ Fehlende Pflichtdateien: `themes/index.md`
<!-- /gen:versions -->

## Quellen
| Quelle | Art | Abgerufen |
|--------|-----|-----------|
| https://github.com/logseq/logseq | Projekt-Repository | ✅ 2026-11-10 |
| https://raw.githubusercontent.com/logseq/docs/master/db-version.md | offizielle Dokumentation, DB-Version | ✅ 2026-11-10 |
| https://discuss.logseq.com/t/the-difference-between-logseqs-block-embeds-and-block-references/8459 | Beitrag im Community-Forum, Verweise gegenüber Einbettungen | ⚠️ keine Anbieter-Dokumentation 2026-11-10 |
