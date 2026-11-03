# Select (Auswahlliste) - Verwendung

## Einfaches Dropdown

```jsx
<Dropdown 
  label="Land"
  value={country}
  onChange={setCountry}
  options={[
    { value: 'de', label: 'Deutschland' },
    { value: 'at', label: 'Österreich' },
    { value: 'ch', label: 'Schweiz' }
  ]}
/>
```

## Mit Suche

```jsx
<Dropdown 
  label="Benutzer"
  value={user}
  onChange={setUser}
  options={users}
  searchable={true}
  placeholder="Benutzer suchen..."
/>
```

## Multi-Select

```jsx
<Dropdown 
  label="Kategorien"
  value={categories}
  onChange={setCategories}
  options={categoryOptions}
  multiple={true}
  showTags={true}
/>
```

## In Formular

```jsx
<Form>
  <Dropdown 
    label="Status"
    value={status}
    onChange={setStatus}
    options={[
      { value: 'open', label: 'Offen' },
      { value: 'in-progress', label: 'In Bearbeitung' },
      { value: 'done', label: 'Erledigt' }
    ]}
  />
</Form>
```

## Mit Event-Handlern

```jsx
<Dropdown 
  label="Land"
  options={options}
  onSelect={(value) => console.log('Selected:', value)}
  onOpen={() => console.log('Open')}
  onClose={() => console.log('Close')}
/>
```

## Beispiele

## Beispiel 1: Länderauswahl

```
┌─────────────────────────────────────────┐
│ Land                                    │
├─────────────────────────────────────────┤
│  Deutschland ▼                          │
├─────────────────────────────────────────┤
│  Österreich                             │
│  Schweiz                                │
│  Frankreich                             │
│  Italien                                │
└─────────────────────────────────────────┘
```

## Beispiel 2: Benutzer-Auswahl

```
┌─────────────────────────────────────────┐
│ Verantwortlicher                        │
├─────────────────────────────────────────┤
│  John Doe ▼                             │
├─────────────────────────────────────────┤
│  John Doe                               │
│  Jane Smith                             │
│  Bob Müller                             │
│  Alice Winter                           │
└─────────────────────────────────────────┘
```

## Beispiel 3: Kategorien (Multi-Select)

```
┌─────────────────────────────────────────┐
│ Kategorien                              │
├─────────────────────────────────────────┤
│  [Java] [Python] [React] ▼             │
├─────────────────────────────────────────┤
│  [✓] Java                               │
│  [✓] Python                             │
│  [ ] React                              │
│  [ ] Node.js                            │
│  [ ] Angular                            │
└─────────────────────────────────────────┘
```

## Beispiel 4: Status-Auswahl

```
┌─────────────────────────────────────────┐
│ Status                                  │
├─────────────────────────────────────────┤
│  🟢 Offen ▼                             │
├─────────────────────────────────────────┤
│  🟢 Offen                               │
│  🟡 In Bearbeitung                      │
│  🟢 Erledigt                            │
│  🔴 Abgelehnt                           │
└─────────────────────────────────────────┘
```

## Beispiel 5: mit Suche

```
┌─────────────────────────────────────────┐
│ Produkt suchen...                       │
├─────────────────────────────────────────┤
│  P                                       │
├─────────────────────────────────────────┤
│  Produkt 1                              │
│  Produkt 2                              │
│  Produkt 3                              │
└─────────────────────────────────────────┘
```
