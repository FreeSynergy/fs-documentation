# Synology DSM - Menu items

## Overview

DSM works like a desktop: an **upper bar** with main menu, search and account, an **app bar** at the bottom edge, **windows** for each application and **desktop widgets** for system status. Which items are visible depends on role and package rights – administrators see control panel and package centre, standard users only the packages they have been enabled for.

## Main menu items

### 1. Main menu (icon top left)
- **Function**: central listing of all installed packages and system functions
- **Details**:
  - Grid of icons, search field in the menu, categories
  - "Pin" moves a program to the app bar
  - **All programs / Edit**: change order, arrange entries
  - Visibility follows the package rights of the group or account

### 2. App bar (bottom)
- **Function**: starting points and open windows
- **Details**:
  - Pinned applications with right-click menu (open, unpin, window list)
  - Running windows show an indicator and title preview
  - The bar can be hidden and set to hide automatically

### 3. Desktop widgets / System Pulse
- **Function**: live system status on the desktop area
- **Details**:
  - Tiles for CPU, memory and network utilisation
  - Volume and storage health, drive status, temperature
  - Notification and task tile, clock/date (scope depends on DSM version)

### 4. Search at the top (Universal Search)
- **Function**: indexed search across shares, packages and settings
- **Details**:
  - Results grouped by type (files, folders, packages, control panel options)
  - Filter by shared folder, type, date
  - Direct actions: open, download, copy path

### 5. Notifications (bell top right)
- **Function**: system, storage and package events
- **Details**:
  - Unread messages, categories, timeline
  - Settings for email/push notification

### 6. Account menu (avatar top right)
- **Function**: personal profile and sign-out
- **Details**:
  - **Sign out**, **close windows**
  - **Personal information**: change password, set up 2FA, email, language, theme choice
  - **Desktop settings**: background, icon size, widget visibility

### 7. Control panel (only with the right)
- **Function**: central system administration
- **Details**:
  - **Users and groups**: accounts, groups, package rights, quotas, domain/LDAP
  - **Shared folder**: create, rights, encryption, recycle bin
  - **File services**: SMB, NFS, AFP, FTP, WebDAV, rsync
  - **Task scheduler**: schedules, scripts, event-driven tasks

### 8. Package centre
- **Function**: install, update, start, remove packages
- **Details**:
  - **Recommended / Categories / Search**, package details and release notes
  - **Installed**: updates, autostart, resources, uninstallation
  - **Manual installation** of a `.spk` file
  - **Settings**: automatic updates, additional package sources, test channel

### 9. Storage manager
- **Function**: storage pools, volumes, drives, cache
- **Details**:
  - Console view with warnings, pool and volume lists, drive details
  - SMART tests, storage analysis, drive buzzer
  - Expand volume, add storage pool, set up cache
  - **Volume/snapshot information** per Btrfs volume

### 10. Quick start (QuickStart)
- **Function**: guided setup and task instructions
- **Details**:
  - Topic blocks "Initial setup", "Remote access", "Backup", "Media"
  - Links to wizards (create share, enable QuickConnect, obtain certificate)

## Context menus

### Desktop right-click
- **Add/remove widgets**, refresh desktop
- **Close/minimise all windows**

### Window title bar
- **Minimise**, **restore/maximise**, **close**
- **Full screen** for certain packages

### File Station
- **Right-click on file/folder**: open, download, download as ZIP, copy, move, rename, delete, share, properties, compress, extract
- **Right-click on empty area**: new folder, upload, tasks, view
- **Share link** with expiry date, password and permission

## Menus by user role

### Administrator (group `administrators`)
- Control panel, package centre, storage manager, log centre, resource monitor
- Users and groups, package rights, firewall, services, update settings
- All shared folders, system settings, configuration restore

### Standard user
- Only packages with an assigned right (e.g. Drive, File Station, Media Server)
- **No** control panel, no package centre, no storage manager
- Own account settings: password, 2FA, language, desktop background
- Access to shares according to ACL

### User with restricted rights
- File Station only on permitted shares, without rename/delete (per ACL)
- No admin tools, no system logs
- Package web interfaces appear only if the group is enabled there

### Guest / application account
- Guest: restricted web access, no administration, no personal settings
- Application account (group `applications`): API/script access, usually without desktop portal rights, but with API permission

## Shortcuts

Keyboard operation in the portal is limited; the complete list, including combinations marked as missing, is in [shortcuts.md](shortcuts.md).
