# Desktop — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Desktop` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

## Programs

| Program | Versions | What it is |
|---------|----------|------------|
| [Alfred](alfred/index.md) | [latest](alfred/latest/description.md) | Alfred is a launcher and productivity tool for macOS: a hotkey opens an input field to launch apps, find files, search the web and run actions. |
| [Dashy](dashy/index.md) | [latest](dashy/latest/description.md) | Dashy is a customizable self-hosted dashboard for your own network: app tiles, status indicators, widgets, themes and search are described via `conf.yml` (or JSON) and can optionally be edited in a… |
| [gethomepage (Library)](gethomepage/index.md) | [latest](gethomepage/latest/description.md) | `gethomepage` refers to the **API library layer** of the project `gethomepage/homepage`: the service clients, proxy handlers, configuration readers and helper functions that turn the YAML entries i… |
| [Heimdall](heimdall/index.md) | [latest](heimdall/latest/description.md) | Heimdall is an application dashboard based on Laravel: app tiles, optional statistics tiles and panels form a personal start page for self-hosted services. |
| [Homarr](homarr/index.md) | [latest](homarr/latest/description.md) | Homarr is a self-hosted dashboard for homelabs: services, containers and links are collected in freely configurable boards (widget grids), monitored live and opened with a click. |
| [Homepage](homepage/index.md) | [latest](homepage/latest/description.md) | Homepage (project `gethomepage/homepage`) is a static dashboard for homelabs: services, links and live widgets are rendered from YAML files under `config/`. |
| [Homer](homer/index.md) | [latest](homer/latest/description.md) | Homer is a static dashboard for self-hosted services: a YAML file describes groups and tiles, and a small single-page application renders the start page from it. |
| [KDE Plasma](kde-plasma/index.md) | [latest](kde-plasma/latest/description.md) | KDE Plasma is the free desktop environment of the KDE community. |
| [LaunchBoard](launchboard/index.md) | [latest](launchboard/latest/description.md) | LaunchBoard is a **commercial, proprietary homelab dashboard**: boards are built by drag and drop without configuration files, widgets deliver live data for containers, media and network services, … |
| [OPNsense](opnsense/index.md) | [latest](opnsense/latest/description.md) | OPNsense is a firewall and router distribution (FreeBSD-based, Deciso) with a complete web UI: interfaces, firewall rules (pf), NAT, VPN, services and plugins are configured via menus, with changes… |
| [Proxmox VE](proxmox/index.md) | [latest](proxmox/latest/description.md) | Proxmox VE is an open-source virtualisation platform based on Debian: KVM/QEMU virtual machines and LXC containers are operated through a shared web UI (port 8006, HTTPS) – optionally as a cluster … |
| [Raycast](raycast/index.md) | [latest](raycast/latest/description.md) | Raycast is a keyboard-driven launcher: one search bar that finds applications and files, runs commands and extensions, and offers AI features. |
| [Synology DSM](synology-dsm/index.md) | [latest](synology-dsm/latest/description.md) | Synology DiskStation Manager (DSM) is the proprietary operating system of Synology NAS devices, with a complete **desktop portal in the browser**: main menu, window management, app bar, desktop wid… |
| [TrueNAS](truenas/index.md) | [latest](truenas/latest/description.md) | TrueNAS (iXsystems, formerly FreeNAS) is the open-source storage platform with end-to-end ZFS management: pools, datasets, snapshots, replication and shares (SMB, NFS, iSCSI, S3) are managed via a … |
| [Unraid](unraid/index.md) | [latest](unraid/latest/description.md) | Unraid is a proprietary server operating system for NAS, media and game servers: an array mixes hard drives of different sizes, a dedicated parity drive protects the data, and Docker containers and… |

## File set per program (ADR 0012)

```
programs/platform/desktop/frontends/<program>/
├── index.md        what it is, notable ideas, documented versions, sources
├── changelog.md    changes between documented versions (≥ 2 versions)
└── <version>/
    ├── description.md    required · Detailed description, differentiation, who it suits
    ├── features.md       required · What the program can do — and what not
    ├── layout.md         required · Window structure, regions, panels
    ├── menus.md          required · Menu structure, context menus, menus by role
    ├── shortcuts.md      required · Keyboard shortcuts
    ├── api.md            required · APIs and protocols, authentication, rate limits
    ├── themes/index.md   required · Themes: colours, typography, spacing — what can be rebuilt
    ├── interaction.md    if needed · Hover, focus, drag, gestures (finger, mouse, pen)
    ├── states.md         if needed · UI states and transitions
    ├── events.md         if needed · Events to the outside (webhooks, push, streams)
    ├── limits.md         if needed · Known limitations
    ├── i18n.md           if needed · Localisation, writing direction
    └── dependencies.md   if needed · Which of our components a frontend in this style needs
```

Protocols (Matrix, IMAP, CalDAV, …) are not frontends; they are described under [data](../../../../data/standards.md).
