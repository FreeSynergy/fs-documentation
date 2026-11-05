# GLPI - Description

## What the program does

GLPI connects support tickets with the complete IT inventory: every ticket can be bound to a machine, a contract or a network object; changes and problems are managed as linked objects. On top of that come a self-service portal, a knowledge base and automatic inventory.

## Advantages

- **one system for helpdesk + assets** — replaces two tools
- **proven in public authorities/universities** (since 2003, huge community, translated into German)
- **rules engine** for assignments, status changes, notifications
- **free of charge** (GLPI Network offers commercial support versions)

## Differentiation

| System | Difference |
|--------|------------|
| **Zammad** | A pure, modern support cockpit without assets — Zammad is UX-driven, GLPI is data-model-driven |
| **Request Tracker** | Strong ticket workflow, no assets |
| **Snipe-IT** | Focused on asset management without a helpdesk — GLPI can do both |

## Technical details

- **Backend**: PHP 8+, MySQL/MariaDB; cron for SLA/inventory queue
- **Frontend**: server-rendered UI (tabulator tables), responsive portal
- **Authentication**: internal, LDAP, CAS, OIDC plugins; API token
- **Hosting**: LAMP, Docker images (officially glpi/glpi), high availability via DB replication
- **Licence**: GPL

## Who it suits

- IT departments that must interlink inventory and tickets
- Public administration/education with SSO requirements
- FreeSynergy skins with an asset + ticket link as a data-model template
