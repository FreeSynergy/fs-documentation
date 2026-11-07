# Unraid - Menu items

## Overview

Unraid has no dropdown menu, but a **horizontal tab bar** at the top of every page: Main, Shares, Users, Docker, VMs, Apps, Plugins, Tools, Settings (order and labels differ slightly by version). In addition there is the icon menu at the top right (notifications, help, Connect, sign out) and, for each tab, its own buttons and dialogues.

## Main menu items (tabs)

### 1. Main
- **Function**: status of system and array at a glance
- **Details**:
  - System identification, update status, sign-in/licence status
  - Array view: parity drive(s), data disks, cache, hot spares
  - Capacity bars per drive and overall; drive icons (colours = status)
  - Buttons: restart array, change PARITY positions, assign additional drives

### 2. Shares
- **Function**: create and manage user shares
- **Details**:
  - Table of all shares with usage, security and share per disk
  - **Add New Share**: wizard with name, security (public/secure/private), include/exclude disks
  - Edit dialogue per share: security, split, minimum free space, quota (version-dependent)

### 3. Users
- **Function**: manage user accounts
- **Details**:
  - User list with description and email
  - Add/edit/delete, set password, validity (version-dependent)
  - Link to SMB/FTP access (version-dependent)

### 4. Docker
- **Function**: containers and basic Docker configuration
- **Details**:
  - Container table: name, path, port, status, WebUI button, logs, update
  - **Add Container**: template search (app store integration) and template form
  - **Docker Settings**: Docker disk or directory mode, container group that can be switched off
  - Compose projects in newer versions (version-dependent)

### 5. VMs
- **Function**: manage virtual machines (higher licence required, version-dependent)
- **Details**:
  - VM list with start/stop/pause/force stop, webVNC console
  - **Add VM**: wizard (RAM, CPU, vDisk type qcow2/raw, bus, network, BIOS/UEFI, start at boot)
  - **VM Settings**: libvirt disk, ISO storage, hypervisor details
  - VM exceptions and driver ISO (virtio) via dialogues

### 6. Apps
- **Function**: Community Applications — store for templates and plugins
- **Details**:
  - Search and categories for application and plugin catalogue
  - Installation dialogues (template → Docker form), updates and error messages
  - Deactivatable maintenance/app mode for forced update steps

### 7. Plugins
- **Function**: manage installed plugins
- **Details**:
  - Installation history with version states, update buttons, remove
  - Plugin configuration pages appear partly as their own tab or settings entry

### 8. Tools
- **Function**: diagnostics and maintenance
- **Details**:
  - **System**: system information, log files, diagnostic dumps
  - **New Permissions**: ACL/rights repair on shares
  - **Startup Procedure / System Profiler**: boot log, device overview (version-dependent)
  - PHP info and web terminal (usually as a plugin)

### 9. Settings
- **Function**: system-wide basic settings
- **Details**:
  - **Management Access**: HTTP/HTTPS, port, certificate, API key, developer options (GraphQL sandbox)
  - **Network Settings**: IP, DNS, workgroup/domain, bridge (version-dependent)
  - **Disk Settings**: spin-down, sleep modes, disk cache behaviour
  - **Scheduler**: parity check, mover, own cron
  - **Identification**: device name, colour scheme, comment
  - **SMB/NFS**: share services and details (version-dependent)
  - **Notifications**: email and webhook dispatch (from 6.12, version-dependent)
  - **Language & Theme**, Docker/VM basic settings, update channel

## Icon menu (top right)

- **Notifications** (bell): event list from the notification service
- **Help/Docs**: link to the official documentation
- **Unraid Connect**: registration status, remote access
- **Sign out** (if WebUI sign-in is enabled)

## Context actions in lists

- **Drive (Main)**: click for details, SMART values, assignment as hot spare/cache
- **Share**: edit/delete, view (browser folder view)
- **Container**: logs, WebUI, update check, terminal/console, remove (keep dialogue for appdata)
- **VM**: start, stop, force stop, pause, webVNC, edit (hardware dialogue), snapshot actions (version-dependent)

## Menus by role

### Not signed in (no WebUI sign-in enforced)
- Full UI visible — therefore sign-in and HTTPS are mandatory in practice

### Restricted user (if set up, version-dependent)
- Read-only views of Main/Shares, no array/settings actions

### Administrator (root/WebUI login)
- All tabs, array control, plugins, settings, API key management, Connect link

## Shortcuts

The available keyboard operation (tab switching via browser, dialogues) is described in [shortcuts.md](shortcuts.md), including the keys clearly marked as not available.
