# Files — Requirements

What `FreeSynergy.Files` must and can do.

**Provisional (2026-11-06).** Eight [frontends](frontends/index.md) are analysed (first pass, one page each). Capabilities
below carry a *Seen in* mark: [Do](frontends/dolphin/index.md) Dolphin · [Na](frontends/nautilus/index.md) Nautilus ·
[Ex](frontends/windows-explorer/index.md) Explorer · [Fi](frontends/finder/index.md) Finder ·
[Nc](frontends/nextcloud-files/index.md) Nextcloud · [Sf](frontends/seafile/index.md) Seafile ·
[Gd](frontends/google-drive/index.md) Google Drive · [Rc](frontends/rclone/index.md) rclone / S3 browsers.
Rows without a mark are still only *arch.* or general knowledge (⚠️). The mark counts only what was read on an official page.

Status: `implemented` · `planned` · `proposed`

## Required

| Capability | Basis | Data / standard | Status |
|------------|-------|-----------------|--------|
| List a folder's content (`folder.list`) | ⚠️ | AS2 `Collection` | proposed |
| Create, rename, delete folders (`folder.create`, `folder.rename`, `folder.delete`) | ⚠️ | AS2 `Collection`, activities | proposed |
| Upload a file, resumable (`file.upload`) | *arch.* (large recordings, photos) | AS2 `Document`, `mediaType` | proposed |
| Download or read part of a file (`file.download`) | *arch.* (`Blob` in `common.capnp`) | `Blob` capability | proposed |
| Move, copy, rename files (`file.move`, `file.copy`, `file.rename`) | ⚠️ | activities `Move`, `Update` | proposed |
| Delete with a way back (`file.delete`, `file.restore`) | Na, Nc, Gd | `Delete` + tombstone | proposed |
| Search by name and metadata (`file.search`) | Do, Na, Ex, Fi | gap | proposed |
| Preview common types without opening the program (`file.preview`) | Fi, Na, Do | derived data | proposed |
| Reference a file from other programs (`file.resolve`) | *arch.* (ADR 0017, 0037) | object id + `Blob` | proposed |
| Choose a storage backend (`backend.list`, `backend.add`, `backend.remove`) | *arch.* | local, S3, WebDAV | proposed |
| Mark sensitive files (`file.classify`) | *arch.* (ADR 0029) | DPV | proposed |
| Notify about changes (`subscribe`) | *arch.* (ADR 0021) | AS2 activities | proposed |
| Name rules of the backend: report what it cannot hold, refuse clashes with a clear error (`name.check`) | Na, Ex, Rc; ADR 0055 | file system rules; case rules differ | proposed |
| Sort and group a listing (by name, size, type, time, folders first) | Do, Na, Fi | parameter of `folder.list` | proposed |
| Rename or delete many files at once (`file.rename` in bulk) | Do, Na | batch call | proposed |
| Empty the trash, set its retention (`trash.purge`, `trash.configure`) | Na, Nc, Gd | settings | proposed |
| Say what to do when a name already exists: refuse, keep both, replace (conflict policy on move, copy, upload) | Na, Sf, Rc, Nc | rule per call | proposed |
| Show free space and quota of a backend (`backend.quota`) | Nc, Gd | gap | proposed |
| List and clean up unfinished uploads (`upload.list`, `upload.abort`) | Rc | S3 multipart | proposed |

## Optional

| Capability | Basis | Data / standard | Status |
|------------|-------|-----------------|--------|
| Share with people or by link (`share.create`, `share.revoke`) | Nc, Gd, Sf | gap, shared specification | proposed |
| File versions (`file.versions`, `file.revert`) | Nc, Sf, Rc (S3 versions) | activity log or gap | proposed |
| Encrypt on the client before storing (`file.encrypt`) | *arch.* (ADR 0024) | to be decided | proposed |
| Sync between devices (`sync.configure`) | ⚠️ | activity log (ADR 0019) | proposed |
| Tags and favourites (`file.tag`) | Do, Fi, Nc | AS2 `tag` | proposed |
| Find duplicates by checksum (`file.duplicates`) | ⚠️ | checksum | proposed |
| Full-text search inside documents (`file.searchContent`) | ⚠️ | gap | proposed |
| Name versions so they never expire; expiry rules for the rest (`file.versions`, `file.pin`) | Nc, Sf | activity log or gap | proposed |
| Roles on a share (viewer, commenter, editor), expiry, password, hide download, drop-only folder, note, transfer ownership | Nc, Gd | gap, shared specification | proposed |
| One file in several places: aliases or shortcuts, collections (`file.link`) | Fi, Gd | AS2 `Collection` | proposed |
| Saved search as a folder (`search.save`) | Do, Fi | gap | proposed |
| Stream or mirror a remote backend as local files, with cache limit; selective and read-only sync | Gd, Sf, Rc | sync, ADR 0019 | proposed |
| Lock a file while it is edited (`file.lock`) | Sf | gap | proposed |
| Conflict copies that name author and time | Sf, Rc | rule | proposed |
| Encrypt file names as well as contents | Rc | with `file.encrypt` | proposed |
| Download a folder as one archive | Nc, Rc | `Blob` | proposed |
| Dry run and delete limit before a sync | Rc | rule | proposed |
| Undo of the last move, rename or delete | Do, Na | frontend, needs reversible calls | proposed |
| Instant search by name from a local index, updated from the file system's change log (`file.search` fast path) | Everything | derived index, gap | proposed |
| File request: ask outside people to send files into a chosen folder, without an account (naming rule, password, deadline) | Dropbox | gap, shared specification | proposed |
| Device-to-device sync without a central server, devices named by key fingerprint | Syncthing | activity log (ADR 0019) | proposed |

## Not planned (deliberately)

- Editing documents: that belongs to the programs for each kind of content.
- Being an S3 server ourselves: operators can run RustFS or another server.
