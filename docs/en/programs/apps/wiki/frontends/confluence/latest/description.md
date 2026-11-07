# Confluence (Cloud, latest) · Description

Sources: see [index.md](../index.md) (S-numbers below refer to its table).

## What it is

A team wiki hosted by Atlassian. Users create pages in spaces, collaborate through comments and version history, and find content through search and a sidebar. [S14][S15]

## Content model (verified)

| Type | Evidence |
|------|----------|
| Page | Create menu and `page` API group [S14][S3] |
| Live doc | Create shortcut and Forge event `avi:confluence:created` family for live docs [S12][S10] |
| Blog post | Create shortcut; blog events [S12][S10] |
| Database | Create menu; `database` events [S14][S10] |
| Whiteboard | Create menu; `whiteboard` events [S14][S10] |
| Folder | `folder` events and `Folder` API group [S10][S1] |
| Custom content | `custom_content` events [S10] |
| Comment | Comment events and Comment API group [S10][S1] |

Spaces contain these items. A space has an overview, pages, live docs, blogs and whiteboards in its sidebar. [S14]

## Differences between Cloud and Data Center

| Topic | Cloud | Data Center |
|-------|-------|-------------|
| Hosting | Atlassian hosts the instance [S14] | Self-managed (the product line in S20) |
| Lifecycle | Updated continuously; no numbered version in the docs read | End of life 2029-03-28 [S20] |
| API base | `/wiki/api/v2`, `/wiki/rest/api` [S1][S2] | Not checked (unverified) |
| Webhooks | Forge events; Connect webhooks (legacy) [S10][S11] | Separate admin webhook feature; not read in full (unverified) |
| Databases, Kanban | Database objects exist in Cloud [S10] | The old file claimed Data Center only; Cloud has databases too. Kanban view: unverified |

## Strengths (verified only)

- Cloud has two REST API generations and a GraphQL API. [S1][S2][S8]
- Live change events exist for most content types (Forge). [S10]
- Export to Word and PDF from the page menu, and PDF/HTML/XML/CSV from space settings. [S16]
- Per-user light and dark theme. [S17]

## Claims dropped from the earlier draft

The following claims could not be verified against official sources and are removed: "enterprise-ready", "audit logs", "mobile app strength", Java and PostgreSQL back end, React and Velocity front end, and all comparisons with Notion, XWiki and Wiki.js. See [changelog.md](../changelog.md).

## Who it suits

Not a product statement in the official sources read. Left out.
