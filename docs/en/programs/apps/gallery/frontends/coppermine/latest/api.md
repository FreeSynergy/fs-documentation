# Coppermine - API Documentation

## Overview

Coppermine has **no documented external API**. Integrations run through the server-side plugin interface (`plugin_api`) and through the theme/template system. For automated access the only route left is via PHP code or the database.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| `plugin_api` (PHP hooks) | Custom logic in upload/display processes | official, server-side |
| Theme/template API | Layout and block control | official |
| REST/JSON for external clients | — | ❌ |
| GraphQL / webhooks | — | ❌ |

## Authentication

- Exclusively the Coppermine session (cookie) or a bridge login via a CMS
- No token or API-key mechanism is present (❌)

## Plugin hooks (selection)

| Hook | Point in time |
|------|---------------|
| `plugin_load` | When the plugin is loaded |
| `page_start` / `page_end` | Around the page output |
| `upload_pre_process` / `upload_post_process` | Before/after the upload |
| `display_image` / `display_thumbnail` | On delivery |
| `cpg_gallery_thumbnail` | When building the thumbnails |
| `admin_config_form` | Extending the configuration form |

Example (a custom hook that reports image metadata externally):

```php
function picture_sync(&$picture_data) {
    $payload = array(
        'pid'    => $picture_data['pid'],
        'title'  => $picture_data['pfilename'],
        'album'  => $picture_data['aid'],
        'url'    => cpg_get_full_image_url($picture_data),
    );
    file_get_contents('https://bridge.example/cpg', false,
        stream_context_create(array('http' => array(
            'method'  => 'POST',
            'header'  => "Content-Type: application/json\r\n",
            'content' => json_encode($payload),
        ))));
}
```

Registration in the plugin: `add_filter('upload_post_process', 'picture_sync');`

## Data access (internal only)

| Table | Content |
|-------|---------|
| `cpg_pictures` | Images, album (`aid`), file name, counters |
| `cpg_albums` | Albums, category (`category`), visibility permissions (`visibility`) |
| `cpg_categories` | Category tree |
| `cpg_comments` / `cpg_votes` | Comments and ratings |
| `cpg_users` / `cpg_usergroups` | Users and permission groups |

Direct database access is prone to breaking on upgrades and should be encapsulated behind your own bridge.

## SDKs and client libraries

- **official**: none
- **Community**: scripts for FTP import, bridge modules for Joomla/WordPress

## Skin note

Because no API exists, the FreeSynergy skin recreates the gallery via its own data storage; the migration fields (`pid`, `aid`) correspond to the standard models ([models.md](../../../../../../data/models.md)).
