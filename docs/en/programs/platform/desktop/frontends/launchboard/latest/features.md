# LaunchBoard - Features

## Overview

LaunchBoard combines four building blocks: **boards** (layouts), **widgets** (tiles from a library), **integrations** (service access including key) and **administration** (users, roles, single sign-on, licences). Everything is changed at runtime via the interface and stored in the bundled database.

---

## 1. Boards and layouts

- **Any number of boards** per instance: "Homelab", "Media", "Team", "Mobile"
- **Drag-and-drop grid** with adjustable number of columns, row heights and spacing
- **Move and resize tiles** via handles, snapping to the grid, alignment guides
- **Separate layouts** for desktop and mobile (own arrangement per device)
- **Templates**: ready-made boards (media server, network, server room) as a starting point
- **Duplicate, rename, archive, delete**, and start board can be set per role

## 2. Widget library

### Structural widgets
- **App tile**: name, URL, icon, target window, optional secondary links
- **Link list, text block, image, divider, embed (iframe)**
- **Folder/tab widget** for several links in one tile

### Status and measurement widgets
- **Reachability indicator** (HTTP status, response time) with interval
- **Container status** (running, stopped, healthy) via the Docker integration
- **System values** (CPU, RAM, disk) for host and containers
- **Charts** for traffic and utilisation, based on stored integrations

### Integration widgets (excerpt)
- **Docker / Portainer**: container list with actions (stop, start, restart)
- **Media stack**: Jellyfin/Plex/Emby (active streams), Sonarr/Radarr/Prowlarr (queue, open requests)
- **Downloads**: qBittorrent, SABnzbd, Transmission (speed, queue)
- **Network**: UniFi, OPNsense/pfSense (clients, throughput), Pi-hole/AdGuard (block statistics)
- **Storage**: NFS/SMB shares, usage, SMART values (depending on the provider integration)
- **Calendar, RSS/feed, weather, notes, clock** for information tiles

### Custom content
- **HTTP/JSON widget**: URL, method, headers, JSON path → values from any interface
- **Markdown/note tile** with limited formatting
- **Import/export of a widget definition** as JSON for reuse and exchange

## 3. Integrations and actions

- **Create integration**: choose type, internal/external URL, key or user name/password
- **Connection test** in the dialog with error description
- **Multiple instances** of the same type; widgets select the desired one
- **Actions** from the tile: restart container, pause download, approve request (supported types)
- **Keys stored encrypted** in the database; access via the server, not via the browser
- **Certificates**: store own root certificates to reach internal HTTPS services

## 4. Authentication, roles and sharing

- **Local accounts** with password, registration can be disabled, invitation procedure
- **OAuth2/OIDC**: Authentik, Keycloak, Entra ID, Google, Generic OIDC (issuer, client ID, secret, scopes)
- **Header authentication** behind a trusted reverse proxy (optional)
- **Roles**: Administrator, Editor (may change boards), Viewer (read only)
- **Board sharing**: public, only own, restricted to persons/groups
- **Session settings**: timeout, multiple sign-ins, optional two-factor authentication (scope of provider per plan)

## 5. Design and themes

- **Light, dark and system setting** per account
- **Accent colour, card style, corner radius, blur, opacity**
- **Background images** (upload or URL) per board
- **Icon libraries** and own icon upload
- **Custom CSS field** in the theme editor (scope/availability per licence **not publicly documented**)

## 6. Configuration and operation

- **No configuration file** for content; boards, widgets and users are stored in the database
- **Environment variables for startup** (container variant): port, database path, session/encryption secret, OIDC parameters, licence key
- **Data persistence**: back up the volume for database and uploads; keep the secret stable, otherwise stored keys become unreadable
- **Updates** via container images or automatically in the cloud variant
- **Backups**: database export from the interface plus volume backup recommended

## 7. What LaunchBoard cannot do

- **No configuration as a file**: boards cannot be placed under version control as YAML/JSON (widget export only)
- **No open source code**: no reimplementations, no fork, no custom widget programming in the product
- **No freely viewable API reference**: integrations rely on the customer portal documentation
- **No monitoring replacement**: measured values are snapshots, not long-term curves with alarms (monitoring package or add-on module per plan)
- **No offline operation**: without server and sign-in, nothing is displayed
- **No reverse proxy replacement**: no routing, no certificate management
- **No multi-tenancy**: instance = one community, no multi-customer operation
- **No open plugin system**: the provider supplies new widget types

## 8. Extensions and integrations

- **HTTP/JSON widget** as the official way to reach own data sources
- **Webhooks** (scope per plan): report events from the dashboard to external systems; details in [api.md](api.md)
- **OIDC as a bridge**: existing identities from Authentik/Keycloak/Entra ID without a second account landscape
- **REST interface** for automation (boards, widgets, integrations) – schema in [api.md](api.md)
- **Support and roadmap**: features are contributed via the provider; customers can make requests
- **Data location**: with cloud use, storage location and data processing are regulated contractually (details in the customer portal)

---

## Comparison with other dashboard types

| Feature | LaunchBoard | Homarr | Heimdall | Homer | Dashy |
|----------|-------------|--------|----------|-------|-------|
| Licence | proprietary, subscription | open source | open source | open source | open source |
| Configuration | Drag & drop | Web interface | Web interface + `.env` | `config.yml` | `conf.yml` |
| Database | yes | SQLite | yes | no | optional |
| Roles/sharing | yes (Admin/Editor/Viewer) | yes | limited | no | yes |
| OAuth/OIDC | core feature | yes | no | no | limited |
| Actions | partly | yes | limited | no | limited |
| Support | commercial | community | community | community | community |

---

## See also

- [menu.md](menus.md) - Menu items and operating levels
- [structure.md](layout.md) - Editor interface and panels
- [api.md](api.md) - Interfaces, OIDC and webhooks
- [../homarr/index.md](../../homarr/index.md) - the open-source alternative with mouse configuration
