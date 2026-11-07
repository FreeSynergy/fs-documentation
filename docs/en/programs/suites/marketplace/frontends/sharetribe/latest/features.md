# Sharetribe - Features

## Main features

### Marketplace basics
- Listings with variants/blocking, map search (Google Maps or **Mapbox/OpenStreetMap routes; check per version**, OSM support to be expanded), calendar bookings
- Transaction processes: inquiry → offer → order/pre-booking (authorization) with Stripe payments + payouts
- two-sided reviews, profile verification, chat

### Flex/Marketplace platform (developer path)
- **API-first**: own frontend (React resource template "default-templates"), custom fields/listing types
- Webhooks for lifecycle events, Marketplace Console as admin overlay

### SaaS variants
- Sharetribe Go (click-together builder), Sharetribe One (current product); community edition = old OSS branch (community forks)

## What Sharetribe cannot do

- **no full self-hosting for the current version** (SaaS core; OSS only as a legacy fork)
- no inventory complexity/shipping logistics (rather services/local rentals)
- auction formats missing (fixed prices/negotiation)
- payment only via Stripe (mind geographic availability)

## Extensions and integrations

| Integration | Path |
|-------------|-----|
| REST API + webhooks | official |
| React template (default-templates) | official |
| Google Analytics/Pixel | built in |
