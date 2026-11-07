# Odoo - Features

## Main features

### Integrated suite
- CRM/lead→quotation→order→invoice→payment end to end; warehouse (double-entry flows, barcodes), manufacturing (MRP/BOM), projects/tasks, HR (leave, salary Enterprise), website/shop/POS
- Shared models (`res.partner` for customers/suppliers/contacts) → clean data relations

### Customisability
- **Modules as Python packages**: models (ORM), views (XML), rights, menus; inheritance of existing ones (`inherit_id`)
- **Studio** (Enterprise): fields/views/automations without code; automations (ir.ql triggers)
- View types: kanban/list/form/calendar/pivot/graph, dashboards

### Operations
- Multi-company/multi-currency/multi-language, portal access, e-mail flows (alias→record), QReport PDF

## What Odoo cannot do

- **Enterprise features are paid** (full accounting only in Enterprise, Studio, mobile barcode)
- **ORM API powerful, but no clean public REST** (XML-RPC standard; REST module new/Enterprise-dependent — check current state)
- **Updates between major versions** require migration (custom-code trap)
- **Consolidation depth** below SAP/DATEV level (add-ons needed)
- Very generic UI: onboarding requires configuration discipline

## Extensions and integrations

| Integration | Route |
|-------------|-----|
| App store (40k+ modules) | partly commercial |
| XML-RPC/JSON-RPC + webhooks (Enterprise) | official |
| Payment/shipping providers | official providers |
