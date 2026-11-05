# Freshdesk - Features

## Main features

### Tickets
- Email ingest per mailbox, portal forms, converter script (rules on arrival)
- Status open/pending/resolved/closed, priorities, products, groups, tags, custom fields
- Saved filters + favourites; bulk actions

### Automation
- **Dispatch'r** (rules), **workflows** (triggers + if-then + scheduling), **escalation**, **assignment rules** (round-robin)
- SLA engine with business hours, due-by colours
- Freddy AI: self-service bot, ticket summary, reply suggestions, sentiment (plan-dependent)

### Self-service
- Knowledge base with categories, multilingual portals, community forum
- Surveys (CSAT) after resolution

### Omnichannel
- Email, telephony (Freshcaller integration), chat (Freshchat), social/messenger (observe plan limits)

## What Freshdesk does NOT do

- **no self-hosting**; the data lives in the Freshworks cloud (data regions selectable, limited)
- **no deep process modelling** (no ITIL changes/CIs — GLPI)
- **the API does not cover everything**: some automations/custom actions only on the UI side
- **custom fields limited** in number/types per plan
- **billing per agent and feature**: light agents only read tickets; chat/telephone cost extra

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| Marketplace | hundreds of apps, serverless functions (Freshworks developer platform) |
| Webhooks + API | REST v2, event subscriptions |
| SSO | SAML, OIDC (newer plans) |
