# Seafile

> Category: [files](../../index.md) · [frontends](../index.md)

## What it is

Open-source file sync, share and document collaboration. The unit is the **library**, not the folder. ✅ (admin manual start page.) Desktop sync client under GPLv2 ✅.

## Notable ideas

- **Library as unit** of sync, sharing, history and encryption ✅ (topic titles in the manual).
- **Encrypted libraries** ✅ (title only; details ⚠️).
- **Two clients:** sync client (copies) and Drive client SeaDrive (virtual drive under `~/SeaDrive`, limited cache, needs FUSE 2) ✅.
- **Sync options:** existing folders, selective sub-folder sync, read-only sync, sync interval, excluding files ✅ (titles).
- **Library history and snapshots** with a retention period ✅ (titles).
- **File locking** ✅ (title).
- **Conflict file:** the first upload wins; the other copy is renamed `name (SFConflict user@example.com 2015-03-07-11-30-28)` ✅.
- **Storage back-ends:** S3, Ceph, OpenStack Swift, several at once ✅. Server tools FSCK and GC ✅ (titles).
- **WebDAV and FUSE extensions**, Web API v2.1 ✅ (titles).

## Capabilities seen

| Capability | Seen | Note |
|------------|------|------|
| Libraries, groups, folder permission, departments | ✅ | Titles |
| Virtual drive with cache | ✅ | On-demand fetching is implied, not stated |
| History with retention | ✅ | Titles |
| Locking | ✅ | Title |
| Metadata function | ✅ | Title |
| Deduplication by blocks | ⚠️ | Not on the pages read |

## Name rules

Conflict naming only (above). Others ⚠️.

## What we take

Conflict handling that keeps both copies and names the author and time. Read-only sync and selective sync as options of `sync.configure`. A cache limit for the stream mode. History retention as a setting.

## Sources (read 2026-11-06)

- https://manual.seafile.com/latest/
- https://help.seafile.com/ (topic list)
- https://help.seafile.com/drive_client/drive_client_for_linux/
- https://help.seafile.com/syncing_client/file_conflicts/
- Failed (404): encrypted libraries page.
