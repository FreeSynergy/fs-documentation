# draw.io - Description

## Overview

draw.io (also diagrams.net since the rename) is an open-source diagramming application with a classic menu bar, shape libraries and a saveable XML file format. It runs without an account, offline, and in any cloud environment.

## What draw.io does

- Technical diagrams: flowcharts, network plans, UML, BPMN, ER diagrams, mockups
- Huge shape libraries: General, Arrows, BPMN, UML, Flowchart, Network, AWS, Azure, GCP, Kubernetes, Cisco and more
- Files as `.drawio`/XML with embedded graphics in PNG, SVG and PDF; VSDX import/export
- Saving to disk, in the browser, on Google Drive, OneDrive, Dropbox, GitHub, GitLab or Trello
- Real-time collaboration via "Realtime Sync" on cloud files (version-dependent)
- Embedding in third-party applications via iframe (postMessage protocol) and own JS plugins

## Advantages

- **Free and open source**: Apache-2.0 licensed, web app and desktop version are free
- **No account needed**: start locally, data stays in your own file
- **Open format**: XML diagrams are readable, diffable and Git-friendly
- **Depth of shapes**: professional libraries including cloud provider icons
- **Embeddable**: reference diagram feature in Confluence, Jira and your own apps
- **Offline**: the desktop version and browser cache work without a network

## Differentiation from other systems

### draw.io vs. Excalidraw
- **draw.io** produces exact, standards-compliant diagrams with connection points and grids
- **Excalidraw** deliberately sketches in a hand-drawn style
- **draw.io** scores with shape libraries and XML, **Excalidraw** with speed and collaboration encryption

### draw.io vs. Miro
- **Miro** is a commercial team platform with templates, voting, permissions and a REST API
- **draw.io** is a pure drawing tool without facilitation features
- **Miro** stores in its own cloud, **draw.io** in your file or your storage

### draw.io vs. PlantUML
- **PlantUML** generates diagrams from text sources (code as diagram)
- **draw.io** edits diagrams graphically, XML is a by-product
- **PlantUML** is more version-control friendly, **draw.io** is directly manipulable

## Technical details

- **Backend**: the web app is almost entirely client-side; the server itself (Java/Jetty, Docker image `jgraph/drawio`) only serves static files and optional configuration
- **Database**: no database of its own; files live with the user or in the attached cloud storage
- **Frontend**: JavaScript/TypeScript based on the mxGraph library (jgraph's own development)
- **Authentication**: OAuth for cloud storages (Google, Microsoft, Dropbox); the app itself knows no user accounts
- **Hosting**: diagrams.net (official), self-hosted via Docker/WAR, desktop (Electron), embedding via iframe

## Who draw.io suits

- **IT architects and network planners**: cloud icon sets, reference architectures
- **Developers**: UML, sequence and ER diagrams as files in the repository
- **Documentation teams**: Confluence/Jira integration, PNG/SVG automatable from the CLI
- **Data protection officers**: offline operation and file storage without vendor lock-in
- **Tool builders**: own plugins and embedding in product interfaces
