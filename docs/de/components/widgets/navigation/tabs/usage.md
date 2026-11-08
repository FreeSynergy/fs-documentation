# Tabs - Verwendung

## Einfache Tabs

```jsx
<Tabs 
  tabs={[
    { id: 'tab1', label: 'Reiter 1', content: 'Inhalt 1' },
    { id: 'tab2', label: 'Reiter 2', content: 'Inhalt 2' },
    { id: 'tab3', label: 'Reiter 3', content: 'Inhalt 3' }
  ]}
  activeTab="tab1"
  onChange={(id) => setActiveTab(id)}
/>
```

## Mit Icons

```jsx
<Tabs 
  tabs={[
    { id: 'tab1', label: 'Start', icon: 'home', content: '...' },
    { id: 'tab2', label: 'Profil', icon: 'user', content: '...' },
    { id: 'tab3', label: 'Einstellungen', icon: 'settings', content: '...' }
  ]}
  showIcons={true}
/>
```

## Schließbare Reiter

```jsx
<Tabs 
  tabs={dynamicTabs}
  closable={true}
  onClose={(id) => removeTab(id)}
/>
```

## Senkrechte Reiter

```jsx
<Tabs 
  tabs={tabs}
  position="left"
  size="large"
/>
```

## In einer Karte

```jsx
<Card>
  <Tabs 
    tabs={tabs}
    variant="card"
    activeTab="tab1"
  />
</Card>
```

## Mit Ereignis-Handlern

```jsx
<Tabs 
  tabs={tabs}
  onSelect={(id) => console.log('Ausgewählt:', id)}
  onClose={(id) => console.log('Geschlossen:', id)}
/>
```

## Beispiele

## Beispiel 1: Einstellungs-Reiter

```
┌─────────────────────────────────────────┐
│ Allgemein │ Sicherheit │ Benutzer       │
├─────────────────────────────────────────┤
│                                         │
│   Einstellungen anzeigen                │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 2: Profil-Reiter

```
┌─────────────────────────────────────────┐
│ Übersicht │ Beiträge │ Fotos │ Freunde  │
├─────────────────────────────────────────┤
│                                         │
│   Profilinhalt                          │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 3: Formular-Reiter

```
┌─────────────────────────────────────────┐
│ Schritt 1 │ Schritt 2 │ Schritt 3       │
├─────────────────────────────────────────┤
│                                         │
│   Formularinhalt                        │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 4: Chat-Reiter

```
┌─────────────────────────────────────────┐
│ Chat │ Gruppen │ Anfragen │ Archiv      │
├─────────────────────────────────────────┤
│                                         │
│   Chatinhalt                            │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 5: Dokumentations-Reiter

```
┌─────────────────────────────────────────┐
│ Übersicht │ Installation │ Verwendung   │
│ API       │ Beispiel     │              │
├─────────────────────────────────────────┤
│                                         │
│   Dokumentationsinhalt                  │
│                                         │
└─────────────────────────────────────────┘
```
