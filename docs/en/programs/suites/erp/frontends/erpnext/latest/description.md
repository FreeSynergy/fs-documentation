# ERPNext - Description

## What the program does

ERPNext delivers the complete ERP (through to period-end closing) under a free licence and provides the technology as a framework: doctypes define the data world, API/webhooks included. Anyone who understands Frappe operates ERPNext with ease.

## Advantages

- **100% FOSS, no feature walls** (unlike Odoo Enterprise)
- **Best API practice** in the ERP field (JSON REST, machine-readable doctype schema)
- Frappe ecosystem also for non-ERP apps (customer portal, helpdesk)

## Differentiation

| System | Difference |
|--------|-------------|
| **Odoo** | broader store/comfort, but an Enterprise window; ERPNext uncompromisingly open |
| **Dolibarr** | simpler (SME invoicing load); ERPNext full manufacturing/HR |
| **SAP Business One** | proprietary/licensed; ERPNext equivalent core, different UX |

## Technical details

- **Stack**: Python (Frappe), MariaDB, Redis, Node build assets; Socket.IO for real-time
- **Models**: doctypes (JSON schema + controller classes), linked documents, name series
- **Auth**: session, **token (`Authorization: token key:secret`)**, OAuth2/OIDC
- **Deploy**: Bench CLI (own servers), Docker, Frappe Cloud
- **Licence**: GPLv3

## For whom it is suitable

- IT-savvy SMEs/medium-sized businesses with a data-sovereignty requirement
- FreeSynergy scenarios: reference ERP for API sync skins (addresses/orders ↔ CRM)
