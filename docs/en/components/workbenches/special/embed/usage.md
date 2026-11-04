# Embed - Usage

!!! note
    The examples are kept syntax-neutral. Once the implementation switches to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass.

## Embedding an external page

```jsx
<Embed source="iframe" src="https://example.org/calendar" title="Course calendar"
       ratio="16:9" onLoad={fit} onError={showFallback} />
```

## Embedding another program

```jsx
<Embed source="app" appId="calendar" config={{ view: "month", filter: "team-a" }} />
```

## Widget with message exchange

```jsx
<Embed source="widget" appId="weather" postMessage={true} origin="https://widgets.example"
       onMessage={updateDashboard} />
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| foreign page without scripts | `source = "iframe"`, set `sandbox` tightly |
| own program in a dashboard | `source = "app"`, hide the header of the embedding program |
| small building block in a list | `size = "small"`, `interactive = false` |
| content is unreachable | `onError` shows a notice with a link outwards |
