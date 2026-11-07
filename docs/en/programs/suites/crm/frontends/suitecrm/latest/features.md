# SuiteCRM - Features

## Overview

SuiteCRM works module-based: each CRM object (lead, contact, company, opportunity, activity) has a list, detail and edit view with relationships to other modules. Dashlets, filters and reports sit on top; customizations run via Studio, the workflow module and the Module Loader.

---

## 1. Leads (prospects)

- **Capture**: form with name, company, industry, source and status
- **Status management**: `New`, `Assigned`, `In Process`, `Converted`, `Recycled`, `Duplicate`
- **Conversion**: a lead becomes a contact, an account and optionally an opportunity
- **Duplicate check**: similar-match rules in the admin area, warning on save
- **Import**: CSV import with field mapping and duplicate handling

## 2. Contacts and accounts (contacts and companies)

- **Contacts**: personal data, addresses, phone, email, team assignment
- **Companies (accounts)**: hierarchy via the "Parent Account" relationship
- **Subpanels**: a company's contacts, related opportunities, cases, activities
- **Field management**: required fields, formats and default values via Studio
- **Mass actions**: merge duplicates, overwrite fields, export

## 3. Opportunities (sales opportunities / deals)

- **Pipeline values**: sales stage, amount, expected close date, probability
- **Sales stages**: stages such as Prospecting, Qualification, Proposal, Closed Won/Lost
- **Contact roles**: roles of those involved (decision maker, buyer, user)
- **Lost reason**: reason for loss as a reporting field
- **Dashlets**: "My Opportunities", "Opportunities by sales stage", chart overview

## 4. Activities

- **Calls**: call history with duration and note text
- **Meetings**: appointments with participants, reminder and duration
- **Tasks**: tasks with due date and status (`Not Started`, `In Progress`, `Completed`)
- **Recurring activities**: series with an interval
- **Calendar-like view**: appointment overview in the meeting module, week and month view

## 5. Cases and bugs (support)

- **Cases**: case with status, priority, origin, solution notes
- **Bugs**: error reports with product and version reference
- **Customer portal**: self-service portal for cases and knowledge articles (version-dependent)
- **History**: timestamp and user history per record

## 6. Email and communication

- **Outbound accounts**: SMTP accounts in the admin area, sending from the application
- **Inbound mail**: query mailboxes, store emails as records
- **Email editor**: compose in the detail view, archive function for outgoing mail

## 7. Products, prices and quotes

- **Products**: product catalog with categories and list prices
- **Quotes**: quotes with product lines, discounts, total amount
- **PDF output**: PDF template module for printing quotes (version-dependent)
- **Relationships**: quote linked with opportunity and account

## 8. Campaigns and targets

- **Campaigns**: type, budget, costs, status, assigned target groups
- **Target lists**: recipient lists (target groups) with filters
- **Marketing emails**: bulk sending via an outbound account
- **ROI analysis**: revenue per campaign via linked opportunities

## 9. Projects and tasks

- **Projects and project tasks**: milestones, duration, simple dependencies
- **Status tracking**: progress per task, assignment to contacts

## 10. Reports, filters and dashlets

- **Report module**: module selection, field filters, group reports, CSV export
- **Dashlets**: panels on the home page (My Tasks, My Activities, pipeline chart, current cases)
- **Saved filters**: own and shared filter sets per module
- **List tools**: column selection, sorting, page size, full-text search

## 11. Automation

- **Workflow module**: triggers (record created/changed), conditions, actions (set field, send email, create task, assign record)
- **Scheduler**: scheduled jobs via `cron.php` (cleanup, campaign sending, workflow run)
- **Team assignment**: allocation via teams and roles
- **Audit log**: change history per field (standard field history)

## 12. Customization and administration

- **Studio**: create fields, change labels, edit list and detail layouts
- **Module Loader**: install extensions as ZIP packages with `manifest.php`
- **Logic hooks**: PHP code on model events (`before_save`, `after_save`)
- **Security Suite**: roles, teams and rights (View, Edit, Delete, Assign) per module
- **Locale and currency**: language packs, time zone, currency conversion
- **Repair functions**: clear cache, check database, rebuild relationships

---

## 13. What SuiteCRM CANNOT do

- **No modern kanban pipeline board out of the box**: opportunities appear as lists, filters and charts; a board like Pipedrive's is missing without an additional module
- **No email marketing with open and click tracking**: additional modules or external services are required
- **No built-in phone system or CTI**: connection only via connectors or third-party providers
- **No graphical database maintenance**: customizations run via Studio, vardefs or direct database access (at your own risk)
- **No multi-tenancy**: one instance serves one organization
- **No native mobile apps**: access via the browser
- **No runtime-configurable plugin system in the SaaS sense**: modules are installed and updated
- **No built-in rate limiting** for the API (see [api.md](api.md))

---

## 14. Extensions, modules and connectors

- **Module Loader packages**: additional field types, PDF tools, calendars, portals
- **Themes**: own themes via template and CSS directories
- **Self-service portal**: module for external customers with their own roles
- **Standard tools**: import/export, LDAP and AD authentication, tagging, audit log

---

## Comparison with related systems

| Feature | SuiteCRM | EspoCRM | SugarCRM |
|----------|----------|---------|----------|
| License | AGPL-3.0 | Open source | commercial |
| Pipeline board | limited (sales stages) | available | available |
| Support modules | Cases, Bugs | limited | Cases |
| API | REST v8, SOAP | REST | REST |
| Customization without code | Studio | Layout editor | Studio |

---

## Shortcuts and API

For keyboard control see [shortcuts.md](shortcuts.md), for interfaces see [api.md](api.md).

## See also

- [menu.md](menus.md) - Menu items by role
- [structure.md](layout.md) - Views and UI details
- [description.md](description.md) - Differentiation and technology
