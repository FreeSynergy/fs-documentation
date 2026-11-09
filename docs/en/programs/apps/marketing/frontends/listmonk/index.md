# Listmonk

> Category: [marketing](../../index.md) · Type: newsletter and mailing-list manager · Vendor: Listmonk project · Licence: AGPL-3.0

## What it is
Listmonk is a self-hosted manager for one-way mailing lists and newsletters. It ships as a standalone binary with PostgreSQL as its only dependency. Backend in Go, frontend in Vue.

## Notable ideas
- **Segmentation by query on subscribers** — lists are cut with a query rather than fixed groups (ADR 0013).
- **Single binary, single database** — small to operate.
- **Messengers** — delivery channels beyond e-mail are pluggable.
- **Transactional e-mail** through the same API.

## Documented versions
| Version | Documented on | Status |
|---------|---------------|--------|
| [latest](latest/description.md) | 2026-11-10 | ⚠️ |

## Protocols and standards used
SMTP (assumed ⚠️, not read); OIDC for sign-in. See [data standards](../../../../data/standards.md).

## Sources
| Source | Kind | Retrieved |
|--------|------|-----------|
| https://listmonk.app/docs/ | official docs ✅ (navigation and overview only) | 2026-11-10 |
