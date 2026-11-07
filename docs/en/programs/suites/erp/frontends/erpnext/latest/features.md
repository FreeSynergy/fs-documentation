# ERPNext - Features

## Main features

### Frappe doctypes
- Every entity = doctype (schema + rights + UI automatically): Customer, Sales Invoice, Stock Entry…; custom fields/properties without code
- **Client/server scripts**, report builder, print formats (Jinja), notification events

### ERP scope
- Multi-company/consolidated accounting (IFRS-capable), multi-currency, assets, payroll (country-dependent), manufacturing (BOM, work orders), quality, subcontracting
- Webshop (Frappe website), POS, portal for customers/suppliers

### Automation
- **Webhooks** (doctype change → POST, signing secret)
- Scheduler/real-time events (Socket.IO), auto-repeat for documents, workflow engine (approval stages)

## What ERPNext cannot do

- **UI less polished** than commercial suites (learning curve of Frappe concepts)
- **Localised accounting** (GoBD/DATEV, local tax) only via community add-ons — note the German country guide
- **No official SaaS reference scale** like Odoo Online (hosting: DIY/Frappe Cloud)
- Very large transaction volumes → MariaDB tuning required

## Extensions and integrations

| Integration | Route |
|-------------|-----|
| REST API + webhooks | official, first class |
| Apps in the Frappe ecosystem | GitHub apps (e.g. German accounting) |
| Zapier/Make | connectors (community) |
