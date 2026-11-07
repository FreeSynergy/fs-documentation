# Pipedrive - Features

## Overview

Pipedrive works with five core objects — leads, persons, organizations, deals and activities — which are aligned toward closing via pipelines, stages and activities. Email sync, Sales Inbox, product list and workflows are built in directly; extensions come mostly from the marketplace or via the API.

---

## 1. Leads (prospects)

- **Lead capture**: name, source, contact route, amount estimate
- **Lead box**: collect and qualify before the pipeline
- **Qualification**: a lead becomes a deal with contacts and a company (one click)
- **Discard with reason**: lost leads remain evaluable
- **Import**: CSV import with field mapping and duplicate check

## 2. Persons (contacts)

- **Contact data**: name, company, job title, phone, email, address
- **Relationships**: contacts at organizations and across several deals
- **Activity history**: collected emails, calls, notes per contact
- **Fields**: own fields via the custom fields setup
- **Duplicates**: warning for the same email address or phone number

## 3. Organizations (companies)

- **Company master data**: name, address, industry, own fields
- **Tree structure**: parent and subsidiary companies via a relationship field
- **Contact list** and related deals in the detail view
- **Use without companies**: smaller teams work only with contacts

## 4. Deals and pipelines

- **Pipeline board**: columns per stage, tiles per deal, column order via drag & drop
- **Multiple pipelines**: e.g. "New business" and "Existing customers", each with its own stages
- **Deal fields**: amount, currency, expected close date, probability, source, owner
- **Closing handling**: move to "Won" or "Lost"; a reason prompt appears on loss
- **List view**: table with filters, sorting and column selection
- **Forecast**: weighted pipeline total per stage

## 5. Activities

- **Types**: task, call, meeting, email discussion; own types can be created
- **Schedule**: day and week view with due activities
- **Reminders**: notification at the set time, also by email
- **Multiple assignees**: assign activities to several users
- **Activity storage**: completed activities remain logged on the deal

## 6. Products and quotes

- **Product list**: catalog with standard price and currency
- **Deal products**: product lines with quantity and unit price on the deal
- **Revenue per deal**: sum of the product lines or a single field
- **Quote sending**: PDF or quote function as an add-on (version-dependent)

## 7. Email and Sales Inbox

- **Two-way sync**: Gmail and Outlook (add-in), IMAP/SMTP for other providers
- **Assignment**: emails are automatically assigned to contacts and deals
- **Sales Inbox**: shared team address with assignee assignment
- **Email templates**: personal and shared templates with placeholders
- **Follow-up**: read and click status for sent emails (version-dependent)

## 8. Automation

- **Workflows**: triggers (deal created, stage changed, field changed) plus actions
- **Actions**: create task, set field, send email, notification, assign lead
- **Pipeline automation**: stage rules and required fields per stage
- **Conditions**: filter per workflow, e.g. only deals above an amount

## 9. Reports and forecasts

- **Report library**: pipeline reports, activity reports, user performance, source analysis
- **Own reports**: freely combine axis, metric and filter
- **Forecast**: weighted closings per month or quarter
- **Team performance**: activities and closings per user and team

## 10. Configuration and rights

- **Pipelines and stages**: create, rename, change order
- **Custom fields**: text, number, date, selection, cascade, file (field types version-dependent)
- **Users and licenses**: Regular, Restricted and Admin; license assignment in the billing setup
- **Visibility groups**: who sees which deals and contacts
- **Import and field settings**: required fields, default values, formats

## 11. What Pipedrive CANNOT do

- **No ticket system / support cases**: no case management with SLA (helper objects only via fields or add-on apps)
- **No extensive email marketing**: no landing pages, forms or segmentation engine like HubSpot
- **No free modeling of new objects**: own modules cannot be created
- **No self-hosting**: data lives exclusively with the provider
- **No CalDAV or CardDAV interface**: calendar sync runs via provider integrations
- **No GraphQL API** and no official server-side event API other than webhooks
- **No multi-step approval workflows** (approvals) like in Zoho CRM
- **No free permanent subscription**: use is paid per user and month

## 12. Extensions, marketplace and integrations

- **Marketplace**: ready-made integrations (email, telephony, forms, accounting, invoicing)
- **Webhooks**: report events to own systems (see [api.md](api.md))
- **Form embedding**: website forms fill leads or contacts
- **Zapier, Make and n8n**: prebuilt connections to third-party apps
- **Browser extensions**: email connection for Gmail and Outlook
- **Mobile apps**: iOS and Android with pipeline, activities and email functions

---

## Comparison with related systems

| Feature | Pipedrive | HubSpot | Zoho CRM |
|----------|-----------|---------|----------|
| Pipeline board | very mature | available | available |
| Marketing hub | limited | extensive | extensive |
| Support tickets | not available | available (Service Hub) | available |
| Custom objects | not possible | limited (custom objects, plan-dependent) | possible |
| Scripting engine | none | workflow logic | Deluge |

---

## See also

- [menu.md](menus.md) - Navigation and roles
- [structure.md](layout.md) - Board, deal detail, themes
- [api.md](api.md) - REST API, token, webhooks
