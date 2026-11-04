# Hotjar - Features

## Main features

- **Heatmaps**: click/move/scroll on real pages (delegation for dynamic content), separated per device
- **Recordings**: DOM-based replays (no video — re-construction), filters + "rage clicks/dead clicks" detection
- **Surveys/feedback**: question templates, targeting (URL/behaviour), answers exportable (CSV)
- **Identify API**: bind your own user IDs to sessions (internal test accounts can be marked)
- Masks (CSS selectors) for personal-data fields; consent coupling

## What Hotjar does NOT do

- **no traffic metrics** (put GA/Matomo/Plausible alongside for that)
- **no open raw heatmap API** (results only to the extent of the UI/CSV)
- Replays without input-field contents (masking is the default) — a debugging limit
- Price by pageviews (scaling costs)

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| GTM tag, Identify API | official |
| Zapier, GA linkage | official |
| Matomo (in parallel) | A complementary pattern |
