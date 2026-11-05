# Google Analytics - Features

## Main features

- **Event model** (GA4): page_view, custom events with parameters; web + app in one property
- **Automatic measurement** (engagement, conversions as key events), funnel/explorer reports
- **Audiences** + attribution (data-driven models), Google Ads sync
- **BigQuery export** (free for standard since 2023/24 — check the status!) for raw-data analysis
- **Consent mode v2**: data-protection-controlled measurement (transmitting the consent signal)

## What Google Analytics does NOT do

- **the GDPR is the perennial topic**: document the transfer bases (EU-US DPF); some data protection authorities are negative — Matomo/Plausible are the "safe" paths
- no raw-data sovereignty (the BigQuery binary export yes, but in Google's cloud)
- **no self-hosting option**
- Session-based comparability is limited (sampling in large reports)
- No email contact resolution (ads personalisation is a different product)

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| Data API v4 / management API | official |
| Tag Manager, Search Console, Ads | The Google family |
| Looker Studio | Free dashboards |
