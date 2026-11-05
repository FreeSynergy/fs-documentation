# LibrePhotos - Description

## What the program does

LibrePhotos builds a private photo cloud: captures are scanned, tagged, assigned to faces and places and shown in a React surface as a timeline, album or map. The holdings exist as files on the server.

## Advantages

- **The complete feature set of a photo cloud** including apps and AI search
- **A clear Python base** (Django), easy to adapt and readable
- **Semantic search** without cloud services

## Differentiation

| System | Difference |
|--------|------------|
| **Immich** | Larger community, smoother timeline, cleaner API; LibrePhotos is more modular in the backend. |
| **PhotoPrism** | Indexes existing folders and is Go-based; LibrePhotos manages the library itself. |
| **Piwigo** | A web-toolkit gallery without AI, but with themes and roles per folder. |

## Technical details

- **Backend**: Python/Django, Celery workers, Redis, PostgreSQL
- **AI**: CLIP (search), face-recognition, Places365 and object classification
- **Frontend**: React SPA, mobile apps in React Native
- **Deployment**: Docker Compose, worker and web containers separated
- **Licence**: AGPLv3

## Who it suits

- Users who want to recreate Google Photos functionality self-hosted and close to Python
- FreeSynergy gallery frontends with an album / photo / person / share model
- Projects that want to adapt the recognition pipelines themselves
