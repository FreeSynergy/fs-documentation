# Änderungsprotokoll

## 2026-11-07: neu geschrieben aus offiziellen Quellen

Die früheren Seiten waren aus dem Gedächtnis geschrieben; diese Aussagen waren falsch.

Bestehende Seiten: `/srv/FreeSynergy/fs-documentation/docs/en/programs/apps/wiki/frontends/wikijs/` (index.md und latest/*.md). Sie wurden aus dem Gedächtnis geschrieben und beschreiben eine Mischung aus Wiki.js 2.x und allgemeinen Wiki-Funktionen. Statuscodes:

- **W** falsch für 3.1.1 (am Quellcode oder an der offiziellen Dokumentation geprüft)
- **U** nicht überprüfbar (keine Quelle gefunden; entfernen oder kennzeichnen)
- **M** im alten Satz fehlend
- **OK** richtig, übernommen

Quellbasis für 3.1.1: https://github.com/requarks/wiki/tree/3.1.1 (Kurzform `3.1.1:<path>`). Fakten zu 2.x: https://github.com/requarks/wiki/tree/v2.5.315 (Kurzform `2.5.315:<path>`).

### index.md

| Status | Alte Aussage | Richtige Tatsache | Quelle |
|--------|---------------|--------------|--------|
| U | „modern, lightweight wiki system“ | „lightweight“ hat keine Quelle. Offizieller Wortlaut: „The open source wiki engine. Built and maintained in the open since 2017.“ | https://js.wiki/ |
| M | „Notable ideas: _To do_“ | in `index.md` ausgefüllt (Speicherziele, acht Editoren, Yjs, persönliche Token, MCP) | `3.1.1:backend/modules/storage/`, `3.1.1:backend/models/sites.ts` |
| W | „Documented versions: latest“ | die neueste 3.x ist **3.1.1** (2026-11-06); 3.1.0 existiert (2026-11-05); 3.1 ist veröffentlicht, nicht fehlend | https://github.com/requarks/wiki/releases |

### description.md

| Status | Alte Aussage | Richtige Tatsache | Quelle |
|--------|---------------|--------------|--------|
| W | Datenbank: „PostgreSQL, MySQL, SQLite“ | 3.1.1 nutzt nur PostgreSQL (pg-Treiber, Drizzle `node-postgres`) | `3.1.1:backend/core/db.ts`, `3.1.1:backend/package.json` |
| W | Frontend: „Vue.js“ | Vue 3.5, Vite 8, Pinia, Tailwind 4 (2.x nutzte Vue 2 und Vuetify 2) | `3.1.1:frontend/package.json`, `2.5.315:package.json` |
| W | Authentifizierung: „OAuth2, LDAP, SAML (via extensions)“ | eingebaut: lokal, LDAP, OIDC, SAML, GitHub, Google, Discord, Entra | `3.1.1:backend/modules/authentication/` |
| W | „Two editor modes: WYSIWYG for beginners, Markdown for advanced users“ | acht Editortypen je Standort: markdown, visual, asciidoc, excalidraw, blog, feedback, redirect, dazu Live-Notizen | `3.1.1:backend/models/sites.ts`, https://docs.js.wiki/guide/editors |
| W | „Confluence has better enterprise features (SSO, audit logs)“ | 3.1.1 hat ein Audit-Protokoll, SAML, OIDC, SCIM und Gruppen. Der Vergleich selbst ist nicht überprüfbar. | `3.1.1:backend/models/auditLog.ts`, `3.1.1:backend/api/scim.ts` |
| U | „Modularly extensible: plugin system for additional functions“ | Module werden für Auth und Speicher von der Festplatte gefunden; kein Plugin-Marktplatz und keine Editor-Plugin-API gefunden | `3.1.1:backend/CLAUDE.md` (Module) |
| U | „Good performance“, „Modern design“, „more lightweight than MediaWiki“, „more modern than MediaWiki“ | Meinung oder Werbung; keine Quelle | — |
| U | „Notion has better visual design“ | Meinung | — |
| U | Liste „Who Wiki.js suits“ | nicht vom Projekt; keine Quelle | — |
| U | „Hosting: self-hosted or cloud“ | offizielle Installationsmethoden: Docker, Kubernetes, Bare Metal, Cloud-Images. Die Formulierung „cloud“ als gehosteter Dienst wurde nicht geprüft. | https://js.wiki/ |
| OK | „Backend: Node.js“ | Node.js >= 26 mit Fastify 5 | `3.1.1:backend/package.json` |
| OK | „Open source“ | AGPL-v3-Lizenz | `3.1.1:LICENSE` |

### features.md

| Status | Alte Aussage | Richtige Tatsache | Quelle |
|--------|---------------|--------------|--------|
| W | „Two editor modes“ (WYSIWYG und Markdown) | siehe description.md: acht Editortypen | wie oben |
| W | Erweiterbar durch Plugins: „Mermaid, LaTeX, Kroki, MathJax, VideoJS, Embeds for Spotify, Twitter“ | Renderer-Module vorhanden: katex, kroki, plantuml, markdown-it-Plugins. Mermaid, MathJax, VideoJS, Spotify und Twitter nicht gefunden. | `3.1.1:frontend/src/renderers/modules/` |
| U | „Syntax highlighting for 200+ languages“ | highlight.js 11.12.0 ist die Bibliothek; die Sprachanzahl wurde nicht geprüft | `3.1.1:frontend/package.json` |
| U | Visual-Editor: „Alignment: left, centre, right, justified“, „Text colour not supported“, „no vertical text alignment“ | nicht geprüft | — |
| U | „Notices/boxes: info, warning, success“ | 3.1.1 hat Inhaltsblöcke (`blocks/block-tabs`, `block-steps`, `block-spoiler`, `block-youtube`, `block-qr-code`, …); die Hinweisarten wurden nicht geprüft | `3.1.1:blocks/` |
| U | „Embeds: videos (YouTube, Vimeo), iframes“ | YouTube-Block existiert; Vimeo und iframes nicht geprüft | `3.1.1:blocks/block-youtube` |
| U | „Images: drag & drop“ in beiden Editoren | es gibt eine Warteschlange für Asset-Uploads; Drag and Drop nicht bestätigt | `3.1.1:frontend/src/components/PageActionsCol.vue` |
| U | „Front matter: metadata for pages (title, description)“ als Nutzerfunktion | Frontmatter erscheint nur im Speichermodul (disk, git, sftp) | `3.1.1:backend/helpers/storageFiles.ts` |
| U | „Snippets: templates for frequently used blocks“ | der Markdown-Editor hat Snippet-Einfügungen für einige Blöcke (Abkürzung); eine allgemeine Snippet-Bibliothek nicht verifiziert | `3.1.1:frontend/src/components/EditorMarkdown.vue` |
| U | „Live preview“ in Markdown | Vorschau mit Scroll-Synchronisation vorhanden | `3.1.1:frontend/src/composables/previewScrollSync.js` |
| U | Vergleichstabelle (Table-Editor visuell vs. Text, „no WYSIWYG while editing“) | nicht geprüft | — |
| OK | Markdown-Unterstützung: GitHub-artige Tabellen, Aufgabenlisten, Durchstreichen | markdown-it mit Plugins für Aufgabenlisten und Multi-Tabellen | `3.1.1:frontend/package.json` |
| M | (fehlt) Zusammenarbeit, Seitenverlauf, Kommentare, Feedback-Boards, Freigaben, Blogs, Glossar, MCP | alle in 3.1.1 vorhanden | siehe `3.1.1/features.md` |

### layout.md

| Status | Alte Aussage | Richtige Tatsache | Quelle |
|--------|---------------|--------------|--------|
| W | Seitenleisten-Einträge: Home, Pages, Media, Users, Groups, Settings | die Schublade enthält den Navigationsbaum des Standorts, ein Durchsuchen-Menü und „Edit Nav“; Admin-Abschnitte liegen im Admin-Bereich | `3.1.1:frontend/src/components/NavSidebar.vue`, `3.1.1:frontend/src/router/routes.js` |
| W | „Sidebar (right): optional meta information (versions, author)“ | die rechte Seite ist die Seitenaktionsleiste (48 px) und die Position des Inhaltsverzeichnisses; die Seitenleiste kann rechts liegen, aber keine Metaspalte | `3.1.1:frontend/src/css/_theme.scss`, `3.1.1:backend/models/sites.ts` |
| W | „Mobile: hamburger menu“ | kein Menüknopf in der Kopfzeile; auf schmalen Bildschirmen ist die Schublade ein Overlay, geöffnet über eine Schaltfläche unten links | `3.1.1:frontend/src/layouts/MainLayout.vue` (Kommentar zur Ecken-Schaltfläche) |
| U | „Breadcrumbs: the navigation path“ | eine Breadcrumb-Komponente existiert (`WBreadcrumbs.vue`); ihre Verwendung in der Seitenansicht wurde nicht geprüft | `3.1.1:frontend/src/components/shared/WBreadcrumbs.vue` |
| U | „Status bar (words, characters, preview button)“ im WYSIWYG | nicht geprüft | — |
| U | „Full-screen editor: only the editor“ | nicht geprüft | — |
| U | „Auto-save“ | nicht geprüft | — |
| U | Typografie: „H1–H6“, „14–16 px“ | nicht extrahiert | — |
| U | „Tablet: reduced sidebar“ | nicht geprüft | — |
| OK | Helles und dunkles Theme, eigene Farben | dunkler Schalter und fünf Markenfarben je Standort | `3.1.1:backend/models/sites.ts` |
| OK | Barrierefreiheit: Tastaturnavigation, ARIA-Labels | Symbolschaltflächen tragen `aria-label` | `3.1.1:frontend/src/components/HeaderNav.vue` |

### menus.md

Die ganze alte Menüliste ist für 3.1.1 falsch.

| Status | Alte Aussage | Richtige Tatsache | Quelle |
|--------|---------------|--------------|--------|
| W | Hauptmenü: Home, Pages, Editor, Trash, Media, Users, Groups, Access, Settings, Appearance, Extensions, Logs, Search | Kopfzeile: Home, Suche, Erstellen, Bibliothek, Posteingang, Administration, Anmeldung/Konto. Admin: etwa 40 Routen (Dashboard, Sites, General, Approvals, Analytics, Blocks, Comments, Editors, Locale, Login, Navigation, Storage, Theme, Auth, Groups, Users, SCIM, API, MCP, Webhooks, Audit, Extensions, Icons, Mail, Metrics, Notifications, Rendering, Scheduler, Search, Security, System, Terminal, Utilities, Flags, …) | `3.1.1:frontend/src/router/routes.js`, `HeaderNav.vue` |
| W | Kontextmenü einer Seite: Edit, Move, Copy, Delete, Show history, Permissions | die Seitenleiste hat: Seiteneigenschaften, Seitendaten, Verlauf, Quelle, Aktionen (umwandeln, neu rendern), Duplizieren, Umbenennen / Verschieben, Löschen. Die Rechteansicht ist ein API-Aufruf (`.../pages/userPermissions`), kein Menüpunkt in der Leiste. | `3.1.1:frontend/src/components/PageActionsCol.vue` |
| W | Nutzermenü: Profile, Settings, Sign out | Profilabschnitte: Infos, Avatar, Authentifizierung, Gruppen, Live-Notizen, Zugriffstoken, Benachrichtigungen; Abmelden im Konto-Eintrag der Kopfzeile | `3.1.1:frontend/src/router/routes.js`, Locale `common.header.logout` |
| U | „Trash: manage deleted pages“ als Hauptmenüpunkt | gelöschte Seiten können „aus dem Verwaltungsbereich“ wiederhergestellt werden (Locale-Text); ein Listen-Endpunkt existiert | `3.1.1:backend/api/pages.ts` (`/sites/:siteId/pages/deleted`) |
| U | „Logs“ | der Admin hat Audit, Metrics, System, Terminal; der Name „Logs“ wurde nicht geprüft | `routes.js` |
| U | „Search: filter options“ | Suche existiert mit Filtern (siehe api.md); der Menüpunktname wurde nicht geprüft | `3.1.1:backend/api/pages.ts` |

### shortcuts.md

Der größte Teil der alten Liste steht nicht im Quellcode von 3.1.1. Die richtige Liste steht in `3.1.1/shortcuts.md`.

| Status | Alte Tastenkürzel | Richtige Tatsache | Quelle |
|--------|--------------|--------------|--------|
| W | Ctrl+Shift+P Befehlspalette | nicht gefunden | Suche im Frontend-Quellcode |
| W | Ctrl+, Einstellungen; F1 Hilfe; Ctrl+Shift+F globale Suche | nicht gefunden | Suche im Frontend-Quellcode |
| W | Ctrl+K Link; Ctrl+K-Link-Kürzel | nicht in den Markdown- oder Visual-Belegungen gefunden | `3.1.1:frontend/src/editor/visual/commands.js`, `EditorMarkdown.vue` |
| OK | Ctrl+B fett (Visual) | richtig für beide Editoren (Mod+B) | `3.1.1:frontend/src/editor/visual/commands.js`, `EditorMarkdown.vue` |
| W | Ctrl+B Seitenleiste ein- oder ausblenden (Abschnitt Ansicht) | Mod+B ist fett in den Editoren; kein Kürzel für die Seitenleiste gefunden | wie oben |
| W | Ctrl+Shift+L Aufzählungsliste | Mod+Shift+8 ist die Aufzählungsliste (Visual) | `3.1.1:frontend/src/editor/visual/commands.js` |
| W | Ctrl+Shift+1…6 Überschriften | richtig (Visual, Mod+Shift+1 bis 6) | `commands.js` |
| W | Ctrl+Shift+X Durchgestrichen | richtig (Mod+Shift+X) | `commands.js` |
| W | Ctrl+Shift+K Code-Tag; Ctrl+Shift+C Codeblock; Ctrl+Shift+M Zitat | Code: Mod+E (Code im Text); Zitat: Mod+Shift+. (Blockzitat); Codeblock: keine Belegung (Mod+Enter verlässt einen Codeblock) | `commands.js` |
| W | Ctrl+E / Ctrl+L / Ctrl+R Ausrichtung; Ctrl+Shift+E Blocksatz | Mod+E ist Code im Text; keine Ausrichtungsbelegungen | `commands.js` |
| W | Ctrl+Shift+H ersetzen mit Kontext | Mod+Shift+H markiert Text im Visual-Editor | `commands.js` |
| W | Ctrl+Enter Vorschau oder veröffentlichen | Mod+Enter verlässt einen Codeblock (Visual); kein Veröffentlichungs-Kürzel gefunden | `commands.js` |
| W | Ctrl+Shift+V Live-Vorschau; Ctrl+Shift+F Dateibaum; Ctrl+Shift+B Statusleiste | nicht gefunden | Suche |
| W | Ctrl+N neue Seite; Ctrl+O Seite öffnen; Ctrl+W schließen; Ctrl+Shift+N neuer Ordner; Ctrl+P drucken oder Dateisuche | nicht gefunden; Ctrl+P drucken ist ein Browser-Kürzel | Suche |
| U | Ctrl+G / Ctrl+Shift+G nächster und vorheriger Treffer | Monaco-Standard im Markdown-Editor; keine Wiki.js-Belegung | Monaco |
| OK | Ctrl+S speichern | Mod+S im Markdown- und AsciiDoc-Editor lässt den Speichern-Knopf der Kopfzeile ausführen | `EditorMarkdown.vue`, `EditorAsciidoc.vue` |
| OK | Ctrl+Z rückgängig, Ctrl+Y wiederholen | Mod+Z, Mod+Shift+Z, Mod+Y (Visual) | `commands.js` |
| OK | Ctrl+Alt+Links/Rechts Überschriftenebene | Mod+Alt+Left/Right in Markdown- und AsciiDoc-Editoren | `EditorMarkdown.vue` |
| U | F11 Vollbild; Ctrl+Shift+I Entwicklertools | Browserfunktionen, nicht Wiki.js | — |
| U | Tastaturnavigation mit Pfeiltasten zwischen Blöcken | nur die Pfeile des Slash-Menüs verifiziert | `slash.js` |

### api.md

| Status | Alte Aussage | Richtige Tatsache | Quelle |
|--------|---------------|--------------|--------|
| W | REST-Basis `/api/v1/…` | REST-Basis ist `/_api/…`; standortbezogene Pfade `/_api/sites/:siteId/pages/…` | `3.1.1:backend/index.ts` (`prefix: '/_api'`), `3.1.1:backend/api/pages.ts` |
| W | GraphQL unter `/graphql`, „complete GraphQL API“ | kein GraphQL in 3.1.1. GraphQL gab es in 2.x (`server/graph/schemas`). | `3.1.1`-Baum (kein graphql); `2.5.315:server/graph/schemas/` |
| W | „API tokens: Configuration > API Tokens“ | Admin: Administration → API (Route `api`); persönliche Token: Profil → Zugriffstoken (`/_profile/tokens`) | `3.1.1:frontend/src/router/routes.js`, `3.1.1:.claude/rules/personal-access-tokens.md` |
| W | Authentifizierungs-Endpunkte `POST /api/v1/auth/login`, `/logout`, `/refresh` | nicht vorhanden. Abmelden ist `POST /_api/sites/:siteId/auth/logout`; Passkey-Anmeldung ist `PUT /_api/sites/:siteId/auth/passkey/login`. Route für Passwort-Anmeldung: im grep nicht gefunden. | `3.1.1:backend/api/authentication.ts` |
| W | `GET /api/v1/meta`, `/meta/stats` | nicht gefunden | `3.1.1:backend/api/` (Dateiliste) |
| W | Nutzer: `GET/POST/PUT/DELETE /api/v1/users` | Nutzer liegen unter `/_api/users…` (Präfix aus `index.ts`); Methoden nicht gelesen. Der alte Pfad ist nicht gültig. | `3.1.1:backend/index.ts` (`users.ts`, Präfix `/users`) |
| W | Seiten: `GET /api/v1/pages`, `PUT /api/v1/pages/:id`, `DELETE`, `GET /pages/:id/history` | Entsprechung existiert unter `/_api/sites/:siteId/pages…` (siehe `3.1.1/api.md`); Basispfad und `:siteId` unterscheiden sich | `3.1.1:backend/api/pages.ts` |
| W | „Create page“-Body: `title, description, content, path, public` | das Schema hat `path, title, description, locale, editor, content` und mehr; ein Feld `public` wurde nicht gefunden | `3.1.1:backend/api/schemas/page.ts` |
| W | Ratenlimit „100 requests per minute per API token“, Header `X-RateLimit-*` | nicht in 3.1.1; nur ein Limiter mit festem Zeitfenster für Anmeldungen | `3.1.1:backend/models/rateLimits.ts` |
| W | Webhook-Ereignisse `page.create`, `page.update`, `page.delete`, `page.move`, `page.revert` | Ereignisse in 3.1.1: `page:create`, `page:edit`, `page:rename`, `page:delete`, `asset:*`, `comment:*`, `user:join`, `user:login`, `user:logout` | `3.1.1:backend/models/hooks.ts` |
| W | Webhooks unter „Configuration > Webhooks“ | Administration → Webhooks (Route `webhooks`) | `3.1.1:frontend/src/router/routes.js` |
| U | Offizielle SDKs `wiki.js-api-client` (npm), `pywikijs` (PyPI) | im offiziellen Repo oder in der Dokumentation nicht gefunden. Nicht auflisten. | `3.1.1`-Baum; https://docs.js.wiki/dev/api |
| U | Python-Beispiel mit `requests` | erfunden, nicht ausgeführt; entfernt | — |
| W | „Session cookie: for internal use“ | die Oberfläche selbst nutzt das Sitzungscookie für alle Aufrufe | `3.1.1:frontend/CLAUDE.md` |
| OK | Bearer-Header für API-Schlüssel | `Authorization: Bearer <key>` ist richtig. Die Admin-Seite heißt API, und ein Systemschlüssel handelt für seine Gruppen, nicht für einen Nutzer. | https://docs.js.wiki/dev/api |
| M | Webhook-Signierung nicht beschrieben | keine Signatur-Kopfzeile in 3.1.1; das auf der Seite angeben | `3.1.1:backend/models/hooks.ts` |
| W | „See also“-Links: `menu.md`, `structure.md` | Zieldateien sind `menus.md` und `layout.md` | Ordnerliste `fs-documentation` |

### themes/index.md

| Status | Alte Aussage | Richtige Tatsache | Quelle |
|--------|---------------|--------------|--------|
| M | Datei fehlt (der generierte Index markiert sie) | im neuen Satz angelegt: `3.1.1/themes/index.md` | `3.1.1:backend/models/sites.ts`, `3.1.1:frontend/src/pages/AdminTheme.vue` |

### Versionsordner

| Status | Alte Aussage | Richtige Tatsache |
|--------|---------------|--------------|
| M | Ordner `latest/` | den genauen Release verwenden: `3.1.1/` (3.1.0 ist der vorherige Release; der Satz trennt 3.1.0 und 3.1.1 nicht, weil die Hinweise zu 3.1.1 nur Fehler- und Sicherheitskorrekturen enthalten; siehe `3.1.1/description.md`) |

Quelle für die Aussage, dass 3.1.1 nur Fehler- und Sicherheitskorrekturen enthält: https://github.com/requarks/wiki/releases/tag/3.1.1

### Noch nicht geprüft (offen)

- Ob die Dokumentationsseite (https://docs.js.wiki) dieselben Tastenkürzel beschreibt. Ihre Anleitungsseiten wurden aufgelistet, nicht gelesen; keine Tastenkürzel-Seite war aufgeführt.
- Das Ziel der Schaltfläche „Library“ in der Kopfzeile.
- Die genaue Wiederholungsregel für Webhooks.
- Die Route für die Passwort-Anmeldung.
