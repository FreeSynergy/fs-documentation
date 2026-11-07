# Notion — API (version 2026-03-11)

Current API version: `2026-03-11` [S1, S8]. Every REST request must send `Notion-Version` [S1].

## Base and headers [S6]

- Base URL: `https://api.notion.com` (HTTPS only).
- `Authorization: Bearer <token>`.
- `Notion-Version: 2026-03-11`.
- `Content-Type: application/json` for JSON bodies. File uploads use multipart form data [S6].

```bash
curl https://api.notion.com/v1/pages/<page_id> \
  -H "Authorization: Bearer $TOKEN" \
  -H "Notion-Version: 2026-03-11"
```

## Authentication [S3]

| Type | Who | How it is issued | Notes |
|------|-----|------------------|-------|
| Internal integration token | Single workspace | Developer portal, Configuration tab; owner only | Each page must be shared with the connection before access [S3] |
| Personal access token (PAT) | A user acting as themselves | Developer portal | Same Bearer header. Expiry can be chosen from 7 days to 1 year (changelog Jul 2) [S8] |
| Public integration (OAuth 2.0) | Any workspace that authorises it | Authorisation flow below | Access token plus refresh token |

### OAuth 2.0 flow [S3]

1. Redirect the user to `https://api.notion.com/v1/oauth/authorize` with `client_id`, `redirect_uri`, `response_type=code`, `owner=user`, optional `state`.
2. The user picks pages. Notion redirects to `redirect_uri` with `code`, or with `error` on cancel.
3. Exchange the code: `POST https://api.notion.com/v1/oauth/token` with HTTP Basic auth (`client_id:client_secret`), body `grant_type=authorization_code`, `code`, and `redirect_uri` where required.
4. The response contains `access_token`, `refresh_token`, `bot_id`, `workspace_id`, `owner` and more.
5. Refresh: same endpoint with `grant_type=refresh_token` and `refresh_token`. Each refresh returns a new access token and a new refresh token. Store both every time [S3].

Token lifetime for OAuth access tokens is not stated in the pages read: unverified.

## Endpoints

Paths as written in the official reference. Only paths with a source are listed. Others are marked unverified.

### Pages

| Method and path | Purpose | Source |
|-----------------|---------|--------|
| `POST /v1/pages` | Create a page. Parent: `page_id`, `database_id`, `data_source_id` or `workspace: true`. Max 100 blocks in `children` | [S20] |
| `GET /v1/pages/{page_id}` | Retrieve page properties. Content is not included; read children of the page block instead | [S19] |
| `PATCH /v1/pages/{page_id}` | Update page; `in_trash: true` trashes, `in_trash: false` restores | [S21] |
| `GET /v1/pages` (list all) | Not found in the reference. Unverified; use search | (404 on reference) |
| `DELETE /v1/pages/{id}` | Not documented as a delete. Trash via PATCH | [S21] |

### Blocks

| Method and path | Purpose | Source |
|-----------------|---------|--------|
| `PATCH /v1/blocks/{block_id}/children` | Append children. Default: end. `position`: `{"type":"start"}` or `{"type":"after_block","after_block":{"id":...}}`. Max 100 per request. The old `after` parameter is deprecated | [S18] |
| `GET /v1/blocks/{block_id}/children` | Read children (used to read page content) | [S19] (referenced there; path not fetched) |
| `PATCH /v1/blocks/{block_id}`, `DELETE /v1/blocks/{block_id}` | Update or remove a block | unverified (not fetched) |

### Databases and data sources

| Method and path | Purpose | Source |
|-----------------|---------|--------|
| `POST /v1/databases` | Create a database with `initial_data_source` | [S7] |
| `GET /v1/databases/{database_id}` | Retrieve database; returns the list of child `data_sources` with `id` and `name` | [S7] |
| `PATCH /v1/databases/{database_id}` | Database-level fields: `parent`, `title`, `is_inline`, `icon`, `cover`, `in_trash` | [S7] |
| `GET /v1/data_sources/{data_source_id}` | Read a data source schema | [S7] |
| `PATCH /v1/data_sources/{data_source_id}` | Change schema (`properties`), `title`, `in_trash` | [S7] |
| `POST /v1/data_sources/{data_source_id}/query` | Query rows: `filter`, `sorts`, `start_cursor`, `page_size`; `filter_properties` is a query parameter. Note: the upgrade guide summary says PATCH; the reference says POST | [S17], [S7] |

Database IDs and data source IDs are not interchangeable [S7]. Since `2025-09-03` the old `POST /v1/databases/{id}/query` no longer applies [S7].

### Search

| Method and path | Purpose | Source |
|-----------------|---------|--------|
| `POST /v1/search` | Search pages and data sources. Body: `query`, `filter`, `sort`, `start_cursor`, `page_size` | [S10] |

- `filter`: `{"property":"object","value":"page"|"data_source"}`, optionally with `in_trash`. `"database"` is not a valid value [S10, S7].
- `sort`: `{"timestamp":"last_edited_time","direction":"ascending"|"descending"}` or `{"property":"relevance"}` [S10].
- Unknown body keys are rejected [S10].
- Results use `next_cursor` and `has_more` [S10].

### Users, comments, Markdown

| Item | Status | Source |
|------|--------|--------|
| List users, retrieve user | exist; need user capability other than "No user information" | [S16] |
| Bot user of token | exists (comment-only connections allowed) | [S16], [S8] (Oct 15) |
| Comments (create, update, delete) | exist; path not verified | [S16], [S8] (Apr 17) |
| Markdown content endpoints | exist (Feb 26, Mar 2, Jun 29 changelog). Paths not verified | [S8] |

Integration capabilities (set in the connection settings): read, update and insert content; read, insert comments; user information level [S16].

## Pagination [S6, S10, S8]

- Lists return `next_cursor` and `has_more`. Pass `next_cursor` as `start_cursor` in the next request [S6, S10].
- Cursor values are opaque (changelog Apr 22) [S8].
- Pagination limit of 10,000 results, reported in `request_status` (changelog Apr 20) [S8].
- Maximum `page_size` is not stated in the pages read: unverified.

## Rate limits [S2, S8]

| Limit | Value |
|-------|-------|
| Per connection, most plans | 180 requests per minute (average 3 per second) |
| Per connection, Business and Enterprise | 600 requests per minute (average 10 per second) |
| Data source queries | about 3 requests per second per connection, counted separately |
| Workspace-wide | a shared limit also applies; throttling can occur below the connection limit |

- Rate-limited response: HTTP 429, error code `rate_limited`.
- Overload: HTTP 529 with `service_overload`. Retry like 429.
- `Retry-After`: integer seconds. Also in the body as `additional_data.retry_after` (changelog Sep 24) [S8].
- Per-connection window is 60 seconds (changelog Sep 9) [S8].
- Do not retry 429 with `public_api_request_blocked` [S2].

Payload limits: 100 block elements per array; 1000 blocks and 500 KB per request; 2000 characters for rich text content and URLs; validation errors return HTTP 400 `validation_error` [S2].

## Versioning [S1, S8]

- A new `Notion-Version` is released only for breaking changes. Additive changes apply to all versions [S1].
- `2022-06-28` and earlier are not supported by SDK v5.0.0 and later [S1].
- The next version will make Notion-flavoured Markdown the default on the Markdown endpoints (changelog Oct 30). Name and date not given [S8].

## SDK

- JavaScript: `@notionhq/client`, v5 adds `notion.dataSources.*` methods [S7]. The webhook signature helper is in v5.23.0 (changelog Jul 8) [S8].
- Python, Go and other clients: not verified on official pages.

## Removed from the earlier page

- `Notion-Version: 2022-06-28` (outdated). See [changelog.md](../changelog.md).
- `GET /v1/pages` (list), `DELETE /v1/pages/:id`, `POST /v1/databases/:id/query`, `POST /v1/webhooks`, rate limit "3 per second / 1 per second for queries", `@notion/client`, `notion-client` (Python), community SDK list.
