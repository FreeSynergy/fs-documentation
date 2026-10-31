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
