# Piwigo - API documentation

## Overview

Piwigo offers a webservice under `ws.php?method=<name>` (parameters via GET/POST, response XML or JSON). It is used by the official apps and numerous plugins.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| Webservice `ws.php` (`format=php`/`json`) | Categories, images, tags, comments, users | official |
| Plugin hooks (`$events`) | Server-side extensions | official |
| OAuth2 / mobile app endpoints | App access | via plugins |
| GraphQL / webhooks | — | ❌ |

## Authentication

- **REST-like**: `ws_login` provides `pwg_token` + cookie session
- **API-key method**: parameter `format=json` with `check_cookie` session
- **Signatures**: plugin-based (HMAC) for mobile clients; the standard is user/password
- Roles determine the permitted methods (guest/user/webmaster/admin)

## Core methods

| Method | Description |
|--------|-------------|
| `pwg.wsdologin` / `pwg.session.login` | Login, provides a session |
| `pwg.getCategories` | Categories incl. image counts |
| `pwg.getImages` | Images per category, `image_ids`, `per_page`, `page` |
| `pwg.getImagesets` | Sets by tag, date, search, "recent" |
| `pwg.getImage` / `getImageInfo` | Detail with URLs for TH/CU/LI |
| `pwg.addImage` | Upload image (Base64/multipart) |
| `pwg.editImage` | Title, author, status, categories |
| `pwg.deleteImage` | Remove image |
| `pwg.addCategory` / `pwg.editCategory` / `pwg.deleteCategory` | Category tree |
| `pwg.addTag` / `pwg.assignTags` / `pwg.getTags` | Tags |
| `pwg.addComment` / `pwg.getComments` | Comments |
| `pwg.getConfig` / `pwg.setConfig` | Gallery settings (admin) |

## Example

Request:

```http
POST /ws.php?format=json HTTP/1.1
Content-Type: application/x-www-form-urlencoded

method=pwg.getImages&category_id=17&per_page=20&page=1
```

Response (JSON):

```json
{
  "stat": "ok",
  "result": {
    "category_id": 17,
    "images": [
      { "id": 1204, "permalink": "https://galerie.example/photo/1204",
        "representative": { "source": "https://…/CU/IMG_1204.jpg" } }
    ],
    "nb_images": 137
  }
}
```

## Rate limits

No built-in limits; limiting in the web server (`mod_qos`, nginx `limit_req`) and session timeouts are recommended.

## SDKs and client libraries

- **official**: the Piwigo apps (iOS/Android) use `ws.php`
- **community**: Python `piwigo-api`, PHP wrappers in plugin examples
- **imports**: Piwigo export/import, Piwigo Companion for uploads

## Skin note

Category/image/tag/group correspond to the standard model ([models.md](../../../../../../data/models.md)); custom fields follow [fields.md](../../../../../../data/fields.md).
