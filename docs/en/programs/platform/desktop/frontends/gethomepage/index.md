# gethomepage (Library) Documentation

## Overview

`gethomepage` refers to the **API library layer** of the project `gethomepage/homepage`: the service clients, proxy handlers, configuration readers and helper functions that turn the YAML entries in `services.yaml` into actual HTTP calls to Sonarr, Pi-hole, Proxmox, Docker or Kubernetes. The library has **no user interface of its own** – operation and configuration take place via the dashboard.

## File structure

- [menu.md](latest/menus.md) - Module and package directory of the library (no UI menu)
- [features.md](latest/features.md) - Client functions, handler types, validation, caching
- [description.md](latest/description.md) - Purpose and distinction from the dashboard application
- [structure.md](latest/layout.md) - Library structure, layers and call path
- [shortcuts.md](latest/shortcuts.md) - Build, dev and CLI commands instead of keyboard shortcuts
- [api.md](latest/api.md) - Library API: clients per service, methods, parameters

- [Homepage (Dashboard)](../homepage/index.md) - Application that uses this library
