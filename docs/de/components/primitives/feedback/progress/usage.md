# Progress - Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Umsetzung auf Rust und Blinc
    wechselt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Upload mit Prozentangabe

```jsx
<Progress
  value={uploadedBytes}
  max={totalBytes}
  showLabel={true}
  onComplete={notifyDone}
/>
```

## Besser als Prozent: eine konkrete Zahl

```jsx
<Progress value={doneFiles} max={totalFiles} showLabel={true} />
```

## Ein Vorgang ohne bekannten Fortschritt

```jsx
<Progress indeterminate={true} aria-label="Index wird aufgebaut" />
```

## Kreisförmig, in einer Card

```jsx
<Card title="Speicher">
  <Progress variant="circular" value={used} max={quota} status={used > quota ? "error" : "active"} />
</Card>
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Datei-Upload, Import | `linear` mit `showLabel` |
| Kompakte Statusanzeige in Cards | `circular` |
| Dauer unbekannt | `indeterminate`, nach höchstens 10 s einen Text ergänzen |
| Abschluss | Farbwechsel zu `success` plus [toast](../toast/) |
