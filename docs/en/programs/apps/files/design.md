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

We propose not to make it the engine of `fs-files`:

- It is a **separate server**, so requiring it would break "every program runs alone" (ADR 0017) on a laptop or phone.
- Its README describes running it as a server. An embedded library form was not found, and this has not been fully checked.
- Reaching it through the S3 protocol keeps us independent of one project. It only reached 1.0 recently.

This is the same role ADR 0018 gives Stalwart: recommended to operators and run separately, with no dependency on it.

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

## Components

Workbench `file-manager` with a compact `file-picker` variant, used wherever a program needs to choose or attach a
file. See [planned components](../../../components/planned.md).

## Stages

1. Local folder, metadata in `fs-store`, browse, move, rename, delete with trash, search by name, resumable upload.
2. S3 backend, sharing, versions, client-side encryption.
3. Sync between devices via `fs-hub`, conflict handling, WebDAV.

## Open questions

1. **Real folder or managed store?** For the local backend we propose real, visible files in a normal folder, with
   changes picked up by watching it. This avoids lock-in but makes conflicts harder.
2. **Is a folder here the same as ADR 0037's "folder = group = mailing list"?** If so, sharing a folder would equal
   sharing with a group. This needs a decision.
3. **Sharing model:** files, gallery, kanban and surveys all need it. We propose one shared specification rather than
   four solutions.
4. **Encryption:** should bytes on S3 always be encrypted on the client, using the key vault (ADR 0024)? We propose yes.
5. **Does the data live in one place?** Bytes are deliberately outside `fs-store`, so backups must cover both.
