# Embed – Verwendung

!!! note
    Die Beispiele bleiben syntaxneutral. Sobald die Implementierung auf Rust und
    Blinc umstellt, werden die Beispiele in `usage.md` in einem eigenen Durchgang ersetzt.

## Eine externe Seite einbetten

```jsx
<Embed source="iframe" src="https://example.org/calendar" title="Course calendar"
       ratio="16:9" onLoad={fit} onError={showFallback} />
```

## Ein anderes Programm einbetten

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
|----------|----------------|
| fremde Seite ohne Skripte | `source = "iframe"`, `sandbox` eng setzen |
| eigenes Programm in einem Dashboard | `source = "app"`, Kopfzeile des einbettenden Programms ausblenden |
| kleiner Baustein in einer Liste | `size = "small"`, `interactive = false` |
| Inhalt ist nicht erreichbar | `onError` zeigt einen Hinweis mit Link nach außen |
