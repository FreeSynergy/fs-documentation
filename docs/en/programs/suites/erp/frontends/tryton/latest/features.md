# Tryton - Features

## Main features

- **Module mix**: account (multi-level plans, multi-currency), sale/purchase (approval stages), stock (locations, moves, lot/serial), production (BOM/work), project/timesheet, CRM, invoice payment reconcile
- **Field logic**: "fields prefill/onchange", state fields with workflow buttons, granular record rules
- **Clients**: desktop (GTK) + web; server multi-instance capable
- **Reports**: report engine (Py3o/ODT or PDF), reports bound to documents

## What Tryton cannot do

- **No website/shop/POS builder** (like Odoo) — pure ERP
- **No drag & drop kanban**, conservative UI
- **Fewer ready-made integrations** (payment/shipping) than Odoo — build your own via modules/RPC
- German localisation (GoBD, DATEV) = community work

## Extensions and integrations

| Integration | Route |
|-------------|-----|
| RPC (XML-RPC/JSON-RPC) | official, stable |
| Module ecosystem (Tryton bug tracker/community) | manageable, quality-focused |
| Tryton dev kit (Python) | own modules as Python packages |
