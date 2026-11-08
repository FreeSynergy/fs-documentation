# File Upload - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung zu Rust und Blinc wechselt,
    werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Anwendung

Ein File Upload ist ein Element zum Auswählen und Hochladen von Dateien.

- Hochladen von Dateien
- Bilder
- Dokumente

## Beispiele

### Hochladen von Dateien

```jsx
<FileUpload value={entries} onChange={action} />
```

### Bilder

```jsx
<FileUpload value={entries} multiple={false} />
```

### Dokumente

```jsx
<FileUpload value={entries} showProgress={true} />
```
