# rclone (and the S3-browser type)

> Category: [files](../../index.md) · [frontends](../index.md)

## What it is

A command-line program that copies, syncs, mounts and serves files across many storage services. Its S3 back-end speaks to any S3 store. It stands here for the whole type of "browse and move objects in S3" tools, including the Windows client S3 Browser. MIT licence ⚠️ (not read).

## Notable ideas

- **One verb set for all stores:** `copy`, `sync`, `move`, `check`, `ncdu` (interactive sizes), `mount`, `serve`, `bisync` ✅.
- **`--dry-run`** to try a sync first; **`--bwlimit`** with a weekday timetable ✅.
- **bisync:** compares to a saved listing of the last run; on a conflict keeps both and suffixes `conflict1/2`, or picks a winner by newer, older, larger and so on; aborts when more than 50% would be deleted; `--resync` for first run ✅.
- **crypt:** encrypts contents (64 KiB chunks), and by default file and folder names; the folder structure, size within 16 bytes, and times stay visible; password change needs re-upload ✅.
- **union** and **chunker** back-ends ✅ (named).
- **mount with cache modes:** off, minimal, writes, full; without a cache mode only sequential writes ✅.
- **rcd with web GUI:** remote control API, optional basic or htpasswd login, zip download ✅.
- **S3 specifics:** modification time as object metadata; MD5 in metadata for multipart; versions listing; `cleanup` removes unfinished multipart uploads older than 24 hours ✅. Empty directories vanish on bucket stores unless markers are used ✅. Keys with `//` are not supported ✅.
- **S3 Browser (Windows client):** lists, aborts and resumes uncompleted multipart uploads by choosing the source file again; they never expire and cost space ✅ (vendor page). Feature list page returned 404, so the rest ⚠️.

## Capabilities seen

| Capability | Seen | Note |
|------------|------|------|
| Copy, move, sync, check | ✅ | |
| Two-way sync with conflict rules | ✅ | |
| Mount as a drive, with cache | ✅ | Needs WinFsp, macFUSE or FUSE-T, fusermount |
| Encrypt before storing | ✅ | |
| List sizes interactively | ✅ | |
| Resume interrupted upload | ⚠️ | Not described on the S3 page; rclone describes cleanup of unfinished parts |
| RustFS | ⚠️ | Not listed on the S3 page |

## Name rules

On S3 any valid UTF-8 key, but `/`, NUL, `.` and `..` as names are replaced ✅. Mount: Linux case-sensitive; Windows and macOS case-insensitive but preserving ✅; Unicode normalisation matters on macOS ✅.

## What we take

Dry-run and a delete limit as safety in sync. Conflict policy as a setting. Listing and cleaning unfinished uploads (`Upload.received` is a good start; a list of pending uploads is missing). Cache mode idea for a stream mode. Encrypted names as an option of client-side encryption.

## Documented versions

<!-- gen:versions (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
No version documented in English yet.
<!-- /gen:versions -->

## Sources (read 2026-11-06)

- https://rclone.org/docs/
- https://rclone.org/commands/rclone_mount/
- https://rclone.org/commands/rclone_rcd/
- https://rclone.org/bisync/ (first 100000 characters)
- https://rclone.org/crypt/
- https://rclone.org/s3/ (first 100000 characters)
- https://s3browser.com/uncompleted-multipart-uploads.aspx
