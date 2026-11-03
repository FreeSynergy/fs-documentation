# File Upload

| Field | Value |
|-------|-------|
| **Category** | `fields` |
| **Inherits from** | `base` |
| **Variants** | `File Picker`, `Drag & Drop`, `Image Preview` |
| **States** | `dragover`, `uploading`, `error` |
| **Gestures** | `tap`, `drag` |
| **Animations** | `progress`, `fade-in`, `expand` |
| **Related** | `image`, `progress`, `input-group`, `field` |
| **Status** | documented |

## Description
A file upload is an element for choosing and uploading files.

## Purpose

- Uploading files
- Images
- Documents

## Variants

| Variant | Description |
|---------|-------------|
| **File Picker** | choosing a file |
| **Drag & Drop** | drag & drop |
| **Image Preview** | preview |

## Features

- Progress
- Preview
- Validation

## Distinction

- **Do not confuse with** [image](../../../primitives/media/image/): the image shows an existing file,
  the upload is what brings files into the system.
- **Do not confuse with** [progress](../../../primitives/feedback/progress/): the progress bar is only
  embedded here; `progress` is what renders it.
- The upload receives files, it does not manage them — the list lives in
  [list-view](../../data/list-view/).

## Best Practices

- Check type and size **before** the upload and name the error ("max. 5 MB"),
  not only after the server response.
- Own progress per file with a cancel and a remove button.
- Offer drag & drop in addition to the file dialog, never as the only way.
- After the upload show file name, size and preview; count a multi-selection clearly
  ("3 files, 12 MB").

## See also

- [fields – overview](../index.md)
- [Image](../../../primitives/media/image/) — showing uploaded images
- [Progress](../../../primitives/feedback/progress/) — progress bar
- [Base component](../../../primitives/basics/base.md)
