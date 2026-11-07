# eBay - Description

## What the program does

eBay rents out marketplace reach: listing, negotiating/auctioning, paying (managed payments), shipping, rating, under platform rules with buyer protection. FreeSynergy skins read and manage **external** sales through it (dashboards, ERP bridges).

## Advantages

- largest reach for second-hand goods and special lots
- well-designed seller APIs (Sell API family)
- auction as a price-discovery tool

## Distinction

| System | Difference |
|--------|-------------|
| **Etsy** | handmade/design curation; eBay open + auction |
| **Kleinanzeigen** | regional/local without payment/protection infrastructure |
| **Sharetribe (own marketplace)** | own rules/fees; eBay's are external |

## Technical details

- **Model**: SaaS platform (eBay Group), country sites
- **Authentication**: eBay account + OAuth2 (app ID/cert ID, user access token)
- **APIs**: REST-style plus traditional XML (Trading API); prefer the modern APIs

## Suitable for

- resale/special-lot logistics with ERP connection
- FreeSynergy skins: order/listing readers for analysis ([models.md](../../../../../../data/models.md))
