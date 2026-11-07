# Tryton - Description

## What the program does

Tryton is ERP for people who love order: small, clean modules, well-considered state models, no feature bulk. The desktop client feels like a database IDE for commercial work — fast, consistent, honest.

## Advantages

- **Extremely stable/long-lived**, disciplined upgrade paths
- **Genuine open source** (no open core)
- RPC interface straightforward — automation without marketing API

## Differentiation

| System | Difference |
|--------|-------------|
| **Odoo** | suite+web+store; Tryton focused and narrow |
| **GnuCash** | accounting only, single user; Tryton multi-user ERP |
| **ERPNext** | framework scope; Tryton module sparseness |

## Technical details

- **Stack**: Python (trytond), PostgreSQL; GTK clients; web UI integrated
- **Model**: ORM with `Model.<name>.execute` RPC methods
- **Deploy**: Debian packages, Docker, own servers
- **Licence**: GPL

## For whom it is suitable

- Cooperatives/offices with IT competence and a focus on stock keeping
- FreeSynergy scenarios: stable accounting backend skin (journals/reconcile)
