# MediaWiki

> Kategorie: [wiki](../../index.md)

## Was es ist

MediaWiki ist die Wiki-Engine hinter Wikipedia und den anderen Wikimedia-Projekten. Es ist eine PHP-Webanwendung mit einer relationalen Datenbank. Der Kern liefert einen serverseitig gerenderten Skin (Vector 2022, seit `$wgDefaultSkin` = `vector-2022` der Standard), einen Wikitext-Quelltexteditor, die Erweiterung VisualEditor, die Action API (`api.php`) und eine kleinere REST-API (`rest.php`). Quellen: https://github.com/wikimedia/mediawiki/blob/REL1_46/includes/config-schema.php (DefaultSkin), https://www.mediawiki.org/wiki/API:REST_API

## Versionsangaben

| Angabe | Wert | Quelle |
|------|------|----------|
| Dokumentierte Version | 1.46 (aktuell stabil, Punktrelease 1.46.2) | https://www.mediawiki.org/wiki/MediaWiki_1.46 |
| Veröffentlichungsdatum 1.46.0 | 30. Juni 2026 | https://www.mediawiki.org/wiki/Version_lifecycle |
| Nächste Version | 1.47, LTS, geführt als „future version“ mit Veröffentlichung im November 2026 | https://www.mediawiki.org/wiki/Version_lifecycle |
| Vorherige LTS | 1.43, veröffentlicht 21. Dezember 2024, Ende des Lebenszyklus Dezember 2027 | https://www.mediawiki.org/wiki/Version_lifecycle |

Plan: Das Frontend in unserem Stil sollte jetzt auf 1.46 zielen. Erneut prüfen, sobald 1.47 getaggt ist, denn 1.47 ändert den Standard-Quelltexteditor (siehe `1.46/features.md`).

## Bemerkenswerte Ideen (für unseren Zweck)

- **Action API als stabiler Vertrag.** Jede Operation ist ein Modul mit einer benannten `action` und typisierten Parametern, mit einem tokenbasierten Schreibmodell. Die API ist auf mediawiki.org dokumentiert, und die Parameterliste beschreibt sich selbst (`action=help`, Special:ApiSandbox). Quelle: https://www.mediawiki.org/wiki/API:Main_page
- **Alles ist eine Seite in einem Namensraum.** Diskussionsseiten, Kategorien, Dateien, Vorlagen und Benutzerseiten sind gewöhnliche Seiten in nummerierten Namensräumen. Ein Reiter „Diskussion“ ist ein Link zum gepaarten Namensraum. Quelle: https://www.mediawiki.org/wiki/Help:Keyboard_shortcuts (Zeilen zu Namensräumen), https://github.com/wikimedia/mediawiki/blob/REL1_46/resources/src/mediawiki.util/jquery.accessKeyLabel.js
- **Versionen sind die Einheit der Historie.** Jedes Speichern erzeugt eine Version. Historie, Vergleich und Zurücksetzen arbeiten mit Versionen, nicht mit Dateien. Quelle: https://www.mediawiki.org/wiki/API:RecentChanges
- **Zugriffstasten als Tastaturmodell.** Aktionen haben Einzelbuchstaben-Zugriffstasten, kombiniert mit einer browserspezifischen Modifikatortaste, nicht Ctrl-basierte Tastenkürzel. Quelle: https://www.mediawiki.org/wiki/Help:Keyboard_shortcuts
- **Geschichteter Skin-Aufbau.** Vector 2022 basiert auf Codex-Design-Tokens und CSS-Custom-Properties (ADR 0002). Quelle: https://github.com/wikimedia/mediawiki-skins-Vector/blob/REL1_46/doc/adr/0002-use-css-custom-properties.md
- **Alles austauschbar** über Erweiterungen (VisualEditor, Echo, CodeMirror, ULS). Der Kern ist klein; viele Funktionen der uns bekannten Seiten sind Erweiterungen. Quelle: https://www.mediawiki.org/wiki/Extension:Echo, https://www.mediawiki.org/wiki/Extension:CodeMirror

## Dokumentierte Versionen

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Vorhandene Pflichtdateien |
|---------|------------------------|
| [1.46](1.46/description.md) | 7/7 |
| [latest](latest/description.md) | 6/7 |

### 1.46

| Datei | Inhalt |
|------|----------|
| [description.md](1.46/description.md) | Ausführliche Beschreibung, Abgrenzung, für wen es geeignet ist |
| [features.md](1.46/features.md) | Was das Programm kann — und was nicht |
| [layout.md](1.46/layout.md) | Fensterstruktur, Bereiche, Panels |
| [menus.md](1.46/menus.md) | Menüstruktur, Kontextmenüs, Menüs nach Rolle |
| [shortcuts.md](1.46/shortcuts.md) | Tastenkürzel |
| [api.md](1.46/api.md) | APIs und Protokolle, Authentifizierung, Rate Limits |
| [themes/index.md](1.46/themes/index.md) | Themes: Farben, Typografie, Abstände — was sich nachbauen lässt |
| [events.md](1.46/events.md) | Ereignisse nach außen (Webhooks, Push, Streams) |
| [limits.md](1.46/limits.md) | Bekannte Grenzen |
| [i18n.md](1.46/i18n.md) | Lokalisierung, Schreibrichtung |
| [dependencies.md](1.46/dependencies.md) | Welche unserer Bausteine ein Frontend in diesem Stil braucht |

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

## Verwendete Quellen

- https://www.mediawiki.org/wiki/API:Main_page
- https://www.mediawiki.org/wiki/API:Login
- https://www.mediawiki.org/wiki/API:Watchlist
- https://www.mediawiki.org/wiki/API:RecentChanges
- https://www.mediawiki.org/wiki/API:REST_API
- https://www.mediawiki.org/wiki/Help:Keyboard_shortcuts
- https://www.mediawiki.org/wiki/VisualEditor/Portal/Keyboard_shortcuts
- https://www.mediawiki.org/wiki/MediaWiki_1.46
- https://www.mediawiki.org/wiki/Version_lifecycle
- https://raw.githubusercontent.com/wikimedia/mediawiki/REL1_46/RELEASE-NOTES-1.46
- https://github.com/wikimedia/mediawiki/tree/REL1_46 (config-schema.php, Api/*.php, resources/src/mediawiki.util, languages/i18n/en.json, includes/Rest/coreRoutes.json)
- https://github.com/wikimedia/mediawiki-skins-Vector/tree/REL1_46 (Vector-2022-Templates, JS, LESS-Variablen, configuration.md)
- https://github.com/wikimedia/codex/tree/main/packages/codex-design-tokens/src (Theme- und Modus-Token-Dateien)

Bekannte Lücken in dieser Recherche: mediawiki.org lieferte für API:Etiquette und API:Authentication bei automatischem Abruf HTTP 403. Die Regeln dieser Seiten wurden über die WebFetch-Zusammenfassung gelesen, was eine schwächere Quelle als der Seitentext ist. Wo es darauf ankommt, als „summary-only“ markiert.
