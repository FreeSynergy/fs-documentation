# Google Drive

> Category: [files](../../index.md) · [frontends](../index.md)

## What it is

Cloud storage by Google: web, apps and a desktop client. Proprietary. ⚠️

## Notable ideas

- **Stream or mirror** in Drive for desktop: stream loads files on demand and uses almost no disk; mirror keeps a full copy. Offline use is possible for chosen files ✅.
- **Three roles:** Viewer, Commenter, Editor ✅. Editors may change permissions by default ✅.
- **Link access:** restricted, anyone with the link (view only), or your organisation ✅.
- **Expiry on a person's access** up to one year (work or school accounts) ✅. **Restrict download, copy, print** per role ✅.
- **Ownership transfer** ✅; deleting a shared file you own removes access for all ✅.
- **Shortcuts:** a metadata-only file pointing to another; folders are files of a folder type; in My Drive a file can have several parents, on a shared drive only one ✅ (API guide).
- **Shared with me** list and **Remove from view** ✅.
- **Trash:** 30 days; counts toward storage until emptied; non-owners can only remove ✅.

## Capabilities seen

| Capability | Seen | Note |
|------------|------|------|
| Roles and link sharing | ✅ | |
| Stream, mirror, offline | ✅ | |
| Trash | ✅ | |
| Shortcuts, multiple parents | ✅ | |
| Stable opaque file ID, name may change | ✅ | |
| Version history | ⚠️ | The page fetched did not cover it |
| Duplicate names in one folder | ⚠️ | API page does not say |

## Name rules

⚠️ Not verified.

## What we take

Roles as a base for the sharing specification. Expiry on a share. Per-role download restriction. A file in several folders without copying (matches "collections, not copies"). Remove-from-view versus delete for people who are not the owner.

## Sources (read 2026-11-06)

- https://support.google.com/drive/answer/2494822 (sharing)
- https://support.google.com/drive/answer/2375057 (shared with me)
- https://support.google.com/drive/answer/2375102 (delete and trash)
- https://support.google.com/drive/answer/10838124 (Drive for desktop)
- https://developers.google.com/workspace/drive/api/guides/about-files
