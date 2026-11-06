# Mural - API documentation

## Overview

Mural has **no broadly opened public content API**: export/import happens via PNG/PDF and workspace administration, automation primarily through Zapier/apps. For skins the rule is: Mural is a reference for UI patterns, not for API mapping.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST (api.mural.co) | Workspace/user administration (SSO operation), individual endpoints | restricted/partially public |
| SCIM/SAML | Provisioning/SSO | official (Enterprise) |
| Content CRUD (notes/shapes) | — | ❌ not public |
| Webhooks | — | ❌ not documented |

## Authentication

- Operations endpoints: an API token per workspace (admin) respectively an OAuth app for partner integrations; the detailed reference is in Mural's customer support (not fully published publicly — deliberately not invented here)

## Exchange routes (practical)

1. Export the mural (PNG/PDF) → further processing
2. Activity log (CSV, Enterprise) → analysis
3. Zapier connector (create mural, membership) → automation skins

## Rate limits

Not publicly documented.

## Frontend note

For API-driven whiteboard skins it is better to take **Miro** or **tldraw** as the model; Mural provides the moderation/sequence patterns ([components/procedures](../../../../../../components/index.md))).
