# Changelog

## 2026-11-07: aus offiziellen Quellen neu geschrieben

Die früheren Seiten wurden aus dem Gedächtnis verfasst; diese Aussagen waren falsch.

Geprüft gegen die in jeder Zeile genannten Quellen am 2026-11-07, für MediaWiki 1.46.2. Bestehende Seiten: `/srv/FreeSynergy/fs-documentation/docs/en/programs/apps/wiki/frontends/mediawiki/` (index.md, latest/*.md).

Statusschlüssel: **FALSCH** = durch eine Quelle widerlegt. **UNGEPRÜFT** = in diesem Lauf keine Quelle gefunden; nicht ohne Prüfung verwenden. **TEILWEISE** = stimmt mit einem fehlenden oder falschen Detail.

### api.md

| Nr. | Bestehende Aussage | Status | Korrekter Fakt | Quelle |
|-----|--------------------|--------|----------------|--------|
| A1 | "MediaWiki bietet eine umfangreiche REST-basierte API für den Zugriff auf alle Wiki-Funktionen ... unterstützt alle CRUD-Operationen" | FALSCH | Die Action API (`api.php`) ist die vollständige API. Die REST API (`rest.php`) ist eine kleinere Auswahl an Ressourcen. | https://www.mediawiki.org/wiki/API:REST_API ; https://www.mediawiki.org/wiki/API:Main_page |
| A2 | Auth-Methoden: "Clientlogin, OAuth, Bot passwords, Session cookies, PATRICIA" | TEILWEISE | Clientlogin und Bot-Passwörter sind Kern. OAuth ist eine Erweiterung, nicht Kern. "PATRICIA" ist keine Auth-Methode von MediaWiki, die in Kern oder API-Doku gefunden wurde. | https://www.mediawiki.org/wiki/API:Login ; Quellbaum `includes/User/BotPassword.php`; kein OAuth- oder PATRICIA-Modul in REL1_46 |
| A3 | Endpunkt `GET/POST /w/api.php` | TEILWEISE | `/w/` ist nur der Pfad auf Wikimedia-Seiten. Der Pfad hängt von der Installation ab. Auf Special:Version finden. | https://www.mediawiki.org/wiki/API:Main_page |
| A4 | Tabelle "Pages": Aktion `history` | FALSCH | Kein Modul `history`. Versionen kommen aus `prop=revisions` (oder REST `/v1/page/{title}/history`). | Quellbaum `includes/Api/ApiQueryRevisions.php`; `coreRoutes.json` |
| A5 | `query&list=images` "Dateien auflisten" | FALSCH | `list=allimages` listet Dateien. `prop=images` listet Dateien, die eine Seite verwendet. | `includes/Api/ApiQueryAllImages.php`, `ApiQueryImages.php` |
| A6 | `query&list=userprop` "Benutzereigenschaften" | FALSCH | Kein `list=userprop`. `list=users` mit `usprop` oder `meta=userinfo` verwenden. | `includes/Api/ApiQueryUsers.php`, `ApiQueryUserInfo.php` |
| A7 | `deletefile` "eine Datei löschen" | FALSCH (Modul) | Kein Modul `ApiDeleteFile` in REL1_46. Das Löschen von Dateien ist hier kein eigenes Modul (Pfad nicht ermittelt). | Dateiliste des Quellbaums |
| A8 | `createaccount` "ein Konto erstellen" | UNGEPRÜFT | Eine Klasse `ApiAMCreateAccount` existiert; der registrierte Modulname wurde nicht geprüft. | `includes/Api/ApiAMCreateAccount.php` |
| A9 | `query&meta=globalinfo` | FALSCH (Kern) | Nicht im Kern. Es gehört zu einer Erweiterung (CentralAuth). Kein `ApiQueryGlobalInfo` in REL1_46. | Quellbaum |
| A10 | `query&meta=siteinfo`, `query&meta=tokens` | TEILWEISE | `tokens` ist korrekt. `siteinfo` ist dokumentiert, aber seine Moduldatei wurde in diesem Lauf nicht geprüft. | `ApiQueryTokens.php` |
| A11 | Bearbeitungsablauf: `action=query&meta=tokens&type=edit` und `edittoken` | FALSCH | Der Edit-Token-Typ ist `csrf`. `edittoken` ist im Kern kein Token-Name. | `includes/Api/ApiQueryTokens.php` (`getTokenTypeSalts`: `csrf`, `watch`, `patrol`, `rollback`, `userrights`, `login`, `createaccount`) |
| A12 | Anmeldeablauf mit `clientlogin` und `logintoken` | TEILWEISE | Im Grundsatz richtig. Das Beispiel lässt die clientlogin-Felder aus, die der Server verlangt (zum Beispiel die Rücksprung-URL); die Statusbehandlung (UI, REDIRECT, `logincontinue`) fehlt. | https://www.mediawiki.org/wiki/API:Login |
| A13 | Python- und JS-Beispiele zum Bearbeiten | FALSCH (Token) | Wie A11. Die Beispiele scheitern am aktuellen Kern mit dem Edit-Token-Namen. | A11 |
| A14 | "GraphQL (MediaWiki 1.39+)" und Endpunkt `/graphql` | FALSCH | Kein GraphQL im Kern. Ein GraphQL-Endpunkt stammt aus einer Erweiterung und wurde nicht geprüft. Die Beispielabfrage ist keine vorhandene API. | Quellbaum (kein GraphQL-Modul) |
| A15 | Ratenbegrenzungen: "50 req/s pro IP", "100 req/s angemeldet", "Bots 10/Sek." | FALSCH | Solche Standardwerte gibt es nicht. Kernbegrenzungen gelten pro Aktion in `$wgRateLimits`: edit 8/60 s pro IP und Neuling, 90/60 s pro Benutzer; move 2/120 s Neuling, 8/60 s Benutzer; upload 8/60 s IP und Neuling; rollback 10/60 s Benutzer. Lesezugriffe haben im Konfigurationsschema kein Standardlimit. | https://github.com/wikimedia/mediawiki/blob/REL1_46/includes/config-schema.php (Schlüssel `RateLimits`); https://www.mediawiki.org/wiki/API:Etiquette (nur Zusammenfassung) |
| A16 | Konfigurationsnamen `$wgRateLimit`, `$wgRateLimitLog`, `$wgUserRateLimit`, `$wgExtensionFunctions` | FALSCH | Der Schlüssel heißt `$wgRateLimits`. `$wgRateLimitLog` und `$wgUserRateLimit` erscheinen nicht im Konfigurationsschema. | config-schema.php |
| A17 | Webhooks über Echo: Ereignisse edit, new, move, delete, protect | FALSCH | Echo ist eine Benachrichtigungserweiterung im Wiki (Hinweise, Web- und E-Mail-Benachrichtigungen, Push-Einstellungen). Es ist kein Webhook-System. Kein URL-Webhook dokumentiert. | https://www.mediawiki.org/wiki/Extension:Echo |
| A18 | SDK-Liste (MediaWiki JS offiziell, mwclient, wikipedia-api, mediawiki-api-client, mwapi, mediawiki-gems, go-mediawiki) | UNGEPRÜFT | In diesem Lauf nicht geprüft. | — |
| A19 | Verweise "See also" auf `menu.md`, `structure.md` | FALSCH (Link) | Die Dateien heißen `menus.md` und `layout.md`. | Dateibestand |
| A20 | Aktionsliste "login (deprecated)", "logout", "userrights", "block", "unblock", "purge", "rollback", "protect", "move", "upload" | ZUTREFFEND | Module existieren in REL1_46. | `includes/Api/Api*.php` |

### description.md

| Nr. | Bestehende Aussage | Status | Korrekter Fakt | Quelle |
|-----|--------------------|--------|----------------|--------|
| D1 | "Datenbank: PostgreSQL, MySQL, MariaDB" | TEILWEISE | Außerdem SQLite. MariaDB wird empfohlen. Mindestversionen: MariaDB 10.3+, MySQL 5.7+, PostgreSQL 10+, SQLite 3.8+. | RELEASE-NOTES-1.46 (Compatibility) |
| D2 | "Authentifizierung: lokale Konten, OAuth, LDAP" | FALSCH (Kern) | Lokale Konten und Bot-Passwörter sind Kern. OAuth und LDAP sind nicht im Kern (Erweiterungen). | Quellbaum; https://www.mediawiki.org/wiki/API:Login |
| D3 | "Frontend: JavaScript, PHP-Vorlagen" | TEILWEISE | Der Standard-Skin (Vector 2022) verwendet Mustache-Vorlagen und JavaScript-Module mit Codex-Design-Tokens. | https://github.com/wikimedia/mediawiki-skins-Vector/tree/REL1_46 |
| D4 | "MediaWiki ist die beliebteste Wiki-Software" | UNGEPRÜFT | Nicht geprüft. "Weit verbreitet; betreibt Wikipedia" nur verwenden, wenn eine Quelle ergänzt wird. | — |
| D5 | Vergleiche mit Wiki.js, XWiki, Confluence (Geschwindigkeit, Lizenzkosten, Makrosysteme, Jira-Integration) | UNGEPRÜFT | In diesem Lauf keine Quelle. Entfernen oder mit Quelle belegen. | — |
| D6 | "Skalierbar: Millionen Seiten" | UNGEPRÜFT | Wikimedia-Wikis sind groß; keine Zahl geprüft. | — |
| D7 | "Etabliert: sehr stabil und gut getestet" | UNGEPRÜFT | Meinung. Durch die Lebenszyklus-Fakten ersetzen (Support-Tabelle). | https://www.mediawiki.org/wiki/Version_lifecycle |
| D8 | Liste "Für wen MediaWiki geeignet ist" | UNGEPRÜFT | Meinung. | — |

### features.md

| Nr. | Bestehende Aussage | Status | Korrekter Fakt | Quelle |
|-----|--------------------|--------|----------------|--------|
| F1 | "VisualEditor: keine direkte Bearbeitung der Wiki-Syntax im visuellen Modus" | TEILWEISE | Der VisualEditor hat einen Eintrag "Edit source" (Zugriffstaste `e`, Meldung `accesskey-ca-editsource`). Er kann in den Quelltexteditor wechseln. | https://www.mediawiki.org/wiki/Help:Keyboard_shortcuts (Tabelle der Zugriffstasten, Zeilen der Erweiterungen) |
| F2 | "Quellen: Zitate und Referenzen" im VisualEditor | TEILWEISE | Der VisualEditor hat die Aktion "Insert citation" (Ctrl+Shift+K). Automatische Zitate (Citoid) sind eine Erweiterung und nicht geprüft. | https://www.mediawiki.org/wiki/VisualEditor/Portal/Keyboard_shortcuts |
| F3 | "Mathematische Formeln: LaTeX (optional)", "Diagramme: Graphviz", "Score", "Kartographer", "Linter", "Citoid", "Graph" als Erweiterungen des VisualEditor | UNGEPRÜFT | Erweiterungen. In diesem Lauf nicht geprüft. | — |
| F4 | "Quelltext-Editor: Syntaxhervorhebung, Zeilennummern, Autovervollständigung, Unterschied im Kontext" als Teil des Quelltext-Editors | TEILWEISE | Hervorhebung, Zeilennummern, Suche, Klammerabgleich und ein Tastendialog stammen aus der Erweiterung CodeMirror, nicht aus dem Kern. Autovervollständigung ist für Wikitext standardmäßig aus. CodeMirror wird in 1.47 für die meisten Integrationen der Standard. | https://www.mediawiki.org/wiki/Extension:CodeMirror |
| F5 | "Quelltext bearbeiten (alternativer Modus)", "Code-Editor für Entwickler" | UNGEPRÜFT | Kein Kernmodus. Als CodeMirror behandeln. | https://www.mediawiki.org/wiki/Extension:CodeMirror |
| F6 | "MediaWiki-Quelltext-Editor-Variante ... Vergleichsansicht: die Änderungen im Kontext" | UNGEPRÜFT | Keine Quelle für eine geteilte Vergleichsansicht. | — |
| F7 | "WikiEditor: erweiterte Werkzeugleiste" | UNGEPRÜFT | Die Seite https://www.mediawiki.org/wiki/Help:WikiEditor lieferte in diesem Lauf HTTP 404. | — |
| F8 | "Vorlagen (visuell)" im VisualEditor | TEILWEISE | Der Vorlagendialog existiert (Tasten auf der Tastenseite des VisualEditor). Seine Grenzen wurden nicht geprüft. | https://www.mediawiki.org/wiki/VisualEditor/Portal/Keyboard_shortcuts |
| F9 | "Live-Vorschau: ja" für den VisualEditor und "nein (optional)" für den Quelltext | UNGEPRÜFT | Nicht geprüft. Der Quelltext-Editor hat eine Vorschau-Aktion (Zugriffstaste `p`). | https://www.mediawiki.org/wiki/Help:Keyboard_shortcuts |
| F10 | Empfehlungen (Einsteiger nutzen VE, Fortgeschrittene den Quelltext) | UNGEPRÜFT | Meinung. | — |

### layout.md

| Nr. | Bestehende Aussage | Status | Korrekter Fakt | Quelle |
|-----|--------------------|--------|----------------|--------|
| L1 | Seitenleiste (links) enthält Logo, Suche und Sprachen | FALSCH | In Vector 2022 stehen Suchfeld und Logo in der Kopfzeile. Die linke Seitenleiste ist das Hauptmenü (anheftbar). Sprachen stehen in der Kopfzeile (ULS-Schaltfläche) oder im Inhalt. | `includes/templates/Header.mustache` (enthält MainMenuDropdown, Logo, SearchBox, UserLinks); `skin.mustache`; `SkinVector22.php` |
| L2 | "Farbschema: nur helles Thema" | FALSCH | Vector 2022 hat einen Nachtmodus: Einstellung `vector-theme` = `day`, `night`, `os`. | https://github.com/wikimedia/mediawiki-skins-Vector/blob/REL1_46/doc/configuration/configuration.md |
| L3 | "Breadcrumbs (optional)" im Inhaltskopf | FALSCH (nicht im Skin) | Kein Breadcrumb-Teilstück in den Vorlagen von Vector 2022. | `includes/templates/skin.mustache`, `Header.mustache` |
| L4 | Inhaltskopf mit Aktion "Teilen" | UNGEPRÜFT | Kein Punkt "Teilen" in den geprüften Vorlagen von Vector 2022 oder in den Kernmeldungen. | — |
| L5 | Schriftgrößen 14–16 px; "Überschrift H1–H6" | TEILWEISE | Vector setzt `@font-size-heading-1` 1.8em, Überschrift 2 1.5em, Überschrift 3 1.2em, Basis-Zeilenhöhe 1.6. Überschriften 4–6 sind in diesen Variablen nicht definiert. Textgröße ist eine Benutzereinstellung (0/1/2). | `resources/skins.vector.styles/variables.less`; `configuration.md` |
| L6 | "Automatisches Speichern im Editor" | UNGEPRÜFT | In den gelesenen Quellen nicht gefunden. | — |
| L7 | "Drag & Drop für Medienuploads" | UNGEPRÜFT | Nicht geprüft. | — |
| L8 | Responsives "Tablet" und "Mobil-Hamburger" | UNGEPRÜFT | Der responsive Modus von Vector 2022 ist ein experimenteller Schalter (`wgVectorResponsive`). Das Verhalten von Hamburger/Hauptmenü ist nicht bestätigt. | `configuration.md` |
| L9 | Layout des VisualEditor: Formatierungsleiste, Statusleiste mit Wortzahl und Vorschau-Schaltfläche | UNGEPRÜFT | Nicht geprüft. | — |
| L10 | Layout des Quelltext-Editors: linker Editor, rechts Vergleich/Vorschau | UNGEPRÜFT | Nicht geprüft. | — |
| L11 | Barrierefreiheits-Angaben (ARIA, Kontrast, Zoom) | UNGEPRÜFT | Allgemein. Nicht geprüft. | — |

### menus.md

| Nr. | Bestehende Aussage | Status | Korrekter Fakt | Quelle |
|-----|--------------------|--------|----------------|--------|
| M1 | "Aktionen (Seitenleiste): ... die Seite drucken" | FALSCH (Gruppe) | Drucken ist ein Werkzeugeintrag (`tooltip-t-print`, Portlet "t"), keine Seitenaktion. | `languages/i18n/en.json` (`tooltip-t-print`); Help:Keyboard_shortcuts (Zugriffstaste `p` in Zeilen "jede Seite") |
| M2 | "Werkzeuge (Seitenleiste): Links auf diese Seite, verwandte Änderungen, neue Seiten, Spezialseiten, Druckversion" | TEILWEISE | Links auf diese Seite, verwandte Änderungen, dauerhafter Link, Seiteninformationen und Drucken sind Werkzeugeinträge. "Neue Seiten" und "Spezialseiten" als Werkzeugeinträge wurden nicht geprüft. | `en.json`-Tooltips `tooltip-t-whatlinkshere`, `tooltip-t-recentchangeslinked`, `tooltip-t-info`, `tooltip-t-permalink` |
| M3 | "Hauptseite (Menüpunkt 1)", "Seiten (Menüpunkt 2)" | UNGEPRÜFT | Der Inhalt des Hauptmenüs von Vector 2022 kommt aus der Website-Konfiguration; "Seiten" ist kein Kernmenü. | `MainMenu.mustache` |
| M4 | "Spezialseiten", "Benutzerbeiträge", "Hochladen", "verwaiste Seiten", "nicht lokalisierte Seiten", "Zufallsseite" als Spezialseiten | TEILWEISE | Zufallsseite ist ein Eintrag des Hauptmenüs (`tooltip-n-randompage`). Hochladen hat `tooltip-t-upload`. Der Rest wurde nicht geprüft. | `en.json` |
| M5 | Benutzermenü für abgemeldete Benutzer: "Diskussionsseite, Beiträge, Konto erstellen, Anmelden" | TEILWEISE | Konto erstellen (`tooltip-pt-createaccount`) und Anmelden (`tooltip-pt-login`) existieren. | `en.json` |
| M6 | Benutzermenü für angemeldete Benutzer: "Beobachtungsliste, Änderungen auf der Beobachtungsliste, Einstellungen, Anmeldestatus" | TEILWEISE | Beobachtungsliste und Einstellungen existieren (`tooltip-pt-watchlist`, `tooltip-pt-preferences`). "Anmeldestatus" und "Änderungen auf der Beobachtungsliste" als Einträge wurden nicht geprüft. | `en.json` |
| M7 | Rollenmenüs (anonym, registriert, sysop) | UNGEPRÜFT | Hängt von `$wgGroupPermissions` und den Erweiterungen ab. Nicht geprüft. | — |
| M8 | Sysop: "Seiten löschen/wiederherstellen, schützen, sperren, umbenennen, Dateien löschen, Logs ansehen" | TEILWEISE | Löschen, Wiederherstellen, Schützen, Sperren, Verschieben (Umbenennen) existieren als Module. "Dateien löschen" hat kein Modul (siehe A7). "Logs ansehen" wurde nicht geprüft. | api.md, Abschnitt 1 |
| M9 | Bearbeiten-Menü: "Quelltext bearbeiten, Visueller Editor, Vorschau, zusammenfassen" | TEILWEISE | Vorschau (`p`), Zusammenfassung (`b`), Bearbeiten (`e`) und der Wechsel Quelltext/VE existieren. "Zusammenfassen" ist kein Kernpunkt. | Help:Keyboard_shortcuts |
| M10 | Diskussions-Menü: "neuen Abschnitt hinzufügen, Abschnitt bearbeiten, Diskussion beenden" | TEILWEISE | "Neuen Abschnitt hinzufügen" ist `ca-addsection` (Taste `+`). "Abschnitt bearbeiten" und "Diskussion beenden" sind keine Kernfunktionen (Diskussionsfunktionen sind Erweiterungen). | Help:Keyboard_shortcuts |
| M11 | Versions-Menü: "Unterschiede anzeigen, wiederherstellen, Verlauf" | TEILWEISE | Vergleich (`v` im Bearbeitungsformular), Verlauf (`h`) und Zurücksetzen existieren. "Wiederherstellen" ist für gelöschte Seiten das Wiederherstellen (undelete), nicht allgemein das Wiederherstellen einer alten Version. | Help:Keyboard_shortcuts; `ApiUndelete` nicht geprüft |

### shortcuts.md

Der größte Teil der Datei ist falsch. MediaWiki-Kern verwendet keine Strg+Buchstaben-Kürzel für Seiten. Es verwendet Zugriffstasten (ein Buchstabe plus browserabhängiger Modifikator, siehe `1.46/shortcuts.md`).

| Nr. | Bestehende Aussage | Status | Korrekter Fakt | Quelle |
|-----|--------------------|--------|----------------|--------|
| S1 | Ctrl+Shift+P Befehlspalette; Ctrl+, Einstellungen; F1 Hilfe; Ctrl+Shift+F globale Suche; Ctrl+K Suchleiste | FALSCH | Keine Befehlspalette und diese Kürzel gibt es im Kern nicht. Suche ist Zugriffstaste `f`; Einstellungen sind `Special:Preferences` (kein Zugriffstaste zum Öffnen angegeben). Ctrl+K im VisualEditor ist "Link einfügen". | Help:Keyboard_shortcuts; VisualEditor/Portal/Keyboard_shortcuts |
| S2 | Ctrl+S speichern; Ctrl+P drucken; Ctrl+N neue Seite; Ctrl+O öffnen; Ctrl+W schließen; Ctrl+Shift+S speichern unter; Ctrl+Shift+P exportieren | FALSCH | Ctrl+S ist kein Speicherkürzel von MediaWiki. Speichern ist Zugriffstaste `s` (VisualEditor: Alt+S unter Windows/Linux, Ctrl+Option+S auf dem Mac). Drucken ist Zugriffstaste `p`. Ctrl+P, Ctrl+N, Ctrl+O, Ctrl+W, Ctrl+Shift+S sind Browserfunktionen, nicht von MediaWiki. | Help:Keyboard_shortcuts; VisualEditor/Portal/Keyboard_shortcuts; jquery.accessKeyLabel.js |
| S3 | VisualEditor Ctrl+U unterstreichen; Ctrl+E/L/R/Shift+E Ausrichtung; Ctrl+Shift+1–6 Überschriften; Ctrl+Shift+L Aufzählung; Ctrl+Shift+M Zitat; Ctrl+Shift+D Bild; Ctrl+Shift+V Video; Ctrl+Shift+T Tabelle/Vorlage; Ctrl+T Vorlageneditor | FALSCH oder UNGEPRÜFT | Die Tastenseite des VisualEditor nennt Ctrl+B, Ctrl+I, Ctrl+K, Ctrl+Shift+K (Zitat), Ctrl+Shift+V (als reinen Text einfügen), Ctrl+Z, Ctrl+Shift+Z, Tab/Shift+Tab (Liste einrücken), Ctrl+\ oder Ctrl+M (Formatierung entfernen), Alt+S (speichern), Ctrl+Shift+X (Schreibrichtung). Unterstreichen, Ausrichtung, Überschriften, Zitat, Bild, Video, Tabelle und Vorlageneditor sind in dieser Liste nicht enthalten. | VisualEditor/Portal/Keyboard_shortcuts |
| S4 | Ctrl+Shift+X durchgestrichen | FALSCH | Ctrl+Shift+X im VisualEditor schaltet die Schreibrichtung um. | VisualEditor/Portal/Keyboard_shortcuts |
| S5 | Quelltext-Editor: Ctrl+B fett, Ctrl+I kursiv, Ctrl+Shift+L Aufzählung, Ctrl+Shift+N nummeriert, Ctrl+Shift+1/2/3 Überschriften, Ctrl+K Link | UNGEPRÜFT | In keiner offiziellen Seite gefunden, die in diesem Lauf gelesen wurde. | — |
| S6 | Quelltext-Editor: Ctrl+Shift+F Syntaxhervorhebung umschalten | UNGEPRÜFT | CodeMirror hat einen Dialog mit Tastenkürzeln; diese Taste wurde nicht bestätigt. | https://www.mediawiki.org/wiki/Extension:CodeMirror |
| S7 | Ctrl+F Suche; Ctrl+G nächster Treffer; Ctrl+H ersetzen; Ctrl+Shift+O Seitenstruktur; Ctrl+P Dateisuche | FALSCH oder UNGEPRÜFT | Ctrl+F, Ctrl+G, Ctrl+H sind Browser- oder Editorfunktionen. Das Dateisuchfenster und die Seitenstruktur sind keine MediaWiki-Kürzel. | — |
| S8 | F11 Vollbild; Ctrl+Shift+I Entwicklerwerkzeuge; Ctrl+B Seitenleiste ein-/ausblenden; Ctrl+Shift+B Statusleiste | FALSCH (MediaWiki) | F11 und Ctrl+Shift+I sind Browserkürzel. Ctrl+B ist im VisualEditor "fett", kein Umschalten der Seitenleiste. | VisualEditor/Portal/Keyboard_shortcuts |
| S9 | Ctrl+Enter Vorschau/Veröffentlichen | FALSCH | Vorschau ist Zugriffstaste `p`; Veröffentlichen ist `s`. | Help:Keyboard_shortcuts |
| S10 | Erweiterungs-Kürzel: Ctrl+Shift+M Mathematik, Ctrl+Shift+C Codeblock, Ctrl+Shift+G Graphviz, Ctrl+Shift+A ASCII-Kunst, Ctrl+Shift+Q Zitat | UNGEPRÜFT | Nicht geprüft. Ctrl+Shift+G kollidiert mit Browserkürzeln, daher zweifelhaft. | — |
| S11 | Mac-Kürzel (Cmd+Shift+P, Cmd+, usw.) | FALSCH | Wie S1 und S2. | — |
| S12 | Tastaturnavigation (Tab, Shift+Tab, Enter, Escape, Leertaste, Pfeiltasten) | UNGEPRÜFT | Allgemeines Browserverhalten. | — |
| S13 | Von MediaWiki verwendete Zugriffstasten (e, h, m, d, u, w, t, c, r, x, z, q, f, j, k, l, y, n, ., o, p, s, v, i, b, =, +) | FEHLT | Dies sind die echten Tastenkürzel von MediaWiki. Die bestehende Seite nennt keine davon. | Help:Keyboard_shortcuts; jquery.accessKeyLabel.js |
| S14 | Modifikator für Zugriffstasten: Ctrl | FALSCH | Der Modifikator hängt vom Browser ab: Firefox und Chrome unter Windows/Linux verwenden Alt+Shift oder Alt; macOS verwendet Ctrl+Option. | jquery.accessKeyLabel.js (Zeilen 38–78) |

### Bestehende Fakten, die korrekt sind (zur Referenz)

- Vector 2022 ist der Standard-Skin; Wikipedia und andere Wikimedia-Seiten verwenden MediaWiki (der Wikimedia-Teil ist ein allgemeiner Fakt und wurde in diesem Lauf nicht geprüft).
- Der Anmeldeablauf über `meta=tokens&type=login` und `clientlogin` ist der aktuelle Weg (A12).
- Der VisualEditor und ein Wikitext-Quelltext-Editor existieren beide.
- Beobachtungsliste, letzte Änderungen, Kategorien und Links auf diese Seite existieren als Funktionen (siehe `1.46/features.md`).
