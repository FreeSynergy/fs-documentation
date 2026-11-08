# Checkbox – Verwendung

## Eine einfache Checkbox

```jsx
<Checkbox
  label="I agree"
  checked={checked}
  onChange={setChecked}
/>
```

## Mit Icon

```jsx
<Checkbox
  label="Important"
  checked={important}
  onChange={setImportant}
  icon="star"
/>
```

## In einem Formular

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

## Zustand „teilweise ausgewählt“

```jsx
<Checkbox
  label="Select all"
  checked={allChecked}
  indeterminate={indeterminate}
  onChange={toggleAll}
/>
```

## Mit Ereignisbehandlern

```jsx
<Checkbox
  label="Enable feature"
  checked={featureEnabled}
  onChange={(checked) => console.log('Changed:', checked)}
/>
```

## Beispiele

## Beispiel 1: einzelne Checkbox

```
┌─────────────────────────────────────────┐
│ [✓] I agree                             │
└─────────────────────────────────────────┘
```

## Beispiel 2: mit Icon

```
┌─────────────────────────────────────────┐
│ [✓] Important  ⭐                       │
└─────────────────────────────────────────┘
```

## Beispiel 3: Formular

```
┌─────────────────────────────────────────┐
│ [✓] Subscribe to newsletter             │
│ [✓] Accept terms                        │
│ [ ] Receive special offers              │
└─────────────────────────────────────────┘
```

## Beispiel 4: teilweise ausgewählt

```
┌─────────────────────────────────────────┐
│ [■] Select all                          │
│   [ ] Item 1                            │
│   [✓] Item 2                            │
│   [✓] Item 3                            │
└─────────────────────────────────────────┘
```

## Beispiel 5: mit Icons

```
┌─────────────────────────────────────────┐
│ [✓] Important  ⭐                       │
│ [✓] Urgent     ⚠️                       │
│ [✓] Done       ✓                        │
└─────────────────────────────────────────┘
```
