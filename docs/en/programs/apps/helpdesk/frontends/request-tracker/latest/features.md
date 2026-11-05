# Request Tracker - Features

## Main features

### Queues and tickets
- Queues as work areas with their own rights, templates, autoresponders
- Ticket status new/open/stalled/resolved/rejected; ticket merging (parents/children)
- Custom fields (text, selection, stages…) per queue, storage of transactions

### Automation with scrips
- Configurable "condition → action" scrips per queue/transaction (Perl one-liners possible)
- AutoReply/AutoCreate from emails, escalation via cron (`rt-crontool`)
- The notification logic is entirely driven by rights/templates

### Search and reports
- Query language (`Queue = "Hardware" AND Status = "open" AND Owner = "nobody"`)
- Saved searches, dashboards, statistics reports; the "charts" shipped with RT (RT-IR)

### Email workflow
- Ingest: everything sent to `queue-name@server` (and aliases) becomes a ticket/reply
- Outgoing per transaction, thread retention via ticket IDs in the subject

### REST and CLI
- REST 1.0 + JSON-RPC 2.0, the CLI `rt` and `rt-mailgate`

## What RT does NOT do

- **No modern web frontend** (Mason template classic; the new MUI interface in RT 5 is only a framework)
- **SLA/deadlines** only via additional modules (`RT-Extension-SLA`)
- **No self-service portal** in the Zammad sense (only email + web login)
- **No chat/telephone channel**
- **No asset module** in the core (RT-IR for inventory as an add-on, not at GLPI level)

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| Extensions (`RT::Extension::*`) | SLA, FullTextSearch, CommandByMail, Telegram, Agenda |
| SSO | LDAP, Shibboleth/OIDC (plugin) |
| Full-text search | GSA (RT-Extension-GSA) or PG triggers |
| Import | `rt-importer` (Outlook, RT2, OTRS) |
