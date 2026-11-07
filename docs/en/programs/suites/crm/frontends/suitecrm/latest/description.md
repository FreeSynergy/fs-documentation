# SuiteCRM - Description

## Overview

SuiteCRM is a free, web-based CRM under AGPL-3.0, which emerged in 2013 as a spin-off of the then-open SugarCRM suite (as of SugarCRM 6.5). It is maintained by a community around the provider SalesAgility. The 7.x line (7.14.x as LTS) uses the classic Sugar frontend; SuiteCRM 8 places an Angular interface in front of the same module layer.

## What SuiteCRM does

SuiteCRM manages customer data and sales processes in modules: **Leads** (unqualified prospects), **Contacts**, **Accounts** (companies), **Opportunities** (sales opportunities/deals) and **Activities** (calls, meetings, tasks). In addition there are cases and bugs for support, products, quotes, campaigns, projects and reports. Permission levels, fields and layouts are adjusted without programming; extensions come into the instance as modules via the Module Loader.

## Advantages

- **Free license**: AGPL-3.0, no license costs, no binding user count
- **Self-hosted**: data stays on your own infrastructure (PHP, MySQL/MariaDB)
- **Broad module range**: leads, contacts, accounts, opportunities, cases, quotes, projects out of the box
- **Customizable without code**: Studio for fields, labels and layouts; workflow module for automations
- **API access**: REST interface (v8) and SOAP on a module basis
- **Extensible**: Module Loader, logic hooks, connectors, own themes
- **German interface**: language packs included

## Differentiation from other systems

### SuiteCRM vs. SugarCRM
- **SugarCRM** is the commercial further development with a cloud offering and newer features
- **SuiteCRM** is based on the last open Sugar version and remains fully free
- **SugarCRM** offers more convenience; **SuiteCRM** the freer license and self-management

### SuiteCRM vs. EspoCRM
- **EspoCRM** is leaner, more modern and faster, but functionally narrower
- **SuiteCRM** covers more areas (support, campaigns, quotes, projects)
- **EspoCRM** is easier to maintain; **SuiteCRM** is more powerful but more complex

### SuiteCRM vs. CiviCRM
- **CiviCRM** is tailored to clubs and associations (constituent management) and depends on a CMS
- **SuiteCRM** is a standalone sales CRM with pipeline orientation
- **CiviCRM** is strong on donations and memberships; **SuiteCRM** on leads and deals

## Technical details

- **Backend**: PHP in the SugarCRM architecture (modules, vardefs, logic hooks); SuiteCRM 8 adds a Symfony layer in front of the legacy layer
- **Database**: MySQL or MariaDB
- **Frontend**: 7.x template sets (Handlebars) and JavaScript in the Sugar layout; 8.x Angular shell with its own theme
- **Authentication**: local accounts with roles and teams, optional LDAP/Active Directory connection, session cookie in the browser
- **Hosting**: Apache or nginx with PHP, Docker images from the community and SalesAgility, scheduler via `cron.php`; shared hosting is possible

## Who is SuiteCRM suitable for?

- **Small and medium enterprises** that run a complete CRM themselves without license costs
- **Sales and support teams** that bundle leads, deals and cases in one instance
- **Administrators with PHP/MySQL knowledge** who maintain fields, layouts and workflows themselves
- **Less suitable** for teams that expect a modern interface without administration effort (then EspoCRM or a SaaS solution)
