# Coppermine - Features

## Main features

- **Categories and albums** with per-album permissions, private albums per user
- **Upload** via web form (multi-step), FTP import ("Add files" mode)
- **Comments, ratings, favourites**, visit and image counters
- **Preview sizes and watermarks**, recalculation via a maintenance function
- **Themes** (layouts) and language files, blocks for page margins
- **Plugin interface** (`plugin_api`) for own extensions and interventions in the flows

## What Coppermine does NOT do

- **No documented REST API** for external clients (❌)
- **No face/object recognition**, no semantic search (❌)
- **No video streaming** (only embedding via a player plugin) (❌)
- **No automatic phone backup** (❌)
- **No modern image editing** (only rotate, crop, watermark) (❌)
- **No responsive default layout** without theme customization (older themes are fixed) (⚠)

## Extensions and integrations

| Integration | Route |
|-------------|-------|
| `plugin_api` | PHP filters/hooks in upload, display and admin flows |
| Themes | Own layouts with templates and CSS |
| Bridge | Connection to a CMS (Joomla, WordPress, bbPress) |
| Import | FTP folders, third-party CSV/batch tools |
| Authentication | Own users, bridge login via the CMS |
