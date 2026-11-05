# Zendesk - Description

## What the program does

Zendesk runs support as a service: customers write via any channel, everything becomes a ticket; agents work in views with triggers/automations, customers help themselves via the help centre. Admins configure rules without code, developers via API.

## Advantages

- **immediately operational** (no installation, channels live within hours)
- **very complete API** — practically every UI function is mirrored in the API
- **ecosystem**: thousands of marketplace apps

## Differentiation

| System | Difference |
|--------|------------|
| **Freshdesk** | A similar SaaS feature scope, often cheaper; a similar API, a smaller events system |
| **Zammad** | A self-hosted alternative with its own data sovereignty, less AI/telephony kit |
| **Intercom** | Messaging/sales-first; Zendesk is ticket-first |

## Technical details

- **Model**: multi-tenant SaaS; subdomain per account (`firma.zendesk.com`)
- **Authentication**: email + password, SSO (SAML/OIDC), API token, OAuth, JWT for apps
- **Data storage**: Zendesk's own; audit-log retention plan-dependent
- **Contracts**: agent/resolution-based (plan-dependent); support tiers

## Who it suits

- Companies that want to outsource support without operating it and accept US/EU cloud centres
- FreeSynergy skins for ticket-first workflows with a clean REST model
- As a reference API (v2) when modelling your own ticket interfaces
