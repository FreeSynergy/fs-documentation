# Wiki.js 3.1.1: API

Die alte Seite beschrieb eine REST-API unter `/api/v1/…` und eine GraphQL-API unter `/graphql`. Beides gibt es in 3.1.1 nicht. Die API von 3.1.1 ist REST unter `/_api`, beschrieben durch eine OpenAPI-Seite. Quellen: https://github.com/requarks/wiki/blob/3.1.1/backend/index.ts (Zeile `routePrefix: '/_api'`, `prefix: '/_api'`), https://github.com/requarks/wiki/blob/3.1.1/backend/api/index.ts, https://docs.js.wiki/dev/api

## Oberflächen

| Oberfläche | Pfad | Protokoll | Quelle |
|---------|------|--------|--------|
| REST-API | `/_api/…` | HTTP JSON (Fastify 5) | `backend/api/index.ts` |
| OpenAPI / Swagger UI | `/_api` (UI); Spezifikations-URL auf einer laufenden Instanz nicht verifiziert | HTML und OpenAPI 3.1.0 | `backend/index.ts` (`fastifySwagger`, `openapi: '3.1.0'`) |
| MCP-Server | `/_mcp` | Model Context Protocol | `.claude/rules/mcp.md`, `backend/controllers/mcp.ts` |
| SCIM | `/_scim` | SCIM-Provisionierung | `backend/api/scim.ts`, `backend/index.ts` |
| Metriken | konfigurierbarer Pfad | HTTP | `backend/models/metrics.ts` |
| Live-Bearbeitung | `/_collab/…` Websocket | Yjs über Websocket | `backend/controllers/collab.ts`, `backend/index.ts` (`_collab` in den reservierten Präfixen) |
| GraphQL | keine | keine in 3.1.1 | keine `graphql`-Datei oder Abhängigkeit im Baum bei Tag 3.1.1 |

Die offizielle Dokumentation beschreibt die REST-API unter `/_api` als „OpenAPI 3.0 compliant“ (https://docs.js.wiki/dev/api). Der Servercode deklariert OpenAPI 3.1.0. Verwende den Servercode als Referenz.

## Authentifizierung

Drei Arten von Zugangsdaten. Alle werden als `Authorization: Bearer <token>` gesendet, wo ein Token verwendet wird. Quellen: `backend/index.ts` (Bearer-`onRequest`-Hook), `.claude/rules/personal-access-tokens.md`, https://docs.js.wiki/dev/api.

| Zugangsdaten | Erstellt von | Handelt als | Erreicht | Quelle |
|------------|-----------|-----------|--------|--------|
| Sitzungscookie | Anmeldung in der Oberfläche | der angemeldete Nutzer | alles, was die Oberfläche nutzt | `frontend/CLAUDE.md` („authentication is the session cookie“) |
| System-API-Schlüssel (JWT, mit einem Server-Schlüsselpaar signiert) | Admin, auf der Seite Admin → API; der Admin muss zuerst den API-Zugriff aktivieren | die Gruppen des Schlüssels; kein Nutzer | `/_api`, `/_scim`, `/_mcp`, Metriken | Dokumentation https://docs.js.wiki/dev/api ; `backend/models/apiKeys.ts` |
| Persönliches Zugriffstoken | Nutzer, auf Profil → Zugriffstoken (`/_profile/tokens`) | der Inhaber, mit den Gruppen und Rechten des Inhabers bei jeder Anfrage; auf Bereiche eingeschränkt | `/_api` (Routen mit einem Bereich) und `/_mcp` | `.claude/rules/personal-access-tokens.md`, `backend/api/personalTokens.ts` |

Hinweise:
- Der Schlüssel wird nur einmal bei der Erstellung angezeigt (Dokumentation).
- Ein Schlüssel oder Token kann widerrufen werden. Die Zeile eines Tokens wird beim Widerruf gelöscht; das Audit-Protokoll behält einen Eintrag.
- Der Server prüft ein Token bei jeder Anfrage. Ein Token, dessen Inhaber Administrator ist, kann trotzdem keine Admin-Routen nutzen, weil Admin-Routen keinen Bereich deklarieren (`.claude/rules/personal-access-tokens.md`).
- Tokens werden mit HTTP 403 abgelehnt, wenn ihnen der Bereich fehlt, und mit 401, wenn sie ungültig, widerrufen oder abgelaufen sind (`backend/index.ts`).
- Persönliche Tokens werden auf anderen Pfaden als `/_api` und `/_mcp` abgelehnt.

### Bereiche persönlicher Tokens

Quelle: `frontend/src/helpers/personalTokens.js` (spiegelt `backend/models/personalTokens.ts`). Jede Kategorie nimmt `:read` oder `:write` (read für GET und HEAD, write für andere Methoden, laut Regeldatei).

| Kategorie | Umfasst (aus dem Namen) |
|----------|--------------------|
| `pages` | Seiten |
| `assets` | Dateien (Assets) |
| `comments` | Kommentare |
| `glossary` | Glossar |
| `navigation` | Navigation |
| `approvals` | Freigaben |
| `profile` | das Profil des Nutzers |
| `mcp` | der MCP-Server |

Es gibt absichtlich keine Admin-Kategorie. Quelle: `.claude/rules/personal-access-tokens.md`.

## Endpunkte (Beispiele, im Quellcode verifiziert)

Alle standortbezogenen Routen nehmen `:siteId`. Die Pfade unten sind relativ zu `/_api`. Vollständige Liste: die OpenAPI-Seite unter `/_api`.

### Seiten (`backend/api/pages.ts`)

| Methode | Pfad | Zweck |
|--------|------|--------|
| GET | `/sites/:siteId/pages` | Seiten auflisten |
| GET | `/sites/:siteId/pages/search` | Suche; query, path, locales, tags, tagsMatch, editor, publishState, creatorId, authorId, orderBy, orderByDirection, offset, limit |
| GET | `/sites/:siteId/pages/suggest` | Autovervollständigung |
| GET | `/sites/:siteId/pages/suggest-path` | Pfadvorschläge |
| GET | `/sites/:siteId/pages/:pageIdOrHash` | eine Seite lesen |
| GET | `/sites/:siteId/pages/id/:pageId` | nach ID lesen |
| GET | `/sites/:siteId/pages/alias/:alias` | nach Alias lesen |
| POST | `/sites/:siteId/pages` | Seite anlegen (Body `PageInput`: path, title, description, locale, editor, content, …) |
| PATCH | `/sites/:siteId/pages/:pageId` | Metadaten aktualisieren |
| PUT | `/sites/:siteId/pages/:pageId/editor` | Inhalt aktualisieren |
| PUT | `/sites/:siteId/pages/:pageId/path` | verschieben oder umbenennen |
| POST | `/sites/:siteId/pages/:pageId/render` | neu rendern |
| DELETE | `/sites/:siteId/pages/:pageId` | löschen (weich) |
| GET | `/sites/:siteId/pages/deleted` | gelöschte Seiten |
| POST | `/sites/:siteId/pages/:pageId/restore` | wiederherstellen |
| GET | `/sites/:siteId/pages/:pageId/history` | Versionen |
| GET | `/sites/:siteId/pages/:pageId/history/:versionId` | eine Version |
| GET | `/sites/:siteId/versions/:versionId` | Version nach ID |
| GET | `/sites/:siteId/pages/:pageId/backlinks` | Rückverweise |
| GET | `/sites/:siteId/pages/:pageId/links` | ausgehende Links |
| POST | `/sites/:siteId/pages/:pageId/unlock` | eine passwortgeschützte Seite entsperren |
| POST | `/sites/:siteId/pages/userPermissions` | wirksame Rechte für einen Pfad |

`PageInput.content` ist die Quelle im eigenen Format des Editors. Bei `redirect`-Seiten ist es ein JSON-Objekt mit `kind`, `target`, `showInterstitial`. Quelle: `backend/api/schemas/page.ts`.

### Baum (`backend/api/tree.ts`)

| Methode | Pfad |
|--------|------|
| GET | `/sites/:siteId/tree` |
| GET | `/sites/:siteId/tree/browse` (Query `path`, `locale`) |
| GET | `/sites/:siteId/tree/pages` |
| GET | `/sites/:siteId/tree/graph` (Query `locale`) |
| GET | `/sites/:siteId/tree/folders/:folderId` |
| POST | `/sites/:siteId/tree/folders` |
| PATCH | `/sites/:siteId/tree/folders/:folderId` |
| DELETE | `/sites/:siteId/tree/folders/:folderId` |

### Nutzer, Gruppen, Tokens

| Methode | Pfad | Quelle |
|--------|------|--------|
| GET | `/users/profile/tokens` | `backend/api/personalTokens.ts` |
| POST | `/users/profile/tokens` | ebenso |
| DELETE | `/users/profile/tokens/:tokenId` | ebenso |
| GET | `/users/:userId/tokens` | ebenso (Admin) |
| — | Gruppen und Nutzer | `backend/api/groups.ts`, `backend/api/users.ts` (Routen existieren; Methoden nicht gelesen) |

### Authentifizierung (`backend/api/authentication.ts`)

| Methode | Pfad | Zweck |
|--------|------|--------|
| GET | `/sites/:siteId/auth/strategies` | Strategien für die Anmeldeseite auflisten |
| POST | `/sites/:siteId/auth/logout` | abmelden |
| POST | `/sites/:siteId/auth/verifyEmail` | E-Mail bestätigen (Body `token`) |
| POST | `/sites/:siteId/auth/resetPassword` | Passwort zurücksetzen |
| POST | `/sites/:siteId/auth/passkey/challenge` | Passkey-Anmeldung starten |
| PUT | `/sites/:siteId/auth/passkey/login` | Passkey-Anmeldung abschließen |
| GET | `/auth/:strategyId/metadata` | Metadaten der Strategie |
| GET/PUT | `/authentication/config` | Admin |
| GET | `/authentication/modules` | Admin |
| — | `/authentication/strategies`, `/authentication/strategies/:strategyId` | Admin; Methoden nicht geprüft |

Die Passwort-Anmeldung wurde im grep nicht als einzelne Route gefunden. Nicht verifiziert: der genaue Pfad für Anmeldung mit Nutzername und Passwort. Die alten Pfade `/api/v1/auth/login`, `/refresh` und `/api/v1/meta` existieren in 3.1.1 nicht (geprüft durch Auflisten von `backend/api/*.ts`).

### System

| Methode | Pfad | Quelle |
|--------|------|--------|
| GET | `/system/mcp` | `backend/api/mcp.ts` |
| GET | `/system/mcp/status` | ebenso |
| PUT | `/system/mcp` | ebenso (Admin-Einstellungen) |
| GET | `/sites/:siteId/mcp` | ebenso |
| PUT | `/sites/:siteId/mcp` (Body `guidelinesPath`) | ebenso |

## Beispiel (verifizierte Form, nicht ausgeführt)

Eine Seite mit einem persönlichen Token lesen (Token-Wert und Standort-ID sind Platzhalter):

```
GET https://<wiki-host>/_api/sites/<siteId>/pages/<pageId>
Authorization: Bearer <personal-token>
```

Die Route deklariert `scope: 'pages'`; ein GET benötigt den Bereich `pages:read`. Die Anfrage wurde nicht ausgeführt; der Pfad stammt aus `backend/api/pages.ts`.

## Webhooks (ausgehend)

Admin → Webhooks (`routes.js`: `webhooks`). Quelle: `backend/models/hooks.ts`.

| Eigenschaft | Wert | Quelle |
|----------|------|--------|
| Methode | POST | `hooks.ts` (`method: 'POST'`) |
| Content-Type | `application/json` | `hooks.ts` |
| User-Agent | `Wiki.js/<version>` | `hooks.ts` |
| Authorization | optionaler fester Headerwert, am Webhook gesetzt (`authHeader`) | `hooks.ts` |
| Body | `{ hookId, event, data, instance }` | `hooks.ts` |
| Signatur | keine gefunden (kein HMAC-Header im Code) | `hooks.ts` |
| Wiederholungen | nicht geprüft | — |

Ereignisse stehen in `events.md`.

## Ratenlimits

Im Quellcode von 3.1.1 wurde kein allgemeines Limit pro Token oder pro Route gefunden. Der einzige gefundene Limiter mit festem Zeitfenster gilt für Anmeldeversuche (`backend/models/rateLimits.ts`, Schlüssel wie `auth:<ip>`). Siehe `limits.md`.

## Git-Synchronisation (Speicher, keine API)

Git ist ein Speicherziel, keine API. Pro Standort unter Admin → Speicher konfiguriert. Quelle: `backend/modules/storage/git/definition.yml`, `.claude/rules/storage.md`.

| Einstellung | Werte | Bedeutung |
|---------|-------|---------|
| `repoUrl` | `git@host:org/repo.git` (SSH) oder `https://host/org/repo.git` (Basic) | Remote; leer bedeutet ein rein lokales Repo |
| `authType` | `ssh` (Standard), `basic` | |
| `sshPrivateKeyMode` | `inline` (Standard), `path` | |
| `branch` | Standard `main` | der erste Push legt den Branch auf einem leeren Remote an |
| `syncMode` | `sync` (zuerst ziehen, dann pushen), `push` (Commits des Wikis per Force-Push schreiben; das Wiki gewinnt), `pull` (nur Änderungen übernehmen; das Remote gewinnt) | |

Jede Änderung wird committet. Ein rein lokales Repository liegt auf der Festplatte einer Instanz und braucht einen persistenten Datenträger und genau eine Instanz (Hinweis in `definition.yml`).

## SDKs

Die alte Seite nannte `wiki.js-api-client` (npm), `pywikijs` (PyPI) und ein „offizielles Node.js SDK“. Keines davon wurde im offiziellen Repository oder in der Dokumentation gefunden. Nicht verifiziert; wird als nicht existent behandelt.

## Nicht verifiziert

- Die OpenAPI-JSON-URL auf einer laufenden Instanz.
- Paginierungsformat für Listen-Endpunkte (`limit`/`offset` bei der Suche; andere nicht gelesen).
- Format des Fehler-Bodys (der Code verwendet `reply.unauthorized(message)`, `reply.forbidden(message)`; Fastify-Fehlerhülle wird angenommen).
