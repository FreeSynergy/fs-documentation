# osTicket - Description

## What the program does

osTicket converts incoming emails into tickets, assigns them to teams and accompanies them until the reply. It keeps the workflow minimal: help topics, status, priorities, SLA deadlines — nothing more, and that is exactly its strength.

## Advantages

- **runs everywhere**: PHP/MySQL suffices, shared hosting too
- **learned quickly**: agents need no training
- **email-centred** without forced web use: customers simply reply by mail
- **predictable**: no feature inflation over the years

## Differentiation

| System | Difference |
|--------|------------|
| **Zammad** | A modern mask, search index, channels, API richness — Zammad is the "modern" counter-design |
| **Request Tracker** | More powerful/regexp-heavy, Perl, rather for large organisations |
| **GLPI** | ITSM incl. assets; osTicket stays with the support ticket |

## Technical details

- **Backend**: PHP (8-compatible), MySQL/MariaDB
- **Frontend**: server-rendered templates (own theme system), agent/portal view
- **Authentication**: local, optionally LDAP
- **Hosting**: Apache/nginx + PHP, cron for fetch/SLA
- **Licence**: GPL (community edition)

## Who it suits

- Small teams/clubs with a mail inbox as the support channel
- Environments with no room for Elasticsearch & Co.
- FreeSynergy skins that show the plain ticket-status workflow (new/open/pending/closed)
