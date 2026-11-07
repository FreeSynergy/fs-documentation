# Proxmox VE - Features

## Overview

Proxmox VE consists of four layers: **virtualisation** (VMs, containers), **infrastructure** (storage, network, firewall), **operations** (backup, replication, HA, updates) and **administration** (users, rights, API). The web UI covers all layers; every action also exists in the REST API.

---

## 1. KVM/QEMU virtual machines

- **Creation wizard**: guest OS type, CD/ISO, disk bus, QCOW2/RAW, thin/thick
- **Hardware tab**: CPU type/sockets/cores, RAM + ballooning, network (models, VLAN tag), disks, PCIe passthrough, GPU (version-dependent)
- **Cloud-init** for templates: hostname, user, SSH keys, network configuration
- **Snapshots** (including memory snapshots), **clones** (full/linked), **templates**
- **QEMU agent** for clean shutdowns and IP display
- **Backup mode** per VM: stop, snapshot, suspend (with quiesce, version-dependent)

## 2. LXC containers

- **Unprivileged containers** as default, privileged optional
- **Template download** directly from the UI (Debian, Ubuntu, Alpine, TurnKey …)
- **Resource limits** (CPU, RAM, swap), feature selection (nesting, FUSE, keyctl)
- **Consoles**: browser (xterm.js) and `pct` on the node (version-dependent)
- **Push/pull migration** between nodes (shared storage required; otherwise replication)

## 3. Storage

- **Types**: directory, LVM, LVM-thin, ZFS (+ RAID levels), BTRFS (version-dependent), CIFS/SMB, NFS, iSCSI, RBD (Ceph), Proxmox Backup Server
- **Storage pools** with assignment per node and content type (disk images, ISO, backup, containers)
- **Disk management** in the VM tab: resize, move (storage migration), detach, backup flag
- **IO throttling**, spin-down flags, cache modes per disk

## 4. Network

- **Linux bridges** per node (vmbr0 …), ports, VLANs, bonds (LACP), MLAG (version-dependent)
- **SDN** (virtual network): zones (simple, VLAN, VXLAN, QinQ), IPAM, subnets (since 8.x, version-dependent)
- **IPv4/IPv6 configuration**, DNS, routes via the network tab
- **Firewall** on three levels: datacenter, node, guest (rules, aliases, rate limits, DHCP/RA guard)

## 5. Cluster and high availability

- **Corosync cluster** with pmxcfs (configuration replicated), quorum model, watchdog automation
- **HA manager**: HA resources, groups, fencing, status "stopped/started"
- **Live migration** (online) and resize-oriented offline migration
- **Ceph integration**: create Mon/OSD/MDS via UI, RBD storage, dashboard (version-dependent)
- **Cluster resource overview** with search, tags and filters

## 6. Backup and replication

- **vzdump** in backup jobs (schedule, storage, retention, email) or directly on the object
- **Proxmox Backup Server**: incremental, deduplicating, encryption, restore/verify
- **Snapshots** (VM) and **container snapshots**; **replication** as a schedule with point-in-time copies
- **Restore** to other nodes/storage, incl. "as new VMID"

## 7. Operations and updates

- **Repositories** (Enterprise/No-Subscription/Test), package updates via the *Updates* tab
- **Subscription management**, support info, **subscription reminder** can be switched off
- **Metric server** (InfluxDB/Graphite export) for monitoring access (since 8.1, version-dependent)
- **Notifications** (Notifications tab: matching, .targets mail/Jabber/SMS, version-dependent)
- **Consoles**: node shell and terminal in the UI; `pvesh`, `qm`, `pct`, `pvecm`, `pvesm` on the console

## 8. Users, rights and API access

- **Realms**: `pam`, `pve` (own store), LDAP/LDAP2, AD, Keycloak/OIDC (version-dependent)
- **Two-factor**: TOTP, recovery keys (version depends on release)
- **Roles and ACL** granular down to VM level; pools as rights collections
- **API tokens** with expiry, node binding and rights — basis for scripts and Terraform

## 9. What Proxmox VE cannot do

- **No classic NAS**: file shares (SMB/NFS for clients) are not the core task — storage is managed for VMs, not for users
- **No built-in monitoring stack**: metrics go to external systems (metric server, Netdata integrations), alerts are rudimentary
- **No webhooks**: none documented, neither incoming nor outgoing
- **Live migration only with shared storage**; without Ceph/LVM & Co. only replication helps
- **LXC has no live migration in the classic sense** and no full kernel guest
- **No tenant self-service**: rights yes, but no cloud portal (for that, e.g. external projects)

## 10. Extensions

- **Proxmox Backup Server** and **Proxmox VE Backup** as product family
- **cloud-init**, **QEMU agent**, **qga scripts** for guest automation
- **Infrastructure as Code**: Terraform provider (bpg/proxmox), Ansible collection `community.proxmox`
- **Community tools**: Proxmox Helper Scripts (container/VM templates), pve-exporter for Prometheus, dashboard libraries
- **Own integrations** via the REST API (see [api.md](api.md)) and hooks (version-dependent)

---

## Comparison with neighbouring systems

| Feature | Proxmox VE | Unraid | TrueNAS |
|----------|------------|--------|---------|
| Core task | Virtualisation + cluster | Flexible storage array + apps | ZFS storage + shares |
| VMs | KVM + LXC, cluster/HA | KVM (single, version-dependent) | KVM (single, since 24.10) |
| API | full REST API | GraphQL (new) | JSON-RPC v2.0 |
| File shares | for guests/storage | SMB/NFS shares | SMB/NFS/iSCSI/S3 (core purpose) |
| Cluster | Corosync, HA, Ceph | ❌ | HA only enterprise (version-dependent) |

---

## See also

- [menu.md](menus.md) - Resource tree and tabs in detail
- [structure.md](layout.md) - UI structure and consoles
- [api.md](api.md) - REST API, tokens, `pvesh`
- [shortcuts.md](shortcuts.md) - Keyboard operation
