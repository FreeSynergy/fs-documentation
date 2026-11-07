# Proxmox VE Documentation

## Overview

Proxmox VE is an open-source virtualisation platform based on Debian: KVM/QEMU virtual machines and LXC containers are operated through a shared web UI (port 8006, HTTPS) – optionally as a cluster with Ceph, replication and high availability. The full feature set is accessible via the REST API (`/api2/json`) with ticket or token authentication.

## File structure

- [menu.md](latest/menus.md) - Resource tree, datacenter/node/VM menus by role
- [features.md](latest/features.md) - VMs, containers, storage, network, backup, cluster
- [description.md](latest/description.md) - Description and differentiation from Unraid, TrueNAS, Homarr
- [structure.md](latest/layout.md) - Three-column layout, tree, tabs, consoles
- [shortcuts.md](latest/shortcuts.md) - Keyboard operation (and clearly marked missing shortcuts)
- [api.md](latest/api.md) - REST `/api2/json`, ticket + CSRF, API tokens, `pvesh`, `proxmoxer`
