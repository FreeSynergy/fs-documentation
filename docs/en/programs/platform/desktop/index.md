# Desktop Applications

## Overview

This section contains documentation for various desktop applications and software.

## Frontend documentation

Programs without their own mask directory are documented following the wiki schema (seven files per program: `index`, `menu`, `features`, `description`, `structure`, `shortcuts`, `api`):

→ [Desktop frontends](frontends/index.md)

Documented: **homarr**, **heimdall**, **homer**, **dashy**, **homepage**, **gethomepage**, **launchboard**, **synology-dsm**, **unraid**, **proxmox**, **truenas**, **opnsense**

## Dashboard and start-page systems

- **homarr** - homelab dashboard with widgets and Docker integration
- **heimdall** - personal dashboard with server statistics
- **homer** - static dashboard built from YAML configuration
- **dashy** - extensible dashboard with authentication and widgets
- **homepage** - service dashboard with live widgets
- **gethomepage** - service client library for the widgets of homepage
- **launchboard** - commercial no-code dashboard
- **synology-dsm** - NAS portal with its own REST API

## System surfaces (NAS, virtualisation, network)

These programs also have a desktop-like surface and are documented as a frontend:

- **unraid** - NAS OS with array, Docker, VMs and GraphQL API
- **proxmox** - virtualisation platform with REST API `/api2/json`
- **truenas** - ZFS NAS with apps, VMs and JSON-RPC API v2.0
- **opnsense** - firewall and router with MVC REST API

## Available Systems

- **libreoffice** - Office suite
- **firefox** - Web browser
- **chrome** - Google Chrome
- **thunderbird** - Email client
- **krita** - Digital painting
- **gimp** - Image editor
- **inkscape** - Vector graphics editor
- **blender** - 3D creation suite
- **obs-studio** - Video recording and streaming
- **audacity** - Audio editor
- **shotcut** - Video editor
- **kdenlive** - Video editor
- **vlc** - Media player
- **mpv** - Media player
- **telegram-desktop** - Desktop messenger
- **element-desktop** - Desktop messaging
- **discord** - Desktop app
- **slack** - Desktop app
- **zoom** - Video conferencing
- **skype** - Communication platform

## What is a Desktop Application?

A desktop application is software that runs directly on a computer's operating system. Desktop applications offer:

- Local execution without web connection
- Access to local resources
- System integration
- Native performance
- Offline usage

## Application Areas

- **Productivity**: Office, word processing, spreadsheets
- **Creativity**: Graphic design, video editing, audio editing
- **Communication**: Email, chat, video conferencing
- **Development**: Development tools and IDEs
- **Multimedia**: Media players, image viewers

## Benefits of Desktop Applications

- **Performance**: Native performance without web limitations
- **Offline usage**: Works without internet connection
- **System integration**: Deep integration into the operating system
- **Security**: Better control over data
- **Customization**: Extensive customization options

## Selection Criteria

When choosing a desktop application, consider the following criteria:

- **Features**: Which features are required?
- **Compatibility**: Does it support the operating system?
- **Open Source**: Is the system open source?
- **Ease of use**: How user-friendly is it?
- **Integration**: Integration with other tools
- **Security**: Data protection and security

## Related Categories

- [Messenger](../../apps/messenger/) - Communication and chat
- [Wiki](../../apps/wiki/) - Knowledge management and documentation
- [Project Management](../../suites/projectmanagement/) - Project management

## Quick Start

1. **Select application**: Choose an application based on requirements
2. **Installation**: Download and install the application
3. **Configuration**: Customize and configure the application
4. **First steps**: First steps with the application
5. **Integration**: Integration into existing workflows

## More Information

Further information can be found in the documentation of individual desktop applications.

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysed programs (15), by function, nothing copied (ADR 0012/0013):

- [Alfred](frontends/alfred/index.md) — Alfred is a launcher and productivity tool for macOS: a hotkey opens an input field to launch apps, find files, search the web and run actions.
- [Dashy](frontends/dashy/index.md) — Dashy is a customizable self-hosted dashboard for your own network: app tiles, status indicators, widgets, themes and search are described via `conf.yml` (or JSON) and can optionally be edited in a…
- [gethomepage (Library)](frontends/gethomepage/index.md) — `gethomepage` refers to the **API library layer** of the project `gethomepage/homepage`: the service clients, proxy handlers, configuration readers and helper functions that turn the YAML entries i…
- [Heimdall](frontends/heimdall/index.md) — Heimdall is an application dashboard based on Laravel: app tiles, optional statistics tiles and panels form a personal start page for self-hosted services.
- [Homarr](frontends/homarr/index.md) — Homarr is a self-hosted dashboard for homelabs: services, containers and links are collected in freely configurable boards (widget grids), monitored live and opened with a click.
- [Homepage](frontends/homepage/index.md) — Homepage (project `gethomepage/homepage`) is a static dashboard for homelabs: services, links and live widgets are rendered from YAML files under `config/`.
- [Homer](frontends/homer/index.md) — Homer is a static dashboard for self-hosted services: a YAML file describes groups and tiles, and a small single-page application renders the start page from it.
- [KDE Plasma](frontends/kde-plasma/index.md) — KDE Plasma is the free desktop environment of the KDE community.
- [LaunchBoard](frontends/launchboard/index.md) — LaunchBoard is a **commercial, proprietary homelab dashboard**: boards are built by drag and drop without configuration files, widgets deliver live data for containers, media and network services, …
- [OPNsense](frontends/opnsense/index.md) — OPNsense is a firewall and router distribution (FreeBSD-based, Deciso) with a complete web UI: interfaces, firewall rules (pf), NAT, VPN, services and plugins are configured via menus, with changes…
- [Proxmox VE](frontends/proxmox/index.md) — Proxmox VE is an open-source virtualisation platform based on Debian: KVM/QEMU virtual machines and LXC containers are operated through a shared web UI (port 8006, HTTPS) – optionally as a cluster …
- [Raycast](frontends/raycast/index.md) — Raycast is a keyboard-driven launcher: one search bar that finds applications and files, runs commands and extensions, and offers AI features.
- [Synology DSM](frontends/synology-dsm/index.md) — Synology DiskStation Manager (DSM) is the proprietary operating system of Synology NAS devices, with a complete **desktop portal in the browser**: main menu, window management, app bar, desktop wid…
- [TrueNAS](frontends/truenas/index.md) — TrueNAS (iXsystems, formerly FreeNAS) is the open-source storage platform with end-to-end ZFS management: pools, datasets, snapshots, replication and shares (SMB, NFS, iSCSI, S3) are managed via a …
- [Unraid](frontends/unraid/index.md) — Unraid is a proprietary server operating system for NAS, media and game servers: an array mixes hard drives of different sizes, a dedicated parity drive protects the data, and Docker containers and…

Overview: [frontends](frontends/index.md)
<!-- /gen:frontends -->
