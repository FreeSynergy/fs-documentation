# Mailchimp - API documentation

## Overview

REST v3 per data-centre subdomain (`https://<dc>.api.mailchimp.com/3.0/`, dc in the API key). Objects: lists, members, tags, segments, campaigns, journeys, reports. Webhooks for member/campaign events.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| REST v3 | CRUD + actions (`/actions/subscribe`) | official |
| OAuth2 | App access | official |
| Webhooks | list.member.*, campaign.* | official |
| Bulk operations (`/bulk-queue`) | Asynchronous mass jobs | official |
| GraphQL | — | ❌ |

## Authentication

- API key: HTTP Basic (`anystring:<api-key>`); OAuth2 for marketplace apps
- Derive the endpoint subdomain from the key suffix (`…us21`)!

## Core endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET/POST` | `/lists/{list_id}/members` | Contacts |
| `POST` | `/lists/{id}/members` (`status: "subscribed"`) | Add |
| `PUT` | `/lists/{id}/members/{subscriber_hash}` | Create/replace (MD5 email) |
| `POST` | `/lists/{id}/members/{hash}/tags` | Set tags |
| `GET` | `/lists/{id}/segments` | Segments |
| `POST` | `/campaigns` + `/actions/send` | Start a campaign |
| `GET` | `/reports` | Metrics |
| `POST` | `/lists/{id}/webhooks` | Webhook subscription |

## Example

Request:

```http
POST /3.0/lists/a1b2c3/members HTTP/1.1
Authorization: Basic b3R0ZXI6<api-key>
Content-Type: application/json

{ "email_address": "ada@example.org", "status": "subscribed",
  "tags": ["spender"], "merge_fields": { "FNAME": "Ada", "LNAME": "Byron" } }
```

Response: `200` member JSON (`id`=MD5, `subscribe_url`, stats).

## Webhooks

Events `subscribe`, `unsubscribe`, `cleaned`, `profile` — verify the HMAC signature with the API key half (documentation example).

## Rate limits

**15 requests/second per account** (reports: separately), 429 + backoff; the bulk endpoints for mass operations.

## SDKs and client libraries

- Official clients: Python (`mailchimp-marketing`), PHP, Node; a Postman collection
- `subscriber_hash` = MD5(lowercased email) — important for the upsert pattern

## Skin note

The member model (email as the primary key + tags) mirrors the contact standard in [data/fields.md](../../../../../../data/fields.md); always use the subscriber hash for sync IDs.
