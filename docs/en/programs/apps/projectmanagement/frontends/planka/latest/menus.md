# Planka - Menu items

## Overview

Planka navigates via a left sidebar with projects and boards, a board header with a
members/actions area, and card dialogs as overlays. Almost all context menus are
dropdown menus with small toolbars; admins and project managers see additional
administration items.

## Main menu items

### 1. Project sidebar (left)
- **Function**: project and board selection
- **Details**:
  - project list with search/quick select (with many projects)
  - boards per project as tabs/sub-items
  - create project (symbol), edit/delete project in the project context menu
  - sidebar collapsible (arrow symbol), width fixed per version

### 2. Project context menu
- **Function**: administer projects
- **Details**:
  - edit project (name, background)
  - administer project managers (who may administer)
  - invite/add members
  - delete project (archiving exists for boards, not for projects - version-dependent)

### 3. Board header (top of the board)
- **Function**: board actions
- **Details**:
  - member avatars: administer board members
  - notification/watch toggle per board
  - board search/filter (label/member filter, version-dependent)
  - board menu (three dots): edit board, change background, archive cards, delete board

### 4. Card dialog (overlay)
- **Function**: open a card in detail (click on the card)
- **Details**:
  - title and description (markdown editor)
  - the card's sidebar: assignees, labels, due date, checklist, attachments, watch, duplicate, archive, delete, card ID/moves info
  - comment field and activity stream (editing chronicle)

### 5. Card context menu (in the list)
- **Function**: quick actions without a dialog
- **Details**:
  - edit, duplicate, move (list/board), assign, set label
  - set due date, archive, delete

### 6. User menu (bottom left)
- **Function**: own account and appearance
- **Details**:
  - profile: change name, avatar, e-mail
  - change password
  - notification settings
  - appearance: light/dark mode (community: toggle; further themes: pro)
  - language (internationalisation), sign out

### 7. Administration area
- **Function**: instance administration (admin role)
- **Details**:
  - create/edit/delete users, grant the administrator role
  - administer API keys per user
  - initial admin creation via environment variables on first start (version-dependent)

## Context menus

### List menu (three dots per column)
- edit list (title), add card
- move right/left
- archive cards, empty list, delete list

### Label administration
- create label (colour, name), edit, remove from board
- label on cards: click on the labels bar in the card dialog

### Attachment menu
- attach a file by drag & drop or picker
- attachment in the menu: rename (title), view/download, delete

## Menus by user role

### Administrator
- user and instance administration (users, roles, API keys)
- all project and board menus, delete/archive everywhere
- webhook administration (community; access via API/admin UI, version-dependent)

### Project manager / editor
- create and edit projects/boards/lists/cards
- administer members and labels, attachments, comments
- no instance administration, no other people's profiles

### Plain member (close to reader)
- read, comment on, watch cards
- move/edit cards only if a member of the board and the board is not read-only (granular read/write roles only as pro guest roles, version-dependent)

## Notes

- Labels follow the chosen UI language (German available)
- Pro features (guest roles, timeline menu item) appear only with a licence
- Planka hides administration actions instead of disabling them — role differences are therefore mainly "menu visible/not visible"
