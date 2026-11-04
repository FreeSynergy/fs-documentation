# Zammad - Description

## What the program does

Zammad bundles support requests from all channels into a shared timeline per ticket. Customers are treated like contacts (organisations, history, products), SLAs are calculated over service times, and almost everything can be automated via API and triggers.

## Advantages

- **modern UX** with full-text search and bulk speed — well above classic PHP helpdesks
- **API-first**: every UI click is an API call; webhooks/triggers replace plugin overgrowth
- **Self-hosted with a clear path**: packages, Docker, source; cloud subscription optional
- **A real team tool**: shared tickets, task assignment, dashboards

## Differentiation

| System | Difference |
|--------|------------|
| **osTicket** | Leaner, PHP classic without Elasticsearch/API comfort; Zammad is faster and richer in API. |
| **GLPI** | ITSM with assets/CIs — whoever needs inventory takes GLPI; whoever needs a support timeline, Zammad. |
| **Request Tracker** | Proven, but Perl-conservative and mask-heavy; Zammad with a modern frontend and automation. |

## Technical details

- **Backend**: Ruby on Rails, background jobs (DelayedJob), WebSocket real-time
- **Search**: Elasticsearch/OpenSearch (a required component)
- **Database**: PostgreSQL (MySQL no longer supported in new versions)
- **Frontend**: Vue-based web UI, responsive
- **Authentication**: internal + LDAP/OIDC/SAML/CAS/Microsoft; API token and OAuth2
- **Hosting**: Ubuntu/Debian packages, Docker Compose, managed cloud
- **Licence**: AGPLv3

## Who it suits

- Support teams that need email-heavy work with a modern mask and SLAs
- FreeSynergy helpdesk skins with a standard ticket/comment/user model
- Migrations from Zendesk/RT/OTRS thanks to import assistants
