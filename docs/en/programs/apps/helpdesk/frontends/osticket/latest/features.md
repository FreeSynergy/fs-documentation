# osTicket - Features

## Main features

### Ticket creation
- Email ingest via a POP3/IMAP fetcher (catch-all or reply address)
- Web forms (public ticket forms with captcha)
- API endpoint (see api.md)
- Help topics as entry points, optionally bound to forms

### Workflow
- Ticket status new → open → pending → closed with configurable status types
- Filter rules: classify incoming mails by pattern/domain/recipient (topic, group, priority, auto-reply, keep the ticket number in the subject)
- SLA plans with a due level per priority, business hours
- Assignment to agents and teams, collaboration via shared tickets

### Customers and knowledge
- Customer/organisation profiles with custom fields (forms)
- Customer portal with its own ticket list, FAQ (knowledge base), article categories

### Operations
- Plain PHP + MySQL, suitable for shared hosting
- Backups via database dump + upload folder

## What osTicket does NOT do

- **No full-text search engine** (MySQL LIKE — slow from a large history onwards)
- **No real-time collaboration** (no WebSocket, no live feed)
- **No channels like chat/Telegram/telephone** out of the box (only email/web)
- **No multi-stage workflows/BPM** and no business-rules engine (only simple filters)
- **No asset/ITSM module** (GLPI territory)
- **No modern theme system**; customizing = forking templates
- **No official cloud** (only third-party hostings)

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| API v1 | API key, create/read tickets/users |
| Cron job | Fetching, SLA escalation, automations |
| LDAP | Login for staff and customers (optional) |
| Plugins | The official plugin ecosystem is small; community patches exist |
