# Sharetribe - Description

## What the program does

Sharetribe provides the complete package to teach **your own marketplaces** how eBay & Co work: providers post offers, prospective customers search including a map, and booking/payment/reviews run through the platform with escrow logic via Stripe.

## Advantages

- fastest path to a working C2C marketplace
- API-first path for a custom frontend (skin-friendly!)
- payment/trust layer already solved

## Distinction

| System | Difference |
|--------|-------------|
| **Arcemall/CS-Cart MV** | shop-based multivendor (products/shipping); Sharetribe = rental/services |
| **eBay/Etsy** | third-party marketplaces; Sharetribe = your own marketplace |
| **WooCommerce + plugin** | WP tinkering; Sharetribe has a more thought-out booking flow |

## Technical details

- **Model**: SaaS (newer versions); legacy community edition in Ruby on Rails (OSS, old)
- **Payments**: Stripe Connect (payouts to providers)
- **APIs**: Marketplace REST API (v1), OAuth2 client credentials + user tokens
- **Maps**: Mapbox (new)/Google; OSM integration can be built yourself ([maps skins](../../../../../apps/maps/index.md))

## Suitable for

- initiatives with a regional exchange/service marketplace
- FreeSynergy scenarios: offer/location model in [models.md](../../../../../../data/models.md); listing geo → [standpunkte.md](../../../../../apps/maps/standpunkte.md)
