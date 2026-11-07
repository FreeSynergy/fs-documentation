# Changelog

## 2026-11-07: aus offiziellen Quellen neu geschrieben

Die früheren Seiten wurden aus dem Gedächtnis verfasst; diese Aussagen waren falsch.

Quelle der früheren Seiten: `fs-documentation/docs/en/programs/apps/wiki/frontends/confluence/` (index.md und latest/*.md). Jede Zeile nennt die frühere Aussage, das Urteil, den korrekten Fakt und die Quelle (S-Nummern aus [index.md](index.md)).

Urteil: **FALSCH** = durch eine Quelle widerlegt. **UNGEPRÜFT** = keine Quelle gefunden; in den neuen Dateien entfernt oder markiert.

### api.md

| Frühere Aussage | Urteil | Korrekter Fakt | Quelle |
|-----------------|--------|----------------|--------|
| Basis `https://confluence.example.com/rest/api` | FALSCH | Cloud-Pfade sind `https://<site>.atlassian.net/wiki/api/v2` (v2) und `/wiki/rest/api` (v1) | S1, S2, S4 |
| Authentifizierungsmethoden: Basic, OAuth2, JWT, Cookie | TEILWEISE FALSCH | Basic-Auth (E-Mail + API-Token) für direkte Aufrufe; OAuth 2.0 (3LO) für Apps; JWT für Cloud-Apps. Cookie-Auth: ungeprüft. | S1, S6, S7 |
| `Authorization: Basic base64(email:api-token)` | FALSCH (wörtlicher Text) | Echtes Base64 von `email:api_token`. Das Beispiel ist ein Platzhalter, kein gültiger Header. | S7 |
| API-Tokens werden unter `atlassian.com` erstellt | UNGEPRÜFT | Ort in S7 nicht angegeben | S7 |
| Endpunkte `/rest/api/content`, `/child/page`, `/history`, `/child/attachment`, `/child/macro`, `/child/comment` | UNGEPRÜFT (größtenteils) | v1-Pfad `content/{id}` mit Präfix `/wiki` bestätigt (S2). Andere v1-Unterpfade nicht bestätigt. v2-Liste in S3. | S2, S3 |
| `GET /rest/api/user`, `GET /rest/api/user/view` | UNGEPRÜFT | Nicht bestätigt; v2 hat eine User-Gruppe (S1) | S1 |
| `GET /rest/api/search` mit `cql` | UNGEPRÜFT | Auf den gelesenen Seiten nicht bestätigt | - |
| Seite erstellen mit `space.key` und `body.storage` (v1-Beispiel) | UNGEPRÜFT | `storage` ist ein gültiger Wert für die Darstellung des Inhalts im v2-Schema; Form der v1-Anfrage nicht bestätigt | S4 |
| Python- und JS-Beispiele mit `requests`, `axios`, `atlassian-python-api` | UNGEPRÜFT | Beispiele verwenden Platzhalter-Hostnamen; Bibliotheksnamen nicht als offiziell bestätigt | - |
| Grenzwerte: 200 Anfragen pro 5 Minuten pro Benutzer | FALSCH | Punktebasiert: 65.000 Punkte pro Stunde (globaler Pool), Punkte pro Objekttyp | S5 |
| Grenzwerte: 100 Anfragen pro Sekunde | FALSCH | Nicht in S5; Burst-Grenzen sind getrennt und zahlenmäßig nicht dokumentiert | S5 |
| Header `X-AUTH-_RATE-LIMIT-REMAINING`, `X-AUTH-_RATE-LIMIT-RESET` | FALSCH | `X-RateLimit-Remaining`, `X-RateLimit-Reset`, `RateLimit-Reason`, `Retry-After` | S5 |
| Webhooks `page.created`, `page.updated`, `page.deleted`, `comment.created`, `space.created` | FALSCH | Forge-Ereignisse `avi:confluence:created:page` usw. Veraltete Connect-Ereignisnamen `page_created`, `page_updated` usw. | S10, S11 |
| Webhook-Konfiguration `POST /rest/webhooks/1.0/webhook` | Für Cloud UNGEPRÜFT | Connect-Webhooks werden im Deskriptor `modules.webhooks` deklariert (S11). Die Abonnierung von Forge-Ereignissen liegt in der Forge-App; der Mechanismus wurde nicht gelesen. | S10, S11 |
| SDK-Liste (`@atlassian/confluence-api` "offiziell", `atlassian-java-client` usw.) | UNGEPRÜFT | Nicht bestätigt; entfernt | - |
| Verweis `See also` auf `structure.md` | FALSCHER Link | Datei heißt `layout.md` | - |
| `Authorization` für OAuth mit `refresh` nicht beschrieben | FEHLT | Rotierende Refresh-Tokens; 90 Tage Inaktivität; Scope `offline_access` | S6 |

### description.md

| Frühere Aussage | Urteil | Korrekter Fakt | Quelle |
|-----------------|--------|----------------|--------|
| Backend Java; DB PostgreSQL, MySQL, H2, Oracle; Frontend "React (neu), velocity (alt)" | UNGEPRÜFT | In keiner gelesenen Cloud-Quelle. Entfernt. | - |
| Unternehmenstauglich, Audit-Logs, starke mobile Apps, umfangreiches Makrosystem | UNGEPRÜFT | Werbeaussage oder nicht geprüft. Entfernt. | - |
| Vergleiche mit Notion, XWiki, Wiki.js ("kommerziell", "bessere Integrationen") | UNGEPRÜFT | Meinung, nicht belegt. Entfernt. | - |
| Nur Data Center: Datenbanken | FALSCH | Cloud hat Datenbank-Objekte und Ereignisse | S10, S14 |
| Selbstbetrieb als "Data Center" ohne Datum | FEHLT | Ende der Lebensdauer von Data Center 2029-03-28 | S20 |
| Für wen es geeignet ist | UNGEPRÜFT | Keine Produktaussage. Entfernt. | - |

### features.md

| Frühere Aussage | Urteil | Korrekter Fakt | Quelle |
|-----------------|--------|----------------|--------|
| "Visueller Editor ist seit Cloud der Standard" | UNGEPRÜFT | Auf den gelesenen Seiten nicht angegeben | - |
| Wiki-Markup-Quelltext-Editor als Cloud-Modus | UNGEPRÜFT | In den gelesenen Cloud-Seiten nicht dokumentiert; Cloud-Doku beschreibt Markdown-Autoformat | S12 |
| "Kein Markdown im visuellen Editor" | FALSCH | Auslöser für Markdown-Autoformat existieren | S12 |
| Makro-Syntax `{note}`, `{code}`, `{table}`, `{embed}`, `{jira:...}` | UNGEPRÜFT | In den gelesenen Cloud-Seiten nicht dokumentiert. Makro-Einfügen existiert (Tastenkürzel `Ctrl+Shift+A` / `Cmd+Shift+A`) | S12 |
| `{toc}`, `!image.jpg!`, `h1.`-Markup | UNGEPRÜFT | Wiki-Markup-Syntax, für Cloud nicht bestätigt | - |
| Tastatur `Ctrl+Shift+1` für Überschrift 1 | FALSCH | Überschrift 1 ist `Ctrl+Alt+1` (Win) / `Cmd+Opt+1` (Mac) | S12 |
| Code-Hervorhebung "mit einer Erweiterung" | UNGEPRÜFT | Nicht geprüft | - |
| Sprachliste für Codeblöcke | UNGEPRÜFT | Nicht geprüft | - |
| Vergleichstabelle (Notion, Tango.io, XWiki) | UNGEPRÜFT | Entfernt | - |
| Live-Vorschau, Statusleiste mit Wortzahl | UNGEPRÜFT | Nicht geprüft | - |
| Liste der Einbettungen (YouTube, Google Maps, Gist, Twitter) | UNGEPRÜFT | Nicht geprüft | - |

### layout.md

| Frühere Aussage | Urteil | Korrekter Fakt | Quelle |
|-----------------|--------|----------------|--------|
| Linke Seitenleiste: Logo, Seiten, Bereiche, Dashboard, Vorlagen | FALSCH | Seitenleiste: For you, Recent, Starred, Spaces, Apps, More, Teams, Drafts, Company Hub (bedingt), Customize sidebar | S14 |
| Obere Leiste "Navigation, Suche, Benutzermenü" | TEILWEISE | Suche, Erstellen, Chat, Benachrichtigungen, Hilfe, Your profile and settings | S14 |
| Rechte Seitenleiste fest: Seiteninfo, Versionen, Autor, Berechtigungen, Tags | FALSCH | Detailbereich wird über eine schwebende Aktionsleiste unten rechts geöffnet; Versionsverlauf ist ein Menüpunkt "..." | S15 |
| Seitenleistenbreiten ca. 50 px und ca. 30 px | UNGEPRÜFT | Nicht geprüft | - |
| Breadcrumbs immer im Kopfbereich | FALSCH (aktuelles Beta-Layout) | Oben links ausgeblendet während der Arbeit; ein Pfeil zeigt den vollen Pfad | S15 |
| Wiki-Markup-Editor mit geteilter Vorschau | UNGEPRÜFT | Für Cloud nicht dokumentiert | - |
| Farbschema "hell und benutzerdefiniert" | TEILWEISE | Pro Benutzer Light oder Dark; Standard der Website unter Settings > Look and feel > Themes | S17 |
| Schrift 14–16 px | TEILWEISE | Gilt für Tokens des Atlassian Design System (Fließtext 14 px, großer Fließtext 16 px), für das Rendering von Confluence nicht geprüft | S19 |
| Automatisches Speichern, responsive Layouts für Tablet und Mobil, ARIA-Unterstützung, Leistungsangaben | UNGEPRÜFT | Nicht geprüft | - |

### menus.md

| Frühere Aussage | Urteil | Korrekter Fakt | Quelle |
|-----------------|--------|----------------|--------|
| Menü "Startseite / Startseite" | TEILWEISE | "For you" | S14 |
| Menüs "Erstellt", "Gespeichert", "Erwähnungen", "Dashboard" | FALSCH oder UNGEPRÜFT | Erstellt entspricht Recent mit Filter "Owned by me"; Gespeichert entspricht Starred; Erwähnungen und Dashboard nicht als Menünamen gefunden | S14 |
| Menü "Profil" mit "Abmelden" | TEILWEISE | "Your profile and settings" | S14 |
| Schnellsuche `Cmd/Ctrl+.` | FALSCH | Schnellsuche ist `Alt+Shift+Z` (Win) / `Ctrl+Opt+Z` (Mac); `Ctrl+.` ist der nächste Kommentar; Mac `Cmd+.` öffnet den Rovo-Chat | S12 |
| Menü Erstellen: "eine Frage erstellen (Answers)" | UNGEPRÜFT | Erstellen bietet Seite, Live-Dokument, Datenbank, Loom, Whiteboard, Folien; Blogbeitrag über Tastenkürzel | S14, S12 |
| Menüpunkte der Seite Bearbeiten, Kopieren, Verschieben, Löschen, Berechtigungen, Drucken | UNGEPRÜFT | Dokumentierte Punkte: Beobachtungseinstellungen, Versionsverlauf, Suchen und Ersetzen, Vorlagen und Import, Archivieren und Löschen, Export nach Word und PDF | S15, S16 |
| Export (PDF, Word) aus dem Seitenmenü | ZUTREFFEND | Pfad: "•••" > Export > Export to Word / Export to PDF | S16 |
| Bereichsmenü "Theme ändern", "Inhalte ordnen" | UNGEPRÜFT | Pfad zu den Bereichseinstellungen: Weitere Aktionen (•••) > Space settings > General > Features | S14, S17 |
| "Bereichs-Backup", "Bereichsstatistik" | UNGEPRÜFT | Nicht geprüft; ein Daten-Backup der Website ist ein eigener Artikel | S16 |
| Dashboard-Widgets (hinzufügen oder entfernen, teilen) | UNGEPRÜFT | Nicht geprüft | - |

### shortcuts.md

Der größte Teil der früheren Tabelle ist falsch. Wichtigste Fehler:

| Frühere Angabe | Urteil | Korrekt (Windows / Mac) | Quelle |
|----------------|--------|-------------------------|--------|
| Ctrl+Shift+F globale Suche | FALSCH | Schnellsuche Alt+Shift+Z / Ctrl+Opt+Z | S12 |
| Ctrl+, Einstellungen | FALSCH | Vorheriger Kommentar | S12 |
| Ctrl+K Befehlspalette / Cmd+Shift+P | UNGEPRÜFT | Nicht in der offiziellen Tabelle | S12 |
| Ctrl+Shift+1…6 Überschriften | FALSCH | Ctrl+Alt+1…6 (Win), Cmd+Opt+1…6 (Mac) | S12 |
| Ctrl+Shift+L Aufzählungsliste | FALSCH | Ctrl+Shift+L ist linksbündig; Aufzählungsliste ist Ctrl+Shift+8 | S12 |
| Ctrl+E / Ctrl+L / Ctrl+R Ausrichtung | FALSCH | Zentriert Ctrl+Alt+E; linksbündig Ctrl+Shift+L; rechtsbündig Ctrl+Alt+T | S12 |
| Ctrl+Shift+X durchgestrichen | FALSCH | Ctrl+Shift+S (Win); Opt+Shift+S (Mac) | S12 |
| Ctrl+Shift+M Zitat | FALSCH | Zitat Ctrl+Shift+9; Ctrl+Shift+M ist Codeblock / Inline-Code | S12 |
| Ctrl+Shift+T Tabelle | FALSCH | Tabelle Ctrl+Shift+I | S12 |
| Ctrl+Shift+D Diagramm | FALSCH | Ctrl+Shift+D ist "Insert markup" und "Create live doc" | S12 |
| Ctrl+Shift+A Aufgabe | FALSCH | Ctrl+Shift+A ist Makro | S12 |
| Ctrl+B / Ctrl+I (Mac Cmd) | TEILWEISE | Windows korrekt; Mac Opt+B / Opt+I laut offizieller Tabelle | S12 |
| Ctrl+B Seitenleiste umschalten | FALSCH | Ctrl+[ | S12 |
| Ctrl+Shift+I Entwicklerwerkzeuge | FALSCH | Ctrl+Shift+I öffnet den Detailbereich | S12 |
| Ctrl+S, Ctrl+P, Ctrl+N, Ctrl+O, Ctrl+W, Ctrl+Shift+N/S/E/X | UNGEPRÜFT | Nicht in der offiziellen Tabelle; Ctrl+Enter veröffentlicht | S12 |
| F1 Hilfe, F11 Vollbild | UNGEPRÜFT | Nicht in der offiziellen Tabelle | S12 |
| Ctrl+Shift+V Video, Ctrl+Shift+B Box, Ctrl+Shift+E Einbettung | UNGEPRÜFT | Nicht in der offiziellen Tabelle | S12 |
| Ctrl+K Link | ZUTREFFEND | Ctrl+K / Cmd+K | S12 |
| Ctrl+F Suchen | ZUTREFFEND | Suchen und Ersetzen (Ctrl+F / Cmd+F) | S12 |
| Ctrl+Enter veröffentlichen | ZUTREFFEND | Ctrl+Enter / Cmd+Enter | S12 |
| Ctrl+Z / Ctrl+Y rückgängig, wiederholen | ZUTREFFEND | Dieselben Tasten, zusätzlich Ctrl+Shift+Z zum Wiederholen | S12 |
| Tastenkürzel können angepasst werden (implizit) | UNGEPRÜFT | Nicht angegeben; allgemeine Tastenkürzel können ausgeschaltet werden | S12, S13 |
| Tabellennavigation mit Tab / Shift+Tab | UNGEPRÜFT | Nicht in der offiziellen Tabelle; die offizielle Tabelle nennt Kürzel zum Hinzufügen von Zeilen und Spalten | S12 |

### api.md, events.md, limits.md: Grenzwerte und Ereignisse, Zusammenfassung

Oben bereits behandelt. Die frühere Angabe eines Cloud-Grenzwerts von "100 Anfragen pro Sekunde" und das Anfragebudget von 5 Minuten werden beide durch das Punktemodell aus S5 ersetzt.

### Frühere index.md

| Frühere Aussage | Urteil | Korrekter Fakt | Quelle |
|-----------------|--------|----------------|--------|
| "Bemerkenswerte Ideen: To do" | FEHLT | In der index.md des neuen Satzes ergänzt | S1, S10, S14 |
| Tabelle "Dokumentierte Versionen", 6/7 Dateien vorhanden | Veraltet | Ersetzt durch `latest/` mit dem neuen Dateisatz | - |

### Punkte, die die früheren Seiten gar nicht behandelt haben

- Design-Tokens des Atlassian Design System (Themes): S18, S19, S21
- Neugestaltung der Cloud-Navigation und Beta-Inhaltslayout: S14, S15
- Exportoptionen für Bereiche: S16
- Ende der Lebensdauer von Data Center: S20
- GraphQL-Grenzwerte: S8
- Regeln für Refresh-Tokens bei OAuth: S6
- Änderung der Veröffentlichungsfreigabe (409) und Änderung der IP-Bereiche: S9
