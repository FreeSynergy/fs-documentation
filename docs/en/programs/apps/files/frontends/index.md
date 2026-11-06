# Files — Frontends

Frontends of well-known programs in this category, analysed for their **functions** — nothing is copied (ADR 0013). A program is documented here because it is widely learned or because it has a notable idea. Our own program for this category is `FreeSynergy.Files` (ADR 0017); its capabilities and status live in [requirements](../requirements.md).

Research date: 2026-11-06. Each claim is marked ✅ (read on the cited official page on that date) or ⚠️ (not verified; known from the product or only from a non-official page). Version numbers were not checked, so each page describes the current documentation, not a fixed version.

## Programs

| Program | Kind | What it is |
|---------|------|------------|
| [Dolphin](dolphin/index.md) | local manager | The file manager of KDE Plasma. Many panels, split view, built-in search. |
| [Nautilus (GNOME Files)](nautilus/index.md) | local manager | The file manager of GNOME. Few options, remote servers through the same window. |
| [Windows Explorer](windows-explorer/index.md) | local manager | File Explorer of Windows. Ribbon or command bar, cloud files next to local ones. |
| [Finder](finder/index.md) | local manager | The file manager of macOS. Four view modes, tags, Quick Look. |
| [Nextcloud Files](nextcloud-files/index.md) | self-hosted | Web, desktop and mobile access to files on your own server. Strong sharing and versions. |
| [Seafile](seafile/index.md) | self-hosted | Libraries as the unit of sync, sharing and encryption. |
| [Google Drive](google-drive/index.md) | cloud | Cloud storage with a stream-or-mirror desktop client and role-based sharing. |
| [rclone](rclone/index.md) | command line, S3-browser type | One tool for many storage services: copy, sync, mount, serve. Stands for S3 browsers too. |

## What every page contains

```
programs/apps/files/frontends/<program>/
└── index.md        what it is, notable ideas, capabilities, name rules, what we take, sources
```

The full file set of ADR 0012 (`<version>/description.md`, `features.md`, `layout.md`, `menus.md`, `shortcuts.md`, `api.md`, `themes/index.md`) is **not written yet**. These pages are the first analysis, made to check the contract. The rest follows when a frontend is built in that style.

## Cross-cutting findings

- **Names.** Local managers show the real name and let the file system decide what may coexist. Linux allows only `/` (✅ GNOME help), Windows forbids nine characters and some device names (✅ Microsoft Learn). Case rules differ (✅ GNOME, ✅ Microsoft Learn, ✅ rclone mount). This fits ADR 0055; the engine must report the rules of the backend, not enforce one set.
- **Delete is two steps.** Every program studied has a trash with restore. Retention differs: 30 days in Nextcloud and Google Drive (✅). Restoring must cope with a missing parent folder (✅ Nextcloud).
- **Conflicts.** Programs that sync keep both copies and rename one: Seafile, rclone bisync (✅). Local managers refuse or ask (✅ GNOME).
- **Sharing is its own subject.** Roles, links with password and expiry, drop-only folders, federation, ownership transfer (✅ Nextcloud, ✅ Google Drive).
- **Stream or mirror.** Two ways to show remote files as local (✅ Google Drive for desktop, ✅ Seafile drive client, ✅ rclone mount with cache modes).
- **Encryption of names.** rclone crypt can hide file and folder names; the structure stays visible (✅). Seafile has encrypted libraries (✅ named in manual index; details ⚠️).
- **Uncompleted uploads cost space** and must be listed and cleaned (✅ S3 Browser, ✅ rclone cleanup).
