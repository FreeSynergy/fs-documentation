# Confluence (Cloud, latest) · API

Sources: S-numbers refer to [index.md](../index.md). "Unverified" = not confirmed in an official source read on 2026-11-07. Do not implement from unverified items without checking the live OpenAPI document (S4).

## Base URLs [S1][S2][S4]

| API | Base path on a site | Source |
|-----|---------------------|--------|
| REST v2 | `https://<site>.atlassian.net/wiki/api/v2` | [S4] server variable `https://{your-domain}/wiki/api/v2`; [S1] example `/wiki/api/v2/pages?limit=5` |
| REST v1 | `https://<site>.atlassian.net/wiki/rest/api` | [S2] example `/wiki/rest/api/content/{id}?expand=...` |
| OAuth 2.0 gateway | `https://api.atlassian.com/ex/confluence/{cloudid}/{api}` | [S6] |
| GraphQL (OAuth) | `https://api.atlassian.com/graphql` | [S8] |
| GraphQL (session or API token) | `https://{subdomain}.atlassian.net/gateway/api/graphql` | [S8] |

The earlier draft used `https://confluence.example.com/rest/api`. That path is missing the `/wiki` prefix and is not a Cloud path. [changelog.md](../changelog.md)

## Pagination [S1][S2]

- v2: `limit` and `cursor`. The next URL is in the `Link` header (`rel="next"`) and in `_links.next`. Both are absent on the last page. [S1]
- v1: `start` (zero-based offset) and `limit`. [S2]

## Authentication [S6][S7]

### Basic auth (scripts and manual calls)

- Credentials: an Atlassian account email and an API token. The token is the password value. [S7]
- Header: `Authorization: Basic <base64(email:api_token)>`. The encoding must be real Base64; the earlier draft had the literal text `base64(...)`. [S7]
- Atlassian says basic auth is "not as secure as other methods" and recommends OAuth for other uses. [S7]
- Where to create the API token: unverified (S7 does not say).
- Scoped API tokens: unverified.

### OAuth 2.0 (3LO) for apps [S6]

| Step | Value |
|------|-------|
| Authorize | `GET https://auth.atlassian.com/authorize` with `audience=api.atlassian.com`, `client_id`, `scope` (space separated), `redirect_uri`, `state`, `response_type=code`, `prompt=consent` |
| Token | `POST https://auth.atlassian.com/oauth/token` with JSON `grant_type`, `client_id`, `client_secret`, `code`, `redirect_uri` |
| Refresh | `POST https://auth.atlassian.com/oauth/token` with `grant_type=refresh_token`, `client_id`, `client_secret`, `refresh_token` |
| Refresh token | Add `offline_access` to `scope`. Rotating: every refresh returns a new refresh token and disables the used one. Inactivity expiry 90 days. Reuse leeway 10 minutes. |
| Failed refresh | `403` with `invalid_grant`: the user must restart authorisation. |
| Resources | `GET https://api.atlassian.com/oauth/token/accessible-resources` with bearer token. Returns `id` (= cloudid), `name`, `url`, `scopes`. |

Note: S6 gives the accessible-resources host as `auth.atlassian.com` in one place and `api.atlassian.com` in the examples. Check before relying on either.

Scope strings seen in S6: `write:confluence-content`, `read:confluence-content.all`, `manage:confluence-configuration`. Full scope list for Confluence REST: unverified (the scopes page read, S22, lists Connect scopes only).

### Connect and Forge apps

JWT or OAuth 2.0 for Cloud apps. [S1]

### Cookie auth

Earlier draft listed cookie auth. Not verified. Removed.

## Endpoints: v2 Page group [S3]

| Method | Path |
|--------|------|
| GET | `/pages` |
| POST | `/pages` |
| GET | `/pages/{id}` |
| PUT | `/pages/{id}` |
| DEL | `/pages/{id}` |
| PUT | `/pages/{id}/title` |
| GET | `/spaces/{id}/pages` |
| GET | `/labels/{id}/pages` |

The v2 group list also includes: Attachment, Blog Post, Children, Comment, Content Permissions, Custom Content, Database, Descendants, Folder, Label, Like, Space, Space Permissions, Task, User, Version, Whiteboard. [S1]

Page body representation enum (v2 write): `storage`, `atlas_doc_format`, `wiki`. The body object is `value` plus a representation key. [S4]

Unverified: v2 request body field names (`spaceId`, `status`, `title`, `parentId`), whether `version.number` must be incremented on PUT, and the message field. The OpenAPI JSON (S4) was read in three chunks; the schemas `PageCreateRequest` and `PageUpdateRequest` were not reached.

## Endpoints: v1 (legacy)

Verified: `GET /wiki/rest/api/content/{id}?expand=...` [S2].
Unverified: the v1 endpoint list in the earlier draft (`/child/page`, `/history`, `/child/attachment`, `/child/macro`, `/user/view`, `/child/comment/{id}` with PUT, `/rest/api/search` CQL usage). Treat as unverified.

Changelog note: a v1 content-restriction behaviour change is dated 2026-10-15 and the v2 content-permission endpoints were added 2026-10-14. [S9]

## Search

Search endpoint and query syntax (CQL or v2 equivalent): unverified in the pages read. The earlier draft's `GET /rest/api/search?cql=...` example is not confirmed.

## GraphQL [S8]

- One version that keeps evolving. Beta fields can change without notice and need the `X-ExperimentalApi` header.
- Rate limit: 10,000 points per currency per minute per user. Over the limit: HTTP 429 with `RETRY-AFTER`. The status applies to the whole request.
- Some fields need OAuth 3LO; the exact scopes are in the field descriptions in the explorer.
- Do not retry 500-range errors (S8).

## Rate limits (REST) [S5]

Points-based, not a request count.

| Item | Value |
|------|-------|
| Base cost | 1 point per request |
| Core objects (pages, spaces, attachments) | +1 |
| Identity and access (users, groups, permissions) | +2 |
| Writes (POST, PUT, PATCH, DELETE) | base cost only |
| Global pool (default, Tier 1) | 65,000 points per hour, shared across tenants |
| Per-tenant pool (Tier 2, after Atlassian review) | Free 65,000/h; Standard 100,000 + 10 × users; Premium 130,000 + 20 × users; Enterprise 150,000 + 30 × users; capped at 500,000/h |
| Reset | Top of each UTC hour; no carry-over |
| Burst limits | Separate, over seconds; Permissions, Search and Admin endpoints have extra burst protection |
| Over quota | HTTP 429, all requests denied until reset ("no partial throttling") |
| Retry | `Retry-After` in seconds; retry only idempotent requests, with exponential backoff and jitter |

Headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` (ISO 8601), `X-RateLimit-NearLimit` (true below 20%), `RateLimit-Reason`, `Retry-After`. Beta headers `Beta-RateLimit-Policy`, `Beta-RateLimit` and `X-Beta-RateLimit-*` are informational until enforcement; at enforcement the `Beta-` prefix is dropped. [S5]

Policy names: `global-app-quota`, `tenant-app-quota`. [S5]

Inconsistency in S5: the reason table lists `conf-global-based`; the sample 429 shows `confluence-quota-global-based`. Use what the live response returns.

The earlier draft claimed "200 requests per 5 minutes" and "100 requests per second" and `X-AUTH-_RATE-LIMIT-*` headers. These are not in S5. Removed.

## Webhooks and events

See [events.md](events.md).

## SDKs

Unverified. The earlier list (`@atlassian/confluence-api`, `atlassian-python-api`, `atlassian-java-client`, `go-confluence`, `atlassian-php-sdk`) is not confirmed by any official page read. Removed.

## Data Center API

Not checked. Do not assume Cloud paths apply.
