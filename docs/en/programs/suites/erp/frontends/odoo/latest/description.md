# Odoo - Description

## What the program does

Odoo wires companies together in one suite: a lead becomes a quote, a delivery, an invoice — the same database, the same partner models. The open-source core plus modular extensibility make it a building-block ERP.

## Advantages

- **One system instead of point solutions** (CRM+ERP+website from one source)
- **Community free and self-hostable**; Cloud/Odoo.sh for convenience
- **ORM/module system** = customisations first-class

## Differentiation

| System | Difference |
|--------|-------------|
| **ERPNext** | similarly open approach, Frappe framework; Odoo larger community/app store |
| **SAP** | group processes/certifications; Odoo more flexible for SMEs |
| **Dolibarr** | leaner (SME invoicing/stock); Odoo broader/deeper |

## Technical details

- **Stack**: Python, PostgreSQL; web frontend (OWL web framework), QWeb reports
- **Models**: ORM with field types, compute/onchange, recursive inheritance
- **Authentication**: session login, portal; API: RPC token/OAuth2 (newer APIs), 2FA
- **Deploy**: own server, Docker, odoo.sh, Odoo Online (SaaS)
- **Licence**: LGPL (Community) + proprietary Enterprise apps

## For whom it is suitable

- SMEs/medium-sized businesses that want ERP+CRM+web from one source and customisable
- FreeSynergy skins: `res.partner`/`sale.order` patterns as reference for address/order models ([models.md](../../../../../../data/models.md))
