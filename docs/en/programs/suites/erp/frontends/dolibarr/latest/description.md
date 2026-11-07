# Dolibarr - Description

## What the program does

Dolibarr covers the commercial side of a small business: who (third parties), what (products), which documents (quotes through to payment), which warehouse, which project. Runs on any web space and has been maintained for over 20 years.

## Advantages

- **LAMP operation without special knowledge**, extremely stable
- **Modular**: what you don't switch on, you don't see
- API + triggers are sufficient for automations (in moderation)

## Differentiation

| System | Difference |
|--------|-------------|
| **Odoo/ERPNext** | Suite depth (manufacturing, HR, website); Dolibarr deliberately smaller |
| **Lexware/wiso** | closed SaaS; Dolibarr open source, self-hosted |
| **CiviCRM** | NPO specialist; Dolibarr has a membership module + commercial chain |

## Technical details

- **Stack**: PHP 8, MariaDB/MySQL; multi-instance setup possible
- **Auth**: session login; API: API key (`Authorization: Bearer <key>`) or session token
- **Deploy**: shared hosting, Docker images, Docker community builds
- **Licence**: GPL

## For whom it is suitable

- Small companies/associations with their own hosting and a focus on paperwork
- FreeSynergy scenarios: lightweight ERP counterpart for CRM/invoice skins
