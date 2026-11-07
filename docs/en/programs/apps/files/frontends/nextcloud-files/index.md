# Nextcloud Files

> Category: [files](../../index.md) · [frontends](../index.md)

## What it is

The Files app of Nextcloud: web interface, desktop and mobile sync, WebDAV, on a server you run. Free software. ⚠️ (licence not read.)

## Notable ideas

- **Versions with a thinning rule:** a new version at most every two minutes; older ones are thinned (seconds, minutes, hours, days, weeks); named versions never expire; version space is capped at 50% of free space ✅.
- **Trash with rules:** at least 30 days by default, capped at 50% of remaining quota, oldest first; restore goes to the root if the old folder is gone; versions travel with the file; trash does not count against quota ✅.
- **Many share targets:** public link, users, groups, circles, Talk conversations, federated servers ✅.
- **File drop:** upload into a folder without seeing its content ✅.
- **Others with access:** shows who reaches a file through a parent folder's share ✅.
- **Federated shares** mounted with `user@server` ✅.
- **Transfer ownership**, **system tags**, **external storage**, **large file uploads**, **server-side and end-to-end encryption** are manual chapters ✅ (titles only).

## Capabilities seen

| Capability | Seen | Note |
|------------|------|------|
| Web, WebDAV, desktop and mobile sync | ✅ | |
| Versions, restore, name a version, delete one | ✅ | |
| Trash, restore, delete permanently | ✅ | |
| Share link with password, expiry, note, hide download, several links with different rights | ✅ | |
| Share permission per recipient; auto-accept or approve | ✅ | |
| Storage quota | ✅ | WebDAV clients cannot show free space (Windows) |
| System tags | ✅ | Title only |
| Locking, comments, favourites | ⚠️ | Not named in the manual contents |

## Name rules

Restore on a name clash gives a unique name ✅. Other rules ⚠️.

## API

WebDAV at `/remote.php/dav/files/USERNAME/`; an app password is advised for third-party clients because normal passwords slow it ✅. Public shares through `public.php/dav/files/` with the token as user name ✅. Chunked upload is a separate page, not read ⚠️.

## What we take

Versions with expiry rules and named (pinned) versions. Trash retention as settings. The sharing model as input for the shared specification (design, question 3). Quota shown to the user. WebDAV as a later backend (design: stage 3).

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
No version documented in English yet.
<!-- /gen:versions -->

## Sources (read 2026-11-06)

- https://docs.nextcloud.com/server/latest/user_manual/en/files/index.html
- https://docs.nextcloud.com/server/latest/user_manual/en/files/version_control.html
- https://docs.nextcloud.com/server/latest/user_manual/en/files/deleted_file_management.html
- https://docs.nextcloud.com/server/latest/user_manual/en/files/sharing.html
- https://docs.nextcloud.com/server/latest/user_manual/en/files/access_webdav.html
