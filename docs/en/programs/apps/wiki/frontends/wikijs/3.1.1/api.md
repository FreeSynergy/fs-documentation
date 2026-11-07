# Wiki.js 3.1.1 — API

The old page described a REST API at `/api/v1/…` and a GraphQL API at `/graphql`. Neither exists in 3.1.1. The 3.1.1 API is REST under `/_api`, described by an OpenAPI page. Sources: https://github.com/requarks/wiki/blob/3.1.1/backend/index.ts (line `routePrefix: '/_api'`, `prefix: '/_api'`), https://github.com/requarks/wiki/blob/3.1.1/backend/api/index.ts, https://docs.js.wiki/dev/api

## Surfaces

| Surface | Path | Protocol | Source |
|---------|------|----------|--------|
| REST API | `/_api/…` | HTTP JSON (Fastify 5) | `backend/api/index.ts` |
| OpenAPI / Swagger UI | `/_api` (UI); spec URL not verified on a running instance | HTML and OpenAPI 3.1.0 | `backend/index.ts` (`fastifySwagger`, `openapi: '3.1.0'`) |
| MCP server | `/_mcp` | Model Context Protocol | `.claude/rules/mcp.md`, `backend/controllers/mcp.ts` |
| SCIM | `/_scim` | SCIM provisioning | `backend/api/scim.ts`, `backend/index.ts` |
| Metrics | configurable path | HTTP | `backend/models/metrics.ts` |
| Live editing | `/_collab/…` websocket | Yjs over websocket | `backend/controllers/collab.ts`, `backend/index.ts` (`_collab` in the reserved prefixes) |
| GraphQL | none | none in 3.1.1 | no `graphql` file or dependency in the tree at tag 3.1.1 |

Official docs describe the REST API at `/_api` as "OpenAPI 3.0 compliant" (https://docs.js.wiki/dev/api). The server code declares OpenAPI 3.1.0. Use the server code as the reference.

## Authentication

Three credential types. All are sent as `Authorization: Bearer <token>` where a token is used. Sources: `backend/index.ts` (bearer `onRequest` hook), `.claude/rules/personal-access-tokens.md`, https://docs.js.wiki/dev/api.

| Credential | Created by | Acts as | Reaches | Source |
|------------|-----------|---------|---------|--------|
| Session cookie | login in the UI | the logged-in user | everything the UI uses | `frontend/CLAUDE.md` ("authentication is the session cookie") |
| System API key (JWT, signed by a server keypair) | admin, on the Admin → API page; the admin must first enable API access | the key's groups; no user | `/_api`, `/_scim`, `/_mcp`, metrics | docs https://docs.js.wiki/dev/api ; `backend/models/apiKeys.ts` |
| Personal access token | user, on Profile → Access Tokens (`/_profile/tokens`) | the owner, with the owner's groups and permissions on each request; narrowed to scopes | `/_api` (routes with a scope) and `/_mcp` | `.claude/rules/personal-access-tokens.md`, `backend/api/personalTokens.ts` |

Notes:
- The key is shown once at creation (docs).
- A key or token can be revoked. A token's row is deleted on revoke; the audit log keeps a record.
- The server checks a token on every request. A token whose owner is an administrator still cannot use admin routes, because admin routes declare no scope (`.claude/rules/personal-access-tokens.md`).
- Tokens are refused with HTTP 403 when they lack the scope, and with 401 when they are invalid, revoked or expired (`backend/index.ts`).
- Personal tokens are refused on any path other than `/_api` and `/_mcp`.

### Personal token scopes

Source: `frontend/src/helpers/personalTokens.js` (mirrors `backend/models/personalTokens.ts`). Each category takes `:read` or `:write` (read for GET and HEAD, write for other methods, per the rule file).

| Category | Covers (from name) |
|----------|--------------------|
| `pages` | pages |
| `assets` | assets |
| `comments` | comments |
| `glossary` | glossary |
| `navigation` | navigation |
| `approvals` | approvals |
| `profile` | the user's profile |
| `mcp` | the MCP server |

There is no admin category by design. Source: `.claude/rules/personal-access-tokens.md`.

## Endpoints (examples verified in source)

All site-scoped routes take `:siteId`. Paths below are relative to `/_api`. Full list: the OpenAPI page at `/_api`.

### Pages (`backend/api/pages.ts`)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/sites/:siteId/pages` | list pages |
| GET | `/sites/:siteId/pages/search` | search; query, path, locales, tags, tagsMatch, editor, publishState, creatorId, authorId, orderBy, orderByDirection, offset, limit |
| GET | `/sites/:siteId/pages/suggest` | autocomplete |
| GET | `/sites/:siteId/pages/suggest-path` | path suggestions |
| GET | `/sites/:siteId/pages/:pageIdOrHash` | read a page |
| GET | `/sites/:siteId/pages/id/:pageId` | read by ID |
| GET | `/sites/:siteId/pages/alias/:alias` | read by alias |
| POST | `/sites/:siteId/pages` | create a page (body `PageInput`: path, title, description, locale, editor, content, …) |
| PATCH | `/sites/:siteId/pages/:pageId` | update metadata |
| PUT | `/sites/:siteId/pages/:pageId/editor` | update content |
| PUT | `/sites/:siteId/pages/:pageId/path` | move or rename |
| POST | `/sites/:siteId/pages/:pageId/render` | re-render |
| DELETE | `/sites/:siteId/pages/:pageId` | delete (soft) |
| GET | `/sites/:siteId/pages/deleted` | deleted pages |
| POST | `/sites/:siteId/pages/:pageId/restore` | restore |
| GET | `/sites/:siteId/pages/:pageId/history` | versions |
| GET | `/sites/:siteId/pages/:pageId/history/:versionId` | one version |
| GET | `/sites/:siteId/versions/:versionId` | version by ID |
| GET | `/sites/:siteId/pages/:pageId/backlinks` | backlinks |
| GET | `/sites/:siteId/pages/:pageId/links` | outgoing links |
| POST | `/sites/:siteId/pages/:pageId/unlock` | unlock a password-protected page |
| POST | `/sites/:siteId/pages/userPermissions` | effective permissions for a path |

`PageInput.content` is the source in the editor's own format. For `redirect` pages it is a JSON object with `kind`, `target`, `showInterstitial`. Source: `backend/api/schemas/page.ts`.

### Tree (`backend/api/tree.ts`)

| Method | Path |
|--------|------|
| GET | `/sites/:siteId/tree` |
| GET | `/sites/:siteId/tree/browse` (query `path`, `locale`) |
| GET | `/sites/:siteId/tree/pages` |
| GET | `/sites/:siteId/tree/graph` (query `locale`) |
| GET | `/sites/:siteId/tree/folders/:folderId` |
| POST | `/sites/:siteId/tree/folders` |
| PATCH | `/sites/:siteId/tree/folders/:folderId` |
| DELETE | `/sites/:siteId/tree/folders/:folderId` |

### Users, groups, tokens

| Method | Path | Source |
|--------|------|--------|
| GET | `/users/profile/tokens` | `backend/api/personalTokens.ts` |
| POST | `/users/profile/tokens` | same |
| DELETE | `/users/profile/tokens/:tokenId` | same |
| GET | `/users/:userId/tokens` | same (admin) |
| — | groups and users | `backend/api/groups.ts`, `backend/api/users.ts` (routes exist; methods not read) |

### Authentication (`backend/api/authentication.ts`)

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/sites/:siteId/auth/strategies` | list strategies for the login page |
| POST | `/sites/:siteId/auth/logout` | log out |
| POST | `/sites/:siteId/auth/verifyEmail` | verify email (body `token`) |
| POST | `/sites/:siteId/auth/resetPassword` | reset password |
| POST | `/sites/:siteId/auth/passkey/challenge` | start a passkey login |
| PUT | `/sites/:siteId/auth/passkey/login` | finish a passkey login |
| GET | `/auth/:strategyId/metadata` | strategy metadata |
| GET/PUT | `/authentication/config` | admin |
| GET | `/authentication/modules` | admin |
| — | `/authentication/strategies`, `/authentication/strategies/:strategyId` | admin; methods not checked |

Password login was not located as a single route in the grep. Unverified: the exact path for username and password login. The old page's `/api/v1/auth/login`, `/refresh` and `/api/v1/meta` do not exist in 3.1.1 (checked by listing `backend/api/*.ts`).

### System

| Method | Path | Source |
|--------|------|--------|
| GET | `/system/mcp` | `backend/api/mcp.ts` |
| GET | `/system/mcp/status` | same |
| PUT | `/system/mcp` | same (admin settings) |
| GET | `/sites/:siteId/mcp` | same |
| PUT | `/sites/:siteId/mcp` (body `guidelinesPath`) | same |

## Example (verified form, not run)

Read a page with a personal token (token value and site ID are placeholders):

```
GET https://<wiki-host>/_api/sites/<siteId>/pages/<pageId>
Authorization: Bearer <personal-token>
```

The route declares `scope: 'pages'`; a GET needs the `pages:read` scope. The request was not executed; the path was taken from `backend/api/pages.ts`.

## Webhooks (outgoing)

Admin → Webhooks (`routes.js`: `webhooks`). Source: `backend/models/hooks.ts`.

| Property | Value | Source |
|----------|-------|--------|
| Method | POST | `hooks.ts` (`method: 'POST'`) |
| Content type | `application/json` | `hooks.ts` |
| User-Agent | `Wiki.js/<version>` | `hooks.ts` |
| Authorization | optional fixed header value set on the webhook (`authHeader`) | `hooks.ts` |
| Body | `{ hookId, event, data, instance }` | `hooks.ts` |
| Signature | none found (no HMAC header in code) | `hooks.ts` |
| Retries | not checked | — |

Events are listed in `events.md`.

## Rate limits

No general per-token or per-route rate limit was found in the 3.1.1 source. The only fixed-window limiter found is for authentication attempts (`backend/models/rateLimits.ts`, keys like `auth:<ip>`). See `limits.md`.

## Git sync (storage, not API)

Git is a storage target, not an API. Configured per site under Admin → Storage. Source: `backend/modules/storage/git/definition.yml`, `.claude/rules/storage.md`.

| Setting | Values | Meaning |
|---------|--------|---------|
| `repoUrl` | `git@host:org/repo.git` (SSH) or `https://host/org/repo.git` (basic) | remote; empty means a local-only repo |
| `authType` | `ssh` (default), `basic` | |
| `sshPrivateKeyMode` | `inline` (default), `path` | |
| `branch` | default `main` | first push creates the branch on an empty remote |
| `syncMode` | `sync` (pull, then push), `push` (force-push the wiki's commits; wiki wins), `pull` (only take changes in; remote wins) | |

Each change is committed. A local-only repository lives on one instance's disk and needs a persistent volume and a single instance (`definition.yml` hint).

## SDKs

The old page named `wiki.js-api-client` (npm), `pywikijs` (PyPI) and an "official Node.js SDK". None of these was found in the official repository or the docs. Unverified; treated as not existing.

## Not verified

- The OpenAPI JSON URL on a running instance.
- Pagination format for list endpoints (`limit`/`offset` on search; others not read).
- Error body format (the code uses `reply.unauthorized(message)`, `reply.forbidden(message)`; Fastify's error envelope is assumed).
