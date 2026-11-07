# Homarr - Menu Items

## Overview

Homarr has no classic application menu, but a lean header, an edit tool for boards, and settings dialogs for board, instance and account. Which items are visible depends on the role (administrator, member, guest) and on the board status.

## Main menu items (header)

### 1. Board switcher (left)
- **Function**: switch between the boards the user may see
- **Details**:
  - dropdown with all released boards
  - start board for desktop and mobile can be set separately
  - administrators can also create new boards here

### 2. Search bar (middle)
- **Function**: find apps/links of the boards and web search
- **Details**:
  - autocomplete with matches from the board contents
  - web search with an adjustable search engine
  - shortcut commands (bangs) in the search text possible

### 3. Edit mode (right)
- **Function**: change board contents: add, move, resize, delete widgets
- **Details**:
  - visible only to users with board permission
  - in edit mode a selection of the available widgets appears
  - changes are saved immediately

### 4. Board settings
- **Function**: adjust the appearance of the current board
- **Details**:
  - grid: number of columns, spacing, default sizes
  - look: background image, hue, transparency/blur
  - icon display and labels
  - visibility of the board and shares

### 5. User menu (icon top right)
- **Function**: account, appearance and sign-out
- **Details**:
  - profile and personal settings
  - colour scheme: light, dark, system setting
  - header options, search preferences, first day of the week
  - behavior of right-click on widgets
  - sign out

### 6. Instance settings (administrators only)
- **Function**: manage the entire Homarr instance
- **Details**:
  - **Users**: create, edit, delete, set role, profile picture
  - **Invitations**: create, list, revoke
  - **Integrations**: create services, maintain keys, test connection
  - **Boards**: global board defaults, default grid
  - **Certificates**: store own root certificates to reach internal HTTPS services

## Context menus in the board

### Widget click (normal board)
- App tile opens the target URL in the configured target frame
- Integration widgets offer their own actions, for example:
  - Container: stop, start, restart, open log
  - Requests: approve or reject
  - Calendar: appointment details, open appointment in calendar

### Widget right-click
- **Function**: direct access to tile actions
- **Details**:
  - settings of the tile (only with edit permission)
  - remove or duplicate the tile
  - open link in new tab
  - **Note**: the right-click menu is a personal setting and may be switched off

### Floating toolbar (edit mode)
- **Function**: access to tile tools on hover
- **Details**:
  - **Edit**: open widget settings dialog
  - **Remove**: take the tile out of the board
  - **Drag**: use the upper left corner to move
  - **Drag corner**: change size (grid snapping, snapping to columns)

### Widget settings dialog
- **Function**: define content and appearance of a tile
- **Details**:
  - title, icon, colour, target URL
  - select the associated integration
  - display parameters (entries, interval, sorting)
  - cancel, save, delete

## Menus by role

### Administrator
- Full board rights, all boards visible and editable
- Users, invitations, integrations, global board settings
- Manage own root certificates
- View instance information (version, server information)

### Member
- Create and edit own boards
- View released boards, change them too if edit permission is granted
- Select integrations, but cannot open instance settings
- Personal settings and colour scheme

### Guest / unassigned user
- Only publicly released boards
- No edit button, no integration management
- Own display (colour scheme) and sign-out

## Settings dialogs (structure)

| Dialog | Areas | Typical fields |
|--------|----------|-----------------|
| Widget settings | content, display, integration | title, URL, icon, interval |
| Board settings | grid, look, shares | columns, background, visibility |
| Integration | type, connection, key | URL, API key, connection test |
| User | account, role, rights | name, role, board shares |
| Instance | general, certificates | registration, root certificate |

## Shortcuts

The available keyboard control (dialogs, drag & drop, focus) is described in [shortcuts.md](shortcuts.md), including the keys clearly marked as not available.
