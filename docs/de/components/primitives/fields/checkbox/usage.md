# Checkbox (Ankreuzfeld) - Verwendung

## Einfache Checkbox

```jsx
<Checkbox 
  label="Einverstanden"
  checked={checked}
  onChange={setChecked}
/>
```

## Mit Icon

```jsx
<Checkbox 
  label="Wichtig"
  checked={important}
  onChange={setImportant}
  icon="star"
/>
```

## In Formular

```jsx
<Form>
  <Checkbox 
    label="Newsletter abonnieren"
    checked={newsletter}
    onChange={setNewsletter}
  />
  <Checkbox 
    label="Terms akzeptieren"
    checked={terms}
    onChange={setTerms}
  />
</Form>
```

## Indeterminate State

```jsx
<Checkbox 
  label="Alle auswählen"
  checked={allChecked}
  indeterminate={indeterminate}
  onChange={toggleAll}
/>
```

## Mit Event-Handlern

```jsx
<Checkbox 
  label="Feature aktivieren"
  checked={featureEnabled}
  onChange={(checked) => console.log('Changed:', checked)}
/>
```

## Beispiele

## Beispiel 1: Einzelne Checkbox

```
┌─────────────────────────────────────────┐
│ [✓] Einverstanden                       │
└─────────────────────────────────────────┘
```

## Beispiel 2: Mit Icon

```
┌─────────────────────────────────────────┐
│ [✓] Wichtig   ⭐                        │
└─────────────────────────────────────────┘
```

## Beispiel 3: Formular

```
┌─────────────────────────────────────────┐
│ [✓] Newsletter abonnieren               │
│ [✓] Terms akzeptieren                   │
│ [ ] Sonderangebote erhalten             │
└─────────────────────────────────────────┘
```

## Beispiel 4: Indeterminate

```
┌─────────────────────────────────────────┐
│ [■] Alle auswählen                      │
│   [ ] Element 1                         │
│   [✓] Element 2                         │
│   [✓] Element 3                         │
└─────────────────────────────────────────┘
```

## Beispiel 5: mit Icons

```
┌─────────────────────────────────────────┐
│ [✓] Wichtig   ⭐                        │
│ [✓] Dringend  ⚠️                        │
│ [✓] Erledigt  ✓                         │
└─────────────────────────────────────────┘
```
