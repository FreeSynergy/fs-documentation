# Notion

> Kategorie: [wiki](../../index.md)

## Was es ist

Notion ist ein gehosteter All-in-one-Arbeitsbereich für Notizen, Dokumente und Datenbanken, aufgebaut aus typisierten Blöcken. Für dieses Projekt sind die relevanten Teile:

- Seiten aus typisierten Blöcken [S9, S11]
- Datenbanken mit Eigenschaften und Ansichten [S13, S7]
- eine REST-API mit OAuth und internen Tokens [S3, S6]
- Webhooks für Änderungsereignisse [S4, S5]

## Versionsangaben

| Angabe | Wert | Quelle |
|------|------|----------|
| Produkt | Notion Web-/Desktop-App, Stand 2026-11-07 | [S22] (keine Produktversionsnummer vorhanden) |
| API-Version (aktuell) | `2026-03-11` | [S1], [S8] |
| Nächste API-Version | angekündigt, nicht veröffentlicht; macht Notion-Flavoured-Markdown auf Markdown-Endpunkten zum Standard. Name und Datum nicht angegeben | [S8] (Eintrag vom 30. Okt.) |

Notion nummeriert seine App-Versionen nicht. Das Produkt von Notion wird laufend aktualisiert. Der Ordner `2026-11-07/` ist das Stichtagsdatum.

## Bemerkenswerte Ideen

- Jede Zeile, Liste, Tabelle, jedes Bild und jeder Embed ist ein Block. Blöcke können verschachtelt werden. Eine Seite ist ein Baum aus Blöcken [S9, S18].
- Eine Datenbank ist eine Menge von Datenquellen. Seit API-Version `2025-09-03` hat jede Datenquelle ein eigenes Schema, und eine Datenbank kann mehrere Datenquellen enthalten [S7].
- Ansichten (Tabelle, Liste, Board, Kalender, Galerie, Diagramm) zeigen dieselben Daten in unterschiedlichen Layouts [S13].
- Tippen im Markdown-Stil erzeugt Blöcke während der Eingabe, zum Beispiel `# ` für eine Überschrift [S11].
- Die Seitenleiste ist eine linke Navigation mit Reitern (Startseite, Bibliothek, Papierkorb, Einstellungen und weitere) sowie den Bereichen Privat, Geteilt, Teamspaces und Favoriten [S12].
- Gelöschte Seiten bleiben standardmäßig 30 Tage im Papierkorb [S14].

## Dateien in diesem Satz

| Datei | Inhalt |
|------|----------|
| [2026-11-07/description.md](2026-11-07/description.md) | Was es ist, für wen es geeignet ist |
| [2026-11-07/features.md](2026-11-07/features.md) | Was es kann und was nicht |
| [2026-11-07/layout.md](2026-11-07/layout.md) | Seitenleiste, Inhaltsbereich, Seitenkopf |
| [2026-11-07/menus.md](2026-11-07/menus.md) | Seitenleisten-Einträge, Seitenmenü, Blockmenü |
| [2026-11-07/shortcuts.md](2026-11-07/shortcuts.md) | Tastenkürzel |
| [2026-11-07/api.md](2026-11-07/api.md) | REST-API, Authentifizierung, Rate Limits, Paginierung |
| [2026-11-07/themes/index.md](2026-11-07/themes/index.md) | Darstellungsoptionen |
| [2026-11-07/events.md](2026-11-07/events.md) | Webhooks |
| [2026-11-07/limits.md](2026-11-07/limits.md) | Bekannte Grenzen |
| [2026-11-07/dependencies.md](2026-11-07/dependencies.md) | Was ein Frontend in diesem Stil von texts.capnp braucht |
| [changelog.md](changelog.md) | Fehler in den früheren Seiten |

## Dokumentierte Versionen

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Vorhandene Pflichtdateien |
|---------|------------------------|
| [2026-11-07](2026-11-07/description.md) | 7/7 |
| [latest](latest/description.md) | 6/7 |

### 2026-11-07

| Datei | Inhalt |
|------|----------|
| [description.md](2026-11-07/description.md) | Ausführliche Beschreibung, Abgrenzung, für wen es geeignet ist |
| [features.md](2026-11-07/features.md) | Was das Programm kann — und was nicht |
| [layout.md](2026-11-07/layout.md) | Fensterstruktur, Bereiche, Panels |
| [menus.md](2026-11-07/menus.md) | Menüstruktur, Kontextmenüs, Menüs nach Rolle |
| [shortcuts.md](2026-11-07/shortcuts.md) | Tastenkürzel |
| [api.md](2026-11-07/api.md) | APIs und Protokolle, Authentifizierung, Rate Limits |
| [themes/index.md](2026-11-07/themes/index.md) | Themes: Farben, Typografie, Abstände — was sich nachbauen lässt |
| [events.md](2026-11-07/events.md) | Ereignisse nach außen (Webhooks, Push, Streams) |
| [limits.md](2026-11-07/limits.md) | Bekannte Grenzen |
| [dependencies.md](2026-11-07/dependencies.md) | Welche unserer Bausteine ein Frontend in diesem Stil braucht |

### latest

| Datei | Inhalt |
|------|----------|
| [description.md](latest/description.md) | Ausführliche Beschreibung, Abgrenzung, für wen es geeignet ist |
| [features.md](latest/features.md) | Was das Programm kann — und was nicht |
| [layout.md](latest/layout.md) | Fensterstruktur, Bereiche, Panels |
| [menus.md](latest/menus.md) | Menüstruktur, Kontextmenüs, Menüs nach Rolle |
| [shortcuts.md](latest/shortcuts.md) | Tastenkürzel |
| [api.md](latest/api.md) | APIs und Protokolle, Authentifizierung, Rate Limits |

⚠️ Fehlende Pflichtdateien: `themes/index.md`
<!-- /gen:versions -->

## Quellen

Abgerufen 2026-11-07. Jede Angabe nennt die Seite, aus der sie stammt. Angaben nur aus Suchausschnitten sind als „snippet“ markiert.

| ID | URL |
|----|-----|
| S1 | https://developers.notion.com/reference/versioning |
| S2 | https://developers.notion.com/reference/request-limits |
| S3 | https://developers.notion.com/guides/get-started/authorization |
| S4 | https://developers.notion.com/reference/webhooks |
| S5 | https://developers.notion.com/reference/webhooks-events-delivery |
| S6 | https://developers.notion.com/reference/intro |
| S7 | https://developers.notion.com/guides/get-started/upgrade-guide-2025-09-03 |
| S8 | https://developers.notion.com/page/changelog |
| S9 | https://developers.notion.com/reference/block |
| S10 | https://developers.notion.com/reference/post-search |
| S11 | https://www.notion.com/help/keyboard-shortcuts |
| S12 | https://www.notion.com/help/navigate-with-the-sidebar |
| S13 | https://www.notion.com/help/intro-to-databases |
| S14 | https://www.notion.com/help/duplicate-delete-and-restore-content |
| S15 | https://www.notion.com/help/customize-and-style-your-content |
| S16 | https://developers.notion.com/reference/capabilities |
| S17 | https://developers.notion.com/reference/query-a-data-source |
| S18 | https://developers.notion.com/reference/patch-block-children |
| S19 | https://developers.notion.com/reference/retrieve-a-page |
| S20 | https://developers.notion.com/reference/post-page |
| S21 | https://developers.notion.com/reference/trash-page |
| S22 | https://www.notion.com/product |
| S23 | https://www.notion.so/help/appearance-settings (nur Ausschnitt, Seite nicht abgerufen) |

Seiten, die 404 lieferten und nicht als Quellen verwendet werden: `notion.com/help/intro-to-notion`, `notion.com/help/trash`, `notion.com/help/customize-your-appearance-in-notion`, `developers.notion.com/reference/search-limitations`, `developers.notion.com/reference/get-pages`. Der Artikel zur Seitenleiste (S12) war unter `navigate-with-the-sidebar` zu finden.
