# GLPI - Features

## Main features

### Tickets (ITIL support)
- Ticket category tree, statuses incl. "accepted/in progress/solved/closed"
- SLA/OLA with business hours, escalation matrices, contract binding
- Linking of tickets with assets, problems and changes (change management)
- Self-service portal, planning (on-site appointments), follow-up tasks

### IT asset management (ITAM)
- Inventory objects incl. history, status chains (ordered → delivered → in use → disposed)
- Automatic inventory via GLPI Agent (formerly FusionInventory)
- Software licences, contracts, consumables, network/rack management

### Projects and tools
- Projects with tasks/Gantt, knowledge base, reports/statistics (SVG reports)

### Automation and integration
- Business rules (ticket assignment by criteria), notification matrices
- Cron-driven tasks; REST API; webhooks via the "glpi-webhooks" plugin (community)
- SSO: LDAP, CAS, OIDC (plugin), SMTP/VoIP headers

## What GLPI does NOT do

- **No modern real-time frontend** (server-rendered, reload instead of live)
- **No channel expansion like chat/Telegram** out of the box
- **No real ITIL process engine** (problems/changes as a data model without workflow states beyond a basic status)
- **The API is not at full parity**: some actions (mass editing) only on the UI side
- **Mobile use** only via the responsive portal/GLPI agent apps

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| Plugins (marketplace) | GLPI Agent, Fields, Webhooks, More reporting, Statistics |
| REST | `/apirest.php` |
| Monitoring | Connection via plugins/Zabbix (the "zabbix" plugin) |
| LDAP/CAS/OIDC | native/plugin |
