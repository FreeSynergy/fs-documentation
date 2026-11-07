# Wiki.js 3.1.1 — description

Version: 3.1.1 (released 2026-11-06). Sources: https://github.com/requarks/wiki/releases/tag/3.1.1 , https://github.com/requarks/wiki/tree/3.1.1

## What it does

Wiki.js is a self-hosted wiki. A site holds a tree of pages. Each page has a path, a locale, an editor type, tags, and a version history. Pages can be published or unpublished, watched, rated, commented on, linked, and searched. Sources: https://github.com/requarks/wiki/blob/3.1.1/backend/api/schemas/page.ts , https://github.com/requarks/wiki/blob/3.1.1/backend/api/pages.ts

Beyond pages, the 3.x line contains:

- Feedback boards (ideas with categories and votes), `frontend/src/components/EditorFeedback.vue`
- Blogs (a page type with its own listing), `EditorBlog.vue`
- Glossary, `backend/models/glossary.ts`
- Approval queues for suggested edits, `backend/models/approvals.ts`
- Page ownership and lifecycle rules, `.claude/rules/page-lifecycle.md`
- Multi-site installs, one database and one set of accounts (`backend/models/sites.ts`)
- Admin area with about 40 sections (see `menus.md`)

## Key facts

| Fact | Value | Source |
|------|-------|--------|
| Server | Node.js >= 26, Fastify 5, TypeScript run directly without a build step | `backend/package.json`, `backend/CLAUDE.md` |
| Database | PostgreSQL (pg pool, Drizzle ORM) | `backend/core/db.ts` (per `backend/CLAUDE.md`), `backend/package.json` |
| Frontend | Vue 3, Vite, Pinia, Vue Router, Tailwind 4 | `frontend/package.json` |
| Editors | Monaco (Markdown, AsciiDoc), ProseMirror (Visual), Excalidraw | `frontend/package.json` |
| Collaboration | Yjs over websocket, Monaco and ProseMirror bindings | `frontend/package.json` (`yjs`, `y-monaco`, `y-prosemirror`), `backend/controllers/collab.ts` |
| Auth | Local, LDAP, OIDC, SAML, GitHub, Google, Discord, Entra | `backend/modules/authentication/` |
| Storage | db (always on), disk, git, S3-compatible, Azure, GCS, SFTP | `.claude/rules/storage.md` |
| Licence | GNU Affero General Public License v3 (file header checked; full text not compared) | https://github.com/requarks/wiki/blob/3.1.1/LICENSE |
| Install | Docker, Kubernetes, bare metal, cloud images | https://js.wiki/ (install links) |

## What is new in 3.x compared with 2.x

- Database-backed storage with optional sync targets. In 2.x the wiki is the database; 3.x adds the same tree on disk or in git.
- REST and an OpenAPI page, not GraphQL. See `api.md`.
- MCP server and personal access tokens with scopes.
- Multi-site, approvals, feedback boards, live notes, page lifecycle.
- Vue 3 and Vite instead of Vue 2 and Vuetify.

Sources for the 3.0 notes: https://github.com/requarks/wiki/releases/tag/3.0.1 (first stable 3.0 release, lists changes since 3.0.0-beta.705).

## What changed in 3.1.x

- **3.1.0** (2026-11-05): new feature to import from HedgeDoc; OIDC endpoints may use plain http (off by default); several 2.x import fixes; security fixes for navigation links, HTML sanitizing, block URL attributes, SVG scanning, and visibility of unpublished pages in the tree, backlinks and tag counts. Source: https://github.com/requarks/wiki/releases/tag/3.1.0
- **3.1.1** (2026-11-06): bug and security fixes only (2.x import stalls, invalid punctuation in import paths, folder duplication, folder permissions on all children). Source: https://github.com/requarks/wiki/releases/tag/3.1.1

## Who it suits (from the project's own positioning)

The site says the product "scales from a weekend side project to thousands of contributors." Source: https://js.wiki/ . The source tree shows the features listed above; the suitability wording in the old pages is not verified and is removed (see `../changelog.md`).
