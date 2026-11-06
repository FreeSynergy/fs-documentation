# Redmine - Menu items

## Overview

Redmine navigates the classic way: a header line with main tabs and a search field,
below it a breadcrumb bar and project tabs, on the right optionally a margin column.
Menus are strongly role-dependent; admins additionally see the "administration" tab.

## Main menu items

### 1. My page
- **Function**: personal start page
- **Details**: block layout (administrative, projects, documents, news, activities); block choice under "options"; newer versions with "my activity"

### 2. Projects
- **Function**: list of all projects (with search)
- **Details**: columns name, description, status; checkboxes for subprojects and "public"; new project (admin permission)

### 3. Administration (admins only)
- **Function**: instance administration
- **Details**:
  - users, groups
  - projects, roles and permissions
  - issue trackers, issue status, workflows, issue fields (custom fields)
  - enumerations (priorities, activities, time-tracking activities)
  - boards (forums), reports
  - e-mail notifications, authentication (password/LDAP), sessions (newer versions)
  - plugins, info

### 4. User menu (top right)
- **Function**: own account
- **Details**: my account, friendships/activities, settings (notifications, notification feed), sign out

### 5. Help link
- **Function**: context help
- **Details**: shows a red help/version mark by default; target configurable (text/URL)

### 6. Search field (header line, right)
- **Function**: global search
- **Details**: search term, optionally "search titles", filter per document type after the results are shown

### 7. Breadcrumb bar (project)
- **Function**: to the start of the project
- **Details**: project name as a link to the project overview

### 8. Project tabs
- **Function**: modules of the open project
- **Details** (names/order per version):
  - overview
  - activity
  - roadmap
  - issues
  - time tracking
  - news
  - documents
  - files
  - wiki
  - calendar
  - boards
  - settings (project admin)

## Context menus

### Issue page
- Links: edit, add a note, history, watch, delete (permission-dependent)
- Top: change status via edit, "jump to issue", predecessor/successor
- "Edit" opens an inline form with a status field and a note field

### Issue lists
- Column headers: sort, group (via list options), column choice
- Top: filter bar with "+ add filter", save/publish query, CSV export, Atom feed

### Wiki
- Tabs "edit page", "history", "attach"; "compare changes" in the version comparison

### Time tracking
- "Log time" per issue; evaluation via "reports" in the time-tracking module

## Menus by user role

### Administrator
- All project tabs plus administration (see above)
- Project settings, member administration, module selection

### Editor (e.g. developer/reporter)
- issues: create, edit, change status per workflow, notes, book time
- wiki, boards, files depending on project module permissions
- "my page", global search, save own queries (permission "manage issue queries")

### Reader / anonymous user
- read-only access to enabled public projects
- no "edit" and "new issue" buttons
- anonymous use only if allowed in authentication

## Notes

- Tabs and labels follow the installation language (German fully translated)
- Plugins bring in additional tabs and menu items (e.g. kanban, Gantt)
- Switching project modules off removes the associated tabs for all roles
