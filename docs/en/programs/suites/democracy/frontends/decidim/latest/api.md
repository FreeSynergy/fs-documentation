# Decidim - API Documentation

## Overview

Decidim is built on **GraphQL** (`/graphql`, public with introspection; write mutations only with a session or token). A webhook module pushes events outwards. Earlier REST plans no longer exist as a standard.

**Overview of API types**

| Type | Use | Status |
|-----|------------|--------|
| GraphQL `/graphql` | Queries (processes, proposals, comments, meetings) + mutations (session) | official (core API) |
| Webhooks module (`decidim-webhooks`) | Proposal created or commented… → POST | official (module) |
| REST | — | ❌ (not core) |
| Action Text exports | JSON/CSV evaluations, admin | official |

## Authentication

- Reading: none (public content; private processes excluded)
- Mutations: sessions/cookies; API tokens depend on version (check the docs)

## GraphQL examples

Query (proposals of a process):

```graphql
query {
  component(id: 42, type: "Decidim::Proposals::ProposalComponent") {
    ... on Decidim::Proposals::ProposalConnection {
      nodes { title body supportsCount createdAt }
    }
  }
}
```

Webhook payload (module):

```json
{ "event": "proposal_created", "resource": {
    "id": 1234, "title": "More bike lanes", "component_id": 42 } }
```

## Core types (selection)

| Type | Description |
|-----|--------------|
| `ParticipatorySpace`/`Process` | Participation container |
| `Component` (Proposals, Budgets, Meetings…) | Module instance |
| `Proposal`, `Comment`, `Meeting` | Core objects |
| `User` (public fields only) | Participants |

## Rate limits

Not built in (instance or proxy limits apply).

## Skin note

GraphQL is an ideal feed for participation dashboards (read-only skin); a webhook → n8n chain can drive notification skins ([models.md](../../../../../../data/models.md): proposal → support → phase).
