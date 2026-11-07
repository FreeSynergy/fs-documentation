# CiviCRM - API Documentation

## Overview

CiviCRM has two equally current APIs: **APIv3** (classic, entity-action) and **APIv4** (modern, nested queries). Both can be used as REST calls via the same endpoint; in addition there is the PHP programming interface.

**API types at a glance**

| Type | Usage | Status |
|-----|------------|--------|
| REST APIv3 `civicrm/ajax/api?entity=…&action=…` | Legacy CRUD | official |
| REST APIv4 `civicrm/api4` (JSON POST) | modern queries, SearchKit logic | official |
| PHP `civicrm_api4()` | Hooks/extensions | official |
| Webhooks | — | ❌ only via extension (e.g. "Webhooks" ext) |

## Authentication

- **site_key + auth_key** (from `civicrm.settings.php`): signature API `civicrm/php/rest` for server-side scripts (HMAC), or
- **Session**: logged-in Civi user in the browser (AJAX)
- APIv4 REST `civicrm/api4` requires CMS login with `Access CiviCRM`

## APIv3 (example)

```http
GET /civicrm/ajax/api?json={"entity":"Contact","action":"get","sequential":1,"return":["display_name","email"],"email":{"LIKE":"%example.org"}}&key=SITE_KEY&key=AUTH_KEY HTTP/1.1
```

Response:

```json
{"values":[{"id":12,"display_name":"Berg, Andrea","email":"a@example.org"}]}
```

## APIv4 (recommended)

```http
POST /civicrm/api4?entity=Contact&action=get HTTP/1.1
Content-Type: application/json
X-Civi-Auth: Bearer <token>   (or session)

{
  "select": ["id", "display_name", "email.email"],
  "where": [["email.is_primary", "=", true]],
  "limit": 50
}
```

Create:

```json
{
  "values": {
    "contact_type": "Individual",
    "first_name": "Andrea",
    "last_name": "Berg",
    "email": [{ "email": "a@example.org", "is_primary": true }]
  }
}
```

Important entities: `Contact`, `Email`, `Phone`, `Group`, `Contribution`, `Event`, `EventParticipant`, `Membership`, `Activity`, `Relationship`, `CustomValue`, `Mailing`.

## Batch and sequences

`civicrm/api4` accepts `chain`/`Batch` for dependencies ("Create Contact, then Email from last created").

## Rate limits

Not built in; observe CMS/web server limits and mailing scheduling.

## SDKs and client libraries

- **Official**: PHP (core), JS (`crm.api4`), **CiviCRM API wrapper** for Bash (WP-CLI-like `cv` tool)
- **cv** (CLI): `cv api4 Contact.get +w 'email.is_primary=1'` — reference for automation
- Community: Python `civicrm-api` packages (APIv3), Zapier connector

## Skin note

Constituent model (Contact + Contribution/Event/Membership as relationships) → mapping to [models.md](../../../../../../data/models.md).
