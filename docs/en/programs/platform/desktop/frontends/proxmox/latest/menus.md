# Proxmox VE - Menu items

## Overview

Proxmox VE works with a **resource tree on the left** and **tabs in the main area on the right**. The tree follows the order datacenter → nodes → VMs/containers → sub-objects. Which branches and tabs are visible depends on rights (roles/ACL) – read-only users see menus without action buttons.

## Datacenter level

### 1. Datacenter → Summary
- **Function**: overall view of nodes, VMs, containers, resources
- **Details**: search field, tags, filters, columns (status, IP, uptime … version-dependent)

### 2. Datacenter → Cluster / Corosync
- **Function**: cluster composition and quorum
- **Details**: nodes, vote devices (version-dependent), cluster status

### 3. Datacenter → Permissions
- **Function**: rights management
- **Details**:
  - **Users**: create/lock, realm, password, 2FA
  - **Realms/Domains**: pam, pve, ldap, ldap2, ad, keycloak (version-dependent)
  - **API Tokens**: token per user, rights, expiry, node binding
  - **ACL/Roles**: distribute rights on pools, nodes, VMs

### 4. Datacenter → Storage
- **Function**: create storage pools and assign them to nodes
- **Details**: type (directory, LVM-thin, ZFS, CIFS, iSCSI, RBD, PBS …), content types, assignment

### 5. Datacenter → Backup / Replication
- **Function**: backup jobs (vzdump/PBS) and replication jobs
- **Details**: schedules, storage, retention, email; replication with retention and snapshots

### 6. Datacenter → HA (Resources, Groups, Status)
- **Function**: high availability management
- **Details**: add resources, groups, fencing mode, status display

### 7. Datacenter → Ceph
- **Function**: Ceph cluster management (version-dependent, only when Ceph is used)
- **Details**: Mon, OSD, pools, RBD, dashboard links

### 8. Datacenter → Metric Server / Firewall / Subscription
- **Function**: metric export (InfluxDB/Graphite), firewall defaults, subscription status (version-dependent)
- **Details**: tab per topic as with nodes/guests

## Node level (example `pve1`)

### 9. Node → Summary / Console / System
- **Function**: node status, shell, basics
- **Details**: load, uptime; **Shell** (xterm.js) = real Linux shell in the browser; System: subscription, support, certificates, settings

### 10. Node → Network
- **Function**: bridges, bonds, VLAN, SDN, DNS
- **Details**: Network tab (vmbr-, bond objects), DNS, SDN (zones, IPAM, version-dependent)

### 11. Node → Storage / Disks
- **Function**: local storage and block devices (version-dependent)
- **Details**: create ZFS/LVM pools, disk SMART, iSCSI discovery

### 12. Node → Backup / Replication / Snapshots
- **Function**: node-local jobs and point-in-time replicas
- **Details**: like datacenter jobs, but filtered to the node

### 13. Node → Software / Updates / Services
- **Function**: repositories, package updates, system services (since 8.2, version-dependent)
- **Details**: Repositories tab (Enterprise/No-Sub/Test), updates (package list), services (restart)

### 14. Node → Firewall / Terminals
- **Function**: node firewall, console, KVM console of the host
- **Details**: rules, aliases, options; **Terminal** and **Shell** separate

## VM/container level

### 15. VM → Summary / Console / Monitor
- **Function**: status, browser console, real-time charts
- **Details**: Console (noVNC/xterm.js), special keyboard actions via the console menu; Monitor: CPU/RAM/network charts

### 16. VM → Hardware
- **Function**: edit VM devices
- **Details**: Add (disk, CD/DVD, network, USB, serial, cloud-init drive), Edit/Detach, CPU/RAM here only in older versions (otherwise Options)

### 17. VM → Options
- **Function**: behaviour and metadata
- **Details**: autostart, boot order, agent, tags, description, migration behaviour, resync

### 18. VM → Backup / Snapshots / Clone / Templates
- **Function**: backup branches on the object
- **Details**: Backup now, Restore; snapshot take/revert; clone (full/linked); convert to template

### 19. VM → Cloud Init / DNS / Firewall / Unmount ISO
- **Function**: guest preparation and security
- **Details**: user/SSH keys/network in cloud-init, DNS suffix, guest firewall, CD-ROM eject

## Context menus and dialogues

- **Right-click in the tree**: copy (ID), further actions depending on the object (version-dependent)
- **Upper button bar**: Start, Stop (emergency), Reboot, Shutdown, Reset, Suspend/Resume, Migrate, Console (dropdown: noVNC/xterm.js/SPICE)
- **Task panel**: running actions as a list, double-click = details
- **Search bar at the top**: finds VMs/containers/nodes by name, ID, tags, IP

## Menus by role

### Administrator
- full datacenter tree, all tabs and buttons

### Read/monitoring role
- tree visible, tabs visible, no start/stop/edit buttons

### VM operator (delegated rights)
- assigned VMs fully, other VMs hidden or only summary

### Console user (VNCProxy)
- console access only to assigned guests

## Shortcuts

Keyboard operation including console keys is described in [shortcuts.md](shortcuts.md); combinations marked as not available are also listed there.
