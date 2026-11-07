# Arcemall - API Documentation

## Overview

Arcemall provides API access for marketplace objects (listings, bookings, users) plus webhooks for status changes. **The published detail scope is narrow**; this page does not invent endpoint names, but marks integration patterns.

**API types at a glance**

| Type | Use | Status |
|-----|------------|--------|
| REST API (marketplace objects) | read/write listings/bookings | official (detailed reference in the vendor portal) |
| API keys in operator cockpit | authentication | official |
| Webhooks | booking/payment events → callback | official |
| GraphQL/webhook signature special cases | — | verify current status |

## Pattern (schema-open)

```
GET  /…/listings?geo=lat,lng&r=5000        → listing list (geo filter)
POST /…/bookings  { listing, slot }        → booking request
Webhook: booking.created / booking.confirmed → n8n/FreeSynergy event
```

(Field names according to the API documentation of the version in use.)

## Example flow (FreeSynergy)

```
FreeSynergy DB (listings) → API import script → Arcemall listings
Arcemall booking → webhook → FreeSynergy appointment/message skin
```

## Rate Limits

Set by the vendor; not publicly standardized. To be negotiated.

## Skin note

Arcemall skin = **adapter pattern** (import + webhook reader), as with all platform skins; connect geo filtering to [standpunkte.md](../../../../../apps/maps/standpunkte.md).
