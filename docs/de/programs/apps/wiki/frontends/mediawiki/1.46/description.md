# MediaWiki 1.46 — Beschreibung

Geprüfte Version: 1.46.2 (aktuell stabil, https://www.mediawiki.org/wiki/MediaWiki_1.46). Support- und Veröffentlichungsdaten: https://www.mediawiki.org/wiki/Version_lifecycle

## Was es tut

- Betreibt ein Wiki: Seiten mit Versionen, Namensräume, Kategorien, Dateien, Vorlagen, Benutzer, Rechte und Protokolle.
- Rendert Wikitext (die eigene Auszeichnungssprache) auf dem Server in HTML. Vorlagen und Parserfunktionen laufen beim Rendern.
- Bietet zwei Bearbeitungswege: den Wikitext-Quelltexteditor und den VisualEditor (eine Erweiterung). Quelle: https://www.mediawiki.org/wiki/VisualEditor/Portal/Keyboard_shortcuts (VisualEditor ist als eigene Editor-Oberfläche vorhanden).
- Stellt zwei HTTP-APIs bereit: die Action API (`api.php`, alle Funktionen) und die REST API (`rest.php`, kleinere Auswahl an Seiten-, Versions- und Suchressourcen). Quelle: https://www.mediawiki.org/wiki/API:REST_API, https://github.com/wikimedia/mediawiki/blob/REL1_46/includes/Rest/coreRoutes.json
- Führt für jede Seite einen Versionsverlauf und ein Protokoll der letzten Änderungen. Quelle: https://www.mediawiki.org/wiki/API:RecentChanges

## Stellung im Feld

MediaWiki ist das Referenzmodell für öffentliche, große Wikis mit vielen Autoren. Seine Stärken und Kosten für uns:

| Aspekt | Fakt (geprüft) | Folge für ein Frontend "im MediaWiki-Stil" |
|--------|----------------|--------------------------------------------|
| Datenmodell | Seite + Versionen + Namensräume; Diskussion ist ein Namensraum | Wir brauchen ein Namensraum-Konzept und Diskussionsseiten als Paare |
| Auszeichnung | Wikitext mit Vorlagen und Parserfunktionen | Unsere Engine speichert ein Dokument (texts.capnp `document` als JSON), daher ist die Auszeichnungsschicht eine Umwandlung, nicht der Speicher |
| API | Große Action API, viele Module, tokenbasierte Schreibvorgänge | Wir verwenden nur die Teilmenge, die wir brauchen, über unseren eigenen Vertrag |
| Skin | Vector 2022 (Standard), serverseitig gerendert mit progressiver Verbesserung | Das Layout kann anhand seiner Struktur nachgebaut werden (siehe `layout.md`) |
| Erweiterungen | Die meisten Funktionen sind Erweiterungen (Echo, CodeMirror, ULS, VisualEditor) | Unsere Funktionsliste muss angeben, welche Teile Kern sind und welche nicht |

Quelle für "Vector 2022 ist der Standard": https://github.com/wikimedia/mediawiki/blob/REL1_46/includes/config-schema.php (Schlüssel `DefaultSkin` = `vector-2022`).

## Für wen es geeignet ist (in unseren eigenen Worten)

Große Wikis mit vielen Autoren, langlebigen Inhalten, vielen Sprachen und öffentlichem Lesen. Der Betrieb ist aufwendig, und die Oberfläche ist für erfahrene Redakteure gebaut. Es ist kein Team-Chat- oder Aufgabenwerkzeug.

## Technische Fakten für später

| Punkt | Wert | Quelle |
|-------|------|--------|
| Sprache | PHP 8.3.0 oder neuer, mit ctype, dom, fileinfo, iconv, intl, mbstring, xml | https://raw.githubusercontent.com/wikimedia/mediawiki/REL1_46/RELEASE-NOTES-1.46 (Abschnitt Compatibility) |
| Datenbank | MariaDB (empfohlen), MySQL 5.7+, PostgreSQL 10+, SQLite 3.8+ | ebenda |
| Standard-DB-Typ in der Konfiguration | `mysql` | config-schema.php, Schlüssel `DBtype` |
| Kern-Installer | MySQL, PostgreSQL, SQLite | `includes/Installer/*` im REL1_46-Baum |

Hinweis: Die bestehende Seite nennt "LDAP" als Kern-Authentifizierungsmethode. LDAP ist nicht im Kern enthalten. Als Kern ungeprüft; als Erweiterung behandeln (siehe `../changelog.md`).
