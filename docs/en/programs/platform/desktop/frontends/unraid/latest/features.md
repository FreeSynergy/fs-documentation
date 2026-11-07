# Unraid - Features

## Overview

Unraid revolves around four building blocks: the **array** (storage with parity), **shares and users**, **containers/VMs**, and the **extension marketplace** of Community Applications and plugins. Almost everything is controlled via the tabs of the web interface; the settings are stored as XML on the USB boot medium.

---

## 1. Storage array

- **Mixed drives**: data drives of different sizes/manufacturers in one array
- **Dedicated parity**: one or two parity drives (version-dependent), protection against single or double drive failure
- **Drive-by-drive expansion**: new, larger disks replace the largest data drives
- **Cache pools**: fast SSD/NVMe drives (also ZFS pools, version-dependent) as write and app intermediate layer
- **Parity checks and corrections** as scheduled or manual runs with progress display
- **Start/stop of the array** via the web interface, incl. rebuild mode (array stopped, disks swapped)

## 2. Shares

- **User shares**: folder shares whose blocks are automatically distributed across the array drives
- **Security levels** per share: `public` (without login), `secure` (optional), `private` (login only)
- **SMB and NFS shares** for Windows, macOS and Linux clients; SMB options (VSS/shadow copy, version-dependent)
- **Upstream/downstream behaviour**: new files move to the cache, aged blocks move to the array (version-dependent)

## 3. Users and rights

- **Local users** with passwords, managed in the *Users* tab
- **Samba/Unix rights** underneath, shares with public/secure/private coupled to them
- **WebUI access** distinguishes not signed in, restricted and administrator (version-dependent)
- **Unraid Connect** as an optional account for remote UI, updates and remote diagnostics

## 4. Docker

- **Docker engine** with its own virtual disk (`docker.img`) or directory mode on a pool (version-dependent)
- **Template catalogue** in the *Docker* tab: ready-made app template forms (paths, ports, variables)
- **Container management**: start/stop/restart, logs, WebUI buttons, update check
- **Compose project** for several containers (newer versions, version-dependent)

## 5. Virtual machines

- **libvirt/KVM VMs** in the *VMs* tab: creation wizard, disk, CPU, RAM, network and GPU passthrough
- **webVNC console** in the browser, optionally RDP after installation
- **Licence requirement**: VM functions tied to higher licence tiers (version-dependent)
- **QCOW2/RAW images** on array or cache, snapshots only limited (no image-based backup tool built in)

## 6. Apps and plugins

- **Community Applications (CA)**: searchable store for container templates, plugins and templates
- **Plugin collection** (Dynamix, Drive Buttons, Unassigned Devices, Web terminal, Language/Translations and more)
- **Plugin updates** centrally in the *Plugins* tab; uninstallation usually cleans up
- **Own templates/plugins**: XML-based templates and Bash/PHP plugins, community-driven

## 7. Tools and monitoring

- **System information and logs** in the *Tools* tab (syslog, SMART values depending on plugin)
- **Scheduler**: parity check, mover (cache→array), disk spin-down, own cron (version-dependent)
- **Notifications**: email and **webhooks** for status events (from version 6.12, version-dependent)
- **Dynamix plugins** supply dashboards, themes and status bars

## 8. Configuration

- **XML framework** on the USB stick: `/boot/config` (shares, identification, super metadata)
- **Management access**: HTTP/HTTPS, certificates, port, optional WebUI sign-in
- **Language/themes** via plugins; base UI is primarily English
- **Backups**: copy the USB boot medium (it also contains the licence file) — a defective stick without a backup means reinstallation with licence issues

## 9. What Unraid cannot do

- **No cluster, no HA**: one server, one array — replication across systems is missing by design
- **No classic RAID**: failure of a data drive costs its contents (parity keeps reconstructing), no RAID-10 behaviour
- **No official core REST API** for years; automation ran via files and plugins, today GraphQL (version-dependent)
- **No snapshot/replication tools** like TrueNAS; backups remain reserved for third-party tools or plugins
- **No real multi-tenancy** and no role-based rights like Proxmox VE
- **Proprietary**: source code of the core components not open; licence costs from the trial phase onwards

## 10. Extensions

- **Community Applications** as the central source for containers and plugins
- **Unraid Connect** for registered devices, remote access and update channels
- **GraphQL API and `unraid-api` CLI** in current versions (see [api.md](api.md))
- **Third-party libraries**: `pyunraid` (Python client for the WebUI endpoints), community dashboards with Unraid widgets
- **Own scripts** via `go` hook files (`/boot/config/go`, version-dependent) and init scripts on the stick

---

## Comparison with neighbouring systems

| Feature | Unraid | TrueNAS | Proxmox VE |
|----------|--------|---------|------------|
| Licence | proprietary | open source (enterprise options) | open source (subscription options) |
| File system/array | mixed array + parity, ZFS cache possible | ZFS throughout | ZFS/LVM at node level |
| Docker/apps | CA store, templates | apps catalogue (SCALE) | container support (LXC/Proxmox VE 8, version-dependent) |
| VMs | KVM, single | KVM (from 24.10), single | KVM + LXC, cluster/HA |
| API | GraphQL (new), otherwise files | JSON-RPC v2.0, CLI | full REST API |

---

## See also

- [menu.md](menus.md) - Tabs, dialogues and roles
- [structure.md](layout.md) - Web UI structure
- [api.md](api.md) - GraphQL, API keys, webhooks
- [shortcuts.md](shortcuts.md) - Keyboard operation
