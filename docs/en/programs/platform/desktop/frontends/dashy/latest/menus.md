# Dashy - Menu Items

## Overview

Dashy is controlled mainly via the configuration file; the interface additionally offers a header with navigation, a settings panel for interactive editing, and context menus on tiles. Which items are visible depends on the minimum role and on whether write access is permitted.

## Main menu items (header)

### 1. Title and logo
- **Function**: identifies the start page, often with a subtitle
- **Details**: taken from `pageInfo.title` and `pageInfo.description`; logo optional; clicking returns to the start page

### 2. Page menu
- **Function**: switch between subpages when `pages` are defined
- **Details**:
  - dropdown or bar with name and icon per page
  - each page uses its own configuration file
  - not visible when there is only one page

### 3. Search bar
- **Function**: filter tiles, start a web search, open URLs directly
- **Details**:
  - no focus needed: typing starts the search immediately
  - `Enter` opens the first match or starts the web search
  - shortcut commands (`searchBangs`) are possible
  - clear with `Esc`

### 4. Launchpad
- **Function**: open all tiles from all pages in a grid view
- **Details**:
  - useful when many pages exist

### 5. Switch view
- **Function**: switch between start view, minimal view and workspace
- **Details**:
  - Minimal: without extras, only tiles and search
  - Workspace: one section displayed across a large area

### 6. Edit (the "Edit" button)
- **Function**: start edit mode for tiles and sections
- **Details**:
  - only visible with a sufficient role
  - in this mode, edit and delete icons appear on the objects
  - saving writes to the configuration file
  - can be switched off if the file may not be changed from the interface

### 7. Settings panel (gear)
- **Function**: change the configuration interactively
- **Details** (labels differ by version):
  - **General and layout**: title, description, language, number of columns, density, header/footer
  - **Theme**: choose scheme, adjust colours, custom CSS
  - **Search and status indicators**: search engine, shortcut commands, web search, check interval and expected responses
  - **Interactive editor**: manage sections, tiles and pages
  - **Import/export**: download and upload the file, view backups
  - **Authentication**: notes on users and roles (editing the keys remains reserved for the file/environment)

### 8. User menu
- **Function**: sign in, sign out, two-factor entry
- **Details**:
  - appears only when authentication is configured
  - login page when there is no session
  - signing out ends the session

## Context menus on tiles and sections

### Right-click on a tile
- **Function**: all opening modes and object actions at once
- **Details**:
  - Open in new tab
  - Open in same tab
  - Open in modal
  - Open in workspace
  - Copy URL to clipboard
  - **Edit** and **Delete** (only in edit mode)

### Floating tools (edit mode)
- **Function**: edit, move, duplicate, remove objects
- **Details**:
  - Edit opens the tile dialog (title, URL, icon, colour, opening mode, tags)
  - Dragging the grip zone moves the tile within the grid
  - Sections can be reordered as a whole
  - Changes are written to the file when saved

### Tile dialog
- **Function**: maintain all fields of a tile
- **Details**:
  - `title`, `url`, `description`, `icon`, `target`, `tags`, `keywords`
  - Display options: hide name, compact, colour, border
  - Status check: check URL and expected response, hotkey digit for quick start

### Section dialog
- **Function**: configure a group
- **Details**:
  - name, order, number of columns
  - add and configure widgets of the section
  - add or remove tiles, delete section (with confirmation prompt)

## Menus by role

### Administrator
- Full write rights: editor, import/export, theme editor, create pages
- Manage users and keys (in the file or via environment variables)
- Set status checks and intervals globally
- API write access (Bearer token or admin session)

### Signed-in user
- Start page, search, launchpad, views, right-click menus
- Editing only if the minimum role allows it
- Personal preferences (e.g. active theme) remain local in the browser

### Anonymous (not signed in)
- With configured authentication: only the login page
- Without authentication: full view, but without editing if the editor is locked

### Locked edit mode
- All changes then go via the file, deployment or API

## Shortcuts

The full keyboard control (typing searches, `Tab`, arrow keys, `Enter`, `Alt+Enter`, `Ctrl+Enter`, `Esc`, hotkeys `0`–`9`) is described in [shortcuts.md](shortcuts.md).
