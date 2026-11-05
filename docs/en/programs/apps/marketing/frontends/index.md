# Marketing Mask Documentation

## Overview

This directory contains the documentation of the programs in this category following the wiki schema: menu items, features, description, structure/UI-UX, keyboard shortcuts and API — seven files per program.

All programs documented here are **not** FreeSynergy in-house developments, but foreign programs whose surface and interfaces are recreated or connected as a mask.

## Included documentation

- [Google Analytics](google-analytics/index.md)
- [Hotjar](hotjar/index.md)
- [Mailchimp](mailchimp/index.md)
- [Matomo](matomo/index.md)
- [Mautic](mautic/index.md)
- [Plausible](plausible/index.md)

## Directory structure

```
docs/de/programs/apps/marketing/masks/
├── index.md              (this file)
├── google-analytics/   (index, menu, features, description, structure, shortcuts, api)
├── hotjar/   (index, menu, features, description, structure, shortcuts, api)
├── mailchimp/   (index, menu, features, description, structure, shortcuts, api)
├── matomo/   (index, menu, features, description, structure, shortcuts, api)
├── mautic/   (index, menu, features, description, structure, shortcuts, api)
└── plausible/   (index, menu, features, description, structure, shortcuts, api)
```

## Content of each documentation

Each program directory contains **seven** files:

1. **index.md** – overview of the program and links to the six detail files
2. **menu.md** – all main menu items, context menus, role-dependent menus
3. **features.md** – main features, what the program can and CANNOT do, extensions
4. **description.md** – description, advantages, differentiation, technical details, target groups
5. **structure.md** – window/page structure, UI/UX, interactions, responsive design, accessibility
6. **shortcuts.md** – all keyboard shortcuts including Mac variants
7. **api.md** – API type, authentication, endpoints, examples, rate limits, webhooks, SDKs

## Notes

- All documentation is written in German
- The content is suitable for users and administrators
- **Keyboard shortcuts are always in the separate file `shortcuts.md`**
- **API documentation is always in the separate file `api.md`**
- Missing features are explicitly marked as not present (❌)

## Related areas

- [Category overview](../) – overview of this program category
- [Wiki masks](../../wiki/frontends/) – reference schema for this documentation
- [Desktop masks](../../../platform/desktop/frontends/) – same file structure
- [Standardised data](../../../../data/) – fields and models for all mask APIs
