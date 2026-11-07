# EspoCRM - Description

## What the program does

EspoCRM is a lean CRM for small and medium-sized sales teams: leads through to deals, contacts and activities, plus the option to build your own object types with the entity manager. It is a single lightweight application (PHP + SPA) and therefore quick to host and quick to learn.

## Advantages

- **Lightweight**: runs on the smallest VPS, fast interface
- **Modelable without code** (the entity manager is the unique selling point)
- **Fair license**: GPL code, optional Pro extensions

## Differentiation

| System | Difference |
|--------|-------------|
| **SuiteCRM** | SuiteCRM is more powerful (Sugar heritage) but heavier; Espo is more modern and leaner |
| **CiviCRM** | non-profit domain (donations/memberships); Espo is a sales CRM |
| **HubSpot** | SaaS suite incl. marketing/content; Espo is a data CRM with its own infrastructure |

## Technical details

- **Backend**: PHP 8, MySQL/MariaDB/PostgreSQL; single-page frontend (Backbone + Handlebars, newer parts React)
- **Authentication**: session, API token, HMAC; LDAP/SAML/OIDC options
- **Extensions**: `.zip` installation without touching the core
- **License**: GPL (core), Pro version commercial

## Suitable for

- Teams that want a fast CRM with their own object types
- FreeSynergy scenarios that map CRM fields to the standard model (Lead/Account/Contact)
