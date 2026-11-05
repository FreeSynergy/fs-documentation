# Mautic - Description

## What the program does

Mautic automates communication workflows with your own data: forms collect contacts, segments sort them, campaigns supply them — all on your own server, API-first for synchronisation with CRM/ERP skins.

## Advantages

- **GPL + self-hosted** = GDPR close to home, no contact price curve
- **A broad REST API** (contacts/campaigns/reports) — the best synchronisation substrate
- The campaign canvas is easy to learn

## Differentiation

| System | Difference |
|--------|------------|
| **Mailchimp** | Comfort/sending included; Mautic is your own infrastructure |
| **Brevo** | SaaS comfort + EU; Mautic has data sovereignty |
| **Odoo Marketing** | Suite-integrated; Mautic is a specialist |

## Technical details

- **Stack**: PHP 8/Symfony, MySQL/MariaDB; campaign/segment batches via cron (`mautic:campaigns`)
- **Auth**: login; API: OAuth2 (recommended) or Basic (API accounts)
- **Deploy**: Docker/Composer; queue modes for scaling
- **Licence**: GPL

## Who it suits

- Organisations with their own IT and a drive to automate communication
- FreeSynergy scenarios: a contact broker between CRM skins (webhook → event, [models.md](../../../../../data/models.md))
