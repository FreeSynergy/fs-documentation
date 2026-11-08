# Modal - Verwendung

## Einfaches Modal

```jsx
<Modal 
  title="Bestätigung"
  isOpen={isOpen}
  onClose={() => setIsOpen(false)}
>
  <p>Möchtest du fortfahren?</p>
  <Modal.Footer>
    <Button onClick={() => setIsOpen(false)}>Abbrechen</Button>
    <Button variant="primary" onClick={handleConfirm}>Bestätigen</Button>
  </Modal.Footer>
</Modal>
```

## Mit Formular

```jsx
<Modal 
  title="Benutzer bearbeiten"
  isOpen={isOpen}
  onClose={() => setIsOpen(false)}
>
  <form>
    <Input label="Name" value={name} onChange={setName} />
    <Input label="E-Mail" value={email} onChange={setEmail} />
  </form>
  <Modal.Footer>
    <Button onClick={() => setIsOpen(false)}>Abbrechen</Button>
    <Button variant="primary" onClick={saveUser}>Speichern</Button>
  </Modal.Footer>
</Modal>
```

## In einer Anwendung

```jsx
<App>
  <Content />
  <Modal 
    title="Info"
    isOpen={showInfo}
    onClose={() => setShowInfo(false)}
  >
    <p>Hier sind die Infos ...</p>
  </Modal>
</App>
```

## Mit Ereignis-Handlern

```jsx
<Modal 
  title="Bestätigung"
  isOpen={isOpen}
  onOpen={() => console.log('Open')}
  onClose={() => console.log('Close')}
  onConfirm={() => console.log('Confirmed')}
/>
```

## Beispiele

## Beispiel 1: Bestätigungs-Modal

```
┌─────────────────────────────────────────┐
│ [✕] Bestätigung                         │
├─────────────────────────────────────────┤
│                                         │
│   Dieses Element endgültig löschen?     │
│                                         │
├─────────────────────────────────────────┤
│  [Nein]                 [Ja]            │
└─────────────────────────────────────────┘
```

## Beispiel 2: Formular-Modal

```
┌─────────────────────────────────────────┐
│ [✕] Benutzer bearbeiten                 │
├─────────────────────────────────────────┤
│ Name                                    │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━        │
│ E-Mail                                  │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━        │
│                                         │
├─────────────────────────────────────────┤
│  [Abbrechen]        [Speichern]         │
└─────────────────────────────────────────┘
```

## Beispiel 3: Info-Modal

```
┌─────────────────────────────────────────┐
│ [✕] Info                                │
├─────────────────────────────────────────┤
│                                         │
│   Mit dieser Funktion kannst du ...     │
│                                         │
│   Weitere Informationen ...             │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 4: Fehler-Modal

```
┌─────────────────────────────────────────┐
│ [✕] Fehler                              │
├─────────────────────────────────────────┤
│                                         │
│   Ein Fehler ist aufgetreten.           │
│                                         │
│   Bitte versuche es später erneut.      │
│                                         │
├─────────────────────────────────────────┤
│         [OK]                            │
└─────────────────────────────────────────┘
```
