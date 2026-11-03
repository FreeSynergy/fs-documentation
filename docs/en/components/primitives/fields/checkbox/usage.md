# Checkbox - Usage

## A simple checkbox

```jsx
<Checkbox
  label="I agree"
  checked={checked}
  onChange={setChecked}
/>
```

## With an icon

```jsx
<Checkbox
  label="Important"
  checked={important}
  onChange={setImportant}
  icon="star"
/>
```

## In a form

```jsx
<Form>
  <Checkbox
    label="Subscribe to newsletter"
    checked={newsletter}
    onChange={setNewsletter}
  />
  <Checkbox
    label="Accept terms"
    checked={terms}
    onChange={setTerms}
  />
</Form>
```

## Indeterminate state

```jsx
<Checkbox
  label="Select all"
  checked={allChecked}
  indeterminate={indeterminate}
  onChange={toggleAll}
/>
```

## With event handlers

```jsx
<Checkbox
  label="Enable feature"
  checked={featureEnabled}
  onChange={(checked) => console.log('Changed:', checked)}
/>
```

## Examples

## Example 1: single checkbox

```
┌─────────────────────────────────────────┐
│ [✓] I agree                             │
└─────────────────────────────────────────┘
```

## Example 2: with an icon

```
┌─────────────────────────────────────────┐
│ [✓] Important  ⭐                       │
└─────────────────────────────────────────┘
```

## Example 3: form

```
┌─────────────────────────────────────────┐
│ [✓] Subscribe to newsletter             │
│ [✓] Accept terms                        │
│ [ ] Receive special offers              │
└─────────────────────────────────────────┘
```

## Example 4: indeterminate

```
┌─────────────────────────────────────────┐
│ [■] Select all                          │
│   [ ] Item 1                            │
│   [✓] Item 2                            │
│   [✓] Item 3                            │
└─────────────────────────────────────────┘
```

## Example 5: with icons

```
┌─────────────────────────────────────────┐
│ [✓] Important  ⭐                       │
│ [✓] Urgent     ⚠️                       │
│ [✓] Done       ✓                        │
└─────────────────────────────────────────┘
```
