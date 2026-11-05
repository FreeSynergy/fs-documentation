# Zammad - Features

## Main features

### Channels and ticket creation
- Email (IMAP/POP/JMAP, outgoing SMTP), web form, Telegram, WhatsApp (cloud), telephone/CTI, online chat
- Tickets/follow-ups arising from article replies, ticket splitting and merge
- Import from Zendesk, Freshdesk, OTRS, RT (assistants)

### Agent work
- Three-column mask: customer context, article stream, attributes
- Text blocks with variables, bulk actions (state, owner, tags, priority)
- Full-text search (Elasticsearch/OpenSearch), saved filters, "overdue" views
- Tasks with follow-up dates, calendars/service times for SLA

### Automation
- Triggers (event-driven actions), schedulers (time-driven), escalations
- Webhooks (outbound, signed), inbound via API
- Barometer/sentiment optional, knowledge base with workflow approvals

### Portal and self-service
- Customer portal with own tickets, knowledge base articles, forms
- Single sign-on: LDAP, OAuth2/OIDC, SAML, CAS, Microsoft

## What Zammad does NOT do

- **No ITIL module** like GLPI: no CIs/assets, changes, contracts (❌)
- **No real project management** (tickets ≠ task management à la OpenProject)
- **No telephony server** — CTI only connects to (3CX, Asterisk, Jitsi …)
- **No multi-tenant SaaS without workarounds** (separating instances is needed)
- **Chat without its own SIP/voice component**, knowledge base without Confluence comfort

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| REST API /api/v1 + webhooks | official |
| Store apps | Jira sync, Microsoft 365, Slack … (installable by admin) |
| ES/OpenSearch | Search index, a prerequisite |
| SSO | LDAP, OIDC, SAML |
| Backups | `zammad backup` (tar: DB + storage + config) |
