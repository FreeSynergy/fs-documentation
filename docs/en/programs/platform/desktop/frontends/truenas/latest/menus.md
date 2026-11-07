# TrueNAS - Menu items

## Overview

TrueNAS (SCALE, current versions) navigates via a **left sidebar** with clearly named areas, a **global search bar** at the top and a **user/system icon menu** at the top right. The order of items changes across major releases (23.10 → 24.04 → 24.10 → 25.x); the basic grouping stays the same. CORE (FreeBSD) shows the same storage items without the apps/VM branches.

## Navigation items (sidebar)

### 1. Dashboard
- **Function**: start page with status cards
- **Details**: pool utilisation, running services, apps, alerts, links; cards can be shown/hidden

### 2. Datasets
- **Function**: dataset tree of all pools
- **Details**:
  - **Create Dataset/Zvol**: wizard (name, case sensitivity, compression, quota, ACL preset)
  - Context actions per dataset: edit, delete, snapshots, clone, encryption, quotas, applications
  - Columns for usage, free, kind (dataset/zvol)

### 3. Pools
- **Function**: pool management
- **Details**: import/export, add, manage (VDEVs), scrub tasks, upgrade, ZFS status messages
- **Disks** (same area or own item, version-dependent): SMART, wipe, SED, overprovisioning

### 4. Shares
- **Function**: share overview with protocol sections
- **Details**: SMB (Time Machine, Samba extras), NFS, iSCSI (targets/extents), S3 buckets, WebShare, FTP (version-dependent); attachments view

### 5. Apps (SCALE)
- **Function**: app catalogue and installed containers
- **Details**:
  - **Discover**: catalogue by category/train, detail page with configuration form
  - **Installed**: status, update, rollback, WebUI link, logs, console
  - **Settings**: app pool, "Docker view", registry access, custom compose

### 6. Virtualization / VMs (from 24.10)
- **Function**: manage KVM VMs
- **Details**: create VM (RAM, CPU, root device on dataset/zvol, bridge), VNC console, cloud-init, ISO selection

### 7. Network
- **Function**: network configuration
- **Details**: interfaces (DHCP/static), VLAN, link aggregation, static routes, DNS; check-in dialogue with countdown against self-lockout

### 8. Services
- **Function**: services table with status/enable
- **Details**: SMB, NFS, iSCSI, SSH, SNMP, WS-DD, FTP; edit dialogue per service (version-dependent: WS-DD, S3)

### 9. Data Protection
- **Function**: backup and replication areas
- **Details**:
  - Periodic snapshot tasks, replication tasks, cloud sync tasks, rsync tasks
  - TrueCloud backup tasks (version-dependent), resilver/scrub settings
  - Snapshot browser for manual snapshots/rollback

### 10. Credentials
- **Function**: access and key material
- **Details**: certificates (CSR, ACME DNS authenticator), SSH key pairs, SSH connections, privileged SSH login, backup credentials (cloud providers), API keys (also via user menu)

### 11. Local Users / Local Groups
- **Function**: accounts and groups
- **Details**: create user (home, shell, SMB/FTP), 2FA reset, AD/LDAP status (directory service)

### 12. Reports / Logs
- **Function**: charts and logs (item names version-dependent)
- **Details**: reporting dashboards (Netdata-based), alert lists, general/audit logs, exporter configuration

### 13. System
- **Function**: system settings
- **Details**:
  - **General**: time zone/country, UI address/port/certificate, language/UI options
  - **NTP**, **Mail**, **Alert Settings/Alert Services**
  - **Advanced**: syslog, init/shutdown scripts, SSH details (version-dependent)
  - **Boot**: activate/clone boot environments (SCALE)
  - **Update**, **Support/Tickets** (community/enterprise, version-dependent)
  - **Failover/HA** enterprise only (version-dependent)

## Icon menu (top right)

- **Jobs icon**: running/completed middleware jobs with progress
- **Bell**: alerts and alert history
- **User icon**: sign out, 2FA, **API Keys** (create/manage), sessions

## Context menus and dialogues

- **Dataset row**: three-dot menu with snapshots, clone, delete, details, applications
- **App card**: open WebUI, update, rollback, redeploy, delete (with data options)
- **Pool card**: manage, export, resize, status messages
- **Job entry**: open logs, cancel (if stoppable)
- **Search bar at the top**: finds menu items, datasets, shares, apps (global search)

## Menus by role

### Admin (default on first start)
- All sidebar items, system/advanced, API key management, update

### Non-privileged user (roles/privileges, version-dependent)
- Visible areas depend on the rights set; no service/system editing

### AD/LDAP group with rights
- Sign-in with directory account, menu scope via assigned roles

### Console/API access
- The console menu on the server offers maintenance points (network, shell, import) independently of UI roles

## Shortcuts

Keyboard operation (forms, search, console menu) is described in [shortcuts.md](shortcuts.md), including the combinations marked as not available.
