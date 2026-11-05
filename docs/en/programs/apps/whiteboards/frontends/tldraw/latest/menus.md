# tldraw - Menu items

## Overview

tldraw deliberately has few menus: the left main menu (file), the toolbar at the bottom, the style panel on the right, and a pages/share menu. Everything else runs through context menus.

## Main menu (tldraw logo, top left)

| Menu item | Description |
|-----------|-------------|
| Export document | File as `.tldr` (JSON), PNG, SVG, JSON |
| New project / new page | New file / new page |
| Print document | Print view |
| Preferences | Dark mode, zoom shortcuts, snap behaviour |
| Static image export | PNG/SVG with background/bounds options |
| Toggle debug mode / editor content | Developer aids |

## Share menu (top right)

- **Share…** — create a link (only in the tldraw cloud respectively with a sync server)
- **Duplicate**, **save as**, **rename**, **document metadata**

## Pages menu

- Page list, rename page, duplicate, delete, new page

## Toolbar (bottom, centred)

Select · hand · laser · pen · eraser · arrow · frame · rectangle · ellipse · line · triangle · cloud · note · text · image · bookmark · (your own tools via the SDK)

## Style panel (right, depending on selection)

Colour, fill, line style, size, font, alignment, opacity, release bindings.

## Context menu (right-click)

| Entry | Description |
|-------|-------------|
| Copy / paste / duplicate | Clipboard |
| Bring to front / send to back | Layers |
| Group / ungroup | Grouping |
| Lock / unlock | Locking |
| Add to new page | Move the selection out |
| Align / distribute | Alignment tools |
| Delete | Delete selection |
| Arrow bindings | Edit bindings (for arrows) |

## Menus by role

| Role | What is visible |
|------|-----------------|
| Editor (write right) | all menus |
| Viewer (read-only link) | only navigation/export |
| Owner | additionally sharing/deleting |
