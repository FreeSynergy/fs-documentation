# Dolibarr - Features

## Main features

### Core SME processes
- Third parties with contacts, commercial chain (quotes→order→delivery→invoice→payment), products/stock (multiple storage locations), projects with tasks/time tracking
- Membership module (members/fees) — NPO-suitable like hardly any other ERP

### Technology
- PHP module system with **triggers/hooks** (`modXxx` classes, e.g. `COMPANY_CREATED`), extension market (DoliaCloud/Dolistore)
- PDF templates (ODT-based), e-mail actions (send invoiced invoices), import/export wizards
- **REST API v3** + API key management; webhooks via the "API REST hooks" module

## What Dolibarr cannot do

- **No production control/MRP** (simple production yes, no planning)
- **Accounting = simplified journal**; DATEV/GoBD export only via add-ons
- **No real multi-tenancy** per instance (multi-company rudimentary)
- **UI functional and dated** (frames-layout era), no kanban aesthetics
- High-performance multi-tenancy: no

## Extensions and integrations

| Integration | Route |
|-------------|-----|
| Dolistore modules | commercial/free |
| REST v3 + webhooks module | official |
| Payment providers/PayPal | modules |
