# Progress (Fortschrittsanzeige) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Upload mit Prozentangabe

```jsx
<Progress
  value={uploadedBytes}
  max={totalBytes}
  showLabel={true}
  onComplete={notifyDone}
/>
```

## Besser als Prozent: konkrete Zahl

```jsx
<Progress value={doneFiles} max={totalFiles} showLabel={true} />
```

## Unbestimmter Vorgang

```jsx
<Progress indeterminate={true} aria-label="Index wird erstellt" />
```

## Kreisförmig in einer Karte

```jsx
<Card title="Speicher">
  <Progress variant="circular" value={used} max={quota} status={used > quota ? "error" : "active"} />
</Card>
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Datei-Upload, Import | `linear` mit `showLabel` |
| Kompakte Statusanzeige in Karten | `circular` |
| Dauer unbekannt | `indeterminate`, nach spätestens 10 s Text ergänzen |
| Abschluss | Farbwechsel auf `success` plus [toast](../toast/) |
