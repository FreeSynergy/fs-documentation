# Pipedrive - Menu items

## Overview

Pipedrive is operated through a left navigation bar with the main modules, an action button at the top right, a personal menu and the company setup for administrators. Which items are visible depends on license and rights (admin, regular, restricted). The exact labels change with releases; deviations are version-dependent.

## Main menu items

### 1. Home / Start
- **Function**: daily overview with due activities and personal key figures
- **Details**:
  - List "Due today" and "Overdue"

### 2. Activities
- **Function**: manage tasks, calls and meetings across all objects
- **Details**:
  - Schedule view by day and week
  - Filter by assignee, type, period, object

### 3. Deals
- **Function**: manage sales opportunities in pipeline or list view
- **Details**:
  - **Pipeline view**: kanban with stage columns, drag & drop between stages
  - **List view (grid)**: table with column selection and sorting
  - Filter bar: pipeline, stage, owner, amount range, close period

### 4. Mailbox / Sales Inbox
- **Function**: work the team's shared email address
- **Details**:
  - Assign, reply to and close incoming requests
  - Linked to contact, organization and deal

### 5. Products
- **Function**: maintain the product catalog and view the price overview
- **Details**:
  - Product list with standard price and currency

### 6. Marketing
- **Function**: basic marketing functions of the subscription
- **Details**:
  - Email campaigns to contact lists (plan-dependent)
  - Website visitor tracking (add-on, version-dependent)

### 7. Reports
- **Function**: open pipeline, activity and performance reports
- **Details**:
  - Report library by category
  - Own reports with axis, metric and filter

### 8. More / additional modules
- **Function**: bundle further modules and add-ons
- **Details**:
  - Leads (lead management), workflows/automations
  - Team performance resp. insights, recurring revenue (ARR)
  - Marketplace integrations and webhook management (plan-dependent)

### 9. "Add" action button (top)
- **Function**: create a record type directly
- **Details**:
  - Activity, deal, person, organization, product, lead

### 10. Personal menu (avatar, top right)
- **Function**: own account and notifications
- **Details**:
  - Personal settings, password, two-factor authentication
  - Manage personal API tokens (tab "Personal access tokens")

### 11. Company setup (administrators only)
- **Function**: configure the instance
- **Details** (selection):
  - **Pipelines & Stages**: create pipelines, maintain stages and their order
  - **Custom Fields**: own fields per object type
  - **Workflows**: automation rules
  - **Users and permissions**: licenses, roles, visibility groups
  - **Email settings**: sync, signatures, Sales Inbox mailboxes
  - **Company data, billing and storage**: plan-dependent

## Context menus

### Deal tile in the pipeline board
- Open deal, edit, duplicate, delete
- Change stage (also via drag & drop)
- Open owner and team
- Close as "Won" or "Lost" with a reason prompt

### Deal detail area
- Tabs: overview, activities, files, products/quotes, team & access
- Actions: edit, duplicate, delete, add activity

### Activity
- Mark as done, move, edit, delete
- Change assignee, set reminder

### Filters and lists
- Create, save and share filters
- Select columns, sort, group by stage

### Right-click
- **Not available**: Pipedrive offers no right-click menus; actions are in icon buttons on the tile and in the detail area

## Menus by role

### Administrator
- Full company setup: pipelines, custom fields, workflows, users, licenses, billing
- All objects and all user records visible and editable
- Manage integrations, webhooks and API access

### Regular user (with license)
- Modules: leads, activities, deals, contacts, organizations, products, reports
- Edit own and shared records; create deals in own team
- No company setup, no user management

### Read-only user (restricted)
- View assigned objects; no creation of new core records
- Own activities and notes depending on permissions
- No report management, no configuration, no API access via account token (version-dependent)

## Shortcuts

Pipedrive does not publish a comprehensive shortcut list. The keyboard controls that actually work and the shortcuts marked as missing are listed in [shortcuts.md](shortcuts.md).
