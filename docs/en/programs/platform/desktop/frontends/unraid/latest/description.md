# Unraid - Description

## Overview

Unraid (Unraid OS, Lime Technology) is a proprietary server operating system that boots from a USB stick and combines network storage, containers and virtual machines in one web interface. The interface works with fixed tabs (Main, Shares, Docker, VMs, Apps, Plugins, Tools, Settings) instead of a desktop portal.

## What Unraid does

Unraid manages an **array of any mix of hard drives**: each data drive keeps its own size, and one (or, with several, multiple) parity drive(s) protect against failures. Capacity can be extended drive by drive. Beyond that, the web interface manages **SMB/NFS shares** (user shares), **users**, **Docker containers** (with template catalogue), **virtual machines** (libvirt/KVM) and a **plugin store** (Community Applications). The configuration is stored as XML on the USB boot medium; newer versions add a GraphQL API with API keys for automation.

## Advantages

- **Flexible array**: any disk sizes can be mixed, capacity-accurate expansion, own parity
- **Everything in one UI**: storage, shares, Docker, VMs, plugins in one system
- **Community Applications**: large, curated catalogue of ready-made container templates
- **Easy entry**: web UI guides through array, shares and apps without configuration files
- **Unraid Connect**: remote access, updates and support diagnostics via the Unraid account
- **API keys and GraphQL**: modern automation foundation in current versions

## Differentiation from other systems

### Unraid vs. TrueNAS
- **Unraid** is proprietary (licence model version-dependent), **TrueNAS** is open source
- **Unraid** uses an mdadm-like array with mixable capacity, **TrueNAS** consistently relies on ZFS
- **TrueNAS** has the deeper data management (datasets, replication, ACL), **Unraid** the more relaxed app/media kitchen

### Unraid vs. Proxmox VE
- **Proxmox VE** is a full-grown virtualisation platform with cluster, Ceph and HA; **Unraid** is a single-server system with a storage focus
- **Proxmox** has a complete REST API, **Unraid** historically none at all and now GraphQL (version-dependent)
- **Unraid** targets media and homelab users, **Proxmox** operators of VM landscapes

### Unraid vs. Homarr/Heimdall
- **Homarr/Heimdall** are dashboards: they only show tiles and status values of other services
- **Unraid** is the system itself; a dashboard can at most integrate Unraid via API
- All three together are common: Unraid operates, the dashboard links and monitors

## Technical details

- **Backend**: Slackware Linux base; web interface as PHP application (webGui/Dynamix), Docker engine and libvirt/QEMU for VMs
- **Database**: no classic database — configuration as XML files on the USB boot medium (`/boot/config`), array metadata on the drives
- **Frontend**: server-rendered HTML pages with forms and tables, jQuery-based details (version-dependent)
- **Authentication**: local WebUI sign-in, Unix/Samba users, Unraid Connect account for remote functions, API keys with roles (`admin`, `connect`, `guest`)
- **Hosting**: bare-metal x86-64, booting from USB stick; web UI on 80/443, SSH optional; licence bound to the hardware (version-dependent)

## Who is Unraid suitable for?

- **Media and homelab users** who want to use many different (mixed) drives with parity
- **Self-sufficient users with app stacks** who want to install Docker applications quickly from templates
- **Single-server operators without a cluster ambition** — for HA clusters and pure storage appliances, TrueNAS or Proxmox VE are the better choice
