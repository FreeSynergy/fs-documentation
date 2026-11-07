# LaunchBoard - API Documentation

## Overview

LaunchBoard is a commercial product with a REST-like HTTP interface and OAuth2/OIDC. **Important for factual accuracy**: the vendor does **not publish a freely accessible endpoint reference**; the authoritative documentation is in the customer portal behind sign-in. The following tables therefore clearly separate **standardised protocol endpoints** (defined by OAuth2/OIDC) from the **schema of this skin documentation**, which depicts the typical resources but must be checked in the customer portal before any integration.

**Overview of API types**

| Type | Use | Documentation status |
|-----|------------|---------------------|
| REST/JSON (resource paths) | manage boards, widgets, integrations, users | referenced only in the customer portal |
| OAuth2 / OIDC | sign-in, single sign-on, tokens for automation | standard protocol, publicly defined |
| Webhooks (outgoing) | report events to external systems | scope per plan, documented in the portal |
| GraphQL | ❌ Not available | — |

## Authentication

- **Session cookie**: after sign-in via local accounts or OIDC, the instance sets a session cookie. The web interface uses only this path.
- **OAuth2/OIDC**: the instance is configured as a client with issuer, client ID and secret. For automation, the **client credentials flow** of the identity provider is used; the instance accepts its access tokens.
- **API token (long-lived)**: in the administration area "Integrations/API", tokens are created with a name and validity. Usually passed as `Authorization: Bearer <token>`.
- **Scopes and roles**: tokens follow the rights of the assigned account. Administrator/Editor/Viewer role determines which resources are writable.
- **No anonymous access**: without token or session, the interface responds with `401`, and with `403` if rights are missing.
- **Transport**: HTTPS is mandatory (specified for the cloud variant; for the container variant, ensure it via a reverse proxy).

## Standardised OIDC endpoints

These paths are defined by the protocol; the **base URL** is composed from configuration and installation and is to be taken from the instance documentation.

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/.well-known/openid-configuration` | Metadata of the OIDC provider (token, authorize, JWKS URL) |
| `GET` | `<authorize-URL>` | Redirect to sign-in of the identity provider |
| `GET` | `<redirect-URI>` | Return to the instance with authorization code |
| `POST` | `<token-URL>` | Exchange code for token; client credentials for scripts |
| `GET` | `<userinfo-URL>` | Profile attributes of the signed-in user |
| `GET` | `<jwks-URL>` | Signing keys for token verification |

## Resource schema (not publicly referenced – check in the portal)

The following pattern corresponds to the usual form of such dashboard products and is used in this documentation as a **working schema**.

### Boards

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/v1/boards` | list accessible boards |
| `POST` | `/api/v1/boards` | create board (name, template, visibility) |
| `GET` | `/api/v1/boards/{id}` | load a single board with layout |
| `PATCH` | `/api/v1/boards/{id}` | change name, visibility, settings |
| `DELETE` | `/api/v1/boards/{id}` | delete board |
| `PUT` | `/api/v1/boards/{id}/layout` | save layout (desktop or mobile) |

### Widgets

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/v1/boards/{id}/widgets` | list tiles of a board |
| `POST` | `/api/v1/boards/{id}/widgets` | create tile (type, integration, layout) |
| `GET` | `/api/v1/widgets/{widgetId}` | read a single tile |
| `PATCH` | `/api/v1/widgets/{widgetId}` | change settings |
| `DELETE` | `/api/v1/widgets/{widgetId}` | remove tile |
| `POST` | `/api/v1/widgets/{widgetId}/duplicate` | duplicate tile |
| `GET` | `/api/v1/widget-types` | available widget types including field schema |
| `POST` | `/api/v1/widget-data/preview` | check the response of a data source in advance |

### Integrations

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/api/v1/integrations` | list connected services |
| `POST` | `/api/v1/integrations` | create service (type, URL, key) |
| `PATCH` | `/api/v1/integrations/{id}` | change access or URL |
| `DELETE` | `/api/v1/integrations/{id}` | remove connection |
| `POST` | `/api/v1/integrations/{id}/test` | test connection, receive error description |
| `POST` | `/api/v1/certificates` | store own root certificate |

### Users, roles and system

| Method | Endpoint | Description |
|---------|----------|--------------|
| `POST` | `/api/v1/users` | create user or generate invitation |
| `PATCH` | `/api/v1/users/{id}` | change role, status, profile |
| `DELETE` | `/api/v1/users/{id}` | remove user |
| `GET` | `/api/v1/groups` | groups and sharing |
| `GET` | `/api/v1/health` | status of the instance |
| `POST` | `/api/v1/backup` | trigger database export |

## Examples

### Get a token from an OIDC provider

```bash
curl -s -X POST "https://id.example.internal/realms/homelab/protocol/openid-connect/token" \
  -d "grant_type=client_credentials" \
  -d "client_id=launchboard" \
  -d "client_secret=$OIDC_SECRET"
```

Response (shortened):

```json
{
  "access_token": "eyJhbGciOiJSUzI1NiIs...",
  "expires_in": 300,
  "token_type": "Bearer"
}
```

### List boards

```bash
curl -s "https://launchboard.example.internal/api/v1/boards" \
  -H "Authorization: Bearer $LAUNCHBOARD_TOKEN"
```

Response (shortened):

```json
{
  "data": [
    { "id": "brd_01H", "name": "Homelab", "visibility": "team", "updatedAt": "2026-10-30T18:22:04Z" }
  ]
}
```

### Create a widget

```bash
curl -s -X POST "https://launchboard.example.internal/api/v1/boards/brd_01H/widgets" \
  -H "Authorization: Bearer $LAUNCHBOARD_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "type": "container-status",
    "integrationId": "int_14",
    "layout": { "x": 0, "y": 0, "w": 3, "h": 2 },
    "settings": { "showActions": true, "intervalSeconds": 30 }
  }'
```

Response:

```json
{ "data": { "id": "wdg_92", "type": "container-status", "boardId": "brd_01H" } }
```

## Rate limits

- **No publicly documented figures.** Quotas depend on the plan and on whether the cloud or container variant is used.
- Observed practice of such services: limited requests per minute and token, response `429` with a note on the waiting time.
- Recommended client strategy: request serialisation, exponential backoff on `429`/`5xx`, caching of immutable resources (widget types, integrations).
- Widget intervals in the interface are the real lever: short intervals produce most of the traffic.
- For the container variant, additionally set limits at the reverse proxy (`limit_req` in nginx, `ratelimit` middleware in Traefik).

## Webhooks

- **Outgoing webhooks are intended**; the exact event catalogue is in the customer portal. Typical scope:

| Event | Trigger |
|----------|-----------|
| `board.created` / `board.updated` / `board.deleted` | board changes |
| `widget.created` / `widget.updated` / `widget.deleted` | tile changes |
| `integration.failed` / `integration.recovered` | connection status of an integration |
| `auth.login` / `auth.logout` | sign-in events |

- **Security**: verify signatures, process idempotently, retry failed deliveries with backoff (retry attempts per provider).
- **Alternative**: interval polling of `/api/v1/health` and integration status if no webhooks are included in the plan.

## SDKs and client libraries

- **No public SDK.** HTTP clients are used (`curl`, `fetch`, `requests`, `httpx`).
- **OpenAPI file**: whether and in which version it is offered in the customer portal is **not publicly documented**; if available, it is suitable for code generation.
- **OIDC side**: for the sign-in flow, standard OIDC libraries of any language can be used (Keycloak, Authentik and Entra ID clients work unchanged).
- **Script tip**: a dedicated account with reader rights for queries, a separate account with editor rights for changes – clearer and auditable.

## Operational notes

- **Observe licence status**: if a subscription expires, the instance restricts write access; automations may then no longer run.
- **Keep secrets stable**: back up session and encryption secrets of the container variant, otherwise stored service keys can no longer be read.
- **Issue tokens with minimum rights** and rotate them regularly.
- **Version binding**: resource paths may change between major versions; couple automations to the version from `/api/v1/version` and check changes.

## See also

- [description.md](description.md)
- [features.md](features.md)
- [menu.md](menus.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
- [../homarr/api.md](../../homarr/latest/api.md) - Comparison: openly documented tRPC interface
