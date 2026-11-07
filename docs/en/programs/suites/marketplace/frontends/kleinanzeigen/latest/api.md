# Kleinanzeigen - API Documentation

## Overview

**Public API: none.** Automated reading/posting violates the platform terms; this documentation only covers legitimate routes.

**API types at a glance**

| Type | Use | Status |
|-----|------------|--------|
| public REST/webhooks | — | ❌ |
| Partner/commercial feeds | ad import for large dealers (contractual) | commercial |
| GDPR data export | request own ads/data | legal entitlement |
| GraphQL | — | ❌ |

## Legitimate exchange routes

```
own ads              → GDPR information/export (account function/request)
commercial offers    → partner feed contract (CSV/XML feed per specification)
reference for skins  → category/radius model as its own data model
                       (see ../../data/models.md)
```

Example feed format (partners only, schematic; the operator's specification is authoritative):

```
offer_id;title;description;price;currency;latitude;longitude;category
1001;3-seater sofa;good condition;120;EUR;52.517;13.404;furniture
```

## Rate Limits

Not applicable (no open API).

## Skin note

Kleinanzeigen skin = **own mini-marketplace skin** in FreeSynergy (listings + radius search via maps skins) instead of a connection: copy the category/radius pattern, do not dock onto it.
