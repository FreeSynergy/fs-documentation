# Consul - Description

## What the program does

Consul brings a city's classic participation formats together under one roof — proposals, budget, votes, debates — and combines online participation with municipal verification. It originated in Madrid ("decide.madrid.es") and has been reused hundreds of times.

## Advantages

- **Proven format library** (citizen budgets are the flagship)
- Apache licence (more permissive than Decidim's AGPL)
- Public API for evaluation dashboards

## Differentiation

| System | Difference |
|--------|-------------|
| **Decidim** | Phase-based process framework; Consul uses format tiles |
| **pol.is** | Deliberation waves instead of a motion catalogue |
| **LiquidFeedback** | Internal group decisions (delegative) |

## Technical details

- **Stack**: Ruby on Rails, PostgreSQL
- **Auth**: Accounts with verification levels (configurable), OAuth2
- **Licence**: Apache-2.0; deployment: Docker, classic Rails servers

## For whom it is suitable

- Municipalities and regions with a classic participation range
- FreeSynergy skins: budget and support patterns ([models.md](../../../../../../data/models.md))
