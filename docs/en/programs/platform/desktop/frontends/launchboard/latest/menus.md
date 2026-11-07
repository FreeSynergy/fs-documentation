# LaunchBoard - Menu items

## Overview

LaunchBoard works with a narrow header bar, a side editor tool and settings dialogs for board, instance and account. Which items are visible depends on the role: **Administrator**, **Editor** and **Viewer** see different menus.

## Main menu items (header)

### 1. Board selection (left)
- **Function**: switch between the boards the user is allowed to see
- **Details**:
  - Dropdown with all shared boards, search by board name
  - Start board can be set per device (desktop/mobile)
  - Administrators and editors: "Create new board" in the same menu

### 2. Edit (right)
- **Function**: change board content: add, move, resize, delete widgets
- **Details**:
  - Visible to administrators and editors; viewers do not see this item
  - In edit mode, the widget library opens as a side panel
  - Changes are saved immediately (no separate "Save" needed)

### 3. Search bar (centre)
- **Function**: find apps, links and boards
- **Details**:
  - Autocomplete with matches from board content
  - Web search via a configurable default search engine
  - Short input patterns (prefix per search engine) possible

### 4. Board settings
- **Function**: display and sharing of the current board
- **Details**:
  - **Layout** tab: columns, spacing, default sizes, reset
  - **Appearance** tab: background image, hue, opacity, blur, icon style
  - **Sharing** tab: public, only own, persons/groups

### 5. Account menu (icon top right)
- **Function**: personal profile and sign-out
- **Details**:
  - Profile, display name, language, time zone
  - Colour scheme: light, dark, system setting
  - Default search engine, start board
  - Two-factor settings (if enabled by the provider)
  - Sign out

### 6. Instance administration (administrators only)
- **Function**: set up the entire instance
- **Details**:
  - **Users**: create, invite, set role, deactivate, profile picture
  - **Groups**: assign boards to groups, bundle sharing
  - **Integrations**: create services, maintain keys, test connection, root certificates
  - **Auth**: configure OIDC provider (issuer, client ID, secret, scopes), header auth, session time
  - **Licence**: subscription status, instance ID, updates
  - **Design editor**: global themes and icon sets
  - **System**: log/event list, trigger backups, restore

### 7. Help and support
- **Function**: documentation, version number, support ticket
- **Details**:
  - Version and build number (important for support requests)
  - Status page of the cloud service (cloud variant only)

## Context menus

### Click on a widget (view mode)
- App tile opens the target URL in the configured frame
- Integration widgets offer their own actions, for example:
  - Container: stop, start, restart, view log
  - Requests: approve or reject
  - Downloads: pause, resume
- Unsupported tiles have no action

### Right-click on a widget
- **Settings** of the tile (only with edit rights)
- **Duplicate** the tile
- **Remove** from the board
- **Open in new tab**

### Floating toolbar (edit mode)
- **Edit**: open the tile's settings dialog
- **Remove**: take the tile off the board
- **Duplicate**: create a tile with identical settings
- **Drag**: grab handle at the top left to move, corner at the bottom right to resize
- **Align**: guide lines and "snap to grid"

### Widget settings dialog
- **Function**: define content, data source and appearance of a tile
- **Details**:
  - Sections: **General** (title, icon, colour), **Data source** (integration, endpoint, fields), **Display** (entries, interval, sorting), **Actions** (target, click behaviour)
  - Footer: Cancel, Test (for data sources), Save, Remove

### Integration dialog
- **Function**: create or change a service
- **Details**: type selection, internal and external URL, credentials, test button with error description, certificate options

## Menus by user role

### Administrator
- Full board view and all edit functions
- Users, groups, integrations, auth/OIDC settings, design editor
- Licence and system area, log, backups
- Manage own root certificates

### Editor
- Create own boards and edit all shared boards
- Select integrations, but cannot open instance settings
- Personal settings, colour scheme, start board

### Viewer
- Only shared boards in read-only view
- No edit button, no right-click tool (at most "Open in new tab")
- Own display settings and sign-out

### Invited user (no account yet)
- Invitation link with expiry date
- Registration or OIDC sign-in, then role according to the invitation

## Shortcuts

The available keys for the editor and navigation are listed in [shortcuts.md](shortcuts.md); commonly expected combinations are marked there as not available.
