# Notion — events (webhooks, 2026-11-07)

Source: [S4] webhooks setup, [S5] events and delivery.

## Setup

- Webhooks are created in the integration's connection settings, in the **Webhooks** tab, with **+ Create a subscription** [S4]. There is no `POST /v1/webhooks` endpoint on the pages read. The earlier page was wrong [changelog.md].
- The webhook URL must be HTTPS and publicly reachable. `localhost` does not work [S4].
- After creation, Notion POSTs a one-time JSON body with `verification_token` to the URL [S4].
- The subscription is activated in the Webhooks tab: Verify, paste the token, Verify subscription. Resend token is available [S4].
- The URL can be changed only before verification. After that, delete and recreate the subscription [S4].
- Paused, unverified or deleted subscriptions receive nothing [S4].

## Signature [S4]

- Header `X-Notion-Signature` with value `sha256=<hex>`.
- Value is HMAC-SHA256 of the raw body, keyed with `verification_token`.
- Compare in constant time.
- JavaScript SDK v5.23.0 has `verifyWebhookSignature()` (changelog Jul 8) [S8].

## Event types [S5]

| Entity | Types |
|--------|-------|
| page | `page.content_updated`, `page.created`, `page.deleted`, `page.locked`, `page.moved`, `page.properties_updated`, `page.undeleted`, `page.unlocked` |
| database | `database.created`, `database.deleted`, `database.moved`, `database.undeleted`; `database.content_updated` and `database.schema_updated` are deprecated for 2025-09-03 |
| data_source | `data_source.content_updated`, `data_source.created`, `data_source.deleted`, `data_source.moved`, `data_source.schema_updated`, `data_source.undeleted` |
| comment | `comment.created`, `comment.deleted`, `comment.updated` |

Note: [S4] mentions `page.content_updated` as aggregated and `comment.created` as needing the comment-read capability [S4, S16]. No `file_upload` or `view` event exists in the pages read.

## Payload [S5]

| Field | Meaning |
|-------|---------|
| `id` | event UUID |
| `timestamp` | ISO 8601 time of the event |
| `workspace_id` | workspace UUID |
| `subscription_id` | subscription id |
| `integration_id` | connection id |
| `type` | event type |
| `authors` | array of `{id, type}`; type `person`, `bot` or `agent` |
| `accessible_by` | users and bots with access (public connections only) |
| `attempt_number` | 1–8 |
| `entity` | `{id, type}`; type `page`, `block`, `database`, `data_source`, others in samples |
| `data` | event-specific details |

Payloads carry metadata, not the full content. The consumer fetches the current state through the API [S5].

## Delivery [S5]

- Aim: at-most-once delivery. Events should arrive within 5 minutes.
- Failed deliveries are retried up to 8 times with exponential backoff; the last retry about 24 hours after the event.
- Events can arrive out of order. Use `timestamp`.
- Some events are aggregated and batched (for example `page.content_updated`), so they arrive later.
- Payloads may not reflect the current state. Fetch fresh data.

## Use for our frontend

- Treat webhooks as hints to refetch, not as a change stream with content.
- Keep the signature check.
- Expect duplicates or gaps in the at-most-once case: reconcile by polling or search.
