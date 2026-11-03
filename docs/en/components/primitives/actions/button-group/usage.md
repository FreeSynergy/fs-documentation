# Button Group - Usage

!!! note
    The examples are kept syntax-neutral. As soon as the implementation moves to
    Rust and Blinc, the `usage.md` examples will be replaced in a separate pass.

## Two actions as one unit

```jsx
<ButtonGroup items={[saveButton, publishButton]} variant="verbund" />
```

## Switching the view (segmented control)

```jsx
<ButtonGroup
  variant="segment"
  value={viewMode}
  onSelect={setViewMode}
  items={[
    { value: "list", label: "List" },
    { value: "grid", label: "Grid" },
    { value: "timeline", label: "Timeline" }
  ]}
/>
```

## Alignment in an editor (multiple selection)

```jsx
<ButtonGroup
  variant="segment"
  selectionMode="multiple"
  value={activeAlignments}
  onSelect={setActiveAlignments}
  items={alignmentOptions}
/>
```

## Main action with a dropdown (split button)

```jsx
<ButtonGroup
  variant="split"
  items={[
    { label: "Save", onClick: save },
    { icon: "chevron-down", menu: saveAsMenu }
  ]}
/>
```

## Scenarios

| Scenario | Recommendation |
|----------|----------------|
| Editor tools (bold, italic, underline) | `segment`, `selectionMode="multiple"` |
| Dialog: Save / Save as | `split` |
| Two equal-rank actions in a form | separate buttons, no group |
| Many options (> 5) | `select` instead of a segment group |
