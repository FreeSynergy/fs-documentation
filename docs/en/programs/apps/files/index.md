# Files

## In short

Files looks after your files and folders. It knows what each file is, how big it is and where it lives, so other programs can refer to a file without ever seeing a path. It answers the question: where is that file, and who else needs it?

**Command:** `fs-files`, one command per program with subcommands ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md); programs are switched over when they are next touched, so not every one is yet).

## What is different here

- With the default local backend, files lie in an ordinary folder under their real names, such as `Urlaub/Foto.jpg`. You can open that folder with any other tool.
- The bytes can also sit in S3-compatible storage such as RustFS.
- Deleting goes through a trash first. A name clash never overwrites silently: you refuse it or keep both.
- Uploads survive a restart and pick up where they stopped.
- Other programs are meant to refer to a file by its id, so a file does not need to be copied into each program.

## Where it stands today

Latest tag: `v0.0.1`. Folders, rename, move, copy, trash, restore and purge work, as do resumable uploads with a checksum, search, sorting and filters. "Rescan" takes over files put into the folder from outside and deletes nothing. A small server offers all of this over a local socket. The S3 backend was tested once against a real RustFS server, not in the automatic tests.

Not there yet: a window, sharing, versions, encryption of file contents, sync, WebDAV and previews. Replacing a file is not offered. The interface is a draft marked provisional, and nothing uses it yet.

## Planned facets

Facets are parts of a program that look like apps of their own ([ADR 0061](../../../decisions/0061-facetten.md)). Each gets its own command, a link to `fs-files` ([ADR 0063](../../../decisions/0063-ein-programm-ein-befehl.md)).

Proposed, not built:

- Gallery: your pictures.
- Music: your music.
- Videos: your videos.
- Documents: your documents.

`FreeSynergy.Files` (`fs-files`) stores, organises and shares any kind of file. Other programs, such as the gallery,
keep their bytes here instead of building their own storage.

The [code lives here](https://github.com/FreeSynergy/fs-files). See the [roadmap](../roadmap.md).

- [Design](design.md): how it is built, storage backends, open questions
- [Requirements](requirements.md): what it must do (provisional)

- [Frontends](frontends/index.md): eight programs analysed for their functions (first pass)

## Frontends

<!-- gen:frontends (scripts/gen_frontend_indexes.py) — edits inside are overwritten -->
Analysed programs (13), by function, nothing copied (ADR 0012/0013):

- [Dolphin](frontends/dolphin/index.md) — The file manager of KDE Plasma.
- [Dropbox](frontends/dropbox/index.md) — Dropbox is a commercial cloud storage service with web, desktop and mobile clients and a developer API.
- [Everything](frontends/everything/index.md) — Everything (voidtools) is a free search program for Windows that finds files and folders by name while you type ✅.
- [Files (Files App for Windows)](frontends/files-community/index.md) — A free, open-source file manager for Windows, built by a community (repository `files-community/Files`, WinUI, C#/.NET) ✅.
- [Finder](frontends/finder/index.md) — The file manager of macOS.
- [Google Drive](frontends/google-drive/index.md) — Cloud storage by Google: web, apps and a desktop client.
- [Nautilus (GNOME Files)](frontends/nautilus/index.md) — The file manager of the GNOME desktop.
- [Nextcloud Files](frontends/nextcloud-files/index.md) — The Files app of Nextcloud: web interface, desktop and mobile sync, WebDAV, on a server you run.
- [rclone (and the S3-browser type)](frontends/rclone/index.md) — A command-line program that copies, syncs, mounts and serves files across many storage services.
- [Seafile](frontends/seafile/index.md) — Open-source file sync, share and document collaboration.
- [Syncthing](frontends/syncthing/index.md) — Syncthing is a free program that keeps chosen folders identical between devices directly, with no central server ✅ (concept; the intro page does not state it, see Open).
- [Total Commander](frontends/total-commander/index.md) — A paid (shareware) two-pane file manager for Windows by Christian Ghisler ✅ (home page links to ordering and shareware sites; price not stated there; Wikipedia: shareware on Windows, freeware on An…
- [Windows Explorer (File Explorer)](frontends/windows-explorer/index.md) — The file manager of Windows.

Overview: [frontends](frontends/index.md)
<!-- /gen:frontends -->
