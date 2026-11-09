# Snipe-IT

> Category: [resources](../../index.md)

## What it is

Snipe-IT is an open-source IT asset management web app. It records assets, accessories, components, consumables and licences, and who holds them.

## Notable ideas

- **Check-out and check-in**: an item is handed to a person, a location or another asset; while it is out it cannot be assigned again. Check-in returns it to stock or marks it for repair.
- Four item classes with different rules: assets (tagged, individual), accessories (interchangeable), components (parts checked out to assets), consumables (used up, never returned).
- Status labels (undeployable, deployable, archived, pending) say whether an item can be assigned.
- Documented because it is the clearest model for lending things with a return (ADR 0013).

## Sources

- ✅ Snipe-IT overview, https://snipe-it.readme.io/docs/overview, retrieved 2026-11-10
- ✅ Snipe-IT releases, https://github.com/grokability/snipe-it/releases (v8.8.3, 22 Oct; year not shown; requires PHP 8.2), retrieved 2026-11-10

## Documented versions

| Version | Contents |
|---------|----------|
| [latest](latest/description.md) | description, features, layout, menus, shortcuts, api |
