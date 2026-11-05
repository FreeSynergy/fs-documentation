# Modal - Usage

## Simple modal

```jsx
<Modal 
  title="Confirmation"
  isOpen={isOpen}
  onClose={() => setIsOpen(false)}
>
  <p>Do you want to continue?</p>
  <Modal.Footer>
    <Button onClick={() => setIsOpen(false)}>Cancel</Button>
    <Button variant="primary" onClick={handleConfirm}>Confirm</Button>
  </Modal.Footer>
</Modal>
```

## With form

```jsx
<Modal 
  title="Edit user"
  isOpen={isOpen}
  onClose={() => setIsOpen(false)}
>
  <form>
    <Input label="Name" value={name} onChange={setName} />
    <Input label="Email" value={email} onChange={setEmail} />
  </form>
  <Modal.Footer>
    <Button onClick={() => setIsOpen(false)}>Cancel</Button>
    <Button variant="primary" onClick={saveUser}>Save</Button>
  </Modal.Footer>
</Modal>
```

## In an app

```jsx
<App>
  <Content />
  <Modal 
    title="Info"
    isOpen={showInfo}
    onClose={() => setShowInfo(false)}
  >
    <p>Here is the info...</p>
  </Modal>
</App>
```

## With event handlers

```jsx
<Modal 
  title="Confirmation"
  isOpen={isOpen}
  onOpen={() => console.log('Open')}
  onClose={() => console.log('Close')}
  onConfirm={() => console.log('Confirmed')}
/>
```

## Examples

## Example 1: confirmation modal

```
┌─────────────────────────────────────────┐
│ [✕] Confirmation                        │
├─────────────────────────────────────────┤
│                                         │
│   Delete this item for good?            │
│                                         │
├─────────────────────────────────────────┤
│  [No]                 [Yes]             │
└─────────────────────────────────────────┘
```

## Example 2: Form modal

```
┌─────────────────────────────────────────┐
│ [✕] Edit user                           │
├─────────────────────────────────────────┤
│ Name                                    │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━        │
│ Email                                   │
│  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━        │
│                                         │
├─────────────────────────────────────────┤
│  [Cancel]           [Save]              │
└─────────────────────────────────────────┘
```

## Example 3: Info-Modal

```
┌─────────────────────────────────────────┐
│ [✕] Info                                │
├─────────────────────────────────────────┤
│                                         │
│   This feature lets you...              │
│                                         │
│   More information...                   │
│                                         │
└─────────────────────────────────────────┘
```

## Example 4: error modal

```
┌─────────────────────────────────────────┐
│ [✕] Error                               │
├─────────────────────────────────────────┤
│                                         │
│   An error occurred.                    │
│                                         │
│   Please try again later.               │
│                                         │
├─────────────────────────────────────────┤
│         [OK]                            │
└─────────────────────────────────────────┘
```
