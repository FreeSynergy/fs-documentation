# Google Analytics - Description

## What the program does

Google Analytics counts visits and events on the web and derives user journeys from them. GA4 unifies web + app, funded through the Google ecosystem — free, powerful, worth weighing up in data-protection policy.

## Advantages

- Free scope + Google bundle (Search Console/Ads)
- Explorers for your own analyses without SQL
- BigQuery raw data for data-warehouse frontends

## Differentiation

| System | Difference |
|--------|------------|
| **Matomo** | Self-hostable, full data sovereignty |
| **Plausible** | Minimalism, cookieless, EU-hostable |
| **Piwik PRO** | An enterprise privacy twin |

## Technical details

- **Measurement**: gtag.js/GTM, server tags; consent signals
- **APIs**: Data API v4 (report retrieval), Management API (administration), export (BigQuery)
- **Models**: property → streams → events/dimensions; user ID optional (settings!)

## Who it suits

- Teams with legally compliant consent infrastructure and a Google stack
- FreeSynergy frontends: a Data API reader for report frontends (with a duty to give privacy notices)
