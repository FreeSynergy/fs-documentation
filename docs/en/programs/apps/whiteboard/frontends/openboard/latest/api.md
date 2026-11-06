# OpenBoard - API documentation

## Overview

OpenBoard has **no API**. The exchange route is the file format: `.obz` archives (ZIP) with SVG pages and metadata — which makes converters/automations outside the program possible.

**API types at a glance**

| Type | Use | Status |
|------|-----|--------|
| `.obz` file format | Export/import, conversion | official (structure stable, weakly documented) |
| PDF export | Presentation/archive | official |
| REST/WebSocket | — | ❌ |
| Webhooks | — | ❌ |

## `.obz` layout (practical)

```
document.obz (ZIP)
├── document.svg / metadata    (page references, title, author)
├── page-1.svg …               (vector elements per page)
└── media/                     (embedded images/PDFs)
```

Tools: unzip → process the SVG (Inkscape, `rsvg-convert`, your own parsers) → repack.

## Example: the PDF chain

```bash
unzip retro.obz -d retro/
rsvg-convert -f pdf -o page-1.pdf retro/page-1.svg
```

## Frontend note

An "OpenBoard skin" in FreeSynergy rebuilds the blackboard UI (page/element) and exchanges `.obz`/SVG — model: [whiteboard elements](../../../../../../data/models.md) page-based rather than canvas records.
