# GLPI - Menu items

## Main navigation (horizontal, at the top)

| Menu | Content |
|------|---------|
| Assistance | Tickets (self-created/assigned/all), SLAs, contract tickets |
| Assets | Computers, monitors, printers, networks, devices, software, consumables, cables, racks |
| Administration | Users, groups, locations, banks, contracts, licences, documents |
| Tools | Projects, tasks, reminders, knowledge base, statistics reports |
| Configuration | General settings, notifications, SLA contracts, rules (business rules), templates |
| Admin (admin bar at the bottom) | Cron, plugins, API, databases, security logs |

## Assistance area

- **Tickets**: CRUD + search + "mass actions"
- Per ticket tab: properties, links (assets! SLA, problems, changes), tasks, follow-ups, plans, statistics
- Actions: take/handle/solve/close, escalation, assign to groups

## Self-service portal

- "Create a helpdesk ticket" with category tree, watchlist, knowledge base search before submitting
- Own tickets + notifications

## Menus by role

| Role | Rights/menus |
|------|--------------|
| Super-admin | Everything incl. plugins/cron |
| Admin | Configuration without plugin installation (delegable) |
| Technician | Assigned tickets, assets of their own areas |
| Requester | Portal + own tickets |
