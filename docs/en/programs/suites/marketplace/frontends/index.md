# Marketplace — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Marketplace` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Arcemall](arcemall/index.md) | [latest](arcemall/latest/description.md) | Arcemall is a **low-code platform for your own marketplaces** (open-source approach): marketplace models (products/services, bookings, payments, search/map) are built with own-code components and t… |
| [CS-Cart Multi-Vendor](cs-cart-multivendor/index.md) | [latest](cs-cart-multivendor/latest/description.md) | CS-Cart Multi-Vendor (commercial software, PHP) turns a shop into a **marketplace with many vendors**: products, stock, shipping, payment gateways, vendor commissions, admin consoles. |
| [eBay](ebay/index.md) | [latest](ebay/latest/description.md) | eBay is the global marketplace for C2C/B2C with auction and fixed-price formats. |
| [Etsy](etsy/index.md) | [latest](etsy/latest/description.md) | Etsy (publicly listed) is the curated marketplace for **handmade goods, vintage and design**, including digital products. |
| [Kleinanzeigen](kleinanzeigen/index.md) | [latest](kleinanzeigen/latest/description.md) | Kleinanzeigen (formerly eBay Kleinanzeigen, Nowint/AVENUE A) is the largest **regional classifieds marketplace** in Germany: private and commercial providers post ads with a local reference, commun… |
| [Sharetribe](sharetribe/index.md) | [latest](sharetribe/latest/description.md) | Sharetribe is the leading **marketplace software**: open source (a marketplace you build yourself, Ruby on Rails; "Sharetribe Flex": API-first with web app/Marketplace Console) as well as SaaS vers… |

## File set per program (ADR 0012)

```
programs/suites/marketplace/frontends/<program>/
├── index.md        what it is, notable ideas, documented versions, sources
├── changelog.md    changes between documented versions (≥ 2 versions)
└── <version>/
    ├── description.md    required · Detailed description, differentiation, who it suits
    ├── features.md       required · What the program can do — and what not
    ├── layout.md         required · Window structure, regions, panels
    ├── menus.md          required · Menu structure, context menus, menus by role
    ├── shortcuts.md      required · Keyboard shortcuts
    ├── api.md            required · APIs and protocols, authentication, rate limits
    ├── themes/index.md   required · Themes: colours, typography, spacing — what can be rebuilt
    ├── interaction.md    if needed · Hover, focus, drag, gestures (finger, mouse, pen)
    ├── states.md         if needed · UI states and transitions
    ├── events.md         if needed · Events to the outside (webhooks, push, streams)
    ├── limits.md         if needed · Known limitations
    ├── i18n.md           if needed · Localisation, writing direction
    └── dependencies.md   if needed · Which of our components a frontend in this style needs
```

Protocols (Matrix, IMAP, CalDAV, …) are not frontends; they are described under [data](../../../../data/standards.md).
