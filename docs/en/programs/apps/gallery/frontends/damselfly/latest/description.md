# Damselfly - Description

## What the program does

Damselfly watches a photo folder, indexes everything and delivers a very fast search gallery with AI features (faces, labels, OCR, similarity). It sees itself as a resource-sparing, container-friendly alternative to full-blown photo clouds.

## Advantages

- **Fast and light**: .NET backend, low memory footprint, quick surface
- **AI without a cloud** including OCR, which PhotoPrism lacks in its community edition
- **Simple operation**: one container plus PostgreSQL

## Differentiation

| System | Difference |
|--------|------------|
| **PhotoPrism** | A similar approach, larger community, editions that differ in features. |
| **Immich** | A photo cloud with apps/auto-backup; Damselfly relies on folder sync. |
| **Lychee** | A pure gallery without AI; in exchange a lean REST API and OAuth logins. |

## Technical details

- **Backend**: C#/.NET, Entity Framework, PostgreSQL with pgvector
- **AI**: ONNX models (face, label, OCR, similarity), optional GPU
- **Frontend**: React SPA, responsive
- **Deployment**: Docker Compose (standard), ARM64/AMD64
- **Licence**: AGPLv3

## Who it suits

- Self-supplied users with an existing photo folder who want AI search
- FreeSynergy gallery skins with an album / photo / person / label model
- Environments with scarce hardware
