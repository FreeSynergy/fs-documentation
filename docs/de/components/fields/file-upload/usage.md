# File Upload (Datei-Upload) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Anwendung

Ein File Upload ist ein Element für Dateiauswahl und Upload.

- Dateien hochladen
- Bilder
- Dokumente

## Beispiele

### Dateien hochladen

```jsx
<FileUpload value={eintraege} onChange={aktion} />
```

### Bilder

```jsx
<FileUpload value={eintraege} multiple={false} />
```

### Dokumente

```jsx
<FileUpload value={eintraege} showProgress={true} />
```
