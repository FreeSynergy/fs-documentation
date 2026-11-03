# File Upload - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Application

A file upload is an element for choosing and uploading files.

- Uploading files
- Images
- Documents

## Examples

### Uploading files

```jsx
<FileUpload value={entries} onChange={action} />
```

### Images

```jsx
<FileUpload value={entries} multiple={false} />
```

### Documents

```jsx
<FileUpload value={entries} showProgress={true} />
```
