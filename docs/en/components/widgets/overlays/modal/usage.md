# Modal (Modaler Dialog) - Verwendung

## Einfaches Modal

```jsx
<Modal 
  title="Bestätigung"
  isOpen={isOpen}
  onClose={() => setIsOpen(false)}
>
  <p>Möchten Sie fortfahren?</p>
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
    <Input label="Email" value={email} onChange={setEmail} />
  </form>
  <Modal.Footer>
    <Button onClick={() => setIsOpen(false)}>Abbrechen</Button>
    <Button variant="primary" onClick={saveUser}>Speichern</Button>
  </Modal.Footer>
</Modal>
```

## In App

```jsx
<App>
  <Content />
  <Modal 
    title="Info"
    isOpen={showInfo}
    onClose={() => setShowInfo(false)}
  >
    <p>Hier ist die Info...</p>
  </Modal>
</App>
```

## Mit Event-Handlern

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
│   Möchten Sie wirklich löschen?         │
│                                         │
├─────────────────────────────────────────┤
│  [Nein]               [Ja]              │
└─────────────────────────────────────────┘
```

## Beispiel 2: Formular-Modal

```
┌─────────────────────────────────────────┐
│ [✕] Benutzer bearbeiten                 │
├─────────────────────────────────────────┤
│ Name                                    │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━        │
│ Email                                   │
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
│   Diese Funktion ermöglicht...          │
│                                         │
│   Weitere Informationen...              │
│                                         │
└─────────────────────────────────────────┘
```

## Beispiel 4: Fehler-Modal

```
┌─────────────────────────────────────────┐
│ [✕] Fehler                              │
├─────────────────────────────────────────┤
│                                         │
│   Es ist ein Fehler aufgetreten.        │
│                                         │
│   Bitte versuchen Sie es später erneut. │
│                                         │
├─────────────────────────────────────────┤
│         [OK]                            │
└─────────────────────────────────────────┘
```
