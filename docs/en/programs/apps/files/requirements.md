# Files — Requirements

What `FreeSynergy.Files` must and can do.

**Provisional (2026-11-06).** No frontends have been analysed for this category, so nothing here has passed the usual
rule (ADR 0006, 0013). Everything comes from our architecture (*arch.*) or is general knowledge of such programs (⚠️),
and must be checked against analysed programs before the contract is written.

Status: `implemented` · `planned` · `proposed`

## Required

| Capability | Basis | Data / standard | Status |
|------------|-------|-----------------|--------|
| List a folder's content (`folder.list`) | ⚠️ | AS2 `Collection` | proposed |
| Create, rename, delete folders (`folder.create`, `folder.rename`, `folder.delete`) | ⚠️ | AS2 `Collection`, activities | proposed |
| Upload a file, resumable (`file.upload`) | *arch.* (large recordings, photos) | AS2 `Document`, `mediaType` | proposed |
| Download or read part of a file (`file.download`) | *arch.* (`Blob` in `common.capnp`) | `Blob` capability | proposed |
| Move, copy, rename files (`file.move`, `file.copy`, `file.rename`) | ⚠️ | activities `Move`, `Update` | proposed |
| Delete with a way back (`file.delete`, `file.restore`) | ⚠️ | `Delete` + tombstone | proposed |
| Search by name and metadata (`file.search`) | ⚠️ | gap | proposed |
| Preview common types (`file.preview`) | ⚠️ | derived data | proposed |
| Reference a file from other programs (`file.resolve`) | *arch.* (ADR 0017, 0037) | object id + `Blob` | proposed |
| Choose a storage backend (`backend.list`, `backend.add`, `backend.remove`) | *arch.* | local, S3, WebDAV | proposed |
| Mark sensitive files (`file.classify`) | *arch.* (ADR 0029) | DPV | proposed |
| Notify about changes (`subscribe`) | *arch.* (ADR 0021) | AS2 activities | proposed |

## Optional

| Capability | Basis | Data / standard | Status |
|------------|-------|-----------------|--------|
| Share with people or by link (`share.create`, `share.revoke`) | ⚠️ | gap, shared specification | proposed |
| File versions (`file.versions`, `file.revert`) | ⚠️ | activity log or gap | proposed |
| Encrypt on the client before storing (`file.encrypt`) | *arch.* (ADR 0024) | to be decided | proposed |
| Sync between devices (`sync.configure`) | ⚠️ | activity log (ADR 0019) | proposed |
| Tags and favourites (`file.tag`) | ⚠️ | AS2 `tag` | proposed |
| Find duplicates by checksum (`file.duplicates`) | ⚠️ | checksum | proposed |
| Full-text search inside documents (`file.searchContent`) | ⚠️ | gap | proposed |

## Not planned (deliberately)

- Editing documents: that belongs to the programs for each kind of content.
- Being an S3 server ourselves: operators can run RustFS or another server.
