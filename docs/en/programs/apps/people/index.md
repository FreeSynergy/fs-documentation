# Contact and CRM Management

## In short

People holds the people in your life: friends, family, colleagues, customers, and groups of them. Each person is one card, and one card can carry several roles. It answers the question: who is this?

**Command:** `fs-people`, one command per program with subcommands ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md); programs are switched over when they are next touched, so not every one is yet).

## What is different here

- A card follows the open JSContact standard (RFC 9553). Anything the program does not understand is kept, not thrown away.
- You can bring contacts in as vCard and take them out again; the original text is kept per card.
- Cards marked sensitive stay out of exports unless you release them by name. Roles are kept apart from the card, so an export does not reveal them.
- If a participant is an AI, the card says so. The mark restricts nothing; it only tells you who you are dealing with.
- People works alone. Other FreeSynergy programs can refer to a person by id instead of keeping their own copy.

## Where it stands today

Latest tag: `v0.0.2`. You can create, edit, delete, list and search cards, import and export vCard, and keep groups, several roles per person and relations. The program can propose that two cards are the same person; nothing is merged until you confirm. A small server and a first, provisional window exist.

Not there yet: managing groups, relations and roles or setting the sensitive mark in the window, undo and live updates, sign-in (the acting person is a placeholder), CardDAV and sync between devices. The interface is a draft with no second user yet, so it may still change.

## Planned facets

Facets are parts of a program that look like apps of their own ([ADR 0061](../../../decisions/0061-facetten.md)). Each gets its own command, a link to `fs-people` ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md)).

Proposed, not built:

- Contacts: your address book.
- Users: people who use the system.
- AIs: participants that are AI.
- Partners: leads, customers and suppliers.
- Team: the people you work with.
- Members: members of a group or association.

## Overview

This section contains documentation for various contact and CRM systems.

## Available Systems

- **civicrm** - Constituent Relationship Management
- **suitecrm** - Open Source CRM
- **odoo** - Business management software (CRM module)
- **frappe** - Modern ERP with CRM
- **metronic** - CRM system
- **pipedrive** - Sales pipeline management
- **lessonly** - Customer data platform
- **salesforce** - CRM platform
- **hubspot** - CRM platform
- **zoho-crm** - CRM software
- **insightly** - CRM and project management
- **pabbly-crm** - CRM software
- **capsule** - CRM for small businesses
- **sugarcrm** - CRM platform
- **roistat** - Marketing analytics and CRM

## What is CRM?

CRM (Customer Relationship Management) is a concept for the systematic management of customer relationships. CRM systems include:

- Manage contact data
- Track interactions and communication
- Manage sales pipeline
- Track sales opportunities (opportunities)
- Customer analysis and segmentation
- Automate marketing and sales processes

## Application Areas

- **Sales**: Lead generation and opportunity management
- **Customer Service**: Customer service and support
- **Marketing**: Campaigns and customer segments
- **E-commerce**: Customer management for online shops
- **Services**: Service provider customer management

## Benefits of CRM Systems

- **Customer proximity**: All customer information in one place
- **Sales promotion**: Identify sales opportunities
- **Customer retention**: Better customer service
- **Analysis**: Customer analysis and reports
- **Automation**: Automate processes
- **Integration**: Connection with other tools

## Selection Criteria

When choosing a CRM system, consider the following criteria:

- **Features**: Which features are required?
- **Scalability**: How many customers and contacts?
- **Ease of use**: How user-friendly is it?
- **Integration**: How well does the system fit into the existing infrastructure?
- **Costs**: Free or paid?
- **Mobile access**: Mobile apps available?

## Related Categories

- [Marketing](../marketing/) - Marketing tools and analytics
- [Helpdesk](../helpdesk/) - Support and ticket systems
- [Project Management](../../suites/projectmanagement/) - Project management

## Quick Start

1. **Select CRM**: Choose a system based on requirements
2. **Installation/Account**: Install system or create account
3. **Configuration**: Customize and configure the system
4. **Import data**: Import existing customers and contacts
5. **Define workflow**: Define sales and marketing processes

## More Information

Further information can be found in the documentation of individual CRM systems.

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysed programs (6), by function, nothing copied (ADR 0012/0013):

- [Apple Contacts](frontends/apple-contacts/index.md) — Apple Contacts is the address book built into Apple's operating systems.
- [GNOME Contacts](frontends/gnome-contacts/index.md) — GNOME Contacts is the lean contact app for GNOME: create contacts, link them, synchronise them with Evolution Data Server sources (local address books, CalDAV/CardDAV accounts, Google, LDAP).
- [Google Contacts](frontends/google-contacts/index.md) — Google Contacts is the address book tied to a Google Account.
- [KAddressBook](frontends/kaddressbook/index.md) — KAddressBook is the contact management application of KDE PIM: vCard-based, managed through Akonadi resources (local folders, IMAP-Contacts, CardDAV, LDAP).
- [Monica](frontends/monica/index.md) — Monica is a self-hosted personal CRM: capture people with all their relationships, activities, gifts, tasks and notes — as a web app (Laravel/Vue) with a REST API.
- [Nextcloud Contacts](frontends/nextcloud-contacts/index.md) — Nextcloud Contacts is the contact app of the Nextcloud suite: address books in the browser, synchronised over CardDAV with all devices, linked to user accounts, circles/groups and the people area o…

Overview: [frontends](frontends/index.md)
<!-- /gen:frontends -->
