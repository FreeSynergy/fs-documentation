# TrueNAS Documentation

## Overview

TrueNAS (iXsystems, formerly FreeNAS) is the open-source storage platform with end-to-end ZFS management: pools, datasets, snapshots, replication and shares (SMB, NFS, iSCSI, S3) are managed via a modern web UI. CORE is based on FreeBSD, SCALE/24+ on Linux and adds Docker apps as well as (from 24.10) KVM VMs. The API v2.0 speaks JSON-RPC 2.0 over HTTP/WebSocket; in addition there are the CLI `midclaw`/`midclt` and API keys.

## File structure

- [menu.md](latest/menus.md) - Navigation items (dashboard, datasets, shares, apps, system) by role
- [features.md](latest/features.md) - ZFS, shares, apps, VMs, data protection, services
- [description.md](latest/description.md) - Description and differentiation from Unraid, Proxmox VE, Synology DSM
- [structure.md](latest/layout.md) - Sidebar layout, panels, jobs, dialogues
- [shortcuts.md](latest/shortcuts.md) - Keyboard operation (and clearly marked missing shortcuts)
- [api.md](latest/api.md) - API v2.0 (JSON-RPC), API keys, `midclaw`/`midclt`, `truenas-api`
