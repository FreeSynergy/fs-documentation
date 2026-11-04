# Monica - Description

## What the program does

Monica gathers everything around a person: who they are, how we are connected, what we did together, what I gave them, what I intend to call them about. It is a personal relationship diary with a CRM structure — self-hosted, with a web UI and an API.

## Advantages

- **Keep what matters**: relationships, activities, gifts, debts in one place
- **GDPR-friendly**: your own instance, export as JSON/vCard
- **API-first enough**: REST + webhooks for automation (n8n & Co.)
- **Lightweight**: PHP/MySQL, Docker image, small resource footprint

## Differentiation

| System | Difference |
|--------|------------|
| **Nextcloud Contacts** | An address book without history; Monica adds the story (activities, gifts, relationships). |
| **Trekk** | A similar personal CRM, younger, Go stack; Monica is more broadly integrated (imports, webhooks). |
| **SuiteCRM/Pipedrive** | A business CRM with leads/deals — the wrong tool for family/friends. |

## Technical details

- **Backend**: PHP (Laravel), MySQL/MariaDB; queue worker for reminders
- **Frontend**: Vue 2 components + Blade views (API-driven, with SSR parts)
- **Authentication**: Session + e-mail verification; API token; 2FA (TOTP) supported
- **Hosting**: Docker (web + worker + cron), Monica CLOUD as the managed variant
- **Licence**: BSL (Business Source License) — source is open, commercial hosting is restricted

## Who it suits

- People with a wide network of relationships who have follow-up anxiety ("when did I last take care of aunt Last?")
- FreeSynergy contact scenarios with an activity-log model: mapping onto contact + event + task
