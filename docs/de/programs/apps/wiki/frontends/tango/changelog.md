# Änderungsprotokoll

## 2026-11-07: neu geschrieben aus offiziellen Quellen

Die früheren Seiten waren aus dem Gedächtnis geschrieben; diese Aussagen waren falsch.

Geprüfte Seiten: `fs-documentation/docs/en/programs/apps/wiki/frontends/tango.io/` (index.md, latest/*.md). Statusschlüssel: **falsch** = von einer Quelle widerlegt, **erfunden** = keine Quelle gefunden, Aussage entfernt, **nicht verifiziert** = in dieser Prüfung keine Quelle gefunden.

Insgesamt beschreiben die bisherigen Seiten ein anderes Produkt (ein blockbasiertes Team-Wiki mit öffentlicher REST-API). Das Produkt, das zum Namen passt, ist ein Werkzeug von der Aufnahme zur Anleitung bei tango.ai. Fast alle API-, Tastenkürzel- und Menüinhalte sind erfunden.

### index.md

| Bisherige Aussage | Status | Richtige Tatsache | Quelle |
|---|---|---|---|
| „Tango.io is a modern knowledge-management platform that focuses on collaboration.“ | falsch | Tango (tango.ai) zeichnet einen Prozess auf und macht daraus eine Schritt-für-Schritt-Anleitung. Kein Wiki. | https://help.tango.ai/en/ |
| Das gemeinte Produkt sei tango.io | falsch | `tango.io` ist ein Dienstleistungsunternehmen „Tango“ ohne Aufnahme-Produkt. Das Produkt liegt bei tango.ai. | https://tango.io/ ; https://www.tango.ai/ |
| Versionstabelle „6/7“, `themes/index.md` fehlt | behoben | Themes-Datei ist jetzt geschrieben; Branding ist die einzige dokumentierte Theme-Oberfläche. | [themes](latest/themes/index.md) |
| „Notable ideas: to do“ | behoben | Aufnahme zur Anleitung, teilbare Ansichten, Tango MCP. | [index](index.md) |

### latest/api.md (ganze Datei)

| Bisherige Aussage | Status | Richtige Tatsache | Quelle |
|---|---|---|---|
| REST-API unter `https://api.tango.io/v1` | erfunden | Keine öffentliche API dokumentiert. | https://help.tango.ai/en/collections/3466202-team-workspaces ; Suche nach öffentlicher API ergab nichts |
| Endpunkte `/v1/pages`, `/v1/workspaces`, `/v1/users`, `/v1/comments`, `/v1/search`, `/oauth/token`, `/oauth/authorize` | erfunden | Keine dokumentiert. | ebenso |
| OAuth2-Flows (Authorization Code und Client Credentials), Header `X-API-Key` | erfunden | Keine dokumentiert. Die einzige dokumentierte Anmeldung ist für den Tango-MCP-Connector (OAuth) und SSO für Nutzer. | https://help.tango.ai/en/articles/17890522-how-do-i-connect-tango-to-my-ai-assistant ; https://www.tango.ai/pricing |
| Ratenlimits 1000/h, 100/min, Header `X-RateLimit-*` | erfunden | Keine API, keine Limits dokumentiert. | — |
| Webhooks (`page.created`, `comment.created`, …) und „Settings > Webhooks“ | erfunden | Keine Webhooks dokumentiert. | — |
| SDKs `@tangoio/sdk`, `tangoio-sdk`, `tangoio-go`, `tangoio-java-sdk`, Installationsbefehle | erfunden | Keine gefunden. Installiere diese Namen nicht: sie sind nicht verifiziert und könnten anderen gehören. | — |
| Python-, Node.js- und curl-Beispiele | erfunden | Nicht zutreffend. | — |
| Support-Aufrufe (`GET /v1/pages/:id` usw.) | erfunden | Nicht zutreffend. | — |

### latest/description.md

| Bisherige Aussage | Status | Richtige Tatsache | Quelle |
|---|---|---|---|
| „Knowledge-management platform focused on collaboration and document management“ | falsch | Prozessdokumentation und Anleitung innerhalb der Anwendung. | https://www.tango.ai/ |
| Backend Node.js, Datenbank PostgreSQL, Frontend React | nicht verifiziert | Keine Quelle. Aus unseren Dokumenten entfernen. | — |
| Authentifizierung OAuth2, SSO | teilweise falsch | SSO und SCIM sind Enterprise. OAuth gilt nur für den MCP-Connector. | https://www.tango.ai/pricing ; https://help.tango.ai/en/articles/17890522-how-do-i-connect-tango-to-my-ai-assistant |
| „Real-time collaboration“ | nicht verifiziert | Keine Quelle. | — |
| „Strong embeds: 100+ embeds“ | nicht verifiziert | Einbettungen existieren (iframe in Wissensdatenbanken; mit einem Klick für Notion, Confluence, Zendesk). Die Anzahl wird nicht genannt. | https://help.tango.ai/en/articles/7142097-how-do-i-embed-a-tango-into-my-website-or-knowledge-base |
| „Cheaper than Confluence“, Vergleiche mit Notion, Confluence, Wiki.js | nicht verifiziert | Die Preise des Anbieters sind veröffentlicht; die Vergleiche nicht. | https://www.tango.ai/pricing |
| „Block-based“-Bearbeitung | falsch | Schrittliste mit Screenshots und Text je Schritt. | https://help.tango.ai/en/articles/7966907-how-do-i-use-tango-for-documentation |
| „Commercial, comes with support“ | teilweise | Kommerziell, ja. Support-Stufen nicht geprüft. | https://www.tango.ai/pricing |
| Zielgruppe (Teams, Startups, Design-Teams) | nicht verifiziert | Das eigene Hilfezentrum nennt Einarbeitung, Support und IT-Dokumentation. | https://help.tango.ai/en/ |

### latest/features.md

| Bisherige Aussage | Status | Richtige Tatsache | Quelle |
|---|---|---|---|
| „Visual editor modelled on Notion“ mit H1–H6, Aufgabenlisten, Emojis, Seitenlinks, @-Erwähnungen, Zeitstempeln | erfunden | Kein solcher Editor dokumentiert. Der Editor arbeitet mit Schritten. | https://help.tango.ai/en/collections/4063296-capturing-editing |
| 12 Blocktypen (Text, Tabelle, To-do, Zitat, Datei …) und Kürzel `-[ ]`, `*`, `1.` | erfunden | Nicht dokumentiert. | — |
| Codeblöcke mit 20+ Sprachen | erfunden | Nicht dokumentiert. | — |
| Tabellen mit Filter, Sortierung, Spaltenformeln | erfunden | Nicht dokumentiert. | — |
| Vorlagen (Besprechungsprotokoll, Fehlerbericht …) | erfunden | Keine Vorlagenfunktion in den gelesenen Hilfe-Sammlungen gefunden. | https://help.tango.ai/en/collections/3466202-team-workspaces |
| Einbettungen: YouTube, Figma, Spotify … 100+ | nicht verifiziert | Nur „Video embeds“ (Pro) ist als Funktionsname dokumentiert. | https://www.tango.ai/pricing |
| „No Markdown“ im Editor | nicht verifiziert | Markdown ist ein Exportformat (Pro/Ent). | https://www.tango.ai/pricing |
| Vergleichstabelle und Abschnitt „Empfehlung“ | erfunden | Marketinginhalte, nicht prüfbar. Entfernt. | — |
| Echte Funktionen fehlen auf der Seite | Lücke | Aufnahme, Neuordnung der Schritte, Verzweigung, Live Blur, Secure Blur, Annotation, Branding, Guide Me, Pins. | [Funktionen](latest/features.md) |

### latest/layout.md

| Bisherige Aussage | Status | Richtige Tatsache | Quelle |
|---|---|---|---|
| Linke Seitenleiste: Home, Pages, Files, Templates, Members, Dashboard, Settings; Arbeitsbereich-Auswahl | nicht verifiziert | Nicht dokumentiert. Dokumentierte Bereiche: Seitenleiste im Browser, Aufnahme-Steuerung, Editor, Teilen & Exportieren, Team-Bibliothek, Einstellungen & Mitglieder. | [Layout](latest/layout.md) |
| Kopfzeile mit Arbeitsbereich, Suche, Nutzermenü | nicht verifiziert | Nicht dokumentiert. | — |
| Drei Layoutvarianten (Standard, kompakt, Vollbild-Editor) | nicht verifiziert | Nicht dokumentiert. | — |
| Helle / dunkle / eigene Farbthemen | nicht verifiziert | Nicht dokumentiert. Nur Branding (Logo, Farben der Aktionsbox, Badge). | https://help.tango.ai/en/articles/5971709-can-i-add-my-own-branding-to-tango-workflows |
| Responsiv: Tablet und Mobil mit Hamburger-Menü | falsch | Keine mobile App; keine Aufnahme auf Smartphones oder Tablets; Anleitungen öffnen sich im mobilen Browser. | https://help.tango.ai/en/articles/17359491-where-does-tango-work |
| Barrierefreiheit (ARIA, hoher Kontrast, Zoom) und Leistung (Lazy Loading, Debounce) | nicht verifiziert | Ein Barrierefreiheits-Artikel existiert, wurde aber nicht gelesen. | https://help.tango.ai/en/articles/6081830-what-accessibility-features-does-tango-include |
| Automatisches Speichern | nicht verifiziert | Nicht dokumentiert. | — |
| ASCII-Diagramm des Blockeditors | erfunden | Nicht zutreffend. | — |

### latest/menus.md

| Bisherige Aussage | Status | Richtige Tatsache | Quelle |
|---|---|---|---|
| 12 Hauptpunkte (Home, Workspace, Pages, Templates, Files, People, Settings, Search, Dashboard, Notifications, Bookmark, Recently viewed) | erfunden | Nicht als Menü dokumentiert. Die Seitenleiste zeigt markierte und zuletzt angesehene Anleitungen; Team-Bibliothek; es gibt die Sammlung „Insights & Analytics“. | https://help.tango.ai/en/articles/7926363-how-do-i-use-the-tango-side-panel ; https://help.tango.ai/en/collections/15535477-insights-analytics |
| Kontextmenü einer Seite: Edit, Copy, Move, Delete, Share, Print, Export | nicht verifiziert | Teilen & Exportieren und Sammelaktionen sind dokumentiert. | [Menüs](latest/menus.md) |
| Mitglieder-, Datei-Menüs | nicht verifiziert | Mitglieder über Einstellungen & Mitglieder. | — |
| Import/Export des Arbeitsbereichs, Statistik des Arbeitsbereichs | nicht verifiziert | Download des Audit-Protokolls ist dokumentiert (Enterprise). | https://help.tango.ai/en/articles/13259730-how-do-i-download-a-workspace-wide-audit-log |

### latest/shortcuts.md (fast ganze Datei)

| Bisherige Aussage | Status | Richtige Tatsache | Quelle |
|---|---|---|---|
| Etwa 150 Tastenkürzel: Ctrl+Shift+P Befehlspalette, Ctrl+K Link, Ctrl+B fett, Ctrl+Shift+1–6 Überschriften, Ctrl+Shift+J/P/H/C/S/M/E Code-Syntax, Ctrl+S speichern, Ctrl+P drucken, F11 Vollbild, Ctrl+Shift+I Entwicklertools, und Mac-Varianten | erfunden | Nicht dokumentiert. Dieselbe Tastenkombination steht in derselben Tabelle für verschiedene Aktionen (z. B. Ctrl+Shift+X Ausschneiden und Durchstreichen; Ctrl+Shift+P Befehlspalette, Absatz und Python; Ctrl+Shift+C Codeblock, CSS und Kopieren). Eine Tabelle mit solchen Kollisionen ist keine echte Tastenbelegung. | — |
| Nur verifizierte Tastenkürzel | Tatsache | Ctrl/Cmd+Z rückgängig, Ctrl/Cmd+Y wiederholen (Editor, Bearbeitungsmodus). Team-Bibliothek: Shift+Klick, Ctrl/Cmd+A, Ctrl/Cmd+Klick, Esc. Cmd+K Suche (Suchausschnitt). | [Rückgängig](https://help.tango.ai/en/articles/17747616-how-do-i-undo-changes-in-the-tango-editor) ; [Sammelaktionen](https://help.tango.ai/en/articles/16652169-how-do-i-use-bulk-actions-in-the-team-library) ; [Tastenkürzel](latest/shortcuts.md) |
| Absatz über Mac und Code-Syntax | erfunden | Nicht zutreffend. | — |

### Sonstiges

- Der Seitenname „Tango.io“ ist eine Namensverwechslung. Der Dokumentationsbaum sollte das Produkt „Tango“ nennen und auf tango.ai verlinken, mit einem Hinweis, dass tango.io ein anderes Unternehmen ist.
- Die Regel für `changelog.md` (ADR 0012, ≥ 2 Versionen) ist nicht erfüllt: nur eine Version.
