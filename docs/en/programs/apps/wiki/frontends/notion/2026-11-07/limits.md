# Notion — known limits (2026-11-07)

Only limits with a source. Numbers from plans other than those named are not given.

## API

| Limit | Value | Source |
|-------|-------|--------|
| Requests per connection | 180 per minute (most plans); 600 per minute (Business, Enterprise) | [S2] |
| Data source queries | about 3 per second per connection | [S2] |
| Workspace-wide shared limit | exists; value not given | [S2] |
| Block children per request | 100 | [S18, S20] |
| Blocks per request | 1000 | [S2] |
| Payload per request | 500 KB | [S2] |
| Rich text content, URL | 2000 characters each | [S2] |
| Equation expression | 1000 characters | [S2] |
| Multi-select options per request | 100 | [S2] |
| Relation or people per request | 100 | [S2] |
| Results pagination | 10,000 results (changelog Apr 20) | [S8] |
| Oversized page edits | HTTP 400 (changelog Oct 2, was 500) | [S8] |
| Free workspace block limits apply to API | yes (changelog Sep 1); numbers not given | [S8] |
| Version support | `2022-06-28` and earlier not supported by SDK v5 and later | [S1] |

## Data model

| Limit | Source |
|-------|--------|
| A new page cannot be created with `block_id` as parent | [S20] |
| Search covers only pages and data sources; not all content types | [S10] |
| Page retrieve does not return block content | [S19] |
| Integration sees only pages shared with it (internal integrations) | [S3] |
| Views: lock prevents property and view changes, not data changes | [S13] |

## Deletion and history

| Item | Value | Source |
|------|-------|--------|
| Trash retention | 30 days, then permanent delete | [S14] |
| After permanent delete | kept 30 more days, then gone for everyone (Enterprise owners may customise) | [S14] |
| Restore | from Trash; a trashed page cannot be edited until restored | [S14] |
| Restore database | brings back pages and properties, not the text in them | [S14] |
| Version history | 7 days (Free), 30 (Plus), 90 (Business), any length (Enterprise) | [S14] |

## Platform

| Item | Source |
|------|--------|
| Small text and full width: desktop and web only | [S15] |
| Page discussion settings on mobile are in "Customize page" | [S15] |
| Webhooks need HTTPS and a public URL | [S4] |

## Unverified

- Mobile feature parity and mobile limits.
- Block count limit on free plans (numbers not published on pages read).
- Maximum `page_size` for list endpoints.
