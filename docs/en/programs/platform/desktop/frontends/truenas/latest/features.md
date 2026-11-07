# TrueNAS - Features

## Overview

TrueNAS revolves around the **data layer**: pools, datasets and shares with ZFS tools (snapshots, replication, scrub) as well as the **service stack** (SMB, NFS, iSCSI, SSH …), plus apps and VMs on SCALE. Everything runs through the middleware; web interface, CLI and API are equivalent entry points.

---

## 1. Pools and VDEVs

- **Pool wizard**: VDEV types (stripe, mirror, RAIDZ1/2/3), disk selection, format
- **Pool management**: import/export, expand (add VDEV, replace, detach), scrub jobs
- **SLOG/L2ARC/L2ARC cache** and special VDEVs (version-dependent)
- **Encryption** (dataset or pool level, passphrase/key, KMIP connection in enterprise versions)
- **Disk overview** with SMART tests, temperature recommendations and SED management

## 2. Datasets and ZFS details

- **Dataset tree** per pool with create/rename/delete/clone
- **Properties**: compression, record size, quota/reservation, atime, snapshot inheritance
- **ACL editor** (mix of POSIX and SMB/NFSv4), "Apply to child datasets"
- **Zvols** for iSCSI/VM storage incl. recommended block sizes (version-dependent)
- **Clone, promote, rollback** on snapshot basis

## 3. Snapshots and data protection

- **Periodic snapshot tasks**: schedule, retention schemes, exclude datasets
- **Manual snapshots**, holds, clone, rollback (UI-guided)
- **Replication tasks**: push/pull, SSH key binding, incremental, dedup options (version-dependent), encrypted replication
- **Cloud sync** (S3, B2, Google Drive, OneDrive …), **rsync tasks**, TrueCloud backup (version-dependent)
- **Audit logs** and **scrub** monitoring as separate areas

## 4. Shares

- **SMB**: Time Machine, shadow copies (snapshot-based), presets, ACL modes
- **NFS**: pseudo paths, clients/maps, NFSv3/v4 details
- **iSCSI**: targets, extents (zvol/file), CHAP authentication
- **S3 object storage**, **WebShare** (HTTP access to datasets) and FTP (each version-dependent)
- **Attachments view**: which datasets/disks are used by shares/apps

## 5. Apps and containers (SCALE)

- **App catalogue** (official trains + community trains), custom compose creation (from 24.10)
- **App management**: deploy, update, rollback, logs, consoles, certificates/connection
- **Docker settings**: pool for app images, "Docker features", GPU passthrough (version-dependent)
- **Registry credentials** for private images (version-dependent)

## 6. Virtualisation (SCALE, from 24.10)

- **KVM VMs** in the UI: creation dialogue, zvol/dataset disks, bridge network, VNC console
- **Cloud-init** support and ISO management (version-dependent)
- No cluster, no live migration — single-host virtualisation

## 7. Users, groups, directory integration

- **Local users/groups** with home directory, shell, SMB/FTP flags, 2FA status
- **Active Directory** and **LDAP** as directory source, idmap details (version-dependent)
- **ACL editor** links Unix rights, SMB rights and directory users
- **API keys** per user (roles/privilege roles, version-dependent), session management

## 8. Services, network and system

- **Services overview**: SMB, NFS, iSCSI, SSH, SNMP, WS-DD, FTP … with start/enable toggle
- **Network**: interfaces, VLAN, link aggregation, IPs, DNS, static routes; network check-in dialogue (self-lockout protection)
- **System**: general (time, region, UI HTTPS), NTP, mail, alert settings/alert services, certificates/ACME, init/shutdown scripts, update, boot environments (SCALE)
- **Reporting**: charts (Netdata-based, version-dependent), exporter, alert integrations
- **High availability / failover** only on enterprise hardware (version-dependent)

## 9. What TrueNAS cannot do

- **No VM cluster**: VMs (SCALE) are single-host, no HA/migration like Proxmox VE
- **No mixed array**: ZFS requires planned VDEVs; ad-hoc single-disk expansion like Unraid is not the way
- **No classic monitoring/alerting ecosystem** (Prometheus/Grafana only via exporter connections)
- **No incoming webhooks**; automation is API-pull/CLI-heavy
- **CORE without Docker/VMs** (apps/VMs are a SCALE topic)
- **No autopilot**: computation-intensive ZFS features (dedup) remain workloads reserved for systems with a lot of RAM

## 10. Extensions

- **App trains** (official, community, enterprise) and custom apps via Docker Compose
- **Plugins** only historically in CORE (jail system has been replaced) — migration path to SCALE apps
- **S.M.A.R.T.**, **syslog forwarding**, **SNMP/Graphite/Prometheus** exports (version-dependent)
- **Community tools**: py-nas (Python WebSocket client), Ansible modules `community.general.truenas_*`, dashboard widgets (Homarr/Homepage)
- **Console menu + `midclaw`** for everything the UI does not cover (version-dependent)

---

## Comparison with neighbouring systems

| Feature | TrueNAS | Unraid | Proxmox VE |
|----------|---------|--------|------------|
| File system/array | ZFS (VDEV plan) | mixed array + parity | ZFS/LVM freely selectable |
| Shares | SMB/NFS/iSCSI/S3 (core) | SMB/NFS (shares) | guest/storage only |
| Snapshots/replication | built-in, deep | ❌ (only third-party tools) | snapshots/replication for VMs |
| Apps/VMs | apps + VMs (SCALE) | apps + VMs (licence) | VMs/containers = core purpose |
| API | JSON-RPC v2.0 + CLI | GraphQL (new) | REST `/api2/json` |

---

## See also

- [menu.md](menus.md) - Navigation and dialogues by role
- [structure.md](layout.md) - UI structure, panels, jobs
- [api.md](api.md) - API v2.0, API keys, CLI
- [shortcuts.md](shortcuts.md) - Keyboard operation
