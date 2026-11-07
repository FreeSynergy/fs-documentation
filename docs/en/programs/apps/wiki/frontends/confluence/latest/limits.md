# Confluence (Cloud, latest) · Limits

Sources: S-numbers refer to [index.md](../index.md). Only verified items are listed as facts. Items not researched are marked "not researched".

## API

| Limit | Value | Source |
|-------|-------|--------|
| REST quota | 65,000 points per hour (global pool, default); per-tenant pool after review | [S5] |
| REST burst | Separate per-second limits; extra on Permissions, Search, Admin | [S5] |
| GraphQL | 10,000 points per currency per minute per user | [S8] |
| Rate-limit response | HTTP 429, whole request denied | [S5][S8] |
| Retry | Use `Retry-After`; retry idempotent requests only | [S5] |
| Pagination | v2 cursor; v1 offset | [S1][S2] |
| Publishing approval | REST page update returns HTTP 409 in spaces that require approval (announced 2026-09-28; rollout date not announced) | [S9] |
| v1 restrictions | v1 content-restriction update now requires read access (2026-10-15 change) | [S9] |

## Export

| Limit | Source |
|-------|--------|
| Only published content is exported | [S16] |
| Word export opens only in Microsoft Word | [S16] |
| PDF space export excludes comments; blogs excluded from PDF and HTML space export; Team Calendars excluded from all space exports | [S16] |
| Organisation admins can block exports per product or classification level | [S16] |
| Large exports: "exporting 100 pages" should finish in a few minutes; split large jobs | [S16] |
| Word export image cap (earlier draft: 50 images) | Unverified; only a community post mentions it |

## Platform

| Item | Status |
|------|--------|
| Max page size, attachment size, number of spaces, number of versions kept | Not researched |
| Connect apps can no longer be published on the Marketplace | [S11] |
| Connect new features | Forge only [S11] |
| GraphQL beta fields can change without notice | [S8] |

## Data Center

| Item | Source |
|------|--------|
| End of life 2029-03-28 (read-only licences); new subscriptions end 2028-03-30 for existing customers | [S20] |
