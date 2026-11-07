# Heimdall - Menu Items

## Overview

Heimdall works with a start page made of panels and a separate administration view (settings). What is visible depends on whether you are signed in, which role the account has and whether several users are enabled.

## Main menu items

### 1. Dashboard (start page)
- **Function**: central view of all panels with app tiles, statistics and search field
- **Details**:
  - panels one below the other, with tiles inside the panels
  - content is built from the saved apps and panels of the account
  - clicking a tile opens the target URL in the configured target frame

### 2. Manage apps
- **Function**: create, change and remove tiles
- **Details**:
  - **Add app**: title, URL, icon, colour, "open in new tab"
  - **Choose icon**: upload, icon list or automatic adoption of the favicon
  - **Choose enhanced app**: select the service, then enter target URL and key
  - **Edit/delete** existing apps, usually via an edit symbol on the tile

### 3. Edit layout (panels)
- **Function**: move, wrap, hide, delete panels
- **Details**:
  - own edit mode via the settings
  - arrange panels via drag & drop, sort tiles within the panel
  - show hidden panels again
  - changes are saved per account

### 4. Search panel
- **Function**: pass the search term to a search engine
- **Details**:
  - search field on the start page
  - provider configurable (default: Google, further providers to choose from)
  - no internal search index across all apps

### 5. Settings (gear)
- **Function**: configure account and application
- **Details**:
  - **Account**: email address, change password
  - **Users** (newer versions): create users, set role, delete
  - **Layout**: reset panels, rearrange the view
  - **Customization**: custom stylesheets, logo/title (version-dependent)
  - **Support/notices**: show or hide project messages
  - **Update information**: notice about available new versions

### 6. Statistics areas
- **Function**: display CPU, memory, disk and network of the server
- **Details**:
  - values come from the Heimdall machine
  - display as a number with a small chart
  - the area can be hidden if no statistics are wanted

### 7. Account menu (top right)
- **Function**: switch account or sign out
- **Details**:
  - signed-in account, sign out
  - if sign-in is disabled, this item is omitted entirely

## Context menus on panels and tiles

### App tile (normal mode)
- **Left click**: open target
- **Toolbar on hover** (version-dependent):
  - Edit (title, URL, icon, colour)
  - Delete
  - Open in new tab (alternatively via the app setting)

### App tile (layout editing)
- **Drag**: move tile within the panel, snapping to the grid
- **Change panel**: drag tile into another panel
- **Edit**: dialog with all fields of the app
- **Enhanced-app dialog**: service, target URL, API key or username/password

### Panel tools
- **Function**: edit the area as a whole
- **Details**:
  - move (grip zone at the panel edge)
  - wrap into two areas or merge
  - hide and restore
  - delete (with confirmation prompt)

### Icon selection dialog
- **Function**: define the image source for a tile
- **Details**:
  - upload file (PNG/SVG/JPG)
  - search existing icons
  - automatic icon detection via the target URL
  - apply and cancel

## Menus by role

### Administrator
- All menu items including user management
- Create and delete apps, set up enhanced apps and maintain keys
- Edit layout, reset panels
- System settings and update notices

### Signed-in user (standard account)
- Dashboard with own layout
- Apps depending on version only viewable or editable by oneself
- Search field and statistics areas
- Account: password and own layout

### Public / without sign-in
- Only the released dashboard (if set up for public use)
- No settings and administration items
- Apps are read-only; order follows the saved layout

### Operation without login
- If sign-in is disabled, administration appears directly for everyone who can reach the page
- **Security note**: access must then be protected via reverse proxy, network or VPN

## Shortcuts

Heimdall provides no application-specific shortcuts; the usable keys and gestures are listed in [shortcuts.md](shortcuts.md).
