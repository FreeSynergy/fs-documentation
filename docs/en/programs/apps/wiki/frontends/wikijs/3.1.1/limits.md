# Wiki.js 3.1.1 — limits

Known limits of the product, from the 3.1.1 source and official docs. Items marked "unverified" were not confirmed.

## Rate limits

| Scope | Limit | Source |
|-------|-------|--------|
| Authentication attempts | fixed window per key (e.g. `auth:<ip>`), with a ban when exceeded; numbers set in policy objects | `backend/models/rateLimits.ts` |
| General API (`/_api`) | none found in the source | search of `backend/api`, `backend/controllers`, `backend/helpers` for rate-limit code: no match outside `rateLimits.ts` |
| Per API key or token | none found | same |
| Response headers `X-RateLimit-*` | not found in source | same search |

The old page claimed "100 requests per minute per token" with `X-RateLimit-*` headers. Those claims are not in 3.1.1 and are listed in `../changelog.md`.

The authentication limiter's numbers (max attempts, window, ban length) were not extracted. Look at the policy values in `backend/models/rateLimits.ts` and `backend/models/authentication.ts` if needed.

## Size and payload

| Limit | Value | Source |
|-------|-------|--------|
| WebSocket payload (collaboration and websocket routes) | 5 MiB (`maxPayload: 5242880`) | `backend/index.ts` (`fastifyWebsocket`) |
| Upload size | a `maxUploadSize` setting in admin security; 3.1.1 changed how that admin field is stored (release note "drop maxUploadSize number prop") | `backend/index.ts`, https://github.com/requarks/wiki/releases/tag/3.1.1 |
| Other request body limits | not read | — |

## Database and runtime

| Limit | Value | Source |
|-------|-------|--------|
| Database | PostgreSQL only in the source (pg driver, Drizzle `node-postgres`) | `backend/core/db.ts`, `backend/package.json` |
| Node.js | >= 26 | `backend/package.json` (`engines`) |
| Worker database pool | one connection per worker thread; transactions in workers must not wait on other queries | `backend/CLAUDE.md` |
| Scheduler | postgres-backed job queue, poolifier thread pool | `backend/CLAUDE.md` |
| Several instances | startup checks run under an advisory lock so that instances booting together agree; file storage must be shared or git-synced | `backend/CLAUDE.md`, storage rule |

The old page's claim "Database: PostgreSQL, MySQL, SQLite" is wrong for 3.1.1 (only PostgreSQL in the source). Source: `backend/core/db.ts`.

## Storage

| Limit | Source |
|-------|--------|
| The database is always a storage target (`db`) and cannot be turned off | `.claude/rules/storage.md` |
| `disk` and `git` targets need a persistent volume or a shared repo for more than one instance | `backend/modules/storage/git/definition.yml` (local repo hint), storage rule |
| Git: force-push in `push` mode overwrites the remote | `backend/modules/storage/git/definition.yml` (`syncMode` hint) |
| SFTP: one connection per target, serialised | `.claude/rules/storage.md` |
| Object stores: keys are paths; no folders | `.claude/rules/storage.md` |

## Editors

| Limit | Source |
|-------|--------|
| Redirect pages have no body and are never searchable | `backend/api/schemas/page.ts` |
| Converting between editors rewrites the source and compares renders before saving | `PageActionsCol.vue` (comment on `convertPage`) |

## Search

| Limit | Source |
|-------|--------|
| Search requires at least 2 characters in the header search | locale `common.header.searchHint` ("Type at least 2 characters") |
| Filters and ordering are the ones in the search endpoint (see `api.md`) | `backend/api/pages.ts` |
| Result count and fuzzy matching rules: not read | — |

## Accounts and access

| Limit | Source |
|-------|--------|
| Personal tokens cannot reach admin routes | `.claude/rules/personal-access-tokens.md` |
| Personal tokens only on `/_api` and `/_mcp` | `backend/index.ts` |
| System API keys act for their groups and are not a user, so cannot do actions that need a user | https://docs.js.wiki/dev/api |
| Token scopes are per category (no admin category) | `frontend/src/helpers/personalTokens.js` |
| Two-factor, passkeys: available per account | `backend/models/passkeys.ts`, profile routes |

## Security fixes in 3.1.x (signals of past weaknesses)

These are in the release notes. They show classes of issues the product has had, and our frontend should test against them.

| Release | Issue class | Source |
|---------|-------------|--------|
| 3.1.0 | invalid link targets in navigation items | release notes (GHSA-35r7-33j8-ghwg) |
| 3.1.0 | client-side HTML rendering not sanitised with the server sanitiser | release notes (GHSA-3c74-j8g3-p255) |
| 3.1.0 | block URL attributes; CSP on `/_files`; SVG scan on rename and adopt | release notes (GHSA-m4c7-x7x7-3ppw) |
| 3.1.0 | unpublished pages visible through tree, backlinks and tag counts | release notes (GHSA-jf48-pw92-vgrx) |
| 3.1.1 | folder actions did not check permissions on all children | release notes (GHSA-p5rv-hmh3-wrv8, GHSA-7mf7-wprw-7fjm) |

Source: https://github.com/requarks/wiki/releases/tag/3.1.0 and https://github.com/requarks/wiki/releases/tag/3.1.1

## Not verified

- Maximum page size, maximum tag count, maximum folder depth.
- Behaviour of the pending-asset upload queue on network loss.
- Accessibility conformance level. Not stated in the source or docs read. Unverified.
