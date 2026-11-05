# OpenBoard - Description

## What the program does

OpenBoard is the digital blackboard tool for teaching and meetings: full-screen pages on which you write with pen/finger, embed media and present — entirely local and open source (GPL).

## Advantages

- **free, offline, data-sovereign** (schools/authorities)
- **instant-image logic**: pages like sections of a blackboard, no folder thinking needed
- **teaching tools** (geometry, timer, browser) integrated

## Differentiation

| System | Difference |
|--------|------------|
| **Xournal++** | note annotation over PDF; OpenBoard is a presentation/class blackboard |
| **Miro/Mural** | team SaaS; OpenBoard is a single local workstation |
| **MyPaint** | painting program, no blackboard/presentation concept |

## Technical details

- **Stack**: C++, Qt (multitouch), Linux-first; Windows/macOS builds
- **Storage**: library under `~/OpenBoard`, documents as `.obz` (ZIP with SVG pages + metadata)
- **Licence**: GPL

## Who it suits

- Teachers and presenters with interactive whiteboards or a stylus
- FreeSynergy skins for **page-based blackboard UIs** (page/element/pen model)
