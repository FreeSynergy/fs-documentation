# Progress - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Upload with a percentage

```jsx
<Progress
  value={uploadedBytes}
  max={totalBytes}
  showLabel={true}
  onComplete={notifyDone}
/>
```

## Better than percent: a concrete number

```jsx
<Progress value={doneFiles} max={totalFiles} showLabel={true} />
```

## An indeterminate process

```jsx
<Progress indeterminate={true} aria-label="Building index" />
```

## Circular, inside a card

```jsx
<Card title="Storage">
  <Progress variant="circular" value={used} max={quota} status={used > quota ? "error" : "active"} />
</Card>
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| File upload, import | `linear` with `showLabel` |
| Compact status display in cards | `circular` |
| Duration unknown | `indeterminate`, after at most 10 s add a text |
| Completion | colour change to `success` plus [toast](../toast/) |
