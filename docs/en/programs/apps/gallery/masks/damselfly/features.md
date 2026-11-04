# Damselfly - Features

## Main features

- **Incremental indexing** via a filesystem watcher; new files appear automatically
- **AI pipeline**: face clustering, scene/object labels, OCR (text in the image), similarity search (vectors in pgvector)
- **Search** over text, date range, folder, labels, people, colour
- **Albums and sharing** with links and embedding (iframe)
- **Duplicate detection** and bulk tools (rename, move, label)

## What Damselfly does NOT do

- **No phone auto-backup** (upload only via web/sync) (❌)
- **No themes/gallery templates** — one uniform React surface (❌)
- **No per-folder permissions** (sharing only per album/link) (❌)
- **No video transcoding** (videos are only pre-marked/delivered) (❌)
- **No RAW development**, only preview provisioning (❌)

## Extensions and integrations

| Integration | Route |
|-------------|-------|
| REST API | Official, also for bulk upload |
| Storage | Local folder, S3-compatible in newer versions |
| Authentication | Local accounts, reverse-proxy auth |
| Webhooks | — (❌) |
| Backups | Database dump plus folder sync |
