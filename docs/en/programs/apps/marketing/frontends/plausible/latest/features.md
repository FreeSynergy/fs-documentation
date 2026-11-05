# Plausible - Features

## Main features

- **one script (~1 KB), no cookies/IP truncation needed** → usually operable without a consent banner (still document the GDPR assessment)
- **Goals/custom events** (`plausible('Spende', {props:{betrag:50}})`), funnels, revenue
- **Stats API**: dashboard metrics over HTTP (filterable) for your own widgets
- Data imports (GA/other tools), GSC keywords, newsletter UTCs
- Self-hosted (ClickHouse + Elixir) or a cloud subscription (EU infrastructure selectable)

## What Plausible does NOT do

- **no visitor logs/single-visitor view** (deliberately!)
- No e-commerce attribution depth (product reports rudimentary)
- No session replays/heatmaps
- User journeys/funnels only via funnel goals (limited complexity)

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| Stats API + events API | official |
| WordPress/Ghost/Shopify integrations | official/community |
| Plausible proxy (`/plausible.io/...` yourself) | The script first-party path |
