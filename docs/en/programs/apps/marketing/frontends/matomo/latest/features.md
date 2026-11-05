# Matomo - Features

## Main features

- **full data sovereignty**: events in your own DB (MySQL/MariaDB), raw data export, deletion policies per site
- **Data-protection modes**: cookieless tracking, anonymisation, consent APIs (the consent manager is integrated)
- Reports in depth (visitor log, custom segments, funnels)
- Plugins: heatmaps & session recordings (premium), A/B testing, media analytics
- **Tracking HTTP API**: `matomo.php?idsite=…` — also for server/app/CLI events (device ID controllable)

## What Matomo does NOT do

- No Google suite automation (the Ads coupling is weaker than GA4)
- Session replay/heatmap/tag-manager integration is partly **chargeable** (premium plugins)
- Big data volumes (billions of events) → infrastructure know-how needed (the archive tables do the job)
- Collaboration comfort (comments/sharing) is thinner than the GA environment

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| Analytics REST API (JSON) | official (cloud too) |
| Tag manager (Matomo's own GTM clone) | official |
| WP plugin/shop systems | official |
