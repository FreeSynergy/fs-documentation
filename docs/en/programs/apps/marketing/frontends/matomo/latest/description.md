# Matomo - Description

## What the program does

Matomo is web analytics with your own rules: tracking code in, reports out — and everything sits in your own basement. The data-protection modes (cookieless, consent APIs) make it the standard replacement for GA on German municipal/association websites.

## Advantages

- **GDPR-fit by design** (self-hosting, no third-party transfer)
- GA import (data can be imported from GA) for migration
- The tracking HTTP API = server-side event skins without a browser

## Differentiation

| System | Difference |
|--------|------------|
| **GA4** | Free/Google coupling; Matomo has data sovereignty |
| **Plausible** | Even more minimalist (one number, one script); Matomo has the full report depth |
| **Piwik PRO** | A privacy enterprise twin (commercial) |

## Technical details

- **Stack**: PHP 8, MySQL/MariaDB (archive tables + visitors/visits), optional: Redis
- **Auth**: login + `token_auth` (API), 2FA
- **Deploy**: suitable for shared hosting, official Docker images, Matomo Cloud
- **Licence**: GPL (core), premium plugins commercial

## Who it suits

- Organisations with a compliance duty + an analytical claim
- FreeSynergy skins: Matomo as the standard analytics layer ([models.md](../../../../../../data/models.md): event → visit → conversion)
