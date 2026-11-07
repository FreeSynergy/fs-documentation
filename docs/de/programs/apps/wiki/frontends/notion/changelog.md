# Änderungsprotokoll

## 2026-11-07: neu geschrieben aus offiziellen Quellen

Die früheren Seiten waren aus dem Gedächtnis geschrieben; diese Aussagen waren falsch.

Geprüft gegen die offiziellen Quellen in [index.md](index.md) (abgerufen 2026-11-07). Status: **falsch** (offizielle Quelle widerspricht), **nicht verifiziert** (keine Quelle gefunden; entfernt oder noch zu prüfen), **veraltet** (war wahr, ist nicht mehr aktuell).

### index.md

| Aussage | Status | Richtige Tatsache | Quelle |
|-----------|--------|--------------|--------|
| „Notion is an all-in-one platform for notes, documentation and collaboration.“ | veraltet | Notion nennt sich einen KI-Arbeitsbereich für Teams und ihre Agenten, mit Erfassen, Finden und Automatisieren | [S22] |
| Abschnitt „Notable ideas“ leer | Lücke | Im neuen Index ausgefüllt | — |
| Dokumentierte Versionen: `latest` | Lücke | API-Version 2026-03-11; die App hat keine Versionsnummer | [S1], [S8] |

### latest/description.md

| Aussage | Status | Richtige Tatsache | Quelle |
|-----------|--------|--------------|--------|
| Backend Node.js, PostgreSQL; Frontend React, TypeScript | nicht verifiziert | In den offiziellen Dokumenten nicht genannt | — |
| Hosting nur SaaS | teilweise | Gehosteter Dienst; auf den offiziellen Seiten keine Option zum Selbsthosten gefunden | — |
| Vorteile: 100+ Einbettungen, starke mobile Apps | nicht verifiziert | Einbettungstypen existieren [S9], Anzahl und Aussagen zu Mobil-Apps nicht geprüft | — |
| Vergleiche mit Tango.io, Confluence, XWiki | nicht verifiziert | Nicht in offiziellen Quellen; entfernt | — |
| Authentifizierung: OAuth2, SSO | teilweise | OAuth 2.0 für öffentliche Integrationen ist verifiziert; SSO nicht | [S3] |
| Liste „Who it suits“ | nicht verifiziert | Meinung; nicht in offiziellen Quellen | — |

### latest/features.md

| Aussage | Status | Richtige Tatsache | Quelle |
|-----------|--------|--------------|--------|
| „No Markdown syntax in the editor“ | falsch | Markdown-Präfixe und Inline-Markdown funktionieren beim Schreiben | [S11] |
| Überschriften-Kürzel `##` usw. | verifiziert | | [S11] |
| Hinweistypen info, warning, success | nicht verifiziert | Hinweise existieren als Blocktyp; die Typliste ist nicht verifiziert | [S9] |
| Codeblock mit 40+ Sprachen, Sprachliste | nicht verifiziert | Nicht in den gelesenen offiziellen Quellen | — |
| LaTeX `$...$` | nicht verifiziert | Schrägstrich-Befehle `/equation`, `/math`, `/latex` existieren | [S11] |
| Mermaid-Diagramme | nicht verifiziert | Nicht in den gelesenen offiziellen Quellen | — |
| Tabelle, Formel, Rollup, Relationen | teilweise | Relation, Rollup, Formel, Status und Mehrfachauswahl existieren als API-Eigenschaftstypen | [S8] |
| Formelbeispiele (`concat`, `dateBetween`, `if`, `format`, `dateAdd`) | nicht verifiziert | Referenz `prop()` verifiziert | [S8] |
| Datenbankansichten: Tabelle, Kanban, Kalender, Liste, Galerie | falsch | Ansichten sind Tabelle, Liste, Board, Kalender, Galerie, Diagramm | [S13] |
| Liste der Datenbankspaltentypen | teilweise | Status, Mehrfachauswahl, Relation, Rollup, Formel bestätigt; andere nicht verifiziert | [S8] |
| Beispiele für Vorlagen | nicht verifiziert | Vorlagen existieren; Beispiele nicht verifiziert | [S12] |
| Automatisches Speichern | nicht verifiziert | Keine offizielle Aussage gelesen | — |

### latest/layout.md

| Aussage | Status | Richtige Tatsache | Quelle |
|-----------|--------|--------------|--------|
| Seitenleisten-Punkte Home, Pages, Database, Templates, Members, Dashboard, Settings | falsch | Home, Chats mit Notion AI, Meetings, Posteingang, Bibliothek, Vorlagen, Papierkorb, Einstellungen; Abschnitte Privat, Geteilt, Teamräume; Favoriten | [S12] |
| Breite der Seitenleiste, Logo ~40 px, Elementgrößen | nicht verifiziert | Nicht in offiziellen Quellen | — |
| Rechte Seitenleiste mit Versionen, Autor | nicht verifiziert | Keine offizielle Quelle gelesen | — |
| Breadcrumbs | nicht verifiziert | | — |
| Statusleiste mit Wort- und Zeichenzahl | nicht verifiziert | | — |
| Hamburger-Menü auf Mobilgeräten | nicht verifiziert | | — |
| Gestaltungsprinzipien (Minimalismus usw.) | nicht verifiziert | Marketingaussagen; nicht verwendet | — |
| Barrierefreiheits-Aussagen (ARIA, Kontrast) | nicht verifiziert | | — |
| Leistungsaussagen (Lazy Loading, Debounce) | nicht verifiziert | | — |

### latest/menus.md

| Aussage | Status | Richtige Tatsache | Quelle |
|-----------|--------|--------------|--------|
| 13 Hauptmenüpunkte (Workspace, Pages, Databases, Trash, Media, Users, Settings, Notifications, Search, Templates, Integrations, Resources, Preferences) | falsch oder nicht verifiziert | Die Reiter und Punkte der Seitenleiste stehen in menus.md; die übrigen Punkte sind nicht verifiziert | [S12] |
| Kontextmenüs (Seite, Datenbank, Block, Nutzer) | teilweise | Blockmenü: `/turn`, `/color`, Blockgriff ⋮⋮ sind verifiziert; andere nicht verifiziert | [S11, S14] |
| Befehlspalette `Ctrl+Shift+P` | nicht verifiziert | Nicht auf der offiziellen Seite mit Tastenkürzeln | [S11] |
| Schnellsuche `Ctrl+P` | teilweise | cmd/ctrl+P öffnet die Suche oder springt zu einer zuletzt besuchten Seite | [S11] |
| Globale Suche `Ctrl+Shift+F` | falsch | Suche ist cmd/ctrl+K (Artikel zur Seitenleiste) | [S12] |
| Blockmenü `/` | teilweise | `/` öffnet Schrägstrich-Befehle | [S11] |

### latest/shortcuts.md

| Aussage | Status | Richtige Tatsache | Quelle |
|-----------|--------|--------------|--------|
| Ctrl+Shift+X durchgestrichen | falsch | cmd/ctrl+shift+S | [S11] |
| Ctrl+E zentrieren, Ctrl+L linksbündig, Ctrl+R rechtsbündig, Ctrl+Shift+E Blocksatz | nicht verifiziert | Nicht auf der offiziellen Seite. Ctrl+E ist Code im Text | [S11] |
| Ctrl+Shift+K Code-Tag | falsch | cmd/ctrl+E Code im Text | [S11] |
| Ctrl+Shift+C Codeblock | falsch | cmd/ctrl+option/shift+8 | [S11] |
| Ctrl+Shift+M Zitat | falsch | Zitat ist `"` + Leerzeichen. cmd/ctrl+shift+M erstellt einen Kommentar | [S11] |
| Ctrl+Shift+A Aufgabe | nicht verifiziert | To-do über `[]` + Leerzeichen und cmd/ctrl+option/shift+4 | [S11] |
| Ctrl+Enter Vorschau / veröffentlichen | falsch | cmd/ctrl+Enter wirkt auf den aktuellen Block (Seite öffnen, To-do abhaken, Umschalter, Vollbild) | [S11] |
| Ctrl+Shift+Backspace Block löschen | falsch | Backspace oder Delete bei ausgewählten Blöcken | [S11] |
| Ctrl+D Block duplizieren | teilweise | cmd/ctrl+D dupliziert ausgewählte Blöcke | [S11] |
| Ctrl+Shift+D Seite duplizieren | falsch | cmd/ctrl+D betrifft Blöcke; Seite duplizieren ist nicht dokumentiert | [S11] |
| Ctrl+↑/↓ Block verschieben | falsch | cmd/ctrl+shift+Pfeiltaste verschiebt den ausgewählten Block | [S11] |
| Ctrl+Shift+↑/↓ Block kopieren | falsch | Verschieben, nicht kopieren | [S11] |
| Ctrl+B Seitenleiste ein- oder ausblenden | falsch | cmd/ctrl+B ist fett; Seitenleiste ist cmd/ctrl+\ | [S11, S12] |
| Ctrl+Shift+L Link einfügen | falsch | cmd/ctrl+K Link hinzufügen; cmd/ctrl+shift+L schaltet den dunklen Modus um | [S11] |
| Ctrl+Shift+F Seite teilen | nicht verifiziert | Nicht auf der offiziellen Seite | — |
| Ctrl+Shift+E Seite exportieren | nicht verifiziert | Nicht auf der offiziellen Seite | — |
| Ctrl+S speichern | nicht verifiziert | Nicht dokumentiert | — |
| Ctrl+W Seite schließen, Ctrl+N neue Seite | teilweise | cmd/ctrl+N neue Seite (Desktop); Schließen nicht dokumentiert | [S11] |
| Ctrl+Shift+N Unterseite | nicht verifiziert | | — |
| Ctrl+Shift+A App-Manager | nicht verifiziert | | — |
| Ctrl+Shift+I Entwicklertools, F11 Vollbild | nicht verifiziert | | — |
| Ctrl+G, Ctrl+H nächster Treffer, Ersetzen | nicht verifiziert | | — |
| Ctrl+Tab nächster Tab | nicht verifiziert | cmd/ctrl+T neuer Tab; Tab-Wechsel nicht dokumentiert | [S11] |
| Ctrl+Y wiederholen, Ctrl+Z rückgängig | nicht verifiziert | | — |
| Schrägstrich `/bullist`, `/numlist` | falsch | `/bullet`, `/num` | [S11] |
| Schrägstrich `/callout`, `/table`, `/md`, `/js`, `/python` und andere Sprach-Schrägstriche | nicht verifiziert | Nicht auf der offiziellen Seite | [S11] |
| `/h1` + Enter usw. | verifiziert | `/h1`, `/h2`, `/h3`, `/todo`, `/toggle`, `/quote`, `/code`, `/embed` | [S11] |
| Ctrl+K Link hinzufügen | verifiziert | | [S11] |
| Esc, Tab, Shift+Tab, Enter | verifiziert | | [S11] |
| Ctrl+Links/Rechts Wortnavigation | nicht verifiziert | | — |
| Mac-Kürzel mit cmd | teilweise | Offiziell wird cmd/ctrl für beide Plattformen verwendet | [S11] |

### latest/api.md

| Aussage | Status | Richtige Tatsache | Quelle |
|-----------|--------|--------------|--------|
| `Notion-Version: 2022-06-28` | veraltet | `2026-03-11` | [S1], [S8] |
| `GET /v1/pages` listet Seiten mit Filter | nicht verifiziert (nicht gefunden) | Kein Endpunkt zum Auflisten aller Seiten in der Referenz gefunden. Nutze `POST /v1/search` | [S10] |
| `DELETE /v1/pages/:id` löscht eine Seite | falsch | Papierkorb mit `PATCH /v1/pages/{id}` und `in_trash: true` | [S21] |
| `POST /v1/pages` mit `page_id` und `properties.title` | teilweise | Übergeordnete Typen: `page_id`, `database_id`, `data_source_id`, `workspace`. Maximal 100 Kinder | [S20] |
| `GET /v1/blocks/:id/children` | verifiziert | | [S19] |
| `POST /v1/blocks/:id/children` fügt Kinder hinzu | falsch | `PATCH /v1/blocks/{block_id}/children` | [S18] |
| `PATCH /v1/blocks/:id` aktualisiert, `DELETE /v1/blocks/:id` löscht | nicht verifiziert | | — |
| `GET /v1/databases/:id` | teilweise | Liefert untergeordnete Datenquellen; Schema über `GET /v1/data_sources/{id}` | [S7] |
| `POST /v1/databases` | teilweise | Erstellt eine Datenbank mit `initial_data_source` | [S7] |
| `PATCH /v1/databases/:id` | teilweise | Nur Felder auf Datenbankebene; das Schema liegt bei den Datenquellen | [S7] |
| `POST /v1/databases/:id/query` | veraltet | `POST /v1/data_sources/{data_source_id}/query` (die Zusammenfassung des Upgrade-Leitfadens nennt PATCH; die Referenzseite nennt POST) | [S17], [S7] |
| `GET /v1/users`, `/v1/users/:id`, `/v1/users/me` | teilweise | Benutzer-Endpunkte existieren mit Fähigkeitsbedingungen; Pfad `/users/me` nicht verifiziert | [S16] |
| `POST /v1/search` | verifiziert | Filterwert `database` heißt jetzt `data_source` | [S10], [S7] |
| `POST /v1/comments` | Pfad nicht verifiziert | Kommentar-Endpunkte existieren; Pfad nicht verifiziert | [S16], [S8] |
| Ratenlimits 3/s pro Integration, 1/s für Datenbankabfragen | falsch | 180 Anfragen pro Minute (etwa 3/s) pro Verbindung; 600/Min. bei Business und Enterprise; Datenquellen-Abfragen etwa 3/s | [S2] |
| Fehler bei Ratenlimit | verifiziert | 429, `rate_limited`, `Retry-After` in Sekunden | [S2] |
| Header `Notion-Request-Id` | nicht verifiziert | | — |
| Webhook-Einrichtung mit `POST /v1/webhooks` | falsch | Wird im Webhooks-Reiter der Integration angelegt | [S4] |
| Webhook-Ereignisse `page.created`, `page.updated`, `page.deleted`, `page.restored` | falsch | Richtige Namen: `page.created`, `page.content_updated`, `page.properties_updated`, `page.deleted`, `page.undeleted` usw. | [S5] |
| SDK `@notion/client` | falsch | `@notionhq/client` | [S7] |
| SDK `notion-client` (Python) | nicht verifiziert | Nicht auf den gelesenen Seiten | — |
| Community-SDKs (Go, Java, Ruby, PHP) | nicht verifiziert | Nicht auf offiziellen Seiten | — |
| Beispielcode `requests.post(...)` | veraltet | Verwendet alte Version und Endpunkte | [S1], [S17] |
| Authentifizierung über OAuth2 | verifiziert | Autorisierungs- und Token-Endpunkte wie beschrieben | [S3] |
| Header `Authorization: Bearer`, `Notion-Version` | verifiziert | | [S6] |

### latest/features.md, layout.md, menus.md: Zusammenfassung der Gegenprüfung

- Die früheren Seiten beschrieben ein Produkt mit den Seitenleisten-Punkten „Dashboard“, „Members“ und „Pages“, was nicht zur offiziellen Seitenleiste passt. Ersetzt.
- Die früheren Seiten wiederholten dieselbe allgemeine Vergleichstabelle. Entfernt.

### themes (neue Datei, keine frühere Version)

Die früheren Seiten hatten keine Themes-Datei. Die Anforderung aus `index.md` an `themes/index.md` ist im neuen Dateisatz erfüllt.
