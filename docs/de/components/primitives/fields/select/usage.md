# Select - Verwendung

## Ein einfaches Dropdown

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
  placeholder="Benutzer suchen…"
/>
```

## Mehrfachauswahl

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

## In einem Formular

```jsx
<Form>
  <Dropdown
    label="Status"
    value={status}
    onChange={setStatus}
    options={[
      { value: 'open', label: 'Offen' },
      { value: 'in-progress', label: 'In Arbeit' },
      { value: 'done', label: 'Erledigt' }
    ]}
  />
</Form>
```

## Mit Ereignis-Handlern

```jsx
<Dropdown
  label="Land"
  options={options}
  onSelect={(value) => console.log('Ausgewählt:', value)}
  onOpen={() => console.log('Geöffnet')}
  onClose={() => console.log('Geschlossen')}
/>
```

## Beispiele

## Beispiel 1: Land auswählen

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

## Beispiel 2: Benutzer auswählen

```
┌─────────────────────────────────────────┐
│ Zuständig                               │
├─────────────────────────────────────────┤
│  John Doe ▼                             │
├─────────────────────────────────────────┤
│  John Doe                               │
│  Jane Smith                             │
│  Bob Müller                             │
│  Alice Winter                           │
└─────────────────────────────────────────┘
```

## Beispiel 3: Kategorien (Mehrfachauswahl)

```
┌─────────────────────────────────────────┐
│ Kategorien                              │
├─────────────────────────────────────────┤
│  [Java] [Python] [React] ▼              │
├─────────────────────────────────────────┤
│  [✓] Java                               │
│  [✓] Python                             │
│  [ ] React                              │
│  [ ] Node.js                            │
│  [ ] Angular                            │
└─────────────────────────────────────────┘
```

## Beispiel 4: Status auswählen

```
┌─────────────────────────────────────────┐
│ Status                                  │
├─────────────────────────────────────────┤
│  🟢 Offen ▼                             │
├─────────────────────────────────────────┤
│  🟢 Offen                               │
│  🟡 In Arbeit                           │
│  🟢 Erledigt                            │
│  🔴 Abgelehnt                           │
└─────────────────────────────────────────┘
```

## Beispiel 5: mit Suche

```
┌─────────────────────────────────────────┐
│ Produkte suchen…                        │
├─────────────────────────────────────────┤
│  P                                      │
├─────────────────────────────────────────┤
│  Produkt 1                              │
│  Produkt 2                              │
│  Produkt 3                              │
└─────────────────────────────────────────┘
```
