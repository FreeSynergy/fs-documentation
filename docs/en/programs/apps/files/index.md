# Files

`FreeSynergy.Files` (`fs-files`) stores, organises and shares any kind of file. Other programs, such as the gallery,
keep their bytes here instead of building their own storage.

**Status: planned, no code yet (2026-11-06).** See the [roadmap](../roadmap.md).

- [Design](design.md): how it is built, storage backends, open questions
- [Requirements](requirements.md): what it must do (provisional)

- [Frontends](frontends/index.md): eight programs analysed for their functions (first pass)

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysed programs (8), by function, nothing copied (ADR 0012/0013):

- [Dolphin](frontends/dolphin/index.md) — The file manager of KDE Plasma.
- [Finder](frontends/finder/index.md) — The file manager of macOS.
- [Google Drive](frontends/google-drive/index.md) — Cloud storage by Google: web, apps and a desktop client.
- [Nautilus (GNOME Files)](frontends/nautilus/index.md) — The file manager of the GNOME desktop.
- [Nextcloud Files](frontends/nextcloud-files/index.md) — The Files app of Nextcloud: web interface, desktop and mobile sync, WebDAV, on a server you run.
- [rclone (and the S3-browser type)](frontends/rclone/index.md) — A command-line program that copies, syncs, mounts and serves files across many storage services.
- [Seafile](frontends/seafile/index.md) — Open-source file sync, share and document collaboration.
- [Windows Explorer (File Explorer)](frontends/windows-explorer/index.md) — The file manager of Windows.

Overview: [frontends](frontends/index.md)
<!-- /gen:frontends -->
