# Files — design

**Status: proposal (2026-11-06).** Back to the [roadmap](../roadmap.md) · [requirements](requirements.md).

## Idea

Two things are kept apart: **what we know about a file** and **where its bytes are**.

- **Metadata** is an object in `fs-store`, like all other data: name, media type, size, checksum, folder, sharing.
- **Bytes** live in a storage backend behind one interface. Which backend is in use makes no difference to the
  program, the frontends or other programs.

Other programs refer to a file by its object id and read it through the `Blob` capability in `common.capnp`. They
never see paths or backends.

## Data

| Piece | Standard | Notes |
|-------|----------|-------|
| File | AS2 `Document` (`Image`, `Video`, `Audio` where they apply), `mediaType` | Fields follow [File / media](../../../data/models.md) |
| Folder | AS2 `Collection` | ADR 0037 treats folder, group and mailing list as one concept; to be checked for files |
| Change | AS2 activities in the log | `Create`, `Update`, `Move`, `Delete` |
| Version | gap | Own specification, or plain activity history; open |
| Sharing, permissions | gap | Shared by all programs, so it must be specified once ([question 3](#open-questions)) |

Sensitive files are marked according to ADR 0029.

## Storage backends

```rust
//! Pattern: Strategy (backend), Decorator (encryption, cache), Repository (metadata).
#[async_trait]
pub trait BlobStore: Send + Sync {
    async fn put(&self, key: &BlobKey, data: ByteStream) -> Result<BlobInfo>;
    async fn get(&self, key: &BlobKey, range: Option<ByteRange>) -> Result<ByteStream>;
    async fn delete(&self, key: &BlobKey) -> Result<()>;
    async fn stat(&self, key: &BlobKey) -> Result<BlobInfo>;
}
```

This sketch shows the shape only. The final form comes from the contract.

| Backend | For whom | Stage |
|---------|----------|-------|
| **Local folder** | Everyone. The default: no server, and files stay ordinary files you can open with anything | 1 |
| **S3** | Teams and servers. Works with RustFS and any other S3 store | 2 |
| **WebDAV** | Existing storage such as Nextcloud | later |

### RustFS

[RustFS](https://github.com/rustfs/rustfs) is an S3-compatible object store written in Rust, under Apache-2.0 (version
1.0.4 on 2026-10-25). It suits our licence and language rules and fits as a **recommended server backend**.

**Decided (2026-11-06): optional, yet used heavily, and we hope to work with the project,** including delivering data
online. It is a separate server, so a laptop or phone must also work without it (ADR 0017). Git is another option.

### Candidates

| Purpose | Crate (2026-11-06) | Notes |
|---------|--------------------|-------|
| Local + S3 + WebDAV behind one API | `opendal` 0.59 | Would be wrapped by our `BlobStore` |
| Same, narrower | `object_store` 0.14 | Alternative |
| Checksums | `blake3` 1.8 | `models.md` currently names `sha256:` as the example; to be aligned |
| Watching a local folder | `notify` | Stable 8.x or the 9.0 release candidate; to be checked |
| Detecting the file type | `infer` 0.22 | |

Resumable uploads are needed for large files. The `tus` crate has had no release since 2023, so it is not a candidate.

## Interface sketch

| Interface | Capabilities |
|-----------|--------------|
| `Files` (root) | `capabilities()`, hands out the others |
| `Folders` | `folder.list`, `folder.create`, `file.move`, `file.rename`, `file.delete`, `file.restore` |
| `Transfer` | `file.upload` (resumable), `file.download` (`Blob`) |
| `Search` | `file.search` |
| `Sharing` | `share.create`, `share.revoke` |
| `Backends` | `backend.list`, `backend.add`, `backend.remove` |
| `subscribe` | Live changes for other programs |

## Saving and exporting

**Saving and exporting are different things** (ADR 0046, building on ADR 0042).

- While you work, you work on a **copy in the database**, always kept. There is no "save" to forget.
- Files are storage and backups.
- Only an **export** produces a file to hand on.

Texts and small objects live in the database. Large files such as videos cannot be copied whole on each edit: they keep
their bytes in the file store, and versions share unchanged blocks.

**Asking on leaving:** we propose not to ask every time, since people click such questions away. A "pass on" action
offers the export when it is wanted. The program asks only when a file was opened from outside, because people then
expect that file to change: "Update the original too?"

## Views

The same files, seen in different ways. Files can suggest a view from the content and remember it per folder; whether a
frontend uses this is up to the frontend.

List, tree, grid, timeline, map, people, music library, video library, reader, shelf of documents, recent activity,
duplicates. **A gallery is a frontend with a built-in filter**: an app that looks like its own program, on the same engine.

Ideas to develop:

- **Collections, not copies:** a file can be in many albums, and an album can also be a saved search.
- **Metadata extractors per file type** behind one [interface](../../../interfaces/index.md): photo, audio, video, PDF.
  Each can be linked to the programs that open that type, much as an operating system does. Standards for each type come first.
- **Embedded:** "all files of this project" inside a project or wiki page.
- Face recognition as an optional, local-only extractor (ADR 0029).

## Components

Workbench `file-manager` with a compact `file-picker` variant, used wherever a program needs to choose or attach a
file. See [planned components](../../../components/planned.md).

## Stages

1. Local folder, metadata in `fs-store`, browse, move, rename, delete with trash, search by name, resumable upload.
2. S3 backend, sharing, versions, client-side encryption.
3. Sync between devices via `fs-hub`, conflict handling, WebDAV.

## Open questions

1. **Real folder or managed store?** Both must be possible. With the working copy in the database, real files are the
   stored form. How changes from outside are picked up remains open.
2. **Is a folder here the same as ADR 0037's "folder = group = mailing list"?** If so, sharing a folder would equal
   sharing with a group. This needs a decision.
3. **Sharing model:** files, gallery, kanban and surveys all need it. We propose one shared specification rather than
   four solutions.
4. **Encryption:** should bytes on S3 always be encrypted on the client, using the key vault (ADR 0024)? We propose yes.
5. **Does the data live in one place?** Bytes are deliberately outside `fs-store`, so backups must cover both.
