# Etsy - Description

## What the program does

Etsy gives makers (seamstresses, printers, illustrators) a shared marketplace with a recognizable aesthetic: search by materials/occasions, shops with history, reviews as trust signals. Digital products extend this without shipping.

## Advantages

- a high-spending niche (gifts, unique items)
- API for listing/order automation (with approval)
- low entry barrier for creatives

## Distinction

| System | Difference |
|--------|-------------|
| **eBay** | open mass market + auction |
| **Kleinanzeigen** | regional, without payment/protection layer |
| **own marketplace (Sharetribe)** | own brand/rules |

## Technical details

- **Model**: SaaS, country shops (etsy.de)
- **Authentication**: Etsy account; API: API key + OAuth2 (authorization code + **PKCE**)
- **Approval**: app acceptance required (especially for write access)

## Suitable for

- creatives with sales automation (listing maintenance, order export to ERP)
- FreeSynergy skins: listing/receipt readers ([models.md](../../../../../../data/models.md))
