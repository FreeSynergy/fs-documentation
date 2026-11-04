# Popover - Usage

!!! note
    The examples are kept syntax-neutral. Once the implementation switches to Rust and
    Blinc, the `usage.md` examples will be replaced in a separate pass.

## Actions on an entry

```jsx
<Popover trigger="click" placement="bottom" variant="aktionen" content={entryActions} />
```

## Quick dialog: set the due date

```jsx
<Popover
  variant="formular"
  trigger="click"
  closeOnAction={true}
  content={<DatePicker value={due} onChange={setDue} />}
/>
```

## Preview on hover

```jsx
<Popover trigger="hover" placement="right" dismiss="click-outside" content={previewCard} />
```

## Controlled opening and closing

```jsx
<Popover open={menuOpen} onClose={() => setMenuOpen(false)} content={rowMenu} />
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| more-menu on table rows | `aktionen`, `trigger="click"` |
| setting a date/colour quickly | `formular`, `closeOnAction` |
| link-target preview | [hover-card](../hover-card/), otherwise `inhalt` with `trigger="hover"` |
| centred confirmation dialog | [modal](../modal/) or [alert-dialog](../alert-dialog/) |
