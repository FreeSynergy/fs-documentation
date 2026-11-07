# Wiki.js 3.1.1: Funktionen

Am Quellcode von 3.1.1 geprüft. Quellen sind je Zeile angegeben. „Nicht verifiziert“ bedeutet, dass die Funktion weder im Quellcode noch in der offiziellen Dokumentation bestätigt wurde.

## Seiten

| Funktion | Kann | Quelle |
|---------|-----|--------|
| Seite an einem Pfad mit Editor anlegen | ja; der Editor ist einer der aktiven Editoren des Standorts | `backend/api/pages.ts` (`POST /sites/:siteId/pages`), `backend/api/schemas/page.ts` (Feld `editor`) |
| Seite bearbeiten | ja; `PATCH` für Metadaten, `PUT .../editor` für Inhalt | `backend/api/pages.ts` |
| Umbenennen / verschieben | ja; `PUT .../path` | `backend/api/pages.ts` |
| Duplizieren | ja (UI-Aktion „Duplicate Page“) | `frontend/src/components/PageActionsCol.vue` |
| Löschen | ja; weiches Löschen, aufgelistet unter `.../pages/deleted`, Wiederherstellungs-Endpunkt existiert | `backend/api/pages.ts`, Locale-Text `common.page.delete` („can be restored from the administration area“) |
| Versionsverlauf | ja; Liste, eine Version lesen, nach Versions-ID lesen | `backend/api/pages.ts` (`.../history`, `.../history/:versionId`, `/sites/:siteId/versions/:versionId`) |
| Seitenquelle anzeigen | ja („Page Source“-Aktion) | `PageActionsCol.vue` |
| Neu rendern | ja („Rerender“-Aktion und Endpunkt `.../render`) | `PageActionsCol.vue`, `backend/api/pages.ts` |
| Seite in einen anderen Editor umwandeln | ja („convertPage“-Aktion im Seitenaktionsmenü) | `PageActionsCol.vue` |
| Veröffentlichungsstatus | ja; Suchfilter `publishState`; Warnung bei unveröffentlicht | `backend/api/pages.ts`, Locale `common.page.unpublishedWarning` |
| Seite mit Passwort gesperrt | ja; Endpunkt zum Entsperren `.../unlock` | `backend/api/pages.ts`, Locale `common.page.locked` |
| Aliase und ID-Links | ja; Routen `/a/:alias` und `/i/:pageId` | `frontend/src/router/routes.js` |
| Seitenbewertung (Daumen hoch/runter) | ja | Locale `common.page.ratePage`, `ratingThumbsUp` |
| Seite beobachten | ja; Routen `watching` | `frontend/src/router/routes.js` (`/_inbox/watching`), Locale `common.page.watch` |
| Rückverweise und ausgehende Links | ja; `.../backlinks`, `.../links` | `backend/api/pages.ts` |
| Tags | ja; Tag-Seite `/_tags`; Suchfilter `tags` mit `tagsMatch` | `routes.js`, `backend/api/pages.ts` |
| Locales | ja; Standort-Locales, Locale-Beziehungen (`.../locale-relations`) | `backend/api/pages.ts`, `backend/models/sites.ts` |
| Inhaltsverzeichnis | ja; Position ist eine Theme-Einstellung | `backend/models/sites.ts` (`tocPosition`) |
| Druckformat | ja; Druckknopf ist eine Theme-Einstellung | `backend/models/sites.ts` (`showPrintBtn`), Locale `common.page.printFormat` |
| Fortschrittsbalken der Seite | ja; Theme-Einstellung | `backend/models/sites.ts` (`showPageProgress`) |
| Änderungsvorschläge durch Leser | ja; Vorschläge gehen in eine Freigabe-Warteschlange | Locale `common.actions.suggestEdits`, `backend/models/approvals.ts`, Route `/_inbox/review` |
| Kommentare | ja; Admin-Bereich hat einen Abschnitt für Kommentare | `backend/api/comments.ts`, `routes.js` (`:siteid/comments`) |
| Seiteneigentum und Lebenszyklus | ja | `.claude/rules/page-lifecycle.md`, `backend/api/pageOwners.ts`, `backend/api/pageLifecycle.ts` |

## Editoren

Jeder Editor hat eine ID, die mit der Seite gespeichert wird. Ein Standort listet, welche Editoren aktiv sind (`backend/models/sites.ts`, Block `editors`).

| Editor-ID | Was es ist | Quelle |
|-----------|-----------|--------|
| `markdown` | Monaco-basierter Markdown-Editor mit Live-Vorschau und einer linken Leiste „insert“ | `frontend/src/components/EditorMarkdown.vue` |
| `visual` | ProseMirror-basierter Rich-Text-Editor mit Slash-Menü, Tabellen, Reitern und Aufgabenlisten | `frontend/src/editor/visual/` |
| `asciidoc` | Monaco-basierter AsciiDoc-Editor | `frontend/src/components/EditorAsciidoc.vue` |
| `excalidraw` | Zeichen-Editor (Excalidraw 0.18.1), mit Zusammenarbeit | `frontend/src/components/EditorExcalidraw.vue`, `frontend/src/editor/excalidraw/` |
| `blog` | Blog-Seitentyp mit eigener Auflistung | `frontend/src/components/EditorBlog.vue` |
| `feedback` | Feedback-Board: Ideen, Kategorien, Stimmen | `frontend/src/components/EditorFeedback.vue` |
| `redirect` | Seite, die den Leser weiterleitet; nie durchsuchbar | `backend/api/schemas/page.ts` |

Die Dokumentation nennt dieselben acht Editoren (https://docs.js.wiki/guide/editors). Die Dokumentationsseite nennt „Live Notes Editor“ als einen davon; im Quellcode sind Live-Notizen eine eigene Route (`/n/`) und kein Eintrag im Block `editors`.

### Verifizierte Funktionen des Markdown-Editors

- Tastenkürzel für fett, kursiv, Überschriftenebene und Speichern (siehe `shortcuts.md`).
- Snippet-artige Einfügungen für Abkürzungen und andere Blöcke (`EditorMarkdown.vue`, `snippetEscape`).
- Vervollständigungen für Links, Tags, Codeblöcke (fences) und Blöcke (`frontend/src/composables/linkCompletions.js`, `tagCompletions.js`, `fenceCompletions.js`, `blockCompletions.js`).
- Dialog mit Bildeigenschaften über Bildern (`frontend/src/composables/imagePropertiesDialog.js`).
- Echtzeit-Zusammenarbeit über die Yjs-Bindung für Monaco (`y-monaco`).

### Verifizierte Funktionen des Visual-Editors

- Block- und Markierungsbefehle, aufgelistet in `shortcuts.md`.
- Slash-Menü (`frontend/src/editor/visual/slash.js`).
- Reiter-Block (`nodeviews.js`, Locale `editor.visual.tabs.*`).
- Zusammenarbeit über Yjs (`frontend/src/editor/visual/collab.js`).

### Andere Funktionen, die nicht verifiziert wurden

Snippet-Bibliothek, Emoji-Auswahlmenü (eine Datei existiert, `EditorEmojiMenu.vue`, aber ihr Verhalten wurde nicht gelesen), Details der Tabellenbearbeitung, Optionen für Mathe- und Diagrammdarstellung sowie der Markdown-Import/-Export-Kreislauf des Visual-Editors. Nicht verifiziert.

## Navigation und Suche

| Funktion | Kann | Quelle |
|---------|-----|--------|
| Volltextsuche | ja; Abfrage plus Filter `path`, `locales`, `tags`, `tagsMatch`, `editor`, `publishState`, `creatorId`, `authorId`, `orderBy`, `orderByDirection`, `offset`, `limit` | `backend/api/pages.ts` (`GET /sites/:siteId/pages/search`) |
| Vorschläge / Autovervollständigung für Seiten | ja; `.../pages/suggest` und `.../pages/suggest-path` | `backend/api/pages.ts` |
| Baum durchsuchen | ja; `.../tree`, `.../tree/browse`, `.../tree/pages`, `.../tree/graph` | `backend/api/tree.ts` |
| Navigationseditor | ja; Admin „Navigation“ und Schaltfläche „Edit Nav“ in der Seitenleiste | `routes.js`, `frontend/src/components/NavEditMenu.vue` |
| Sitemap | ja; Locale `common.header.siteMap` | Locale-Datei |
| Ordner anlegen / verschieben / löschen | ja; Endpunkte `.../tree/folders` | `backend/api/tree.ts` |
| Dateiverwaltung (Assets) | ja; Drag and Drop zum Verschieben in 3.0.1 | https://github.com/requarks/wiki/releases/tag/3.0.1 |

## Konten und Zugriff

| Funktion | Kann | Quelle |
|---------|-----|--------|
| Gruppen mit Seitenregeln | ja | `routes.js` (`groups`), `backend/api/groups.ts` |
| Persönliche Zugriffstoken mit Bereichen (`pages`, `assets`, `comments`, `glossary`, `navigation`, `approvals`, `profile`, `mcp`) | ja | `frontend/src/helpers/personalTokens.js` (spiegelt `backend/models/personalTokens.ts`) |
| Profilabschnitte (Infos, Avatar, Authentifizierung, Gruppen, Notizen, Token, Benachrichtigungen) | ja | `routes.js` (`/_profile/*`) |
| Zwei-Faktor und Passkeys | ja, in den Kontoeinstellungen | `backend/models/passkeys.ts`, `backend/api/personalTokens.ts`-Kommentar („passwords, 2FA, passkeys“) |
| SCIM | ja; Admin-Abschnitt und Endpunkt `/_scim` | `routes.js` (`scim`), `backend/api/schemas/scim.ts` |

## Was Wiki.js 3.1.1 nicht kann (verifiziert oder im Quellcode genannt)

| Grenze | Quelle |
|-------|--------|
| Kein GraphQL-Endpunkt | keine Datei `graphql` und keine Abhängigkeit im Baum von 3.1.1 |
| Persönliche Token können keine Admin-Routen erreichen | `backend/index.ts` (Bearer-Hook: Tokens werden auf Routen ohne Bereich abgelehnt), `.claude/rules/personal-access-tokens.md` |
| Persönliche Token werden nur auf `/_api` und `/_mcp` akzeptiert | `backend/index.ts` |
| API-Schlüssel können nicht im Namen eines Nutzers handeln (keine Nutzerzuordnung) | Dokumentation https://docs.js.wiki/dev/api |
| Annahmen zur Atomarität eines einzelnen Prozesses bei manchen Schreibvorgängen | `backend/CLAUDE.md` (HA-Satz, Advisory-Lock beim Start) |

## Nicht verifiziert (alte Seiten behaupteten dies; als unbekannt behandeln)

- Markdown-Frontmatter als Funktion für Nutzer (nur als Speicherdetail in `helpers/storageFiles.ts` gesehen).
- Intervall des automatischen Speicherns.
- Tastenkürzel für eine Befehlspalette, globale Suche, Dateibaum, Umschalten der Live-Vorschau und neue Seite (im Quellcode nicht gefunden).
- Plugin-System für Editoren und Renderer über die Speicher- und Auth-Module hinaus.
- Namen der Mermaid-, KaTeX-, Kroki- und Syntax-Hervorhebungs-Plugins. Der Quellcode hat `frontend/src/renderers/modules/katex.js` und `kroki.js`; Mermaid wurde nicht geprüft.
