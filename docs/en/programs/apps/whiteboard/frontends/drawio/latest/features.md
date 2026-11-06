# draw.io - Features

## Overview

draw.io follows the classic drawing-program layout: menu bar, shape library on the left, formatting panel on the right, canvas with pages below. The features divide into drawing tools, shape libraries, the object model, collaboration, files/export and embedding.

---

## 1. Editing and canvas

- **Pages**: several pages per file, tabs at the bottom, their own background colours (Extras > Pages)
- **Grid and guides**: magnetic snapping, orange alignment lines, page margins
- **Connection points**: shapes show inlets/outlets on hover; edges run orthogonally or curve-based
- **Line jumps**: crossing lines create visible arcs
- **Grouping and containers**: shapes can contain other shapes (groups, swimlanes, frames)
- **Style editor**: every shape style is a readable style string (`rounded=1;fillColor=#dae8fc;...`)

## 2. Shape libraries

- **Standard folders**: General, Arrows, Basic, BPMN, Flowchart, UML, Network, Mockup, ER
- **Cloud and vendor sets**: AWS, Azure, GCP, Kubernetes, Cisco, Citrix, F5, NetApp, OpenStack, VMware
- **Switching** via "More shapes" at the bottom left; libraries are collapsible
- **Own shapes**: create from SVG/PNG and store in the personal sidebar
- **Shape search**: the search field at the top left finds shapes across all active libraries

## 3. Object model (mxCell)

- A diagram consists of cells: `vertex` (shapes), `edge` (connectors) and cell labels
- Edges reference `source` and `target` and move along when shapes are moved
- Parent relationships form groups and containers (`parent` attribute)
- Style as a string, geometry as a rectangle (`x`, `y`, `width`, `height`) in the XML
- **Data attachments**: cells can carry custom attributes (Edit > Edit Data) — useful for evaluation and generated diagrams

## 4. Real-time synchronisation and collaboration

- **Realtime Sync** (Extras menu): all editing steps of a cloud file are seen together (version-dependent)
- **Versions** (File > Versions): history of the cloud storage, comparison and restoration
- Permissions come from the storage (Google Drive, OneDrive, GitHub): whoever may change the file may change it
- No end-to-end protection: the content sits readable with the storage provider unless encrypted

## 5. Files and export

- **Format**: `.drawio` or `.xml` (optionally compressed), `.drawio.png`/`.drawio.svg` with embedded diagram
- **Export**: PNG, JPEG, SVG, PDF, HTML, XML, VSDX (import and export for Microsoft Visio files)
- **Auto-save** can be enabled for cloud storage
- **Printing** including page-break preview; "paginating" large diagrams

## 6. Embedding and plugins

- **iframe embedding**: `https://embed.draw.io/?embed=1&proto=json` with a documented postMessage exchange (load, save, export)
- **URL parameters**: reduce the interface (`chrome=0`), theme, libraries, dark mode — list in the official FAQs
- **JS plugins**: own scripts that extend the editor at runtime (repository examples included)
- **Integrations**: draw.io apps for Confluence and Jira, GitHub/GitLab editing via link

## Configuration

- **Additional configuration**: JSON objects for storage keys, allowed services and UI options (Configure page of the self-hosted instance, `configure.js` for the desktop/web app)
- **Storage client keys**: your own Google/Microsoft/Dropbox OAuth client for productive environments
- **Appearance**: light/dark theme (version-dependent), language via Extras
- **Desktop version**: file associations and auto-update via the Electron settings

### Data and automation

- Cell attributes as data attachments (Edit > Edit Data)
- **CSV/XML import**: generate diagrams from tables (Extras menu, version-dependent)
- Batch export via the desktop CLI for CI pipelines
- Style defaults for organisations via configuration files

---

## Comparison with the neighbours

| Criterion | draw.io | Excalidraw | tldraw |
|-----------|---------|------------|--------|
| Style | technically exact | hand-drawn | clean, quick |
| Format | XML (`.drawio`) | JSON (`.excalidraw`) | snapshot JSON |
| Shape libraries | very large, cloud sets | small + libraries | basic shapes, extensible via SDK |
| Collaboration | Realtime Sync (cloud) | E2E-encrypted rooms | sync server/cloud (SDK) |
| Public API | ❌ (embedding/CLI) | ❌ (file/SDK) | ❌ (SDK/sync) |
| Role | standard diagrams | sketches | building block for your own apps |

---

## What draw.io does NOT do

- **No moderation**: no voting, timers, comments in the board (that is what Miro offers)
- **No public REST API**: diagrams are controlled via files, embedding and plugins (see [api.md](api.md))
- **No webhooks**: changes do not emit external signals
- **No sketch style**: the canvas is technical, not handwritten (that is Excalidraw)
- **No permission management in the app**: roles come from the cloud storage
- **No end-to-end protection**: files sit readable with the storage provider
- **No true multi-canvas**: draw.io thinks in pages, not whiteboards (little freehand, no sticky-note culture)

## Modules and integrations

- **Google Drive / OneDrive / Dropbox / GitHub / GitLab / Trello**: direct save and open dialogs
- **draw.io for Confluence and Jira**: diagrams as attachments directly in Atlassian pages
- **GitHub Actions workflows** (community): automatic PNG/SVG export from repositories
- **Community CLI tools**: batch export and conversion (details in [api.md](api.md))

## Extensions and plugins

- **Plugin API (JavaScript)**: menus, actions and automation at runtime; examples in the source folder `plugins/`
- Define **your own shape sets** as `.shape` files
- Provide **styles and themes** via configuration files (organisational defaults)
