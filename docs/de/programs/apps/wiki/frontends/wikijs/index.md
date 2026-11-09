# Wiki.js

> Kategorie: [wiki](../../index.md)

## Was es ist

Wiki.js ist eine Open-Source-Wiki-Engine zum Selbsthosten. Das Projekt beschreibt sich selbst als "The open source wiki engine. Built and maintained in the open since 2017." Quelle: https://js.wiki/

Die aktuelle Linie ist 3.x. Der Server basiert auf Node.js (Fastify), die Oberfläche auf Vue 3, und Inhalte werden in PostgreSQL gespeichert; der Seiteninhalt wird optional auf Speicherziele gespiegelt (Festplatte, Git, S3-kompatibel, Azure, GCS, SFTP). Quellen: https://github.com/requarks/wiki/blob/3.1.1/backend/CLAUDE.md , https://github.com/requarks/wiki/blob/3.1.1/frontend/CLAUDE.md , https://github.com/requarks/wiki/blob/3.1.1/backend/package.json

## Versionsangaben

| Angabe | Wert | Quelle |
|------|------|----------|
| Hier dokumentierte Version | **3.1.1** (neueste 3.x-Version) | https://github.com/requarks/wiki/releases/tag/3.1.1 |
| Veröffentlichungsdatum | 2026-11-06 (GitHub `published_at`) | `gh api repos/requarks/wiki/releases/tags/3.1.1` |
| Auf GitHub als "Latest" markiert | ja | https://github.com/requarks/wiki/releases |
| Außerdem veröffentlicht | 3.1.0 (2026-11-05), 3.0.2, 3.0.1 (erste stabile 3.0), 3.0.0-beta.* | https://github.com/requarks/wiki/releases |
| Gibt es 3.1? | **ja**: Tags 3.1.0 und 3.1.1 sind veröffentlicht, keine Vorabversionen | ebenso |
| Neueste 2.x | v2.5.315 (2026-09-21) | https://github.com/requarks/wiki/releases/tag/v2.5.315 |

Der Eigentümer hat nach 3.1 gefragt. Sowohl 3.1.0 als auch 3.1.1 existieren; 3.1.1 wird dokumentiert, weil es das neueste ist und gegenüber 3.1.0 nur Fehler- und Sicherheitskorrekturen enthält (siehe `3.1.1/description.md`).

## Bemerkenswerte Ideen

Hier sind nur Ideen aufgeführt, die im Quellcode von 3.1.1 verifiziert sind.

1. **Ein Wiki, viele Speicherziele.** Inhalte liegen in der Datenbank. Eine Site kann denselben Seitenbaum zusätzlich auf der Festplatte, in einem Git-Repository (Commit pro Änderung, Sync mit einem Remote) oder in Objektspeicher ablegen. Quelle: https://github.com/requarks/wiki/blob/3.1.1/.claude/rules/storage.md
2. **Acht Editoren pro Site.** Markdown (Monaco), Visuell (ProseMirror), AsciiDoc, Excalidraw-Zeichnung, Blog, Feedback-Board, Weiterleitung. Jeder lässt sich ein- oder ausschalten. Live-Notizen sind ein eigener Seitentyp unter `/n/`. Quellen: https://github.com/requarks/wiki/blob/3.1.1/backend/models/sites.ts , https://docs.js.wiki/guide/editors
3. **Gemeinsames Bearbeiten in Echtzeit.** Der Markdown- und der visuelle Editor teilen sich ein Yjs-Dokument über einen Websocket. Quellen: https://github.com/requarks/wiki/blob/3.1.1/frontend/src/editor/visual/collab.js , https://github.com/requarks/wiki/blob/3.1.1/backend/controllers/collab.ts
4. **Persönliche Zugriffstokens pro Benutzer mit Scopes**, getrennt von System-API-Keys. Ein persönliches Token handelt als sein Eigentümer und ist auf die deklarierten Scopes beschränkt. Quelle: https://github.com/requarks/wiki/blob/3.1.1/.claude/rules/personal-access-tokens.md
5. **MCP-Server** unter `/_mcp`, damit KI-Assistenten mit einem persönlichen Token im Wiki suchen und lesen können. Quelle: https://github.com/requarks/wiki/blob/3.1.1/.claude/rules/mcp.md
6. **Darstellungseinstellungen pro Site in der Datenbank** (Farben, Schriften, Inhaltsbreite, Seite der Seitenleiste, eingefügtes CSS/HTML), nicht als Theme-Datei. Quelle: https://github.com/requarks/wiki/blob/3.1.1/backend/models/sites.ts

## Wichtige Unterschiede zu 2.x

| Thema | 2.5.x | 3.1.1 | Quelle |
|-------|-------|-------|--------|
| Frontend | Vue 2, Vuetify 2, Apollo | Vue 3, Vite, Pinia, Tailwind 4 | https://github.com/requarks/wiki/blob/3.1.1/frontend/package.json |
| API | GraphQL (`server/graph/schemas/*.graphql`) | REST unter `/_api` (Fastify), OpenAPI-Seite unter `/_api`; kein GraphQL im Baum | https://github.com/requarks/wiki/tree/v2.5.315/server/graph/schemas , https://github.com/requarks/wiki/blob/3.1.1/backend/index.ts |
| Auth-Module | viele (auth0, okta, keycloak, …) | local, ldap, oidc, saml, github, google, discord, entra | `backend/modules/authentication/` bei jedem Tag |
| Node.js | >= 20 | >= 26 | package.json `engines` bei jedem Tag |

## Dokumentierte Versionen

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Vorhandene Pflichtdateien |
|---------|------------------------|
| [3.1.1](3.1.1/description.md) | 7/7 |
| [latest](latest/description.md) | 6/7 |

### 3.1.1

| Datei | Inhalt |
|------|----------|
| [description.md](3.1.1/description.md) | Ausführliche Beschreibung, Abgrenzung, für wen es geeignet ist |
| [features.md](3.1.1/features.md) | Was das Programm kann — und was nicht |
| [layout.md](3.1.1/layout.md) | Fensterstruktur, Bereiche, Panels |
| [menus.md](3.1.1/menus.md) | Menüstruktur, Kontextmenüs, Menüs nach Rolle |
| [shortcuts.md](3.1.1/shortcuts.md) | Tastenkürzel |
| [api.md](3.1.1/api.md) | APIs und Protokolle, Authentifizierung, Rate Limits |
| [themes/index.md](3.1.1/themes/index.md) | Themes: Farben, Typografie, Abstände — was sich nachbauen lässt |
| [events.md](3.1.1/events.md) | Ereignisse nach außen (Webhooks, Push, Streams) |
| [limits.md](3.1.1/limits.md) | Bekannte Grenzen |
| [dependencies.md](3.1.1/dependencies.md) | Welche unserer Bausteine ein Frontend in diesem Stil braucht |

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

- Offizielle Website: https://js.wiki/
- Offizielle Dokumentation (Seitenstruktur geprüft; nicht Seite für Seite gelesen): https://docs.js.wiki/
- Versionsliste: https://github.com/requarks/wiki/releases
- Quellcode bei Tag 3.1.1: https://github.com/requarks/wiki/tree/3.1.1
- Quellcode bei Tag v2.5.315: https://github.com/requarks/wiki/tree/v2.5.315

Weitere Dateien in diesem Satz: `3.1.1/` (Analyse pro Version) und `corrections.md` (was die alten Seiten falsch darstellten).
