# TrueNAS

> Category: [desktop](../../index.md)

## What it is

TrueNAS (iXsystems, formerly FreeNAS) is the open-source storage platform with end-to-end ZFS management: pools, datasets, snapshots, replication and shares (SMB, NFS, iSCSI, S3) are managed via a modern web UI. CORE is based on FreeBSD, SCALE/24+ on Linux and adds Docker apps as well as (from 24.10) KVM VMs. The API v2.0 speaks JSON-RPC 2.0 over HTTP/WebSocket; in addition there are the CLI `midclaw`/`midclt` and API keys.

## Notable ideas

_To do: what does this program do that others don't? Why is it documented here (ADR 0013)?_

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
| Version | Required files present |
|---------|------------------------|
| [latest](latest/description.md) | 6/7 |

### latest

| File | Contents |
|------|----------|
| [description.md](latest/description.md) | Detailed description, differentiation, who it suits |
| [features.md](latest/features.md) | What the program can do — and what not |
| [layout.md](latest/layout.md) | Window structure, regions, panels |
| [menus.md](latest/menus.md) | Menu structure, context menus, menus by role |
| [shortcuts.md](latest/shortcuts.md) | Keyboard shortcuts |
| [api.md](latest/api.md) | APIs and protocols, authentication, rate limits |

⚠️ Missing required files: `themes/index.md`
<!-- /gen:versions -->
