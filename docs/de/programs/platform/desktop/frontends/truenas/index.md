# TrueNAS Dokumentation

## Übersicht

TrueNAS (iXsystems, ehemals FreeNAS) ist die Open-Source-Speicherplattform mit durchgängiger ZFS-Verwaltung: Pools, Datasets, Snapshots, Replikation und Freigaben (SMB, NFS, iSCSI, S3) werden über eine moderne Web-UI verwaltet. CORE basiert auf FreeBSD, SCALE/24+ auf Linux und ergänzt Docker-Apps sowie (ab 24.10) KVM-VMs. Die API v2.0 spricht JSON-RPC 2.0 über HTTP/WebSocket, dazu kommen die CLI `midclaw`/`midclt` und API-Keys.

## Dateistruktur

- [menu.md](latest/menus.md) - Navigationspunkte (Dashboard, Datasets, Shares, Apps, System) nach Rolle
- [features.md](latest/features.md) - ZFS, Freigaben, Apps, VMs, Datenschutz, Dienste
- [description.md](latest/description.md) - Beschreibung und Abgrenzung zu Unraid, Proxmox VE, Synology DSM
- [structure.md](latest/layout.md) - Sidebar-Layout, Panels, Jobs, Dialoge
- [shortcuts.md](latest/shortcuts.md) - Tastatursteuerung (und klar als fehlend markierte Shortcuts)
- [api.md](latest/api.md) - API v2.0 (JSON-RPC), API-Keys, `midclaw`/`midclt`, `truenas-api`
