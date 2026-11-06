# Wekan - Features

## Main features

### Kanban core
- boards with **swimlanes** (trough levels, e.g. per team/month), lists, cards, labels, checklists, due dates
- card custom fields, template boards, import from Trello/CSV, JSON export

### Collaboration
- organisations and teams, observer/member/admin roles
- activity feed, comments, attachments (local/S3), real-time sync (Meteor DDP)

### Integrations
- **invoke webhooks** (incoming: POST → create/comment a card) — ideal for alerts
- **outgoing webhooks** per board (card moved, comment …) → HTTP
- e-mail notifications (SMTP), ICal feed for due dates

## What Wekan does NOT do

- **no SaaS quality** like Trello (mobile apps experimental, push rudimentary)
- **no automation engine** (Butler rules: ❌ — webhooks only)
- **no reports/throughput charts** (activity only)
- **no stable official API versioning** (the API is used stably, but thinly documented)
- custom fields without permission logic

## Extensions and integrations

| Integration | Way |
|-------------|-----|
| REST API (personal token) | documented + community |
| invoke/outgoing webhooks | board panel |
| LDAP/OAuth2/SAML | admin panel |
| storage | local filesystem/S3 |
