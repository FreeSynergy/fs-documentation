# Pipedrive - Description

## Overview

Pipedrive is a proprietary SaaS CRM from Estonia (since 2010), deliberately kept narrow: it organizes sales around pipeline, deals and activities and forgoes the broad marketing and service features of large platforms. There is no self-installation; the service is used in the browser and with official mobile apps.

## What Pipedrive does

Pipedrive manages **leads** (new prospects that still need to be qualified), **persons** (contacts), **organizations** (companies), **deals** (sales opportunities in pipelines with stages) and **activities** (calls, meetings, tasks). A deal carries an amount, expected close date, probability and involved contacts; the pipeline board shows the total per stage. In addition there is email synchronization with Gmail and Outlook, a shared Sales Inbox, a product list with quote lines, a report library and rule-based workflows.

## Advantages

- **Pipeline first**: kanban board with stages, drag & drop and close probability
- **Quick to learn**: few concepts, short onboarding for sales teams
- **Two-way email sync**: conversations land automatically on the deal or contact
- **Sales Inbox**: shared team email address with assignment to records
- **Built-in automations**: workflows for stage changes, tasks and field values
- **Well-documented REST API** with personal token and OAuth2
- **Reports out of the box**: pipeline forecast, activity reports, user performance

## Differentiation from other systems

### Pipedrive vs. HubSpot
- **HubSpot** is a platform with marketing, content and service hubs; **Pipedrive** stays with sales
- **HubSpot** has extensive outreach and campaign tools; **Pipedrive** has only basic email marketing
- **Pipedrive** is leaner to operate; **HubSpot** is more powerful but more complex

### Pipedrive vs. Zoho CRM
- **Zoho CRM** covers significantly more process depth with modules, Deluge scripts and blueprints
- **Pipedrive** is more narrowly focused on sales and therefore simpler
- **Zoho CRM** is cheaper as a package with the wider Zoho suite; **Pipedrive** excels at pipeline management

### Pipedrive vs. SuiteCRM
- **SuiteCRM** is open source and self-hosted; **Pipedrive** is SaaS only
- **SuiteCRM** includes support modules and free field modeling; **Pipedrive** has no cases without a workaround
- **SuiteCRM** requires administration; **Pipedrive** delivers updates automatically

## Technical details

- **Backend**: the provider's closed server landscape, reachable via the REST API v1
- **Database**: provider-side, no choice of own database; exports as CSV via the interface
- **Frontend**: browser application (single page application), official apps for iOS and Android
- **Authentication**: account with password, optional two-factor protection; API personal token and OAuth2
- **Hosting**: Pipedrive cloud only, no self-hosting; data storage and contract options depend on the agreement (version- and contract-dependent)

## Who is Pipedrive suitable for?

- **Small and medium sales teams** that want to run their pipeline visually
- **Agencies and service providers** that need deals, contacts and email history in one place
- **Teams without IT administration** that want SaaS usable immediately, without a project phase
- **Less suitable** for support tickets, elaborate marketing campaigns or organizations that must host their data themselves (then SuiteCRM or Zoho CRM)
