# eBay - Features

## Main features

- **Formats**: auction, buy it now, price proposal (best offer); local pickup (location-based, maps reference)
- **Seller tools**: bulk listings (File Exchange), price/stock API, promotions, shipping labels
- **Catalog/category system** (Browse API) with product identifiers (MPN/GTIN)
- Buyer protection/fraud detection, double opt-in for ratings, case-based dispute resolution (if applicable)

## What you must NOT do / what eBay cannot do

- **no full access**: APIs allow listings/orders, but not community features (chats only to a limited extent), no webhooks to arbitrary endpoints (use the notification systems of each API)
- account suspensions for policy violations; automation must comply with policies
- the auction mechanism is proprietary; no export of complete marketplace data
- the fee structure makes very small volumes unattractive

## Extensions and integrations

| Integration | Path |
|-------------|-----|
| Sell/Browse/Inventory/Fulfillment/Marketing API | official (approval levels) |
| Notification systems (pull/`getListings` poll vs. push, depending on API) | official |
| WaWi/ERP connectors (lexoffice, JTL…) | partners |
