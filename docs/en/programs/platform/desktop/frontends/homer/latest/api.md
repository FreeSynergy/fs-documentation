# Homer - API Documentation

## No official API

Homer is a **static page without a backend**. There is no REST, GraphQL or WebSocket interface, no authentication, no API keys and no webhooks. Homer only provides files and evaluates the configuration in the browser.

**What Homer delivers**

| Method | Endpoint | Description |
|---------|----------|--------------|
| `GET` | `/` | Base HTML page (`index.html`) |
| `GET` | `/assets/config.yml` | The complete dashboard description (readable by anyone who can reach the page) |
| `GET` | `/assets/<name>.yml` | Further configurations, addressable via `?config=<name>.yml` (newer versions) |
| `GET` | `/assets/icons/<file>` | Custom icons |
| `GET` | `/assets/<css-file>` | Custom stylesheet |
| `GET` | `/assets/js/…` | JavaScript of the single-page application |

> These are file retrievals, not API endpoints. There are no response formats, no status codes for domain errors and no versioning.

## Authentication

- **None.** Homer does not ask for credentials and knows no sessions.
- Protection only upstream: Basic auth in the web server, forward auth with Authelia/Authentik, IP filter, VPN or network segmentation.
- **Important**: `assets/config.yml` is also public without this protection. The file contains internal host names and port numbers.

## The configuration file as interface

`assets/config.yml` is the only place where Homer is "controlled". It is loaded when the page is called, but is **not** part of an API: there is no writing, no check by a server and no response message.

### Loading and variants

| Mechanism | Description |
|-------------|--------------|
| Standard path | `assets/config.yml` is loaded automatically |
| Query parameter | `https://home.example/?config=team.yml` loads a different file (newer versions) |
| Download button | `download-config` makes the active file available for download |
| Volume in the container | file can be exchanged without rebuilding the image |
| Templates in the image | the official image creates a template if no configuration exists (switch `INIT_ASSETS`, version-dependent); placeholders from environment variables are replaced at start (version-dependent) |

### Configuration fields

| Field | Type | Description |
|------|-----|--------------|
| `title` | Text | Heading of the page |
| `subtitle` | Text | Line below the title |
| `document-title` | Text | Title in the browser tab |
| `logo` | Path/URL | Image on the left in the header |
| `icon` | Path | Favicon |
| `header` | Switch | show/hide header |
| `footer` | Text/HTML | Footer |
| `links` | List | Icon links at the top right (`name`, `icon`, `url`, `target`) |
| `columns` | Number/text | Number of columns and width behavior (details version-dependent) |
| `theme` | Text | light or dark base scheme |
| `stylesheet` | List of own paths | custom CSS |
| `search` | Switch | search field on/off |
| `message` | Object | texts for loading, error and offline state |
| `download-config` | Text/switch | download of the own configuration |
| `apps` | List | groups with `name`, `logo`, `class` and the `services` they contain |

### Fields of a tile (`services`)

| Field | Type | Description |
|------|-----|--------------|
| `name` | Text | visible name |
| `url` | URL | target of the link |
| `icon` | Text/path | symbol from icon set, own file or URL |
| `target` | Text | `_blank`, `_self` etc. |
| `keywords` | List/text | additional search words, format version-dependent |
| `tag` | Text/object | small marker on the tile (colour definition version-dependent) |
| `type` | Text | display type for extended tiles (newer versions) |

### Complete example

```yaml
title: "Homelab"
subtitle: "Our start page"
document-title: "Homelab"
logo: "assets/logo.png"
icon: "assets/icons/favicon.png"
header: true
footer: "<p>As of: today</p>"
columns: "4"
theme: light
stylesheet:
  - "assets/styles.css"
search: true
message:
  offline: "No connection"
  error: "Configuration could not be loaded"
  loading: "Loading …"
links:
  - name: "Git"
    icon: "fab fa-git-alt"
    url: "https://git.local"
    target: "_blank"
apps:
  - name: "Media"
    logo: "assets/icons/media.png"
    class: "fa-solid fa-photo-film"
    services:
      - name: "Jellyfin"
        url: "https://jellyfin.local"
        icon: "sh-jellyfin"
        target: "_blank"
        keywords: "[film, series]"
        tag: "active"
      - name: "Radarr"
        url: "https://radarr.local"
        icon: "sh-radarr"
  - name: "Network"
    services:
      - name: "Router"
        url: "http://192.168.1.1"
        icon: "fas fa-network-wired"
```

## Examples with curl

```bash
# View the built-in configuration (only sensible with proxy protection)
curl -s https://home.example/assets/config.yml

# Load an alternative configuration (parameter takes effect on the page)
curl -s "https://home.example/?config=team-a.yml"

# Check own CSS file
curl -sI https://home.example/assets/styles.css
```

Expected response: YAML text with HTTP status `200`; if the file is missing, the web server returns `404`. There is no structured error message as with an API.

## Request/response examples (extended display types)

If a tile shows values from a foreign endpoint, that endpoint is **foreign infrastructure** — Homer only provides the display. Typical sequence (version-dependent):

```bash
# Own endpoint whose value should appear in a tile
curl -s https://grafana.local/api/health
```

```json
{
  "database": "ok",
  "version": "11.2.0"
}
```

In the tile, a path to a field is given via configuration; the exact field name can be found in the documentation of the Homer version in use.

## Rate limits

- **Not applicable**: Homer generates no requests to a service of its own.
- Limiting and caching happen in the web server or CDN (cache headers for `assets/`, HTTP/2, compression).
- For extended display types the rate limit of the **foreign** endpoint applies; intervals that are too short burden those systems.

## Webhooks and internal eventing

- **Not available.** Homer sends no events and receives none.
- The display is updated by reloading the page.
- Automation runs entirely outside: Git commit, pipeline, file exchange, then reload.

## SDKs and client libraries

- **Not available.** There is no library to control Homer.
- Integration routes are files and deployment:
  - **Git repository** with `config.yml` and icons, changes via pull requests
  - **CI/CD** that copies the files into the target folder, into the volume or into a bucket
  - **Container volume** that exchanges `assets/config.yml` without changing the image
  - **Multiple files** (`?config=`) to separate teams or devices

## Security notes

- Protect `assets/config.yml` from access from the internet, or deliberately treat it as public.
- Activate `download-config` only if the configuration may be shared.
- Do not write secrets (API keys, passwords) into the file — it is readable.
- Continue to secure protected services with single sign-on or proxy auth; Homer replaces none of this.

## See also

- [menu.md](menus.md)
- [features.md](features.md)
- [description.md](description.md)
- [structure.md](layout.md)
- [shortcuts.md](shortcuts.md)
