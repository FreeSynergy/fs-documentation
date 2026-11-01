# Embed (Einbettung) - Verwendung

!!! note
    Die Beispiele sind syntaxneutral gehalten. Sobald die Umsetzung auf Rust und
    Blinc umgestellt wird, werden `usage.md`-Beispiele in einem eigenen Durchlauf
    ersetzt.

## Externe Seite einbetten

```jsx
<Embed source="iframe" src="https://example.org/kalender" title="Kurskalender"
       ratio="16:9" onLoad={fit} onError={showFallback} />
```

## Anderes Programm einbetten

```jsx
<Embed source="app" appId="calendar" config={{ view: "month", filter: "team-a" }} />
```

## Widget mit Nachrichtenaustausch

```jsx
<Embed source="widget" appId="weather" postMessage={true} origin="https://widgets.example"
       onMessage={updateDashboard} />
```

## Szenarien

| Szenario | Empfehlung |
|----------|------------|
| Fremde Seite ohne Skripte | `source = "iframe"`, `sandbox` eng setzen |
| eigenes Programm im Dashboard | `source = "app"`, Kopfzeile des einbettenden Programms ausblenden |
| kleiner Baustein in einer Liste | `size = "small"`, `interactive = false` |
| Inhalt ist nicht erreichbar | `onError` zeigt Hinweis mit Verweis nach außen |
