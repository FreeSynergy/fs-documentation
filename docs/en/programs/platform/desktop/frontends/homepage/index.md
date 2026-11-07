# Homepage Documentation

## Overview

Homepage (project `gethomepage/homepage`) is a static dashboard for homelabs: services, links and live widgets are rendered from YAML files under `config/`. The application runs as a Next.js container, ships **without a database** and has **no login of its own** – access protection is handled by the reverse proxy.

## File structure

- [menu.md](latest/menus.md) - Operation and configuration areas (no classic application menu)
- [features.md](latest/features.md) - Widgets, Docker/Kubernetes integration, configuration
- [description.md](latest/description.md) - Description and distinction from Homer, Dashy and Homarr
- [structure.md](latest/layout.md) - Page structure, themes, interactions, performance
- [shortcuts.md](latest/shortcuts.md) - Keyboard control and keys clearly marked as missing
- [api.md](latest/api.md) - Internal `/api/...` proxy endpoints and widget data sources
- [gethomepage (library)](../gethomepage/index.md) - Service client layer behind the widgets
