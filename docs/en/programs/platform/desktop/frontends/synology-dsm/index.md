# Synology DSM Documentation

## Overview

Synology DiskStation Manager (DSM) is the proprietary operating system of Synology NAS devices, with a complete **desktop portal in the browser**: main menu, window management, app bar, desktop widgets, package centre and control panel. Management API access runs via `GET/POST /webapi/entry.cgi` with `SYNO.*` APIs; default ports are **5000 (HTTP)** and **5001 (HTTPS)**.

## File structure

- [menu.md](latest/menus.md) - Main menu, app bar, package centre, role menus
- [features.md](latest/features.md) - Packages, services, rights, backup, monitoring
- [description.md](latest/description.md) - Description and differentiation from Homarr, Heimdall, Homer, Dashy
- [structure.md](latest/layout.md) - Desktop portal, windows, widgets, themes
- [shortcuts.md](latest/shortcuts.md) - Keys in the portal and clearly marked missing combinations
- [api.md](latest/api.md) - `entry.cgi`, `SYNO.API.Auth` with OTP, `SYNO.Core.*`, session handling
