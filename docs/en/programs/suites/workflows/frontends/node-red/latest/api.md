# Node-RED - API Documentation

## Overview

Node-RED provides two API surfaces: (1) self-defined HTTP endpoints via **HTTP-In nodes** (the actual integration API), (2) the internal **admin REST API** (manage flows), plus file exchange via `flows.json` and `node-red-admin`.

**API types at a glance**

| Type | Use | Status |
|-----|------------|--------|
| HTTP-In/Out (`http://host:1880/<path>`) | Own REST/webhook endpoints | official (user design) |
| Admin REST `/<adminRoot>/flows` | Read/write flow JSON | official-internal |
| MQTT/WebSocket | Message buses | official |
| Webhooks (outbound) | via function/HTTP request nodes | DIY |
| GraphQL | — | ❌ |

## Authentication

- HTTP endpoints: self-built (e.g. `httpNodeAuth` Basic auth, token check in the function node)
- Admin API: `adminAuth` in `settings.js` (login cookie/Basic), `read/write` levels

## Admin endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| `GET` | `/flows` | Complete flow JSON |
| `POST` | `/flows` | Replace flows (deploy) |
| `POST` | `/flow` | Single flow tab |
| `GET` | `/nodes` | Running nodes + status |
| `POST` | `/nodes/<id>/inject` | Trigger inject node |
| `POST` | `/settings` | Read Node-RED version/settings |

## Example: webhook endpoint (HTTP-In)

HTTP-In node `POST /hooks/ticket`:

```json
// incoming
{ "ticket": { "id": 9982, "state": "closed" } }
```

Function node:

```js
if (msg.payload.ticket?.state === "closed") {
  node.warn("Ticket " + msg.payload.ticket.id + " geschlossen");
  return msg; // → HTTP-Response
}
return null;
```

## flows.json as exchange format

Import/export via the header menu or `node-red-admin import`; credentials export is separate and encrypted.

## Rate limits

Per instance (Node.js process); HTTP limits via reverse proxy.

## SDKs and client libraries

- `node-red-admin` (CLI), `flows` JSON schema in the documentation
- REST test tools: any HTTP client

## Skin note

Node + wire model = [flow model](../../../../../../data/models.md): nodes with ports, msg payload as the standard message format.
