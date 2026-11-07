# Wiki.js 3.1.1: Beschreibung

Version: 3.1.1 (veröffentlicht 2026-11-06). Quellen: https://github.com/requarks/wiki/releases/tag/3.1.1 , https://github.com/requarks/wiki/tree/3.1.1

## Was es tut

Wiki.js ist ein selbst gehostetes Wiki. Ein Standort enthält einen Baum aus Seiten. Jede Seite hat einen Pfad, eine Locale, einen Editortyp, Tags und einen Versionsverlauf. Seiten können veröffentlicht oder nicht veröffentlicht, beobachtet, bewertet, kommentiert, verlinkt und durchsucht werden. Quellen: https://github.com/requarks/wiki/blob/3.1.1/backend/api/schemas/page.ts , https://github.com/requarks/wiki/blob/3.1.1/backend/api/pages.ts

Neben Seiten enthält die 3.x-Linie:

- Feedback-Boards (Ideen mit Kategorien und Stimmen), `frontend/src/components/EditorFeedback.vue`
- Blogs (ein Seitentyp mit eigener Auflistung), `EditorBlog.vue`
- Glossar, `backend/models/glossary.ts`
- Freigabe-Warteschlangen für Änderungsvorschläge, `backend/models/approvals.ts`
- Seiteneigentum und Lebenszyklusregeln, `.claude/rules/page-lifecycle.md`
- Installationen mit mehreren Standorten, eine Datenbank und ein gemeinsamer Satz Konten (`backend/models/sites.ts`)
- Admin-Bereich mit etwa 40 Abschnitten (siehe `menus.md`)

## Kernfakten

| Fakt | Wert | Quelle |
|------|------|--------|
| Server | Node.js >= 26, Fastify 5, TypeScript läuft direkt ohne Build-Schritt | `backend/package.json`, `backend/CLAUDE.md` |
| Datenbank | PostgreSQL (pg-Pool, Drizzle ORM) | `backend/core/db.ts` (laut `backend/CLAUDE.md`), `backend/package.json` |
| Frontend | Vue 3, Vite, Pinia, Vue Router, Tailwind 4 | `frontend/package.json` |
| Editoren | Monaco (Markdown, AsciiDoc), ProseMirror (Visual), Excalidraw | `frontend/package.json` |
| Zusammenarbeit | Yjs über Websocket, Bindungen für Monaco und ProseMirror | `frontend/package.json` (`yjs`, `y-monaco`, `y-prosemirror`), `backend/controllers/collab.ts` |
| Authentifizierung | lokal, LDAP, OIDC, SAML, GitHub, Google, Discord, Entra | `backend/modules/authentication/` |
| Speicher | db (immer aktiv), Festplatte, git, S3-kompatibel, Azure, GCS, SFTP | `.claude/rules/storage.md` |
| Lizenz | GNU Affero General Public License v3 (Dateikopf geprüft; Volltext nicht verglichen) | https://github.com/requarks/wiki/blob/3.1.1/LICENSE |
| Installation | Docker, Kubernetes, Bare Metal, Cloud-Images | https://js.wiki/ (Installationslinks) |

## Was in 3.x gegenüber 2.x neu ist

- Datenbankgestützter Speicher mit optionalen Synchronisationszielen. In 2.x ist das Wiki die Datenbank; 3.x fügt denselben Baum auf Festplatte oder in git hinzu.
- REST und eine OpenAPI-Seite, nicht GraphQL. Siehe `api.md`.
- MCP-Server und persönliche Zugriffstoken mit Bereichen.
- Mehrere Standorte, Freigaben, Feedback-Boards, Live-Notizen, Seiten-Lebenszyklus.
- Vue 3 und Vite statt Vue 2 und Vuetify.

Quellen für die Hinweise zu 3.0: https://github.com/requarks/wiki/releases/tag/3.0.1 (erste stabile 3.0-Version, listet Änderungen seit 3.0.0-beta.705).

## Was sich in 3.1.x geändert hat

- **3.1.0** (2026-11-05): neue Funktion zum Import aus HedgeDoc; OIDC-Endpunkte dürfen einfaches http verwenden (standardmäßig aus); mehrere Importkorrekturen aus 2.x; Sicherheitskorrekturen für Navigationslinks, HTML-Bereinigung, URL-Attribute von Blöcken, SVG-Prüfung und Sichtbarkeit unveröffentlichter Seiten im Baum, bei Rückverweisen und Tag-Zählern. Quelle: https://github.com/requarks/wiki/releases/tag/3.1.0
- **3.1.1** (2026-11-06): nur Fehler- und Sicherheitskorrekturen (hängende 2.x-Importe, ungültige Satzzeichen in Importpfaden, Ordnerduplikation, Ordnerrechte für alle Unterelemente). Quelle: https://github.com/requarks/wiki/releases/tag/3.1.1

## Für wen es passt (aus der eigenen Positionierung des Projekts)

Die Seite sagt, das Produkt „skaliere von einem Wochenend-Nebenprojekt bis zu tausenden Mitwirkenden“. Quelle: https://js.wiki/ . Der Quellbaum zeigt die oben genannten Funktionen; die Formulierungen zur Eignung in den alten Seiten sind nicht verifiziert und entfernt (siehe `../changelog.md`).
