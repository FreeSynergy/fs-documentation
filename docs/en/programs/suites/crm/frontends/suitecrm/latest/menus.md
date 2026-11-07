# SuiteCRM - Menu items

## Overview

SuiteCRM is operated via a horizontal main menu bar (7.x) or a navigation bar with a module menu (SuiteCRM 8). In addition there is a user menu at the top right and an admin menu that only administrators see. Which modules are visible depends on role, team and access rights.

## Main menu items

### 1. Home
- **Function**: home page with dashlets and personal panels
- **Details**:
  - Add, move and remove dashlets (dashboard edit mode)

### 2. Activities
- **Function**: manage tasks, calls and meetings
- **Details**:
  - Tasks with due date and status
  - Calls as call notes
  - Meetings with participants and reminders

### 3. Leads
- **Function**: capture, qualify and convert prospects
- **Details**:
  - List with status filters (New, Assigned, Converted)
  - Action "Convert" (wizard) creates a contact, a company and optionally an opportunity

### 4. Opportunities (sales opportunities)
- **Function**: track deals with stage, amount and close date
- **Details**:
  - List filterable by sales stage, owner, open/closed
  - Detail area with subpanels: involved contacts, products, notes, activities

### 5. Contacts and companies (Contacts, Accounts)
- **Function**: master data on persons and organizations
- **Details**:
  - Subpanels for relationships (company, opportunities, cases, activities)
  - Import, export and mass actions

### 6. Support (Cases, Bugs)
- **Function**: track customer requests and errors
- **Details**:
  - Case status: New, Assigned, In Progress, Closed, Rejected

### 7. Communication (Emails, Inbound Mail)
- **Function**: outgoing email, archives and mailbox retrieval
- **Details**:
  - Compose email in the "Emails" module or from a record
  - Inbound mailboxes as modules (configuration in the admin area)

### 8. Sales extensions (Products, Quotes, Campaigns, Projects)
- **Function**: product catalog, quotes, campaigns and projects
- **Details**:
  - Quotes with product lines and PDF output
  - Campaigns with target groups (target lists) and ROI fields

### 9. Reports
- **Function**: create queries via module and field selection
- **Details**:
  - Report library with shared and private reports
  - Group and cross-tab reports, CSV export

### 10. User menu (top right)
- **Function**: own account and display
- **Details**:
  - My profile, my settings (password, language, theme, dashboard)
  - Log out

### 11. Admin menu (administrators only)
- **Function**: manage the instance
- **Details** (selection):
  - **Studio**: customize fields, labels and layouts
  - **Module Loader**: install and remove extensions
  - **Security Suite / users and roles**: accounts, teams, rights
  - **Locale and currency**: translations, formats, time zone
  - **Scheduler**: scheduled jobs, cron check
  - **Workflow**: automation rules
  - **Email setup**: outbound accounts, inbound mail server
  - **Repair / clear cache**: maintenance after updates

## Context menus

### Actions menu in list view
- Edit, duplicate, delete
- Mass actions: assign, mark as campaign target, export, duplicate check
- Apply "Filter" and "Saved Filters"

### Detail view
- Edit, duplicate, delete, view history
- Subpanel menu: add entry, link existing entries, remove relationship

### Dashboard
- Add dashlet (list of available dashlets)
- Configure dashlet, close it, change its order

### Right-click
- **Not available**: SuiteCRM offers no right-click menus; actions are in buttons and dropdowns

## Menus by user role

### Administrator
- Full admin menu (Studio, Module Loader, Security Suite, Scheduler, email setup, repair)
- All modules with access rights "All" (own, team and foreign records)
- Create and share reports; maintain roles and teams

### Editor (standard user with "Team"/"Own" rights)
- Module menus for leads, contacts, accounts, opportunities, activities, cases
- Edit own and team records; read foreign records only (depending on rights)
- Dashlets on own home page, private saved filters
- No admin menu, no Module Loader, no Studio

### Reader (view rights only)
- Lists and detail views visible, no edit button
- Run reports, but do not save own reports
- Own dashlets and personal settings still possible

## Shortcuts

SuiteCRM does not publish its own shortcut list. The keyboard controls that are actually usable (Tab, Enter, Esc, browser keys) and the shortcuts explicitly marked as missing are listed in [shortcuts.md](shortcuts.md).
