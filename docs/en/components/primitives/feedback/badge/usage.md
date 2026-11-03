# Badge - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## A count on the navigation

```jsx
<BottomNavigationItem
  icon="mail"
  label="Inbox"
  badge={<Badge variant="counter" value={unread} max={99} />}
/>
```

## Status on a list entry

```jsx
<ListViewItem
  title="Request 1042"
  badge={<Badge status="warning" value="under review" />}
/>
```

## A dot for new activity

```jsx
<Icon name="bell" badge={<Badge dot status="info" />} />
```

## A count with text screen readers can understand

```jsx
<Badge
  variant="counter"
  value={openTasks}
  aria-label={openTasks + " open tasks"}
/>
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| New messages | `counter` on the navigation |
| Pipeline status in tables | `status` with one consistent colour palette |
| Less space than 3 characters | `dot` |
| Tags that should be removed | `tags-input`, not a badge |
