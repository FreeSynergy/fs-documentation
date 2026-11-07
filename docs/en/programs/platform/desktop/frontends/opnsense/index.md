# OPNsense Documentation

## Overview

OPNsense is a firewall and router distribution (FreeBSD-based, Deciso) with a complete web UI: interfaces, firewall rules (pf), NAT, VPN, services and plugins are configured via menus, with changes activated by "Apply". Every UI function follows an MVC pattern and can be addressed via the REST API under `/api/<module>/<controller>/<method>` with API key (Basic Auth).

## File structure

- [menu.md](latest/menus.md) - Menu paths (Firewall → Rules, VPN, Services, System …) by role
- [features.md](latest/features.md) - Firewall, VPN, services, HA, monitoring, plugins
- [description.md](latest/description.md) - Description and differentiation from Proxmox, TrueNAS, pfSense
- [structure.md](latest/layout.md) - Top menu, grids, dialogues, apply flows
- [shortcuts.md](latest/shortcuts.md) - Keyboard operation (and clearly marked missing shortcuts)
- [api.md](latest/api.md) - MVC REST API, API key Basic Auth, `curl` examples
