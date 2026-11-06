# Adhocracy4 - Description

## What the program does

Adhocracy4 structures municipal participation into traceable phase modules — from brainstorming through review to the Kiezkasse. It is the framework behind several German city portals and thus the pragmatic middle ground between the formalism of Decidim and the format mix of Consul.

## Advantages

- Proven in large cities (Berlin, many municipalities in the STADTLAND network)
- Clean REST API for evaluation skins
- Geo focus (ideas on a city map) — a natural bridge to map skins

## Differentiation

| System | Difference |
|--------|-------------|
| **Decidim** | Process- and component-strict; A4 uses phase modules |
| **Consul** | Format tiles and polls; A4 idea review and Kiezkasse |
| **pol.is** | Mass deliberation; A4 curated projects |

## Technical details

- **Stack**: Python/Django, PostgreSQL, Leaflet maps
- **Auth**: Accounts (municipal login procedures can be connected)
- **Licence**: AGPL; deployment: Django hosting/Docker
- **Origins**: liqd (liquid democracy e.V.) → STADTLAND

## For whom it is suitable

- Municipalities that run participation coupled with administrative follow-up
- FreeSynergy skins: ideas, rating and geo as a model ([models.md](../../../../../../data/models.md) + [positions](../../../../../apps/maps/standpunkte.md))
