# Node-RED - Menu items

## Header menu (☰)

| Entry | Content |
|---------|--------|
| Flows | Import/export (JSON), library, collections, undo history |
| Manage palette | Manage palette: installing/updating nodes |
| Manage context | Show flow/global context (JS scope) |
| Configuration nodes | Commons (HTTP port, MQTT broker, serial…) |
| View | Zoom, grid, sidebar toggles, dark theme |
| Appearance | Node sizing/labels |

## Node context menu (right-click)

- Disable/enable, delete, cut/copy, "Trigger node", docs (help panel), set subflow boundaries

## Sidebar tabs (right)

| Tab | Content |
|-----|---------|
| Info | Node docs, node information |
| Debug | Message stream (debug node outputs) |
| Config nodes | Instances of shared configuration |
| Dashboard | UI builder for dashboards (group/page/widget) |

## Node palette (left, categorized)

common (inject, debug, function, switch…) · network (http, mqtt, websocket) · sequence · parser (json, csv, yaml) · storage · analysis · social — plus community palettes.

## Menus by role

Node-RED has no user roles in the core (deployment protection: `adminAuth` in `settings.js`, reader/writer).
