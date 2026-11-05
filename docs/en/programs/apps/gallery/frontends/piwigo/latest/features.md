# Piwigo - Features

## Main features

### Gallery structure
- Categories (albums) of arbitrary depth, one image in several categories
- Status per image: published, pending, private; visibility per group
- Tags, custom fields, description/subtitle, EXIF display

### Presentation
- Themes and templates, configurable start page, slideshow, direct link to full size
- Multilingual support, RTL, RSS, sitemap
- Best rating, counters, comments with moderation

### Administration
- "AddPictures": bring folders from the server into the gallery (sync)
- Batch management: rotate, metadata, categories, tags, delete in series
- Watermark cron, generate sizes (TH/CU/…), import from Picasa/Piwigo export

## What Piwigo does NOT do

- **No face/object detection and semantic search** in the base (only via plugins, then limited) (❌)
- **No phone auto-backup** as a core feature (❌)
- **No video streaming** with adaptive bitrate — video only via a player plugin (❌)
- **No modern photo-cloud timeline** like Immich, the interface is classic web-toolkit design
- **No real image editing** (only rotate, crop, watermark) (❌)

## Extensions and integrations

| Integration | Method |
|-------------|--------|
| Webservice API `ws.php` | official, used by the mobile apps |
| Plugins | >300 extensions (Comment, Metadata, Video-js, Companion …) |
| Companion (app) | official mobile app, upload from role |
| OAuth2/social | login/registration via provider (plugin) |
| Import | Picasa, Piwigo export, FTP/sync folder |
